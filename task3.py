class Buiding:
    def __init__(self, gift=None):
        self.numberOfFloors = 10
        self.buildingType = 'Десятиэтажка'

    def __eg__(self, other):
        return self.numberOfFloors == other.buildingType


numberOfFloors = Buiding(gift=10)
buildingType = Buiding(gift='Десятиэтажка')
if numberOfFloors == buildingType:
    print('Атрибуты равны')
else:
    print('Атрбуты не равны')
if Buiding.__eq__(self=numberOfFloors, other=buildingType):
    #print('Атрибуты равны!')
#else:
    #print('Атрибуты не равны!')