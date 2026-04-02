class MemoryManager:
    """
    Manages long-term and short-term memory for AI agents.
    """
    def __init__(self, storage_type="local"):
        self.storage_type = storage_type
        self.short_term = []
        self.long_term = {}

    def store_short_term(self, item):
        self.short_term.append(item)
        if len(self.short_term) > 100:
            self.short_term.pop(0)

    def store_long_term(self, key, value):
        self.long_term[key] = value

    def retrieve(self, key):
        return self.long_term.get(key, None)
