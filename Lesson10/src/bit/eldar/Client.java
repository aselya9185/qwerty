package bit.eldar;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        try{
            System.out.println("Insert your name");
            String name = in.next();
            Socket socket = new Socket("127.0.0.1",1978);

            ObjectOutputStream outStream =
                    new ObjectOutputStream(socket.getOutputStream());
            ObjectInputStream inStream =
                    new ObjectInputStream(socket.getInputStream());

            while(true){
                System.out.println("Insert message");
                String message = in.nextLine();
                PackageData pd = new PackageData(name,message);
                outStream.writeObject(pd);

                if((pd = (PackageData) inStream.readObject())!=null){
                    System.out.println(pd.getMessage());
                    if(pd.getMessage().equals("list")){
                        ArrayList<String> names = pd.getNames();
                        for (String n : names){
                            System.out.println(n);
                        }
                    }
                }
            }

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}