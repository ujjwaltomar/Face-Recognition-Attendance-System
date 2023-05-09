import os
import yagmail

receiver = "reviever@gmail.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance_2019-08-29_13-09-07.csv"  # attach the file

# mail information
yag = yagmail.SMTP("jojozodiac4@gmail.com", "HP L1706@jt")

# sent the mail
yag.send(
    to="ujjwaltomar123@gmail.com",
    subject="Attendance Report",  # email subject
    contents=body,  # email body
    attachments=filename,  # file attached
)
