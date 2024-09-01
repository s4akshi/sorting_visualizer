import matplotlib.pyplot as plt
import random
import time

class SortingVisualizer:
    def __init__(self, data):
        self.data = data

    def plot(self, data, algorithm_name, color):
        plt.bar(range(len(data)), data, color=color)
        plt.title(f"{algorithm_name}")
        plt.draw()
        plt.pause(0.1)
        plt.clf()

    def bubble_sort(self):
        data = self.data.copy()
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                self.plot(data, "Bubble Sort", "blue")
        return data

    def insertion_sort(self):
        data = self.data.copy()
        for i in range(1, len(data)):
            key = data[i]
            j = i-1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
            self.plot(data, "Insertion Sort", "green")
        return data

    def selection_sort(self):
        data = self.data.copy()
        for i in range(len(data)):
            min_idx = i
            for j in range(i+1, len(data)):
                if data[min_idx] > data[j]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
            self.plot(data, "Selection Sort", "red")
        return data

if __name__ == "__main__":
    n = 20  # Number of elements
    data = random.sample(range(1, 100), n)
    
    visualizer = SortingVisualizer(data)

    plt.ion()  # Turn on interactive mode
    visualizer.bubble_sort()
    time.sleep(1)
    visualizer.insertion_sort()
    time.sleep(1)
    visualizer.selection_sort()
    plt.ioff()  # Turn off interactive mode
    plt.show()
