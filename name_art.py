#Name Art Programme

from art import text2art

def name_art():
    name = input("Enter your name: ")
    art = text2art(name)
    print(art)
    
# Run the programme

name_art()
