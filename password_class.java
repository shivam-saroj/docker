package password_generator;
import java.util.Date;
import java.text.SimpleDateFormat;
//import java.util.*;
import java.io.*;
public class password_class {
	
	public static void main(String args[]) throws Exception {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter your First name: ");
		String name=new String(br.readLine());		
		 Date date = new Date();
		 SimpleDateFormat getYearFormat = new SimpleDateFormat("yyyy");
	     String currentYear = getYearFormat.format(date);
	     System.out.println(currentYear);
		String password=name.substring(0,4);
		System.out.println("password => "+password+currentYear);
	}
}
