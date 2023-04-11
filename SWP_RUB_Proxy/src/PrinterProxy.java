public class PrinterProxy implements Printer 
{
    private Printer cPrinter;

    public PrinterProxy(Printer printer) 
    {
        this.cPrinter = printer;
    }

    public void switchTo(Printer printer) 
    {
        this.cPrinter = printer;
    }

    @Override
    public void print(String document) 
    {
        if (document == null) 
        {
            System.out.println("No Document");
        } 
        else 
        {
            cPrinter.print(document);
        }
    }
}