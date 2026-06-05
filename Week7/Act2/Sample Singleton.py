import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()  # Ensures thread safety

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

# Usage
singleton1 = ThreadSafeSingleton()
singleton2 = ThreadSafeSingleton()

# Verifying they are the exact same instance
print(singleton1 is singleton2)  # Output: True