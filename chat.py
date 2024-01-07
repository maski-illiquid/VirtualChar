from openai import OpenAI
import creds


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


OpenAi_client = OpenAI(api_key=creds.OPENAI_API_KEY)

def GenerateResponse(text):
  print( f'Got text:-  {text}')
  response = OpenAi_client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      messages=[{
          "role":
          "system",
          "content":
          "You are Bender from Futurama, the iconic robot known for his outrageous behavior and snarky comments and give response less than 30 to 40 characters"
      }, {
          "role":"user",
          "content": text
      }])
  OpenAi_Text = response.choices[0].message.content

  print(OpenAi_Text)
  return OpenAi_Text