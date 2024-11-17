import tkinter as tk
from tkinter import scrolledtext, messagebox
import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the OpenAI API key
api_key = os.getenv('key')
if not api_key:
    raise ValueError("API key not found. Please add OPENAI_API_KEY to your .env file.")

openai.api_key = api_key

# Function to interact with ChatGPT
def generate_response():
    user_prompt = input_text.get("1.0", tk.END).strip()
    if not user_prompt:
        messagebox.showwarning("Warning", "Please enter a prompt!")
        return
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": user_prompt}],
        )
        output_text.delete("1.0", tk.END) 
        output_text.insert(tk.END, response['choices'][0]['message']['content'])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
app = tk.Tk()
app.title("Python Coding Assistant")
app.geometry("600x600")

# Input text area
tk.Label(app, text="Enter Prompt", font=("Arial", 14)).pack(pady=5)
input_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=70, height=10)
input_text.pack(pady=10)

# Submit button
submit_button = tk.Button(app, text="Submit", font=("Arial", 14), command=generate_response)
submit_button.pack(pady=5)

# Output text area
tk.Label(app, text="Generated Response:", font=("Arial", 14)).pack(pady=5)
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=70, height=20)
output_text.pack(pady=10)

# Run the GUI loop
app.mainloop()
