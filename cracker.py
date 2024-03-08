import hashlib

def crackhash(hash_func, input_hash):
    hash_algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }

    try:
        with open('wordlist.txt', 'r') as passFile:
            for password in passFile:
                password = password.strip()  # Remove leading/trailing whitespace
                digest = hash_algorithms[hash_func](password.encode()).hexdigest()
                if digest == input_hash:
                    print("Success: Password found -", password)
                    return  # Found the password, so exit the function
        print("Password not found in the wordlist.")
    except FileNotFoundError:
        print("Error: Wordlist file not found.")
    except KeyError:
        print("Error: Invalid hash function.")

if __name__ == '__main__':
    hash_func_input = input("Enter the hash function (md5, sha1, sha256, sha512): ").lower()
    hash_input = input("Enter the hash to crack: ")
    crackhash(hash_func_input, hash_input)
