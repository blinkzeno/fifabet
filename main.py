import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connexion à la base de données SQLite
conn = sqlite3.connect('fifa_predictions.db')
cursor = conn.cursor()

# Fonction pour ajouter une équipe
def add_team():
    team_name = team_name_entry.get()
    cursor.execute('INSERT INTO Teams (team_name) VALUES (?)', (team_name,))
    conn.commit()
    messagebox.showinfo("Succès", "Équipe ajoutée avec succès!")
    team_name_entry.delete(0, tk.END)

# Fonction pour ajouter un match
def add_match():
    home_team_id = int(home_team_id_entry.get())
    away_team_id = int(away_team_id_entry.get())
    home_score = int(home_score_entry.get())
    away_score = int(away_score_entry.get())
    match_date = match_date_entry.get()
    cursor.execute('INSERT INTO Matches (home_team_id, away_team_id, home_score, away_score, match_date) VALUES (?, ?, ?, ?, ?)',
                   (home_team_id, away_team_id, home_score, away_score, match_date))
    conn.commit()
    messagebox.showinfo("Succès", "Match ajouté avec succès!")
    home_team_id_entry.delete(0, tk.END)
    away_team_id_entry.delete(0, tk.END)
    home_score_entry.delete(0, tk.END)
    away_score_entry.delete(0, tk.END)
    match_date_entry.delete(0, tk.END)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Application de Prédiction de Buts FIFA")

# Section pour ajouter une équipe
tk.Label(root, text="Nom de l'équipe").grid(row=0, column=0)
team_name_entry = tk.Entry(root)
team_name_entry.grid(row=0, column=1)
tk.Button(root, text="Ajouter Équipe", command=add_team).grid(row=0, column=2)

# Section pour ajouter un match
tk.Label(root, text="ID de l'équipe à domicile").grid(row=1, column=0)
home_team_id_entry = tk.Entry(root)
home_team_id_entry.grid(row=1, column=1)

tk.Label(root, text="ID de l'équipe en déplacement").grid(row=2, column=0)
away_team_id_entry = tk.Entry(root)
away_team_id_entry.grid(row=2, column=1)

tk.Label(root, text="Score de l'équipe à domicile").grid(row=3, column=0)
home_score_entry = tk.Entry(root)
home_score_entry.grid(row=3, column=1)

tk.Label(root, text="Score de l'équipe en déplacement").grid(row=4, column=0)
away_score_entry = tk.Entry(root)
away_score_entry.grid(row=4, column=1)

tk.Label(root, text="Date du match (AAAA-MM-JJ)").grid(row=5, column=0)
match_date_entry = tk.Entry(root)
match_date_entry.grid(row=5, column=1)

tk.Button(root, text="Ajouter Match", command=add_match).grid(row=6, column=1)

# Lancement de la boucle principale de Tkinter
root.mainloop()

# Fermeture de la connexion à la base de données
conn.close()
