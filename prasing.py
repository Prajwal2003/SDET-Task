import json
import re

har_file_path = 'exactspace.har'

def clean_har_content(raw_data):
    cleaned_data = re.sub(r"(?<!\\)'", '"', raw_data)
    cleaned_data = re.sub(r',\s*}', '}', cleaned_data)
    cleaned_data = re.sub(r',\s*]', ']', cleaned_data)

    return cleaned_data


def analyze_har_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    cleaned_content = clean_har_content(content)

    try:
        har_data = json.loads(cleaned_content)

        status_code_counts = {}
        category_counts = {'2XX': 0, '4XX': 0, '5XX': 0}

        for entry in har_data['log']['entries']:
            status_code = entry['response']['status']
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            if 200 <= status_code < 300:
                category_counts['2XX'] += 1
            elif 400 <= status_code < 500:
                category_counts['4XX'] += 1
            elif 500 <= status_code < 600:
                category_counts['5XX'] += 1

        return status_code_counts, category_counts

    except json.JSONDecodeError as e:
        return f"Error parsing HAR file: {e}", None

status_code_counts, category_counts = analyze_har_file(har_file_path)

if status_code_counts is not None:
    print("Status Code Counts:", status_code_counts)
    print("Category Counts:", category_counts)
else:
    print("Failed to parse the HAR file.")
