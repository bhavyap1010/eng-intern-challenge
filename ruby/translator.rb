TABLE = {
    'a' => 'O.....',
    'b' => 'O.O...',
    'c' => 'OO....',
    'd' => 'OO.O..',
    'e' => 'O..O..',
    'f' => 'OOO...',
    'g' => 'OOOO..',
    'h' => 'O.OO..',
    'i' => '.OO...',
    'j' => '.OOO..',
    'k' => 'O...O.',
    'l' => 'O.O.O.',
    'm' => 'OO..O.',
    'n' => 'OO.OO.',
    'o' => 'O..OO.',
    'p' => 'OOO.O.',
    'q' => 'OOOOO.',
    'r' => 'O.OOO.',
    's' => '.OO.O.',
    't' => '.OOOO.',
    'u' => 'O...OO',
    'v' => 'O.O.OO',
    'w' => '.OOO.O',
    'x' => 'OO..OO',
    'y' => 'OO.OOO',
    'z' => 'O..OOO',
    'cap' => '.....O',
    'NUM' => '.O.OOO',
    '.' => '..OO.O',
    ',' => '..O....',
    '?' => '..O.OO',
    '!' => '..OOO.',
    ':' => '..OO..',
    ';' => '..O.O.',
    '-' => '....OO',
    '/' => '.O..O.',
    ' ' => '......',
    '(' => 'O.O..O',
    ')' => '.O.OO.'
}

NUM = {
    '.' => '.O...O',
    '1' => 'O.....',
    '2' => 'O.O...',
    '3' => 'OO....',
    '4' => 'OO.O..',
    '5' => 'O..O..',
    '6' => 'OOO...',
    '7' => 'OOOO..',
    '8' => 'O.OO..',
    '9' => '.OO...',
    '0' => '.OOO..',
    '<' => '.OO..O',
    '>' => 'O..OO.'
}

REVERSED = TABLE.invert
REVERSED_NUM = NUM.invert

def main
    if ARGV.empty?
        puts "Please provide input text or braille."
        return
    end

    txt = ARGV[0]

    if is_braille(txt)
        puts to_english(txt)
    else
        txt = ARGV.join(' ')
        puts to_braille(txt)
    end
end

def is_braille(txt)
    txt.chars.all? { |c| ['O', '.'].include?(c) }
end

def to_english(txt)
    brailles = txt.chars.each_slice(6).map(&:join)
    out = ""
    is_cap = false
    is_NUM = false

    brailles.each do |b|
        if b == TABLE['cap']
            is_cap = true
        elsif b == TABLE['NUM']
            is_NUM = !is_NUM
        elsif b == TABLE[' ']
            out += ' '
        elsif is_cap && REVERSED[b]
            out += REVERSED[b].upcase
            is_cap = false
        elsif is_NUM && REVERSED_NUM[b]
            out += REVERSED_NUM[b]
        elsif REVERSED[b]
            out += REVERSED[b]
        else
            out += '?'
        end
    end
    out
end

def to_braille(txt)
    out = ""
    is_NUM = false

    txt.each_char do |c|
        if c =~ /\d/
        out += TABLE['NUM'] if !is_NUM
        is_NUM = true
        out += NUM[c]
        else
        is_NUM = false
            if c =~ /[A-Z]/
                out += TABLE['cap'] + TABLE[c.downcase]
            elsif TABLE[c]
                out += TABLE[c]
            end
        end
    end
    out
end

if __FILE__ == $0
    main
end