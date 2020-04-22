import smtplib
from email.mime.text import MIMEText

def send_mail(msg):
    msg_from='1301862177@qq.com'
    passwd='**********'
    msg_to='1301862177@qq.com'
                                
    subject="email subject"
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465)
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("send mail success, MESSAGE:\n{msg}".format(msg=msg))
    except s.SMTPException as e:
        print("send mail failed, ERROR:\n{err}".format(err=str(e)))
    finally:
        s.quit()