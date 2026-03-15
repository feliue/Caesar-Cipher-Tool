"""
==============================================
  Caesar Cipher Tool
  Author: Abdulhakeem Umar Toyin
  GitHub: github.com/feliue
  Description: A cryptography tool that encodes
               and decodes messages using the
               Caesar cipher with brute force
               decryption capability
==============================================
"""

import string
import time


# ── COLOUR CODES ──────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
PURPLE = "\033[95m"
WHITE  = "\033[97m"
BOLD   = "\033[1m"
RESET  = "\033[0m"


# ── BANNER ────────────────────────────────────────────────────────────────────
def banner():
    print(f"""
{CYAN}{BOLD}
   ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗
  ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
  ██║     ███████║█████╗  ███████╗███████║██████╔╝
  ██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
  ╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
   ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
{RESET}
{PURPLE}{BOLD}   ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗
  ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
  ██║     ██║██████╔╝███████║█████╗  ██████╔╝
  ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
  ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
   ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{RESET}

{WHITE}  Author : {GREEN}Abdulhakeem Umar Toyin{RESET}
{WHITE}  GitHub : {CYAN}github.com/feliue{RESET}
{WHITE}  Tool   : {YELLOW}Caesar Cipher Tool v1.0{RESET}
  {'─'*55}
""")


# ── CORE CAESAR CIPHER ────────────────────────────────────────────────────────
def caesar_cipher(text, shift, mode='encode'):
    """
    Encode or decode text using Caesar cipher.
    Only shifts letters — numbers, spaces, symbols stay the same.
    """
    result = []
    shift  = shift % 26  # Normalize shift to 0-25

    if mode == 'decode':
        shift = -shift  # Reverse the shift for decoding

    for char in text:
        if char.isalpha():
            # Determine base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around with modulo 26
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            # Keep non-letter characters unchanged
            result.append(char)

    return ''.join(result)


# ── BRUTE FORCE ───────────────────────────────────────────────────────────────
def brute_force(ciphertext):
    """
    Try all 25 possible shifts and display results.
    Used when we don't know the shift key.
    """
    print(f"\n  {YELLOW}{BOLD}BRUTE FORCE — Trying all 25 shifts:{RESET}\n")
    print(f"  {'SHIFT':<8} {'DECRYPTED TEXT'}")
    print(f"  {'─'*8} {'─'*50}")

    results = []
    for shift in range(1, 26):
        decrypted = caesar_cipher(ciphertext, shift, mode='decode')
        results.append((shift, decrypted))

        # Highlight likely English text
        score = score_text(decrypted)
        if score > 0.7:
            print(f"  {GREEN}{BOLD}{shift:<8}{RESET} {GREEN}{decrypted}{RESET}  ← {YELLOW}Likely match!{RESET}")
        else:
            print(f"  {CYAN}{shift:<8}{RESET} {WHITE}{decrypted}{RESET}")

    return results


# ── TEXT SCORER (detects likely English) ─────────────────────────────────────
def score_text(text):
    """
    Score text based on common English letter frequency.
    Higher score = more likely to be English.
    """
    common_letters = set('etaoinshrdlcumwfgypbvkjxqz')
    letters_only   = [c.lower() for c in text if c.isalpha()]

    if not letters_only:
        return 0

    common_count = sum(1 for c in letters_only if c in common_letters)
    return common_count / len(letters_only)


# ── FREQUENCY ANALYSIS ────────────────────────────────────────────────────────
def frequency_analysis(text):
    """
    Analyze letter frequency in the ciphertext.
    The most frequent letter is likely 'E' in English.
    """
    letters_only = [c.lower() for c in text if c.isalpha()]

    if not letters_only:
        print(f"\n  {RED}No letters found in text.{RESET}")
        return

    # Count frequency
    freq = {}
    for char in letters_only:
        freq[char] = freq.get(char, 0) + 1

    # Sort by frequency
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    total       = len(letters_only)

    print(f"\n  {YELLOW}{BOLD}FREQUENCY ANALYSIS:{RESET}")
    print(f"  {WHITE}Most common letter in English: {GREEN}E{RESET}")
    print(f"  {WHITE}Most common letter in your text: {GREEN}{sorted_freq[0][0].upper()}{RESET}\n")

    # Suggest likely shift
    most_common = sorted_freq[0][0]
    likely_shift = (ord(most_common) - ord('e')) % 26
    print(f"  {GREEN}[+]{RESET} Suggested shift key: {CYAN}{BOLD}{likely_shift}{RESET}")
    print(f"  {GREEN}[+]{RESET} Try decoding with shift {likely_shift}:\n")
    print(f"  {WHITE}{caesar_cipher(text, likely_shift, 'decode')}{RESET}\n")

    # Show frequency table
    print(f"\n  {'LETTER':<10} {'COUNT':<8} {'FREQUENCY':<12} BAR")
    print(f"  {'─'*10} {'─'*8} {'─'*12} {'─'*30}")
    for char, count in sorted_freq[:10]:
        pct = count / total * 100
        bar = "█" * int(pct / 2)
        print(f"  {GREEN}{char.upper():<10}{RESET} {WHITE}{count:<8}{RESET} {CYAN}{pct:>6.1f}%{RESET}      {YELLOW}{bar}{RESET}")


