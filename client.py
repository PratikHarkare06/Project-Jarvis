from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)