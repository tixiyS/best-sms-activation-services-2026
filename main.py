import requests
import time

# Tiger SMS API V2 Wrapper Example (2026)
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.tiger-sms.com/stubs/handler_api.php"

def get_number(service_code="tg", country_code="6"):
    """Request a physical virtual number for a specific service."""
    params = {
        "action": "getNumberV2",
        "api_key": API_KEY,
        "service": service_code,
        "country": country_code
    }
    response = requests.get(BASE_URL, params=params).json()
    if "phoneNumber" in response:
        print(f"[+] Successfully acquired number: {response['phoneNumber']} for {response['activationCost']} USD")
        return response['activationId'], response['phoneNumber']
    else:
        print(f"[-] Error or No numbers available: {response}")
        return None, None

if __name__ == "__main__":
    print("--- SMS Verification API Script ---")
    print("Register at tiger-sms.com to get your API key.")
    # Example: Get a number for Telegram (tg) in USA (6)
    # get_number("tg", "6")
