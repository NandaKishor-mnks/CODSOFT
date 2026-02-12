print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Chatbot: Hi there!")

    elif user == "how are you":
        print("Chatbot: I am fine. How can I help you?")

    elif user == "what is your name":
        print("Chatbot: I am a rule-based chatbot.")

    elif user == "bye":
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")
