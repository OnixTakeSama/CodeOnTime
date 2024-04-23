import itertools

# DATASET 5 BEST SCORE

# def build_relay_teams(input_file, num_athletes_per_team, output_file):
#     # Lecture des données des athlètes à partir du fichier
#     with open(input_file, 'r') as file:
#         athletes_data = [tuple(map(float, line.strip().split(','))) for line in file]

#     # Tri des athlètes par temps croissant
#     athletes_data.sort(key=lambda x: x[1])

#     # Nombre d'équipes
#     num_teams = len(athletes_data) // num_athletes_per_team

#     # Sélection du nombre d'athlètes le plus proche d'un multiple de num_athletes_per_team
#     num_athletes = num_teams * num_athletes_per_team
#     athletes_data = athletes_data[:num_athletes]

#     # Distribution équilibrée des athlètes dans les équipes
#     teams = [[] for _ in range(num_teams)]
#     for i, (athlete_id, _) in enumerate(athletes_data):
#         team_index = i % num_teams
#         teams[team_index].append((int(athlete_id), _))

#     # Répartition équilibrée des athlètes dans les équipes
#     for i, team in enumerate(teams):
#         while len(team) < num_athletes_per_team:
#             # Sélection de l'athlète suivant en fonction de la différence de temps entre les équipes
#             best_athlete = min(athletes_data, key=lambda x: abs(x[1] - sum([t[1] for t in team])))
#             team.append(best_athlete)
#             athletes_data.remove(best_athlete)

#     # Calcul des temps pour chaque équipe
#     team_times = []
#     for team in teams:
#         team_time = 0
#         for i in range(len(team) - 1):
#             # Calcul du temps de transmission du relais avec arrondi à la centième de seconde la plus proche
#             relais_time = round(((team[i + 1][1] - team[i][1]) ** 2) * 100) / 100
#             team_time += (team[i][1] + relais_time)
#         # Ajout du temps du dernier athlète
#         team_time += team[-1][1]
#         team_times.append(team_time)

#     # Calcul de la différence de temps entre la meilleure équipe et la dernière
#     time_difference = max(team_times) - min(team_times)

#     # Écriture des équipes dans un fichier texte
#     with open(output_file, 'w') as output:
#         for team in teams:
#             output.write(" ".join(map(str, [athlete[0] for athlete in team])) + " \n")

#     return time_difference

# # Fichier contenant les données des athlètes
# input_file = "data5.txt"

# # Fichier de sortie pour les compositions d'équipes
# output_file = "relay_teams.txt"

# # Taille des équipes
# num_athletes_per_team = 128

# # Construction des équipes et écriture dans le fichier de sortie
# time_difference = build_relay_teams(input_file, num_athletes_per_team, output_file)

# # Affichage de la différence de temps entre la meilleure équipe et la dernière
# print("Différence de temps :", time_difference)

# ---------------------------------------------------------------
# DATASET 4 / 3 / 2 / 1 BEST SCORE
# ---------------------------------------------------------------

def build_relay_teams(input_file, num_athletes_per_team, output_file):
    # Lecture des données des athlètes à partir du fichier
    with open(input_file, 'r') as file:
        athletes_data = [tuple(map(float, line.strip().split(','))) for line in file]

    # Tri des athlètes par temps croissant
    athletes_data.sort(key=lambda x: x[1])

    # Construction des équipes
    teams = [[] for _ in range(num_athletes_per_team)]
    for i, athlete in enumerate(athletes_data):
        teams[i % num_athletes_per_team].append(athlete)

    # Calcul des temps pour chaque équipe
    team_times = []
    for team in teams:
        team_time = team[0][1]  # Temps du premier athlète
        for i in range(len(team) - 1):
            # Calcul du temps de transmission du relais
            relais_time = ((team[i + 1][1] - team[i][1]) ** 2) ** 0.5
            team_time += (team[i][1] + relais_time)
        # Ajout du temps du dernier athlète
        team_time += team[-1][1]
        team_times.append(team_time)

    # Calcul du temps minimum de la meilleure équipe et du temps maximum de la pire équipe
    min_best_team_time = min(team_times)
    max_worst_team_time = max(team_times)

    # Calcul de la différence de temps entre la meilleure équipe et la dernière
    time_difference = max_worst_team_time - min_best_team_time

    # Écriture des équipes dans un fichier texte
    with open(output_file, 'w') as output:
        for team in teams:
            output.write(" ".join(map(str, [int(athlete[0]) for athlete in team])) + " \n")

    return min_best_team_time, max_worst_team_time, time_difference

# Fichier contenant les données des athlètes
input_file = "data5.txt"

# Fichier de sortie pour les compositions d'équipes
output_file = "relay_teams.txt"

# Taille des équipes
num_athletes_per_team = 128

# Construction des équipes et écriture dans le fichier de sortie
min_best_team_time, max_worst_team_time, time_difference = build_relay_teams(input_file, num_athletes_per_team, output_file)

# Affichage du temps minimum de la meilleure équipe et du temps maximum de la pire équipe
print("Temps minimum de la meilleure équipe :", min_best_team_time)
print("Temps maximum de la pire équipe :", max_worst_team_time)

# Affichage de la différence de temps entre la meilleure équipe et la dernière
print("Différence de temps :", time_difference)