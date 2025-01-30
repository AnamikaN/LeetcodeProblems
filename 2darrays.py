# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix1 = [
  [ 1,  2,  3,  4,  5],
  [ 6,  7,  8,  9, 10],
  [11, 12, 13, 14, 15]];

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def linearizeRowMajor(matrix: list[list[int]]) -> list[int]:
  result = []
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      result.append(matrix[i][j])
  return result

def linearizeColumnMajor(matrix: list[list[int]]) -> list[int]:
  result = []
  for i in range(len(matrix[0])):
    for j in range(len(matrix)):
      result.append(matrix[j][i])
  return result

def averageColumnMinimum(matrix: list[list[int]]) -> float:
    result = []
    sum = 0.0
    for i in range(len(matrix[0])):
        minimum = float('inf')
        for j in range(len(matrix)):
            minimum = min(matrix[j][i], minimum)
        sum = sum+minimum
    result = sum/len(matrix[0])
    return result

def averageRowMinimum(matrix: list[list[int]]) -> float:
    result = []
    sum = 0.0
    for i in range(len(matrix)):
        minimum = float('inf')
        for j in range(len(matrix[0])):
            minimum = min(matrix[i][j], minimum)
        sum = sum + minimum
    result = sum / len(matrix)
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(linearizeRowMajor(matrix))
    print(linearizeColumnMajor(matrix))
    print(averageColumnMinimum(matrix))
    print(averageRowMinimum(matrix))
    print(averageColumnMinimum(matrix1))
    print(averageRowMinimum(matrix1))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
