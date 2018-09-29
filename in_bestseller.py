import requests
import bs4
import csv
url = "https://www.amazon.in/gp/bestsellers/books/"
page = requests.get(url)
soup = bs4.BeautifulSoup(page.content, "lxml")
# print(soup)
pages = ["https://www.amazon.in/gp/bestsellers/books/"]
name = ["Name"]
authors = ["Author"]
url1 = ["URL"]
ratings = ["Average Rating"]
noofratings = ["Number of Ratings"]
price = ["Price"]
d = soup.find_all("li", class_='zg_page ')
chutiya = 2
size = 1
i = 1
for names in d:
    di = names.find("a")
    pages.append(di.get("href") + "#" + str(chutiya))
    chutiya += 1
    size += 1
while size > 0:
    divs = soup.find_all("div", class_='zg_itemImmersion')
    for names in divs:
        d = names.find("div", class_='p13n-sc-truncate p13n-sc-line-clamp-1')
        if d:
            name.append(d.string)
        else:
            name.append("Not available")
        # print(divss.string)
    for names in divs:
        divss = names.find("div", class_='a-row a-size-small')
        if divss:
            authors.append(divss.string)
        else:
            authors.append("Not available")
        # print(divss.string)
    for names in divs:
        divss = names.find("a")
        if divss:
            url1.append("https://www.amazon.in" + divss.get("href"))
        else:
            url1.append("Not available")
    for names in divs:
        divss = names.find("div", class_='a-icon-row a-spacing-none')
        if divss:
            avg = divss.find("i")
            ratings.append(avg.string)
        else:
            ratings.append("Not available")
    for names in divs:
        divss = names.find("a", class_='a-size-small a-link-normal')
        if divss:
            noofratings.append(divss.string)
        else:
            noofratings.append("Not available")
    for names in divs:
        divss = names.find("span", class_='p13n-sc-price')
        if divss:
            price.append(divss.getText())
        else:
            price.append("Not available")
    size -= 1
    if i <= 4:
        url = pages[i]
        page = requests.get(pages[i])
        soup = bs4.BeautifulSoup(page.content, "lxml")
    i += 1
rows = zip(name, url1, authors, price, noofratings, ratings)
with open('in_book.cv', 'w') as file:
    writer = csv.writer(file, delimiter=";")
    for row in rows:
        writer.writerow(row)
