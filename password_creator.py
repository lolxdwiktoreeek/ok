import random

# znaki których może użyć hasło
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890+-/*!&$#?=@"
# pusta lista
password_characters_list = []

# funkcja tworząca te hasło
def password_creator(all_chars, empty):
    length = input("Podaj długość hasła.")
    num = ""
    # zamiana długości hasła na integer
    while not num is int:
        # próba zamiany
        try:
            num = int(length)
            break
        # jeśli się nie uda:
        except:
            print("Przepraszam, ale długość musi być liczbą.")
            length = input("Podaj długość hasła.")
    # generacja hasła
    for i in range(num):
        character = random.choice(all_chars)
        empty.append(character)
    # przygotowanie i wysłanie wygenerowanego hasła
    password = "".join(empty)
    print("Wygenerowane hasło:", password)

# aktywacja funkcji
password_creator(chars, password_characters_list)
