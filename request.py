import csv
import requests
import time

def read_txt(websites):
    with open(websites, 'r') as txtfile:
        websites_list = [line.strip() for line in txtfile]
    return websites_list

# Use the correct path to your 'websites.txt' file
websites_list = read_txt(r'C:\Users\amujt\OneDrive\Desktop\Request\websites.txt')

def process_websites(websites):
    results = []

    for website in websites:
        url_http = f"http://{website}"
        url_https = f"https://{website}"

        try:
            http_response = requests.get(url_http, timeout=10)
            http_status = http_response.status_code
            http_size = len(http_response.content)
        except requests.exceptions.RequestException:
            http_status = "Error"
            http_size = 0

        try:
            https_response = requests.get(url_https, timeout=10)
            https_status = https_response.status_code
            https_size = len(https_response.content)
        except requests.exceptions.RequestException:
            https_status = "Error"
            https_size = 0

        results.append((website, http_status, http_size))
        results.append((website, https_status, https_size))

        # Introduce a delay of 1 second between requests
        time.sleep(1)

    return results

def write_response_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Subdomain', 'HTTP Response Code', 'HTTP Response Size', 'HTTPS Response Code', 'HTTPS Response Size'])
        writer.writerows(data)

if __name__ == "__main__":
    response_data = process_websites(websites_list)
    write_response_csv(response_data, 'responses.csv')
