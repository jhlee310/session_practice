import requests
from bs4 import BeautifulSoup
from book_function import extract_info
import csv

file = open("book_csv.csv", mode="w", newline="")
writer = csv.writer(file)
writer.writerow(["title", "img_src", "link", "author", "publisher" ])

final_result = []

print("크롤링을 시작합니다.")
for i in range(1, 8):
    print(f"{i+1}번째 페이지 크롤링 중...")
    book_html = requests.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("ol", {"class" : "basic"})
    book_list = book_list_box.find_all("li")

    result = extract_info(book_list)
    final_result += result

# print(final_result)

for book in final_result:
    row = []
    row.append(book["title"])
    row.append(book["img_src"])
    row.append(book["link"])
    row.append(book["author"])
    row.append(book["publisher"])
    writer.writerow(row)
    
print("크롤링 끝")