# ── ENCODE MENU ───────────────────────────────────────────────────────────────
def encode_menu():
    print(f"\n  {CYAN}{'─'*55}{RESET}")
    print(f"  {BOLD}{WHITE}ENCODE A MESSAGE{RESET}")
    print(f"  {CYAN}{'─'*55}{RESET}\n")

    message = input(f"  {CYAN}Enter message to encode:{RESET} ").strip()
    if not message:
        print(f"  {RED}No message entered.{RESET}")
        return

    while True:
        try:
            shift = int(input(f"  {CYAN}Enter shift key (1-25):{RESET} ").strip())
            if 1 <= shift <= 25:
                break
            print(f"  {YELLOW}Please enter a number between 1 and 25.{RESET}")
        except ValueError:
            print(f"  {YELLOW}Invalid input. Enter a number.{RESET}")

    encoded = caesar_cipher(message, shift, 'encode')

    print(f"\n  {GREEN}{'─'*55}{RESET}")
    print(f"  {WHITE}Original  :{RESET} {message}")
    print(f"  {WHITE}Shift Key :{RESET} {CYAN}{shift}{RESET}")
    print(f"  {GREEN}Encoded   :{RESET} {BOLD}{encoded}{RESET}")
    print(f"  {GREEN}{'─'*55}{RESET}\n")

    # Show how each letter was shifted
    show_detail = input(f"  {CYAN}Show detailed shift table? (y/n):{RESET} ").strip().lower()
    if show_detail == 'y':
        print(f"\n  {'ORIGINAL':<12} {'SHIFTED':<12} {'CHANGE'}")
        print(f"  {'─'*12} {'─'*12} {'─'*20}")
        for orig, enc in zip(message, encoded):
            if orig.isalpha():
                print(f"  {WHITE}{orig:<12}{RESET} {GREEN}{enc:<12}{RESET} {CYAN}{orig} → {enc} (+{shift}){RESET}")
        print()


# ── DECODE MENU ───────────────────────────────────────────────────────────────
def decode_menu():
    print(f"\n  {CYAN}{'─'*55}{RESET}")
    print(f"  {BOLD}{WHITE}DECODE A MESSAGE{RESET}")
    print(f"  {CYAN}{'─'*55}{RESET}\n")

    message = input(f"  {CYAN}Enter message to decode:{RESET} ").strip()
    if not message:
        print(f"  {RED}No message entered.{RESET}")
        return

    print(f"\n  {YELLOW}Do you know the shift key?{RESET}")
    print(f"  {WHITE}[1]{RESET} Yes, I know the key")
    print(f"  {WHITE}[2]{RESET} No — brute force all 25 shifts")
    print(f"  {WHITE}[3]{RESET} No — use frequency analysis")

    choice = input(f"\n  {CYAN}Choose (1-3):{RESET} ").strip()

    if choice == '1':
        while True:
            try:
                shift = int(input(f"  {CYAN}Enter shift key (1-25):{RESET} ").strip())
                if 1 <= shift <= 25:
                    break
                print(f"  {YELLOW}Please enter a number between 1 and 25.{RESET}")
            except ValueError:
                print(f"  {YELLOW}Invalid input. Enter a number.{RESET}")

        decoded = caesar_cipher(message, shift, 'decode')
        print(f"\n  {GREEN}{'─'*55}{RESET}")
        print(f"  {WHITE}Encoded   :{RESET} {message}")
        print(f"  {WHITE}Shift Key :{RESET} {CYAN}{shift}{RESET}")
        print(f"  {GREEN}Decoded   :{RESET} {BOLD}{decoded}{RESET}")
        print(f"  {GREEN}{'─'*55}{RESET}\n")

    elif choice == '2':
        brute_force(message)

    elif choice == '3':
        frequency_analysis(message)

    else:
        print(f"  {RED}Invalid choice.{RESET}")


# ── CHALLENGE MODE ────────────────────────────────────────────────────────────
CHALLENGES = [
    {"cipher": "Khoor Zruog",        "shift": 3,  "plain": "Hello World"},
    {"cipher": "Gur dhvpx oebja sbk", "shift": 13, "plain": "The quick brown fox"},
    {"cipher": "Zhofrph wr Vhfxulwb", "shift": 3,  "plain": "Welcome to Security"},
    {"cipher": "Furvwdolqh",          "shift": 3,  "plain": "Crystalline"},
    {"cipher": "Wpcs yi qofmuzs",     "shift": 8,  "plain": "Love is patient"},
]

