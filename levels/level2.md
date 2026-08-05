```
                                                            
  _|_|_|    _|_|    _|_|_|_|    _|_|_|    _|_|    _|_|_|    
_|        _|    _|  _|        _|        _|    _|  _|    _|  
_|        _|_|_|_|  _|_|_|      _|_|    _|_|_|_|  _|_|_|    
_|        _|    _|  _|              _|  _|    _|  _|    _|  
  _|_|_|  _|    _|  _|_|_|_|  _|_|_|    _|    _|  _|    _|  
```

# Level 2 → 3

**Goal:** `krypton3` (the file inside `krypton2`'s home directory) holds the password for the next level, run through a Caesar cipher — but this time the shift isn't given, it has to be recovered.

`krypton2`'s home directory also has an `encrypt` executable and a `keyfile.dat` the executable reads to know which shift to apply. Nothing states the shift directly.

## What I did

The plan: feed `encrypt` a string I already know the plaintext of, and compare the output against the input. Whatever shift explains that transformation is the same shift protecting the real password, since both runs read the same keyfile.

```
ABC > MNO   :   shift 14
```

`encrypt` expects its keyfile to sit next to wherever it's invoked from, and I didn't want to touch anything inside `/krypton/krypton2/` directly. So I gave it that file in a throwaway directory instead of the real one:

```
mktemp -d                                            # scratch space
cd /tmp/tmp13ui34                                     # into it
ln -s /krypton/krypton2/keyfile.dat                   # symlink, same filename the binary expects
chmod 777 .                                           # make sure it can write here
/krypton/krypton2/encrypt /krypton/krypton2/krypton3
```

That produced the real ciphertext:

```
raw cyphertext = AYCQYPGQCYQW
```

## Brute-force fallback

Known-plaintext comparison only works when I can get the binary to encrypt something I recognize. When that's not available, trying all 26 possible shifts and reading off whichever one looks like English is basically free — a Caesar cipher only has 26 keys:

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

## Takeaway

Two things worth keeping from this one:

- **Known-plaintext beats brute force when you can get it.** If a program will encrypt something for you on demand, feeding it a string you control tells you the key directly — no guessing needed.
- **`mktemp -d` + `ln -s` is a clean way to satisfy a program's assumptions about its own file layout.** Rather than copying files into place or hoping I have write access where the real ones live, I gave the binary the filename it expected inside a directory I fully control. Same instinct as fake `PATH` entries or `LD_PRELOAD` — work with what the program *expects to find*, not where the real thing happens to live.

**Password for next level encoded with base64:** `Q0FFU0FSSVNFQVNZ`