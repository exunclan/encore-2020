from enigma.machine import EnigmaMachine
from itertools import permutations

c = 'pogaekucczigdsgwkvb'

roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']

combos = permutations(roman_numerals, 3)

n = 1
for (i, j, k) in combos:
    rotor_choice = 'Gamma {} {} {}'.format(i, j, k)

    machine = EnigmaMachine.from_key_sheet(
        rotors=rotor_choice,
        reflector='C-Thin',
        ring_settings='4 9 3 20',
        plugboard_settings='en cr ys it al xh wd'
    )

    machine.set_display('BENE')

    m = machine.process_text(c)

    print([i, j, k], n, m)

    if 'encore'.upper() in m:
        print("FOUND FOUND FOUND")
        break

    n += 1
