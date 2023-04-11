public class BWPrinter implements Printer 
{
    @Override
    public void print(String document) 
    {
        System.out.println("Black'n'White: "+document);
    }
}