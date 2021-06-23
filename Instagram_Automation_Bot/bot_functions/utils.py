

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from time import perf_counter
def scrolldown(self, numpeople, classname="FPmhX", people_number_flex = 7):

    """This function is made to scroll down the list of followers/following for a person. It can be tweaked to
    become a regular automatic scroller.
    After scrolling all the way down, it return an array of the people that it has scrolled through."""
    try:

        thingtodo = ActionChains(self.browser)  # we need to create a separate action chains object due to the bugs
        # with the send_keys function
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()
        thingtodo.send_keys(Keys.TAB).perform()

        now = self.browser.find_elements_by_class_name(classname)
        past_num = len(now) + 2
        changetime = perf_counter()
        while (len(now) <= numpeople - people_number_flex) and (past_num != len(now) or perf_counter() -
                                                                changetime<10):

            if past_num != len(now):
                changetime = perf_counter()
                print("Yes")


            past_num = len(now)
            now = self.browser.find_elements_by_class_name(classname)
            thingtodo.send_keys(Keys.END).perform()
            sleep(self.scrollsleep)
            # print(len(now))

        now = self.browser.find_elements_by_class_name(classname)
        final = []
        for i in now:
            final.append(i.text)

        return final

    except:
        return self.scrolldown(numpeople=numpeople, classname=classname)