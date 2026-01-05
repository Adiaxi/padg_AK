from project_lib import model, view



def add_bank(banks_data: list)->None:
    name, town, street, number, logo = banks_data
    model.banks.append(model.Bank(name=name,town=town,street=street, build_numb=number, logo=logo))
    print(model.banks)
    #user_info(users_data)



        # def user_info(users_data: list) -> None:
        #     listbox_lista_obiektow.delete(0, END)
        #     for idx, user in enumerate(users_data):
        #         listbox_lista_obiektow.insert(END,
        #                                       f"{idx} {user.name} {user.location} {user.posts} {user.img_url} posty")