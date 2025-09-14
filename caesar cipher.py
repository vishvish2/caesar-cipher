Alphabet = ["a", "b", "c", "d", "e", "f", "g",  "h",  "i",
            "j",  "k",  "l",  "m", "n",  "o",  "p",  "q", "r",
            "s",  "t",  "u",  "v",  "w",  "x",  "y",  "z"]
Capitals = ["A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "I",
            "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Q",  "R",
            "S",  "T",  "U",  "V",  "W",  "X",  "Y",  "Z"]
Cipher_Text = []
Plain_Text = input("Enter some text to encrypt: ")
while Plain_Text.isalpha() is False:
    Plain_Text = input("Enter some text to encrypt: ")
key = int(input("How many places do you want to shift your letters: "))
for letter in range(0, len(Plain_Text)):
    if Plain_Text[letter] in Alphabet:
        position1 = Alphabet.index(Plain_Text[letter])
        new1 = position1 + key
        if new1 >= 26 or new1 <= -26:
            new1 = new1 % 26
        Cipher_Text.append(Alphabet[new1])
    elif Plain_Text[letter] in Capitals:
        position2 = Capitals.index(Plain_Text[letter])
        new2 = position2 + key
        if new2 >= 26 or new2 <= -26:
            new2 = new2 % 26
        Cipher_Text.append(Capitals[new2])

print("".join(Cipher_Text), "is your encrypted text")
