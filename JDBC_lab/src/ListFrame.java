import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class ListFrame extends Container {

    private JButton back;
    private JTextArea area;
    private ArrayList<Students>students;
    private JList list;

    public ListFrame(){
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension dimension = toolkit.getScreenSize();
        setBounds(dimension.width/2-250,dimension.height/2-250,500,500);
        setLayout(null);

        area = new JTextArea();
        area.setBounds(50,50,400,300);
        area.setEditable(false);
        add(area);

        PackageData packageData = null;
        try{
            ArrayList<Students> students=packageData.getStudentList();
            for (int i=0;i<students.size();i++){
                area.append(students.get(i).toString()+"\n");
            }
        }catch (Exception e){
            e.printStackTrace();
        }


        back = new JButton("BACK");
        back.setBounds(200,400,100,30);
        back.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Main.frame.openMainMenu();
            }
        });
        add(back);
    }
}
