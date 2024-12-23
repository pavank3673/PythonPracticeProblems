from random import randint

arr = []
for i in range(3):
    arr.append([0] * 3)

def print_array(ar):
    for i in range(3):
        for j in range(3):
            print(ar[i][j], end=' ')
        print()


while(True):

    print("user turn ")
    while(True):
        row = int(input("Enter row :"))
        col = int(input("Enter col :"))
        if arr[row][col] == "X":
            print("Cell is occupied")
            continue
        else:
            break
   
    arr[row][col] = 'X'
    print_array(arr)    

    if (arr[0][0] == "X" and arr[0][1] == "X" and arr[0][2] == "X") or (arr[1][0] == "X" and arr[1][1] == "X" and arr[1][2] == "X") or (arr[2][0] == "X" and arr[2][1] == "X" and arr[2][2] == "X") or (arr[0][0] == "X" and arr[1][0] == "X" and arr[2][0] == "X") or (arr[0][1] == "X" and arr[1][1] == "X" and arr[2][1] == "X") or (arr[0][2] == "X" and arr[1][2] == "X" and arr[2][2] == "X") or (arr[0][0] == "X" and arr[1][1] == "X" and arr[2][2] == "X") or (arr[2][0] == "X" and arr[1][1] == "X" and arr[0][2] == "X"): 
        print("user win")
        break

    print("computer turn ")
    while(True):
        row =  randint(0, 2)
        col =  randint(0, 2)
        if arr[row][col] == "X":
            continue
        else:
            break
   
    arr[row][col] = 'X'
    print_array(arr)    

    if (arr[0][0] == "X" and arr[0][1] == "X" and arr[0][2] == "X") or (arr[1][0] == "X" and arr[1][1] == "X" and arr[1][2] == "X") or (arr[2][0] == "X" and arr[2][1] == "X" and arr[2][2] == "X") or (arr[0][0] == "X" and arr[1][0] == "X" and arr[2][0] == "X") or (arr[0][1] == "X" and arr[1][1] == "X" and arr[2][1] == "X") or (arr[0][2] == "X" and arr[1][2] == "X" and arr[2][2] == "X") or (arr[0][0] == "X" and arr[1][1] == "X" and arr[2][2] == "X") or (arr[2][0] == "X" and arr[1][1] == "X" and arr[0][2] == "X"): 
        print("computer win")
        break    


