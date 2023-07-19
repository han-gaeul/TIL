import threading, grpc
from tkinter import *
from tkinter import simpledialog

import chatting_pb2, chatting_pb2_grpc


address = 'localhost'
port = 11912


class Client:
    def __init__(self, u: str,window):
        self.window = window
        self.username = u
        channel = grpc.insecure_channel(address + ':' +str(port))
        self.conn = chatting_pb2_grpc.ChatServerStub(channel)
        threading.Thread(target=self.__listen_for_messages, daemon=True).start()
        self.__setup_ui()
        self.window.mainloop()
    def __listen_for_messages(self):
        for note in self.conn.ChatStream(chatting_pb2.Empty()):
            print("R[{}] {}".format(note.name, note.message))
            self.chat_list.insert(END, "[{}] {}\n".format(note.name, note.message))
    def send_message(self, event):
        message = self.entry_message.get()
        if message != '':
            n = chatting_pb2.Note()
            n.name = self.username
            n.message = message
            print("S[{}] {}".format(n.name, n.message))
            self.conn.SendNote(n)
    def __setup_ui(self):
        self.chat_list = Text()
        self.chat_list.pack(side=TOP)
        self.lbl_username = Label(self.window, text=self.username)
        self.lbl_username.pack(side=LEFT)
        self.entry_message = Entry(self.window, bd=5)
        self.entry_message.bind('<Return>', self.send_message)
        self.entry_message.focus()
        self.entry_message.pack(side=BOTTOM)

if __name__ == '__main__':
    root = Tk()
    frame = Frame(root, width=300, height=300)
    frame.pack()
    root.withdraw()
    username = None
    while username is None:
        username = simpledialog.askstring("Username", "What's your username?", parent=root)
    root.deiconify()
    c = Client(username, frame)