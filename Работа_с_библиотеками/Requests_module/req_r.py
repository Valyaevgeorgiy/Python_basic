import requests

s = ""

with open("dataset_3378_2.txt", mode="r", encoding="utf-8") as f:
    s += f.readline().strip()

r = requests.get(s)
print(len(r.text.splitlines()))