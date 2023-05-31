row1 = ["_", "_", "_"]
row2 = ["_", "_", "_"]
row3 = ["_", "_", "_"]
map = [row1, row2, row3]
print(f"{row1}\n,{row2}\n,{row3}\n")
position = input("Where do you want to hide the treasure?")
col_row = position.split(",")
column = int(col_row[0]) - 1
row = int(col_row[1]) - 1

map[row][column] = "X"
print(f"{row1}\n,{row2}\n,{row3}\n")