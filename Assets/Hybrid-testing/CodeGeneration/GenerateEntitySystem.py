sb_template = """using Unity.Entities;
using Unity.Mathematics;

public class MoveSystemDOD{} : SystemBase
"""

sb_template2 = """{
    protected override void OnUpdate()
    {
        """

sb_template3 = """Entities.WithAll<MoveComponentDOD{}>().ForEach((ref MoveComponentDOD{} t) =>
        """

sb_template4 = """{
            t.Value.x += 0.01f;
        }).ScheduleParallel();
    }
}"""

def generateSystemBase(n):
    for i in range(n):
        f = open("MoveSystemDOD{}.cs".format(i), "w")
        f.write(sb_template.format(i) + sb_template2 + sb_template3.format(i,i) + sb_template4)

        f.close()
