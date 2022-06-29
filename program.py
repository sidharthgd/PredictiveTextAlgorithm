
# import tweepy
import tweepy as tw
import re

# your Twitter API key and API secret
my_api_key = "uie1OPB42CbQWl5Biap06RB9I"
my_api_secret = "dmUdIxeXAcqWa9FeI28il26TiNO4xL7VwkWD2IfBBplBvxL8ce"
my_bearer_token = "AAAAAAAAAAAAAAAAAAAAAC39aAEAAAAAEH0F7kqEugMxcDNzvzIduDKCHDs%3DOw0Gyv5wsEpNELll3f3UKyFm8HmLccMbKxrZ7XZa0gDsq5HN2V"
my_access_token = "1503602837304987648-gIZRr0WWpqE6txtxghB4hM9wRptOU1"
my_secret_access_token = "A8aXRh17cd3kEh6pVY935Wn31OYHRgxlBTppb7V2s7qLf"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)
client = tw.Client(bearer_token=my_bearer_token,
                        consumer_key=my_api_key,
                        consumer_secret=my_api_secret,
                        access_token=my_access_token,
                        access_token_secret=my_secret_access_token,
                        return_type=tw.Response,
                        wait_on_rate_limit=True)

user = api.get_user(screen_name='ihyjuju')
#print(user.data)


usersArr = client.get_users_followers(user.id,
                                      max_results=3,
                                      pagination_token=None,
                                      tweet_fields=None,
                                      user_fields="id",
                                      user_auth=False)



userIdArr = []
for i in usersArr[0]:
    userIdArr.append(i.id)



tweetsArr = []
for id in userIdArr:
    tweetsArr.append(client.get_users_tweets(id,
                            end_time=None,
                            exclude=None,
                            expansions=None,
                            max_results=5,
                            media_fields=None,
                            pagination_token=None,
                            place_fields=None,
                            poll_fields=None,
                            since_id=None,
                            start_time=None,
                            tweet_fields=None,
                            until_id=None,
                            user_fields=None,
                            user_auth=False))

#(str(tweetsArr))
'''
print((tweetsArr))
print("\n *******")
print((tweetsArr[1]))
print("\n *******")
print((tweetsArr[1][0]))
print("\n *******")
print((tweetsArr[1][0][0]))
'''

tweetTextArrOrg = []
for response in tweetsArr:
    if response.data == None:
        continue

    data = response.data
    for tweet in data:
        tweetTextArrOrg.append(tweet.text)

tweetTextArr = [re.sub(r'\s*[@]+\w+\s*', '', x) for x in tweetTextArrOrg]

print(tweetTextArr)
print(len(tweetTextArr))

file = open("tweetData.txt", "w")

for i in tweetTextArr:
    file.write(str(i) + "\n")
