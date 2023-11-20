import whoisjson
import re
import argparse
import csv
import sys


def start_parse(arg):
    # Creates cmd-line option for csv input
    parser = argparse.ArgumentParser(
        description="Check if domain is available for purchase"
    )
    parser.add_argument(
        "-f",
        "--file",
        required=False,
        help="Path to csv file",
    )
    args = parser.parse_args()
    csv_file = args.file
    return csv_file


def get_input():
    domains = input("Enter the domains to search, separated by a comma: ").split(", ")
    return domains


def validate_domain(domain):
    # Performs regex validation and generates a list of domains
    regex = "^((?!-\s)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    p = re.compile(regex)
    # domain_list = []
    # for domain in domains:
    if domain == None:
        print("Domain name cannot by empty!")
    if re.search(p, domain):
        return domain
    else:
        print(
            f"'{domain}' is not a valid domain. Ensure that domains are separated by a space and comma.The following characters are not allowed: .! @ # $ % ^ & * ( ) ; : , ? / '\ ' = + < >"
        )
        sys.exit(1)
    # return domain_list


def domain_lookup(domain):
    # Makes API call to WHOISJSON
    lookup = whoisjson.WhoIsJSON()

    # for domain in domains:
    response = lookup.whois(domain.strip())
    # Return domain registration status
    try:
        # print(f"{domain} from csv lookup inside try")
        if response["registered"]:
            return f"Sorry, {response['name']} is already registered! \nContact info as follows:\n {response['contacts']}"
        if response["registered"] == False:
            return f"{response['name']} is available for registration!"
    except KeyError:
        # If API cannot lookup domain, return status message
        return response


def read_csv(file):
    # Read csv file and executes downstream functions
    with open(file, mode="r", encoding="utf-8-sig") as f:
        csvFile = csv.reader(f)
        for line in csvFile:
            for domain in line:
                valid_domain = validate_domain(domain)
                print(domain_lookup(valid_domain))


def main():
    csv_file = start_parse(sys.argv[1:])
    try:
        if csv_file is not None and not csv_file.lower().endswith(("csv")):
            print(f"File {csv_file} is not a .csv file!")
        # Check for file as input
        elif csv_file is not None and csv_file.lower().endswith(("csv")):
            read_csv(csv_file)
        else:
            # Fall back to user input if no file provided
            answer = get_input()
            for domain in answer:
                valid_domain = validate_domain(domain)
                print(domain_lookup(valid_domain))
    except FileNotFoundError:
        print(f"File {csv_file} not found!", file=sys.stderr)


if __name__ == "__main__":
    main()
