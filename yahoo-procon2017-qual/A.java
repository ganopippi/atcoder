import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Your code here!
        Scanner sc = new Scanner(System.in);
		String str=sc.next();//yahoo
		String ans = "yahoo";
		List<String> strArray = new ArrayList<String>();
		List<String> ansArray = new ArrayList<String>();
		
		for (int i = 0; i < str.length(); i++) {
       // 配列に順番に格納する
            strArray.add(String.valueOf(str.charAt(i)));
        }
        for (int j = 0; j < ans.length(); j++) {
       // 配列に順番に格納する
            ansArray.add(String.valueOf(ans.charAt(j)));
        }
        
        
		if (str.length() != 5){
		    System.out.println("NO");
		} else {
		    for(int k=0;k<5;k++) {
		        
		        for(int l = 0;l<ansArray.size();l++) {

		            
		            if(strArray.get(k).equals(ansArray.get(l))){
		                ansArray.remove(l);
		            }
		        
		        
		        //System.out.println(strArray.size());   
		        }
		    
		    } // for k の終わり
		    if(ansArray.size()>0){
		        System.out.println("NO");
		    } else {
		        System.out.println("YES");
		    }
		    
            } // end else
        
    }}
    
		
        
