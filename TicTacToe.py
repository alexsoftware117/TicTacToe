# Displays an empty board
brd = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Variable to check if the game is still running
game_still_going = True

# Changes to X or O, depending on the winner (or none if a tie)
winner = None

# Starts the current player as X (as per tic tac toe rules)
current_player = "X"

# declares function that displays the board
def display_brd():
  print(brd[0] + " | " + brd[1] + " | " + brd[2])
  print(brd[3] + " | " + brd[4] + " | " + brd[5])
  print(brd[6] + " | " + brd[7] + " | " + brd[8])

# plays the game
def play_game():

  # Displays the initial board
  display_brd()

  # Active while the game is still in progress
  while game_still_going:
    
    # Handles the turn of the current player
    handle_turn(current_player)

    # Checks if the game is over
    check_if_game_over()

    # Flips to the next player
    flip_player()

  # Executed when the game is over and displays the winner
  if winner == "X" or winner == "O":
    print(winner + " won!")
  elif winner == None:
    print("There was a tie!")

# Handles a turn of the current player
def handle_turn(player):
  
  print(player + "'s turn!")
  position = input("Choose a position from 1-9: ")

  # While loop to check for valid or invalid input
  valid = False
  while not valid:

    # Ensures input is between 1-9
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid input, please choose 1-9: ")

    position = int(position) - 1

    # Displays if there is a piece already in the inputed position
    if brd[position] == "-":
      valid = True
    else:
      print("There is an " + brd[position] + " there. Try again!")

  # Sets the position to the player, either X or O
  brd[position] = player

  # Displays the board after the position is picked
  display_brd()

# Checks if the game is over, either through a win or a tie
def check_if_game_over():
  check_if_win()
  check_if_tie()

# Checks if the game has been won
def check_if_win():

  global winner
  # Checks rows for a winning player
  row_winner = check_rows()

  # Checks columns for a winning player
  column_winner = check_columns()

  # Checks diagonals for a winning player
  diagonal_winner = check_diagonals()

  # If row_winner, column_winner, or diagonal_winner set to true,
  # will set winner to X or O
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    # If there are no winners, then the winner will still be none
    winner = None
  return

# checks if row is the same symbol to declare a win
def check_rows():
  # declares the game_still_going global variable
  global game_still_going

  row_1 = brd[0] == brd[1] == brd[2] != "-"
  row_2 = brd[3] == brd[4] == brd[5] != "-"
  row_3 = brd[6] == brd[7] == brd[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False

  # returns the winner, X or O
  if row_1:
    return brd[0]
  elif row_2:
    return brd[3]
  elif row_3:
    return brd[6]
  return

# checks if column is the same symbol to declare a win
def check_columns():
  # declares the game_still_going global variable
  global game_still_going

  col_1 = brd[0] == brd[3] == brd[6] != "-"
  col_2 = brd[1] == brd[4] == brd[7] != "-"
  col_3 = brd[2] == brd[5] == brd[8] != "-"

  if col_1 or col_2 or col_3:
    game_still_going = False

  # returns winner, X or O
  if col_1:
    return brd[0]
  elif col_2:
    return brd[1]
  elif col_3:
    return brd[2]
  return

# checks if diagonal is the same symbol to declare a win
def check_diagonals():

  # declares the game_still_going global variable
  global game_still_going

  diag_1 = brd[0] == brd[4] == brd[8] != "-"
  diag_2 = brd[2] == brd[4] == brd[6] != "-"
  
  if diag_1 or diag_2:
    game_still_going = False

  # returns winner, X or O
  if diag_1:
    return brd[0]
  elif diag_2:
    return brd[2]
  return

# Checks if there is a tie
def check_if_tie():

  # declares the game_still_going global variable
  global game_still_going

  if "-" not in brd:
    game_still_going = False
  return

# Changes the player after each turn
def flip_player():

  # declares the current_player global variable
  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return

# Starts the game when ran
play_game()

