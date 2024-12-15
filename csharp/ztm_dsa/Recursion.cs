using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ztm_dsa;

public class Recursion
{
    public Recursion()
    {
        Console.WriteLine("factorial of 5 is: " + fact(5));
        Console.WriteLine("fibonachi number 5 is: " + fib(6));

        for(int i = 0; i<10; i++)
        {
            Console.WriteLine($"number {i}-th fibonacci is: "+ fib(i));
        }
    }

    int fact(int n) 
    {
        if (n <= 1) return 1;

        return n * fact(n-1); 
    }

    int fib(int n)
    {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
    }

    int fibprint(int n)
    {
        if (n <= 1)
            Console.WriteLine(n);
            return n;
        
        return fib(n-1) + fib(n - 2);

        
    }



}
