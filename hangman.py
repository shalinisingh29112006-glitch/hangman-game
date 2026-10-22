import random
def Hangman():
    list=["cacophony","technology","privacy","computer","programming",
          "microwave","python","algorithm","function","variable","ubuntu"]         
    stages={
        0: """  
        +--------+
            |    |
                 | 
                 |
                 |
                 |
       ============""",# FOR NO MISTAKE
       1:"""
        +--------+
            |    |
            0    | 
                 |
                 |
                 |
       ============""",
       2:"""
        +--------+
            |    |
            0    | 
            |    |
                 |
                 |
       ============""",
       3:"""
        +--------+
            |    |
            0    | 
           /|    |
                 |
                 |
       ============""",
       4:r"""
        +--------+
            |    |
            0    | 
           /|\   |
                 |
                 |
       ============""",
       5:r"""
        +--------+
            |    |
            0    | 
           /|\   |
           /     |
                 |
       ============""",
       6:r"""
        +--------+
            |    |
            0    | 
           /|\   |
           / \    |
                 |
       ============""",
    }
    word=random.choice(list)
    count=6
    for i in range(0,2):                      #i just want to give the user to guess 2 letters
        if i==0:
            str1=random.randrange(1,int(len(word)/2))   #the place where mystry begins
            mystry_letter1=word[str1]                     #the 1st letter that is going to be missing
            the_word=word.replace(mystry_letter1,"_",1)   #1st mystry
        else:
            
            str2=random.randrange(int(len(word)/2)+1,len(word))    #the place where 2nd mystry begins
            mystry_letter2=word[str2]                     #the 2nd letter that is going to be missing
            if mystry_letter2==mystry_letter1:
                str2=random.randrange(1,len(word))    #the place where mystry begins
                mystry_letter2=word[str2]                     #the letter that is going to be missing
            the_word=the_word.replace(mystry_letter2,"_",1)   #the word with the missing letter

    guessed_letters=[]                                  #list to store guessed letters
    print("||-------------------------------------------------------------||")
    print("||----------------------WELCOME TO HANGMAN---------------------||")
    print("||-------------------------------------------------------------||")
    print("+---------------------------------------------------------------+")
    print("|-----------------------RULES OF THE GAME-----------------------|")
    print("+---------------------------------------------------------------+")
    print("|--------You will be given a word with 2 missing letters--------|")
    print("|----------and you have to guess the letters in 6 chances-------|")
    print("+---------------------------------------------------------------+")
    print("|--When the hangman will be completed, you will lose the game.--|")
    print("|-------You have to guess the letters before that happens-------|")
    print("+---------------------------------------------------------------+")
    print("|-------------------------GOOD LUCK-----------------------------|")
    print(stages[0])
    print("The word is: "+the_word)
    while count>0:                     #i just want to give the user to guess 6 chances
        str=input("Enter the 1st letter: ")
        if str.lower()==mystry_letter1.lower(): 
            print("you guessed 1st letter right")
            for i in range(0,6):
                str2=input("Enter the 2nd letter: ")
                if str2.lower()==mystry_letter2.lower():
                    print("\n    🎉 VICTORY! Player wins the game! 🎉   \n" )
                    return "You guessed it right I can say you are a genius   \n  \n             **VICTORY**"                 
                    
                        
                else:
                    if str2 in guessed_letters:
                        i-=1                        #to give a another chance to user in loop 
                        print("||-------------You have already guessed this letter-------------------||")
                        print("||----------------------please try again------------------------------||")
                        
                    else:
                        guessed_letters.append(str2)
                        count-=1
                        print("||--------------------sorry to disappoint u-------------------||")
                        print("||-------------------but the answer is wrong------------------||")
                        if count==0:
                            i-=1
                            print(stages[6]) 
                            return "The word was: " + word+ "    \n      **defeat**"
                        elif count==1: 
                            print(stages[5])   
                            print("||------------------answer the last time-----------------||")               
                        elif count==2: 
                            print(stages[4])
                            print("||------------------answer the 5th time------------------||") 
                        elif count==3:
                            print(stages[3])
                            print("||------------------answer the 4th time------------------||") 
                        elif count==4:
                            print(stages[2])
                            print("||------------------answer the 3th time------------------||") 
                        elif count==5:
                            print(stages[1])
                            print("||------------------answer the 2th time------------------||") 
                                                                                                            
        else:
            if str in guessed_letters:
                print("||--------------------sorry to disappoint u-----------------||")                            
                print("||----------You have already guessed this letter------------||")
                print("||-------------------please try again-----------------------||")
            else:                
                guessed_letters.append(str) 
                count-=1
                print("||---------------------sorry to disappoint u-----------------||")
                print("||--------------------but the answer is  wrong---------------||")                                   
                if count==0:
                    stages[6]                       
                    return "||--------------------The word was: " + word+ "----------------||"+"\n                  **defeat**"         
                elif count==1:
                    print(stages[5]) 
                    print("||----------------------answer the 6th time-----------------||")                       
                elif count==2:
                    print(stages[4])
                    print("||----------------------answer the 5th time-----------------||") 
                elif count==3:
                    print(stages[3])
                    print("||----------------------answer the 4th time-----------------||") 
                elif count==4:
                    print(stages[2])
                    print("||----------------------answer the 3th time-----------------||") 
                elif count==5:
                    print(stages[1])
                    print("||----------------------answer the 2th time-----------------||") 
                                    
print(Hangman())
while True:
    d=input("||---------Do u want to play again if yes type yY-------||")
    if d.lower()=='y':
        print(Hangman())
    else:
        break