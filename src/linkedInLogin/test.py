import contextlib
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
with contextlib.closing(webdriver.Firefox()) as driver:
    driver.get('http://www.google.com')
    print "1\n"
    wait = ui.WebDriverWait(driver, 10) # timeout after 10 seconds
    print "2\n"
    print driver.title
    #inputElement = driver.find_element_by_name('Leapkit') #'viewport')
    test = wait.until(lambda driver: driver.title == 'Leapkit')
    print "3\n"
    driver.get('http://www.leapkit.com')
    print "lol DONE"