#!/usr/local/bin/python3
import random
import csv

def inplace_quick_sort(S, a, b):
  """Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm."""
  if a >= b: return 0                                      # range is trivially sorted
  pivot = S[b]                                           # last element of range is pivot
  left = a                                               # will scan rightward
  right = b-1                                            # will scan leftward
  count = 0
  while left <= right:
    # scan until reaching value equal or larger than pivot (or right marker)
    while left <= right and S[left] < pivot:
      left += 1
      count += 1
    # scan until reaching value equal or smaller than pivot (or left marker)
    while left <= right and pivot < S[right]:
      right -= 1
      count += 1
    if left <= right:                                    # scans did not strictly cross
      S[left], S[right] = S[right], S[left]              # swap values
      left, right = left + 1, right - 1                  # shrink range
      count += 1

  # put pivot into its final place (currently marked by left index)
  S[left], S[b] = S[b], S[left]
  count += 1
  # make recursive calls
  inplace_quick_sort(S, a, left - 1)
  inplace_quick_sort(S, left + 1, b)

  return count


with open("quick_sort.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Size", "Count"])
    dataset_sizes = [10000, 20000, 30000, 40000, 50000]

    for size in dataset_sizes:
        for _ in range(300):
            arr = random.sample(range(size * 10), size)
            count = inplace_quick_sort(arr, 0, len(arr) - 1)
            writer.writerow([size, count])

print("finished")


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Syafino Yunalfian
