import requests

def send_sms():
    # Prompt the user for input
    license_key = input("Enter your license key: ")
    from_name = input("Enter sender name (from): ")
    to_numbers = input("Enter recipient numbers (comma-separated): ")
    text_message = input("Enter your message text: ")

    # Define the API endpoint
    url = "https://spoofwave.com/api/sms"

    # Define the payload data
    data = {
        "license_key": license_key,
        "from": from_name,
        "to": to_numbers,
        "text": text_message
    }

    # Set the headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Make the POST request
    response = requests.post(url, data=data, headers=headers)

    # Print the response
    if response.status_code == 200:
        response_data = response.json()
        print("Status:", response_data.get("status"))
        print("Message:", response_data.get("message"))
        print("Remaining Credits:", response_data.get("remaining_credits"))
    else:
        print("Failed to send SMS.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    send_sms()