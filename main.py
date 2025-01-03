import openai
import os
from dotenv import load_dotenv

# Load API key securely from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Chat function
def chat_with_gpt(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Welcome to the Hiring Assistant chatbot! Type 'exit' to quit.")
    
    # Initialize conversation
    conversation = [{"role": "system", "content": "You are a helpful assistant for a hiring agency."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Thank you for using the Hiring Assistant chatbot. Goodbye!")
            break

        # Add user message to the conversation
        conversation.append({"role": "user", "content": user_input})

        # Get chatbot response
        response = chat_with_gpt(conversation)
        print("Chatbot:", response)

        # Add chatbot response to the conversation
        conversation.append({"role": "assistant", "content": response})
