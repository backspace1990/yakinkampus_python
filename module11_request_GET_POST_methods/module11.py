import requests
from collections import Counter

# url_adress = "https://data.police.uk/api/forces"

# print(requests.get(url_adress))

# for i in requests.get(url_adress).json():
#    print(i)

# result_respons = requests.get(url_adress)
# if result_respons.status_code == 200:
#    # print(result_respons.json())
#    for i in result_respons.json():
#        print(i)
# else:
#    print(f"result_respons.status_code != 200 status code : {result_respons.status_code}")


# https://data.police.uk/api/crime-categories?date=2011-08
categories_of_crimes_url = "https://data.police.uk/api/crime-categories"
payload = {'date': '2020-06'}
response2 = requests.get(categories_of_crimes_url, params=payload)
print(response2.status_code)
print(response2.url)
print(50 * "*")
# for i in response2.json():
# print(i)

# https://data.police.uk/api/crimes-no-location?category=all-crime&force=leicestershire&date=2017-03

crimed_url = "https://data.police.uk/api/crimes-no-location"
# ?category=all-crime&force=leicestershire&date=2017-03

payload = {
    'category': 'all-crime',
    'force': 'city-of-london',
    'date': '2021-12'
}

response3 = requests.get(crimed_url, params=payload)
# print(response3.json())
for i in response3.json():
    print(i)

print(50 * "*")


# Application

class crimed_raptors:
    def __init__(self, location, date, crimed_type='all-crime'):
        self.location = location
        self.date = date
        self.crimed_type = crimed_type
        self.find_crimes = self.find_crimes()

    def find_crimes(self):
        crimed_urls = "https://data.police.uk/api/crimes-no-location"

        payloads = {
            'category': self.crimed_type,
            'force': self.location,
            'date': self.date}
        response5 = requests.get(crimed_urls, params=payloads)

        if response5.status_code == 200:
            return response5.json()
        else:
            return None

    def send_data_crime(self):
        crimed_lists = []

        if self.find_crimes is not None:
            for crime in self.find_crimes:
                crimed_lists.append(crime['category'])

            return Counter(crimed_lists)


crime_rap = crimed_raptors('city-of-london', '2021-12', 'all-crime')
# for i in crime_rap.find_crimes:
#     print(i)

print(50 * '*')

print(crime_rap.send_data_crime())
