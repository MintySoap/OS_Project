import main

def schedule(times, mem): #same as schedule 1 for Q3 but no sort
    queue = main.PriorityQueue()
    queue2 = main.PriorityQueue()
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

    for p,m in new:
        if new.index((p,m)) % 3 != 0 and m < 8000:
            total_burst_time += p
            next = queue.delete()
            time = next + p
            wait_time += next
            queue.insert(time)
        else:
            total_burst_time2 += p
            next = queue2.delete()
            time = next + p
            wait_time2 += next
            queue2.insert(time)

    wait_time /= 2000000000
    wait_time2 /= 4000000000
    total_burst_time /= 2000000000
    total_burst_time2 /= 4000000000
    avg_wait_time =  (wait_time + wait_time2) / len(new)
    avg_turnaround_time = (wait_time + wait_time2 + total_burst_time + total_burst_time2) / len(new)

    print("First Algorithm")
    print("Average Wait Time (cycles/secs): " + str(avg_wait_time))
    print("Average Turnaround Time (cycles/secs): " + str(avg_turnaround_time))

def schedule2(times, mem): #same as schedule 2 of Q3 but no sort
    queue = main.PriorityQueue()
    queue2 = main.PriorityQueue()
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

    for p,m in new:
        next = queue.delete()
        next2 = queue2.delete()
        if next < next2 and m < 8000:
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

def schedule3(times, mem): #finds and compares each value to the average
    queue = main.PriorityQueue()
    queue2 = main.PriorityQueue()
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
    num_of_cycles = 0
    num_of_processes_so_far = 0

    new = list(zip(times, mem))
    avg = 0

    for p,m in new:
        num_of_cycles += p
        num_of_processes_so_far += 1
        avg = num_of_cycles / num_of_processes_so_far #calculates the average number of cycles with each new process
        if p < avg * 3 / 2 and m < 8000:
            total_burst_time += p
            next = queue.delete()
            time = next + p
            wait_time += next
            queue.insert(time)
        else:
            total_burst_time2 += p
            next = queue2.delete()
            time = next + p
            wait_time2 += next
            queue2.insert(time)

    wait_time /= 2000000000
    wait_time2 /= 4000000000
    total_burst_time /= 2000000000
    total_burst_time2 /= 4000000000
    avg_wait_time =  (wait_time + wait_time2) / len(new)
    avg_turnaround_time = (wait_time + wait_time2 + total_burst_time + total_burst_time2) / len(new)

    print("Third Algorithm:")
    print("Average Wait Time (cycles/secs): " + str(avg_wait_time))
    print("Average Turnaround Time (cycles/secs): " + str(avg_turnaround_time))

if __name__ =="__main__":
    schedule(main.burst_times, main.memories)
    schedule2(main.burst_times, main.memories)
    schedule3(main.burst_times, main.memories)