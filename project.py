import whoisjson
import re
import argparse
import csv
import sys


def start_parse():
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
    if csv_file is not None and not csv_file.lower().endswith(("csv")):
        sys.stderr.write("Must be a .csv file")
        sys.exit(1)
    else:
        return csv_file


def get_input():
    domains = input("Enter the domains to search, separated by a comma: ").split(", ")
    return domains


def validate_domain(domains):
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    p = re.compile(regex)
    domain_list = []
    for domain in domains:
        if domain == None:
            print("Domain name cannot by empty!")
        if re.search(p, domain):
            domain_list.append(domain)
        else:
            print(
                "Not a valid domain. The spaces and the following characters are not allowed: .! @ # $ % ^ & * ( ) ; : , ? / '\ ' = + < >"
            )
            sys.exit(1)
    return domain_list


def domain_lookup(domains):
    # Makes API call to WHOISJSON
    lookup = whoisjson.WhoIsJSON()
    for domain in domains:
        response = lookup.whois(domain.strip())
        # Return domain registration status
        try:
            if response["registered"]:
                return f"Sorry, {response['name']} is already registered!"
            if response["registered"] == False:
                return f"{response['name']} is available for registration!"
        except KeyError:
            # If API cannot lookup domain, return status message
            return response


def read_csv(file):
    with open(file, mode="r", encoding="utf-8-sig") as f:
        csvFile = csv.reader(f)
        for domain in csvFile:
            domains = validate_domain(domain)
            print(domain_lookup(domains))


def main():
    print(domain_lookup(["yahoo.com"]))
    # csv_file = start_parse()
    # if csv_file is not None:
    #     read_csv(csv_file)
    # else:
    #     answer = get_input()
    #     domains = validate_domain(answer)
    #     print(domain_lookup(domains))


if __name__ == "__main__":
    main()
