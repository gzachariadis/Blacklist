import os
import re
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Find the Git repository root
def find_git_root(start_path):
    current_path = Path(start_path).resolve()
    while current_path != current_path.parent:
        if (current_path / '.git').exists():
            return current_path
        current_path = current_path.parent
    raise FileNotFoundError("Git repository root not found")

# Check string is valid URL
def is_valid_url(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme) and bool(parsed_url.netloc)

# Check URL is accessible and has non-empty content
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
def process_folder(input_folder, output_file):
    unique_urls = set()
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    logging.info(f'{filename} - {line_number}: {line}')
                    if is_valid_url(line) and is_accessible_and_non_empty(line):
                        page_urls = extract_urls_from_page(line)
                        unique_urls.update(page_urls)
    
    with open(output_file, 'w') as file:
        for url in sorted(unique_urls):
            file.write(url + '\n')
    logging.info(f'Unique URLs written to: {output_file}')

# Repository Directory
repo_root = find_git_root(__file__)

# Relative Paths 
input_folder = repo_root / 'Consolidate' / 'Input'
output_file = repo_root / 'Consolidate' / 'Output' / 'domains.txt'

# Ensure the output directory exists
output_file.parent.mkdir(parents=True, exist_ok=True)

# Run the script
process_folder(input_folder, output_file)

