import sqlite3

# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect('fifa_predictions.db')
cursor = conn.cursor()

# Création de la table Teams
cursor.execute('''
CREATE TABLE IF NOT EXISTS Teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL
)
''')

# Création de la table Matches
cursor.execute('''
CREATE TABLE IF NOT EXISTS Matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    home_team_id INTEGER,
    away_team_id INTEGER,
    home_score INTEGER,
    away_score INTEGER,
    match_date DATE,
    FOREIGN KEY (home_team_id) REFERENCES Teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES Teams(team_id)
)
''')

# Création de la table Predictions
cursor.execute('''
CREATE TABLE IF NOT EXISTS Predictions (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER,
    total_goals REAL,
    FOREIGN KEY (match_id) REFERENCES Matches(match_id)
)
''')

# Validation des changements et fermeture de la connexion
conn.commit()
conn.close()

print("Base de données et tables créées avec succès.")
