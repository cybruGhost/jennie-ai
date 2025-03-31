import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import json
from PIL import Image, ImageTk
from modules.text_to_speech import speak
from modules.web_search import search
import threading
import openai
import os

openai.api_key = os.getenv('')  # Make sure to set this environment variable

def load_predefined_answers():
    with open("data/predefined_qa.json", 'r', encoding='utf-8') as file:
        qa_data = json.load(file)
    return qa_data

class JennieApp:
    def __init__(self, root, answers):
        self.root = root
        self.root.title("Jennie AI")
        self.answers = answers

        # Load and display Jennie's image
        self.jennie_image = Image.open("jennie_face.png")
        self.jennie_photo = ImageTk.PhotoImage(self.jennie_image)
        self.image_label = tk.Label(root, image=self.jennie_photo)
        self.image_label.pack(pady=20)

        # Status label to show if Jennie is listening
        self.status_label = tk.Label(root, text="Not Listening", fg="red")
        self.status_label.pack()

        # Text input field
        self.text_input = tk.Entry(root, width=50)
        self.text_input.pack(pady=10)
        self.text_input.bind("<Return>", self.handle_text_input)

        # Toggle Listening button
        self.toggle_listening_button = tk.Button(root, text="Speak to Jennie", command=self.toggle_listening)
        self.toggle_listening_button.pack(pady=5)

        # Response textbox
        self.response_textbox = ScrolledText(root, height=10, width=50)
        self.response_textbox.pack(pady=5)
        self.response_textbox.config(state=tk.DISABLED)

        self.is_listening = False
        self.stop_listening_event = threading.Event()

    def toggle_listening(self):
        if not self.is_listening:
            self.is_listening = True
            self.toggle_listening_button.config(text="Stop Listening")
            self.status_label.config(text="Listening...", fg="green")
            self.start_listening()
        else:
            self.stop_listening()

    def start_listening(self):
        self.stop_listening_event.clear()
        threading.Thread(target=self.handle_speech_input, daemon=True).start()

    def stop_listening(self):
        self.stop_listening_event.set()
        self.is_listening = False
        self.toggle_listening_button.config(text="Speak to Jennie")
        self.status_label.config(text="Not Listening", fg="red")

    def handle_speech_input(self):
        user_input = listen(self.stop_listening_event)  # Listen function should support stop event
        if user_input:
            # Display the recognized speech in the text input field
            self.root.after(0, lambda: self.update_text_input(user_input))
            # Simulate pressing the "Enter" key or directly process the query
            self.root.after(0, lambda: self.process_query(user_input))
        self.stop_listening()

    def update_text_input(self, text):
        """Updates the text input field with the provided text."""
        self.text_input.delete(0, tk.END)  # Clear the current content
        self.text_input.insert(0, text)  # Insert the new text

    def handle_text_input(self, event=None):
        user_input = self.text_input.get().strip()
        self.process_query(user_input)
        self.text_input.delete(0, tk.END)

    def process_query(self, query):
        if query.lower().startswith("search"):
            query_terms = query[6:].strip()
            response = search(query_terms)
        else:
            response = self.answers.get(query, "Let me look that up for you.")
            if response == "Let me look that up for you.":
                response = search(query)
        speak(response)
        self.display_response(response)

    def display_response(self, response):
        self.response_textbox.config(state=tk.NORMAL)
        self.response_textbox.delete(1.0, tk.END)
        self.response_textbox.insert(tk.END, response)
        self.response_textbox.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    answers = load_predefined_answers()
    app = JennieApp(root, answers)
    root.mainloop()
