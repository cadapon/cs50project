import requests
import ip2locationio
import config


class IP2WHOIS:
    def __init__(self):
        # Configures IP2WHOIS API key
        self.config = configuration = ip2locationio.Configuration(
            config.ip2locationiotoken
        )
        self.domainwhois = ip2locationio.DomainWHOIS(configuration)

    def lookup(self, domain):
        # Lookup domain information
        results = self.domainwhois.lookup(domain)
        return results

    def extension(self, domain):
        # Get domain extension (gTLD or ccTLD) from URL or domain name
        result = self.ip2whois_init.getDomainExtension(domain)
        return result


class WHOISJSON:
    def __init__(self):
        # Configures IP2WHOIS API key
        self.baseurl = "https://whoisjson.com/api/v1"
        self.token = config.whoisjsontoken

    def whois(self, domain):
        # Lookup domain information
        params = {"domain": domain}
        response = requests.get(
            self.baseurl + "/whois",
            headers={"Authorization": self.token},
            params=params,
        )
        return response.json()


def main():
    domain = str(input("Domain to lookup: "))
    # ip2whois = IP2WHOIS()
    # print(ip2whois.lookup(domain))
    whoisjson = WHOISJSON()
    response = whoisjson.whois(domain)
    print(response["contacts"])
    # print(whoisjson.whois(domain))


if __name__ == "__main__":
    main()
