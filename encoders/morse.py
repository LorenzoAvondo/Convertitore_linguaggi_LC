# Dizionario Morse corretto
morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/"  # aggiunta opzionale per gli spazi
}

def encode(text: str) -> str:
    """
    Traduce il testo in codice Morse.
    Tra le lettere c'è uno spazio, tra le parole c'è '/'.
    """
    text = text.upper()
    morse_words = []

    # Ciclo sulle parole del testo
    for word in text.split(" "):
        morse_letters = []

        # Ciclo sulle lettere della parola
        for char in word:
            morse_letters.append(morse.get(char, ""))  # qui metti il Morse

        # Unisce le lettere della parola con uno spazio
        morse_words.append(' '.join(morse_letters))

    # Unisce le parole con '/'
    return ' / '.join(morse_words)
