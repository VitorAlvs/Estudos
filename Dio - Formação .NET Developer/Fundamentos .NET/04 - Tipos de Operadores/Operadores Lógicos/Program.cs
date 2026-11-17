// Or (Pipe, ||)

bool eMaiordeIdade = false;
bool possuiAltorizacaoResponsavel = false;

if(eMaiordeIdade || possuiAltorizacaoResponsavel)
{
    Console.WriteLine("Entrada Liberada.");
}
else
{
    Console.WriteLine("Entrada não liberada.");
}

Console.WriteLine("--------------------");

// And (&&)
bool presencaMin = true;
double media = 7.5;

if(presencaMin && media >= 7.5){
    Console.WriteLine("Aprovado");
}
else
{
    Console.WriteLine("Reprovado");
}

Console.WriteLine("--------------------");

// Not (!)

bool choveu = false;
bool estaTarde = false;

if(!choveu && !estaTarde)
{
    Console.WriteLine("Vou pedalar hoje!");
}
else
{
    Console.WriteLine("Não vou pedalar hoje.");
}