import subprocess
import time

chip = input("Enter GPIO chip: ")
pin = input("Enter GPIO pin: ")

previous_state = None

print("\n===== LIVE GPIO MONITOR =====")
print("Press Ctrl + C to stop...\n")

while True:
    # read GPIO value
    result = subprocess.getoutput(
        f"sudo gpioget {chip} {pin}"
    )

    current_state = result.strip()

    # detect state change
    if current_state != previous_state:
        print(f"GPIO {pin} changed to: {current_state}")

        if current_state == "1":
            print("EVENT: SIGNAL HIGH DETECTED")

        elif current_state == "0":
            print("EVENT: SIGNAL LOW DETECTED")

        previous_state = current_state

    time.sleep(1)
