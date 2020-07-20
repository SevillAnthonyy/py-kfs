from datetime import datetime

old_print = print

def timestamped_print(*args, **kwargs):
  old_print(datetime.now(), *args, **kwargs)

print = timestamped_print

def log(mssg):
    print(mssg)
