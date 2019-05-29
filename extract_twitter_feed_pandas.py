import configparser
import pandas as pd
from twython import Twython
import json

def extract_twitter_feed(twitter_properties_file, search_query):
    twitter_config = configparser.ConfigParser()
    twitter_config.read(twitter_properties_file)
    consumer_key = twitter_config['TwitterAuthentication']['twitter.consumer_key']
    consumer_secret = twitter_config['TwitterAuthentication']['twitter.consumer_secret']
    #the next two are used erither for POSTED tweets or if you want to use the professional api instead of the standard free
    access_token_key = twitter_config['TwitterAuthentication']['twitter.consumer_access_token_key']
    access_token_secret = twitter_config['TwitterAuthentication']['twitter.consumer_access_token_secret']

    python_tweets = Twython(consumer_key, consumer_secret)


    dict_ = {'search': [], 'id': [], 'date': [], 'text': [], 'user_name': [], 'user_description': [], 'user_location':[], 'hashtags':[], 'favorite_count': [], 'retweet_count': []}

    for status in python_tweets.search(**search_query)['statuses']:
        dict_['search'].append(search_query['q'])
        dict_['id'].append(status['id'])
        dict_['date'].append(status['created_at'])
        dict_['text'].append(status['text'])
        dict_['user_name'].append(status['user']['screen_name'])
        dict_['user_description'].append(status['user']['description'])
        dict_['user_location'].append(status['user']['location'])
        hashtags = status['entities']['hashtags']
        if hashtags == []:
            dict_['hashtags'].append('')
        else:
            dict_['hashtags'].append(hashtags[0]['text'])
        dict_['favorite_count'].append(status['favorite_count'])
        dict_['retweet_count'].append(status['retweet_count'])
    result = pd.DataFrame(dict_)
    return result

if __name__ == "__main__":
    twitter_search_properties = 'search.properties'
    search_config = configparser.ConfigParser()
    search_config.read(twitter_search_properties)
    search_phrase = search_config['TrendsSearch']['trends.search_phrase']
    search_language = search_config['TrendsSearch']['trends.search_language']
    search_from = search_config['TrendsSearch']['trends.search_from']
    search_to = search_config['TrendsSearch']['trends.search_to']
    #https: // developer.twitter.com / en / docs / tweets / search / api - reference / get - search - tweets
    search_query = {'q': search_phrase,
             'result_type': 'popular',
             'count': 100,  #maximum
             'lang': search_language,
             'until': search_to,
             }
    result = extract_twitter_feed('twitter.properties', search_query)
    print(result)
