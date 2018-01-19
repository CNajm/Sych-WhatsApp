import whatsapp
import threading
import queue
import time
import datetime
import youtubeSearch

x = whatsapp.WhatsApp(5000)

group = "Test group please ignore"
#group = "Maf2oud since 1990"
prefix = "⚒ Comrade, "

#x.send_message(group, "hello", prefix)
#x.send_message(group, "world :heart:", prefix)

check_msgs = True
message_history = []
lock = threading.Lock()

def message_checker():
    global message_history
    while check_msgs:
        check = x.get_message(group, 3)
        #message_history.append(check)
        
        with lock:
            for m in check:
                message_history.append(m)

            message_history = list(set(message_history))
        #print(message_history)
        time.sleep(2)
# def monitor(currentH, oldH):
#     m_history = set(oldH) - set(currentH)
#     for m in m_history:
#         if m.content.startswith("%"):
#             handle_command(m)
#
#     monitor(oldH)
#     time.sleep(3)
class bot:
    def __init__(self, whatsappInstance):
        self.client = whatsappInstance
        self.history = []

    # def cmdPrefix(message):
    #     if message.content.lower().startswith("%"):
    #         return True
    #     else:
    #         return False

    def handle_command(self, message):
        for i in self.history:
            if message == i:
                return
        
        # TODO: Eliminate repetitive command code
        if message.content.lower().startswith("%test"):
            self.history.append(message)
            self.client.send_message(group, "I'm alive!", prefix)

        elif message.content.lower().startswith("%today"):
            self.history.append(message)
            n = datetime.datetime.now().strftime("%A %B %d @ %I:%M %p my time")
            self.client.send_message(group, "today is {}".format(n), prefix)

        elif message.content.lower().startswith("%yt"):
            self.history.append(message)
            url = message.content.lower()[len("%yt"):].strip()

            try:
                vid = youtubeSearch.SearchVid(url.replace(" ", "%20"))[0]
                self.client.send_message(group, "```{}```  {}".format(vid[0], vid[1]), prefix)
            except Exception as e:
                print(e)

t = threading.Thread(target=message_checker)
t.start()
b = bot(x)
q = queue.Queue()
while True:
    for m in message_history:
        q.put(b.handle_command(m))

def queue_handler():
    while True:
        item = q.get()
        if item is None:
            break
        func = item[0]
        args = item[1:]
        with lock:
            func(*args)
#
#
t = threading.Thread(target=queue_handler)
t.start()
print(t)

from random import randint
