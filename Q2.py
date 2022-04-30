import main

def schedule(list): #basically splits the list of processses in half with the second half being taken care of by the faster processors
    #establishes the queue for the processors
    queue = main.PriorityQueue() #Processors A,B,C
    queue2 = main.PriorityQueue() #Processors D,E,F
    i = 6
    while i > 3:
        queue.insert(0)
        i-=1
    while i > 0:
        queue2.insert(0)
        i-=1

    #establishes the variables
    wait_time = 0 #for slow group
    wait_time2 = 0 #for fast group
    total_burst_time = 0 #for slow group
    total_burst_time2 = 0 #for fast group
    l = int(len(list) / 2)
    list.sort() #sorts the list of burst times in ascending order. This will matter later.

    #takes the first half of the list, the half with the shorter burst times, and lets the slower processors deal with them.
    for p in list[:l]:
        total_burst_time += p
        next = queue.delete()
        time = next + p
        wait_time += next
        queue.insert(time)

    #gets the top half of processes, the half with the longer burst times, and lets the faster processors deal with them.
    list.reverse()
    for p in list[:l]:
        total_burst_time2 += p
        next = queue2.delete()
        time = next + p
        wait_time2 += next
        queue2.insert(time)

    #calculates the averages
    wait_time /= 2000000000
    wait_time2 /= 4000000000
    total_burst_time /= 2000000000 #divide by this number due to this being the burst time of the 2 GB processor group
    total_burst_time2 /= 4000000000 #divide by this number due to this being the burst time of the 4 GB processor group
    avg_wait_time =  (wait_time + wait_time2) / len(list)
    avg_turnaround_time = (wait_time + wait_time2 + total_burst_time + total_burst_time2) / len(list)

    #output
    print("First Algorithm:")
    print("Average Wait Time (cycles/secs): " + str(avg_wait_time))
    print("Average Turnaround Time (cycles/secs): " + str(avg_turnaround_time))

def schedule2(list): #basically assigns every third process to the slower processors so the bulk of the work is taken care of by the faster processors
    #initializes the queues to hold the processors
    queue = main.PriorityQueue() #slow processors A,B,F
    queue2 = main.PriorityQueue() #fast processors D,E,F
    i = 6
    while i > 3:
        queue.insert(0)
        i-=1
    while i > 0:
        queue2.insert(0)
        i-=1

    #establishes variables
    wait_time = 0
    wait_time2 = 0
    total_burst_time = 0
    total_burst_time2 = 0

    #sorts the list from shortest burst time to longest burst time
    list.sort()

    for p in list:
        if list.index(p) % 3 == 0: #every third process is processed by the slow processors
            total_burst_time += p
            next = queue.delete()
            time = next + p
            wait_time += next
            queue.insert(time)
        else: #two thirds of the processes will be processed by the faster processors
            total_burst_time2 += p
            next = queue2.delete()
            time = next + p
            wait_time2 += next
            queue2.insert(time)

    #calculate average wait time and average turn around time
    wait_time /= 2000000000
    wait_time2 /= 4000000000
    total_burst_time /= 2000000000 #divide by this number due to this being the burst time of the 2 GB processor group
    total_burst_time2 /= 4000000000 #divide by this number due to this being the burst time of the 4 GB processor group
    avg_wait_time =  (wait_time + wait_time2) / len(list)
    avg_turnaround_time = (wait_time + wait_time2 + total_burst_time + total_burst_time2) / len(list)

    #output
    print("Second Algorithm:")
    print("Average Wait Time (cycles/secs): " + str(avg_wait_time))
    print("Average Turnaround Time (cycles/secs): " + str(avg_turnaround_time))

if __name__ =="__main__":
    schedule(main.burst_times)
    schedule2(main.burst_times)