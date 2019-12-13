import java.io.ObjectInputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

public class Server {
    public static Connection connection;

    public static void main(String[] args) {

        setConnection();

        try {
            ServerSocket server = new ServerSocket(1979);
            System.out.println("Waiting for client...");

            while (true){
                Socket socket = server.accept();
                System.out.println("Client connected");
                ServerThread st = new ServerThread(socket);
                st.start();
            }
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public static void setConnection() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection =DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/jdbc?useUnicode=true&serverTimezone=UTC","root", ""
            );
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public static void addStudentToDb(Students student){
        try {
            PreparedStatement statement = connection.prepareStatement("" +
                    "INSERT INTO students (id,name,surname,age) " +
                    "VALUES (NULL, ?, ?, ?)"
            );
            statement.setString(1,student.getName());
            statement.setString(2,student.getSurname());
            statement.setInt(3,student.getAge());
            statement.executeUpdate();
            statement.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public static ArrayList<Students> getAllStudets(){
        PackageData pd = new PackageData();

        ArrayList<Students> studentList = new ArrayList<>();
        try {
            PreparedStatement statement = connection.prepareStatement("SELECT * FROM students");
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()){
                Long id = resultSet.getLong("id");
                String name = resultSet.getString("name");
                String surname = resultSet.getString("surname");
                int age = resultSet.getInt("age");
                studentList.add(new Students(id,name,surname,age));
                pd.setStudentList(studentList);
            }
            statement.close();
        }catch (Exception e){
            e.printStackTrace();
        }
        return pd.getStudentList();
    }

    public static void deleteItem(Long id){
        try {
            PreparedStatement statement = connection.prepareStatement("" +
                    "DELETE FROM students WHERE id = ?"
            );
            statement.setLong(1, id);
            int rows =statement.executeUpdate();
            statement.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
