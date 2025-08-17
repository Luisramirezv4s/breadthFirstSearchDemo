from collections import deque #import fuction's queue
 #python use the double-ended queue (deque) function for this

# hash table implemantation
graph = {} #Hash fuction, dictionary
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

#Mango seller function
def personIsSeller(name): 
    return name[-1] == "b"


#breadth-first_search function 
def search(name): 
    searchQueue = deque()           #creates a new queue
    searchQueue += graph[name]      #Adds all of your neighbors to the search queue 
    searched = []                   #This array is how you you keep track of which people you've searched before
    while searchQueue:              #while the queue is't empty
        person = searchQueue.popleft()  # ... grabs the first person off the queue
        if not person in searched:  #Only search this person if you haven't already searched them
            if personIsSeller(person):  # checks weather the person is a mango seller
                print(person + " is a mango seller") # done
                return True
            else: 
                searchQueue += graph[person] #No, they aren't. Add all of this person's fiends to the search queue
                searched.append(person)     #Mark this person as searched
    return False #There's no one seller


search("you")

