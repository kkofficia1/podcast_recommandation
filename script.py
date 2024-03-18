from podcast import categories
from podcast import podcasts

def greet():
    print("Welcome to this podcast reccomendation software. We'll find the right podcast for you.")

def goodbye():
    print("Thanks for using this service. We hope we could help you.")

def recommend(category):
    possible_podcasts = []
    for i in podcasts:
        if category == i[3]:
            possible_podcasts.append(i)
        else:
            continue
    sorted_podcast_list = sort_by_rating(possible_podcasts)
    for i in sorted_podcast_list:
        print("Title: {0}\nLanguage: {1}\nRating: {2}".format(i[0],i[1],i[2]))

def sort_by_rating(lst):
    l = len(lst)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (lst[j][2] < lst[j+1][2]):
                tempo = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tempo
    return lst
    

def autocomplete():
    possible_categories = []
    user_category = input("Which category do you like?\nThis feature uses autocomplete so just type the beginning of your word and press enter to see if it is here: ")
    check_length = len(user_category)
    for category in categories:
        if check_length == 1:
            if category[0] == user_category:
                possible_categories.append(category)
        elif check_length > 1: 
            if category[0:(check_length)] == user_category:
                possible_categories.append(category)
            else:
                continue
        else:
            autocomplete()
    if len(possible_categories) > 1:
        print("With those beginning letters, your choices are " + str(possible_categories))
        autocomplete()
    elif len(possible_categories) < 1:
        print("With those beginning letters, you do not have any choices. Try again")
        autocomplete()
    elif len(possible_categories) == 1:
        print("This is your category: " + str(possible_categories))
        right_choice = input("Are you okay with this choice? y/n ")
        if right_choice == "y":
            print("For your category: " + str(possible_categories) + " These are your options:")
            recommend(possible_categories[0])
        else:
            autocomplete()
    return possible_categories
    

if __name__ == "__main__":
    greet()
    autocomplete()
    ask_more = True
    while ask_more:
        more_podcasts = input("Do you want to get some more recommendations? y/n ")
        if more_podcasts =="y":
            autocomplete()
        else:
            ask_more = False
            goodbye()