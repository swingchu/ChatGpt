import os
import openai
from dotenv import load_dotenv

load_dotenv()

def AskChatGpt(question) :
  openai.api_key = os.getenv("OPENAI_API_KEY")
  #print(openai.api_key)

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.7,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  #print(response)
  return response['choices'][0].text

def main() :
  q_str=input('請提出您的問題 : ')
  print('查詢中, 請稍候...')
  print(AskChatGpt(q_str))

main()