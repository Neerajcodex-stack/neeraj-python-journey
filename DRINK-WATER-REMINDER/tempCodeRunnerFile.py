import os
import time

while True:
    title = "💧 Hydration Reminder"
    message = "Please drink some water!"
    os.system(f'''osascript -e 'display notification "{message}" with title "{title}"' ''')
    time.sleep(3)