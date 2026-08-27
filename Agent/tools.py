import os
import re

import requests
from dotenv import load_dotenv
from langchain_core.tools import tool

from RAG.rag import rag


load_dotenv()

NTFY_TOPIC = os.getenv("NTFY_TOPIC")


def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


@tool
def search_personal_knowledge(question: str) -> str:
    """
    Search Mohammad's personal knowledge base.

    Use this tool when the user asks about Mohammad's
    education, skills, projects, interests, experience,
    background, or other personal information.
    """
    return rag(question)


@tool
def send_contact_message(
    name: str,
    email: str,
    message: str,
) -> str:
    """
    Send a contact message to Mohammad.

    Use this tool only when the user explicitly wants
    to contact Mohammad.

    The user's name, email, and message are required.
    Do not call this tool if the name or email is missing.
    """

    if not name.strip():
        return "The user's name is required."

    if not is_valid_email(email):
        return "The email address is invalid."

    if not message.strip():
        return "The message cannot be empty."

    if not NTFY_TOPIC:
        return "Notification service is not configured."

    notification_message = (
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Message:\n{message}"
    )

    url = f"https://ntfy.sh/{NTFY_TOPIC}"

    response = requests.post(
        url,
        data=notification_message.encode("utf-8"),
        headers={
            "Title": "New Contact Request",
            "Priority": "high",
            "Tags": "speech_balloon",
        },
        timeout=10,
    )

    if response.status_code == 200:
        return "The message was successfully sent."

    return "Failed to send the message."