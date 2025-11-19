import os
import google.generativeai as genai

genai.configure(api_key="?")

model = genai.GenerativeModel("gemini-2.0-flash")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = model.generate_content(user_input)
    print("Gemini:", response.text)

