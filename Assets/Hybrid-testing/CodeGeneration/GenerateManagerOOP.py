moop_template1 = """using System;
using UnityEngine;
using System.Collections;
using System.IO;

public class MoveManagerOOPHybrid : MonoBehaviour
{
    private int N = 100000;

    private int _seconds = 60;

    private float _frames = 0;

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

"""

moop_template2 = """for (int i = 0; i < N; i++)
        {
            GameObject go = new GameObject(i.ToString());
            """

moop_template3 = """go.AddComponent<MoveComponentOOP{}>();
"""

moop_template4 = """        }
        """

moop_template5 = """float after = Time.realtimeSinceStartup;
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

def generateManagerOOP(n):
    f = open("MoveManagerOOPHybrid.cs","w")

    s = moop_template1
    for i in range(n):
        s += moop_template2 + moop_template3.format(i) + moop_template4
    s += moop_template5

    f.write(s)
    
    f.close()