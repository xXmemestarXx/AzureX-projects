package pacman;

import java.util.LinkedList;

import javafx.scene.Node;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.HBox;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;

public class LivesView {

    /**
     * The the amount of lives PacMan
     * has
     */
    private final int maxLives;

    /**
     * The images that are used to
     * show the lives
     */
    private final LinkedList<Node> lifeIcons;

    /**
     * The height of the ScoreView
     * in pixels
     */
    private double height;

    /**
     * The width of the ScoreView
     * in pixels
     */
    private double width;

    private Board board;

    private int scale;

    /**
     * The pane which contains the
     * the icons for lives
     */
    private HBox livesBox;

    /**
     * box that contains both the the HBoxes
     */
    private final AnchorPane livesPane;

    /**
     * Constructor for LivesView.
     *
     * @param board        the game board
     * @param scale        the scale factor for the size of the icons
     * @param maxLives     the maximum number of lives PacMan can have
     * @param heightOfBars the height of the lives view in pixels
     * @param widthOfMaze  the width of the maze in pixels
     */
    LivesView(Board board, int scale, int maxLives, double heightOfBars, double widthOfMaze) {

        double d = 1.0 * board.getTileSize();

        this.board = board;

        this.scale = scale;

        this.height = heightOfBars;

        this.width = widthOfMaze;

        this.maxLives = maxLives;

        this.livesPane = new AnchorPane();

        this.livesPane.setPrefSize(this.width, this.height);

        this.lifeIcons = new LinkedList<Node>();

        this.livesBox = new HBox();

        this.livesPane.getChildren().addAll(livesBox);

        setUpIcons();

        AnchorPane.setBottomAnchor(livesBox, d);

        AnchorPane.setLeftAnchor(livesBox, d);
    };

    /**
     * Sets up the icons for the lives view.
     * This method clears any existing icons and adds new ones based on the
     * maximum number of lives.
     */
    private void setUpIcons() {
        lifeIcons.clear();
        livesBox.getChildren().clear();

        for (int i = 0; i < this.maxLives; i++) {
            ImageView lifeIcon = new ImageView(new Image("heart.png"));
            lifeIcon.setPreserveRatio(false);
            lifeIcon.setFitHeight(this.board.getTileSize() * this.scale * 3);
            lifeIcon.setFitWidth(this.board.getTileSize() * this.scale * 3);
            lifeIcons.add(lifeIcon);
            livesBox.getChildren().add(lifeIcon);
        }
    }

    /**
     * Updates the lives view by removing the first life icon.
     * This method is called when PacMan loses a life.
     *
     * @param lives the current number of lives left
     */
    public void updateLives(int lives) {
        if (lives < lifeIcons.size()) {
            this.livesBox.getChildren().remove(0);
            this.lifeIcons.remove(0);
        }
    }

    /**
     * Resets the lives view to its initial state.
     * This method clears the current icons and sets up new ones based on the
     * maximum number of lives.
     */
    public void reset() {
        setUpIcons();
    }

    /**
     * Returns the HBox containing the life icons.
     *
     * @return the HBox that contains the life icons
     */
    public Node getGroup() {
        return this.livesPane;
    }

    /**
     * Returns the height of the lives view.
     *
     * @return the height of the lives view in pixels
     */
    public double getHeight() {
        return this.height;
    }

    /**
     * Returns the width of the lives view.
     *
     * @return the width of the lives view in pixels
     */
    public double getWidth() {
        return this.width;
    }

    /**
     * Sets the height of the lives view.
     *
     * @param newHeight the new height to set
     */
    public void setHeight(double newHeight) {
        this.height = newHeight;
    }

    /**
     * Sets the width of the lives view.
     *
     * @param newWidth the new width to set
     */
    public void setWidth(double newWidth) {
        this.height = newWidth;
    }

}
