package pacman;

import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

/**
 * Handles input events for PacMan, allowing it to change direction based on
 * keyboard input.
 */
public class PacManInputHandler {
    private final PacManController pacMan;

    PacManInputHandler(PacManController pacMan) {
        this.pacMan = pacMan;
    }

    /**
     * Handles key pressed events to change PacMan's desired direction.
     *
     * @param event the KeyEvent containing the key pressed information
     */
    public void keyPressed(KeyEvent event) {
        if (event.getCode().equals(KeyCode.UP)) {
            pacMan.setDesiredDirection(Direction.UP);
        } else if (event.getCode().equals(KeyCode.DOWN)) {
            pacMan.setDesiredDirection(Direction.DOWN);
        } else if (event.getCode().equals(KeyCode.LEFT)) {
            pacMan.setDesiredDirection(Direction.LEFT);
        } else if (event.getCode().equals(KeyCode.RIGHT)) {
            pacMan.setDesiredDirection(Direction.RIGHT);
        }

    }

}