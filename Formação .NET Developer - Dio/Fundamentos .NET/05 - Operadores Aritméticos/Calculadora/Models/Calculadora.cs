using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Calculadora.Models
{
    public class Calculadora
    {
        public void Somar(int x, int y)
        {
            Console.WriteLine($"{x}+{y}={x+y}");
        }
        public void Subtrair(int x, int y)
        {
            Console.WriteLine($"{x}-{y}={x-y}");
        }
        public void Multiplicar(int x, int y)
        {
            Console.WriteLine($"{x}*{y}={x*y}");
        }
        public void Dividor(int x, int y)
        {
            Console.WriteLine($"{x}/{y}={x/y}");
        }
    }
}