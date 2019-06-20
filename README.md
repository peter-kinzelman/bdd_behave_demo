[![Build Status](https://img.shields.io/badge/chrome-75.0-brightgreen.svg?style=flat)](https://github.com/rubocop-hq/ruby-style-guide)

# BDD behave demo

Example python BDD project using behave for [JPL Solar System Dynamics for NASA](https://ssd.jpl.nasa.gov/) api and [Yahoo Finance](https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-tre-srch) api

Requires `python >= 2.6`

Requires `chrome = 75.0.3770.90`

```shell
git clone https://github.com/OptimumPartners/bdd_behave_demo.git
cd bdd_behave_demo
pip install -r requirements.txt
```

## Running Tests
``` shell
behave # run all feature files
behave features/ # run all feature files in the given folder
behave features/search.feature # run the search.feature file only
```
## General Features:
  1. Used a JSON file that contains URLs and Paths.
  2. Used a seperate file for each web page that pulls web elements.
  3. Verifies that required API Data is present, common patterns like Url patterns and evaluates the data types ..etc.
  4. Collect all errors before assertion, so that all errors will detected.
  5. Verify that the API data matches the displayed UI data.
  6. Used variables in each step for different calls, response codes, ...etc.

## Future Features:
  1. Execute multiple tests simultaneusly using threading.
  2. Export test results as html/stat files.
  3. Jira integration.
  4. Add support for browsers other than Chrome and support for cloud browsers.
  5. Save execution results in database to create a history report.
  6. Predefine weights and severity for scenarios.
  7. Capture screenshots on failures.
