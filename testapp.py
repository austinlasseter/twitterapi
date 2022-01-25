import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAC2eYQEAAAAA1idxHQ1U4YFvQO2kiDSrOlW2GRI%3DAFAvR8Gb8M6CjKEJMzFdlY37o1tb1QzHUZ1OgLwTbWu7GLKap0"

search_url = "https://api.twitter.com/2/tweets/search/recent"

query_params = {'query': '#collectiveashbery','tweet.fields': 'author_id','user.fields': 'location', 'max_results': 25}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    response = requests.get(https://api.twitter.com/2/tweets/search/recent, auth=bearer_oauth, params={'query': '#collectiveashbery','tweet.fields': 'author_id','user.fields': 'location', 'max_results': 25})
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    parsed_data = data.json()
    return response.json()

    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
