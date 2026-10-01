# OpenAlex Source Cache

This directory stores raw OpenAlex records retrieved for AISO source-level discovery.

Each source is retrieved once and cached locally before geographic matching and screening.

## Purpose

The cache:

- preserves the raw records used in discovery;
- prevents unnecessary repeated OpenAlex API requests;
- separates data acquisition from AISO matching and screening logic;
- allows geographic dictionaries and matching procedures to be revised without redownloading source records;
- improves reproducibility of corpus construction.

## Data rule

Files in this directory are raw source snapshots.

They should not be manually edited.

Derived candidate records belong in downstream discovery or processed-data directories.

## Coverage

Initial S1 coverage:

- 11 premier Information Systems journals
- publication years 2000–2026
- source metadata retrieved through OpenAlex
