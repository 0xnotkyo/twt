import json
import os
import sys
from requests_oauthlib import OAuth1Session

text = sys.argv[1]
if len(text) > 280:
    print("character limit exceeded, please keep it concise!")
    sys.exit(1)

with open("secrets.json", "r") as j:
    secrets = json.load(j)

consumer_key = secrets["consumer_key"]
consumer_secret = secrets["consumer_secret"]

payload = {"text": text}

def load_tokens():
    if os.path.exists("tokens.json"):
        with open("tokens.json", "r") as f:
            return json.load(f)
    return None

tokens = load_tokens()

if tokens:
    print("Using saved tokens...")
    access_token = tokens["access_token"]
    access_token_secret = tokens["access_token_secret"]
else:
    print("Running OAuth flow...")
    request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
    oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

    try:
        fetch_response = oauth.fetch_request_token(request_token_url)
    except ValueError as e:
        print(f"There may have been an issue with the consumer_key or consumer_secret you entered: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error occurred during the OAuth flow: {e}")
        sys.exit(1)

    resource_owner_key = fetch_response.get("oauth_token")
    resource_owner_secret = fetch_response.get("oauth_token_secret")
    print("Got OAuth token: %s" % resource_owner_key)

    base_authorization_url = "https://api.twitter.com/oauth/authorize"
    authorization_url = oauth.authorization_url(base_authorization_url)
    print("Please go here and authorize: %s" % authorization_url)
    verifier = input("Paste the PIN here: ")

    access_token_url = "https://api.twitter.com/oauth/access_token"
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
        verifier=verifier,
    )

    try:
        oauth_tokens = oauth.fetch_access_token(access_token_url)
    except Exception as e:
        print(f"Error occurred while fetching access tokens: {e}")
        sys.exit(1)

    tokens = {
        "access_token": oauth_tokens["oauth_token"],
        "access_token_secret": oauth_tokens["oauth_token_secret"],
    }
    with open("tokens.json", "w") as f:
        json.dump(tokens, f)

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=tokens["access_token"],
    resource_owner_secret=tokens["access_token_secret"],
)

response = oauth.post("https://api.twitter.com/2/tweets", json=payload)

if response.status_code != 201:
    raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))

print("Response code: {}".format(response.status_code))

json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
