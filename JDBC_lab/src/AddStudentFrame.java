import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class AddStudentFrame extends Container {

    private JLabel name,surname,age;
    private JTextField nameTxt,surnameTxt,ageTxt;
    private JButton addButton,back;

    public AddStudentFrame(){
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension dimension = toolkit.getScreenSize();
        setBounds(dimension.width/2-250,dimension.height/2-250,500,500);
        setLayout(null);

        name = new JLabel("NAME:");
        name.setBounds(100,70,90,30);
        add(name);

        nameTxt = new JTextField();
        nameTxt.setBounds(200,70,200,30);
        add(nameTxt);

        surname = new JLabel("SURNAME:");
        surname.setBounds(100,120,90,30);
        add(surname);

        surnameTxt = new JTextField();
        surnameTxt.setBounds(200,120,200,30);
        add(surnameTxt);

        age = new JLabel("AGE:");
        age.setBounds(100,170,90,30);
        add(age);

        ageTxt = new JTextField();
        ageTxt.setBounds(200,170,200,30);
        add(ageTxt);

        addButton = new JButton("ADD");
        addButton.setBounds(100,300,100,30);
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = nameTxt.getText();
                String surname = surnameTxt.getText();
                int age = Integer.parseInt(ageTxt.getText());
                Students student = new Students(null,name,surname,age);
                Main.addStudent(student);
            }
        });
        add(addButton);

        back = new JButton("BACK");
        back.setBounds(300,300,100,30);
        back.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Main.frame.openMainMenu();
            }
        });
        add(back);
    }
}
