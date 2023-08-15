import requests
import time

def fetch_common_english_words():
    response = requests.get("https://api.datamuse.com/words?max=10&sp=???????")
    if response.status_code == 200:
        words = [word["word"] for word in response.json()]
        return words
    else:
        return []

def is_username_available(username):
    response = requests.get(f"https://www.instagram.com/{username}/")
    return "Sorry, this page isn't available" in response.text

while True:
    common_english_words = fetch_common_english_words()
    available_usernames = []

    for word in common_english_words:
        username = word
        if is_username_available(username):
            available_usernames.append(username)

    with open("available_usernames.txt", "a") as file:
        for username in available_usernames:
            file.write(username + "\n")

    print("Available usernames:")
    print(available_usernames)

    time.sleep(60)  # Wait for 1 minute before checking again
