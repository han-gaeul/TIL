import time, grpc
from concurrent import futures

import chatting_pb2, chatting_pb2_grpc

class ChatServer(chatting_pb2_grpc.ChatServerServicer):
    def __init__(self):
        self.chats = []
    def ChatStream(self, request, context):
        lastindex = 0
        while True:
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n
    def SendNote(self, request, context):
        print("[{}] {}".format(request.name, request.message))
        self.chats.append(request)
        return chatting_pb2.Empty()

if __name__ == '__main__':
    port = 11912
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chatting_pb2_grpc.add_ChatServerServicer_to_server(ChatServer(), server)
    print('Starting server...')
    server.add_insecure_port('[::]:' + str(port))
    server.start()
    while True:
        time.sleep((64 * 64 * 100))