import requests
import openai
from bs4 import BeautifulSoup

url = "https://t.me/uniannet/136771"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find the meta tags with og:description property
    description_tags = soup.find_all('meta', attrs={'property': 'og:description'})

    # Extract the value of the first tag (if it exists).
    if description_tags:
        description = "Here should be AI descriptor " + description_tags[0].get('content')
        #print(description)
    else:
        print("Description tag not found")
else:
    print("Error:", response.status_code)



openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "Whatever"


response = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[
        {'role': 'system', 'content': 'you are a helpful assistant'},
        {'role': 'user', 'content': description}
    ],
    temperature=0.5,
    max_tokens=1024
)

#print(response)
print(response.choices[0].message.content)