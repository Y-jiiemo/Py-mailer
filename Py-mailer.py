"""
Email Agent - A simple Python email client
Usage: Run the script and follow prompts to send emails
Requirements: Python 3.x with standard libraries
"""
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import decode_header

# 发送邮件的函数
def send_email(smtp_server, smtp_port, username, password, recipient, subject, body):
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = ','.join(recipient)
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain'))

    # 连接到 SMTP 服务器并发送邮件x    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 启用 TLS 加密
        server.login(username, password)
        server.sendmail(username, recipient, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("邮件发送失败：", e)
        
# 接收邮件的函数
def receive_emails(imap_server, username, password):
    # 连接到 IMAP 服务器
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        mail.select('inbox')  # 选择收件箱

        # 搜索所有邮件
        status, messages = mail.search(None, 'ALL')
        messages = messages[0].split()

        # 遍历邮件并打印基本信息
        for mail_id in messages:
            status, msg_data = mail.fetch(mail_id, '(RFC822)')
            raw_message = msg_data[0][1]
            email_message = email.message_from_bytes(raw_message)

            # 解码邮件主题
            subject = email_message['Subject']
            decoded_subject = ''
            if isinstance(subject, str):
                decoded_header = decode_header(subject)
                for part, encoding in decoded_header:
                    if encoding:
                        decoded_subject += part.decode(encoding)
                    else:
                        decoded_subject += part

            # 打印邮件主题和发件人
            print(f"邮件ID：{mail_id.decode()}")
            print(f"主题：{decoded_subject}")
            print(f"发件人：{email_message['From']}")
            print("-" * 50)

        mail.close()
        mail.logout()
    except Exception as e:
        print("接收邮件失败：", e)

# 主函数
def main(body):
    # 获取用户输入的邮箱信息
    username = "  "  #这里输入您的邮箱地址
    password = "  "  #这里输入您的邮箱授权码 **注意不是登录密码**

    # 邮箱服务器设置 这里使用的是QQ邮箱服务器
    smtp_server = 'smtp.qq.com'
    smtp_port = 587
    imap_server = 'imap.qq.com'

    # 发送邮件
    # ---这里可以直接输入邮件内容或者整合其他模块的内容作为邮件正文 ---
    # 可以直接在函数中写死接收人以及标题内容，也可以通过input()函数获取用户输入
    recipient = input("输入收件人邮箱地址（多个地址用逗号分隔）：").split(',')
    subject = input("输入标题内容：")

    print(recipient,subject,body)

    send_email(smtp_server, smtp_port, username, password, recipient, subject, body)

    # 接收邮件
    # receive_emails(imap_server, username, password)
body = input("输入邮件内容：") #这里输入邮件内容

if __name__ == "__main__":
    main(body)
