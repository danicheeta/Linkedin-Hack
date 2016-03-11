from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

chrome_options = Options()
chrome_options.add_experimental_option( "prefs", {'profile.default_content_settings.images': 2})
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fpeople%2Fpymk%2Fhub%3Fref%3Dglobal-nav%26trk%3Dnav_utilities_pymk_header&fromSignIn=true&trk=uno-reg-join-sign-in')

browser.execute_script("var elem = document.getElementById(\"session_key-login\");elem.value = \"danicheeta@yahoo.com\";")
browser.execute_script("var elem = document.getElementById(\"session_password-login\");elem.value = \"2331374\";")
browser.execute_script("$(\".btn-primary\").trigger(\"click\");")

time.sleep(5)

browser.execute_script("window.setInterval(function(){window.scrollBy(0, 1000);}, 100);")
browser.execute_script("setTimeout(function(){$(\".bt-request-buffed\").trigger(\"click\");}, 100000)")


