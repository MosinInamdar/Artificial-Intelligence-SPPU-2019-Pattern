def greet():
    print("Welcome to Customer Care. How can I assist you today?")

def respond(message):
    message = message.lower()

    if "order" in message:
        return "For order-related inquiries, please provide your order number."
    elif "delivery" in message or "shipping" in message:
        return "For delivery-related inquiries, please provide your tracking number."
    elif "refund" in message or "return" in message:
        return "For refund or return requests, please provide your order number."
    elif "complaint" in message or "issue" in message:
        return "I'm sorry to hear that. Please provide more details so I can assist you better."
    elif "thanks" in message or "thank you" in message:
        return "You're welcome! If you need further assistance, feel free to ask."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase or provide more details?"

def main():
    greet()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Thank you for contacting us. Have a great day!")
            break
        response = respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
