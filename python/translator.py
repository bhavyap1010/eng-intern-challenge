import sys

table = {
    'a': 'O.....',
    'b': 'O.O...',
    'c': 'OO....',
    'd': 'OO.O..',
    'e': 'O..O..',
    'f': 'OOO...',
    'g': 'OOOO..',
    'h': 'O.OO..',
    'i': '.OO...',
    'j': '.OOO..',
    'k': 'O...O.',
    'l': 'O.O.O.',
    'm': 'OO..O.',
    'n': 'OO.OO.',
    'o': 'O..OO.',
    'p': 'OOO.O.',
    'q': 'OOOOO.',
    'r': 'O.OOO.',
    's': '.OO.O.',
    't': '.OOOO.',
    'u': 'O...OO',
    'v': 'O.O.OO',
    'w': '.OOO.O',
    'x': 'OO..OO',
    'y': 'OO.OOO',
    'z': 'O..OOO',
    'cap': '.....O',
    '.': '.O...O',
    'num': '.O.OOO',
    '.': '..OO.O',
    ',': '..O....',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    ' ': '......',
    '(': 'O.O..O',
    ')': '.O.OO.',
}

num = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..',
    '<': '.OO..O',
    '>': 'O..OO.',
}

reversed = {v: k for k, v in table.items()}
reversed_num = {v: k for k, v in num.items()}


def main():
    txt = sys.argv[1]

    if is_braille(txt):
        print(to_english(txt))
    else:
        txt = ' '.join(sys.argv[1:])
        print(to_braille(txt))

def is_braille(txt):
    for c in txt:
        if c not in ['O', '.']:
            return False
    return True

def to_english(txt):

    brailles = [txt[i:i+6] for i in range(0, len(txt), 6)]

    out = ""

    is_cap = False
    is_num = False
    for b in brailles:
        if b in reversed:
            if b == table['cap']:
                is_cap = True
            elif b == table['num']:
                is_num = not is_num
            elif is_cap:
                out += reversed[b].upper()
                is_cap = False
            elif is_num:
                out += reversed_num[b]
            else:
                out += reversed[b]

    return out

def to_braille(txt):
    out = ''
    for c in txt:
        if c in table:
            out += table[c]
        elif c.lower() in table and c.isalpha() and c.isupper():
            out += table['cap'] + table[c.lower()]
        elif c in num:
            out += table['num'] + num[c]
                
    return out
        

if __name__ == '__main__':
    main()