namespace kalkulator
{
    class Project
    {
        static void Main(string[] args)
        {
            System.Console.Write("Upišite prvi broj: ");
            Global.x = Convert.ToDouble(Console.ReadLine());

            System.Console.Write("Upiši drugi broj: ");
            Global.y = Convert.ToDouble(Console.ReadLine());

            System.Console.Write("Koju radnju želiš(+, -, *, /)? ");
            var rad = Console.ReadLine();


            if (rad == "*") { System.Console.WriteLine(Global.x + Global.y); }
            if (rad == "/")
            {
                if (Global.x != 0)
                {
                    if (Global.y != 0)
                    {
                        System.Console.WriteLine(Global.x / Global.y);
                    }
                }
                else
                {
                    System.Console.WriteLine("You can't divade with zero!");
                }
            }
            if (rad == "+") { System.Console.WriteLine(Global.x + Global.y); }
            if (rad == "-") { System.Console.WriteLine(Global.x - Global.y); }

            Console.Beep();
        }
        static void Množi()
        {
            System.Console.WriteLine(Global.x + Global.y);
        }
        static void Dijeli()
        {
            if (Global.x != 0)
            {
                if (Global.y != 0)
                {
                    System.Console.WriteLine(Global.x / Global.y);
                }
            }
            else
            {
                System.Console.WriteLine("You can't divade with zero!");
            }
        }
        static void Zbroji()
        {
            System.Console.WriteLine(Global.x + Global.y);
        }
        static void Oduzmi()
        {
            System.Console.WriteLine(Global.x - Global.y);
        }
    }
    class Global
    {
        public static double x;
        public static double y;
    }
}