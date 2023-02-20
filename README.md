# About Insure.com 
Insure.com offers you the most comprehensive information on your insurance choices, along with tools and resources so you have the knowledge needed to make the best financial decisions for your situation.

# Testing Insure.com
This repository is made with the purpose of testing insure.com website's functional flows.

**Note:** This repository was created in a constrained amount of time for informative purposes only; it does not cover all functional flows.

**Test URL:** http://d3j8nuwp74eyml.cloudfront.net/5U5PU/S2xbn  
**Test Framework:** Playwright + PyTest (Python)\
**Test Coverage:** 20%\
**Browser:** Chromium\
**Functional scenario:** Perform validation of GUI by performing end-to-end flow for adding user's insurance

# Installing Playwright:

To function, each Playwright version requires a certain set of browser binaries.
Playwright automatically downloads Firefox, WebKit, and Chromium browsers.

```
$ pip install playwright
$ playwright install
$ pip install -r requirements.txt
```

# Running playwright tests
```
$ pytest test_name.py
```

For successfully running _test_functional.py_ , follow below steps after installing playwright & required modules:
```
$ git clone https://github.com/SAPadhiar/playwright_pytest.git
$ cd playwright_pytest
$ pytest -vs tests/test_functional.py
```
