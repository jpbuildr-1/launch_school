class Banner:
    def __init__(self, message, width=None):
        self.message = message
        self.width = width

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return f"| {' ' * self._content_width()} |"

    def _horizontal_rule(self):
        return f"+-{'-' * self._content_width()}-+"

    def _message_line(self):
        if self.width is None:
            return f"| {self.message} |"

        return f"| {self.message[:self.width].strip()} |"

    def _content_width(self):
        return len(self.message) if self.width is None else len(self.message[:self.width].strip())


# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

banner = Banner('To boldly go where no one has gone before.', 10)
print(banner)
# +------------+
# |            |
# | To boldly  |
# |            |
# +------------+
