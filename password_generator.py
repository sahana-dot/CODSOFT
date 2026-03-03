import secrets
import string

def generate_secure_password(length):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    # Required character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # All possible characters
    all_characters = lowercase + uppercase + digits + symbols

    # Fill the remaining length
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Secure shuffle
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def main():
    print("=======================================")
    print("     SECURE PASSWORD GENERATOR 🔐      ")
    print("=======================================")

    while True:
        try:
            length = int(input("\nEnter desired password length (min 8): "))
            password = generate_secure_password(length)
            print("\nGenerated Secure Password:", password)

        except ValueError as e:
            print("Error:", e)

        again = input("\nGenerate another password? (yes/no): ").lower()
        if again != "yes":
            print("Program closed.")
            break


if __name__ == "__main__":
    main()