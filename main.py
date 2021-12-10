# We import the random module
# On importe le module random
import random

# same for string
# Pareil pour string

import string

# We initialize the variable to zero
# On créer une variable password_len et on l'initialise à zéro
password_len = 0

# We try to convert the value of input to int if this does not work, an error message is displayed
# On essaie de convertir la valeur de input en int si cela ne marche pas affiche un message d'erreur
try:
    password_len = int(input("Choissisez la longeur du mot de passe : "))
except:
    print("Erreur vous devez rentrer un chiffre correct")

# Generate the password with numbers and letters
# On génére le mot de passe avec des lettres et des chiffres
character = string.ascii_letters + string.digits
passwords = ''.join(random.choice(character) for i in range(password_len))
print("Mot de passe : ", passwords)
