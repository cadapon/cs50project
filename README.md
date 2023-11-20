# CS50P Final - Domain Availability Tool

#### Video Demo

 <URL HERE>

#### Description

The Domain Availability Tool performs a WHOIS lookup on a given domain(s) and returns whether domain can be registered. Domains can be passed in by either user input or as command-line agrument. The tool leverages the [whoisjson.com](https://whoisjson.com/whois-api) REST API.

#### Usage

1. Install requirements.txt file:

```
pip install -r reuqirements.txt
```

2. Execute in interactive mode:

```
python project.py
```

Or by providing a csv file at the command-line:

```
python project.py -f <Path to csv file>
```

#### Project Files

The following files have been essential to the development of this tool. A brief explanation of the files are as follows:

- project.py: main file
- apitesting.py: test file for whoisjson API to be added to whoisjson.py
- whoisjson.py: class file for whoisjson API
- config.py: API token and other secrets not uploaded to public Git repo
- domains_test.csv: test csv file for demo purposes
- requirements.txt: required modules
- test_func.py: test file that would be later used in pytest file 'testing_project.py'

### Design Considerations and Learnings

When first designing the tool, the main outcome was to tell the user whether a domain was registered or not. I realized shortly after that I would need to consider the user's experience using the tool. If a user needed multiple domains to be checked, it would be easier for them to "upload" a file for the program rather than having to run the program for each domain.

If I had more time to work on this program, a better outcome would be to include support for Punycode (emoji) domain names. The ip2whois library is capable of parsing Punycode and other international domain names/characters. An even better outcome would also feature an option to take a user to a domain registrar landing page to complete a purchase of a domain. In addition, the whoisjson API is a free tier service so I would like to include logging API calls in the event that the program reaches the rate limit, as well as general logging.

The project helped me understand how important planning is during development. Had I spent more time breaking down the main issue into parts, a I would have caught more issues upfront, than spend more time refactoring code as I code. One instance was when I initially created functions that took in a list as an argument. When I was testing the APIs, I was passing a single domain into the GET request, as per the API document. I found myself having to perform For Loops in all my subsequent functions. Another hard lesson learned was unit testing for argparse. I spent a few hours reading through stackoverflow and articles and was able to piece together other use-cases with mine to suit my testing needs. While on the subject of stackoverflow research, I found several great regex patterns that I used for input validation. Although their documentation did not explicity state their API offers their own domain validation which can parse subdomains. In hindsight, I probably could have removed the regex pattern and let the API handle that workload, but I wanted to practice the coursework. Lastly, I decided to store my code in my personal Github account. This was to help me become more familiar with Git operations for my day to day workflow and use the Github Project tool. It acted like a JIRA tracker for my issues, features, to-do's, etc. Another thing to note about Github, I realized that I was exposing my API token in the code. It was a great opportunity and a practical use-case for me to research how to secure secrets using the .gitignore file!
