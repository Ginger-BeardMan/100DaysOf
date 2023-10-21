import pandas

data = pandas.read_csv("Squirrel_Data.csv")

squirrel_list = data["Primary Fur Color"].to_list()

squirrel_dict = {'Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': []}
gray = 0
cinnamon = 0
black = 0

for color in squirrel_list:
    if color == 'Gray':
        gray += 1
    elif color == 'Cinnamon':
        cinnamon += 1
    elif color == 'Black':
        black += 1

squirrel_dict['Count'].append(gray)
squirrel_dict['Count'].append(cinnamon)
squirrel_dict['Count'].append(black)

print(squirrel_dict)

s_data = pandas.DataFrame.from_dict(squirrel_dict)

s_data.to_csv("s_color_data.csv")
