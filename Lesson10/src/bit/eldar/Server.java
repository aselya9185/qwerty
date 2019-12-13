package bit.eldar;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) {
        int count = 0;
        try{
            ServerSocket server = new ServerSocket(1978);
            while (true){
                Socket socket = server.accept();
                count++;
                System.out.println("Client connected");
                ServerThread st = new ServerThread(socket,count);
                st.start();
            }

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
