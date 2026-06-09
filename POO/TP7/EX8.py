"""
1. On dispose de : ["A","B","C","D","E","F"]
2. Tous les 3 joueurs, un joueur est éliminé.
3. Trouver le survivant.
"""

players = ["A","B","C","D","E","F"]
while len(players) > 1:
    eliminated = players[2]  # Every 3rd player is eliminated
    print(f"Eliminated: {eliminated}")
    players.remove(eliminated)
print(f"Survivor: {players[0]}")    
