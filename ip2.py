import ip2locationio

# Configures IP2Location.io API key
configuration = ip2locationio.Configuration("96042FD29611374AF4B811F0C4D5CB1E")
domainwhois = ip2locationio.DomainWHOIS(configuration)

# Lookup domain information
# print(domainwhois.lookup("yahoo.com"))
print(domainwhois.getdomainextension("example.com"))
print(domainwhois.lookup("google.com"))
