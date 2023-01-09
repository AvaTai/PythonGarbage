import math
def printPattern(radius):
    for i in range((2 * radius)+1):
        for j in range((4 * radius)+2):
            dist = math.sqrt((i - radius) * (i - radius) + (j - radius) * (j - radius))
            #for closed circle do the following:
            if (dist > radius - 0.5):
                print("  ",end="")
            else:
                print("* ",end="")
            #for open circle do the following:
            #if (dist > radius - 0.5 and dist < radius + 0.5):
                #print("* ",end="")
            #else:
                #print("  ",end="")
        print()
#set radius here
radius = 10
printPattern(radius)