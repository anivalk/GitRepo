import requests
import os 
from dotenv import load_dotenv

def make_request(query_parameters):
    base_url = "https://api.nasa.gov/neo/rest/v1/feed/"
    load_dotenv()
    api_key2 = os.environ.get('NASAWEB_API_KEY')
    HEADER = {'Authorization': api_key2}
    url= base_url + '?api_key=' + api_key2
    print(url)
    response = requests.get(url, headers=HEADER)
    print(response.json())
    return response





# Now you can access the environment variable just like before


