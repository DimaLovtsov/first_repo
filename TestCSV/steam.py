import requests

api_key = "YOUR_API_KEY"
steam_id = "1507743284"

url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_id}"

try:
    response = requests.get(url)
    response.raise_for_status()  # Проверка на успешность запроса
    data = response.json()  # Попытка декодировать JSON
    if 'response' in data and 'players' in data['response']:
        player_info = data['response']['players'][0]
        country_code = player_info.get('loccountrycode', 'Country not specified')
        print(f"Country: {country_code}")
    else:
        print("User information not available")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"Error occurred: {err}")
except ValueError:
    print("Response content is not valid JSON")