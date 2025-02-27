import json
import csv

input_file = "news.json"
output_file = "news.csv"

articles = []
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        articles.append(json.loads(line))

csv_headers = ["source_name", "author", "title", "publishedAt", "url", "description", "content"]

with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(csv_headers)

    for article in articles:
        writer.writerow([
            article.get("source", {}).get("name", ""),
            article.get("author", ""),
            article.get("title", ""),
            article.get("publishedAt", ""),
            article.get("url", ""),
            article.get("description", ""),
            article.get("content", "")
        ])

print(f"Data collection complete saved to '{output_file}'")
