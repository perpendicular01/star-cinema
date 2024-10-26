class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []   #list
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)


    def entry_show(self, id, movie_name, time):
        info =  {"id": id, "movie_name": movie_name, "time": time}
        self.__show_list.append(info)
        seat_allocation = [['0' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seat_allocation

    def book_seats(self, show_id, row, col):
        flag = False
        for show in self.__show_list:
            if show['id'] == show_id:
                flag = True
                

        if flag:
            if 0<=row<self.__rows  and  0<=col< self.__cols:
                if self.__seats[show_id][row][col] == '0':
                    self.__seats[show_id][row][col] = '1'
                    print(f'Your seat ({row}, {col}) booked for Show ID {show_id}.')
                else:
                    print(f'Seat at Row {row}, Col {col} is already booked for Show ID {show_id}.')
            else:
                print('Invalid row or column.')
        else:
            print('Invalid Show ID')

        

    def view_show_list(self):
        print("\nList of Shows:")
        for show in self.__show_list:
            print(f"Movie Name: {show['movie_name']},    Show ID: {show['id']},   Time: {show['time']}")



    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            seat_allocation = self.__seats[show_id]
            print(f"Available Seats for Show ID {show_id}:")
            available_seats = []
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if seat_allocation[row][col] == '0':
                        available_seats.append((row, col))
            if not available_seats:
                print("No available seats.")
            else:
                for row, col in available_seats:
                    print(f"Seat ({row}, {col})")
                
                # matrix akare deikhaite
                for row in range(self.__rows):
                    mat = ""
                    for col in range(self.__cols):
                        if seat_allocation[row][col] == '0':
                            mat += "0"
                        else:
                            mat += "1"
                    print(" ".join(mat))
                print('\n')
        else:
            print(f'Show ID {show_id} not found.')



cinema = Star_Cinema()
hall1 = Hall(5, 5, 5)
hall1.entry_show(1, 'Harry Potter', '25-10-24   11:00 AM')
hall1.entry_show(3, 'Into the wild', '25-10-24   03:00 PM')
hall1.entry_show(4, 'Charlie', '25-10-24   06:00 PM')


while True:
    print('\n\n1. View  all shows today')
    print('2. View available seats for a show')
    print('3. Book  a seat')
    print('4. Exit')
    
    ch = int(input('Enter your choice: '))

    
    if ch == 1:
        hall1.view_show_list()
    
    elif ch == 2:
        show_id = int(input('\tEnter the Show ID: '))
        hall1.view_available_seats(show_id)
    
    elif ch == 3:
        show_id = int(input("\tShow ID: "))

        row = int(input("\tEnter the row number: "))

        col = int(input("\t1Enter the column number: "))

        hall1.book_seats(show_id, row, col)
    
    elif ch == 4:
        print('Exiting..tata')
        break
    
    else:
        print("Invalid Option!")
