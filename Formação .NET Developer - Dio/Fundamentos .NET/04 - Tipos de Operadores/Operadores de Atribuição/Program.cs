// Operador de atribuição
int a = 4;
int b = 5;

int c = a + b;

Console.WriteLine(c);

c += 5;
Console.WriteLine(c);
c -= 5;
Console.WriteLine(c);
c *= 5;
Console.WriteLine(c);
c /= 5;
Console.WriteLine(c);

Console.WriteLine("-------------------------");

int d = 5;
Console.WriteLine(d);
/*Cast - casting*/
int e = Convert.ToInt32("9");
Console.WriteLine(e);

int f = int.Parse("7");
Console.WriteLine(f);

Console.WriteLine("-------------------------");
int g = Convert.ToInt32(null);
Console.WriteLine(g);
// int h = int.Parse(null);
// Console.WriteLine(h);

Console.WriteLine("-------------------------");

int i = 5;
string j = i.ToString();
Console.WriteLine(i);

Console.WriteLine("-------------------------");
// Cast Implícito
int k = 8;
double l = k;

Console.WriteLine(l);

long m = k;
Console.WriteLine(m);

int n = Convert.ToInt32(m);
Console.WriteLine(n);

long o = long.MaxValue;
Console.WriteLine(o);

int p = int.MaxValue;
long q = p;
Console.WriteLine(q);

Console.WriteLine("-------------------------");

double r = 4/2+2;
Console.WriteLine(r);
double s = 4/(2+2);
Console.WriteLine(s);

Console.WriteLine("-------------------------");
string t = "15";
int u = Convert.ToInt32(t);
Console.WriteLine(u);

string v = "85";
int w = 0;
int.TryParse(v, out w);

Console.WriteLine(w);

