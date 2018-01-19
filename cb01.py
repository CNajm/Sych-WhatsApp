import whatsapp
import threading
import queue
import time
import datetime
import youtubeSearch

x = whatsapp.WhatsApp(5000)

#group = "Test group please ignore"
group = "Maf2oud since 1990"
#group = "Tony carlosFriend"
prefix = "⚒ Comrade, "

#x.send_message(group, "hello", prefix)
#x.send_message(group, "world :heart:", prefix)

# message_history = x.get_message(group, 2)
# time.sleep(4)
# v = x.get_message(group, 2)
# print(message_history)
# print("2nd:~")
# print(v)
# print("merge")
# merg = message_history+v
# print(merg)
# print("set")
# a = set(merg)
#print(a)


# for m in a:
#     print(m == list(a)[0])
#     print("{}: {} : {:%m/%d/%Y}".format(m.sender,m.content,m.date))

check_msgs = True
message_history = []

def message_checker():
    global message_history
    while check_msgs:
        check = x.get_message(group, 3)
        #message_history.append(check)
        for m in check:
            message_history.append(m)

        message_history = list(set(message_history))
        #print(message_history)
        time.sleep(1)
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

        if message.content.lower().startswith("%testes"):
            self.history.append(message)
            self.client.send_message(group, "IM ALIIIIVE", prefix)

        elif message.content.lower().startswith("%istodaywednesday"):
            self.history.append(message)
            n = datetime.datetime.now().strftime("%A %B %d @ %I:%M %p my time")
            self.client.send_message(group, ":c unfortunately, today is {}".format(n), prefix)

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
while True:
    for m in message_history:
        b.handle_command(m)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.ensure_future(message_checker(), loop=loop))

# q = queue.Queue()
# def queue_handler():
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         func = item[0]
#         args = item[1:]
#         func(*args)
#
#
# t = threading.Thread(target=queue_handler)
# t.start()
# print(t)

from random import randint
# #print(x.send_message(group, "test_001_010_{}".format(randint(1,100)), prefix))
# v = x.get_message(group, 10)
# for m in v:
#     print(m.sender, ": ", m.content, m.date)
