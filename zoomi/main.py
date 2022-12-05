from components.basedock import BaseDock
from components.battery import Battery
from components.cleaningprofile import CleaningProfile
from components.dirtcompartment import DirtCompartment
from roomsimulation.room import Room
from graphicalzoomi import GraphicalZoomi
from roomsimulation.obstacle import obstacle


def main():
    room = Room(50, 50, [obstacle(20, 20, 5, 5), obstacle(10, 20, 5, 5), obstacle(20, 30, 5, 5), obstacle(
        30, 40, 5, 5), obstacle(40, 10, 5, 5), obstacle(10, 40, 5, 5)], [obstacle(40, 25, 5, 5)])
    battery = Battery()
    defaultCleaningProfile = CleaningProfile("default", "fast", 2)
    dirtCompartment = DirtCompartment()
    baseDock = BaseDock()
    zoomi = GraphicalZoomi(battery, dirtCompartment,
                           defaultCleaningProfile, room, baseDock)


if __name__ == "__main__":
    main()
