import statistics

def stats_finder(array):
  # Write your code here
  print("Median: " + str(statistics.median(array)))
  print("Mode: " + str(statistics.mode(array)))
  print("Mean: " + str(statistics.mean(array)))

stats_finder([500, 400, 400, 375, 300, 350, 325, 300])
