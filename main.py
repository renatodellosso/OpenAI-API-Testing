import openai

print("Reading key.env...")
key = ""
with open("key.env", "r") as file: #Read the API key from key.env
    key = file.read()
key = key.replace("OPENAI_API_KEY=", "")
print("Read key.env")

#Set the API key
openai.api_key = key

#Make a request to OpenAI
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=50,
    messages=[
        { "role": "system", "content": "You are a helpful chatbot." }, #This just clarifies what the bot should be doing
        { "role": "user", "content": "This is a test." }, #The actual prompt
    ],
)

#Get the response
print(response.choices[0].message.content)
print("Tokens Used:", response.usage)