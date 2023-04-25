from flask import Flask
app = Flask(__name__)

@app.route('/',  methods=['GET'])
def helloIndex():
    myReply = popHead();
    myReply += popH1('Welcome to SDEV 300- The Web App!')
    myReply += "<p></p>"
    myReply += popTable()
    myReply += popEnd()
    return myReply

def popH1(myString):
    newString = '<H1>' + myString + '</H1>'
    return newString

def popTable():
    tabledata = "<table> <thead>"
    tabledata += "<tr><th>Date</th><th>Holiday</th></tr></thead>"
    tabledata += "<tbody><tr><td>Jan 1</td> <td> New Years Day </td></tr>"
    tabledata += "<tr><td>May 26</td> <td> Memorial Day </td></tr>"
    tabledata += "<tr><td>Oct 31</td> <td> Halloween </td></tr>"
    tabledata += "</tbody></table>"
    return tabledata

def popHead():
    headData = "<!DOCTYPE html> "
    headData +="<head> "
    headData +="<title>Flask Shop</title>"
    headData +="<style>" + getStyle() + "</style>"
    headData +="</head>"
    headData +="<body>"
    return headData

def getStyle():
    myStyle = "table,td {"
    myStyle += "border: 5px solid #117;"
    myStyle += "}"
    return myStyle

def popEnd():
    endData = "</body>"
    endData += "</html>"
    return endData

app.run()