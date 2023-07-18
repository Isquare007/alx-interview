def ArrayChallenge(strArr):
  newArr = []

  for x in range(0, len(strArr)):
    if (strArr[x] in newArr):
      newArr.remove(strArr[x])
    newArr.append(strArr[x])
    if len(newArr) > 5:
      newArr.pop(0)  # Remove the first element instead of the last

  strOutput = "-".join(newArr)
