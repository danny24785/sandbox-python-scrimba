#Sets - Exercise

#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']
all_friends = friends.union(my_friends)
all_friends_pipe = friends | my_friends
intersection_friends = friends.intersection(my_friends)
intersection_friends_ampersand = friends & my_friends
friends_which_are_in_my_friends = friends.difference(my_friends)
friends_which_are_in_my_friends_minus = friends - my_friends
my_friends_which_are_in_friends_minus = my_friends - friends
unique_friend = friends.symmetric_difference(my_friends)
unique_values_roof = friends ^ my_friends
new_cars_list = set(cars)

print('Eric' in friends and 'John' in friends)
print('all_friends', all_friends)
print('all_friends_pipe', all_friends_pipe)
print('intersection_friends', intersection_friends)
print('intersection_friends_ampersand', intersection_friends_ampersand)
print('friends_which_are_in_my_friends', friends_which_are_in_my_friends)
print('friends_which_are_in_my_friends_minus', friends_which_are_in_my_friends_minus)
print('my_friends_which_are_in_friends_minus', my_friends_which_are_in_friends_minus)
print('unique_friend', unique_friend)
print('unique_values_roof', unique_values_roof)
print('new_cars_list', new_cars_list)