class HashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        """Simple hash function based on built-in hash and modulo."""
        return hash(key) % self.capacity

    def put(self, key, value):
        """Insert or update a key-value pair."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        bucket.append((key, value))  # Add new

    def get(self, key):
        """Retrieve value for a given key."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def remove(self, key):
        """Remove key-value pair if it exists."""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def contains(self, key):
        """Check if key exists in map."""
        index = self._hash(key)
        return any(k == key for k, _ in self.buckets[index])

    def keys(self):
        """Return all keys."""
        return [k for bucket in self.buckets for (k, _) in bucket]

    def values(self):
        """Return all values."""
        return [v for bucket in self.buckets for (_, v) in bucket]
