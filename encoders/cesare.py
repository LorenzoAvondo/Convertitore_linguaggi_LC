def encode(text: str, shift: int) -> str:
    """
    Tradurre nel cifrario di Cesare vuol dire spostare le lettere di 
    tot lettere nell'alfabetp (3 default usato da Cesare )
    a -> D 
    """
    result = []
    for char in text:
        if char.isalpha():
            # SE È MAIUSCOLA -> usa 'A' come base (65)
            if char.isupper():
                base = ord('A')
            # ALTRIMENTI (È MINUSCOLA) -> usa 'a' come base (97)
            else:
                base = ord('a')
                
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)


def decode(text: str, shift: int) -> str:
    """Decodifica un testo cifrato con il cifrario di Cesare."""
    return encode(text, -shift)
    
