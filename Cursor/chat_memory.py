class ChatMemory:
    def __init__(self, max_length=5):
        self.max_length = max_length
        self.messages = []

    def add_message(self, role, message):
        self.messages.append((role, message))
        if len(self.messages) > self.max_length * 2:  # 2 per turn (user + bot)
            self.messages = self.messages[-self.max_length * 2:]

    def get_context(self):
        return "\n".join([f"{role}: {msg}" for role, msg in self.messages])
