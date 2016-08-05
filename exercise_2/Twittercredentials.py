import tweepy

consumer_key = "AqrCRBU9ZhJdd4LwaHJ4nBAgp";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "NVKZB8ASQyC01onWuzwQN5MJWH3qTB8bcb5yPICu6tp4z2Txsu";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "22733355-rIUkywT1ZHhIC1in7AZTmlRju6KLJ6lwc61FLBwK1";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "EZU4vwmQWpspiTTxbdmkiTE0Qb8v8EQqWTqvXxWUbG8Xx";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



