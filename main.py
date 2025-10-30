alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, direction_option):
  output = ""
  if direction_option == "encode":
    a = 1
  elif direction_option == "decode":
    a = -1
  else:
    a = 0
    print("invalid option")
  for letter in original_text:
    if letter in alphabet:
      i = (alphabet.index(letter) + a*shift_amount) % len(alphabet)
      output += alphabet[i]
    else:
      output += letter
  print(f'Here is the {direction_option}d result: {output}')

print("logo")
option = "y"
while option != "n":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar (original_text=text, shift_amount=shift, direction_option=direction)
  option = input("Do you wish to continue? (Y)es or (N)o?").lower()

print("Good bye!")
