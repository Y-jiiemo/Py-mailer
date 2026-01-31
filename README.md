# 📧 Python Email Agent

A lightweight and secure Python-based email agent for sending and receiving emails via SMTP/IMAP protocols. Perfect for automating email notifications, alerts, and integrating email functionality into your applications.

## ✨ Features

- **📤 Send Emails** - Send emails to multiple recipients with TLS encryption
- **📥 Receive Emails** - Fetch and parse emails from your inbox via IMAP
- **🔒 Secure** - Uses TLS encryption and supports app passwords/authorization codes
- **🚀 Easy to Use** - Simple command-line interface and programmable API
- **🔄 Extensible** - Built with standard Python libraries, easy to customize

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/Y-jiiemo/Py-mailer.git
cd mail-agent

# No additional dependencies required!
# Uses Python's standard library
```

## 🚀 Quick Start

1. **Configure your email settings** (using QQ Mail as example):

```python
# In the script, update these variables:
username = "your-email@qq.com"  # Your email address
password = "your-authorization-code"  # Your email authorization code (not password)
```

2. **Run the script**:

```bash
Py-mailer.py
```

3. **Follow the prompts** to send emails.

## 📋 Usage Examples

### Send an Email
```python
# Programmatic usage
from mail_agent import send_email

send_email(
    smtp_server='smtp.qq.com',
    smtp_port=587,
    username='your-email@qq.com',
    password='your-auth-code',
    recipient=['recipient1@example.com', 'recipient2@example.com'],
    subject='Hello from Python!',
    body='This email was sent using Python Email Agent.'
)
```

### Receive Emails
```python
# Fetch and display recent emails
from Py-mailer import receive_emails

receive_emails(
    imap_server='imap.qq.com',
    username='your-email@qq.com',
    password='your-auth-code'
)
```

## 🔧 Configuration

### Supported Email Providers
This script works with any email provider that supports SMTP/IMAP:

| Provider | SMTP Server | IMAP Server | Port |
|----------|-------------|-------------|------|
| QQ Mail | smtp.qq.com | imap.qq.com | 587 |
| Gmail | smtp.gmail.com | imap.gmail.com | 587 |
| Outlook | smtp.office365.com | outlook.office365.com | 587 |

### Getting Authorization Codes
Most email providers require an **app-specific password** or **authorization code** instead of your regular password:

- **QQ Mail**: Settings → Account → Generate Authorization Code
- **Gmail**: Google Account → Security → App Passwords
- **Outlook**: Microsoft Account → Security → App Passwords

## 📁 Project Structure

```
mail-agent/
├── Py-mailer.py          # Main email agent script
├── README.md               # This documentation
├── requirements.txt        # Dependencies (none for now)
├── examples/               # Usage examples
│   ├── send_notification.py
│   └── check_inbox.py
└── tests/                  # Test scripts
    └── test_email_agent.py
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- Add HTML email support
- Implement email attachment handling
- Add email filtering and searching
- Create a GUI interface
- Add logging and error handling improvements

## ⚠️ Important Notes

- **Never commit your actual email credentials** to version control
- Use environment variables or configuration files for sensitive data
- Different email providers have different security requirements
- Some providers may require enabling "Less Secure Apps" or similar settings

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with Python's standard `smtplib`, `imaplib`, and `email` libraries
- Inspired by various email automation needs
- Thanks to all contributors who help improve this project

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/Y-jiiemo/Py-mailer/issues) page
2. Create a new issue with detailed information
3. Include your Python version and email provider details

---

**Happy Emailing!** 🚀

*Disclaimer: This tool is for legitimate email automation purposes only. Please respect email service terms and anti-spam regulations.*
