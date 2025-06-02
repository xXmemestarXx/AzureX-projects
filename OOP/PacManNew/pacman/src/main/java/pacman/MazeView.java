package pacman;

import java.util.ArrayList;
import java.util.List;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class MazeView {

    private final Board board;
    private final double pixelHeight;
    private final double pixelWidth;
    private final int scale;
    private final List<MovableView<? extends Entity>> dynamics;
    private final List<ConsumableView<? extends Consumable>> consumables;

    private final StackPane contents;

    private final Pane wallPane;

    private final Pane consumablePane;

    private final Pane movablePane;

    /**
     * Constructor for MazeView.
     *
     * @param board the game board
     * @param scale the scale factor for the size of the maze
     */
    MazeView(Board board, int scale) {
        super();
        this.board = board;
        this.pixelHeight = scale * board.getHeight() * board.getTileSize();
        this.pixelWidth = scale * board.getWidth() * board.getTileSize();
        this.scale = scale;
        this.dynamics = new ArrayList<>();
        this.consumables = new ArrayList<>();

        contents = new StackPane();
        wallPane = new Pane();
        consumablePane = new Pane();
        movablePane = new Pane();

        contents.getChildren().add(this.wallPane);

        contents.getChildren().add(this.consumablePane);

        contents.getChildren().add(this.movablePane);

        drawWalls();

    }

    /**
     * Returns the height of the maze in pixels.
     *
     * @return the height of the maze
     */
    private void drawWalls() {
        for (int i = 0; i < board.getWalls().size(); i++) {
            Rectangle wallView = new Rectangle(board.getWalls().get(i).getWidth() * scale,
                    board.getWalls().get(i).getHeight() * scale, Color.BLUE);

            wallView.setTranslateX(board.getWalls().get(i).getX() * scale);
            wallView.setTranslateY(board.getWalls().get(i).getY() * scale);

            wallView.setStroke(Color.BLACK);

            wallView.setStrokeWidth(4);

            wallPane.getChildren().add(wallView);
        }
    }

    /**
     * Returns the width of the maze in pixels.
     *
     * @return the width of the maze
     */
    public void drawMovable(MovableView<? extends Entity> view) {
        dynamics.add(view);
        movablePane.getChildren().add(view.getNode());
    }

    /**
     * Draws a consumable view on the maze.
     *
     * @param view the consumable view to be drawn
     */
    public void drawConsumable(ConsumableView<? extends Consumable> view) {
        consumables.add(view);
        consumablePane.getChildren().add(view.getNode());
        view.getNode().toBack();
    }

    /**
     * Updates the views of all dynamics and consumables in the maze.
     * This method should be called to refresh the visual representation
     * of the entities based on their current state.
     */
    public void updateViews() {
        for (int i = 0; i < dynamics.size(); i++) {
            dynamics.get(i).updateView(scale);
        }
        for (int i = 0; i < consumables.size(); i++) {
            consumables.get(i).updateView(scale);
        }
    }

    /**
     * Returns the height of the maze in pixels.
     *
     * @return the height of the maze
     */
    public StackPane getGroup() {
        return this.contents;
    }

}