from project_lib import model, view



def add_bank(name, town, street, number, logo)->None:
    model.banks.append(model.Bank(name=name,town=town,street=street, build_numb=number, logo=logo))

def delete_bank(bank):
    model.banks.remove(bank)


