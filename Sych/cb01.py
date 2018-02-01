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
#group = "Maf2oud since 1990"
group = "?this_search_will_fail"

prefix = "⚒ Comrade, "
cmdsymbol = "%"

#x.send_message(group, "hello", prefix)
#x.send_message(group, "world :heart:", prefix)

class bot:
    def __init__(self, whatsappInstance):
        self.client = whatsappInstance
        self.message_history = deque(maxlen=20)
        self.history = deque(maxlen=20)

        self.q = queue.Queue()
        self.lock = threading.Lock()
        self.check_msgs = True

        # TODO: make prefix a class attribute instead of passing it with every send_message call

    def send_message(self, to, msg, prefix=prefix):
        with self.lock:
            self.client.send_message(to, msg, prefix)

    def handle_command(self, message):
        # TODO: Eliminate repetitive command code/more scalable format
        def command(command, prefix=cmdsymbol, msg=message):
            if msg.content.lower().startswith(prefix + command):
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




        if command("test"):
            """
            Command
                Responds with "I'm alive!"
            """
            self.send_message(group, "I'm alive!")


        elif command("today"):
            """
            Command
                Responds with today's date + time (12hr format)
            """
            n = datetime.datetime.now().strftime("%A %B %d @ %I:%M %p UTC-8")
            self.send_message(group, "today is {}".format(n))


        elif command("yt"):
            """
            Command
                Queries youtube for "titanic theme song" and responds with name + url of first result
            Example
                %yt titanic theme song
            """
            url = get_context("yt")
            try:
                vid = ext.youtubeSearch.SearchVid(url)[0]
                self.send_message(group, "```{}```\n{}".format(vid[0], vid[1]))
            except Exception as e:
                print(e)


        elif command("wiki"):
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

            self.send_message(group, msgdata)


    # TODO: Figure out which sleep-deprived 4 AM coding session synthesized this event loop
    def message_checker(self):
        """
        Since there's no way to detect new messages, we make our own:

        Updates message_history with messages.
        Message Detection step by step:
            1. Grab latest messages up to limit (get_message second param. Think of limit as the look-behind range.)
            2. Append them to list of all messages
            3. Eliminate duplicate/non-unique messages by converting to a set() and back.

        This allows us to detect new messages by monitoring message_history for new entries.
        """
        while self.check_msgs:
            with self.lock:
                check = x.get_message(group, 3) # How many prev. messages to get
            try:
                for m in check:
                    self.message_history.append(m)
            except TypeError: # This happens when getting the messages fails while they are still loading
                print("typeerror")
                pass

            self.message_history = deque(list(set(self.message_history)), maxlen=20) # Convert list to set to remove duplicate Message objects. See Message class for hashing specifics.
            time.sleep(2) # How many seconds to wait between checks

    def queue_handler(self):
        while True:
            item = self.q.get()
            if item is None:
                break
            func = item[0]
            args = item[1:]
            func(*args)

    def messageIsNew(self, message):
        for old_message in self.history:
            if message == old_message:
                return False
        return True

    def run(self):
        """
        1. Check if message object is new
        2. If it is, then
            add it to the queue to be handled
            add it to the command history so it is not looped over again.
        """
        mc = threading.Thread(target=self.message_checker)
        qh = threading.Thread(target=self.queue_handler)
        mc.start()
        qh.start()
        while True:
            for m in reversed(list(self.message_history)): # Handle oldest messages first
                if self.messageIsNew(m):
                    self.q.put(self.handle_command(m)) # If message is new, handle it and add it to history so we don't handle it again.
                    self.history.append(m)

#b = bot(x).run()
print(x.send_message(group, "a", prefix))
print(x.send_message(group, "as", prefix))
print(x.send_message(group, "asd", prefix))
print(x.send_message(group, "asd@", prefix))
print(x.send_message(group, "asd@#", prefix))
print(x.send_message(group, "asd@#$", prefix))
print(x.send_message(group, "asd@#$@", prefix))
print(x.send_message(group, "asd@#$@e", prefix))
print(x.send_message(group, "asd@#$@ex", prefix))
print(x.send_message(group, "asd@#$@exz", prefix))