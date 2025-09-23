a = [1, 3, 2, 4, 5]
print(a)
a[2] = "apple"
print(a)
print(a[0])
print(a[4])
for i in range(10):
    print(i)

b = (1, 2, 3, 4, 5)
#b[2] = "apple"
#print(b)

fruit = {"name":"apple","price":1000,"產地":"台灣"}
print(fruit.keys())

info = {
    "場地":"台北",
    "場次":{
        "場次1":"10:00",
        "場次2":"14:00",
        "場次3":"18:00",
    }
}
print(info)
print(info["場次"]["場次1"])
