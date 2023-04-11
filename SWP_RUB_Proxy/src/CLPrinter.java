public class CLPrinter implements Printer 
{
   @Override
   public void print(String document) 
   {
       System.out.println("Color: "+document);
   }
}