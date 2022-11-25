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
    room_one = Room(50,50,[obstacle(20,20,5,5),obstacle(10,20,5,5),obstacle(20,30,5,5),obstacle(30,40,5,5),obstacle(40,10,5,5),obstacle(10,40,5,5)],[])
    wheels = Wheels()
    sensors = Sensors(wheels)
    battery = Battery()
    cleaning_mode = CleaningProfile("default","fast", 2, sensors)
    dirt_compartment = DirtCompartment()
    light = Light()
    base_dock = BaseDock()
    print(cleaning_mode)
    zoomi = GraphicalZoomi(battery,sensors,light,dirt_compartment,cleaning_mode, wheels,room_one, base_dock)
    print(zoomi.activate_zoomi())
    

if __name__ == "__main__":
    main()
