from base_dock import BaseDock
from battery import Battery
from cleaningprofile import CleaningProfile
from dirt_compartment import DirtCompartment
from light import Light
from room import Room
from sensors import Sensors
from wheels import Wheels
from zoomi import Zoomi
from graphicalzoomi import GraphicalZoomi
from obstacle import obstacle

       
def main():
    room_one = Room(100,100,[obstacle(5,6,30,20),obstacle(25,60,30,20),obstacle(70,40,30,20)],[obstacle(80,0,15,20)])
    wheels = Wheels()
    sensors = Sensors(wheels)
    battery = Battery()
    cleaning_mode = CleaningProfile(sensors)
    dirt_compartment = DirtCompartment()
    light = Light()
    base_dock = BaseDock()
    print(cleaning_mode)
    zoomi = GraphicalZoomi(battery,sensors,light,dirt_compartment,cleaning_mode, wheels,room_one, base_dock)
    print(zoomi.set_zoomi_state("activated"))
    print(zoomi.activate_zoomi())
    

if __name__ == "__main__":
    main()


#one this is after mid clean charge, idk if it goes back to cleaning 