from project_lib import controller as con, view
import osmnx as ox


workers=[]
users=[]

class Bank:
    def __init__(self, name:str, town:str, street:str, build_numb:int, logo:str):
        self.name = name
        self.town = town
        self.street = street
        self.build_numb = build_numb
        self.logo = logo
        self.coords =self.get_coords()

    def get_coords(self):
        place = f"{self.street} {self.build_numb}, {self.town}, Poland"
        lat, lon = ox.geocode(place)
        return lat, lon



banks=[
    Bank("PKO Bank Polski", "Wieluń", "Wojska Polskiego", 12, "pko.png"),
    Bank("ING Bank Śląski", "Kraków", "Długa", 5, "ing.png"),
    Bank("Narodowy Bank Polski", "Warszawa", "Świętokrzyska", 11, "nbp.png"),
    Bank("Santander Bank Polska", "Wrocław", "Rynek", 9, "santander.png"),
    Bank("mBank", "Łódź", "Piotrkowska", 87, "mbank.png"),
    Bank("Alior Bank", "Gdańsk", "Długa", 13, "alior.png"),
    Bank("Bank Millennium", "Poznań", "Półwiejska", 32, "millennium.png"),
    Bank("Credit Agricole", "Opole", "Ozimska", 19, "ca.png"),
    Bank("BNP Paribas", "Katowice", "3 Maja", 10, "bnp.png"),
    Bank("Citi Handlowy", "Szczecin", "Aleja Niepodległości", 22, "citi.png")
]
class Worker:
    def __init__(self, name:str, surname:str, bank:str, role:str, town:str, street:str, home_number:int, img:str):
        self.name = name
        self.surname = surname
        self.bank = bank
        self.role = role
        self.town = town
        self.street = street
        self.home_number = home_number
        self.img = img


    def get_coords(self):
        from bs4 import BeautifulSoup
        import requests
        url: str = f'https://pl.wikipedia.org/wiki/{self.town}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        # print(response.text)
        response_html = BeautifulSoup(response.text, "html.parser")
        # print(response_html.prettify())

        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        return ([latitude, longitude])