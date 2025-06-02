package pacman;

import javafx.geometry.Pos;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.scene.text.TextAlignment;

public class GUI {
    /**
     * The maps where the game
     * takes place
     */
    private final Board board;

    /**
     * An amount that multiplies
     * the size of the GUI window
     */
    private final int scale;

    /**
     * The height of the maze
     * meassured in pixels
     * 
     * Used for middle canvas
     */
    private final double mazeHeight;

    /**
     * The height of the top and bottom
     * bars meassured in pixels
     * 
     * Used for the upper and lower
     * canvas
     */
    private final double barsHeight;

    /**
     * Width of the GUI Pane
     * in pixels (as a double)
     */
    private final double boardWidth;

    /**
     * Houses the upper part of the GUI
     * such as the sore
     */
    private final ScoreView scoreView;

    /**
     * Houses the middle part of the GUI
     * which includes the maze with PacMan
     */
    private final MazeView mazeView;

    /**
     * Houses the lower part of the GUI
     * that contains the amount of lives
     * and PowerUps
     */
    private final LivesView livesView;

    /**
     * Group that contains the three parts
     * of the GUI
     */

    /**
     * Creates a pane that
     * vertically stacks the three
     * parts of the GUI
     */
    private final VBox guiBox;

    /**
     * Constuctor of the GUI
     * 
     * @param board
     * @param scale
     */
    GUI(Board board, int scale) {
        this.board = board;

        this.mazeHeight = board.getHeight();
        this.barsHeight = (mazeHeight / 6);
        this.boardWidth = board.getWidth();

        this.scale = scale;

        this.scoreView = new ScoreView(this.board, this.scale, barsHeight, boardWidth);

        this.mazeView = new MazeView(this.board, this.scale);

        this.guiBox = new VBox();

        this.livesView = new LivesView(this.board, this.scale, 3, barsHeight + 100, boardWidth);

        setUpGUIBox();

    }

    /**
     * Sets up the GUI box that contains
     * the three parts of the GUI
     * 
     * The title is added to the top of the GUI
     * and the score, maze, and lives views are added
     * below it.
     */
    private void setUpGUIBox() {
        Text title = new Text("PacMan");

        title.setFont(Font.font("Comic Sans MS", FontWeight.BOLD, (this.board.getWidth() * this.scale)));

        title.setStroke(Color.ORANGE);
        title.setFill(Color.YELLOW);

        title.setStrokeWidth(0.5);

        title.setTextAlignment(TextAlignment.CENTER);

        guiBox.getChildren().add(title);

        guiBox.getChildren().add(scoreView.getGroup());

        guiBox.getChildren().add(mazeView.getGroup());

        guiBox.getChildren().add(livesView.getGroup());

        guiBox.setAlignment(Pos.CENTER);
    }

    /**
     * Updates all the views
     * in the GUI
     * 
     * @param score
     * @param lives
     */
    public void updateAllViews(int score, int lives) {

        this.scoreView.updateScoreText(score);

        this.mazeView.updateViews();

        this.livesView.updateLives(lives);

    }

    /**
     * Resets the lives view
     * to a new amount of lives
     * 
     * @param newLives
     */
    public void resetLives(int newLives) {
        livesView.reset();
    }

    /**
     * Used to draw moving
     * things on the maze
     * such as PacMan and ghosts
     * 
     * @param view
     */
    public void drawMovable(MovableView<? extends Entity> view) {
        // System.out.println("ello 3");
        this.mazeView.drawMovable(view);
    }

    /**
     * Used to draw non-moving
     * things on the maze such
     * as pills and PowerUps
     * 
     * @param view
     */
    public void drawConsumable(ConsumableView<? extends Consumable> view) {
        this.mazeView.drawConsumable(view);
    }

    /**
     * Returns the VBox that contains
     * the three parts of the GUI
     * 
     * @return VBox containing the GUI
     */
    public VBox getGroup() {
        return this.guiBox;
    }
}
