import os
from random import choice

from connections import episodes_list, search_shows, show_info


EPISODE_FORMAT = """
The random episode picker has found this episode from {show_name}:
Name: {episode_name} | Season: {season} Episode: {episode_num}
Description: {description}
"""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_search_prompt():
    clear()
    search = input("Please provide search terms for the show you'd like to find: ")
    search_results = search_shows(search)
    if not search_results:
        input("I'm sorry, there were no matches found. Press enter to try again.")
        show_search_prompt()
    list_shows(search_results)


def list_shows(search_results):
    clear()
    print("Search results:")
    for index, show in enumerate(search_results, 1):
        print("{}. {}".format(index, show['name']))
    show_index = int(
        input("Type the number of the show you would like to select from the list: ").strip()
    ) - 1
    if search_results[show_index]:
        preview_show(search_results, search_results[show_index]['show_id'])
    else:
        print("Please try again with a number from the list.")
        list_shows(search_results)


def random_episode(show_id, show_name):
    episodes = episodes_list(show_id)
    if len(episodes) > 0:
        random_episode_info = choice(episodes)
        print(EPISODE_FORMAT.format(
            show_name = show_name,
            episode_name = random_episode_info['name'],
            season = random_episode_info['season'],
            episode_num = random_episode_info['number'],
            description = random_episode_info['description']
        ))
        user_input = input(
            "Type 'show' for new show | 'ep' for new episode | 'exit' to exit app\n"
        )
    else:
        print("There are no episodes listed in the database for this show.")
        user_input = input(
            "Type 'show' for new show | 'exit' to exit app\n"
        )
    clear()
    if user_input.lower() == 'show':
        show_search_prompt()
    elif user_input.lower() == 'ep' and len(episodes) > 0:
        random_episode(show_id, show_name)
    else:
        pass


def preview_show(search_results, show_id):
    show = show_info(show_id)
    clear()
    print("{name} | Premiere Date: {premiered}".format(
        name = show['name'],
        premiered = show['premiered'],
    ))
    print("Description: {}".format(show['summary']))
    user_input = input("Type 'r' for random episode | 's' for show list.\n")
    if user_input.lower() == 'r':
        random_episode(show_id, show['name'])
    else:
        list_shows(search_results)


if __name__ == '__main__':
    show_search_prompt()