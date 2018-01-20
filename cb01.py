import whatsapp
import threading
import queue
import time
import datetime
import youtubeSearch

x = whatsapp.WhatsApp(5000)

#group = "Test group please ignore"
group = "Maf2oud since 1990"
prefix = "⚒ Comrade, "

#x.send_message(group, "hello", prefix)
#x.send_message(group, "world :heart:", prefix)

class bot:
    def __init__(self, whatsappInstance):
        self.client = whatsappInstance
        self.history = []

    def handle_command(self, message):
        """
        1. Check if message object exists in history, if it is then we should exit as to not infinitely loop.
        2. Check if message has the format desired for a command and do stuff if True.
        """
        for i in self.history:
            if message == i:
                return


        # TODO: Eliminate repetitive command code

        if message.content.lower().startswith("%test"):
            """
            Command: Responds with "I'm alive!"
            """
            self.history.append(message) # add this message object to history to signal that it has been acted on
            self.client.send_message(group, "I'm alive!", prefix)

        elif message.content.lower().startswith("%today"):
            """
            Command: Responds with today's date + time (12hr format)
            """
            self.history.append(message)
            n = datetime.datetime.now().strftime("%A %B %d @ %I:%M %p my time")
            self.client.send_message(group, "today is {}".format(n), prefix)

        elif message.content.lower().startswith("%yt"):
            """
            Example: %yt titanic theme song
            Command: Queries youtube for "titanic theme song" and responds with name + url of first result
            """
            self.history.append(message)
            url = message.content.lower()[len("%yt"):].strip() # Get everything after the command invokation "%yt"

            try:
                vid = youtubeSearch.SearchVid(url.replace(" ", "%20"))[0] # Make query string http compatible and search
                self.client.send_message(group, "```{}```  {}".format(vid[0], vid[1]), prefix)
            except Exception as e:
                print(e)

b = bot(x)
q = queue.Queue()
lock = threading.Lock()

check_msgs = True
message_history = []


# TODO: Figure out which sleep-deprived 4 AM coding session synthesized this event loop
def message_checker():
    """
    Since there's no way to detect new messages, we make our own:

    Updates message_history with messages.
    Message Detection step by step:
        1. Grab latest messages up to limit(get_message second param)
        2. Append them to list of all messages
        3. Eliminate duplicate/non-unique messages by converting to a set() and back.

    This allows us to detect new messages by monitoring message_history for new entries.
    """
    global message_history
    while check_msgs:
        check = x.get_message(group, 3)
        #with lock:
        for m in check:
            message_history.append(m)

        message_history = list(set(message_history)) # Convert list to set to remove duplicate Message objects. See Message class for hashing specifics.
        time.sleep(2)

def queue_handler():
    while True:
        item = q.get()
        if item is None:
            break
        func = item[0]
        args = item[1:]
        with lock:
            func(*args) # call func with args under thread lock

mc = threading.Thread(target=message_checker)
qh = threading.Thread(target=queue_handler)
mc.start()
qh.start()
while True:
    for m in message_history:
        q.put(b.handle_command(m))
