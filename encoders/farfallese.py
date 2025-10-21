def encode(text: str) -> str:
    """
    Traduce in farfallese la regola è che quando c'è una vocale viene aggiunga f + la vocale
    es. Ciao -> Cifiafaofo
    """

    vocali = "aeiouAEIOUàèìòù"
    result = ""

    for char in text:
        if char in vocali:
            result += char + "f" + char.lower()
        else:
            result += char
    return result

def decode(text: str) -> str:
    """ 
    decodifica il farfallese
    """
    vocali = "aeiouAEIOUàèìòù"
    i=0
    result = ""

    while i < len(text):
        char = text[i]
        if(
            char in vocali
            and i + 2 < len(text)
            and text[i + 1] == "f"
            and text[i + 2].lower() == char.lower()
        ):
            result += char
            i += 3
        else:
            result += char
            i += 1
    return result
