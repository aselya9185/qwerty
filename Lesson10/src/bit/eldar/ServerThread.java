package bit.eldar;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.ArrayList;

public class ServerThread  extends Thread{
    private ArrayList<String> names = new ArrayList<String>();
    private Socket socket;
    private  int number;

    public ServerThread(Socket socket,int number) {
        this.socket = socket;
        this.number = number;
        names.add("John");
        names.add("David");
        names.add("Will");
        names.add("Drake");
    }

    public void run(){
        try{
            ObjectInputStream inStream =
                    new ObjectInputStream(socket.getInputStream());
            ObjectOutputStream outStream = new ObjectOutputStream(socket.getOutputStream());
            PackageData pd = null;
            while((pd = (PackageData) inStream.readObject())!=null){
                System.out.println(pd);
                if(pd.getMessage().toLowerCase().equals("hello")){
                    PackageData response = new PackageData();
                    response.setMessage("HI From server!");
                    outStream.writeObject(response);
                }else if(pd.getMessage().toLowerCase().contains("how")&&pd.getMessage().toLowerCase().contains("are")&&pd.getMessage().toLowerCase().contains("you")){
                    PackageData response = new PackageData();
                    response.setMessage("I am fine! You?");
                    outStream.writeObject(response);
                }else if(pd.getMessage().toLowerCase().equals("list")){
                    PackageData response = new PackageData();
                    response.setNames(names);
                    response.setMessage("list");
                    outStream.writeObject(response);
                }else{
                    outStream.writeObject(null);
                }
            }
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
