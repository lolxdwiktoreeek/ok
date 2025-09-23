meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "SYBAU": 'Żartobliwy sposób powiedzenia "zamknij się"',
            "RIZZ": "Skrót od słowa charyzma",
            "REL": "Skrót od angielskiego słowa relatable, oznaczającego 'możliwe do powiązania'",
            "RELL": "Skrót od angielskiego słowa relatable, oznaczającego 'możliwe do powiązania'",
            }

word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Przepraszam, nie ma takiego słowa w tym słowniku")
