# Define diseases and their associated symptoms
diseases = {
    "Alzheimer's Disease": ['memory_loss', 'confusion', 'irritability', 'personality_changes'],
    "Common Cold": ['runny_nose', 'sneezing', 'Sore_throat', 'Watering_eyes'],
    "Influenza": ['fever', 'body_aches', 'chills', 'sneezing', 'Sore_throat'],
    "Allergies": ['itchy_eyes', 'rash', 'hives', 'fever', 'swollen_airways'],
    # Add more diseases and associated symptoms as needed
}

def diagnose(symptoms, threshold=0.6):
    possible_diseases = []
    for disease, disease_symptoms in diseases.items():
        matching_symptoms = sum(symptom in symptoms for symptom in disease_symptoms)
        match_percentage = matching_symptoms / len(disease_symptoms)
        if match_percentage >= threshold:
            possible_diseases.append((disease, match_percentage))
    
    return possible_diseases

# Function to prompt user for symptoms
def get_symptoms():
    symptoms = set()
    print("Please answer with 'yes' or 'no'.")

    for symptom in all_symptoms:
        answer = input(f"Do you have {symptom.replace('_', ' ')}? ").strip().lower()
        if answer == 'yes':
            symptoms.add(symptom)
    
    return symptoms

if __name__ == "__main__":
    # Get all symptoms
    all_symptoms = set()
    for symptoms_list in diseases.values():
        all_symptoms.update(symptoms_list)

    # Prompt user for symptoms
    input_symptoms = get_symptoms()

    # Get diagnosis
    possible_diseases = diagnose(input_symptoms)

    if possible_diseases:
        print("Possible diseases:")
        for disease, match_percentage in possible_diseases:
            print(f"- {disease} (Match Percentage: {match_percentage:.0%})")
    else:
        print("No matching diseases found.")

