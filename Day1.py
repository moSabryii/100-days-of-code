print("Hello citizen")
city = input("What was the city you grow up in?\n")
pet = input("Do you have a cat? y/n")
if pet == "y":
    cat_name = input("What is their name?")
    print("Your band name can be " + city + " " + cat_name)
else:
    other_pet = input("ok, write your other pet name:\n")
    print("Your band name can be " + city + " " + other_pet)
