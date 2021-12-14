using UnityEngine;

public class MoveTestOOP : MonoBehaviour
{
    void Update()
    {
        transform.position = transform.position + new Vector3(0.01f,0f);
    }
}
