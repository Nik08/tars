import sys, os, pickle

class userConversation:
    def init(x):
        if "how" in x and "are" in x and "you" in x:
            print("My emotional or physical status is not important in the overall scheme of life. I am a semi-sentient piece of code aimed at helping the user interact with their computer. Also... I'm feeling kind of philosophical...")
        if "what" in x and "your" in x and "name" in x:
            print("My name is Cortana! I am code, but I am also your helper")
        if "what" in x and "my" in x and "name" in x:
            try:
                name = pickle.load(open( "userName.p", "rb" ))
                print("Why are you asking? Ok... Your name is " + name)
            except:
                print("It seems we dont have a name for you yet. Say call me and then your name to set a name that I should call you!")
        if "call" in x and "me" in x:
            splitCommand = x.split()
            index = 0
            for val in splitCommand:
                if val == "me":
                    index += 1
                    userName = splitCommand[index]
                index += 1
            pickle.dump(userName, open( "userName.p", "wb" ) )
            print(userName)
            print("Ok I shall call you " + userName + " from now on!")
