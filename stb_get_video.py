from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import webbrowser

def main():
	chrome_options = Options()
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--log-level=3")
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) 
	url = input("URL: ")
	driver.get(url)
	driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
	link_elements = driver.find_elements_by_xpath('//link[contains(@rel, "preload")]')
	src = link_elements[-1].get_attribute("href")
	print(src)
	webbrowser.open(src, new=2)
	driver.quit()
			
if __name__ == '__main__':
	main()