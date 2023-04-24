#Margarita Chistiakova
# 4/19/2023
# Palindrome Check

def palindrome_check(phrase):
  # convert the phrase to lower case
  phrase = phrase.strip()
  if len(phrase) < 2:
    return "The word is a palindrome"
  elif phrase[0] != phrase[-1]:
    return "The word is not a palindrome"
  #strip the phrase
  #check to see if the string phrase is a palindrome
  else:
    return palindrome_check(phrase[1:-1])
    
#strip first and last character
# return palindrome_cheeck(modified phrase)
choice = 0
while choice != 2:
  #continue main program
  print("""\nPlease choose an option from the menu below:
  1. Check if the word or a phrase is a palindrome
  2. Quit the program""")
  choice = int(input("> "))
  if choice == 1:
    print("You can enter a phrase and I will tell you if it is a palindrome!")
    phrase = input("Please enter a string to check: ")
    phrase = phrase.lower()
    result = palindrome_check(phrase)
    print(result)
  else: 
    print("Thank you for taking part in my program 'Palindrome Check'!Bye!")