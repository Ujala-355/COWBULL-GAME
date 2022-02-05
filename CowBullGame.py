import random
def play():
    n=[0,1,2,3,4,5,6,7,8,9]
    a=random.sample(n,3)
    print(a)
    chance=10
    cow=[]
    bull=[]
    for i in range(chance):
        if bull==a:
                print("You are the winner!!")
                play_again=input("Do you want to play Again!!!if yes then type 'y'/'n':")
                if play_again=="y":
                    play()
                else:
                    print("Thanks for playing!!")
                    break
        choice=int(input("enter a guess number:"))
        position=int(input("enter a position number:"))
        for j in range(len(a)):
            if choice in a:
                if a[j] in a and a.index(choice)==position:
                    bull.insert(position,choice)
                    print("Bull No:",bull)
                    break
                else:
                    cow.insert(position,choice)
                    print("Cow NO:",cow)
                    break
            elif choice not in a:
                print("You number is not exist in secret list!")
                break
    print("Your chances are finished now!!")
play()