from conftest import *
from selenium.webdriver.common.by import By
import re
# google use english len by clicking on the text "English"
def click_english_text_on_google_page():
    try:
        element = driver.find_element(By.LINK_TEXT, "English")
        element.click()
    except Exception as e:
        print(f"Failed to click 'English': {e}")


# function for clicking on images btn on google page

def click_on_image_btn():
    try:
        images_text = driver.find_element(By.LINK_TEXT, "Images")
        images_text.click()
    except Exception as e:
        print(f"Failed to click 'Images': {e}")


# function fo clicking on search text and insert search term "Rick and Morty"

def search_for_rick_and_morty():
    search_box = driver.find_element(By.XPATH, '//*[@title="Search"]')
    search_box.click()
    search_text = "Rick and Morty"
    return search_box, search_text


# function that extracts the names of randon characters that were saved to txt file

def extract_random_character_name_from_file():
    with open(file_path, 'r') as file:
        lines = file.readlines()
    character_names = []
    pattern = re.compile(r"Hi! I'm ([\w\s'-]+),")
    for line in lines:
        match = pattern.search(line)
        if match:
            name = match.group(1)  # Extract the captured name
            character_names.append(name)
    if len(character_names) < 2:
        print("File contains fewer than two character names.")
        return []
    first_name = character_names[0]
    second_name = character_names[1]
    driver.implicitly_wait(5)
    return first_name, second_name

# function extract location from txt file

def extract_character_location_from_file():
    with open(file_path, 'r') as file:
        lines = file.readlines()
    character_locations = []
    pattern = re.compile(r"I'm from ([\w\s'-]+)")
    for line in lines:
        match = pattern.search(line)
        if match:
            location = match.group(1)  # Extract the captured name
            character_locations.append(location)
    if len(character_locations) < 2:
        print("File contains fewer than two locations.")
        return []
    first_location = character_locations[0]
    second_location = character_locations[1]
    driver.implicitly_wait(5)
    return first_location, second_location

# function extracts id from txt file


def extract_random_character_id_from_file():
    with open(file_path, 'r') as file:
        lines = file.readlines()

    characters_id = []
    pattern = re.compile(r"My ID is (\d+)")
    for line in lines:
        match = pattern.search(line)
        if match:
            ids = match.group(1)  # Extract the captured name
            characters_id.append(ids)
    if len(characters_id) < 2:
        print("Warning: File contains fewer than two character names.")
        return []
    first_id = characters_id[0]
    second_id = characters_id[1]

    return {"first_id": first_id, "second_id": second_id}

# function calculate position on ui grid of an image based on id of the character
def calculate_position_based_on_extracted_character_id(character_id):

    char_id_str = str(character_id)
    if len(char_id_str) >= 3:
        position = int(char_id_str[-3]) + int(char_id_str[-1])
    elif len(char_id_str) == 2:
        position = int(char_id_str[-2]) + int(char_id_str[-1])
    else:
        position = int(char_id_str[-1])
    return position


# def extract_image_position_based_on_id():
#     character_id = extract_random_character_id_from_file()
#     position = calculate_position_based_on_extracted_character_id(character_id)
#     image_selector = f"div[data-q]:nth-of-type({position - 1})"
#     driver.find_element(By.CSS_SELECTOR, image_selector).click()