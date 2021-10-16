#Create a dictionary with questions and answers 
import random
#Example 
#format
d = {
  1:["", ""],
  2:["", ""],
}

def sportquestion():
  dictionary = {
    1:["Who won the NBA championship in 2021?\n A. Lakers \n B. Bucks \n C. Suns \n D. Clippers", ""],

    2:["How many Super Bowls has Tom Brady won? \n A. 6 \n B. 4\nC. 3 \n D. 5", ""],

    3: ["How many players are used in a baseball game? \n A. 10 \n B. 7 \n C. 9 \n D. 8", ""],

    4: ["How many seconds are their on a shot clock for basketball? \n A. 22 \n B. 30 \n C. 28 \n D. 24", ""],

    5: ["How many sets are volleyball games played up to? \n A. 5 \n B. 10 \n C. 13 \n D. 12", ""],

    6: ["How many world titles has Lionel Messi won? \n A. 35"]
  }

  return dictionary[random.randint(1,6)]



  