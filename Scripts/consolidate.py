import os
import re
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from pathlib import Path

# Function to check if a string is a valid URL
def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

# Function to check if a URL is accessible and has non-empty content
def is_accessible_and_non_empty(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.text.strip():
            return True
    except requests.RequestException:
        pass
    return False

# Function to extract unique URLs from a page
def extract_urls_from_page(url):
    unique_urls = set()
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)
            if is_valid_url(full_url):
                unique_urls.add(full_url)
    except requests.RequestException:
        pass
    return unique_urls

# Main processing function
def process_folder(folder_path, output_file):
    unique_urls = set()
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    if is_valid_url(line) and is_accessible_and_non_empty(line):
                        page_urls = extract_urls_from_page(line)
                        unique_urls.update(page_urls)
    
    with open(output_file, 'w') as file:
        for url in sorted(unique_urls):
            file.write(url + '\n')

# Determine the base directory (the directory where this script is located)
base_dir = Path(__file__).parent

# Define relative paths
folder_path = base_dir / 'Blacklist' / 'Consolidate' / 'Input'
output_file = base_dir / 'Blacklist' / 'Consolidate' / 'Output' / 'domains.txt'

# Ensure the output directory exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Run the script
process_folder(folder_path, output_file)

