import time
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Jarvis',
        timeout=10
    )

def schedule_task(task, time_schedule):
    while True:
        current_time = time.strftime('%H:%M')
        if current_time == time_schedule:
            send_notification('Jarvis', task)
            break
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    # Example schedule: Wake up notification at 8:00 AM
    schedule_task('Wake up, Sir! This is Jarvis speaking.', '12:52')

    # Example schedule: Cooking reminder at 8:00 PM
    schedule_task('Sir, it\'s cooking time. Head to the kitchen!', '20:00')

    # Add more schedules for other tasks as needed
