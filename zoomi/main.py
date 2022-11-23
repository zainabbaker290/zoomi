from  components.base_dock import BaseDock
from  components.battery import Battery
from  components.cleaningprofile import CleaningProfile
from  components.dirt_compartment import DirtCompartment
from  components.light import Light
from  roomsimulation.room import Room
from  components.sensors import Sensors
from  components.wheels import Wheels
from  graphicalzoomi import GraphicalZoomi
from  roomsimulation.obstacle import obstacle

       
def main():
    room_one = Room(100,100,[obstacle(5,6,30,20),obstacle(25,60,30,20),obstacle(70,40,30,20)],[obstacle(80,0,15,20)])
    wheels = Wheels()
    sensors = Sensors(wheels)
    battery = Battery()
    cleaning_mode = CleaningProfile("default","fast", 1, sensors)
    dirt_compartment = DirtCompartment()
    light = Light()
    base_dock = BaseDock()
    print(cleaning_mode)
    zoomi = GraphicalZoomi(battery,sensors,light,dirt_compartment,cleaning_mode, wheels,room_one, base_dock)
    print(zoomi.activate_zoomi())
    

if __name__ == "__main__":
    main()
