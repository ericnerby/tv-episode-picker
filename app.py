from picker import search_shows, episodes_list
from random import choice


def show_search_prompt():
    search = input("Please provide search terms for the show you'd like to find: ")
    search_results = search_shows(search)
    if not search_results:
        print("I'm sorry, there were no matches found. Please try again.")
        show_search_prompt()
    list_shows(search_results)


def list_shows(search_results):
    print("Search results:")
    for index, show in enumerate(search_results, 1):
        print("{}. {}".format(index, show['name']))
    show_index = int(
        input("Type the number of the show you would like to select from the list: ")
    ) - 1
    if search_results[show_index]:
        random_episode(search_results[show_index]['show_id'], search_results[show_index]['name'])
    else:
        print("Please try again with a number from the list.")
        list_shows(search_results)


def random_episode(show_id, show_name):
    episodes = episodes_list(show_id)
    random_episode_info = choice(episodes)
    user_input = input("""
The random episode picker has found this episode from {show_name}:
Name: {episode_name} | Season: {season} Episode: {episode_num}
Description: {description}
Type 's' for new show | 'n' for new episode | 'e' to exit
""".format(
        show_name = show_name,
        episode_name = random_episode_info['name'],
        season = random_episode_info['season'],
        episode_num = random_episode_info['number'],
        description = random_episode_info['description']
    ))
    if user_input.lower() == 's':
        show_search_prompt()
    elif user_input.lower() == 'n':
        random_episode(show_id, show_name)
    else:
        pass


show_search_prompt()