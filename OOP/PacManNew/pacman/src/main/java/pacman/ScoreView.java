package pacman;

import javafx.geometry.Insets;
import javafx.scene.Group;
import javafx.scene.layout.HBox;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.scene.text.TextAlignment;
import javafx.scene.paint.Color;

public class ScoreView {

    /**
     * The score that is shown
     * on the GUI.
     */
    private int score;

    /**
     * The high score that is shown
     * on the GUI.
     *
     * Note: is the Class Integer
     * and not the data type int
     */

    /**
     * The height of the ScoreView
     * in pixels
     */
    private final double height;

    /**
     * The width of the ScoreView
     * in pixels
     */
    private final double width;

    /**
     * The canvas of the ScoreView
     * which is used to draw shapes
     */

    /**
     * The class that actually draws
     * on the Canvas object
     */

    /**
     * The pane which contains the
     * score text
     */
    private final HBox scoreBox;

    /**
     * Group that contains both the Canvas
     * background and the Hbox which contains
     * the text
     */
    private final Group scoreViewGroup;

    /**
     * The Text object that shows the score
     * on the GUI
     */
    private final Text scoreText;

    /**
     * Constructor for the ScoreView class.
     * Initializes the score view with a given board,
     * scale, height of bars, and width of maze.
     *
     * @param board        The game board.
     * @param scale        The scale factor for the text size.
     * @param heightOfBars The height of the bars in pixels.
     * @param widthOfMaze  The width of the maze in pixels.
     */
    public ScoreView(Board board, int scale, double heightOfBars, double widthOfMaze) {

        this.height = heightOfBars;

        this.width = widthOfMaze;

        this.scoreBox = new HBox();

        this.scoreBox.setFillHeight(false);

        this.scoreBox.setPrefSize(this.width, this.height);

        this.scoreBox.setSpacing(this.width / 2);

        this.scoreBox.setPadding(new Insets(15, 12, 15, 12));

        this.scoreViewGroup = new Group(scoreBox);

        this.scoreText = new Text(Integer.toString(score));

        this.setUpScoreText(board, scale);

        this.updateScoreText(100);

    };

    /**
     * Sets up the score text on the GUI.
     * It initializes the font, color, and position
     * of the score text.
     *
     * @param board The game board used to determine tile size.
     * @param scale The scale factor for the font size.
     */
    private void setUpScoreText(Board board, int scale) {

        Font theFont = Font.font("Comic Sans MS", FontWeight.BOLD, (board.getTileSize() * scale / 2));

        scoreText.setStroke(Color.WHITE);
        scoreText.setFill(Color.WHITESMOKE);

        scoreText.setStrokeWidth(0.5);

        scoreText.setFont(theFont);

        scoreText.setLineSpacing(this.width / 4);

        scoreText.setTextAlignment(TextAlignment.CENTER);

        scoreText.setText("Score" + "\n" + Integer.toString(this.score));

        scoreText.setX(width / 2);

        scoreText.setY(height / 2);

        scoreBox.getChildren().addAll(scoreText);
    }

    /**
     * Updates the score text displayed in the ScoreView.
     * This method changes the score and updates the text accordingly.
     *
     * @param newScore The new score to be displayed.
     */
    public void updateScoreText(int newScore) {
        this.score = newScore;
        scoreText.setText("Score" + "\n" + Integer.toString(this.score));
    }

    /**
     * Appends the score view background to a given group.
     *
     * @param g The group to which the score view background will be added.
     */
    public void appendBackgroundToGroup(Group g) {
        g.getChildren().add(scoreViewGroup);
    }

    /**
     * Returns the Group that contains the score view.
     *
     * @return The Group containing the score view.
     */
    public Group getGroup() {
        return this.scoreViewGroup;
    }

    /**
     * Returns the height of the ScoreView.
     *
     * @return The height of the ScoreView in pixels.
     */
    public double getHeight() {
        return this.height;
    }

    /**
     * Returns the width of the ScoreView.
     *
     * @return The width of the ScoreView in pixels.
     */
    public double getWidth() {
        return this.width;
    }
}
