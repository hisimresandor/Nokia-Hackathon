import os

os.system("cls")

# Listák létrehozása a kínálattal feltöltve
pizza_types = ["ananász", "húsimádó", "szalámi"]
pizza_sizes = ["kicsi", "közepes", "nagy", "családi"]
drinks = ["pepsi", "limonádé", "sprite"]

# Bekérendő adatok tárolására használt változók létrehozása
pizza_type = ""
pizza_size = ""
drink = ""

# Beszélgetés kezdése
print("Pizzéria: Üdvözlöm! Mit kíván ma?")

# Beszélgetés folytatása, amíg minden adatot meg nem ad a felhasználó
while pizza_type == "" or pizza_size == "" or drink == "":
    # Üzenet bekérése
    user = input("Ön: ")

    # Üzenet ellenőrzése, az adatok esetleges tárolása
    for p_type in pizza_types:
        if p_type in user.lower():
            pizza_type = p_type

    for p_size in pizza_sizes:
        if p_size in user.lower():
            pizza_size = p_size

    for d in drinks:
        if d in user.lower():
            drink = d

    # További kérdések feltétele az adatok bekéréséhez
    if pizza_type == "":
        print("Pizzéria: Milyen feltétet szeretne a pizzájára?")
    elif pizza_size == "":
        print("Pizzéria: Milyen méretű pizzát szeretne?")
    elif drink == "":
        print("Pizzéria: Milyen üdítőt kér a pizzája mellé?")

# Elköszönő üzenet
print(f"Pizzéria: Köszönjük rendelését! Nem sokára szállítjuk a {pizza_size} méretű {pizza_type} pizzát a {drink}-val/vel.")