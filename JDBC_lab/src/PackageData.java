import java.util.*;
import java.io.*;

public class PackageData implements Serializable{

    private ArrayList<Students> studentList;
    private Students student;
    private String operationType;

    public PackageData(){

    }

    public void setStudent(Students student){
        this.student = student;
    }

    public Students getStudent(){
        return this.student;
    }

    public void setStudentList(ArrayList<Students> students){
        this.studentList = studentList;
    }

    public ArrayList<Students> getStudentList(){
        return this.studentList;
    }

    public void setOperationType(String operationType){
        this.operationType = operationType;
    }

    public String getOperationType(){
        return this.operationType;
    }

}