from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
num_user_moves = 0
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)
# print(stacks)

#Set up the Game
num_disk = int(input("\nHow many disks do you want to play with?\n"))
while num_disk <= 3:
  num_disk = int(input("Enter a number greater than or equal to 3\n"))
  break
for disk in range(num_disk, 0, -1):
  left_stack.push(disk)
num_optimal_moves = 2**num_disk - 1
print("\nThe fastest you can solve this game is in {num} moves".format(num = num_optimal_moves))
#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {let} for {n}".format(let=letter, n=name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
#Play the Game
while(right_stack.get_size() != num_disk):
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack == 0:
      print("\n\nInvalid Move. Try Again.")
    elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
  print("\n\nYou completed the game in {num} moves, and the optimal number of moves is {nom}".format(num=num_user_moves, nom=num_optimal_moves))
