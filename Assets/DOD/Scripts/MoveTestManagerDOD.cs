using UnityEngine;
using Unity.Entities;
using Unity.Collections;
using Unity.Mathematics;
using System;
using System.Collections;
using System.IO;

public class MoveTestManagerDOD : MonoBehaviour
{
    private int N = 10000;

    private int _seconds = 60;

    private float _frames = 0;

    private EntityManager entityManager;

    private void Awake()
    {
        string[] args = Environment.GetCommandLineArgs();

        for (int i = 0; i < args.Length; i++)
        {
            if (args[i] == "-amount")
            {
                N = int.Parse(args[i + 1]);
                Debug.Log("N = " + N);
            }
            if (args[i] == "-time")
            {
                _seconds = int.Parse(args[i + 1]);
                Debug.Log("Seconds = " + _seconds);
            }
        }

        float before = Time.realtimeSinceStartup;

        entityManager = World.DefaultGameObjectInjectionWorld.EntityManager;

        EntityArchetype archetype = entityManager.CreateArchetype(typeof(MoveDOD));

        NativeArray<Entity> entities = new NativeArray<Entity>(N, Allocator.Temp);
        entityManager.CreateEntity(archetype, entities);

        for (int i = 0; i < N; i++)
        {
            Entity entity = entities[i];

            entityManager.SetComponentData(entity, new MoveDOD { Value = new float3(0f, 0f, 0f) });
        }
        float after = Time.realtimeSinceStartup;
        Debug.Log("Entity creation in seconds: " + (after - before));
        Debug.Log("Total startup time: " + Time.realtimeSinceStartup);

        StartCoroutine(Shutdown());
    }

    private void Update()
    {
        _frames++;
    }

    private IEnumerator Shutdown()
    {
        yield return new WaitForSeconds(_seconds);

        File.WriteAllText((N / 1000) + "k - T" + _seconds.ToString() + ".txt", (_frames/_seconds).ToString());

        Application.Quit();
    }
}
