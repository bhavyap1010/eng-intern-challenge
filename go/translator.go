package main

import (
    "fmt"
    "os"
    "strings"
)

var table = map[rune]string{
    'a': "O.....",
    'b': "O.O...",
    'c': "OO....",
    'd': "OO.O..",
    'e': "O..O..",
    'f': "OOO...",
    'g': "OOOO..",
    'h': "O.OO..",
    'i': ".OO...",
    'j': ".OOO..",
    'k': "O...O.",
    'l': "O.O.O.",
    'm': "OO..O.",
    'n': "OO.OO.",
    'o': "O..OO.",
    'p': "OOO.O.",
    'q': "OOOOO.",
    'r': "O.OOO.",
    's': ".OO.O.",
    't': ".OOOO.",
    'u': "O...OO",
    'v': "O.O.OO",
    'w': ".OOO.O",
    'x': "OO..OO",
    'y': "OO.OOO",
    'z': "O..OOO",
    ' ': "......",
    '.': "..OO.O",
    ',': "..O....",
    '?': "..O.OO",
    '!': "..OOO.",
    ':': "..OO..",
    ';': "..O.O.",
    '-': "....OO",
    '/': ".O..O.",
    '(': "O.O..O",
    ')': ".O.OO.",
    'C': ".....O",
    'N': ".O.OOO",
}

var num = map[rune]string{
    '1': "O.....",
    '2': "O.O...",
    '3': "OO....",
    '4': "OO.O..",
    '5': "O..O..",
    '6': "OOO...",
    '7': "OOOO..",
    '8': "O.OO..",
    '9': ".OO...",
    '0': ".OOO..",
    '.': ".O...O",
    '<': ".OO..O",
    '>': "O..OO.",
}

var reversed = make(map[string]rune)
var reversedNum = make(map[string]rune)

func init() {
    for k, v := range table {
        reversed[v] = k
    }
    for k, v := range num {
        reversedNum[v] = k
    }
}

func isBraille(txt string) bool {
    for _, c := range txt {
        if c != 'O' && c != '.' {
            return false
        }
    }
    return true
}

func toEnglish(txt string) string {
    brailles := strings.FieldsFunc(txt, func(r rune) bool { return r == ' ' })
    out := ""
    isCap := false
    isNum := false

    for _, b := range brailles {
        if b == table[' '] {
            out += " "
            continue
        }
        if b == table['C'] {
            isCap = true
            continue
        }
        if b == table['N'] {
            isNum = !isNum
            continue
        }
        
        if val, exists := reversed[b]; exists {
            if isCap {
                out += strings.ToUpper(string(val))
                isCap = false
            } else {
                out += string(val)
            }
        } else if val, exists := reversedNum[b]; exists {
            out += string(val)
        } else {
            out += "?"
        }
    }
    return out
}

func toBraille(txt string) string {
    out := ""
    isNum := false

    for _, c := range txt {
        if c >= '0' && c <= '9' {
            if !isNum {
                out += table['N']
                isNum = true
            }
            out += num[c]
        } else {
            if isNum {
                isNum = false
            }
            if c >= 'A' && c <= 'Z' {
                out += table['C'] + table[rune(c+32)]
            } else {
                out += table[c]
            }
        }
    }
    return out
}

func main() {
    if len(os.Args) <= 1 {
        fmt.Println("Please provide input text or braille.")
        return
    }

    txt := strings.Join(os.Args[1:], " ")

    if isBraille(txt) {
        fmt.Println(toEnglish(txt))
    } else {
        fmt.Println(toBraille(txt))
    }
}