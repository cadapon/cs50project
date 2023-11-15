import requests
import config


class WhoIsJSON:
    def __init__(self):
        # Configures API key
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
        jsonResponse = response.json()
        return jsonResponse
        # if jsonResponse["registered"]:
        #     return f"Sorry, {domain} is already registered!"
        # else:
        #     return f"{domain} is available for registration!"


def testapi():
    whoisjson = WhoIsJSON()
    print(whoisjson.whois("charlesadapon.org"))


if __name__ == "__main__":
    testapi()
