<div align="center"><i>post tweets from terminal </i></div>

<br>

<div align="center">
    <img height="300" src="./assets/twt.png" />
</div>

## Table of Contents

- [Usage](#usage)
- [Installation](#installation)
- [Requirements](#requirements)
- [Docs](#docs)

## Usage

- post tweets from terminal like this
   
```bash
python3 twt.py "this tweet have been posted from my terminal"
```

## Installation

1. Get API keys from [developer.twitter.com](https://developer.twitter.com/).

   - Make a project/app, enable OAuth 1.0a
   - Set to "Read and Write" perms (IMPORTANT)
   - Copy your API Key and API Secret (also called `consumer_key` and `consumer_secret`)

2. Create a file named `secrets.json` in the same directory as the script.

```json
{
  "consumer_key": "your_api_key",
  "consumer_secret": "your_api_secret"
}
   ```

3. Paste this in your config file and replace `your_api_key` and `your_api_secret` with the actual keys you obtained from Twitter.

4. Run the script for the first time, passing the tweet text as an argument:

 ```bash
python3 twt.py "{text}"
```
5. The script will output a URL like this, open it and authorize the app.

  ```bash
Please go here and authorize: https://api.twitter.com/oauth/authorize...
```

6. Twitter will give you a PIN code. Copy it and paste the PIN code into the script when it asks:

  ```bash
Paste the PIN here:
```
7. The script will complete the OAuth process and you will be able to post tweets using the script normally.

<div align="center">
    <img height="300" src="./assets/twt_terminal.gif" />
</div>

## Requirements

- Python 3.x installed
- `requests_oauthlib` library installed

## Docs

For more information about Twitter API OAuth, see:

- [Twitter Developer Documentation](https://docs.x.com/resources/fundamentals/authentication/oauth-1-0a/api-key-and-secret)
- [Requests-oauthlib Documentation](https://requests-oauthlib.readthedocs.io/en/latest/)
