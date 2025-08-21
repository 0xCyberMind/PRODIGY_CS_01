def caesar(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

msg = input("Message: ")
shift = int(input("Shift: "))
choice = input("Encrypt or Decrypt (e/d): ").lower()

if choice == "e":
    print("Encrypted:", caesar(msg, shift))
else:
    print("Decrypted:", caesar(msg, shift, True))
