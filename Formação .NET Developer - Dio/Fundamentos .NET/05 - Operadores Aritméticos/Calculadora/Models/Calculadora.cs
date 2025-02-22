using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Calculadora.Models
{
    public class Calculator
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
        public void Dividir(int x, int y)
        {
            Console.WriteLine($"{x}/{y}={x/y}");
        }
        public void Potencia(int x, int y)
        {
            double pot = Math.Pow(x, y);
            Console.WriteLine($"{x}^{y}={pot}");
        }
        public void Seno(double angulo)
        {
            double radiano = angulo * Math.PI / 180;
            double seno = Math.Sin(radiano);
            Console.WriteLine($"Seno de {angulo}º = {seno}");
        }
        }
        public void Coseno(double angulo)
        {
            double radiano = angulo * Math.PI / 180;
            double coseno = Math.Cos(radiano);
            Console.WriteLine($"Coseno de {angulo}º = {seno}");
        }
        public void Tangente(double angulo)
        {
            double radiano = angulo * Math.PI / 180;
            double tangente = Math.Tan(radiano);
            Console.WriteLine($"Tangente de {angulo}º = {seno}");
        }
    }

    

}