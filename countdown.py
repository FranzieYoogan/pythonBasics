import time


myTime = int(input("Enter seconds: "))

for z in range(myTime, 0 , -1):
    print(f"{(z // 3600):02d}:{(z // 60):02d}:{(z % 60):02d}")
    time.sleep(1)

print("Time's up!")