from project_lib import model, view
import osmnx as ox


def add_bank(name, town, street, number, logo) -> None:
    model.banks.append(model.Bank(name=name, town=town, street=street, build_numb=number, logo=logo))


def delete_bank(bank):
    for w in model.workers[:]:
        if w.bank is bank:
            model.workers.remove(w)

    for u in model.users[:]:
        if u.bank is bank:
            model.users.remove(u)

    model.banks.remove(bank)


def details_bank(bank):
    return {
        "name": bank.name,
        "town": bank.town,
        "street": bank.street,
        "number": bank.build_numb,
        "coords": bank.coords
    }


def add_worker(name, surname, bank, role, town, street, number, logo, login, password) -> None:
    model.workers.append(
        model.Worker(name=name, surname=surname, bank=bank, role=role, town=town, street=street, home_number=number,
                     img=logo, login=login, password=password))


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
        "login": worker.login,
        "coords": worker.coords
    }


def add_user(name, surname, bank, town, street, number, email, phone, password, balance) -> None:
    model.users.append(
        model.User(
            name=name,
            surname=surname,
            bank=bank,
            town=town,
            street=street,
            home_number=number,
            email=email,
            phone=phone,
            password=password,
            balance=balance
        )
    )


def delete_user(user):
    model.users.remove(user)


def details_user(user):
    return {
        "name": user.name,
        "surname": user.surname,
        "bank": user.bank.name,
        "town": user.town,
        "street": user.street,
        "number": user.home_number,
        "email": user.email,
        "phone": user
    }
