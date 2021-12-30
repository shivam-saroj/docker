import random
choices=['rock','paper','scissor']
computer=random.choice(choices)
#print(computer)
player=None
while player not in choices:
    player=input('rock,paper or scissor:')
if player == computer:
   print('computer:',computer)
   print('player:',player)
   print('Tie')
elif player=='rock':
   if computer=='paper':
      print('computer',computer)
      print('player:', player)
      print('You lose')
   if computer=='scissor':
      print('computer', computer)
      print('player:', player)
      print('You win')

elif player=='scissor':
   if computer=='rock':
      print('computer',computer)
      print('player:', player)
      print('You lose')
   if computer=='paper':
      print('computer:', computer)
      print('player:', player)
      print('You win')

elif player=='paper':
   if computer=='scissor':
      print('computer:',computer)
      print('player:', player)
      print('You lose')
   if computer=='rocks':
      print('computer', computer)
      print('player:', player)
      print('You win')


