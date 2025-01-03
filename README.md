# Intelligent-Hiring-Assistant-Chatbot
# Intelligent Hiring Assistant Chatbot for TalentScout

## Project Overview

This project involves the development of an intelligent Hiring Assistant chatbot for **TalentScout**, a fictional recruitment agency specializing in technology placements. The chatbot is designed to assist in the initial screening of candidates by efficiently gathering essential information and posing relevant technical questions based on the candidate's declared tech stack.

The chatbot enhances the recruitment process by automating the information collection and technical assessment, allowing for faster and more effective candidate evaluation.

## Key Features

- **User Interface:**
  - Developed using **Streamlit** (or **Gradio**), providing an intuitive and user-friendly interface for candidates to interact with the chatbot.
  
- **Information Gathering:**
  - Collects essential details such as:
    - Full Name
    - Email Address
    - Phone Number
    - Years of Experience
    - Desired Position(s)
    - Current Location
    - Tech Stack
  
- **Tech Stack Declaration:**
  - Prompts candidates to specify their tech stack (e.g., programming languages, frameworks, databases, tools), which the chatbot uses to tailor technical questions.

- **Technical Question Generation:**
  - Based on the declared tech stack, the chatbot generates 3-5 relevant technical questions to assess the candidate's proficiency in each specified technology.

- **Context Handling:**
  - Maintains the context of the conversation to ensure coherent interactions and follow-up questions.

- **Fallback Mechanism:**
  - Provides meaningful responses when the chatbot does not understand the user input or when unexpected inputs are received.

- **End of Conversation:**
  - Gracefully concludes the conversation, thanking the candidate and informing them about the next steps.

## Technologies Used

- **Python:** The core programming language used to implement the chatbot.
- **Streamlit/Gradio:** Used for developing the front-end interface.
- **OpenAI API (GPT-3/4):** Utilized for natural language processing and generating responses based on candidate inputs.
- **Environment Variables:** Secure handling of the OpenAI API key using `.env` files to ensure privacy.

## Installation Instructions

### Prerequisites
Make sure you have **Python 3.7+** installed on your system.

1. Clone this repository:
   ```bash
   git clone https://github.com/urodge/talentscout-hiring-assistant.git
   cd talentscout-hiring-assistant
