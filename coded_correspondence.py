# Step 1: Decode Message
# decode the following message and print the result. This message has an offset of 10
# xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!


# 26 alphabet as a string
alphabet = "abcdefghijklmnopqrstuvwxyz"

# The message to be translated (encoded with a Caesar cipher)
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!zbx"

# Empty string to hold the translated message
translated_message = ""

for character in message:   
  if character in alphabet:
     # Find the index of the character in the alphabet
    character_value = alphabet.find(character)
    # Shift the character by 10 positions in the alphabet, wrapping around using modulo 26
    translated_message += alphabet[(character_value + 10) % 26]    
  else:
    # If the character is not a letter (e.g., punctuation or space), it stays unchanged
    translated_message += character

print(translated_message)