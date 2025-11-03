from pyfiglet import Figlet

f = Figlet(font='slant')

print(f.renderText('CoinCan.'))

# Prices per item
PRICE_CAN = 0.10
PRICE_BOTTLE = 0.10


def main():
    # Totals
    total_cans = 0
    total_bottles = 0

    print("Welcome! Let's calculate your refund.")
    print("You can enter any number for pack size, or type 'done' to finish.")

    while True:
        item_type = input("Enter item type (can/bottle or 'done' to finish): ").lower()

        if item_type == "done":
            break
        elif item_type not in ["can", "bottle"]:
            print("Invalid type. Please enter 'can', 'bottle', or 'done'.\n")
            continue

        pack_type = input("Enter pack size (any positive number): ").strip()

        if pack_type.isdigit() and int(pack_type) > 0:
            quantity = int(pack_type)
        else:
            print("Invalid pack size. Please enter a positive number.\n")
            continue

        if item_type == "can":
            total_cans += quantity
        else:
            total_bottles += quantity

        print(f"Added {quantity} {item_type}(s). Current total: {total_cans} cans, {total_bottles} bottles.\n")

    # Calculate totals
    total_items = total_cans + total_bottles
    total_refund = (total_cans * PRICE_CAN) + (total_bottles * PRICE_BOTTLE)

    # Prepare summary text
    summary = f"""
============= Refund Summary =============
=============                =============
=============                =============
=============                =============

Cans: {total_cans} x ${PRICE_CAN:.2f} = ${total_cans * PRICE_CAN:.2f}
Bottles: {total_bottles} x ${PRICE_BOTTLE:.2f} = ${total_bottles * PRICE_BOTTLE:.2f}
Total items: {total_items}
Total refund: ${total_refund:.2f} CAD

=============                =============
=============                =============
=============                =============
=============                =============
=============                =============
"""

    print() # Just Space

    # Display summary
    print(summary)

    # Save to file
    with open("refund_summary.txt", "w") as file:
        file.write(summary.strip())

    print("Summary saved to 'refund_summary.txt'")

# ...existing code...

while True:
    main()
    choice = input("\nPress ENTER to restart or q to quit: ")
    if choice.lower() == "q" or choice == "Q":
        print("Goodbye!")
        break
    elif choice == "":
        print("\nRestarting...\n")
    else:
        print("Invalid option. Restarting...\n")
# ...existing code...
