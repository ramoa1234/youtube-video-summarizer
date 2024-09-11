from openai import OpenAI
import requests
from bs4 import BeautifulSoup

def get_data(url):
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        return text

OPEN_AI_API_KEY = "Enter your api key here"

def send_data(data):
    client = OpenAI(
            api_key = OPEN_AI_API_KEY
    )
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "you are a helpful assiant can you please summarize what this text is about"},
            {"role": "user", "content": data}
        ]
    )

    message = response.choices[0].message.content
    print(message)



def main():
      url =  input("enter the url to summarize?")
      data = get_data(url)
      response = send_data(data)
      print(response)

main()
