import random as rd

def get_word():
    words = ["flecha", "garrafa", "trigger", "carta"]  # get a random word in strings's set
    word = rd.choice(words)
    return word

def play(word):
    print("Inicio de jogo, dica: tamanho da palavra = ", len(word) )
    tries = 0
    aux_word = "_" * len(word)
    input_letters = [] 
    win = 0
    while(tries <= 6) :
        error = True
        # verify error input
        while error:
            # choice letter
            letter = input("Informe uma letra: ")
            if len(letter) != 1:
                print("Entrada inválida")
                error = True
            else:
                error = False
                input_letters.append(letter)
                win = win + 1
        
        # verify if the word contains choice letter
        contains, indexes = find_ocorrences(letter, word)  # return numbers of ocorrences and indexes
        if contains != 0: 
            print("Letra encontrada: ")
            aux_word_list = list(aux_word)
            for i in range(contains):
                aux_word_list[indexes[i]] = input_letters[-1]  # very good gambiarra
            aux_word = "".join(aux_word_list)  # last insert letter  
            print(aux_word)  
        else:
            tries = tries + 1
            stage = display_hangman(tries)
            print(stage)

        if aux_word == word:
            print("Você ganhou !!! ")
            print("A palavra é: ", word )
            tries = 7

def find_ocorrences(letter, word):
    counter = 0
    indexes = []
    for index, l in enumerate(word):
        if letter == l:
            counter = counter + 1
            indexes.append(index)
    return counter, indexes

def display_hangman(tries):
    stages = [  # cabeça, tronco, braços e pernas: morte.
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # cabeça, tronco e braços, perna
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # cabeça, tronco e braços
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # cabeça, tronco e braço
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # cabeça e tronco
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # cabeça
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # vazio
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Jogar de novo? (S/N) ").upper() == "S":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()