from project_lib import controller as con, view
import osmnx as ox
import random


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

    def update(self, name, town, street, build_numb, logo):
        self.name = name
        self.town = town
        self.street = street
        self.build_numb = build_numb
        self.logo = logo
        self.coords = self.get_coords()



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

    def update(self, name, surname, bank, role, town, street, home_number, img, password):
        self.name = name
        self.surname = surname
        self.bank = bank
        self.role = role
        self.town = town
        self.street = street
        self.home_number = home_number
        self.img = img
        self.password = password
        self.coords = self.get_coords()

workers = [
    Worker("Jan", "Kowalski", banks[0], "Doradca", "Warszawa", "Marszałkowska", 11, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Anna", "Nowak", banks[0], "Kasjer", "Warszawa", "Aleje Jerozolimskie", 22, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Piotr", "Wiśniewski", banks[0], "Manager", "Warszawa", "Nowy Świat", 33, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Katarzyna", "Mazur", banks[0], "Doradca", "Warszawa", "Puławska", 44, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Michał", "Lewandowski", banks[1], "Doradca", "Kraków", "Długa", 12, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Julia", "Zając", banks[1], "Kasjer", "Kraków", "Floriańska", 24, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Krzysztof", "Lis", banks[1], "Manager", "Kraków", "Lubicz", 36, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Alicja", "Baran", banks[1], "Doradca", "Kraków", "Karmelicka", 48, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Adam", "Borkowski", banks[2], "Doradca", "Wrocław", "Rynek", 3, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Ewa", "Szulc", banks[2], "Kasjer", "Wrocław", "Świdnicka", 14, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Rafał", "Michalak", banks[2], "Manager", "Wrocław", "Legnicka", 27, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Paulina", "Sadowska", banks[2], "Doradca", "Wrocław", "Grabiszyńska", 39, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Michał", "Domański", banks[3], "Doradca", "Łódź", "Piotrkowska", 7, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Karolina", "Urbańska", banks[3], "Kasjer", "Łódź", "Narutowicza", 19, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Paweł", "Laskowski", banks[3], "Manager", "Łódź", "Zielona", 31, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Natalia", "Czajka", banks[3], "Doradca", "Łódź", "Pomorska", 44, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Krzysztof", "Urban", banks[4], "Doradca", "Gdańsk", "Długa", 4, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Alicja", "Wrona", banks[4], "Kasjer", "Gdańsk", "Grunwaldzka", 17, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Marcin", "Sowa", banks[4], "Manager", "Gdańsk", "Kartuska", 26, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Patrycja", "Lis", banks[4], "Doradca", "Gdańsk", "Hallera", 39, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Mateusz", "Kaczor", banks[5], "Doradca", "Poznań", "Półwiejska", 6, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Ewelina", "Mróz", banks[5], "Kasjer", "Poznań", "Głogowska", 18, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Piotr", "Głowacki", banks[5], "Manager", "Poznań", "Dąbrowskiego", 27, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Justyna", "Olejniczak", banks[5], "Doradca", "Poznań", "Hetmańska", 41, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Tomasz", "Kowalczyk", banks[6], "Doradca", "Katowice", "3 Maja", 5, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Aleksandra", "Piekarska", banks[6], "Kasjer", "Katowice", "Warszawska", 17, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Marek", "Sikora", banks[6], "Manager", "Katowice", "Chorzowska", 28, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Natalia", "Gajda", banks[6], "Doradca", "Katowice", "Sokolska", 41, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Michał", "Zieliński", banks[7], "Doradca", "Opole", "Ozimska", 6, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Joanna", "Kopeć", banks[7], "Kasjer", "Opole", "Katowicka", 18, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Kamil", "Barczyk", banks[7], "Manager", "Opole", "Niemodlińska", 29, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Patrycja", "Duda", banks[7], "Doradca", "Opole", "Reymonta", 44, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Tomasz", "Lewicki", banks[8], "Doradca", "Szczecin", "Aleja Niepodległości", 4, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Magdalena", "Sarnecka", banks[8], "Kasjer", "Szczecin", "Wojska Polskiego", 16, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Paweł", "Kosiński", banks[8], "Manager", "Szczecin", "Jagiellońska", 27, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Katarzyna", "Brzozowska", banks[8], "Doradca", "Szczecin", "Bohaterów Warszawy", 39, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Adam", "Wierzbicki", banks[9], "Doradca", "Warszawa", "Puławska", 8, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Karolina", "Michalak", banks[9], "Kasjer", "Warszawa", "Wilanowska", 19, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Piotr", "Sadowski", banks[9], "Manager", "Warszawa", "Dolna", 31, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
    Worker("Natalia", "Ciechanowska", banks[9], "Doradca", "Warszawa", "Rakowiecka", 44, "https://cdn.pixabay.com/photo/2021/12/20/17/22/cat-6883580_1280.png", "123"),
]


class User:
    def __init__(
        self,
        name: str,
        surname: str,
        bank: Bank,
        town: str,
        street: str,
        home_number: int,
        email: str,
        phone: str,
        password: str,
        balance: float
    ):
        self.name = name
        self.surname = surname
        self.bank = bank
        self.town = town
        self.street = street
        self.home_number = home_number
        self.email = email
        self.phone = phone
        self.password = password

        self.__balance = float(balance)

        self.coords = self.get_coords()

    def get_coords(self):
        place = f"{self.street} {self.home_number}, {self.town}, Poland"
        lat, lon = ox.geocode(place)
        return lat, lon

    def update(self, name, surname, bank, town, street, home_number, email, phone, password):
        self.name = name
        self.surname = surname
        self.bank = bank
        self.town = town
        self.street = street
        self.home_number = home_number
        self.email = email
        self.phone = phone
        self.password = password

    def get_balance(self):
        return self.__balance


users = [
    User("Adam", "Kaczmarek", banks[0], "Warszawa", "Marszałkowska", 5, "adam.k@gmail.com", "501111222", "123", 1200.50),
    User("Monika", "Lis", banks[0], "Warszawa", "Aleje Jerozolimskie", 18, "monika.l@gmail.com", "502333444", "123", 5400.00),
    User("Paweł", "Zieliński", banks[0], "Warszawa", "Nowy Świat", 33, "pawel.z@gmail.com", "503555666", "123", 300.25),
    User("Karolina", "Dąbrowska", banks[0], "Warszawa", "Puławska", 47, "karolina.d@gmail.com", "504777888", "123", 8900.00),
    User("Tomasz", "Baran", banks[1], "Kraków", "Długa", 4, "tomasz.b@gmail.com", "511111222", "123", 150.00),
    User("Natalia", "Kopeć", banks[1], "Kraków", "Floriańska", 16, "natalia.k@gmail.com", "512333444", "123", 7600.75),
    User("Kamil", "Urban", banks[1], "Kraków", "Lubicz", 29, "kamil.u@gmail.com", "513555666", "123", 980.00),
    User("Julia", "Wrona", banks[1], "Kraków", "Karmelicka", 52, "julia.w@gmail.com", "514777888", "123", 2300.00),
    User("Piotr", "Szulc", banks[2], "Wrocław", "Rynek", 6, "piotr.s@gmail.com", "521111222", "123", 999.99),
    User("Agnieszka", "Bąk", banks[2], "Wrocław", "Świdnicka", 19, "agnieszka.b@gmail.com", "522333444", "123", 4500.00),
    User("Łukasz", "Mazur", banks[2], "Wrocław", "Legnicka", 31, "lukasz.m@gmail.com", "523555666", "123", 125.00),
    User("Paulina", "Król", banks[2], "Wrocław", "Grabiszyńska", 44, "paulina.k@gmail.com", "524777888", "123", 8200.00),
    User("Michał", "Pawlak", banks[3], "Łódź", "Piotrkowska", 3, "michal.p@gmail.com", "531111222", "123", 400.00),
    User("Oliwia", "Czarnecka", banks[3], "Łódź", "Narutowicza", 14, "oliwia.c@gmail.com", "532333444", "123", 2100.00),
    User("Daniel", "Kubiak", banks[3], "Łódź", "Zielona", 27, "daniel.k@gmail.com", "533555666", "123", 15000.00),
    User("Weronika", "Sikora", banks[3], "Łódź", "Pomorska", 39, "weronika.s@gmail.com", "534777888", "123", 670.00),
    User("Marcin", "Zając", banks[4], "Gdańsk", "Długa", 2, "marcin.z@gmail.com", "541111222", "123", 100.00),
    User("Klaudia", "Rogalska", banks[4], "Gdańsk", "Grunwaldzka", 15, "klaudia.r@gmail.com", "542333444", "123", 980.00),
    User("Patryk", "Konieczny", banks[4], "Gdańsk", "Kartuska", 28, "patryk.k@gmail.com", "543555666", "123", 3500.00),
    User("Magda", "Olszewska", banks[4], "Gdańsk", "Hallera", 41, "magda.o@gmail.com", "544777888", "123", 7200.00),
    User("Sebastian", "Witkowski", banks[5], "Poznań", "Półwiejska", 8, "sebastian.w@gmail.com", "551111222", "123", 40.00),
    User("Iga", "Kaczmarek", banks[5], "Poznań", "Głogowska", 19, "iga.k@gmail.com", "552333444", "123", 2500.00),
    User("Norbert", "Gajos", banks[5], "Poznań", "Dąbrowskiego", 33, "norbert.g@gmail.com", "553555666", "123", 870.00),
    User("Laura", "Michalska", banks[5], "Poznań", "Hetmańska", 47, "laura.m@gmail.com", "554777888", "123", 13200.00),
    User("Rafał", "Cichy", banks[6], "Katowice", "3 Maja", 6, "rafal.c@gmail.com", "561111222", "123", 400.00),
    User("Daria", "Klimczak", banks[6], "Katowice", "Warszawska", 18, "daria.k@gmail.com", "562333444", "123", 5200.00),
    User("Artur", "Malinowski", banks[6], "Katowice", "Chorzowska", 27, "artur.m@gmail.com", "563555666", "123", 75.00),
    User("Sandra", "Borowska", banks[6], "Katowice", "Sokolska", 42, "sandra.b@gmail.com", "564777888", "123", 960.00),
    User("Łukasz", "Sowa", banks[7], "Opole", "Ozimska", 1, "lukasz.s@gmail.com", "571111222", "123", 1300.00),
    User("Emilia", "Biel", banks[7], "Opole", "Katowicka", 12, "emilia.b@gmail.com", "572333444", "123", 500.00),
    User("Dominik", "Górski", banks[7], "Opole", "Niemodlińska", 25, "dominik.g@gmail.com", "573555666", "123", 2200.00),
    User("Zuzanna", "Kurek", banks[7], "Opole", "Reymonta", 40, "zuzanna.k@gmail.com", "574777888", "123", 9100.00),
    User("Damian", "Kaczor", banks[8], "Szczecin", "Aleja Niepodległości", 7, "damian.k@gmail.com", "581111222", "123", 60.00),
    User("Eliza", "Sienkiewicz", banks[8], "Szczecin", "Wojska Polskiego", 21, "eliza.s@gmail.com", "582333444", "123", 7800.00),
    User("Bartek", "Duda", banks[8], "Szczecin", "Jagiellońska", 35, "bartek.d@gmail.com", "583555666", "123", 440.00),
    User("Martyna", "Lewicka", banks[8], "Szczecin", "Bohaterów Warszawy", 48, "martyna.l@gmail.com", "584777888", "123", 12000.00),
    User("Krzysztof", "Tomczak", banks[9], "Warszawa", "Puławska", 2, "krzysztof.t@gmail.com", "591111222", "123", 3300.00),
    User("Olga", "Maj", banks[9], "Warszawa", "Wilanowska", 17, "olga.m@gmail.com", "592333444", "123", 1000.00),
    User("Filip", "Orłowski", banks[9], "Warszawa", "Dolna", 26, "filip.o@gmail.com", "593555666", "123", 520.00),
    User("Natalia", "Borowska", banks[9], "Warszawa", "Rakowiecka", 44, "natalia.b@gmail.com", "594777888", "123", 8700.00),
]
