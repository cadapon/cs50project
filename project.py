import whoisjson
import re
import argparse


def start_parse():
    parser = argparse.ArgumentParser(
        description="Check if domain is available for purchase"
    )
    parser.add_argument(
        "-f", "--file", type=str, required=False, help="Path to csv file"
    )
    args = parser.parse_args()


def get_input():
    # Get user input on domains to search
    domains = input("Enter the domains to search, separated by a comma: ").split(", ")
    return domains


def validate_domain(domains):
    # Taken from https://www.geeksforgeeks.org/how-to-validate-a-domain-name-using-regular-expression/
    # Regex to check valid domain name.
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    # Compile the ReGex
    p = re.compile(regex)
    domain_list = []
    for domain in domains:
        # If the string is empty
        # return false
        if domain == None:
            print("Domain name cannot by empty!")
        # Return if the string
        # matched the ReGex
        if re.search(p, domain):
            domain_list.append(domain)
        else:
            print(
                "Not a valid domain. The spaces and the following characters are not allowed: .! @ # $ % ^ & * ( ) ; : , ? / \ = + < >"
            )
            pass
    return domain_list


def domain_lookup(domains):
    # Makes API call to WHOISJSON
    lookup = whoisjson.WhoIsJSON()
    try:
        for domain in domains:
            response = lookup.whois(domain.strip())
            print(parse_lookup(response))

    except:
        print("Error attempting to make API call!")


def parse_lookup(response):
    # Return if domain is available for registration
    if response["registered"]:
        return f"Sorry, {response['name']} is already registered!"
    if response["registered"] == False:
        return f"{response['name']} is available for registration!"
    else:
        # If API cannot lookup domain, return status message
        return response


def main():
    start_parse()
    answer = get_input()
    domains = validate_domain(answer)
    domain_lookup(domains)


if __name__ == "__main__":
    main()
