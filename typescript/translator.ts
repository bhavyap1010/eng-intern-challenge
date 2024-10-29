const table: { [key: string]: string } = {
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
    ')': '.O.OO.'
};

const num: { [key: string]: string } = {
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
    '>': 'O..OO.'
};

const reversed: { [key: string]: string } = Object.fromEntries(Object.entries(table).map(([k, v]) => [v, k]));
const reversed_num: { [key: string]: string } = Object.fromEntries(Object.entries(num).map(([k, v]) => [v, k]));


function isBraille(txt: string): boolean {
    return txt.split('').every(c => c === 'O' || c === '.');
}

function toEnglish(txt: string): string {
    const brailles = txt.match(/.{1,6}/g) || [];
    let out = '';
    let isCap = false;
    let isNum = false;

    for (let b of brailles) {
        if (b === table['cap']) {
            isCap = true;
        } else if (b === table['num']) {
            isNum = !isNum;
        } else if (b === table[' ']) {
            out += ' ';
        } else if (isCap && reversed[b]) {
            out += reversed[b].toUpperCase();
            isCap = false;
        } else if (isNum && reversed_num[b]) {
            out += reversed_num[b];
        } else if (reversed[b]) {
            out += reversed[b];
        } else {
            out += '?';
        }
    }
    return out;
}

function toBraille(txt: string): string {
    let out = '';
    let isNum = false;

    for (let c of txt) {
        if (/\d/.test(c)) {
            if (!isNum) {
                out += table['num'];
                isNum = true;
            }
            out += num[c];
        } else {
            isNum = false;
            if (/[A-Z]/.test(c)) {
                out += table['cap'] + table[c.toLowerCase()];
            } else if (table[c]) {
                out += table[c];
            }
        }
    }
    return out;
}

function main(): void {
    const args = process.argv.slice(2);

    if (args.length === 0) {
        console.log("Please provide input text or braille.");
        return;
    }

    const txt = args.join(' ');

    if (isBraille(txt)) {
        console.log(toEnglish(txt));
    } else {
        console.log(toBraille(txt));
    }
}

main();
