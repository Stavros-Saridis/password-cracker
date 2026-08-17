# Password Cracker

A password cracking tool built with Python demonstrating three attack techniques: brute force, dictionary attack, and rainbow table lookup. Also demonstrates why salting defeats rainbow tables. Educational tool for understanding password security.

## Features

- Hash generator — supports MD5, SHA1, SHA224, SHA256, SHA384, SHA512
- Hash identifier — automatically detects algorithm from hash length
- Brute force attack — tries all character combinations using multiprocessing across all CPU cores
- Dictionary attack — tests passwords from a wordlist against the target hash
- Rainbow table — pre-computes hashes for instant lookup
- Salting demo — shows why salted hashes defeat rainbow table attacks
- 12-core multiprocessing — parallel cracking across all available CPU cores

## Results

| Attack | Target | Password | Result |
|--------|--------|----------|--------|
| Dictionary | MD5 hash | password | Found in 2 attempts |
| Brute force | MD5 hash | ab | Found in 3 seconds (12 cores) |
| Brute force | MD5 hash | Sapes210! | ~18,000 years (CPU) |

## Why Passwords Like "Sapes210!" Are Safe

A 9-character password using uppercase, lowercase, digits and symbols has 94^9 = ~572 quadrillion combinations. At 2 million attempts per second (12-core CPU), cracking it would take ~18,000 years. Even a military-grade GPU (RTX 4090 at 100 billion hashes/sec) would need ~66 days. This is why length and complexity matter.

## Project Structure

    password-cracker/
    ├── src/
    │   ├── hasher.py        # Hash generation, salting, identification
    │   ├── brute_force.py   # Multiprocessing brute force engine
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

Brute force (12 cores):

    python main.py --crack 5f4dcc3b5aa765d61d8327deb882cf99 --method brute --max-length 6

Salting demo:

    python main.py --demo-salt password123

Build rainbow table:

    python main.py --build-rainbow --wordlist wordlists\common.txt

Rainbow lookup:

    python main.py --crack <hash> --method rainbow

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| hashlib | Built-in hash generation |
| itertools | Brute force combinations |
| multiprocessing | Parallel cracking across all CPU cores |
| argparse | CLI interface |

## Author

Stavros Saridis — BSc Computer Science (First Class Honours), University of Derby
MSc Cybersecurity student | Aspiring SOC Analyst
GitHub: https://github.com/Stavros-Saridis
LinkedIn: https://linkedin.com/in/stavros-saridis