def flatten_tweets(tweets):
    """ Flattens out tweet dictionaries so relevant JSON is
        in a top-level dictionary. """

    tweets_list = []

    # Iterate through each tweet
    for tweet_obj in tweets:

        ''' User info'''
        # Store the user screen name in 'user-screen_name'
        tweet_obj['user-screen_name'] = tweet_obj['user']['screen_name']

        # Store the user location
        tweet_obj['user-location'] = tweet_obj['user']['location']

        ''' Text info'''
        # Check if this is a 140+ character tweet
        if 'extended_tweet' in tweet_obj:
            # Store the extended tweet text in 'extended_tweet-full_text'
            tweet_obj['extended_tweet-full_text'] = \
                                    tweet_obj['extended_tweet']['full_text']

        if 'retweeted_status' in tweet_obj:
            # Store the retweet user screen name in
            # 'retweeted_status-user-screen_name'
            tweet_obj['retweeted_status-user-screen_name'] = \
                        tweet_obj['retweeted_status']['user']['screen_name']

            # Store the retweet text in 'retweeted_status-text'
            tweet_obj['retweeted_status-text'] = \
                                        tweet_obj['retweeted_status']['text']

            if 'extended_tweet' in tweet_obj['retweeted_status']:
                # Store the extended retweet text in
                #'retweeted_status-extended_tweet-full_text'
                tweet_obj['retweeted_status-extended_tweet-full_text'] = \
                tweet_obj['retweeted_status']['extended_tweet']['full_text']

        if 'quoted_status' in tweet_obj:
            # Store the retweet user screen name in
            #'retweeted_status-user-screen_name'
            tweet_obj['quoted_status-user-screen_name'] = \
                            tweet_obj['quoted_status']['user']['screen_name']

            # Store the retweet text in 'retweeted_status-text'
            tweet_obj['quoted_status-text'] = \
                                            tweet_obj['quoted_status']['text']

            if 'extended_tweet' in tweet_obj['quoted_status']:
                # Store the extended retweet text in
                #'retweeted_status-extended_tweet-full_text'
                tweet_obj['quoted_status-extended_tweet-full_text'] = \
                    tweet_obj['quoted_status']['extended_tweet']['full_text']

        ''' Place info'''
        if 'place' in tweet_obj:
            # Store the country code in 'place-country_code'
            try:
                tweet_obj['place-country'] = \
                                            tweet_obj['place']['country']

                tweet_obj['place-country_code'] = \
                                            tweet_obj['place']['country_code']

                tweet_obj['location-coordinates'] = \
                            tweet_obj['place']['bounding_box']['coordinates']
            except: pass

        tweets_list.append(tweet_obj)

    return tweets_list
