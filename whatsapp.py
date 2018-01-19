import time
import datetime as dt
import json
import logging
import random
from dateutil.parser import parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

logging.basicConfig(level=logging.INFO)# Set up logger. This lets us switch console outputs on and off easily rather than have many print statements

class Message:
    """
    Represents a message object
    """
    def __init__(self, date, sender, content):
        self.in_or_out = ""
        self.status = "" # TODO: Return metadata Sent/Received/Read(OneCheck/TwoGreyChecks/TwoBlueChecks) from class="status-icon" div
        self.date = date
        self.sender = sender
        self.content = content

        self.hashed = (self.date, self.sender, self.content)
    def __hash__(self):
        return hash(self.hashed)

    def __eq__(self, other):
        if not isinstance(other, Message):
            # only equality checks to other Message instances supported
            return NotImplemented
        return self.hashed == other.hashed

        # def __repr__(self):
        #     return '<message({!r})>'.format(self.hashed)



class WhatsApp:
    """
    Main class used to interact with whatsapp web
    """
    emoji = {}  # This dict will contain all emojis needed for chatting
    #browser = webdriver.Chrome(executable_path="chromedriver.exe") # we are using chrome as our webbrowser
    browser = webdriver.Chrome()
    timeout = 10  # The timeout is set for about ten seconds

    # This constructor will load all the emojies present in the json file and it will initialize the webdriver
    def __init__(self, wait, screenshot=None):
        self.browser.get("https://web.whatsapp.com/")
        # emoji.json is a json file which contains all the emojis
        with open("emoji.json") as emojies:
            self.emoji = json.load(emojies)  # This will load the emojies present in the json file into the dict
        WebDriverWait(self.browser,wait).until(EC.presence_of_element_located((By.ID, "input-chatlist-search")))
        if screenshot is not None:
            self.browser.save_screenshot(screenshot)  # This will save the screenshot to the specified file location

    # This method is used to send the message to the individual person or a group
    # will return true if the message has been sent, false else

    def navigate(self, name):
        try:
            chatHeader = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "header.pane-chat-header > div.chat-body > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")))
            assert name == chatHeader.get_attribute("title")
        except:
            pass
        else:
            return chatHeader
        search = self.browser.find_element_by_id("input-chatlist-search")
        search.send_keys(name)  # we will send the name to the input key box
        time.sleep(random.uniform(0.3, 0.8)) # Artificial, humanizing delay
        search.send_keys(Keys.ENTER)
        current_time = time.time()
        try:
            chatHeader = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "header.pane-chat-header > div.chat-body > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")))
            assert name == chatHeader.get_attribute("title") # Make sure current chat name is the same as receipient name

        except TimeoutException:
            raise TimeoutError("Request has been timed out!")
            return False
        except NoSuchElementException:
            return False
        except Exception as e:
            print(e)
            return False

        else:
            return chatHeader

    def send_message(self, name, message, prefix=None):
        """
        Send message by contact/group name
        Returns
            Bool : Success Status
        """
        message = self.emojify(message)  # emojify all emoji present as text in string
        if prefix:
            message = prefix + message

        chatHeader = self.navigate(name)
        send_msg = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
            (By.CLASS_NAME, "input-container"))) # Grab input box
        #     chatHeader = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, "header.pane-chat-header > div.chat-body > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")))
        #     assert name == chatHeader.get_attribute("title") # Make sure current chat name is the same as receipient name

        time.sleep(random.uniform(0.7, 1.3))
        send_msg.send_keys(message+Keys.ENTER) # send the message
        logging.info("Sent to " + format(chatHeader.get_attribute("title")))
        time.sleep(random.uniform(0.3, 0.8))
        return True

        # except TimeoutException:
        #     raise TimeoutError("Request has been timed out!")
        #     return False
        # except NoSuchElementException:
        #     return False
        # except Exception as e:
        #     print(e)
        #     return False

    def get_message(self, name, limit):
        """
        Get messages by contact/group name

        Params
            name  : Contact/Group name to return messages from
            limit : Maximum number of messages to return

        Returns
            if successful
                Message : Message object containing data
            if unsuccessful
                Bool : False
        """
        self.navigate(name)
        #time.sleep(4)
        msgPaneBody = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
             (By.CLASS_NAME, "pane-chat-msgs")))
        msgBody = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
             (By.CLASS_NAME, "msg")))
        try:
            msgs = self.browser.find_elements(By.CSS_SELECTOR, "div.msg > div.message-chat") # > div:nth-child(1) > div:nth-child(1) > div.copyable-text")
            msgs.reverse() # Get latest msgs
            msgList = []
            for count, m in enumerate(msgs):
                if count >= limit:
                    break

                content = msgs[count].find_element(By.CSS_SELECTOR, "div.copyable-text")
                #print(content.text)
                #print(content.get_attribute('data-pre-plain-text'))
                metaC = content.get_attribute('data-pre-plain-text').strip().split(']')
                metaDate = parse(metaC[0].replace('[',''))
                metaSender = metaC[1].strip().replace(':','')
                msgList.append(Message(metaDate, metaSender, content.text))

        except Exception as e:
            raise(e)
            return False
        else:
            return msgList
            # return {
            #         'success' : True,
            #         'date'    : metaDate,
            #         'sender'  : metaSender,
            #         'text'    : content.text
            #         }

    #
    # Below code has not been updated yet and may not work. It will be in the near future.
    #

    # This method will count the no of participants for the group name provided
    def participants_for_group(self, group_name):
        search = self.browser.find_element_by_class_name("input-search")
        search.send_keys(group_name+Keys.ENTER)  # we will send the name to the input key box
        # some say this two try catch below can be grouped into one
        # but I have some version specific issues with chrome [Other element would receive a click]
        # in older versions. So I have handled it spereately since it clicks and throws the exception
        # it is handled safely
        try:
            click_menu = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "header.pane-header:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")))
            click_menu.click()
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException as e:
            return "None"
        except Exception as e:
            return "None"
        current_time = dt.datetime.now()
        participants_css_selector = "div.animate-enter2:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)"
        while True:
            try:
                participants_count = self.browser.find_element_by_css_selector(participants_css_selector).text
                if "256" in participants_count:
                    return participants_count
            except Exception as e:
                pass
            new_time = dt.datetime.now()
            elapsed_time = (new_time - current_time).seconds
            if elapsed_time > self.timeout:
                return "NONE"

    # This method is used to get the main page
    def goto_main(self):
        self.browser.get("https://web.whatsapp.com/")

    # get the status message of a person
    # TimeOut is approximately set to 10 seconds
    def get_status(self, name):
        search = self.browser.find_element_by_class_name("input-search")
        search.send_keys(name+Keys.ENTER)  # we will send the name to the input key box
        try:
            group_xpath = "/html/body/div/div/div/div[3]/header/div[1]/div/span/img"
            click_menu = WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.XPATH, group_xpath)))
            click_menu.click()
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return "None"
        except Exception:
            return "None"
        try:
            status_css_selector = ".drawer-section-body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"   # This is the css selector for status
            WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, status_css_selector)))
            status = self.browser.find_element_by_css_selector(status_css_selector).text
            # We will try for 100 times to get the status
            for i in range(10):
                if len(status) > 0:
                    return status
                else:
                    time.sleep(1) # we need some delay
            return "None"
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return "None"
        except Exception:
            return "None"

    # to get the last seen of the person
    def get_last_seen(self, name, timeout=10):
        search = self.browser.find_element_by_class_name("input-search")
        search.send_keys(name+Keys.ENTER)  # we will send the name to the input key box
        last_seen_css_selector = ".chat-subtitle-text"
        start_time = dt.datetime.now()
        try:
            WebDriverWait(self.browser,self.timeout).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, last_seen_css_selector)))
            while True:
                last_seen = self.browser.find_element_by_css_selector(last_seen_css_selector).text
                if last_seen and "click here" not in last_seen:
                    return last_seen
                end_time = dt.datetime.now()
                elapsed_time = (end_time-start_time).seconds
                if elapsed_time > 10:
                    return "None"
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return "None"
        except Exception:
            return "None"

    # This method does not care about anything, it sends message to the currently active chat
    # you can use this method to recursively send the messages to the same person
    def send_blind_message(self, message):
        try:
            message = self.emojify(message)
            send_msg = self.browser.find_element_by_class_name("input")
            send_msg.send_keys(message+Keys.ENTER)  # send the message
            return True
        except selenium.common.exceptions.NoSuchElementException:
            return "Unable to Locate the element"
        except Exception as e:
            return False

    # override the timeout
    def override_timeout(self, new_timeout):
        self.timeout = new_timeout

    # This method is used to emojify all the text emoji's present in the message
    def emojify(self,message):
        for emoji in self.emoji:
            message = message.replace(emoji, self.emoji[emoji])
        return message

    # This method is used to quit the browser
    def quit(self):
        self.browser.quit()

if __name__ == "__main__":
    pass
