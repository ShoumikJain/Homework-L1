import time


print("Hello! I am Jarvis an AI BOT , What is your name?:")
name = input()
print("Nice to meet you", name)
print("How are you feeling today?: (good/bad/ok)")
mood = input().lower()
if mood == "good":
    print("I am glad to hear that!")
elif  mood == "bad": 
    print("I am sorry to hear that, hope things get better for you soon.")
elif mood == "ok": 
    print("I see, hope that it becomes good later on in your life.")

time.sleep(1)

print(f"It was nice chatting with you {name}! Goodbye.")