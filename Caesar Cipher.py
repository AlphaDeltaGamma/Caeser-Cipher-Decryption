alphabets="abcdefghijklmnopqrstuvwxyz"
string_input=input("enter your message:")
key=int(input("enter your key:")
n=len(string_input)
string_output=""
for i in range(n):
     character=string_input[i]
     location=alphabets.find(character)
     new_location=(location+key)%26
     string_output+=alphabets(new_location)
print(string_output)     
     
     
     
     
