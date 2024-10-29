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
    '.': '.O...O',
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
    if len(sys.argv) <= 1:
        print("Please provide input text or braille.")
        return

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
        if b == table['cap']:
            is_cap = True
        elif b == table['num']:
            is_num = not is_num
        elif b == table[' ']:
            out += ' '
        elif is_cap and b in reversed:
            out += reversed[b].upper()
            is_cap = False
        elif is_num and b in reversed_num:
            out += reversed_num.get(b, '') 
        elif b in reversed:
            out += reversed[b]
        else:
            out += '?'
    return out

def to_braille(txt):
    out = ''
    is_num = False
    for c in txt:
        if c.isdigit():
            if not is_num:
                out += table['num']
                is_num = True
            out += num[c]
        else:
            if is_num:
                is_num = False
            if c.isalpha():
                if c.isupper():
                    out += table['cap'] + table[c.lower()]
                else:
                    out += table[c]
            elif c in table:
                out += table[c]
    return out

if __name__ == '__main__':
    main()