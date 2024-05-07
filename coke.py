# Define the cost of one bottle of Coke
cost_of_coke = 50
# Initialize the amount due
amount_due = cost_of_coke

# Loop until the amount due is less than or equal to 0
while amount_due > 0:
    # Prompt the user to insert a coin
    coin = int(input("Insert Coin: "))
    # Check if the inserted coin is an accepted denomination
    if coin in [5, 10, 25]:
        # Subtract the value of the coin from the amount due
        amount_due -= coin
        # Inform the user of the amount due
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        elif amount_due == 0:
            print(f"Change Owed: {amount_due}")
        elif amount_due < 0:
            print(f"Change Owed: {abs(amount_due)}")
    else:
        print(f"Amount Due: {amount_due}")