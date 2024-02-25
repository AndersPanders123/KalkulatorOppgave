using system;

class kalkulator
{
    static void Main(
        Console.WriteLine("Anders super kule kalkulator");

        //første input
        double n1 = GetUserInput("Skriv det første nummeret her");

        //Ander input
        double n2 = GetUserInput("Skrive det andere nummeret her");

        //Her matter matten
        Console.WriteLine($"Pluss: {n1 + n2}");
        Console.WriteLine($"Minus: {n1 - n2}");
        Console.WriteLine($"Ganging: {n1 * n2}");

        //her matter delingen
        if (n2 != 0) 
        {
            Console.WriteLine($"Deling: {n1 / n2}");
        }
        else
        {
            Console.WriteLine("Kanke dele på 0 din melkekartong")
        }
    )

    static double GetUserInput(string promt)
    {
        while (true)
        {
            Console.WriteLine(promt);
            string input = Console.ReadLine();

            if (double.TryParse(input, out double num))
            {
                return num
            }
            else
            {
                Console.WriteLine("Skriv ett nummer a, din tullebokk")
            }
        }
    }
}