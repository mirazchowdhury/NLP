"""
You own a Goal Parser that can interpret a string command.
The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
The interpreted strings are then concatenated in the original order.


Given the string command, return the Goal Parser's interpretation of command.

"G", "()" "(al)"
"G" as the string "G"
"()" as the string "o"
"(al)" as the string "al"

"G()(al)" --->  "Goal"
"G()()()()(al)" --->  "Gooooal"
"(al)G(al)()()G" ---> "alGalooG"




"""

def interpret(command):
    return command.replace("()","o").replace("(al)","al")



print(interpret("(al)G(al)()()G"))
print(interpret("(al)G(al)()()()()()()()()(al)G"))

        