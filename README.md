# Random TV Episode Picker!

## Why did I make this?

Have you ever found yourself wanting to watch an episode of your favorite show, but couldn't decide which episode to watch?

**ME TOO!!**

I made this python app which pulls episode data for whatever show you want from the [TV Maze API](https://www.tvmaze.com/api).

## How to use it

1. Clone the repo to your computer.
1. Before you run the app, you can make sure you have all the requirements installed by navigating to the root of the project folder and running `pip install -r requirements.txt` from a terminal.
1. Run `python app.py` from a terminal in the project folder.
1. Once the app is running, follow the prompts to search for and pick a show.
1. You pick the show, and the app picks the episode.
1. If you don't like the episode or want to try another show, just follow the prompts.

## How it works

Random TV Episode Picker uses the python `requests` library to interact with the [TV Maze API](https://www.tvmaze.com/api), and then randomly picks an episode from the show you've chosen.

You pick the show, and the app picks the episode. If you don't like the episode, just tell it to pick another one!