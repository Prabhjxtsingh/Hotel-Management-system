# Hotel Management System

This is a simple hotel management system implemented in Python using the Pandas library. 
The system allows users to view the status of hotel rooms, book rooms, and vacate rooms.

## Features

- Display the status of hotel rooms.
- Book a room for a guest.
- Vacate a room.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/hotel-management-system.git
    ```
2. Change to the project directory:
    ```bash
    cd hotel-management-system
    ```
3. Install the required libraries:
    ```bash
    pip install pandas
    ```

## Usage

Run the script using Python:

```bash
python hotel_management_system.py
```

### Main Menu

1. **Display Room Status**: View the current status of all rooms.
2. **Book a Room**: Book a room for a guest by entering the room number and guest name.
3. **Vacate a Room**: Vacate a room by entering the room number.
4. **Exit**: Exit the application.

## Example

### Display Room Status

```
Hotel Management System
1. Display Room Status
2. Book a Room
3. Vacate a Room
4. Exit

Enter your choice: 1

Hotel Room Status:
   Room Number Occupancy Guest Name
0            1    Vacant            
1            2    Vacant            
2            3    Vacant            
3            4    Vacant            
4            5    Vacant            
5            6    Vacant            
6            7    Vacant            
7            8    Vacant            
8            9    Vacant            
9           10    Vacant
```

### Book a Room

```
Hotel Management System
1. Display Room Status
2. Book a Room
3. Vacate a Room
4. Exit

Enter your choice: 2
Enter the room number you want to book (1-10): 3
Enter guest name: John Doe

Room 3 is booked for John Doe.
```

### Vacate a Room

```
Hotel Management System
1. Display Room Status
2. Book a Room
3. Vacate a Room
4. Exit

Enter your choice: 3
Enter the room number you want to vacate (1-10): 3

Room 3 is now vacant.
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Acknowledgements

- [Pandas](https://pandas.pydata.org/) - For data manipulation and analysis.

Feel free to customize this README file according to your project's specific needs.
```
