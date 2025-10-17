def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easy comparison

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks for asking! 😊"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day! 👋"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple chatbot created in Python. 🤖"
    else:
        return "I'm sorry, I don't understand that yet. 😅"

# Step 2: Main program loop
print("🤖 Welcome to the Basic Chatbot! Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Chatbot: Goodbye! Have a great day! 👋")
        break

    # Get chatbot response
    response = chatbot_response(user_input)
    print("Chatbot:", response)
