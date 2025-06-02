package pacman;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

public class App extends Application {
    static GUI boardView;
    static Board board;
    static GameManager gameManager;
    static PacManInputHandler pacManInputHandler;

    static Stage stage;

    @Override
    public void start(Stage stage) {

        Group root = new Group();
        Scene scene = new Scene(root, Color.BLACK);

        App.stage = stage;
        gameManager = new GameManager(2, root, scene);
        boardView = gameManager.getGUI();
        pacManInputHandler = gameManager.getPacManInputHandler();

        root.getChildren().add(boardView.getGroup());

        stage.setScene(scene);
        stage.show();

        gameManager.startLoop();

        scene.setOnKeyPressed(pacManInputHandler::keyPressed);
    }

    public static void main(String[] args) {
        launch(args);
    }
}
