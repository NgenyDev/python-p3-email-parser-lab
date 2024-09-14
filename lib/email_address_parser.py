
import re

class EmailAddressParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        """Extracts email addresses from the provided text."""
        email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        return sorted(email_regex.findall(self.text))
