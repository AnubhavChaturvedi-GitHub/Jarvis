import tkinter as tk
from googleapiclient.discovery import build

# Set up your API key and search engine ID
API_KEY = "your_api_key"
SEARCH_ENGINE_ID = "your_search_engine_id"

def search_google():
    query = entry.get()
    service = build("customsearch", "v1", developerKey=API_KEY)
    results = service.cse().list(q=query, cx=SEARCH_ENGINE_ID).execute()

    # Clear the previous search results
    result_text.delete(1.0, tk.END)

    # Display the search results
    for idx, result in enumerate(results.get("items", []), start=1):
        result_text.insert(tk.END, f"{idx}. {result['title']}\n{result['link']}\n\n")

# Create the main GUI window
root = tk.Tk()
root.title("Google Search")

# Create a label
label = tk.Label(root, text="Enter your search query:")
label.pack()

# Create an entry widget for the search query
entry = tk.Entry(root)
entry.pack()

# Create a search button
search_button = tk.Button(root, text="Search", command=search_google)
search_button.pack()

# Create a Text widget to display results
result_text = tk.Text(root, wrap=tk.WORD)
result_text.pack()

# Start the GUI main loop
root.mainloop()
