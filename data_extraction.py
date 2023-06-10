import pandas as pd




# this function receive a Json with the answer of the chatbot return a dictionary with the list of players
def player_request(chatGPT_answer):
    # read a csv file and plot the data
    df = pd.read_csv('data/players_22.csv')

    # to this prototype we will generalize the categories of the players positions
    general_positions = {
        'delantero': ['CF', 'ST'],
        'centrocampista': ['CM', 'CAM', 'CDM'],
        'defensa': ['CB', 'RB', 'LB', 'RWB', 'LWB'],
        'portero': ['GK'],
        'extremo': ['LW', 'RW', 'LM', 'RM']
    }




    players_index_positions = []

    # this is the list of player positions that the users want to find 
    find_player_positions = []

    for position in chatGPT_answer['posiciones']:
        find_player_positions.extend(general_positions[position])

    # iterate pandas dataframe and filter rows with multiple conditions
    for index, row in df.iterrows():
        if any(item in row['player_positions'].split(', ') for item in find_player_positions):
            # print(row['short_name'])
            players_index_positions.append(index)



    player_index_max_value = []
    # this is the max amount in euros that the user want to spend in the player
    max_value_eur = 10000000

    # iterate pandas dataframe and filter rows with amount <= max_value_eur
    for index, row in df.iterrows():
        if row['value_eur'] <= max_value_eur:
            # print(row['short_name'])
            player_index_max_value.append(index)

    player_index_max_value = []
    # this is the max amount in euros that the user want to spend in the player
    max_value_eur = chatGPT_answer['valor']

    # iterate pandas dataframe and filter rows with amount <= max_value_eur
    for index, row in df.iterrows():
        if row['value_eur'] <= max_value_eur:
            # print(row['short_name'])
            player_index_max_value.append(index)


    # leave the index values that are in both lists
    players_index = list(set(players_index_positions) & set(player_index_max_value))

    # columns to show
    columns = ['sofifa_id', 'short_name', 'age', 'nationality_name', 'value_eur', 'wage_eur', 'player_positions', 'club_name', 'player_face_url', 'pace',	'shooting',	'passing',	'dribbling',	'defending',	'physic'  ]


    df_recomendations = df.loc[players_index, columns]
    df_recomendations.loc[players_index, 'player_positions'] = df_recomendations.loc[players_index, 'player_positions'].str.split(', ')

    # filter the dataframe with the index values and the columns with columns, without column index, and create a dictionary with the records
    df_recomendations_dict = df_recomendations.loc[players_index, columns].to_dict(orient='records')

    return df_recomendations_dict


# JSON example
chatGPT_answer = { "valor": 30000000, "posiciones": ["delantero", "centrocampista"] }

answer_dict = player_request(chatGPT_answer)

print(answer_dict)