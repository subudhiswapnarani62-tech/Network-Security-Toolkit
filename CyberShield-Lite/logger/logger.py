from datetime import datetime

# Logger Module
def log_event(msg):
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")
