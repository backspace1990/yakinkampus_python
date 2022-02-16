import requests
from PIL import Image
from io import BytesIO


graph_url = 'https://image-charts.com/chart'

payload = {
    'cht': 'p3',
    'chs': '900x900',
    'chd': 't:50,50',
    'chl': 'Selam|Nasilsin',
    'chan': None,
    'chf': 'ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1'
}

response = requests.post(graph_url, data=payload)
print(response.status_code)
print(response.content)
print(type(response.content))
print(100 * "*", '\n', 'OPENING IMAGE', '\n', 100 * '*')

image = Image.open(BytesIO(response.content))
image.show()

# Radar chart

graph_url2 = 'https://image-charts.com/chart'

payload2 = {
    'chco': '3092de',
    'chd': 't:81,65,50,67,59,81,81',
    'chdl': 'Falcao',
    'chdlp': 'b',
    'chs': '900x900',
    'cht': 'r',
    'chtt': 'football player traits',
    'chl': 'pace|shooting|passing|dribbling|defending|physical',
    'chxl': '0:|0|20|40|60|80|100',
    'chxt': 'x',
    'chxr': '0,0.0,100.0',
    'chm': 'B,AAAAAABB,0,0,0'
}

response2 = requests.post(graph_url, data=payload2)
print(response2.status_code)
print(response2.content)
print(type(response2.content))
print(100 * "*", '\n', 'OPENING IMAGES', '\n', 100 * '*')

image2 = Image.open(BytesIO(response2.content))

image2.show()
