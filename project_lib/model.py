from project_lib import controller as con, view
import osmnx as ox


users=[]

class Bank:
    def __init__(self, id:int, name:str, town:str, street:str, build_numb:int, logo:str):
        self.id = id
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



banks = [
    Bank(1, "PKO Bank Polski", "Warszawa", "Marszałkowska", 12, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(2, "ING Bank Śląski", "Kraków", "Długa", 5, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(3, "Santander Bank Polska", "Wrocław", "Rynek", 9, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(4, "mBank", "Łódź", "Piotrkowska", 87, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(5, "Alior Bank", "Gdańsk", "Długa", 13, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(6, "Millennium Bank", "Poznań", "Półwiejska", 32, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(7, "BNP Paribas", "Katowice", "3 Maja", 10, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(8, "Credit Agricole", "Opole", "Ozimska", 19, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(9, "Citi Handlowy", "Szczecin", "Aleja Niepodległości", 22, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
    Bank(10, "Nest Bank", "Warszawa", "Puławska", 145, "https://cdn.pixabay.com/photo/2017/11/01/11/34/bank-2907728_1280.jpg"),
]

class Worker:
    def __init__(self, name:str, surname:str, bank:str, role:str, town:str, street:str, home_number:int, img:str, password:str):
        self.name = name
        self.surname = surname
        self.bank = bank
        self.role = role
        self.town = town
        self.street = street
        self.home_number = home_number
        self.img = img
        self.password = password
        self.coords=self.get_coords()

    def get_coords(self):
        place = f"{self.street} {self.home_number}, {self.town}, Poland"
        lat, lon = ox.geocode(place)
        return lat, lon


workers=[
    Worker("Jan", "Kowalski", "PKO Bank Polski", "Doradca", "Warszawa", "Marszałkowska", 10, "https://example.com/photo.jpg", "haslo123")
 ]

