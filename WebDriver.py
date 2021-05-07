import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.youtube.com/")

WebDriverWait(browser, 3)
browser.find_element_by_css_selector('[name="search_query"]').send_keys("lofi")
time.sleep(1)
browser.find_element_by_css_selector('[name="search_query"]').click()
time.sleep(3)
for i in range(4):
    browser.find_element_by_css_selector('[name="search_query"]').send_keys(Keys.ARROW_DOWN)
    time.sleep(1)

time.sleep(2)
browser.find_element_by_css_selector('[name="search_query"]').send_keys(Keys.RETURN)

time.sleep(2)

titlelist = browser.find_elements_by_css_selector('a#video-title')
firstvideo = titlelist[0]
browser.get(firstvideo.get_attribute('href'))

time.sleep(20)
browser.execute_script("window.scrollTo(0, 100)")
time.sleep(2)
channel = browser.find_elements_by_css_selector('a.ytd-video-owner-renderer')
Music = channel[0]
browser.get(Music.get_attribute('href'))

channelSays = browser.title
print(channelSays)
expectedText = "Lo-fi Music - YouTube"

assert channelSays == expectedText

time.sleep(10)
browser.quit()
