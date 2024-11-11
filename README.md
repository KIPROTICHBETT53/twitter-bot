# Football Twitter Bot

A Twitter bot that streams and reposts tweets from specific accounts in real-time. This bot automatically reposts tweets from the given list of Twitter handles (excluding retweets) using the Twitter API v2.

## Features
- **Real-time streaming:** The bot listens for new tweets from specified accounts.
- **Reposts tweets:** The bot automatically reposts tweets to your Twitter account.
- **Filter retweets:** The bot avoids reposting retweets.
- **Customizable accounts:** You can add Twitter handles to the list to follow and repost from.

## Prerequisites
Before you start, ensure that you have the following installed:

- Python 3.x
- `pip` for installing Python dependencies

## Installation

### 1. Clone the repository

  ```bash
git clone https://github.com/your-username/football-bot.git
cd football-bot
```
### 2. Create a virtual environment
```bash
python -m venv venv
```
### 3. Activate the virtual environment
On Windows:
```bash
.\venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
### 4. Install the required dependencies
```bash
pip install -r requirements.txt
```
### 5. Set up environment variables
Create a .env file in the root directory of the project and add your Twitter API credentials:
```bash
BEARER_TOKEN=your_bearer_token_here
```
You can obtain your Bearer Token from the Twitter Developer Portal.

### 6. Run the bot
Once everything is set up, you can start the bot by running:

```bash
python bot.py
```
Usage
The bot will start streaming tweets from the specified Twitter accounts and repost them if they are not retweets. You can customize the accounts to follow by updating the target_usernames list in the bot.py file.

Modify target accounts:
In the bot.py file, replace the target_usernames list with the Twitter handles you want to follow:

python
Copy code
target_usernames = ["FabrizioRomano", "jack"]
Troubleshooting
Error: Consumer key must be string or bytes, not NoneType

This error occurs if your API credentials are not properly set in the .env file. Ensure that your BEARER_TOKEN is correctly added.
Error: Too Many Requests (429)

If you see this error, it means you've hit the rate limit for Twitter's API. Try again later or check Twitter's API rate limits documentation.
Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

### Key Sections Explained:
- **Installation:** This section guides users through setting up the project, including creating a virtual environment and installing dependencies.
- **Prerequisites:** Outlines the requirements such as Python and pip.
- **Usage:** Provides clear instructions on how to run the bot and how to customize it.
- **Troubleshooting:** Highlights common issues users may face, along with solutions.
- **Contributing:** Encourages contributions to the project.
- **License:** Specifies the project license, which you can modify based on your preference (MIT License is used here).

Make sure to replace placeholders like `your-username` with actual details, and you can further elaborate on your project’s unique features and setup as needed.





