import ast
import collections
import sys

from flask import Flask, jsonify, request
import csv
import mysql.connector
import json

app = Flask(__name__)

db = mysql.connector.connect(host="localhost", user="root", password="test.Password", database="SOA")


@app.route('/getbyid', methods=['POST'])
def getStudentBySID():
    requestJSON = request.json
    requestRaw = requestJSON["InputSID"]
    requestSID = (requestRaw,)
    #print(requestSID, file=sys.stdout)
    basicInfoCursor = db.cursor()

    getInfoQuerry = "SELECT * FROM personalInfo WHERE SID = %s"
    basicInfoCursor.execute(getInfoQuerry, requestSID)
    basicInfoFetched = basicInfoCursor.fetchall()

    basicInfo = dict()
    for row in basicInfoFetched:
        basicInfo["SID"] = row[0]
        basicInfo["name"] = row[1]
        basicInfo["gender"] = row[2]
        basicInfo["DOB"] = row[3].strftime("%Y-%m-%d")
    # print(basicInfo)

    emailCursor = db.cursor()
    getEmailQuerry = "SELECT * FROM email WHERE SID = %s"
    emailCursor.execute(getEmailQuerry, requestSID)
    emailFetched = emailCursor.fetchall()
    email = []
    for row in emailFetched:
        email.append(row[1])
    # print(email)
    # print(emailDict)

    relativeCursor = db.cursor()
    getRelativeQuerry = "SELECT * FROM relative WHERE SID = %s"
    relativeCursor.execute(getRelativeQuerry, requestSID)
    relativeFetched = relativeCursor.fetchall()

    relative = []
    for row in relativeFetched:
        relativeHandler = dict()
        relativeHandler["relationship"] = row[1]
        relativeHandler["name"] = row[2]
        relativeHandler["address"] = row[3]
        temp = dict()
        temp["person"] = relativeHandler
        relative.append(temp)
    # print(relative)

    resultCompositor = dict()
    resultCompositor = basicInfo
    resultCompositor["email"] = email
    resultCompositor["relative"] = relative
    # print(resultCompositor)
    result = dict()
    result["personalInfo"] = resultCompositor
    #print(result)

    return result



if __name__ == '__main__':

    app.run(host='localhost', port='5000', debug=True)
    # getStudentBySID()

