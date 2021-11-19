last_player = "O"
winner = None


def print_board(board_map):
    print("""
    _{}_|_{}_|_{}_
    _{}_|_{}_|_{}_
    _{}_|_{}_|_{}_
    """.format(board_map.get(1),
               board_map.get(2),
               board_map.get(3),
               board_map.get(4),
               board_map.get(5),
               board_map.get(6),
               board_map.get(7),
               board_map.get(8),
               board_map.get(9)))


def parse_player(player):
    return str(player).rjust(3, player)


def check_combinations(board_map, player):
    def win_by_rows():
        r1 = board_map.get(1) + board_map.get(2) + board_map.get(3)
        r2 = board_map.get(4) + board_map.get(5) + board_map.get(6)
        r3 = board_map.get(7) + board_map.get(8) + board_map.get(9)
        return parse_player(player) in [r1, r2, r3]

    def win_by_columns():
        c1 = board_map.get(1) + board_map.get(4) + board_map.get(7)
        c2 = board_map.get(2) + board_map.get(5) + board_map.get(8)
        c3 = board_map.get(3) + board_map.get(6) + board_map.get(9)
        return parse_player(player) in [c1, c2, c3]

    def win_by_diagonals():
        d1 = board_map.get(1) + board_map.get(5) + board_map.get(9)
        d2 = board_map.get(3) + board_map.get(5) + board_map.get(7)
        return parse_player(player) in [d1, d2]

    global winner
    winner = player if win_by_rows() or win_by_columns() or win_by_diagonals() else None


def get_current_player():
    global last_player
    next_player = "X" if last_player == "O" else "O"
    last_player = next_player
    return next_player


def jogar():
    print("***************************")
    print("* PyGames - Jogo da Velha *")
    print("***************************\n")
    print("Jogador 1 - X")
    print("Jogador 2 - O")

    board_map = {
        1: "_",
        2: "_",
        3: "_",
        4: "_",
        5: "_",
        6: "_",
        7: "_",
        8: "_",
        9: "_",
    }

    print_board(board_map)

    for i in range(1, 10):
        current_player = get_current_player()
        player_choice = int(input("Jogador {} escolha uma posição entre 1 e 9: ".format(current_player)))
        board_map[player_choice] = current_player
        print_board(board_map)
        check_combinations(board_map, current_player)
        if winner is not None:
            print("Vencedor: ", current_player)
            break


if __name__ == "__main__":
    jogar()
