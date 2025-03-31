import json

def get_response(text):
    with open("data/predefined_qa.json", "r") as file:
        qa = json.load(file)
    
    return qa.get(text, "Sorry, I don't understand that.")
