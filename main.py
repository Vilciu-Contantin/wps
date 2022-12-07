import random

piatra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

hartie = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

foarfeca = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

imagini = [piatra, hartie, foarfeca]
alegere_user = int(input("Ce doresti sa alegi:\n0 - piatra, 1 - hartie, 2 - foarfeca\n"))

if(alegere_user >= 0 and alegere_user <= 2):
  print(f"Alegerea utilizatorului:\n{imagini[alegere_user]}")

  alegere_computer = random.randint(0, 2)
  print(f"Alegerea computerului:\n{imagini[alegere_computer]}")

  if alegere_user == 0 and alegere_computer == 2:
    print("Ati castigat")
  elif alegere_computer == 0 and alegere_user == 2:
    print("Ati pierdut")
  elif alegere_computer > alegere_user:
    print("Ati pierdut")
  elif alegere_user > alegere_computer:
    print("Ati castigat")
  elif alegere_computer == alegere_user:
    print("Este remiza")
  
else:
  print("Ati ales un numar gresit, ati pierdut!")