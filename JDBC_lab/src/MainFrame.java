import javax.swing.*;
import java.awt.*;

public class MainFrame extends JFrame {
    private MainMenu mainMenu;
    private AddStudentFrame addFrame;
    private ListFrame listFrame;

    public MainFrame(){
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension dimension = toolkit.getScreenSize();
        setBounds(dimension.width/2-250,dimension.height/2-250,500,500);
        setTitle("STUDENT APPLICATION");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(null);
        setResizable(false);

        mainMenu = new MainMenu();
        mainMenu.setLocation(0,0);
        add(mainMenu);

        addFrame = new AddStudentFrame();
        addFrame.setLocation(0,0);
        add(addFrame);
        addFrame.setVisible(false);

        listFrame = new ListFrame();
        listFrame.setLocation(0,0);
        add(listFrame);
        listFrame.setVisible(false);

        repaint();
    }

    public void openMainMenu(){
        addFrame.setVisible(false);
        listFrame.setVisible(false);
        mainMenu.setVisible(true);
    }

    public void openAddFrame(){
        addFrame.setVisible(true);
        mainMenu.setVisible(false);
    }

    public void openListFrame(){
        listFrame.setVisible(true);
        mainMenu.setVisible(false);
    }
}
