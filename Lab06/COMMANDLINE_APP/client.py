import grpc

import getStudent_pb2
import getStudent_pb2_grpc


def client():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = getStudent_pb2_grpc.getStudentStub(channel)
        response = stub.getByID(getStudent_pb2.inputSID(sid=17021254))
    print("Student's name: " + response.name)
    print("Student's ID: " + response.sid)
    print("Student's gender: " + response.gender)
    print("Student's date of birth: " + response.dob)
    print("Student's email: " + response.email)
    # print(response)

if __name__ == '__main__':
    # logging.basicConfig()
    client()