import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		
	    int res = meth();
	    System.out.println(res);
}
    public static int meth(){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
	    int b = sc.nextInt();
	    return (int) Math.pow(a,b);
    }
