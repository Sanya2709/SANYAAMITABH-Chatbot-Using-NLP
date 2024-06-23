# SANYAAMITABH-Chatbot-Using-NLP
Explanation:
Data Preparation: The sample dataset (training_data) contains example queries and their corresponding intents.
Responses Mapping: The responses dictionary maps intents to predefined responses.
NLU Pipeline: CountVectorizer and LinearSVC are used within a Pipeline to train and predict intents based on user input.
Response Generation: The generate_response function selects an appropriate response based on the predicted intent.
Interactive Loop: The script runs an interactive loop where it continuously prompts the user for input and provides responses based on the predicted intent.
Usage:
Copy and paste the entire combined code into a Python script (chatbot.py for example).
Run the script (python chatbot.py).
Enter user inputs in the console and observe the bot's responses.
This combined code provides a basic framework for a text-based chatbot capable of understanding intents and generating predefined responses
