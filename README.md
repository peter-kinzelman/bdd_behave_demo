# BDD behave demo

Example python BDD project using behave for [JPL Solar System Dynamics for NASA](https://ssd.jpl.nasa.gov/) api and [Yahoo Finance](https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-tre-srch) api

Requires `python >= 2.6`

```shell
git clone https://github.com/OptimumPartners/bdd_behave_demo.git
cd python-bdd-behave
pip install -r requirements.txt
```

## running tests
``` shell
behave # run all feature files
behave features/ # run all feature files in the given folder
behave features/search.feature # run the search.feature file only
```
