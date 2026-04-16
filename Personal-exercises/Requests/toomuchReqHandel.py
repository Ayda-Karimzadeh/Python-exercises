import requests
import time

response = requests.get('https://example.com/api')

if response.status_code == 429:
    retry_after = int(response.headers.get('Retry-After', 1))
    print(f"Rate limit exceeded. Waiting {retry_after} seconds before retrying...")
    time.sleep(retry_after)
    response = requests.get('https://example.com/api')