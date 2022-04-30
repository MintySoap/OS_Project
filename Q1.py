import main
import matplotlib.pyplot as plt

def schedule(algorithm, list): #used for both SJF and FIFO

    #creates the queue that holds the 6 processors as they are working
    processor_queue = main.PriorityQueue()
    i = 6
    while i > 0:
        processor_queue.insert(0)
        i-=1

    total_wait_time = 0
    total_burst_time = 0

    #iterates through the list. With each iteration, total_burst_time and total_wait_time are increased.
    #The shortest process is then considered finished and terminates. Afterwards, the idle processor is given a new process (with the previous times added on)
    for p in list:
        total_burst_time += p
        next = processor_queue.delete() #holds the turnaround time of the current process and terminates the process, considering it finished
        time = next + p #calculates the turnaround time of the newest process by adding the burst time to turnaround time of the previously deleted process
        total_wait_time += next #total_wait_time += turnaround time of previous process
        processor_queue.insert(time) #simulates assigning the new process to the now idle processor

    avg_wait_time = total_wait_time / len(list) / 4000000000 #assumes a 4 GHz processor to calculate cycles per second
    avg_turnaround_time = (total_wait_time + total_burst_time) / len(list) / 4000000000 #assumes a 4 GHz processor to calculate cycles per second

    print("Average Wait Time using " + algorithm + " (cycles/secs): " + str(avg_wait_time))
    print("Average Turnaround Time using " + algorithm + " (cycles/secs): " + str(avg_turnaround_time))

def round_robin(list):
    #creates the queue that holds the 6 processors as they are working
    processor_queue = main.PriorityQueue()
    i = 6
    while i > 0:
        processor_queue.insert(0)
        i-=1
    
    #establishes variables
    total_wait_time = 0
    total_burst_time = 0

    #creates a copy of the list of processes that we can work with and alter.
    copy = [0] * len(list)
    for i in range(len(list)):
        copy[i] = list[i]
        total_burst_time += copy[i]
    
    #quantum is the duration of each time slice. Based on the mean average of the total_burst_time
    quantum = total_burst_time / len(list)

    #loop basically runs until all of the processes in the list have a leftover burst time of zero
    while(1):
        done = True
        for i in range(len(copy)): #iterates through all the values of the list of processes
            if copy[i] > 0: #If the current process still hasn't been completely processed, run the following code block
                done = False
                next = processor_queue.delete() #records the turnaround time of the shortest process that was running on the processors and takes the process off the processor
                if copy[i] > quantum: #If the current process cannot be finished in the given time slice, execute the code block below
                    time = next + quantum #records the turnaround time for the next process
                    copy[i] -= quantum #assigns the leftover burst time after the time slice
                else: #If the current process can be finished in the given time slice, execute the code block below
                    time = next + copy[i] #records the turnaround time for the next process
                    copy[i] = 0 #sets the process to 0 since it was finished within the time slice
                total_wait_time += next #turnaround time of the process we just 'deleted' is added to total wait time
                processor_queue.insert(time) #next process is assigned to the now idle processor
        if (done == True): #terminates the loop
            break

    #outputs results
    avg_wait_time = total_wait_time / len(list) / 4000000000 #assumes a 4 GHz processor
    avg_turnaround_time = (total_wait_time + total_burst_time) / len(list) / 4000000000 #assumes a 4 GHz processor

    print("Average Wait Time using Round Robin (cycles/secs): " + str(avg_wait_time))
    print("Average Turnaround Time using Round Robin (cycles/secs): " + str(avg_turnaround_time))

if __name__ =="__main__":
    schedule("FIFO", main.burst_times)
    round_robin(main.burst_times)
    main.burst_times.sort() #sorts the list of processes for SJF
    schedule("SJF", main.burst_times)