def challenge_mode():
    print(f"\n  {PURPLE}{BOLD}{'─'*55}{RESET}")
    print(f"  {BOLD}{WHITE}🎯 CHALLENGE MODE — Can you crack it?{RESET}")
    print(f"  {PURPLE}{BOLD}{'─'*55}{RESET}\n")

    import random
    challenge = random.choice(CHALLENGES)
    ciphertext = challenge["cipher"]
    answer     = challenge["plain"].lower()
    shift      = challenge["shift"]

    print(f"  {WHITE}Crack this ciphertext:{RESET}")
    print(f"  {CYAN}{BOLD}  {ciphertext}{RESET}\n")
    print(f"  {YELLOW}Hint: Use brute force or frequency analysis!{RESET}\n")

    attempts = 0
    while attempts < 3:
        guess = input(f"  {CYAN}Your answer (attempt {attempts+1}/3):{RESET} ").strip().lower()
        if guess == answer:
            print(f"\n  {GREEN}{BOLD}🎉 Correct! Well done!{RESET}")
            print(f"  {WHITE}The shift key was: {CYAN}{shift}{RESET}")
            print(f"  {WHITE}Plaintext was    : {GREEN}{challenge['plain']}{RESET}\n")
            return
        else:
            attempts += 1
            remaining = 3 - attempts
            if remaining > 0:
                print(f"  {RED}Wrong! {remaining} attempt(s) left.{RESET}")
                if remaining == 1:
                    print(f"  {YELLOW}Hint: The shift is {shift}{RESET}")

    print(f"\n  {RED}Out of attempts!{RESET}")
    print(f"  {WHITE}The answer was: {GREEN}{challenge['plain']}{RESET}")
    print(f"  {WHITE}Shift key was : {CYAN}{shift}{RESET}\n")


# ── HISTORY LESSON ────────────────────────────────────────────────────────────
def history():
    print(f"""
  {YELLOW}{BOLD}📜 HISTORY OF THE CAESAR CIPHER{RESET}

  {WHITE}The Caesar cipher is one of the oldest known encryption
  techniques, named after {GREEN}Julius Caesar{WHITE} who used it to
  protect his military communications around {CYAN}58 BC{WHITE}.

  How it works:
  Each letter in the message is shifted by a fixed number
  of positions in the alphabet.

  Example with shift 3:
  {CYAN}A → D,  B → E,  C → F,  Z → C{RESET}

  {WHITE}Caesar reportedly used a shift of {CYAN}3{WHITE} for his messages.

  {YELLOW}Is it secure today?{RESET}
  {RED}No!{RESET} {WHITE}With only 25 possible keys, a computer can crack
  it in milliseconds. Modern encryption uses keys with
  billions of possible combinations (AES-256).

  {WHITE}But it's a perfect starting point to understand:{RESET}
  {GREEN}✓{WHITE} How encryption works
  {GREEN}✓{WHITE} The concept of keys
  {GREEN}✓{WHITE} Why longer keys = more security
  {GREEN}✓{WHITE} Frequency analysis attacks
""")


# ── MAIN MENU ─────────────────────────────────────────────────────────────────
def main():
    banner()

    while True:
        print(f"  {BOLD}{WHITE}MAIN MENU{RESET}")
        print(f"  {'─'*40}")
        print(f"  {WHITE}[1]{RESET} 🔒 Encode a message")
        print(f"  {WHITE}[2]{RESET} 🔓 Decode a message")
        print(f"  {WHITE}[3]{RESET} 💥 Brute force cipher")
        print(f"  {WHITE}[4]{RESET} 📊 Frequency analysis")
        print(f"  {WHITE}[5]{RESET} 🎯 Challenge mode")
        print(f"  {WHITE}[6]{RESET} 📜 History of Caesar cipher")
        print(f"  {WHITE}[7]{RESET} ❌ Exit")
        print(f"  {'─'*40}")

        choice = input(f"\n  {CYAN}Choose option (1-7):{RESET} ").strip()

        if choice == '1':
            encode_menu()
        elif choice == '2':
            decode_menu()
        elif choice == '3':
            print(f"\n  {CYAN}{'─'*55}{RESET}")
            print(f"  {BOLD}{WHITE}BRUTE FORCE DECODER{RESET}")
            print(f"  {CYAN}{'─'*55}{RESET}\n")
            msg = input(f"  {CYAN}Enter ciphertext to brute force:{RESET} ").strip()
            if msg:
                brute_force(msg)
        elif choice == '4':
            print(f"\n  {CYAN}{'─'*55}{RESET}")
            print(f"  {BOLD}{WHITE}FREQUENCY ANALYSIS{RESET}")
            print(f"  {CYAN}{'─'*55}{RESET}\n")
            msg = input(f"  {CYAN}Enter ciphertext to analyze:{RESET} ").strip()
            if msg:
                frequency_analysis(msg)
        elif choice == '5':
            challenge_mode()
        elif choice == '6':
            history()
        elif choice == '7':
            print(f"\n  {GREEN}Thanks for using Caesar Cipher Tool. Stay curious! 🔐{RESET}\n")
            break
        else:
            print(f"\n  {RED}Invalid option. Please choose 1-7.{RESET}\n")


if __name__ == "__main__":
    main()
