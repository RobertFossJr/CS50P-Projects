greeting = input("What is your greeting? ").strip().lower()
    
if "hello" in greeting:
    print("$0")
elif greeting.startswith("h") and greeting != "hello":
    print("$20")
else:
    print("$100")