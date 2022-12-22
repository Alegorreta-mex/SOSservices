INFORMATION_EMAIL = 1
REQUEST_MAIL = 2
TYPES_EMAIL_KEYS = {
    INFORMATION_EMAIL: ("ID","NAME","STATUS", "MESSAGE"),
    REQUEST_MAIL: ("ID","NAME", "NAME_WORKER", "DAYS_TAKEOFF", "TYPE_TAKEOFF", "REASON")
}


def send_email_aws(type_email, to, payload):
    """
    Function tha send email via SMS
    """
    if check_payload(type_email, payload):
        print(f"Email send to {to}")
        return True
    else:
        return False


def check_payload(type_email, payload):
    """
    function that it checks the correct payload of a message
    """
    return True
