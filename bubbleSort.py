import time

print()
# set up to time the code

start_time = time.time()


# ** Bubble Sort **


def bubbleSort_copilot(arr):  # copilot - Time elapsed:  3.78 seconds
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSort(arr):  # my attempt -Time elapsed:  2.61 seconds
    counter = len(arr)

    while counter > 0:
        run1 = 0
        run2 = 1

        for i in range(counter - 1):
            if arr[run1] > arr[run2]:
                arr[run1], arr[run2] = arr[run2], arr[run1]
            run1 += 1
            run2 += 1
        counter -= 1

    return arr


num_list1 = [6, 5, 3, 1, 8, 7, 2, 4] * 1000

bubbleSort(num_list1)

#
end_time = time.time()
# time_elapsed = end_time - start_time
# conver to seconds
# time_elapsed = time_elapsed * 1000
print("time start: ", start_time)
print("Time end: ", end_time)
print("Time elapsed: ", round((end_time - start_time), 2), "sec")
#
#
#
print()
