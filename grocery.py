def main():
    grocery_list = {}
    
    try:
        while True:
            item = input().strip().capitalize()
            
            if not item:
                break
            
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass
    
    for item, quantity in sorted(grocery_list.items()):
        print(f"{quantity} {item.upper()}")

if __name__ == "__main__":
    main()
