import requests

headers = {
  "apikey": "YOUR-APIKEY"}

params = (
   ("q","webflow responsive problem"),
   ("search_engine","google.com"),
   ("gl","US"),
   ("hl","en"),
   ("num","50"),
);

response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params);
# create a .csv file with the results
print(response.text)