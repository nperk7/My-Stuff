__author__ = 'naperkins'
def make_word(words):
    result = ""
    for i in words:
        result += i
    return result
def encr(plain):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-',
                '[', ']', '!', '.', ',', "'", '"', '?', ';', ':', '%', '$', '#', '(', ')', '{', '}', '^', '&', '*', '=',
                '+', '_', '<', '>', '|']
    encrypted = ''
    for a in plain:
        alpha = make_word(alphabet)
        c = alpha.find(a) + 1
        b = plain.find(a)
        if plain[b] == ' ' or plain[b] == '\n' or plain[b] == '\r':
            encrypted += a
        if a in alphabet:
            a = 89 - c
            encrypted += alphabet[a]
    return encrypted