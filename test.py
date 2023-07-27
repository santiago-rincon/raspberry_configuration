data = {"Mac":"ff:aa:ee:cc:dd:12", "temp":25, "ha":52, "hs":76, "rad":600.3, "co2":60}
mac = data.pop("Mac")
print(mac)
print(data)
for key,value in data.items():
    print(key,value)