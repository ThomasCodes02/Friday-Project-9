import tkinter as tk
from tkinter import messagebox
import openai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("key")

if not api_key:
    raise ValueError("API key not found. Ensure it is defined in the .env file as 'key'.")

# Set the API key
openai.api_key = api_key

# Function to generate a response from OpenAI
def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred. Please try again."

# Function to handle the submit button click
def on_submit():
    prompt = prompt_entry.get("1.0", tk.END).strip()  # Get user input from Text widget
    if not prompt:
        messagebox.showerror("Error", "Please enter a prompt!")
        return
    
    # Get the response from OpenAI
    response = generate_response(prompt)
    response_text.delete("1.0", tk.END)  # Clear previous response
    response_text.insert(tk.END, response)  # Display the response

# Set up the GUI
root = tk.Tk()
root.title("ChatGPT Prompt GUI")

# Prompt label and entry
prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack(pady=5)

prompt_entry = tk.Text(root, height=10, width=50)
prompt_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Response label and text box
response_label = tk.Label(root, text="Response:")
response_label.pack(pady=5)

response_text = tk.Text(root, height=15, width=50)
response_text.pack(pady=5)

# Run the application
root.mainloop()