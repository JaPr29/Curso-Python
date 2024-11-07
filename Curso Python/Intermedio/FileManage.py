import os, json, csv, xml

with open("Intermedio/my_file.txt", "r+") as my_file:
    if my_file.read() == "":
        my_file.write("Hello World")
    else:
        my_file.seek(0)
        my_file.readline()
        if my_file.readline().strip() == "Hello BAD World":
            my_file.write("\nFUCK YOU PYTHON")

        
        else:
            my_file.write("\nHello BAD World")
    
    
with open("Intermedio/my_file.json", "r+") as my_file:
    json_file = {"name": "Jano", "apellido": "Juarez", "age": 18}
    json.dump(json_file, my_file, indent=4)
    my_file.seek(0)
    for i in my_file.readlines():
        print(i)
    my_file.seek(0)
    mydict = json.load(my_file)
    lista = list(mydict.values())
    print(f"My name is {lista[0]} {lista[1]} and I'm {lista[2]} years old")
def create_jsons_file():
        json1 = {"name": "Jano", "surname": "Juarez", "age": 18}
        json2 = {"name": "Rodrigo", "surname": "Sanchez", "age": 44}
        json3 = {"name": "Gustavo", "surname": "Fring", "age": 29}

        json4 = {"car": "Ford", "model": "Mustang", "year": 1964}
        json5 = {"car": "Tesla", "model": "Model S", "year": 2020}
        json6 = {"car": "Nissan", "model": "Leaf", "year": 2019}

        json7 = {"building": "The Great Wall", "country": "China", "year": 1922}
        json8 = {"building": "Empire State", "country": "USA", "year": 1930}

        jsons = {"people": [json1, json2, json3], "Cars": [json4, json5, json6], "Buildings": [json7, json8]}
        with open("Intermedio/my_jsons_file.json", "w+") as f: # Crea el archivo y lo llena de información
            json.dump(jsons, f, indent=4)

try: 
    with open("Intermedio/my_jsons_file.json", "r+") as my_file:
        jsonlist = json.load(my_file)
        people, buildings, cars = [], [], []
        
        for i in jsonlist["people"]:
            people.append(i)
        for i in jsonlist["Buildings"]:
            buildings.append(i)
        for i in jsonlist["Cars"]:
            cars.append(i)

        print(f"{people}\n {buildings}\n {cars}")

except FileNotFoundError:
    print("File not found")
    
except json.decoder.JSONDecodeError:
    print("File is empty")
    create_jsons_file()


finally:
    print("Program finished")
    jano = people[0]
    print(f"My name is {jano['name']} {jano['surname']} and I'm {jano['age']} years old")

with open("Intermedio/my_file.csv", "w+") as my_file:
    csv_writer = csv.writer(my_file)
    csv_writer.writerow(["name", "surname", "age"])
    csv_writer.writerow(["Jano", "Juarez", 18])
    csv_writer.writerow(["Rodrigo", "Sanchez", 44])
    csv_writer.writerow(["Gustavo", "Fring", 29])
    my_file.seek(0)
    for line in my_file.readlines():
        print(line)

