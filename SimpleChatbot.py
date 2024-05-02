def tokenize(text):
    """Converts text to lowercase and splits it into tokens."""
    return text.lower().split()

def customer_care_chatbot():
    # Dictionaries to hold responses for different categories
    responses = {
        'hours': "We're open from 9 AM to 8 PM, Monday to Saturday. Let us know if you need more information!",
        'returns': "You can return a product within 30 days of purchase with a receipt. Need help with the process?",
        'contact': "You can reach us at 1-800-123-4567 or email us at contact@example.com. Don't hesitate to contact us!",
        'location': "Our store is located at 123 Main St, Anytown, USA. Visit us for an amazing shopping experience!",
        'appointments': "You can book an appointment by calling us or visiting our website. We're here to help you!"
    }
    
    keywords = {
        'hours': ['hours', 'open', 'time', 'when'],
        'returns': ['return', 'refund', 'exchange'],
        'contact': ['contact', 'phone', 'email', 'call', 'reach'],
        'location': ['where', 'location', 'address', 'find'],
        'appointments': ['appointment', 'book', 'schedule', 'meeting']
    }
    
    print("Hello! I'm here to help with any questions you have. What would you like to know today?")
    
    while True:
        user_input = input("You: ")
        if 'exit' in user_input.lower() or 'goodbye' in user_input.lower():
            print("Bot: Thank you for contacting us. Have a great day!")
            break

        tokens = tokenize(user_input)
        responded = False
        
        for category, keys in keywords.items():
            if any(token in tokens for token in keys):
                print(f"Bot: {responses[category]}")
                responded = True
                break
        
        if not responded:
            print("Bot: I'm not sure how to answer that. Could you try a different question or maybe rephrase that?")

# Run the chatbot
customer_care_chatbot()
