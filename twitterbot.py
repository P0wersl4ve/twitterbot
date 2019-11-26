# Hello there, I'm new to python so I thought it could be fun to do
# some python automation projects in order to dive further in the language,
# this is the first one I've done so, I did it following a video on youtube that I found very interesting

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self):
        bot = self.bot
        # Here you can set the url your bot will go to and start scrapping
        bot.get('https://twitter.com/hashtag-or-profile-to-look')  
        time.sleep(3)
        # we are going to save all tweets we can find by scrolling the page for about 20 times
        for i in range(1, 20):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(4)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    # We are going to  find any element in the page that has a "HeartAnimation" class attached to it and click it,
                    # as you can imagine this is not so optimal because it may stop working in the future if the element changes in its design
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(5)
                except Exception as ex:
                    time.sleep(60)


# You need to pass your username and password as parameters in order to log in
ed = TwitterBot('username', 'password')
ed.login()
ed.like_tweet()