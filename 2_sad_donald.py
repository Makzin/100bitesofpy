import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def makeHimSad(tweet):
    tweetList = tweet.text.split()
    for word in tweetList:
        if word.lower() == 'sad':
            return True

browser = webdriver.Chrome('enter_path_to_chromedriver')
base_url = u'https://twitter.com/'
query = u'realDonaldTrump'
url = base_url + query

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for i in range(350):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    print(i)

tweets = browser.find_elements_by_class_name('tweet-text')

sadTweets = list(filter(makeHimSad, tweets))

for sadTweet in sadTweets:
    print(sadTweet.text)