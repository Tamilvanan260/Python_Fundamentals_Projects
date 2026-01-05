import requests
import sys

def fetch_github_data():
    url = "https://api.github.com"
    try:
        response = requests.get(url)
        response.raise_for_status()  # raise error if status != 200
        print(" API Data fetched successfully!")
        data = response.json()
        print("Current GitHub API keys available:", list(data.keys()))
    except requests.exceptions.HTTPError as http_err:
        print(f" HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Other error occurred: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    print("=== Welcome to GitHub Data Fetcher ===")
    fetch_github_data()
    print("\nThank you for using this project!")
    print("This project works only inside a virtual environment (venv) 🔥")

if __name__ == "__main__":
    main()
