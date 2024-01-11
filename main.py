import requests
import time
import random
import argparse

# Read search terms from the file
with open('search_terms.txt', 'r') as file:
    search_terms = [line.strip() for line in file]

# Mimic a web browser user agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def search_with_duration(total_search_time):
    # Get the start time
    start_time = time.time()

    while time.time() - start_time < total_search_time:
        # Pick a random search term
        term = random.choice(search_terms)
        print(f"Searching for {term}")
        
        # Construct the search URL
        search_url = f'https://www.google.com/search?q={term}'

        # Make the request with a delay
        response = requests.get(search_url, headers=headers)

        # Introduce a random delay between requests (3 to 300 seconds)
        # you can change this according to your need
        # wouldn't recommend you to do lower thou
        time.sleep(random.uniform(3, 300))

    print(f"Total search time of {total_search_time/60} minutes completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Nudibranch Search Script')
    parser.add_argument('--duration', type=int, default=60, help='Total search time in minutes (default: 60 minutes)')

    args = parser.parse_args()
    search_with_duration(args.duration)
    print("Congratulations, search finished")
    print("\n\n\n\t  /\_ /\    ♡\n\t ̳(• - • ̳)\n\t  |、ﾞ~ヽ\n\t  じしf_; )ノ \n\t © Joan Li, 2024")