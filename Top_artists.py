import pylast
import pandas as pd

lastfm = pd.read_csv('Piroman92.csv')

head = lastfm.head()
# print(head)
lastfm = lastfm.drop(columns=['Album'])
lastfm = lastfm.dropna(axis=0)
# lastfm['Date'] = pd.to_datetime(lastfm['Date'], format="%d/%m/%y")
lastfm = lastfm.loc[lastfm.Date>'1970-01']
lastfm['Track'] = lastfm['Artist'] + ' - ' + lastfm['Track']
# group = lastfm.groupby(by=[lastfm.Date.dt.year, lastfm.Date.dt.month]) # Sprawdzić dla Szeregów a nie dla Indexu
group = lastfm.groupby(by=lastfm['Date'].dt.to_period('M')) # Sprawdzić dla Szeregów a nie dla Indexu

lastfm = group.apply(lambda x: x.value_counts().head(10))

# lastfm = lastfm.drop(index='1970', columns='Date')
# lastfm.Date = lastfm


lastfm.to_csv("Topki.csv")

# API_KEY = 
# API_SECRET = 

# print("Enter username: ")
# username = 'Piroman92'
# print(username)
# print("Enter password: ")
# password =
# password_hash = pylast.md5(password)

# network = pylast.LastFMNetwork(
#     api_key=API_KEY,
#     api_secret=API_SECRET,
#     username=username,
#     password_hash=password_hash,
# )

# print(network.get_top_albums())

# things = network.get_geo_top_tracks("Croatia", limit=2)
# print(things)