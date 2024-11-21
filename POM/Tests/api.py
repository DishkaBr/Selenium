import conftest
from conftest import *
import requests
import random

# this api call is getting all episodes from base url ( see conftest file )
def get_all_episodes():
    response = requests.get(f"{base_url}/episode")
    return response.json()

# this function is checking episode with more than or equal to 30 characters in episode
def filter_episode_by_char_len_30andup():
    response = get_all_episodes()
    episodes_with_30_or_more_characters = [episode for episode in response["results"] if len(episode["characters"]) >= 30]
    if episodes_with_30_or_more_characters:
        random_episode = random.choice(episodes_with_30_or_more_characters)
        print(f"random episode name is: {random_episode['name']} number of characters: {len(random_episode['characters'])}")
        return random_episode


# the function selects randomly 2 characters from episodes that has more or equal to 30 characters
# after selecting the characters the name, id and location are written to the file txt
def random_character_selection():
    response = get_all_episodes()
    episodes_with_30_or_more_characters = [episode for episode in response["results"] if
                                           len(episode["characters"]) >= 30]
    file = conftest.file_path
    with open(file, "w") as file:
        if episodes_with_30_or_more_characters:
            random_episode = random.choice(episodes_with_30_or_more_characters)

            characters_objects = random.sample(random_episode["characters"], 2)

            for character in characters_objects:
                response = requests.get(character)
                character_data = response.json()
                location = character_data['location']

                extracted_location_name = location['name']

                output = f"Hi! I'm {character_data['name']}, My ID is {character_data['id']}, I'm from {extracted_location_name}, My species is {character_data['species']}\n"
                file.write(output)





