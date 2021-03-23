import tweepy


class TwitterStreamingApi:

    def __init__(self, consumer_key, consumer_secret, access_token, access_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.__api = tweepy.API(auth)

    def get_user_details(self, user_name):
        self.__user = self.__api .get_user(user_name)
        return self.__user.screen_name

    def get_follower_count(self):
        return self.__user.followers_count

    def get_list_of_followers(self):
        return self.__user.friends()

if __name__ == "__main__":

    consumer_key='Provide details'
    consumer_secret='Provide details'
    access_token ='Provide details'
    access_secret='Provide details'
    tsa = TwitterStreamingApi(consumer_key, consumer_secret, access_token, access_secret)
    print("User : ",tsa.get_user_details('balakrishnamadu'))
    print("User follower count : ",tsa.get_follower_count())
    print("User follower names : ",tsa.get_list_of_followers())