import requests
from PIL import Image
from io import BytesIO


class futbol_player:
    def __init__(self, name, pace, shoot, pas, dribbl, defend, physic):
        self.name = name
        self.pace = pace
        self.shoot = shoot
        self.pas = pas
        self.dribbl = dribbl
        self.defend = defend
        self.physic = physic

    def coming_traits(self):
        return ','.join([
            str(self.pace),
            str(self.shoot),
            str(self.pas),
            str(self.dribbl),
            str(self.defend),
            str(self.physic),
            str(self.pace)
        ])

    def traits_fut_plyr(self):
        graph_url = 'https://image-charts.com/chart'

        payload = {
            'chco': '3092de',
            'chd': 't:' + self.coming_traits(),
            'chdl': self.name,
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
        response = requests.post(graph_url, data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()

    def compared_to_talent(self, second_fut_plyr):
        graph_url = 'https://image-charts.com/chart'

        payload = {
            'chco': '3092de,027182',
            'chd': 't:' + self.coming_traits() + '|' + second_fut_plyr.coming_traits(),
            'chdl': self.name + '|' + second_fut_plyr.name,
            'chdlp': 'b',
            'chs': '900x900',
            'cht': 'r',
            'chtt': 'football player traits',
            'chl': 'pace|shooting|passing|dribbling|defending|physical',
            'chxl': '0:|0|20|40|60|80|100',
            'chxt': 'x',
            'chxr': '0,0.0,100.0',
            'chm': 'B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0'
        }
        response = requests.post(graph_url, data=payload)

        image = Image.open(BytesIO(response.content))
        image.show()


messi = futbol_player('Messi', 85, 92, 91, 95, 38, 65)
ronaldo = futbol_player('Ronaldo', 89, 93, 81, 89, 35, 77)

# messi.traits_fut_plyr()

ronaldo.compared_to_talent(messi)
