import requests
import ip2whois


WHOISJSON = "a44628d14be119fdd207fc8fdd6e417effe265577594bdda7ba58bb5fa6e5386"
WHOISJSONBASEURL = "https://whoisjson.com/api/v1"
DOMAIN = "charlesadapon.com"


class IP2:
    def __init__(self):
        # Configures IP2WHOIS API key
        IP2WHOIS = "96042FD29611374AF4B811F0C4D5CB1E"
        self.ip2whois_init = ip2whois.Api(IP2WHOIS)

    def lookup(self, domain):
        # Lookup domain information
        results = self.ip2whois_init.lookup(domain)
        return results

    def extension(self, domain):
        # Get domain extension (gTLD or ccTLD) from URL or domain name
        result = self.ip2whois_init.getDomainExtension(domain)
        return result


class WHOISJSON:
    def __init__(self):
        # Configures IP2WHOIS API key
        IP2WHOISKEY = "96042FD29611374AF4B811F0C4D5CB1E"
        self.ip2whois_init = ip2whois.Api(WHOISJSON)

    def lookup(self, domain):
        # Lookup domain information
        results = self.ip2whois_init.lookup(domain)
        return results


def main():
    domain = str(input("Domain to lookup: "))
    ip2whois = IP2()
    print(ip2whois.lookup(domain))


if __name__ == "__main__":
    main()
