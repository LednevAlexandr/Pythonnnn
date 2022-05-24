import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
		System.out.println(tre());
		    }
	public static int tre(){
	    Scanner sc = new Scanner(System.in);
	    System.out.print("Введите n: ");
	    int n = sc.nextInt();
	    return n*(n+1)/2;
	}
	
}
