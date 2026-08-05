```
      ___           ___           ___           ___           ___           ___           ___     
     /\__\         /\  \         |\__\         /\  \         /\  \         /\  \         /\__\    
    /:/  /        /::\  \        |:|  |       /::\  \        \:\  \       /::\  \       /::|  |   
   /:/__/        /:/\:\  \       |:|  |      /:/\:\  \        \:\  \     /:/\:\  \     /:|:|  |   
  /::\__\____   /::\~\:\  \      |:|__|__   /::\~\:\  \       /::\  \   /:/  \:\  \   /:/|:|  |__ 
 /:/\:::::\__\ /:/\:\ \:\__\     /::::\__\ /:/\:\ \:\__\     /:/\:\__\ /:/__/ \:\__\ /:/ |:| /\__\
 \/_|:|~~|~    \/_|::\/:/  /    /:/~~/~    \/__\:\/:/  /    /:/  \/__/ \:\  \ /:/  / \/__|:|/:/  /
    |:|  |        |:|::/  /    /:/  /           \::/  /    /:/  /       \:\  /:/  /      |:/:/  / 
    |:|  |        |:|\/__/     \/__/             \/__/     \/__/         \:\/:/  /       |::/  /  
    |:|  |        |:|  |                                                  \::/  /        /:/  /   
     \|__|         \|__|                                                   \/__/         \/__/    
```

# OverTheWire - Krypton

Personal practice log across [OverTheWire](https://overthewire.org/) wargames. Using this as a small portfolio — not a full writeup dump, just short, honest notes on what each challenge asked, how I solved it, and what it taught me.

Solved levels record their password/flag as proof-of-work — these are public, but will be encoding with base64 to avoid spoilers.

## Summary

| Wargame | Status | Notes |
|---------|--------|-------|
| [Krypton](levels/level0.md) | Levels 0–3 in progress | Classical cryptography fundamentals — encoding vs. encryption, substitution ciphers, known-plaintext cryptanalysis |

## Structure

```
.
├── README.md
├── NOTES.md
└── levels/
    ├── level0.md
    ├── level1.md
    └── level2.md
```

## Skills demonstrated

- Telling encoding apart from encryption (base64 is reversible by anyone; a cipher needs a key/shift)
- ROT13 / Caesar substitution via `tr`
- Known-plaintext cryptanalysis — feeding a test string through an unknown cipher to recover its shift, then applying that shift to the real ciphertext
- Working around a program's assumptions about its own file layout with `mktemp -d` and `ln -s`, instead of touching the original files
- Writing a small brute-force script as a fallback when a clean known-plaintext comparison isn't available
- Documenting findings clearly and concisely — a habit that matters more in red teaming than people expect

## Levels

| Level | Challenge | Core skill |
|-------|-----------|------------|
| [0 → 1](levels/level0.md) | Decode a base64 password | `base64 -d` |
| [1 → 2](levels/level1.md) | Decode a ROT13 password | `tr` |
| [2 → 3](levels/level2.md) | Recover an unknown Caesar shift and decode the password | known-plaintext comparison, `mktemp -d`, `ln -s`, brute force |

Krypton keeps going past this into heavier ciphers (Vigenère, XOR, block modes, RSA) — not yet attempted, so not written up here.

## Notes

See [NOTES.md](NOTES.md) for my running annotations — what I did, what tripped me up, what it means for how I'd approach recon later on.

## Setup, if you want to follow along

```
ssh krypton0@krypton.labs.overthewire.org -p 2231
```

Password for level 0 is `krypton0` (publicly given by OverTheWire to get started). Everything after that you earn.

## Setup alias in bashrc

```
krypton() {
    ssh -p 2231 -o ServerAliveInterval=60 "krypton$@krypton.labs.overthewire.org
}
```