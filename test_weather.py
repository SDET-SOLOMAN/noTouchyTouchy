from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_page(engine):
    engine.get("https://openweathermap.org/")


def test_check_title(engine):
    engine.get("https://openweathermap.org/")
    print(engine.title)
    expected_title = "Сurrent weather and forecast - OpenWeatherMap"
    assert expected_title == engine.title, f"Titles dont mathc, expected title: {expected_title}," \
                                           f"but the actual one is {engine.title}"


# find search bar
def test_search_the_bar(engine):
    engine.get("https://openweathermap.org/")
    search = engine.find_element(By.CSS_SELECTOR, "div.search-container input")
    search.clear()
    search.send_keys("New York", Keys.RETURN)
    city_visible = WebDriverWait(engine, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.search-container "
                                                         "li:nth-child("
                                                         "1)"))).click()
    new_page = WebDriverWait(engine, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.current-container"
                                                           ".mobile"
                                                           "-padding h2"),
                                         "New York City, US"))

    expected = "New York"
    actual = engine.find_element(By.CSS_SELECTOR, "div.current-container.mobile-padding h2").text
    print(expected, actual)
    assert expected in actual
