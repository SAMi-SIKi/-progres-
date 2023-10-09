namespace projekt1
{
    class Project
    {
        static void Main(string[] args)
        {
            System.Console.Write("I like... ");
            var y = Console.ReadLine();

            Sleep(2);

            if (y == "men")
            {
                System.Console.WriteLine("...yes...men");
            }
            else
            {
                System.Console.WriteLine("...no...MEN");
            }

            Console.Beep();
        }
        static void Sleep(int seconds)
        {
            Thread.Sleep(seconds * 1000);
        }
    }
}