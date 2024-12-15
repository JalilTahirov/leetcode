using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ztm_dsa;

public class InsertionSort
{
    public InsertionSort()
    {
        int[] ints = new int[] { 8,7,4,5,6,8 };

        Sort(ints);

        string intss = string.Join(",", ints);  
        Console.WriteLine(intss);
    }

    void Sort(int[] arr)
    {
        for( int i = 1; i < arr.Length; i++)
        {
            int j = i - 1; 
            while (j>=0 && arr[j+1] < arr[j])
            {
                int tmp = arr[j + 1];
                arr[j+1] = arr[j];
                arr[j] = tmp;
                j = j - 1;
            }
        }
    }

    void SortTwo(int[] arr)
    {
        for (int i = 1; i < arr.Length; i++)
        {
            int j = i - 1;
            while (j > 0 && arr[j] < arr[j + 1])
            {
                int tmp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = tmp;
                j = j-1;
            }
        }
    }
}
