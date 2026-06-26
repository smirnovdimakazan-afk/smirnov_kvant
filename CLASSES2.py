class Transport:
    def __init__(self, vmestimost, speed):
        self.vmestimost = vmestimost
        self.speed = speed
    def deistvie(self):
        print("vrooom")

class Avtobus(Transport):
    def __init__(self,vmestimost,speed,ostanovka):
        Transport.__init__(self, vmestimost,speed)
        self.ostanovka = ostanovka
    def deistvie(self):
        print("ostorojno dveri zakrivayatsa....")
class Gruzoviki(Transport):
    def __init__(self,vmestimost,speed,gryz):
        Transport.__init__(self, vmestimost,speed)
        self.gryz = gryz
    def deistvie(self):
        print("vezy kamen")

transport = Transport("randomnaya", "randomnaya")
avtobus = Avtobus(50, 50, "NIZNAY")
gryzi = Gruzoviki(2, 70, "KAMEN")
gryzi.deistvie()
avtobus.deistvie()