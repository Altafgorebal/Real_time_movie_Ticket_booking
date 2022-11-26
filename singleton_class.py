def outer(arg):
    d = {}
    def inner():
        if arg not in d:
            d[arg] = arg()
        return d[arg]
    return inner

@outer
class innovative_multiplex():
    def __init__(self):
        self.Movie = 'pathan'
        self.Mtickets = 150

    def booking(self,n):
        if self.Mtickets>=n:
            self.Mtickets-=n
            print(n , "Tickets for ", self.Movie ,"successfully Booked")
        else:
            if self.Mtickets == 0:
                print("No tickets available")
            else:
                print("only ",self.Mtickets ," tickets are avaliable")

def book():
    n = int(input("Enter number of Tickets to Book"))
    ob = innovative_multiplex()
    ob.booking(n)
book()
book()
book()
            
