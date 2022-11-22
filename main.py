from base_dock import BaseDock
from battery import Battery
from cleaning_mode import CleaningMode
from dirt_compartment import DirtCompartment
from light import Light
from room import Room
from sensors import Sensors
from wheels import Wheels
from zoomi import Zoomi

def main():
    room_one = Room(100,100,{0:2,0:5},{18:9})
    wheels = Wheels()
    sensors = Sensors(wheels)
    battery = Battery()
    cleaning_mode = CleaningMode(sensors)
    dirt_compartment = DirtCompartment()
    light = Light()
    base_dock = BaseDock(battery)
    print(cleaning_mode)

    zoomi = Zoomi(battery,sensors,light,dirt_compartment,cleaning_mode, wheels,room_one, base_dock)


    print(zoomi.set_zoomi_state("activated"))
    print(zoomi.activate_zoomi())

if __name__ == "__main__":
    main()
