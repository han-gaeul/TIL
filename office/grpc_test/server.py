from concurrent import futures
import grpc

import calc_pb2, calc_pb2_grpc


class Calcuator(calc_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return calc_pb2.AddReply(n1=request.n1 + request.n2)
    def Substract(self, request, context):
        return calc_pb2.SubstractReply(n1=request.n1 - request.n2)
    def Multiply(self, request, context):
        return calc_pb2.MultiplyReply(n1=request.n1 * request.n2)
    def Divide(self, request, context):
        return calc_pb2.DivideReply(f1=request.n1 / request.n2)

def serve():
    print("Server Start...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calc_pb2_grpc.add_CalculatorServicer_to_server(Calcuator(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()