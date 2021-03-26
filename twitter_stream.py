import tweepy
import socket
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

    def get_socket(self):
        s = socket.socket()
        host = "0.0.0.0"
        port = 5555
        s.bind((host, port))
        print('socket is ready')
        s.listen(5)
        print('socket is listening', str(port))
        self.__c_socket, self.__addr = s.accept()
        print("Received request from: " + str(addr))


    def send_data(self):
        self.get_socket()
        twitter_stream = tweepy.Stream(auth, TweetsListener(self.__c_socket))
        twitter_stream.filter(track = keyword, languages=["en"])

if __name__ == "__main__":

    consumer_key='K9DRJ3aEXjHDXcmX7xqykBax8'
    consumer_secret='oR4qaQidrsoXbuG4FWnEB7oy7E17PvwJuxJvm7w5eRgqQviS4b'
    access_token ='301786944-AiPiiXQ48Mqiv6hBtpWVvTOSh6LyDrZz93OUlI17'
    access_secret='9qthZHzm0JnbTnNd7BEyMn4l2qMx5SA9bTsTCyEWvG6by'
    tsa = TwitterStreamingApi(consumer_key, consumer_secret, access_token, access_secret)
    tsa.send_data()
#    print("User : ",tsa.get_user_details('balakrishnamadu'))
#    print("User follower count : ",tsa.get_follower_count())
#    print("User follower names : ",tsa.get_list_of_followers())