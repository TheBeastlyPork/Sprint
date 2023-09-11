import time
import pytimedinput

sprinting = True
obedience = 0

def start():
    printByLetter("You awaken, the picture of the world itself blossoming as you begin to see."  + "\n")
    printByLetter("You're in a bare, stone room - lit by a rotating cube floating atop a door."  + "\n")
    printByLetter("The cube fades through the door, leaving the room dark."  + "\n")
    printByLetter("A command echos through your mind."  + "\n")
    printByLetter("FOLLOW"  + "\n")
    response = input()
    return response

def printByLetter(message):
    for i in message:
        print(i, end="")
        time.sleep(0.01)


def battleEvent(promptText, eventText, failText, sucessText, correctAction, reactTime):
    printByLetter(promptText + "\n")

    action, timedOut = pytimedinput.timedInput("", reactTime)

    print(eventText)

    if action.lower() == correctAction:
        printByLetter(sucessText)
        return True
    else:
        printByLetter(failText)
        return False


# printByLetter("hello")


while sprinting:
    answer = start()
    if answer.lower() == "follow":
        obedience += 1
        printByLetter("You step outside the door."  + "\n")
    else:
        obedience -= 1
        printByLetter("The cube drags you through the door anyway."  + "\n")
        printByLetter("Your answer affects nothing."  + "\n")

gunFight = battleEvent("*WHIT*\nYou hear the slide of a holster.", "*CR-CRACK!*\nBullets fly through the air.",
                       "*THWACK*\nOne sinks into your chest...", "*WHIZ WHIZ*\nThey soar over your head.", "drop", 5)