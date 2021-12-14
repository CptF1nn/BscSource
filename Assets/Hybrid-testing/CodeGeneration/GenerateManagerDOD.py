m_template1 = """using UnityEngine;
using Unity.Entities;
using Unity.Collections;
using Unity.Mathematics;
using System;
using System.Collections;
using System.IO;

public class MoveManagerDODHybrid : MonoBehaviour
{
    private int N = 10000;

    private int _seconds = 60;

    private float _frames = 0;

    private EntityManager entityManager;
    NativeArray<Entity> entities;
    EntityArchetype archetype;

    private void Awake()
    {
        string[] args = Environment.GetCommandLineArgs();

        for (int i = 0; i < args.Length; i++)
        {
            if (args[i] == "-amount")
            {
                N = int.Parse(args[i + 1]);
                Debug.Log("N=" + N);
            }
            if (args[i] == "-time")
            {
                _seconds = int.Parse(args[i + 1]);
                Debug.Log("Seconds = " + _seconds);
            }
        }


        float before = Time.realtimeSinceStartup;

        entityManager = World.DefaultGameObjectInjectionWorld.EntityManager;
        """

m_template2 = """archetype = entityManager.CreateArchetype(typeof(MoveComponentDOD{}));
        """
m_template3 = """entities = new NativeArray<Entity>(N, Allocator.Temp);
        entityManager.CreateEntity(archetype, entities);

        for (int i = 0; i < N; i++)
        {
            """

m_template4 = """Entity entity = entities[i];

            entityManager.SetComponentData(entity, new MoveComponentDOD{}"""

m_template5 = """ { Value = new float3(0f, 0f, 0f) });
        }
        """

m_template6 = """float after = Time.realtimeSinceStartup;
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

        File.WriteAllText(N.ToString() + "k - T" + _seconds.ToString() + ".txt", (_frames/_seconds).ToString());

        Application.Quit();
    }
}"""


def generateManagerDOD(n):
    f = open("MoveManagerDODHybrid.cs", "w")
    
    s = m_template1
    for i in range(n):
        s += m_template2.format(i) + m_template3 + m_template4.format(i) + m_template5
    s += m_template6
    
    f.write(s)

    f.close()
    