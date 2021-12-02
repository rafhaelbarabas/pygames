# import getpass

def print_gibbet(gibbet_dic):
    print(" ______________")
    print("|             |")
    print("|             |")
    print("|            {}".format(gibbet_dic[1]))
    print("|            {}{}{}".format(gibbet_dic[2], gibbet_dic[3], gibbet_dic[4]))
    print("|            {}{}".format(gibbet_dic[5], gibbet_dic[6]))
    print("|            ")
    print("|            ")


def print_answer(answer):
    print("Palavra-chave: ", "".join(answer.values()))


def print_letters(letters):
    print("Letras já informadas: " + ", ".join(letters))


def jogar():
    print("***************************")
    print("* PyGames - Jogo da Forca *")
    print("***************************\n")

    # getpass lib won't work on Pycharm's terminal
    # use your system console to run this app ou change these lines to use simple input method
    # key_word = str.upper(getpass.getpass("Escolha uma palavra para jogar: "))
    key_word = str.upper(input("Escolha uma palavra para jogar: "))

    gibbet_dic = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: ""
    }

    try_dic = {
        1: " Õ",
        2: "/",
        3: "|",
        4: "\\",
        5: "/",
        6: " \\",
    }

    try_count = 0
    max_tries = 6
    answer = {}
    word_length = len(str(key_word))
    letters_template = {}
    already_input = []

    for i in range(0, word_length):
        letters_template[i] = "{}".format(key_word[i])
        answer[i] = " _ "

    print_gibbet(gibbet_dic)
    print_answer(answer)

    while True:
        user_letter = str.upper(input("Informe uma letra: "))
        template_values = letters_template.values()
        if user_letter in already_input:
            print("A letra {} já foi informada, tente outra...".format(user_letter))
            print_letters(already_input)
            continue
        if user_letter in template_values:
            for i in range(0, len(template_values)):
                if letters_template[i] == user_letter:
                    answer[i] = user_letter
        else:
            try_count = try_count + 1
            if try_count > max_tries:
                print_gibbet(gibbet_dic)
                print("As tentativas acabaram, a palavra era: ", key_word)
                break
            gibbet_dic[try_count] = try_dic[try_count]
        already_input.append(user_letter)
        print_gibbet(gibbet_dic)
        print_answer(answer)
        print_letters(already_input)

        if "".join(answer.values()) == key_word:
            print("Você encontrou a palavra!")
            break


if __name__ == "__main__":
    jogar()

# TODO List
# Validar palavras com espaços em branco e outros caracteres especiais e já inseri-los na resposta para facilitar.
# Validar entrada do usuário, caso ele digite mais de uma letra.
# considerar acerto uma sequencia de palavras ou a palavra inteira.
# Por exemplo - Palavra-chave = notebook
# Se o usuário digitar "not", deve preencher "N O T _ _ _ _ _"
# Mas se ele digitar "noty", será considerado um erro na forca. Pois contará como um chute da palavra completa.
