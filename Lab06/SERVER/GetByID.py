import mysql.connector
import grpc
from concurrent import futures
import getStudent_pb2
import getStudent_pb2_grpc

class getStudentServicer(getStudent_pb2_grpc.getStudentServicer):
    def getByID(self, request, context):
        print("Function started.")

        #print(requestSID)
        result = getStudent_pb2.studentInfo
        requestProc = (request.sid,)
        db = mysql.connector.connect(host="localhost", user="root", password="test.Password", database="SOA")
        basicInfoCursor = db.cursor()
        getInfoQuerry = "SELECT * FROM personalInfo WHERE SID = %s"
        basicInfoCursor.execute(getInfoQuerry, requestProc)
        basicInfoFetched = basicInfoCursor.fetchall()

        # basicInfo = dict()
        for row in basicInfoFetched:
            result.sid = row[0]
            result.name = row[1]
            result.gender = row[2]
            result.dob = row[3].strftime("%Y-%m-%d")
        # print(basicInfo)
        basicInfoCursor.close()
        print("Requested SID: " + result.sid)

        emailCursor = db.cursor()
        getEmailQuerry = "SELECT * FROM email WHERE SID = %s"
        emailCursor.execute(getEmailQuerry, requestProc)
        emailFetched = emailCursor.fetchall()
        email = []
        for row in emailFetched:
            email.append(row[1])
        # print(email)
        # print(emailDict)
        result.email = email
        emailCursor.close()

        relativeCursor = db.cursor()
        getRelativeQuerry = "SELECT * FROM relative WHERE SID = %s"
        relativeCursor.execute(getRelativeQuerry, requestProc)
        relativeFetched = relativeCursor.fetchall()

        relative = []
        for row in relativeFetched:
            relativeHandler = getStudent_pb2.relative
            relativeHandler.relationship = row[1]
            relativeHandler.relaName = row[2]
            relativeHandler.address = row[3]
            relative = relative + [relativeHandler]
            # result.person.extend([relativeHandler])
        # print(relative)

        result.person = relative
        relativeCursor.close()
        # print("Person object array struct " + result.person)
        print("Function successfully terminated.")
        return result

def serve() :
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    getStudent_pb2_grpc.add_getStudentServicer_to_server(getStudentServicer(), server)

    print('Server started. Listening on port 50051.')
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()