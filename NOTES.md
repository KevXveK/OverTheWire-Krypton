# Notes

Annotations as I go — less "here's the solution," more "here's what this taught me."

## Level 0 → 1

First level is base64. Every level directory holds a file named after the *next* level (`krypton0` has a file called `krypton1`, and so on) with that next password encoded or encrypted inside it. Here it was just base64:

```
echo "S1JZUFRPTklTR1JFQVQ=" | base64 -d
```

Straight decode, no key involved. Good level to set the tone for the rest of the wargame: not every "encoded" string is a secret, some of them are just formatted for transport. Base64 is the clearest example — anyone with the `-d` flag can reverse it.

## Level 1 → 2

ROT13 — a Caesar cipher with the shift hardcoded to 13. That fixed shift is what makes it self-inverse: shifting the alphabet by 13 twice gets you back to the start (13 + 13 = 26, a full loop), so the same command decodes and encodes.

```
cat /krypton/krypton1/krypton2 | tr "A-Za-z" "N-ZA-Mn-za-m"
```

Raw Text: `YRIRY GJB CNFFJBEQ EBGGRA` 

`tr` with two matched ranges (`A-Za-z` → `N-ZA-Mn-za-m`) does the whole substitution table in one shot — no need to spell out all 26 letters like I would for an arbitrary Caesar shift.

## Level 2 → 3

The one that actually took effort, and where "cipher" stopped meaning "look up the fixed rule" and started meaning "figure out the key first."

This level gave three things: a file holding the (encrypted) password for level 3, an `encrypt` executable, and a keyfile the executable reads to know its shift. The shift itself isn't published anywhere — I had to recover it.

The idea: feed the executable a string I already know, and compare what it outputs against what I put in. Whatever shift maps my input to that output is the same shift protecting the real password, since it's reading the same keyfile either way.

```
ABC > MNO   :  shift 14
```

Once I had a shift I trusted, decoding the real ciphertext was just applying it:

```
raw cyphertext = AYCQYPGQCYQW
```

Getting the executable to actually run against the target file (rather than my own scratch copy) needed a bit of setup, since it expects to find its keyfile relative to wherever it's invoked from:

```
mktemp -d                                          # scratch space, don't touch the real files
cd /tmp/tmp13ui34
ln -s /krypton/krypton2/keyfile.dat                # symlink named exactly like the file it expects, in my own dir
chmod 777 .                                         # make sure the binary can actually write here
/krypton/krypton2/encrypt /krypton/krypton2/krypton3
```

That symlink trick is the part I'm keeping: instead of copying files around or hoping I have write access to `/krypton/krypton2/`, I gave the binary its expected filename inside a throwaway directory I fully control. Same pattern as `LD_PRELOAD` tricks or fake `PATH` entries — satisfy what a program assumes about its environment without touching the real one.

As a fallback for whenever I don't have a clean before/after pair to compare, I wrote a small brute-force script that just tries all 26 shifts and prints every candidate so I can eyeball which one is readable English:

```python
import string

list_alphabet = string.ascii_uppercase
text_value = input("Type your text: ").upper()
phrase_decoded = []
attempt  = 0
def ceaser_decode(text):
    shift_number = 0
    while len(phrase_decoded) < 26:
        shifted_text = list_alphabet[shift_number:] + list_alphabet[:shift_number]
        map_table = str.maketrans(list_alphabet, shifted_text)
        phrase_decoded.append(text.translate(map_table))
        shift_number += 1
    return phrase_decoded
test_decoded = ceaser_decode(text_value)
while attempt < 26:
    print(f"Cipher number {attempt}: {test_decoded[attempt]} \n")
    attempt += 1
```

Only 26 possible shifts means brute force is basically free — this is the same reason Caesar ciphers are a teaching tool and not real security. Good one to keep in my back pocket for any single-shift substitution where I can't get a known-plaintext sample.

## Running status

- [x] Level 0 → 1
- [x] Level 1 → 2
- [x] Level 2 → 3
- [ ] Level 3 → 4 — not attempted yet