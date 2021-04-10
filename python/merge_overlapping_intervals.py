class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  def __str__(self):
    return f"({self.first}, {self.second})"

def merge_intervals(v):
  arrLen = len(v)

  if arrLen == 0:
    return []

  result = []
  currentMerge = v[0]

  for i in range(1, arrLen):
      pair = v[i]

      merge = checkOverlapAndCreateMerge(currentMerge, pair)

      if merge is not None:
        currentMerge = merge
      else:
        result.append(currentMerge)
        currentMerge = pair

  result.append(currentMerge)

  return result

def checkOverlapAndCreateMerge(pair1, pair2):
  if pair1.first <= pair2.first <= pair1.second:
    newPairFirst = min(pair1.first, pair2.first)
    newPairSecond = max(pair1.second, pair2.second)
    return Pair(newPairFirst, newPairSecond)
  return None

def printIntervals(v):
  for interval in v:
    print(interval)

if __name__ == "__main__":
  pairs = [
    Pair(1, 5),
    Pair(3, 7),
    Pair(4, 6),
    Pair(6, 8)
  ]
  pairs2 = [
    Pair(10, 12),
    Pair(12, 15)
  ]
  printIntervals(merge_intervals(pairs))
  print("------------------------------")
  printIntervals(merge_intervals(pairs2))