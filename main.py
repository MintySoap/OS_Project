#helper file that provides methods to be used in the rest of the questions
import csv

#goes through the csv file and records the burst_times and memories of each individual process
burst_times = []
memories = []
with open('processes.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    skipColumnHeader = True
    for row in csv_reader:
        if skipColumnHeader:
            skipColumnHeader = False
        else:
            burst_times.append(int(row[1]))
            memories.append(int(row[2]))

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    def isEmpty(self):
        return len(self.queue) == 0
  
    def insert(self, data):
        self.queue.append(data)
  
    def delete(self): #records the lowest value in the queue, deletes that value from the queue, and returns that value
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

    def len(self): #returns the length of the queue
        return len(self.queue)

    def lowest_value(self): #returns the lowest value in the queue without deleting it afterwards
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min = i
            item = self.queue[min]
            return item
        except IndexError:
            print()
            exit()