using Unity.Entities;

public class MoveTestSystemDOD : SystemBase
{
    protected override void OnUpdate()
    {
        Entities.WithAll<MoveDOD>().ForEach((ref MoveDOD t) =>
        {
            t.Value.x += 0.01f;
        }).ScheduleParallel();
    }
}