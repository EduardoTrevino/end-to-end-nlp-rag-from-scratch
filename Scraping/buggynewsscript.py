import requests
from bs4 import BeautifulSoup

url = 'https://www.cmu.edu/news/stories/archives/2021/april/buggy.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    content_elements = soup.find_all(class_='content')
    with open('content_output.txt', 'w') as file:
        for element in content_elements:
            file.write(element.get_text(separator='\n', strip=True))
            file.write('\n\n')
else: 
    print("Bug present")











##Assisted via gpt 