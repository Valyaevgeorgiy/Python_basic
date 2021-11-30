import requests

s = ""
count = 1

with open("dataset_3378_3.txt", mode="r", encoding="utf-8") as f:
    s += f.readline().strip()

s_lst = s.split('/')

s_now = s_lst[0] + "//" + s_lst[2] + "/" + s_lst[3] + "/" + s_lst[4] + "/" + s_lst[5] + "/" + s_lst[6] + "/"

final_string = "oopoppo"

while final_string[0:2] != "We":

    print(f"{count} итерация:")
    count += 1
    r = requests.get(s)

    final_string = r.text

    print(f"Ссылка на файл - {s}")
    #print(f"Имя следующего файла - {r.text}")
    s = s_now + r.text

else:
    print("ВНЕЗАПНО итерации закончились, потому что...")
    print(final_string)
