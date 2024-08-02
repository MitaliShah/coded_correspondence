# decode the following message and print the result. This message has an offset of 10
# xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!

alphabet = "abcdefghijklmnopqrstuvwxyz"

message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!zbx"

translated_message = ""

for character in message:   
  if character in alphabet:
    character_value = alphabet.find(character)
    translated_message += alphabet[(character_value + 10) % 26]    
  else:
    translated_message += character

print(translated_message)