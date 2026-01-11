from project_lib import model, view



def add_bank(name, town, street, number, logo)->None:
    model.banks.append(model.Bank(name=name,town=town,street=street, build_numb=number, logo=logo))

def delete_bank(bank):
    model.banks.remove(bank)

def details_bank(bank):
    return {
        "name": bank.name,
        "town": bank.town,
        "street": bank.street,
        "number": bank.build_numb,
        "coords": bank.coords
    }

def add_worker(name, surname, bank, role, town, street, number, logo, password)->None:
    model.workers.append(model.Worker(name=name, surname=surname, bank=bank, role=role, town=town, street=street, home_number=number, img=logo, password=password))

def delete_worker(worker):
    model.workers.remove(worker)

def details_worker(worker):
    return {
        "name": worker.name,
        "surname": worker.surname,
        "bank": worker.bank,
        "role": worker.role,
        "town": worker.town,
        "street": worker.street,
        "number": worker.home_number,
        "coords": worker.coords
    }


