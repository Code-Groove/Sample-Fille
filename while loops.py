#While Loops: Execute a blockk of code mutiple times:
guess_count=1
while guess_count<=5:
    print('*' * guess_count)
    guess_count= guess_count + 1
print("Task done")




#CAR GAME USING WHILE LOOP:
command=""
while True:
    command = input("> ")
    if command.lower()=="start":
        print("Car started....Vroom Vroom!!")
    if command.lower()== "start again":
        print("Don't trouble the trouble if you trouble the trouble, the trouble troubles you! I'm not the trouble, I'm the truth!, I'm the truth, I'm the truth!")
    elif command.lower()=="stop":
        print("Car has stopped😯😯")
    elif command.lower()== "stop again":
        print("Dabidi Dibide!")
    elif command== "help":
        print(""" 
Start- To start the car
Stop- To stop the car
Quit- To quit the game
                  """)

    elif command.lower()=="quit":
        break
    else:
        print("Sorry, I don't understand that!")







