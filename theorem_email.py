import os
import smtplib
from email.message import EmailMessage
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


HOME = "https://www.theoremoftheday.org/"

GMAIL_ADDRESS = os.environ["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]


def get_todays_theorem():
    r = requests.get(HOME, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    for link in soup.find_all("a", href=True):
        text = " ".join(link.stripped_strings).lower()

        if "today" in text and "theorem" in text:
            return urljoin(HOME, link["href"])

    for link in soup.find_all("a", href=True):
        if ".pdf" in link["href"].lower():
            return urljoin(HOME, link["href"])

    raise RuntimeError("Could not find today's theorem.")


def send_email(url):
    msg = EmailMessage()

    msg["From"] = GMAIL_ADDRESS
    msg["To"] = GMAIL_ADDRESS
    msg["Subject"] = "Theorem of the Day"

    msg.set_content(
        f"""Today's theorem:

{url}

Theorem of the Day
{HOME}
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        smtp.send_message(msg)


if __name__ == "__main__":
    theorem_url = get_todays_theorem()
    print(f"Found theorem: {theorem_url}")
    send_email(theorem_url)
    print("Email sent.")