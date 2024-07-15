import pandas as pd

# Sample hotel room data
rooms_data = {
    'Room Number': list(range(1, 11)),
    'Occupancy': ['Vacant'] * 10,
    'Guest Name': [''] * 10
}

# Create a DataFrame from the sample data
hotel_df = pd.DataFrame(rooms_data)

# Function to display the hotel room status
def display_status():
    print("\nHotel Room Status:")
    print(hotel_df[['Room Number', 'Occupancy', 'Guest Name']])

# Function to book a room
def book_room(room_number, guest_name):
    if hotel_df.loc[hotel_df['Room Number'] == room_number, 'Occupancy'].values[0] == 'Vacant':
        hotel_df.loc[hotel_df['Room Number'] == room_number, 'Occupancy'] = 'Occupied'
        hotel_df.loc[hotel_df['Room Number'] == room_number, 'Guest Name'] = guest_name
        print(f"Room {room_number} is booked for {guest_name}.")
    else:
        print(f"Room {room_number} is already occupied.")

# Function to vacate a room
def vacate_room(room_number):
    if hotel_df.loc[hotel_df['Room Number'] == room_number, 'Occupancy'].values[0] == 'Occupied':
        hotel_df.loc[hotel_df['Room Number'] == room_number, 'Occupancy'] = 'Vacant'
        hotel_df.loc[hotel_df['Room Number'] == room_number, 'Guest Name'] = ''
        print(f"Room {room_number} is now vacant.")
    else:
        print(f"Room {room_number} is already vacant.")

# Main menu
while True:
    print("\nHotel Management System")
    print("1. Display Room Status")
    print("2. Book a Room")
    print("3. Vacate a Room")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_status()
    elif choice == '2':
        room_number = int(input("Enter the room number you want to book (1-10): "))
        guest_name = input("Enter guest name: ")
        if room_number in range(1, 11):
            book_room(room_number, guest_name)
        else:
            print("Invalid room number. Please enter a number between 1 and 10.")
    elif choice == '3':
        room_number = int(input("Enter the room number you want to vacate (1-10): "))
        if room_number in range(1, 11):
            vacate_room(room_number)
        else:
            print("Invalid room number. Please enter a number between 1 and 10.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
