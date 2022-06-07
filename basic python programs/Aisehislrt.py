a = 123

print("let's play a game, guess the 3 digit number")



for i in range(5):
    b = int(input("try here : "))
    if a == b :
        print("boom!! you guessed it right!")
        print("it took you ",i+1," tries to guess correct")
        break
    elif a-b < 20 or b-a < 20 :
        print("you are near try little hard")
        print("you have only ",4-i," chances left")
    else :
        print("too far try something different")
        print("you have only ", 4 - i, " chances left")
else:
    print("ran out of lives")
