
def find_min_capacity(input_file):
    # Lecture du fichier et stockage des données dans une liste
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Stockage des timestamps d'entrée et de sortie dans deux listes distinctes
    entries = []
    exits = []

    for line in lines:
        athlete_id, entry, exit = line.strip().split(',')
        entries.append((int(entry), athlete_id))
        exits.append((int(exit), athlete_id))

    # Tri des timestamps d'entrée et de sortie par ordre croissant
    entries.sort()
    exits.sort()

    # Initialisation des compteurs
    max_athletes = 0
    current_athletes = set()
    entry_index = 0
    exit_index = 0

    # Parcours des timestamps pour déterminer le nombre maximal d'athlètes présents simultanément
    while entry_index < len(entries) and exit_index < len(exits):
        entry_time, entry_athlete = entries[entry_index]
        exit_time, exit_athlete = exits[exit_index]

        if entry_time < exit_time:
            current_athletes.add(entry_athlete)
            max_athletes = max(max_athletes, len(current_athletes))
            entry_index += 1
        else:
            current_athletes.remove(exit_athlete)
            exit_index += 1

    return max_athletes

# Utilisation de la fonction
min_capacity = find_min_capacity("data.txt")

# Affichage du résultat
print("La capacité minimale du vestiaire est de :", min_capacity)
