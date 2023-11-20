import requests
import config
import sys


class WhoIsJSON:
    def __init__(self):
        # Configures API key
        self.baseurl = "https://whoisjson.com/api/v1"
        self.token = config.whoisjsontoken

    def whois(self, domain):
        # Lookup domain information
        params = {"domain": domain}
        try:
            response = requests.get(
                self.baseurl + "/whois",
                headers={"Authorization": self.token},
                params=params,
            )
            response.raise_for_status()
            jsonResponse = response.json()
            return jsonResponse
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
            sys.exit(1)
        except requests.exceptions.ReadTimeout as errrt:
            print("Time out")
            sys.exit(1)
        except requests.exceptions.ConnectionError as conerr:
            print("Connection error")
            sys.exit(1)
        except requests.exceptions.RequestException as errex:
            print("Exception request")
            sys.exit(1)


def testapi():
    whoisjson = WhoIsJSON()
    print(whoisjson.whois("charlesadapon.org"))


if __name__ == "__main__":
    testapi()
