import hashlib
import itertools
import string
import time


def hash_password(password, algorithm):
    password = password.encode()

    if algorithm == "md5":
        return hashlib.md5(password).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(password).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(password).hexdigest()
    else:
        raise ValueError("Nepodržan algoritam")



def brute_force(target_hash, max_length, algorithm):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()

    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            password = ''.join(attempt)
            attempts += 1

            if hash_password(password, algorithm) == target_hash:
                elapsed = time.time() - start_time
                print("---------------------------")
                print(f"\n[+] Password pronađen: {password}")
                print(f"[i] Pokušaja: {attempts}")
                print(f"[i] Vrijeme: {elapsed:.2f} sekundi")
                print("---------------------------")
                return


            if attempts % 10000 == 0:
                print(f"[i] Pokušaja: {attempts}", end="\r")

    print("\n[-] Password nije pronađen")



def dictionary_attack(target_hash, wordlist, algorithm):
    attempts = 0
    start_time = time.time()

    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                password = line.strip()
                attempts += 1

                if hash_password(password, algorithm) == target_hash:
                    elapsed = time.time() - start_time
                    print(f"\n[+] Password pronađen: {password}")
                    print(f"[i] Pokušaja: {attempts}")
                    print(f"[i] Vrijeme: {elapsed:.2f} sekundi")
                    return

                if attempts % 5000 == 0:
                    print(f"[i] Pokušaja: {attempts}", end="\r")

    except FileNotFoundError:
        print("[-] Wordlist file nije pronađen")
        return

    print("\n[-] Password nije pronađen")



def main():
    print("==== PASSWORD CRACKER ====")
    print("1. Brute Force")
    print("2. Dictionary Attack")

    choice = input("Odaberi opciju: ").strip()
    target_hash = input("Unesi hash: ").strip().lower()
    algorithm = input("Algoritam (md5/sha1/sha256): ").strip().lower()

    if choice == "1":
        max_length = int(input("Maksimalna duljina passworda: "))
        brute_force(target_hash, max_length, algorithm)

    elif choice == "2":
        wordlist = input("Putanja do wordlist file-a: ")
        dictionary_attack(target_hash, wordlist, algorithm)

    else:
        print("[-] Nepoznata opcija")


if __name__ == "__main__":
    main()