/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package learnjava;

/**
 *
 * @author lenovo-pc
 */
public class LearnJava {

    /**
     * @param args the command line arguments
     */
       
    public static String reverseString(String name){
         int size = name.length();
         String reverseName = "";
            while(size > 0){
                reverseName  = reverseName + name.charAt(size -1);              
                size--;
            }
        return reverseName;
          
    }
    
    public static String reverseString(String name, String extra){
         int size = name.length();
         String reverseName = "";
                
            while(size > 0){
                reverseName  = reverseName + name.charAt(size -1);              
                size--;
            }
        return reverseName + " " + extra ;   
          
    }
    
    public static void main(String args[]){
            //TODO code application logic here
            
            //TODO code application logic here
            String mary = "Mary";
            String tom = "tom";
            String larry = "larry";
           
            System.out.println(reverseString(mary));
            System.out.println(reverseString(tom));
            System.out.println(reverseString(larry, " hi larry"));
        
        
    }  
         
          
}
             
            
      
    

            
    
         
   
            
            

    
        
    

