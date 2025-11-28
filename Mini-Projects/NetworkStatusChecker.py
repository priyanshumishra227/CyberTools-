'''A network status checker is a simple program that pretends to check whether a network is up or not '''

device = input("Enter the device name (router /switch / server): ")

status = input("Enter the status (up / down / slow): ")

if status == "up":
    print(f"{device} is up ")

elif status == "down":
    print(f"{device} is down ")

elif status == "slow":
    print(f"{device} is slow ")

else :
    print("Invalid status entered ")