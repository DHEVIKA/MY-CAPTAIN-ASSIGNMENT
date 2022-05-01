car = {
    "brand":"Ford",
    "model":"Mustang",
    "Year":1964
}
car.clear()
print(car)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x = car.copy()
print(x)
x =('key1','key2','key3')
y =0
thisdict = dict.fromkeys(x,y)
print(thisdict)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x = car.get("model")
print(x)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x = car.items()
print(x)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x = car.keys()
print(x)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x = car.pop("model")
print(car)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x = car.popitem()
print(car)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x = car.setdefault("model","Bronco")
print(x)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
car.update({"color":"White"})
x = print(car)
car ={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964"
}
x = car.values()
print(x)


