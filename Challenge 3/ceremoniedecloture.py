# On sépare les entrées et les sorties dans deux fichiers différents que l'on trie en ordre croissant
def separate_entries_exits(input_file, entries_file, exits_file):
    # Dictionnaires pour stocker les timestamps d'entrée et de sortie
    entry_timestamps = {}
    exit_timestamps = {}

    # Lecture du fichier et stockage des données dans les dictionnaires
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        athlete_id, entry, exit = line.strip().split(',')
        entry_timestamps.setdefault(int(entry), []).append((int(athlete_id), int(exit)))
        exit_timestamps.setdefault(int(exit), []).append((int(athlete_id), int(entry)))

    # Tri des timestamps d'entrée et de sortie par ordre croissant
    sorted_entry_timestamps = sorted(entry_timestamps.items())
    sorted_exit_timestamps = sorted(exit_timestamps.items())

    # Écriture des timestamps triés dans les fichiers d'entrées et de sorties
    with open(entries_file, 'w') as entries:
        for timestamp, athletes in sorted_entry_timestamps:
            for athlete, exit_time in athletes:
                entries.write(f"{athlete},{timestamp},{exit_time}\n")

    with open(exits_file, 'w') as exits:
        for timestamp, athletes in sorted_exit_timestamps:
            for athlete, entry_time in athletes:
                exits.write(f"{athlete},{timestamp},{entry_time}\n")

def findMaxGuests(entries_file, exits_file):
    with open(entries_file, 'r') as file:
        arrl = [line.strip() for line in file]
    with open(exits_file, 'r') as file:
        exit = [line.strip() for line in file]
    
    n = len(arrl)

    guests_in = 1
    max_guests = 1
    time = arrl[0]
    i = 1
    j = 0
 
    while (i < n and j < n):
         
        if (arrl[i] <= exit[j]):
            guests_in = guests_in + 1
            if(guests_in > max_guests):
         
                max_guests = guests_in
                time = arrl[i]
    
            i = i + 1 
     
        else:
            guests_in = guests_in - 1
            j = j + 1
     
    print("Maximum Number of Guests =",
           max_guests, "at time", time)

separate_entries_exits("data.txt", "entries.txt", "exits.txt")
# findMaxGuests("entries.txt", "exits.txt")