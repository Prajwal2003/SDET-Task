# ExactSpace HAR File Analysis

This project analyzes the HAR (HTTP Archive) file generated from the ExactSpace website (`exactspace.co`). The goal is to inspect and categorize the HTTP status codes from the HAR data to better understand the website's traffic patterns.

## Requirements

- Python 3.x
- BrowserMob Proxy (to capture the HAR file)
- Selenium (for automation)
- Chrome WebDriver (for browsing)

## Setup

1. **Install required libraries**:
   Ensure that you have Python 3.x installed, and then install the required packages using pip:

   ```bash
   pip install selenium browsermob-proxy
   ```
   
2. **Set up BrowserMob Proxy**:

Download BrowserMob Proxy from the official website: https://github.com/lightbody/browsermob-proxy
Could you extract and set the path to the browsermob-proxy executable in the script?

3. **WebDriver**:

Download Chrome WebDriver from: https://sites.google.com/a/chromium.org/chromedriver/
Ensure the WebDriver is accessible from your PATH.

4. **Usage**:
Capture HAR Data: Run The script will capture the HTTP Archive data from the ExactSpace website and save it to a file called exactspace.har.

Analyze HAR Data: The parsing.py script analyzes the captured HAR file, categorizing HTTP status codes into groups (2XX, 3XX, 4XX, 5XX), and counts the occurrences of each status code.

Run the analysis: Execute the parse_har.py file to parse and analyze the HAR file:

The output will display a summary of the status codes and their categories.

**Sample Output**:
Status Code Counts:
```
{
    200: 2497,
    301: 156,
    302: 96,
    404: 73,
    500: 12,
    503: 8,
    403: 5
}
Category Counts:
{
    '2XX': 2497,
    '3XX': 302,
    '4XX': 78,
    '5XX': 20
}
```
