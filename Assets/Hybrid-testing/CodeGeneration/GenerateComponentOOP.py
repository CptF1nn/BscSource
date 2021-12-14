c_template1 = """using UnityEngine;
public class MoveComponentOOP{} : MonoBehaviour
"""

c_template2 = """{
    void Update()
    {
        transform.position = transform.position + new Vector3(0.01f,0f);
    }
}"""

def generateComponentsOOP(n):
    for i in range(n):
        f = open("MoveComponentOOP{}.cs".format(i), "w")
        
        s = c_template1.format(i) + c_template2

        f.write(s)
        
        f.close()