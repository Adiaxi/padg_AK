from project_lib import controller as con, view

class Bank:
    def __init__(self, name:str, town:str, street:str, build_numb:int, logo:str):
        self.name = name
        self.town = town
        self.street = street
        self.build_numb = build_numb
        self.logo = logo
        self.coords =self.get_coords()

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


class Worker:
    def __init__(self, name:str, surname:str, town:str, street:str, home_number:int, img:str):
        self.name = name
        self.surname = surname
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