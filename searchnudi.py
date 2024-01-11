import requests
import time
import random

# Read search terms from the file
with open('search_terms.txt', 'r') as file:
    search_terms = [line.strip() for line in file]

# Mimic a web browser user agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Set the duration for searching in seconds (24 hours in this case)
search_duration = 24 * 60 * 60  # 60 seconds/minute * 60 minutes/hour

# Get the start time
start_time = time.time()

while time.time() - start_time < search_duration:
    # Pick a random search term
    term = random.choice(search_terms)
    print(f"searching {term}")
    # Construct the search URL
    search_url = f'https://www.google.com/search?q={term}'

    # Make the request with a delay
    response = requests.get(search_url, headers=headers)
    
    # Process the response here...

    # Introduce a random delay between requests
    time.sleep(random.uniform(3, 30))

# Your search will continue for the specified duration (24 hours) and then the loop will exit.
