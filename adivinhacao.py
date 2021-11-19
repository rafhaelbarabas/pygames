import math
from random import randrange


# Do not cheat, i'm watching you ...
def generate_secret_number():
    return randrange(1, 101)


def is_equals(user_number, secret_number):
    return user_number == secret_number


def is_bigger(user_number, secret_number):
    return user_number > secret_number


def is_smaller(user_number, secret_number):
    return user_number < secret_number


def get_rounds_by_difficulty(difficulty_level):
    choices = {
        "0": math.inf,
        "1": 10,
        "2": 5,
        "3": 3
    }
    return choices.get(difficulty_level, math.inf)


def discount_score(actual_score, value, secret_number):
    return actual_score - abs(secret_number - value) if actual_score >= 0 else 0


def jogar():
    print("*********************************")
    print("* PyGames - Jogo da adivinhação *")
    print("*********************************\n")

    print("* Tente adivinhar o número gerado aleatoriamente entre 1 e 100 - Boa sorte. *")
    print("Você começa com 1000 pontos, e seus pontos são descontados de acordo com a diferença do valor digitado, "
          "em relação ao número secreto")
    print("Escolha a dificuldade: ")
    print("0 - Modo treinamento - Tentativas infinitas - não conta pontuação")
    print("1 - Fácil   - 10 tentativas")
    print("2 - Médio   -  5 tentativas")
    print("3 - Dificil -  3 tentativas")

    secret_number = generate_secret_number()

    round_counter = 1
    result = False

    difficulty = input("Informe a dificulde desejada: ")

    score = 1000
    max_rounds = get_rounds_by_difficulty(difficulty)
    is_training_mode = max_rounds == math.inf

    while not result:
        if round_counter > max_rounds:
            print("As tentativas acabaram... O número secreto era: ", secret_number)
            break
        else:
            print("\nRodada {} de {}".format(round_counter, max_rounds))

        user_number = int(input("Digite o seu número: "))
        discount_value = user_number if not is_training_mode else 0

        print("Valor digitado: {}".format(user_number), sep=": ")
        result = is_equals(user_number, secret_number)

        if user_number not in range(1, 101):
            print("O valor digitado deve estar entre 1 e 100")
            continue

        round_counter = round_counter + 1

        if result:
            print("Acerto mizeravi!")
        else:
            print("Erroooooow!")
            if not is_training_mode:
                score = discount_score(score, discount_value, secret_number)
            if is_bigger(user_number, secret_number):
                print("O número é maior do que o esperado")
            elif is_smaller(user_number, secret_number):
                print("O número é menor do que o esperado")

    print("Sua pontuação foi: ", score)
    print("\n*** Game over ***")


if __name__ == "__main__":
    jogar()
