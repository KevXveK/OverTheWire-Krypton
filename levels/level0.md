```
                                                            
_|_|_|      _|_|      _|_|_|  _|_|_|_|    _|_|_|  _|  _|    
_|    _|  _|    _|  _|        _|        _|        _|  _|    
_|_|_|    _|_|_|_|    _|_|    _|_|_|    _|_|_|    _|_|_|_|  
_|    _|  _|    _|        _|  _|        _|    _|      _|    
_|_|_|    _|    _|  _|_|_|    _|_|_|_|    _|_|        _|    
                                                            
```

# Level 0 → 1

**Goal:** `krypton1` (the file inside `krypton0`'s home directory) holds the password for the next level, encoded as base64.

## What I did

```
echo "S1JZUFRPTklTR1JFQVQ=" | base64 -d
```

`-d` decodes instead of encoding. One command, plain text password out:

## Takeaway

First level in the wargame, and it's here to make a point before anything gets hard: base64 is an *encoding*, not encryption. It's not trying to hide anything, it's just representing bytes in a text-safe alphabet — reversible by anyone with the right one-liner. Worth remembering for later levels too: the fact that something looks garbled doesn't mean it's protected.

**Password for next level encoded with base64:** `S1JZUFRPTklTR1JFQVQ=`