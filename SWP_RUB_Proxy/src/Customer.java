public class Customer 
{
    public static void main(String[] args) 
    {
        PrinterProxy printerProxy = new PrinterProxy(new BWPrinter());

        printerProxy.print("Document 1");

        printerProxy.switchTo(new CLPrinter());
        printerProxy.print("Dokument 2");

        printerProxy.switchTo(new BWPrinter());
        printerProxy.print("Dokument 3");

        printerProxy.switchTo(new CLPrinter());
        printerProxy.print("Dokument 4");
        
        printerProxy.print("");
    }
}