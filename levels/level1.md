```
                                                
_|_|_|      _|_|    _|_|_|_|_|    _|  _|_|_|    
_|    _|  _|    _|      _|      _|_|        _|  
_|_|_|    _|    _|      _|        _|    _|_|    
_|    _|  _|    _|      _|        _|        _|  
_|    _|    _|_|        _|        _|  _|_|_|    
                                                
```

# Level 1 → 2

**Goal:** `krypton2` (the file inside `krypton1`'s home directory) holds the password for the next level, run through ROT13.

## What I did

ROT13 is a Caesar cipher with the shift fixed at 13. `tr` can do the whole substitution in one shot by mapping the normal alphabet onto itself shifted 13 places:

```
cat /krypton/krypton1/krypton2 | tr "A-Za-z" "N-ZA-Mn-za-m"
```

```
raw     = YRIRY GJB CNFFJBEQ EBGGRA
```

## Takeaway

The fixed shift of 13 is exactly half of the 26-letter alphabet, which is what makes ROT13 its own inverse — shift by 13 twice and you're back where you started (13 + 13 = 26). That's why the identical `tr` command both encodes and decodes it. It's a neat property, but it's also why ROT13 shows up more as an "obfuscate this spoiler" convention than as anything resembling real security — the same one-liner breaks it either direction.

**Password for next level encoded with base64:** `TEVWRUwgVFdPIFBBU1NXT1JEIFJPVFRFTg==`