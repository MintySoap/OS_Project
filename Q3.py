import main

def schedule(times, mem): #same as schedule2 from Q2 but accounts for memory
    #creates the queues for the processors
    queue = main.PriorityQueue() #processors A,B,C
    queue2 = main.PriorityQueue() #processors D,E,F
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

    #makes a list of the processe pairs of cpu cycles and their memories and sorts this list
    new = list(zip(times, mem))
    new.sort()

    #iterates through the cycle,memory pairs
    for p,m in new:
        if new.index((p,m)) % 3 != 0 and m < 8000: #every third process that is under 8 GB of memory will be processed by the slower processors
            total_burst_time += p
            next = queue.delete()
            time = next + p
            wait_time += next
            queue.insert(time)
        else: #two thirds of the processes plus all processes that are over 8 GB will be processed by the faster processors
            total_burst_time2 += p
            next = queue2.delete()
            time = next + p
            wait_time2 += next
            queue2.insert(time)

    #calculates averages
    wait_time /= 2000000000
    wait_time2 /= 4000000000
    total_burst_time /= 2000000000
    total_burst_time2 /= 4000000000
    avg_wait_time =  (wait_time + wait_time2) / len(new)
    avg_turnaround_time = (wait_time + wait_time2 + total_burst_time + total_burst_time2) / len(new)

    #output
    print("First algorithm:")
    print("Average Wait Time (cycles/secs): " + str(avg_wait_time))
    print("Average Turnaround Time (cycles/secs): " + str(avg_turnaround_time))

def schedule2(times, mem): #sees which group of processes has the shortest overall process. This way it will always pull the lowest available processor, not always putting larger processes in faster processor
    queue = main.PriorityQueue() #processor A,B,C
    queue2 = main.PriorityQueue() #processor D,E,F
    i = 6
    while i > 3:
        queue.insert(0)
        i-=1
    while i > 0:
        queue2.insert(0)
        i-=1

    wait_time = 0
    wait_time2 = 0
    total_burst_time = 0
    total_burst_time2 = 0

    new = list(zip(times, mem))
    new.sort()

    for p,m in new:
        next = queue.delete() #gets the shortest process from 2GHz, 8GB processors
        next2 = queue2.delete() #gets the shortest process from 4GHz, 16GB processors
        #sees which group has the shorter process.
        if next < next2 and m < 8000: #If the 2GHz processors have the shorter process then this process will be terminated, and the next process will replace it
            total_burst_time += p
            time = next + p
            wait_time += next
            queue.insert(time)
            queue2.insert(next2)
        else:
            total_burst_time2 += p
            time = next2 + p
            wait_time2 += next2
            queue2.insert(time)
            queue.insert(next)

    wait_time /= 2000000000
    wait_time2 /= 4000000000
    total_burst_time /= 2000000000
    total_burst_time2 /= 4000000000
    avg_wait_time =  (wait_time + wait_time2) / len(new)
    avg_turnaround_time = (wait_time + wait_time2 + total_burst_time + total_burst_time2) / len(new)

    print("Second Algorithm:")
    print("Average Wait Time (cycles/secs): " + str(avg_wait_time))
    print("Average Turnaround Time (cycles/secs): " + str(avg_turnaround_time))

if __name__ =="__main__":
    schedule(main.burst_times, main.memories)
    schedule2(main.burst_times, main.memories)