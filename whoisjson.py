import requests
import config


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


def testapi():
    whoisjson = WHOISJSON()
    whoisjson.whois("example.com")


if __name__ == "__main__":
    testapi()
