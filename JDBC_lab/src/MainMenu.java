import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class MainMenu extends Container {

    private JButton addButton,listButton,exit;
    private ArrayList<Students>students;

    public MainMenu(){
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension dimension = toolkit.getScreenSize();
        setBounds(dimension.width/2-250,dimension.height/2-250,500,500);
        setLayout(null);

        addButton = new JButton("ADD STUDENT");
        addButton.setBounds(150,100,200,30);
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Main.frame.openAddFrame();
                Main.frame.repaint();
            }
        });
        add(addButton);


        listButton = new JButton("LIST STUDENTS");
        listButton.setBounds(150,150,200,30);
        add(listButton);
        listButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Main.frame.openListFrame();

            }
        });


        exit = new JButton("EXIT");
        exit.setBounds(150,200,200,30);
        exit.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
        add(exit);
    }


}
