import ip2locationio
import config


class IP2WhoIs:
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


def testapi():
    ip2whois = IP2WHOIS()
    ip2whois.lookup("example.com")


if __name__ == "__main__":
    testapi()
