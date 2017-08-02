import java.util.Scanner;

public class JavaProgram
{
    public static int HexadecimalToDecimal(String s)
    {
             String digits = "0123456789ABCDEF";
             s = s.toUpperCase();
             int val = 0;
             for (int i = 0; i < s.length(); i++)
             {
                 char c = s.charAt(i);
                 int d = digits.indexOf(c);
                 val = 16*val + d;
             }
             return val;
    }
    public static void main(String args[])
    {
        String HexadecimalNumber;
        int DecimalNumber, i=1, j;
        int OctalNumber[] = new int[100];
        Scanner scan = new Scanner(System.in);
		
        System.out.print("Hexadecimal Number = ");
        HexadecimalNumber = scan.nextLine();
        
        DecimalNumber = HexadecimalToDecimal(HexadecimalNumber);
        
        while(DecimalNumber != 0)
        {
            OctalNumber[i++] = DecimalNumber%8;
            DecimalNumber = DecimalNumber/8;
        }
		
        System.out.print("Octal Number = \n");
        for(j=i-1; j>0; j--)
        {
            System.out.print(OctalNumber[j]);
        }
    }
}
