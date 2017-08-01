import java.util.Scanner;

public class JavaProgram
{
    public static void main(String args[])
    {
        int decimalnumber, remainder;
        String hexadecimalnumber="";
        
        char hexa[]={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
        
        Scanner scan = new Scanner(System.in);
		
        System.out.print("Decimal Number : ");
        decimalnumber = scan.nextInt();
		
        while(decimalnumber>0)
        {
            remainder = decimalnumber%16;
            hexadecimalnumber = hex[remainder] + hexadecimalnumber;
            decimalnumber = decimalnumber/16;
        }
		
        System.out.print("Equivalent Hexadecimal Value of " + decimalnumber + " is :\n");
        System.out.print(hexadecimalnumber);
    }
}
