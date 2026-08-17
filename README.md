# Password Cracker

A password cracking tool built with Python that demonstrates three attack techniques: brute force, dictionary attack, and rainbow table lookup. Shows why weak passwords are dangerous and how attackers crack credentials.

## Features

- Hash generator — hash any password with MD5, SHA1, SHA224, SHA256, SHA384, SHA512
- Hash identifier — automatically detects the algorithm from hash length
- Brute force attack — tries all possible character combinations using itertools
- Dictionary attack — tests passwords from a wordlist against the target hash
- Rainbow table — pre-computes hashes for instant lookup
- Clean CLI interface — built with argparse, progress updates every 100k attempts

## Results

| Attack | Target | Password | Attempts |
|--------|--------|----------|----------|
| Dictionary | MD5 hash | password | 2 |
| Brute force | MD5 hash | ab | 38 |

## Project Structure

    password-cracker/
    ├── src/
    │   ├── hasher.py        # Hash generation and identification
    │   ├── brute_force.py   # Brute force attack engine
    │   ├── dictionary.py    # Dictionary attack engine
    │   └── rainbow.py       # Rainbow table build and lookup
    ├── wordlists/
    │   └── common.txt       # Sample wordlist
    └── main.py              # CLI entry point

## Installation

    git clone https://github.com/Stavros-Saridis/password-cracker.git
    cd password-cracker
    python -m venv venv
    venv\Scripts\activate

## Usage

Hash a password:

    python main.py --hash password123 --algorithm sha256

Identify hash type:

    python main.py --identify 5f4dcc3b5aa765d61d8327deb882cf99

Dictionary attack:

    python main.py --crack 5f4dcc3b5aa765d61d8327deb882cf99 --method dictionary --wordlist wordlists\common.txt

Brute force attack:

    python main.py --crack 5f4dcc3b5aa765d61d8327deb882cf99 --method brute --max-length 6

Build rainbow table:

    python main.py --build-rainbow --wordlist wordlists\common.txt

Rainbow lookup:

    python main.py --crack 5f4dcc3b5aa765d61d8327deb882cf99 --method rainbow

## Why This Matters

This tool demonstrates why password security matters. A 2-character password takes 38 brute force attempts. A 6-character password takes ~2.2 billion. Adding uppercase letters, numbers, and symbols multiplies the search space exponentially — making brute force practically impossible. Dictionary attacks show why common passwords like "password" or "123456" are instantly cracked.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| hashlib | Built-in hash generation |
| itertools | Brute force combinations |
| argparse | CLI interface |

## Author

Stavros Saridis — BSc Computer Science (First Class Honours), University of Derby
MSc Cybersecurity student | Aspiring SOC Analyst
GitHub: https://github.com/Stavros-Saridis
LinkedIn: https://linkedin.com/in/stavros-saridis