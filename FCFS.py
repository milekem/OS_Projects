import csv

# Declarations of necessary variables
processes = [[]]
queue = [[]]
completed = [[]]
currentProcess = []
processTimer = 0
globalTimer = 0
timeStarted = 0
timeFinished = 0
avgWT = 0

def updateQueue():
    # Search for a new process to add to the queue
    for i in range(0, counter - 1):
        if processes[i][2] == str(globalTimer):
            queue.append(processes[i])
            print(queue)

def initialize():
    global currentProcess, processTimer
    if len(queue) != 0 and queue[0][2] == str(globalTimer):
        currentProcess = queue[0]
        processTimer = 0

def processFinished():
    # Check if the currently executing process has finished
    if not len(currentProcess) == 0:
        if currentProcess[1] == str(processTimer):
            del queue[0]
            return True
        else:
            return False

def calculateData():
    # Calculate waiting time and record it
    waitingTime = globalTimer - processTimer - int(currentProcess[2])
    currentProcess.append(str(waitingTime))
    currentProcess.append(str(globalTimer))  # Record the end time of the process

def updateTimers():
    # Update timers
    global processTimer, globalTimer, timeStarted, timeFinished
    processTimer += 1
    globalTimer += 1
    timeStarted += 1
    timeFinished += 1

def quitProgram():
    # Check if the program can be terminated
    if len(queue) == 0 and len(completed) >= counter - 1:
        return True
    else:
        return False

def avgWaitingTime():
    global avgWT
    for n in completed:
        avgWT += int(n[3])
    avgWT = avgWT / (counter - 1)

with open('test.csv', newline='') as dataFile:
    # Read data from the file for testing
    reader = csv.reader(dataFile, delimiter=',')
    counter: int = 0
    for row in reader:
        if counter == 0:
            print(f'Column names are {", ".join(row)}')
            counter += 1
        else:
            for i in range(0, 3):
                processes[counter - 1].insert(i, row[i])
            processes.append([])
            counter += 1

del queue[0]
del completed[0]

# Main program loop
while True:
    updateQueue()
    initialize()

    if quitProgram():
        avgWaitingTime()
        with open('results_FCFS.csv', 'w') as f:
            # Save data to a file
            f.write("%s%s\n" % ("Average waiting time: ", str(avgWT)))
            f.write("%s,%s,%s,%s,%s\n" % ('pNumber', "burstTime", "arrivalTime", "waitingTime", "endTime"))
            for i in range(0, counter - 1):
                for j in range(0, 5):
                    f.write("%s," % (completed[i][j]))
                f.write("\n")
        break

    if processFinished():
        calculateData()
        completed.append(currentProcess)  # Add to the completed list
        if not len(queue) == 0:
            currentProcess = queue[0]
        processTimer = 0
        print("Completed: ", completed)

    updateTimers()
