import adivinhacao
import forca
import tictactoe

print("********************************")
print("* PyGames - by Rafhael Andrade *")
print("********************************")
print("Escolha um jogo: ")
print("1 - Adivinhação")
print("2 - Forca")
print("3 - Jogo da Velha (Tic-Tac-Toe)")
print("0 - Escolha zero para sair")

selected_game = input("Escolha um jogo: ")

games = {
    "1": adivinhacao,
    "2": forca,
    "3": tictactoe
}

games.get(selected_game).jogar() if games.get(selected_game) else None
