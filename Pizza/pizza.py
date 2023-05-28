import os

os.system("cls")

pizza_types = ["ananász", "húsimádó", "szalámi"]
pizza_sizes = ["kicsi", "közepes", "nagy", "családi"]
drinks = ["pepsi", "limonádé", "sprite"]

pizza_type = ""
pizza_size = ""
drink = ""

print("Pizzéria: Üdvözlöm! Mit kíván ma?")

while pizza_type == "" or pizza_size == "" or drink == "":
    user = input("Ön: ")

    for p_type in pizza_types:
        if p_type in user.lower():
            pizza_type = p_type

    for p_size in pizza_sizes:
        if p_size in user.lower():
            pizza_size = p_size

    for d in drinks:
        if d in user.lower():
            drink = d

    if pizza_type == "":
        print("Pizzéria: Milyen feltétet szeretne a pizzájára?")
    elif pizza_size == "":
        print("Pizzéria: Milyen méretű pizzát szeretne?")
    elif drink == "":
        print("Pizzéria: Milyen üdítőt kér a pizzája mellé?")

print(f"Pizzéria: Köszönjük rendelését! Nem sokára szállítjuk a {pizza_size} méretű {pizza_type} pizzát a {drink}-val/vel.")