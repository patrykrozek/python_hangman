def get_select_level():
  # Słownik zawierający poziomy trudności i odpowiadające im ilości żyć
  levels = {
      "easy": 5,
      "medium": 3,
      "hard": 1
  }

  # Wyświetlanie dostępnych poziomów
  print("Available difficulty levels:")
  for level in levels.keys():
      print(level)

  # Wprowadzenie przez użytkownika poziomu trudności
  difficult_level = input("Type your difficult level: ").lower()  # Zamieniamy na małe litery dla spójności

  # Sprawdzenie czy wybrany poziom znajduje się w słowniku
  if difficult_level in levels:
      print(f"Chosen {difficult_level} difficulty stage.")
      number_of_lives = levels[difficult_level]  # Pobranie ilości żyć na podstawie klucza
  else:
      print("Chosen difficulty level not found, defaulting to easy.")
      number_of_lives = levels["easy"]  # Domyślnie ustawiamy ilość żyć na poziomie łatwym

  MSG_INPUT_WORD = "Please input the word for your friend to guess: "
  word = input(MSG_INPUT_WORD)
  tab_of_letters = list(word)

  # Zwracamy wyniki jako listę
  return [number_of_lives, tab_of_letters]

def get_score(tab_of_letters,score):
   if "." in tab_of_letters:
      score += 1
      print(f"Your score: {score}pkt")
      return score

def score_saver(score):
    with open('score.txt','r') as file:
       best_score = file.read()
    if score > int(best_score):
      with open('score.txt','w') as file:
        file.write(str(score))

def score_printer():
   with open('score.txt','r') as file:
      return file.read()



def start_game(tab_of_letters, number_of_lives):
    guess_tab = []
    score = 0
    num_of_letters = len(tab_of_letters)
    for i in range(len(tab_of_letters)):
        guess_tab.append("_")

    while number_of_lives > 0 and num_of_letters > 0:
        letter_flag_guess = 0
        guess = input("Guess the letter: ")
        for index, char in enumerate(tab_of_letters):
            if char == guess:

                guess_tab[index] = char
                tab_of_letters[index] = "."
                letter_flag_guess = 1
                num_of_letters = num_of_letters -1
                print(f'You guessed {char}, which has {index} index, you have {num_of_letters} letters  and  {number_of_lives} lifes left')
                score = get_score(tab_of_letters,score)

        if not letter_flag_guess:
            number_of_lives = number_of_lives -1
            print(f'Try again, you have: {number_of_lives} lives left')
        print(f'\n--------------------------\n\n{guess_tab}\n\n--------------------------') 


    score_saver(score)

stage_choose = "Choose difficult level easy,medium,hard."
difficult_stage_easy ="Selected level have five lives."
difficult_stage_med ="Selected level have three lives."
difficult_stage_hard = "Selected level have one lives."


print("\nWelcome in Hangman\n")
print(f'Last best score: {score_printer()}')
results = get_select_level()
number_of_lives = results[0]
tab_of_letters = results[1]
start_game(tab_of_letters,number_of_lives)
print("You finished the game")