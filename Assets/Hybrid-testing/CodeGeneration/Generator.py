from GenerateIComponentData import generateComponentData
from GenerateEntitySystem import generateSystemBase
from GenerateManagerDOD import generateManagerDOD
from GenerateComponentOOP import generateComponentsOOP
from GenerateManagerOOP import generateManagerOOP

def GenerateAll():
    generateComponentData(n)
    generateSystemBase(n)
    generateManagerDOD(n)
    generateComponentsOOP(n)
    generateManagerOOP(n)

n = int(input())

GenerateAll()
