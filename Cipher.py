from art import text2art

logo = text2art("balu")
print(logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original, shift, direction):
    cipher_txt = ""
    shift_amount = shift
    if direction == "decode":
        shift_amount *= -1
    for letter in original:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_txt += alphabet[shifted_position]
        else:
            cipher_txt += letter
    print(f"Here is the {direction} text: {cipher_txt}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' or 'decode':\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))
    
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again, otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("goodbye")
