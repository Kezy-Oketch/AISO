import csv
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path


GEOGRAPHY_FILE = Path(
    "data/reference/AISO_Geography_Dictionary_v0.1.csv"
)

OUTPUT_FILE = Path(
    "data/raw/pilot_discovery/openalex_misq_country_pilot.jsonl"
)

SOURCE_NAME = "MIS Quarterly"
SOURCE_ID = "S57293258"

START_YEAR = 2000
END_YEAR = 2026


def load_countries():
    """Load canonical AISO country names."""
    with GEOGRAPHY_FILE.open("r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return [row["country_name"] for row in reader]


def reconstruct_abstract(inverted_index):
    """Reconstruct an abstract from OpenAlex's inverted index."""
    if not inverted_index:
        return ""

    positions = []

    for word, indexes in inverted_index.items():
        for index in indexes:
            positions.append((index, word))

    positions.sort()

    return " ".join(word for _, word in positions)


def retrieve_source_works():
    """
    Retrieve all MIS Quarterly works within the AISO coverage period.

    Geography is NOT used in the OpenAlex query. Geographic matching
    occurs locally against explicit bibliographic fields.
    """
    cursor = "*"
    works = []

    while cursor:

        params = {
            "filter": (
                f"primary_location.source.id:{SOURCE_ID},"
                f"from_publication_date:{START_YEAR}-01-01,"
                f"to_publication_date:{END_YEAR}-12-31"
            ),
            "per-page": 100,
            "cursor": cursor,
        }

        url = (
            "https://api.openalex.org/works?"
            + urllib.parse.urlencode(params)
        )

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent":
                    "AISO/0.1 (African Information Systems Observatory)"
            },
        )

        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode("utf-8"))

        works.extend(data.get("results", []))

        cursor = data.get("meta", {}).get("next_cursor")

        if not data.get("results"):
            break

        time.sleep(0.2)

    return works


def searchable_text(work):
    """
    Construct the explicit text fields used for geographic matching.

    Included:
      - title
      - abstract
      - author keywords

    OpenAlex topics and generic search relevance signals are excluded.
    """
    title = work.get("title") or ""

    abstract = reconstruct_abstract(
        work.get("abstract_inverted_index")
    )

    keywords = " ".join(
        keyword.get("display_name", "")
        for keyword in (work.get("keywords") or [])
    )

    return f"{title} {abstract} {keywords}".lower()


def match_country(work, country):
    """Return True when country appears in controlled searchable fields."""
    return country.lower() in searchable_text(work)


def main():

    # Kenya only for validation.
    countries = ["Kenya"]

    print("=" * 65)
    print("AISO OpenAlex Controlled Geography Pilot")
    print(f"Source: {SOURCE_NAME} ({SOURCE_ID})")
    print(f"Years: {START_YEAR}-{END_YEAR}")
    print("=" * 65)

    print("\nRetrieving source corpus...")

    works = retrieve_source_works()

    print(f"MISQ works retrieved: {len(works)}")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as outfile:

        for country in countries:

            matches = [
                work
                for work in works
                if match_country(work, country)
            ]

            print(f"\nCountry: {country}")
            print(f"Controlled matches: {len(matches)}")

            for i, work in enumerate(matches, 1):
                print(
                    f"  {i}. {work.get('title')} "
                    f"({work.get('publication_year')})"
                )

            record = {
                "search_country": country,
                "source_target": SOURCE_NAME,
                "source_id": SOURCE_ID,
                "coverage_start": START_YEAR,
                "coverage_end": END_YEAR,
                "matching_fields": [
                    "title",
                    "abstract",
                    "author_keywords",
                ],
                "results_count": len(matches),
                "results": matches,
            }

            outfile.write(
                json.dumps(record, ensure_ascii=False) + "\n"
            )

    print("\n" + "=" * 65)
    print("Controlled geography pilot complete.")
    print(f"Output: {OUTPUT_FILE}")
    print("=" * 65)


if __name__ == "__main__":
    main()
