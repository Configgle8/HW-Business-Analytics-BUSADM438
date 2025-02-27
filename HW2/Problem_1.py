import requests
import json

API_KEY = "4e1808d472274641be5fccae329122c4"

student_id = 991414801
keywords = ['business', 'entertainment', 'health', 'sports', 'technology']
selected_keyword = keywords[student_id % 5]

url = ('https://newsapi.org/v2/everything?'
       f'q={selected_keyword}&'
       'from=2025-02-14&'
       'to=2025-02-20&'
       'language=en&'
       'sortBy=popularity&'
       'pageSize=50&'
       f'apiKey={API_KEY}')

r = requests.get(url)
json_data = r.json()

if json_data["status"] == "ok":
       articles = json_data["articles"]

       with open("news.json", "w", encoding="utf-8") as file:
              for article in articles:
                     json.dump(article, file)
                     file.write("\n")
       print("News articles saved to 'news.json'")
else:
       print("Error collecting news:", json_data.get("message", "Unknown error"))