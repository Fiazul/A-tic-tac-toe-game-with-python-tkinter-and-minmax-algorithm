import tkinter as tk

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

player = "X"
game_over = False

root = tk.Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")


def set_pvp_mode():
    global frame
    global player
    frame.destroy()
    pvp_button.destroy()
    pve_button.destroy()

    global label
    label = tk.Label(root, text=player + " Starts first", font=("Helvetica", 24))
    label.pack()

    frame = tk.Frame(root)
    frame.pack()

    draw_board()


def set_pve_mode():
    global frame
    global player
    frame.destroy()
    pvp_button.destroy()
    pve_button.destroy()

    global label
    label = tk.Label(root, text=player + " Starts first", font=("Helvetica", 24))
    label.pack()

    frame = tk.Frame(root)
    frame.pack()

    draw_board_player()


frame = tk.Frame(root)
frame.pack()
frame.place(relx=.5, rely=.5, anchor=tk.CENTER)

pvp_button = tk.Button(frame, text="PvP", width=12, height=6, bd=8, font=32, command=set_pve_mode)

pve_button = tk.Button(frame, text="PvE", width=12, height=6, bd=8, font=32, command=set_pvp_mode)
pve_button.grid()
pvp_button.grid()


def draw_board():
    for i in range(9):
        button = tk.Button(frame, text=board[i], width=12, height=6, bd=8, font=32,
                           command=lambda idx=i: make_move(idx))
        button.grid(row=i // 3 + 1, column=i % 3)


def draw_board_player():
    for i in range(9):
        button = tk.Button(frame, text=board[i], width=12, height=6, bd=8, font=32,
                           command=lambda idx=i: make_move_player(idx))
        button.grid(row=i // 3 + 1, column=i % 3)


def winner():
    # row
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] and board[i + 1] == board[i + 2] and board[i] != " ":
            return True
    # column
    for i in range(3):
        if board[i] == board[i + 3] and board[i + 3] == board[i + 6] and board[i] != " ":
            return True

    # diagonal
    if board[0] == board[4] and board[4] == board[8] and board[0] != " ":
        return True

    if board[2] == board[4] and board[4] == board[6] and board[2] != " ":
        return True

    return False


def tie():
    for i in range(9):
        if board[i] == " ":
            return False
    return True


def make_move_player(idx):
    global player, game_over

    if board[idx] == " " and not game_over:
        board[idx] = player
        draw_board_player()

        if player == "X" and not winner():
            player = "O"

        elif player == "O" and not winner():
            player = "X"
        label.config(text=player + "'s turn", font=("Helvetica", 24))

        if winner():
            label.config(text=player + " wins!")
            game_over = True

        elif tie():
            label.config(text="Draw!!")
            game_over = True


def make_move(idx):
    global player, game_over

    if board[idx] == " " and not game_over:
        board[idx] = player
        draw_board()

        if player == "X" and not winner():
            player = "O"

        elif player == "O" and not winner():
            player = "X"
        label.config(text=player + "'s turn", font=("Helvetica", 24))

        if winner():
            label.config(text=player + " wins!")
            game_over = True

        elif tie():
            label.config(text="Draw!!")
            game_over = True

        if player == "O" and not game_over:
            label.config(text="Computer thinking...", font=("Helvetica", 24))
            root.update()
            idx = get_best_move()
            board[idx] = "O"
            draw_board()

            if winner():
                label.config(text="Computer wins!", font=("Helvetica", 24))
                game_over = True
            elif tie():
                label.config(text="Draw!!", font=("Helvetica", 24))
                game_over = True
            else:
                player = "X"
                label.config(text=player + "'s turn", font=("Helvetica", 24))


def get_best_move():
    best_score = float('-inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    return best_move


def minimax(board, depth, is_maximizing):
    if winner():
        if is_maximizing:
            return -1
        else:
            return 1
    elif tie():
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


root.mainloop()
