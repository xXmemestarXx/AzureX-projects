package pacman;

import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.geometry.Pos;

public class EndView {

    private final GameManager gameManager;

    /**
     * Constructor for EndView.
     *
     * @param gameManager The GameManager instance to handle game state.
     */
    EndView(GameManager gameManager) {
        this.gameManager = gameManager;
    }

    /**
     * Returns a VBox layout for the end view of the game.
     *
     * @param sceneWidth  The width of the scene.
     * @param sceneHeight The height of the scene.
     * @return A VBox containing the end view elements.
     */
    public VBox getView(double sceneWidth, double sceneHeight) {
        Label endLabel = new Label("Game Over!");
        endLabel.setStyle("-fx-font-size: 30px; -fx-text-fill: red;");

        Button resetButton = new Button("Reset");
        resetButton.setOnAction(e -> gameManager.resetGame());

        VBox layout = new VBox(20, endLabel, resetButton);
        layout.setAlignment(Pos.CENTER);
        layout.setStyle("-fx-background-color: rgba(0, 0, 0, 0.7); -fx-padding: 20px;");
        layout.getStyleClass().add("end-view");

        // Manually center since Group doesn't auto-layout
        layout.setLayoutX((sceneWidth - 300) / 2);
        layout.setLayoutY((sceneHeight - 150) / 2);

        return layout;
    }

}