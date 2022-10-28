import tweepy

auth = tweepy.OAuthHandler("api_key", "api_secret")
auth.set_access_token("access_token", "access_token_secret")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
