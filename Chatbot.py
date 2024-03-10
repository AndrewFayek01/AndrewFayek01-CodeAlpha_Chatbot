import nltk
import random
from nltk.chat.util import Chat, reflections

# Define reflections to be used in the chat
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# Define some patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am good, thank you!', 'I am doing well, how about you?']),
    (r'(.*) your name?', ["I'm a chatbot.", "You can call me Chatbot."]),
    (r'(.*) (location|city) ?', ['I am a virtual entity, so I do not have a physical location.']),
    (r'bye|good bye|quit| Good bye ', ['Bye, take care.', 'Goodbye!', 'See you later!']),
    (r'thank you', ['you welcome ']),
    (r'(.*)', ['Sorry, I did not understand that.', 'Could you please repeat that?'])
]

# Create a Chatbot instance
chatbot = Chat(patterns, reflections)

# Function to start the conversation
def start_chat():
    print("Hello! I'm a chatbot. Ask me anything or type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() in ("bye", "good bye", "quit"):         
            break

# Start the conversation
start_chat()
