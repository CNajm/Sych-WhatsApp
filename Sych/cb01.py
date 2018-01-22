import whatsapp
import threading
import queue
import time
import datetime
from collections import deque
import ext.youtubeSearch
import ext.wikiSearch

x = whatsapp.WhatsApp(5000)

# This is where we will send and receive messages
#group = "Test group please ignore"
group = "Maf2oud since 1990"

prefix = "⚒ Comrade, "
cmdsymbol = "%"

#x.send_message(group, "hello", prefix)
#x.send_message(group, "world :heart:", prefix)

class bot:
    def __init__(self, whatsappInstance):
        self.client = whatsappInstance
        self.history = deque(maxlen=20)
        # TODO: make prefix a class attribute instead of passing it with every send_message call

    def handle_command(self, message):
        """
        1. Check if message object exists in history, if it is then we should exit as to not infinitely loop.
        2. Check if message has the format desired for a command and do stuff if True.
        """
        for i in self.history:
            if message == i:
                return


        # TODO: Eliminate repetitive command code/more scalable format
        def is_command(command, prefix=cmdsymbol, msg=message):
            if msg.content.lower().startswith(prefix+command):
                self.history.append(message) # add this message object to history to signal that it has been acted on
                return True
            else:
                return False

        # TODO: Wrap context + command under decorator or such
        def get_context(command, msg=message):
            """
            Separates the message context from the command invokation and returns it.
            Example
                %hello world i am an example
                -> "world i am an example"
            """
            context = message.content.lower()[len(cmdsymbol+command):].strip() # Get everything after the command invokation
            return context


        if is_command("test"):
            """
            Command
                Responds with "I'm alive!"
            """
            with lock:
                self.client.send_message(group, "I'm alive!", prefix)


        elif is_command("today"):
            """
            Command
                Responds with today's date + time (12hr format)
            """
            n = datetime.datetime.now().strftime("%A %B %d @ %I:%M %p UTC-8")
            with lock:
                self.client.send_message(group, "today is {}".format(n), prefix)


        elif is_command("yt"):
            """
            Command
                Queries youtube for "titanic theme song" and responds with name + url of first result
            Example
                %yt titanic theme song
            """
            url = get_context("yt")
            try:
                vid = ext.youtubeSearch.SearchVid(url)[0]
                with lock:
                    self.client.send_message(group, "```{}```\n{}".format(vid[0], vid[1]), prefix)
            except Exception as e:
                print(e)


        elif is_command("wiki"):
            """
            Command
                Queries wikipedia using the Opensearch API and responds with wiki page title, url, and short description
            Example
                %wiki
            """
            query = get_context("wiki")
            data = ext.wikiSearch.SearchWiki(query)
            if data:
                msgdata = "I will run a search for _{query}_ :\n*{title}*\n```{content}```\n{url}".format(
                    query     =   data["inputquery"],
                    title     =   data["title"],
                    content   =   data["content"],
                    url       =   data["url"])
            else:
                msgdata = "No results found for _{}_".format(query)

            with lock:
                self.client.send_message(group, msgdata, prefix)


b = bot(x)
q = queue.Queue()
lock = threading.Lock()

check_msgs = True
message_history = deque(maxlen=20)


# TODO: Figure out which sleep-deprived 4 AM coding session synthesized this event loop
def message_checker():
    """
    Since there's no way to detect new messages, we make our own:

    Updates message_history with messages.
    Message Detection step by step:
        1. Grab latest messages up to limit (get_message second param. Think of limit as the look-behind range.)
        2. Append them to list of all messages
        3. Eliminate duplicate/non-unique messages by converting to a set() and back.

    This allows us to detect new messages by monitoring message_history for new entries.
    """
    global message_history
    while check_msgs:
        with lock:
            check = x.get_message(group, 3)
        try:
            for m in check:
                message_history.append(m)
        except TypeError: # This happens when getting the messages fails while they are still loading
            print("typeerror")
            pass

        message_history = deque(list(set(message_history)), maxlen=20) # Convert list to set to remove duplicate Message objects. See Message class for hashing specifics.
        time.sleep(2)

def queue_handler():
    while True:
        item = q.get()
        if item is None:
            break
        func = item[0]
        args = item[1:]
        func(*args) # call func with args under thread lock

mc = threading.Thread(target=message_checker)
qh = threading.Thread(target=queue_handler)
mc.start()
qh.start()
while True:
    for m in list(message_history):
        q.put(b.handle_command(m))
