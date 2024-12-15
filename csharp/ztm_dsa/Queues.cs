using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ztm_dsa;

internal class Queues
{
    public Queues()
    {
        Console.WriteLine("QUEUE IN C#");

        Queue<string> strings = new Queue<string>();
        strings.Enqueue("fhfh");
        strings.Enqueue("hgege");
        strings.Enqueue("heh");

        string hh = strings.Dequeue();
        string he = strings.Dequeue();


    }

}
