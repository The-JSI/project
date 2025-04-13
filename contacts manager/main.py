import json


def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|" ,person["age"], "|" ,person["email"], "|")

def add_person():
    name = input("name: ")
    age = input("age: ")
    email = input("email: ")

    person = {"name": name, "age": age, "email": email}
    return person

def delete_contact(people):
     display_people(people)

     while True:
        number = input("enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("invalid number out of range.")
            else:
                break
        except:
            print("invalid number")

     deleted_person = people.pop(number - 1)
     print(f"{deleted_person["name"]} deleted!")

def search(people):
    search_name = input("Search for a name: ").lower()
    search_results = [] #searches for people that macth a particular result

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            search_results.append(person)

    display_people(search_results)

print("hello. welcome to contact list")
print()

with open ("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print("No. of contects:", len(people))
    command = input("add, delete or search  or quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("person added!")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "quit":
        break
    else:
        print("invalid command")

with open ("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
