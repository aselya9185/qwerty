import java.net.*;
import java.io.*;
import java.util.*;

public class ServerThread extends Thread{

    private Socket socket;

    public ServerThread(Socket socket){
        this.socket=socket;
    }

    public void run(){

        try {
            ObjectInputStream inputStream=new ObjectInputStream(socket.getInputStream());
            ObjectOutputStream outputStream = new ObjectOutputStream(socket.getOutputStream());


            while (true){
                PackageData pd=null;
                PackageData res=null;
                try {
                    if (!((pd=(PackageData)inputStream.readObject())!=null)) break;
                } catch (ClassNotFoundException e) {
                    e.printStackTrace();
                }

                if(pd.getOperationType().equals("ADD")){
                    Server.addStudentToDb(pd.getStudent());
                }else if (pd.getOperationType().equals("LIST")){
                    res.setStudentList(Server.getAllStudets());
                }
                outputStream.writeObject(res);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
