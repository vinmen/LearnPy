import pyodbc 
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def run():
    data = get_data()
    email_report(data)


def get_data():
    cnxn = pyodbc.connect("Driver={SQL Server};Server=xxxxxxxx;Database=xxxxxxxxx;uid=xxxxxxxx;pwd=xxxxxxxx;")   
    cursor = cnxn.cursor()
    cursor.execute("select * from table")

    data = "<table border='1' width='50%' cellspacing='0' cellpadding='0'>"
    for row in cursor:
        data = data + "<tr><td>" + str(row[0]) + "</td><td>" + str(row[1]) + "</td><td>" + str(row[2]) + "</td></tr>"
    
    data = data + "</table>"
    return data


def email_report(data):
    fromaddr = "from@123.com"
    toaddr = "to@123.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Report " + datetime.datetime.today().strftime('%m/%d/%Y')
    
    body = data
    msg.attach(MIMEText(body, 'html'))
    
    server = smtplib.SMTP('email.domain.com', 25)
    server.starttls()
    server.login("username", "password")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


if __name__ == "__main__":
    run()
