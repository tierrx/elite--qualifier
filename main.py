import random
import time
import sys

  
def main():
  
 print("Hello and welcome to chatbot")
 time.sleep(2)

 print("My names skippy!")
 time.sleep(2)

 print("What is your name?")

 name = input()

 print(f'Nice to meet you {name}, what would you like to chat about?')
 time.sleep(1)

 print("I have the options of games, movies, and music.")
 time.sleep(1)

 answer = input('movies, games and music:')
 time.sleep(1)

 if answer == "movies":
  print("what's your favorite movie?")
  answer = input()
  response_list = ['Wow I like that one too!', 'Hmmm, I have  not seen that one yet, I will check it out!', 'Eh not my favorite', 'No taste at all :/', 'one of the best ever made, purrrr']
  print("", random.choice(response_list))
  time.sleep(1)

 if answer == "music":
  print("Would you like to talk about an artist or song?")
  answer = input('artist or song:')
  if answer == "artist":
    print(f'Whos your favorite artist {name}?')
    answer = input()
    response_list = ['Their music is amazing!', 'I bet their music rocks!', 'They literally suck, sorry' , 'No taste at all :/', 'Ooooo, I like your style']
    print("", random.choice(response_list))
    time.sleep(1)
  if answer == "song":
    print("What is your favorite song?")
    answer = input()
    response_list = ['No wayyyyy, me too!', 'Oh uhhh thats cool..... I guess?', 'Ohhhhhhh um I havent heard it yet, Ill check it out', 'You have.... questionable taste..', 'WHAT ARE YOU SERIOUS THATS THE BEST SONG EVER MADE DHBEHDBDC']
    print("", random.choice(response_list))
    time.sleep(1)

 if answer == "games":
  print("Do you prefer video games or mobile games?")
  answer = input()
  response_list = [ 'Same the other choice is terrible','Eh agree to disagree I like the other choice better', 'Hmmm... I dont know I think theyre both great', 'AHHHH see now I like you a lot :)']
  print("", random.choice(response_list))
  time.sleep(1)

 print("Wait finish these lyrics")
 guess_lyircs = input("Walk through fire for you....:")

 correct_lyrics = "just let me adore you"
 if correct_lyrics != guess_lyircs:
   guess_lyircs= input('Not a harry stan I see, what a  shame,"just let me adore you"')
   time.sleep(1)
 
 elif guess_lyircs == correct_lyrics:
    print("Nice youre a harry stan I see ;)")

 print("Okay, Let's move foward")
 time.sleep(1)

 print(f'Would you like to talk about another topic {name}?')
 answer = input('yes or no:')
 time.sleep(1)

 if answer == 'yes':
  print("Thoughts on sports?")
  answer = input()
  response_list = ['Honestly same,I agree', 'No way, your opinion is very false', 'uhhhhhhhhhh no <3, #respectfully', 'hmmmmmmm Im kinda in the middle here', 'No tea, no shade but I think I hate you :)']
  print("", random.choice(response_list))
  time.sleep(2)

 if answer == 'no':
  print("Okay that's fine we can keep going")
  time.sleep(1)

 print("Now for the most important question of the day.........")
 time.sleep(1)
 print("Was your day good?")
 answer = input('yes or no?:')
 if answer == 'yes':
  print("Thats wonderful, I hope us talking made it even better XD")
 if answer == 'no':
  print("oh no :(")
  time.sleep(2)
  print("Well I hope it gets better and that us talking made it a little better")

 print(f'Thanks for chatting with me {name}, Chat with me again sometime soon')
 time.sleep(1)

 print("Bye, Bye XD")

choice = input('Press q to quit, press enter to continue')
if choice == 'q':
    sys.ext(1)

else:
   main()

