"""Sending email using smtplib python3"""
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("Your email id", "Password")

msg = "SUCCESS"
server.sendmail("your email id ", "to email id", msg)
server.quit()