import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static MainFrame frame;
    public static Socket socket;
    public static ObjectOutputStream objectOutputStream;
   // public static ObjectInputStream inputStream;

    public static void main(String[] args) {
        connectToServer();

        frame = new MainFrame();
        frame.setVisible(true);

    }

    public static void addStudent(Students student){

        PackageData packageData = new PackageData();
        packageData.setOperationType("ADD");
        packageData.setStudent(student);
        try {
            objectOutputStream.writeObject(packageData);
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public static void connectToServer(){
        try {
            socket = new Socket("127.0.0.1",1979);
            objectOutputStream = new ObjectOutputStream(socket.getOutputStream());
           // inputStream = new ObjectInputStream(socket.getInputStream());


        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
