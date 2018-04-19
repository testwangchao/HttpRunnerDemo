import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os


def send_email(file):
    # 发送邮箱
    sender = "937129141@qq.com"
    # 接受邮箱
    receiver = "15201403874@163.com"
    # title
    title = "demo"
    # server
    server = "smtp.qq.com"
    # sender data
    username = "937129141"
    passwd = "jvezcostromebffd"
    # text
    f = open(file, 'rb')
    mail_body = f.read()
    f.close()
    # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = Header(title, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver
    # 登录并发送邮件
    try:
        smtp = smtplib.SMTP_SSL(server, port=465)
        smtp.login(username, passwd)
        smtp.sendmail(sender, receiver, msg.as_string())
    except:
        print("邮件发送失败！")
    else:
        print("邮件发送成功！")
    finally:
        smtp.quit()


def main():
    path = os.getcwd()+"/reports/"
    for file in os.listdir(path):
        if os.path.isfile(path + file):
            html_path = path + file
            send_email(html_path)
    # print(os.getcwd())

if __name__ == '__main__':
    main()
