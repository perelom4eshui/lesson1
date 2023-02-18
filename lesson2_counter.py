from collections import Counter
phones = ["iPhone 12", "Samsung Galaxy S21", "Xiaomi Mi11", "iPhone 12",
            "iPhone 12", "Xiaomi Mi11"]
count = Counter(phones)

print(count)

text = "Ехал грека через реку видит Грека в реке рак"
count = Counter(text.lower().replace(" ",""))
print(count)