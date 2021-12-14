using System;
using System.Collections;
using System.IO;
using UnityEngine;

public class MoveTestManagerOOP : MonoBehaviour
{
    private int N = 100000;

    private int _seconds;

    private float _frames;

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

        for (int i = 0; i < N; i++)
        {
            GameObject go = new GameObject(i.ToString());
            go.AddComponent<MoveTestOOP>();
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
