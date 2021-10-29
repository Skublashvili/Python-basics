row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Write numbers of column and row where do you want to put the treaasure: ")

column = int(position[0]) - 1
row = int(position[1])
print(column)

selected_row = map[row - 1]
selected_row[column] = "X"

# if row == 1:
#     row1[column] = "X"
# elif row == 2:
#     row2[column] = "X"
# else:
#     row3[column] = "X"

print(f"{row1}\n{row2}\n{row3}")