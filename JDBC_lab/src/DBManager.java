import java.sql.*;
import java.util.ArrayList;

public class DBManager {
    private Connection connection;
    public void setConnection() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection =DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/dbpractice?useUnicode=true&serverTimezone=UTC","root", ""
            );
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public void addStudent(Students student){
        try {
            PreparedStatement statement = connection.prepareStatement("" +
                    "INSERT INTO items (id,name,surname,age) " +
                    "VALUES (NULL, ?, ?, ?)"
            );
            statement.setString(1,student.getName());
            statement.setString(2,student.getSurname());
            statement.setInt(3,student.getAge());
            int rows = statement.executeUpdate();
            statement.close();
        }catch (Exception e){
            e.printStackTrace();
        }
    }

    public ArrayList<Students> getAllStudets(){
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
            }
            statement.close();
        }catch (Exception e){
            e.printStackTrace();
        }
        return studentList;
    }

    public void deleteItem(Long id){
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
