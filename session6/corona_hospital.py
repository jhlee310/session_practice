import requests
from bs4 import BeautifulSoup
import csv

hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'
hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")

# 이제부터 시도, 시군구, 선별진료소(이름), 전화번호 크롤링 후 csv 파일에 저장하시면 됩니다!

file = open("hospital.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["province", "state", "hospital_name", "telephone"])

result = []
final_result = []

print("크롤링을 시작합니다.")
hospital_list_box = hospital_soup.find("tbody", {"class" : "tb_center"})
hospital_list = hospital_list_box.find_all("tr")
for hospital in hospital_list:
    hospital_data = hospital.find_all("td")
    info_list = []
    for data in hospital_data:
        info = data.get_text()
        info_list.append(info)
    result.append(info_list)

for i in result:
    province = i[0]
    state = i[1]
    hospital_name = i[2]
    telephone = i[3]

    hospital_info = {
        "province" : province,
        "state" : state,
        "hospital_name" : hospital_name.strip(),
        "telephone" : telephone
    }
    final_result.append(hospital_info)

# print(final_result)

print("크롤링 끝")
print("csv 변환 시작")

for result in final_result:
    row = []
    row.append(result["province"])
    row.append(result["state"])
    row.append(result["hospital_name"])
    row.append(result["telephone"])

    writer.writerow(row)

print("csv 변환 끝")
