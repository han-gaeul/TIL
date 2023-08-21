# Python gRPC Server/Client 구현하기





### 💡목적

------

gRPC 동작 방식에 대해 이해하고, 직접 구현해보는 것





### ⚙️동작 방식

------

![Untitled](C:/Users/tritech-fall/Desktop/TIL/office/study/gRPC.assets/Untitled.png)

1. 프로토콜 버퍼(Protobuf) 정의
    1. 클라이언트와 서버 간의 통신에 사용할 데이터 형식을 정의하는 프로토콜 버퍼 파일 작성
    2. 구조화된 데이터를 직렬화 하고, 다양한 언어 간에 데이터를 교환하는 데 사용
2. 프로토콜 버퍼 컴파일
    1. 작성한 프로토콜 버퍼 파일을 `protoc` 이라는 컴파일러를 사용해 클라이언트 및 서버 언어에 맞는 코드로 변환
    2. 데이터 메시지와 통신을 위한 서비스 코드가 포함됨
3. 서버 구현
    1. gRPC 서비스를 구현
    2. 프로토콜 버퍼에서 생성된 서비스 인터페이스를 구현하고, 클라이언트 요청을 처리하는 메소드 작성
    3. gRPC 서비스를 제공하는 네트워크 서비스로 동작하며, 클라이언트로부터 요청을 수신하고 응답 반환
4. 클라이언트 호출
    1. 클라이언트는 gRPC 서비스를 호출하여 서버에 데이터를 보냄
    2. 클라이언트는 프로토콜 버퍼에서 생성된 클라이언트 스텁을 사용해 서버의 메소드를 호출하고, 요청과 함께 데이터 전달
5. 네트워크 통신
    1. 클라이언트의 요청은 네트워크를 통해 서버로 전달
    2. 기본적으로 HTTP/2 프로토콜을 사용해 양방향 스트리밍 통신을 지원
6. 요청 및 응답 처리
    1. 서버는 클라이언트의 요청을 수신하고 해당 요청을 처리하여, 응답을 생성하고 클라이언트로 반환
    2. 응답은 프로토콜 버퍼로 직렬화 되어 네트워크를 통해 클라이언트로 전송
7. 클라이언트 응답 처리
    1. 클라이언트는 서버에서 수신한 응답을 받아 처리
    2. 응답은 프로토콜 버퍼 형식으로 수신 되며, 클라이언트는 해당 응답을 역직렬화하여 사용 가능한 형식으로 변환





### 👩🏻‍💻pip 설치

------

**#gRPC**

```bash
$ python -m pip install grpcio
```

**#gRPC 도구**

```bash
$ python -m pip install grpcio-tools
```





### ⌨️calc.proto 버퍼 작성

------

- 파일 경로

    - `C:\\Users\\tritech-fall\\Desktop\\grpc_test\\proto`

        ![Untitled](C:/Users/tritech-fall/Desktop/TIL/office/study/gRPC.assets/Untitled-1692580964188-2.png)

- 사칙연산의 Input, Output 결과값을 Server, Client에서 알 수 있는 Service와 Message 작성

```python
syntax = "proto3";

package calc;

service Calculator {
    rpc Add (AddRequest) returns (AddReply) {}
    rpc Substract (SubstractRequest) returns (SubstractReply) {}
    rpc Multiply (MultiplyRequest) returns (MultiplyReply) {}
    rpc Divide (DivideRequest) returns (DivideReply) {}
}

message AddRequest {
    int32 n1 = 1;
    int32 n2 = 2;
}
message AddReply {
    int32 n1 = 1;
}

message SubstractRequest {
    int32 n1 = 1;
    int32 n2 = 2;
}
message SubstractReply {
    int32 n1 = 1;
}

message MultiplyRequest {
    int32 n1 = 1;
    int32 n2 = 2;
}
message MultiplyReply {
    int32 n1 = 1;
}

message DivideRequest {
    int32 n1 = 1;
    int32 n2 = 2;
}
message DivideReply {
    float f1 = 1;
}
```





### 💾proto 컴파일

------

- calc.proto 버퍼를 python에서 직접 grpc.proto를 이용해 컴파일
- Python 코드로 calc.proto 버퍼 내용의 함수들이 자동으로 생성 됨
- 다음 명령어를 실행하면 calc_pb2.py, calc_pb2_grpc.py 2개의 파일이 자동 생성 됨

```bash
# 절대 경로
$ python -m grpc_tools.protoc -I/C/Users/tritech-fall/Desktop/grpc_test/proto --python_out=. --grpc_python_out=./C/Users/tritech-fall/Desktop/grpc_test/proto/calc.proto

# 상대 경로
$ python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/calc.proto
```

- `-I=<proto 파일 경로> --<언어>_out=<출력 디렉토리> <proto 파일>`

- 에러 사항(해결)

    1. 파일 경로를 상대 경로로 설정하다 보니 컴파일이 제대로 되지 않음 → 절대 경로로 설정해 명령어를 입력하니 파일 생성이 잘 되었음

    2. protoc directory does not exist

        1. https://github.com/protocolbuffers/protobuf/releases 해당 링크로 들어가 현재 환경에 맞는 protoc 다운로드

        2. `C:\\Users\\tritech-fall\\Desktop\\grpc_test` 경로에 압축 해제

            ![Untitled](C:/Users/tritech-fall/Desktop/TIL/office/study/gRPC.assets/Untitled-1692581104783-4.png)

    3. 시스템 환경 변수 설정

        1. PATH 등록

            1. `C:\\Users\\tritech-fall\\Desktop\\grpc_test\\proto-23.4-win64\\bin` 경로 추가

                ![Untitled](C:/Users/tritech-fall/Desktop/TIL/office/study/gRPC.assets/Untitled-1692581205706-6.png)





### 📑Server/Client 작성

------

**#Server**

```python
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
```

**#Client**

```python
import grpc

import calc_pb2, calc_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50050')
    stub = calc_pb2_grpc.CalculatorStub(channel)
    respones = stub.Add(calc_pb2.AddRequest(n1=20, n2=10))
    print(respones.n1)
    respones = stub.Substract(calc_pb2.SubstractRequest(n1=20, n2=10))
    print(respones.n1)
    respones = stub.Multiply(calc_pb2.MultiplyRequest(n1=20, n2=10))
    print(respones.n1)
    respones = stub.Divide(calc_pb2.DivideRequest(n1=10, n2=2))
    print(respones.f1)

if __name__ == '__main__':
    run()
```





### 🔓실행

------

**#Server**

- server.py가 있는 경로에서 실행

```bash
$ python server.py
```

**#Client**

- 실행 결과

```bash
$ python client.py
30
10
200
2.0
```





### 💻채팅 만들기

---

[python-grpc-chat](https://github.com/melledijkstra/python-grpc-chat)