CS50P Final
Domain Availability Tool

#### Video Demo: <URL HERE>

#### Description: What will your software do? What features will it have? How will it be executed?

TODO:

Project Files

- project.py: main file
- apitesting.py: test file for whoisjson API to be added to whoisjson.py
- whoisjson.py: class file for whoisjson API
- config.py: API token and other secrets not uploaded to public Git repo
- domains_test.csv: test csv file for demo purposes
- requirements.txt: required modules
- test_func.py: test file that would be later used in pytest file 'testing_project.py'

Design Considerations

- What might you consider to be a good outcome for your project? A better outcome? The best outcome?
  Good outcome: Tool can successfully return whether a domain is available
  Better outcome: Good outcome with ability to search with Punycode (emoji) domains
  - ip2whois handles puny code
    Best outcome:
  - Better outcome with the ability to return a link for users to register an available domain
  - Logging for API calls and domain results

What new skills will you need to acquire? What topics will you need to research? Any learnings?
-API doc

- rate limiting
- leveraged features for tld checking and subdomain checking. Documentation did not mention. Had to test to find out
- requests library
  - exception handling
- argparse and pytest
  - stackoverflow for unit testing
- function refactoring/iterative decomposition
  - passing list of domains into functions created required For Loops. Better to pass in one domain into function for better troubleshooting and consistency
- referred to stackoverlfow for regex in domain tld validation
- GitHub
  - .gitignore
  - Git basics
