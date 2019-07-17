#PROGRAMMING FUNDAMENTALS REINFORCEMENT 5

#1

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

def sum_of_odd (listx):
    x = 0
    for num in listx:
        if num % 2 == 1:
            x += num 
    return x

print(sum_of_odd(num_list))

#2

name_list = ['Billy', 'Bob', 'Thorton']

print('Hello please enter your name')
user_name = input()

if user_name in name_list:
    print("Hello, {}!".format(user_name))
else:
    print("Who goes there?")
