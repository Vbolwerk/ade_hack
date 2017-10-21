
# coding: utf-8

# ## Musimap API v 3.0 Turorial in Python 
# 
# Documentation: https://developers.musimap.net/documentation/api/usage/introduction
# 
# latest update: 30.09.2017

# In[15]:

import requests
import base64
import pandas as pd


# In[2]:

base = 'https://api.musimap.net/'


# #### Request your credentials: https://developers.musimap.net/account/clients 
# 
# click 'Add a client' and request a client_id and a client_secret which you have to set below:
# 

# In[3]:

# ADD YOUR CLIENT ID AND SECRET HERE
client_id = 'z15pn8s1j4kpi8d1'
client_secret = 'dywd5rn1ys715ed45y8hua8lo5mxwu16'


# ## Authenticate 
# 
# Get an access token. Needed for all further requests.

# In[4]:

call = 'oauth/access_token'
params = {'grant_type': 'client_credentials', 'client_id': client_id, 'client_secret': client_secret} 
resp = requests.post(base + call, params)
resp.status_code


# In[5]:

resp.text


# In[6]:

json = resp.json()
token = json['access_token']
token


# #### OAuth Header 

# In[7]:

token_enc = base64.standard_b64encode((bytes(token, 'utf-8')))


# In[8]:

# Some trouble with b64 encoding
token_enc = str(token_enc)[2:-1]


# In[9]:

# we add this token to extended HTTP request headers (used in all API requests below)
headers = {'Authorization': 'Bearer ' + token_enc}
headers


# ## Doing search on artists

# In[10]:

call = 'artists/search'

artist = 'Rihanna'
#artist = 'Adele' # note: other artists come first, the real Adele is #5

# SEARCH BY UID NOT POSSIBLE IN V 2.0
#artist_uid = '07CCB340-9C88-FE9C-0258-0398531415AF' # Rihanna (use above query to get the UID)

# output parameter controls the result and is one of the following:
# details, properties, moods, influences, memberships, discography, social (= ids of other web services)
# (can be combined in comma-separated way)

params = {'nickname': artist, 'output': 'details', 'access_token': token}
#params = {'nickname': artist, 'output': 'rhythmicmoods'}

resp = requests.get(base + call, params, headers=headers)
resp.status_code


# In[11]:

json = resp.json()
results = json['results']
results


# In[12]:

json = resp.json()
results = json['results']
for r in results:
    print (str(r['score']) + '\t' + r['uid'] + '\t' + r['nickname'])


# In[25]:

artists = pd.read_excel('DGTL_lineup_2016.xlsx', encoding='latin_1')['artist']


# In[28]:

call = 'artists/search'

for artist in artists:
#artist = 'Adele' # note: other artists come first, the real Adele is #5

# SEARCH BY UID NOT POSSIBLE IN V 2.0
#artist_uid = '07CCB340-9C88-FE9C-0258-0398531415AF' # Rihanna (use above query to get the UID)

# output parameter controls the result and is one of the following:
# details, properties, moods, influences, memberships, discography, social (= ids of other web services)
# (can be combined in comma-separated way)

    params = {'nickname': artist, 'output': 'details', 'access_token': token}
#params = {'nickname': artist, 'output': 'rhythmicmoods'}

    resp = requests.get(base + call, params, headers=headers)
    
    json = resp.json()
    results = json['results']
    for r in results:
        if r['score']==100:
            print(r['nickname'])
        


# In[ ]:



