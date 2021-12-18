from ip2geotools.databases.noncommercial import DbIpCity

def location():
    response = DbIpCity.get('122.177.76.214', api_key='free')
    # print(response.ip_address)
    # print(response.latitude)
    # print(response.longitude)
    print(response.city)
    print(response.region)
    print(response.country)