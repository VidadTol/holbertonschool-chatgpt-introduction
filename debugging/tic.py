def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérification des lignes pour un gagnant
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes pour un gagnant
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales pour un gagnant
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board):
        print_board(board)
        
        # Demande de la ligne avec validation
        while True:
            try:
                row = int(input(f"Entrez la ligne (0, 1 ou 2) pour le joueur {player}: "))
                if row < 0 or row > 2:
                    print("La ligne doit être entre 0 et 2. Essayez encore.")
                else:
                    break
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier entre 0 et 2.")
        
        # Demande de la colonne avec validation
        while True:
            try:
                col = int(input(f"Entrez la colonne (0, 1 ou 2) pour le joueur {player}: "))
                if col < 0 or col > 2:
                    print("La colonne doit être entre 0 et 2. Essayez encore.")
                else:
                    break
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier entre 0 et 2.")

        # Vérifie si la case est vide et effectue le coup
        if board[row][col] == " ":
            board[row][col] = player
            # Changer de joueur après un coup valide
            player = "O" if player == "X" else "X"
        else:
            print("Cette case est déjà occupée ! Essayez encore.")

    print_board(board)
    # Le dernier joueur qui a joué perd, donc on affiche l'autre joueur comme gagnant
    winner = "O" if player == "X" else "X"
    print(f"Le joueur {winner} a gagné !")

tic_tac_toe()

