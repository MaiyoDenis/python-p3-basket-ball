from basket_ball import game_dict

def get_all_players():
    game = game_dict()
    return game["home"]["players"] + game["away"]["players"]

def num_points_per_game(player_name):
    for player in get_all_players():
        if player["name"] == player_name:
            return player["points_per_game"]
    return None

def player_age(player_name):
    for player in get_all_players():
        if player["name"] == player_name:
            return player["age"]
    return None

def team_colors(team_name):
    game = game_dict()
    for location in ["home", "away"]:
        if game[location]["team_name"] == team_name:
            return game[location]["colors"]
    return None

def team_names():
    game = game_dict()
    return [game["home"]["team_name"], game["away"]["team_name"]]

def player_numbers(team_name):
    game = game_dict()
    for location in ["home", "away"]:
        if game[location]["team_name"] == team_name:
            return [player["number"] for player in game[location]["players"]]
    return []

def player_stats(player_name):
    for player in get_all_players():
        if player["name"] == player_name:
            return player
    return None

def average_rebounds_by_shoe_brand():
    players = get_all_players()
    brand_rebounds = {}
    for player in players:
        brand = player["shoe_brand"]
        rebounds = player["rebounds_per_game"]
        if brand not in brand_rebounds:
            brand_rebounds[brand] = []
        brand_rebounds[brand].append(rebounds)
    for brand, rebounds_list in brand_rebounds.items():
        average = sum(rebounds_list) / len(rebounds_list)
        print(f'{brand}:  {average:.2f}')
