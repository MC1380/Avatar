from .tools import send_contact_message


if __name__ == "__main__":

    result = send_contact_message(
        "سلام محمد! این یک پیام آزمایشی از Avatar است."
    )

    print(result)