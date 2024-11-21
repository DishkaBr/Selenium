
from POM.Logic.logic_pages import *
from POM.Tests.api import *
import time
timestamp = time.strftime("%d-%m-%Y_%H-%M-%S")


# file_path = "/Users/dianabrook/PycharmProjects/pythonProjectSelenium/characters_introduction.txt"

# the test is testing open google, insert search text and
# search the specified text and character name in image section > take screenshot and save to file

def test_access_google_search_first_char():
    # Access Google and maximize the window
    driver.get(google_url)
    driver.maximize_window()
    driver.implicitly_wait(2)

    # Click "English" link by searching the text
    click_english_text_on_google_page()

    # Navigate to "Images" by text search
    click_on_image_btn()

    #  extract character names from file
    try:
        random_character_selection()
        names = extract_random_character_name_from_file()
        first_name, second_name = names
        print(f"Extracted names: {names}")
    except ValueError as e:
        print(f"Error during character extraction: {e}")
        return

    search_box, search_text = search_for_rick_and_morty()

    search_box.send_keys(search_text + " " +names[0])
    driver.implicitly_wait(1)
    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Google Search"]')
    button.click()
    driver.implicitly_wait(1)
    character_id = extract_random_character_id_from_file()
    position = calculate_position_based_on_extracted_character_id(character_id["first_id"])
    print(position)
    # print the total number of found images
    total_images = driver.find_elements(By.CSS_SELECTOR, "div[data-q]")
    print(f"Total images: {len(total_images)}")

    images_selector = driver.find_elements(By.CSS_SELECTOR, f"div[data-q] > div > div")
    # images_selector = driver.find_elements(By.CSS_SELECTOR, f"div[data-q]>div:nth-of-type({position})")  # Учитываем, что индексация начинается с 0
    print(f"number of  images: {len(images_selector)}")
    # image_element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, images_selector))
    # )
    image_element = driver.find_element(By.CSS_SELECTOR, f"div[data-q] > div > div:nth-of-type({position})")
    print("image found by position")
    image_element.click()
    driver.implicitly_wait(2)
    #first_character_screenshot_file = f"{first_name}_{character_id(["first_id"])}_{timestamp}.jpg"
    first_character_screenshot_file = f"{first_name}_{character_id['first_id']}_{timestamp}.jpg"
    image_element.screenshot(first_character_screenshot_file )
    driver.quit()



# second test search for character and retrieve the url from an image
def test_access_google_search_second_char():
    # Access Google and maximize the window
    driver.get(google_url)
    driver.maximize_window()
    driver.implicitly_wait(2)

    # Click "English" link by searching the text
    click_english_text_on_google_page()

    # Navigate to "Images" by text search
    click_on_image_btn()

    #  extract character names from file
    try:
        random_character_selection()
        driver.implicitly_wait(1)
        names = extract_random_character_name_from_file()
        first_name, second_name = names
        print(f"Extracted names: {names}")
    except ValueError as e:
        print(f"Error during character extraction: {e}")
        return
    search_box, search_text = search_for_rick_and_morty()

    search_box.send_keys(search_text + " " + names[1])
    driver.implicitly_wait(1)
    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Google Search"]')
    button.click()
    driver.implicitly_wait(1)


    character_id = extract_random_character_id_from_file()
    second_position = calculate_position_based_on_extracted_character_id(character_id["second_id"])

    image_element = driver.find_element(By.CSS_SELECTOR, f"div[data-q] > div > div:nth-of-type({second_position})")
    print("image found by position")
    image_element.click()
    element = image_element.find_element(By.CSS_SELECTOR, 'img')
    image_url = element.get_attribute("src")
    print(f"Image URL: {image_url}")
    driver.implicitly_wait(2)

    second_character_screenshot_file = f"{second_name}_{character_id['second_id']}_{timestamp}.jpg"
    image_element.screenshot(second_character_screenshot_file)

    driver.quit()


# test that check the location of 2 characters
def test_location_assertion():
    random_character_selection()
    driver.implicitly_wait(5)
    names = extract_random_character_name_from_file()
    first_name, second_name = names

    locations = extract_character_location_from_file()
    first_location, second_location = locations
    try:
        assert first_location == second_location

        print(f"both characters are from {first_location}")

    except AssertionError as e:
        print(f"Assertion failed: {e}")
        print(f"{first_name} is from {first_location}, {second_name} is from {second_location}")


