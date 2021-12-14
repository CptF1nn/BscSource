cd_template = """using Unity.Entities;
using Unity.Mathematics;

public struct MoveComponentDOD{} : IComponentData
"""

cd_template2 = """{
    public float3 Value;
}"""

def generateComponentData(n):
    for i in range(n):
        f = open("MoveComponentDOD{}.cs".format(i), "w")
        f.write(cd_template.format(i) + cd_template2)

        f.close()
