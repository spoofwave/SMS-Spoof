# SMS Spoofer

This Python script allows you to send spoofed SMS messages using the SpoofWave API. It prompts the user for necessary details such as license key, sender name, recipient numbers, and message text, and then sends an SMS with the provided details.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the `spoofsms.py` script.

2. Install the required Python library:
    ```bash
    pip install requests
    ```

## Usage

1. Run the script from the command line:
    ```bash
    python3 spoofsms.py
    ```

2. Enter the required details when prompted:
    - **License Key**: Obtain your license key from [SpoofWave](https://spoofwave.com/buy/sms).
    - **Sender Name (From)**: The name or number that appears as the sender.
    - **Recipient Numbers (Comma-Separated)**: Enter one or more phone numbers in international format, separated by commas.
    - **Message Text**: The text content of the SMS message.

3. The script will send the SMS using the provided details and print the response from the API.

## Example

```bash
$ python3 spoofsms.py
Enter your license key: your_license_key
Enter sender name (from): SpoofWave
Enter recipient numbers (comma-separated): +351123456789,+351987654321
Enter your message text: Hello, this is a test message.

Status: success
Message: SMS sent successfully!
Remaining Credits: 50
