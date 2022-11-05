import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

site = "https://realpython.github.io/fake-jobs/"
page = requests.get(site)

parse = bs(page.content, "html.parser")
results = parse.find(id = "ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
job_title1 = []
company_name1 = []
job_location1 = []

for element in job_elements:
    job_title = element.find("h2", class_ = "title").text.strip()
    company_name = element.find("h3", class_ = "company").text.strip()
    job_location = element.find("p", class_ = "location").text.strip()
    
    job_title1.append(job_title)
    company_name1.append(company_name)
    job_location1.append(job_location)
    
    # ids = [job_id]
    links = element.find_all("a")
    for link in links:
        job_link = link["href"]
        data = {
           "title":job_title1,
           "company":company_name1,
           "Location":job_location1,
           "Link":job_link
        }
    df = pd.DataFrame(data)
    
print(df)

n=0
while n <len(df):
    df.Location[n] = df.Location[n].strip()
    n = n+1
df.Location
print(df)

# df.to_csv("all1.csv")