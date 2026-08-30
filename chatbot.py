print("======================================")
print("       RULE-BASED AI CHATBOT")
print("======================================")
print("Bot: Hello! I am your AI Chatbot.")
print("Bot: Type 'bye' or 'exit' to end the conversation.")
print()

while True:
    user_input = input("You: ").lower().strip()

    # Greeting
    if user_input in ["hello", "hi", "hey", "good morning", "good evening"]:
        print("Bot: Hello! How can I help you?")

    # Asking the chatbot's name
    elif user_input in ["what is your name", "your name"]:
        print("Bot: I am a Rule-Based AI Chatbot.")

    # Asking about capabilities
    elif user_input in ["what can you do", "help"]:
        print("Bot: I can respond to predefined messages using if-else logic.")

    # Asking how the bot is doing
    elif user_input in ["how are you", "how are you doing"]:
        print("Bot: I am doing great! Thanks for asking.")

    # Asking about Artificial Intelligence
    elif user_input in ["what is ai", "what is artificial intelligence"]:
        print("Bot: Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence.")

    # Thanks
    elif user_input in ["thank you", "thanks"]:
        print("Bot: You're welcome!")

    # Exit commands
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")