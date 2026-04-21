# Qual AI A/B Test

This repository contains an A/B test for a website change made as part of my broader qualitative research workflow.

The experiment is based on the main research product in [`custom-gpt-interview-research`](/Users/bapbap23/Desktop/custom-gpt-interview-research), which is a qualitative AI interview platform for running studies, managing interview materials, and analyzing research outputs. This repo is a focused analysis workspace for testing whether a navigation change improves how people move through that experience.

## Project Purpose

The goal of this project is to evaluate a website design change and understand whether it improves the user journey.

Instead of making the update based only on instinct, this project treats the design decision as a measurable experiment:

- define the change
- compare the original and updated experiences
- measure task completion and navigation behavior
- determine whether the new design reduces friction

## Change Being Tested

This test compares two navigation variants in the product:

- `vertical`
- `horizontal`

The working assumption in this dataset is that the updated experience changes the site's navigation pattern in order to make movement through the workflow clearer and more intuitive.

The reason for making this change was to improve usability across a multi-step research application where users move between pages such as sign-in, study selection, workflow steps, and task completion. A navigation update was worth testing because it could affect:

- how quickly users understand where to go next
- how often users backtrack
- whether they complete tasks in order
- whether they reach the end of the workflow successfully

## Research Context

This repository is intentionally separate from the main application repo.

The main repo contains the product itself, while this repo is for the experiment and analysis around one specific design decision. Keeping the A/B test isolated makes it easier to:

- work with experiment data independently
- analyze outcomes in notebooks
- load results into Postgres
- document the reasoning behind the UI change

## Data

The main dataset in this repo is:

- [`navigation_ab_test.csv`](/Users/bapbap23/Desktop/qual_ai_ab_test/navigation_ab_test.csv)

The event data includes fields related to:

- assigned variant
- event type
- page and target page
- workflow stage
- task success
- time since session start
- click order and workflow order
- backtracking behavior
- end-of-workflow completion

This makes it possible to compare not just raw completion counts, but also behavioral patterns that help explain why one version performs better than the other.

## Analysis Questions

This project is designed to answer questions like:

- Does the new navigation improve task completion?
- Do users move through the workflow with less backtracking?
- Do users complete the workflow in order more often?
- Does the updated design reduce friction at key navigation points?
- Is the change strong enough to justify rolling it into the main product?

## Environment

This workspace includes a local Python environment and notebook support for analysis in Cursor.

Important files:

- [`requirements.txt`](/Users/bapbap23/Desktop/qual_ai_ab_test/requirements.txt)
- [`.env`](/Users/bapbap23/Desktop/qual_ai_ab_test/.env)
- [`analysis.ipynb`](/Users/bapbap23/Desktop/qual_ai_ab_test/analysis.ipynb)
- [`testing.ipynb`](/Users/bapbap23/Desktop/qual_ai_ab_test/testing.ipynb)

## Local Setup

Activate the virtual environment:

```bash
cd /Users/bapbap23/Desktop/qual_ai_ab_test
source .venv/bin/activate
```

Install dependencies if needed:

```bash
pip install -r requirements.txt
```

Open the notebooks in Cursor and select the kernel:

```text
Python (.venv) qual_ai_ab_test
```

## Postgres Loading

This repo also includes environment variables for loading the CSV into Postgres.

Current database-related variables live in:

- [`.env`](/Users/bapbap23/Desktop/qual_ai_ab_test/.env)

These include:

- `POSTGRES_HOST`
- `POSTGRES_PORT`
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_SCHEMA`
- `POSTGRES_TABLE`
- `POSTGRES_SSLMODE`

## Repository Structure

```text
qual_ai_ab_test/
├── analysis.ipynb
├── testing.ipynb
├── navigation_ab_test.csv
├── requirements.txt
├── .env
└── .venv/
```

## Notes

- This project supports research and product decision-making for the main qualitative AI interview platform.
- The test focuses on whether a website navigation change creates a better user experience.
- The final outcome of this repo should help justify whether the design change should be kept, revised, or rolled back.
