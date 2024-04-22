import pandas as pd 

def calculate_average_time():
    
    # On importe les données
    data = pd.read_csv('datas.csv', sep=',')

    # Création d'un dictionnaire pour stocker les temps de chaque coureur de chaque pays
    country_times = {}
    country_count = {}

    # On parcourt les lignes du fichier
    for _, row in data.iterrows():
        # On récupère le pays et le temps du coureur
        country = row['pays']
        time = row['temps']

        # On ajoute le temps à la liste des temps du pays
        if country in country_times:
            country_times[country].append(time)
            country_count[country] += 1
        else:
            country_times[country] = [time]
            country_count[country] = 1

    # On calcule la moyenne des temps pour chaque pays
    country_average = {}
    for country in country_times:
        country_average[country] = sum(country_times[country]) / country_count[country]

    winner = min(country_average, key=country_average.get)
    return winner, country_average[winner]

print(calculate_average_time())