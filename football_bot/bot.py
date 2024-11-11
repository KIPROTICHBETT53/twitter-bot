import tweepy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Print the Bearer Token to check if it's loaded correctly
print("Bearer Token:", os.getenv('BEARER_TOKEN'))

# Set up authentication with the bearer token
client = tweepy.Client(
    bearer_token=os.getenv('BEARER_TOKEN')  # Ensure you are using the correct bearer token
)

# Test the authentication
try:
    client.get_me()  # This makes a call to get the authenticated user's data
    print("Authentication successful")
except Exception as e:
    print("Error during authentication:", e)


# Define the Stream Listener class using StreamingClient
class MyStreamListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        # Only repost if the tweet is not a retweet to avoid duplicates
        if not tweet.referenced_tweets:
            tweet_text = tweet.text
            print(f"New tweet from {tweet.author_id}: {tweet_text}")
            # Repost the tweet
            client.create_tweet(text=tweet_text)
            print("Reposted the tweet.")

    def on_error(self, status_code):
        if status_code == 420:
            # Disconnect the stream to avoid rate limits
            print("Rate limit exceeded. Disconnecting...")
            return False  # Stop the stream
        else:
            print(f"Error occurred: {status_code}")
            return True  # Continue streaming despite other errors


def get_user_id(username):
    """Get the user ID for a Twitter username."""
    try:
        user = client.get_user(username=username)
        if user:
            return user.data.id
        else:
            print(f"User {username} not found.")
            return None
    except Exception as e:
        print(f"Error getting user ID for {username}: {e}")
        return None


def start_stream(target_usernames):
    """Start the stream to follow specific accounts in real-time."""
    # Get user IDs for each target account
    target_account_ids = [get_user_id(username) for username in target_usernames]

    # Filter out None values in case there were errors in retrieving user IDs
    target_account_ids = [user_id for user_id in target_account_ids if user_id]

    # Initialize and start the stream
    if target_account_ids:  # Only start streaming if there are valid user IDs
        my_listener = MyStreamListener(bearer_token=os.getenv('BEARER_TOKEN'))  # Ensure bearer token is set
        # Add rules to track specific user IDs
        for user_id in target_account_ids:
            my_listener.add_rules(tweepy.StreamRule(f'from:{user_id}'))

        my_listener.filter(expansions=["author_id"], is_async=True)
        print("Started streaming for accounts:", target_usernames)
    else:
        print("No valid user IDs found. Exiting...")


if __name__ == "__main__":
    # List of Twitter handles you want to follow and repost from
    target_usernames = ["FabrizioRomano", "jack"]  # Use valid Twitter usernames
    start_stream(target_usernames)
