import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from src.hasher import hash_password, identify_hash
from src.brute_force import brute_force
from src.dictionary import dictionary_attack
from src.rainbow import rainbow_lookup, build_rainbow_table

def main():
    parser = argparse.ArgumentParser(
        description='Password Cracker — brute force, dictionary attack, rainbow tables',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  Hash a password:
    python main.py --hash password123 --algorithm sha256

  Brute force:
    python main.py --crack 5f4dcc3b5aa765d61d8327deb882cf99 --method brute --algorithm md5

  Dictionary attack:
    python main.py --crack <hash> --method dictionary --wordlist wordlists/common.txt

  Build rainbow table:
    python main.py --build-rainbow --wordlist wordlists/common.txt

  Rainbow lookup:
    python main.py --crack <hash> --method rainbow
        '''
    )

    parser.add_argument('--hash', type=str, help='Hash a password')
    parser.add_argument('--algorithm', type=str, default='sha256',
                        choices=['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'],
                        help='Hash algorithm (default: sha256)')
    parser.add_argument('--crack', type=str, help='Hash to crack')
    parser.add_argument('--method', type=str, choices=['brute', 'dictionary', 'rainbow'],
                        help='Attack method')
    parser.add_argument('--wordlist', type=str, help='Path to wordlist file')
    parser.add_argument('--max-length', type=int, default=4, help='Max length for brute force (default: 4)')
    parser.add_argument('--build-rainbow', action='store_true', help='Build rainbow table from wordlist')
    parser.add_argument('--identify', type=str, help='Identify hash type')

    args = parser.parse_args()

    if args.hash:
        result = hash_password(args.hash, args.algorithm)
        print(f"\n[+] Password: {args.hash}")
        print(f"[+] Algorithm: {args.algorithm}")
        print(f"[+] Hash: {result}\n")

    elif args.identify:
        algo = identify_hash(args.identify)
        print(f"\n[+] Hash: {args.identify}")
        print(f"[+] Likely algorithm: {algo}\n")

    elif args.build_rainbow:
        if not args.wordlist:
            print("[-] Please provide a wordlist with --wordlist")
            sys.exit(1)
        build_rainbow_table(args.wordlist)

    elif args.crack:
        target = args.crack
        algo = identify_hash(target)
        print(f"\n[*] Target hash: {target}")
        print(f"[*] Detected algorithm: {algo}\n")

        if args.method == 'brute':
            brute_force(target, algo, max_length=args.max_length)
        elif args.method == 'dictionary':
            if not args.wordlist:
                print("[-] Please provide a wordlist with --wordlist")
                sys.exit(1)
            dictionary_attack(target, algo, args.wordlist)
        elif args.method == 'rainbow':
            rainbow_lookup(target)
        else:
            print("[-] Please specify a method: --method brute/dictionary/rainbow")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()