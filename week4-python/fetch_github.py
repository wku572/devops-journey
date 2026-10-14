import json
import os
import sys

import requests


def fetch_profile(username):
    url = f"https://api.github.com/users/{username}"
    headers = {}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

def main():
    username = sys.argv[1] if len(sys.argv) > 1 else "wku572"

    try:
        data = fetch_profile(username)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(f"Request failed: {err}")
        sys.exit(1)

    summary = {
        "username": data.get("login"),
        "name": data.get("name"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "created_at": data.get("created_at"),
    }

    with open("github_profile.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"Saved profile for {summary['username']}")
    print(f"Public repos: {summary['public_repos']}")


if __name__ == "__main__":
    main()
