import csv
import requests
from bs4 import BeautifulSoup

url = "https://phys.org/technology-news/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    with open("tech_news.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "url", "subcategory", "time", "forwards"])

        news_articles = soup.find_all("article", class_="accent")

        for article in news_articles:
            try:
                title_ele = article.find("h3", class_="text-large mt-2 mb-1")
                title = title_ele.get_text().strip()

                url_ele = article.find("a", class_="news-link")
                url = url_ele["href"].strip()

                subcategory_ele = article.find("figcaption", class_="accent-figure__desription").find("p")
                subcategory = subcategory_ele.get_text().strip()

                time_ele = article.find("p", class_="text-uppercase text-low")
                time = time_ele.get_text().strip()

                forwards_ele = article.find_all("p", class_="text-uppercase text-low")
                forwards = forwards_ele[2].get_text().strip()

                writer.writerow([title, url, subcategory, time, forwards])

            except Exception as e:
                print(f"Error extracting article: {e}")

    print("Data saved to tech_news.csv")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
