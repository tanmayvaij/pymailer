import smtplib

HOST = "smtp.gmail.com"
PORT = 587

FROM_EMAIL = "tejastestemail23@gmail.com"
PASSWORD = "Tejas@123"

TO_EMAIL = "tanmayvaij22@gmail.com"

MESSAGE = """
Message using python
"""

smtp = smtplib.SMTP(HOST, PORT)

status_code, respose = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {respose}")

status_code, respose = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {respose}")

try:

    status_code, respose = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Starting TLS connection: {status_code} {respose}")

    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    smtp.quit()

except Exception as e:
    print(e)

