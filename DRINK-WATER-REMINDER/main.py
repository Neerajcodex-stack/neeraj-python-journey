from pync import Notifier
import time
import os

while True:
    Notifier.notify("Please drink some water!", title="💧 Hydration Reminder")
    os.system('afplay /System/Library/Sounds/wind.aiff')  # ✅ Plays sound
    time.sleep(10)