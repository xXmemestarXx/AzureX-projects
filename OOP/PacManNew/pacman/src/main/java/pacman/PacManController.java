package pacman;

public class PacManController {
    private final PacMan pacMan;
    private final ICollisionChecker<Wall, PacMan> wallCollisionChecker;
    private Direction desiredDirection;

    /**
     * Constructor for PacManController
     * 
     * @param pacMan               pacMan object
     * @param wallCollisionChecker collision checker for walls
     */
    PacManController(PacMan pacMan, WallCollisionChecker wallCollisionChecker) {
        this.pacMan = pacMan;
        this.wallCollisionChecker = wallCollisionChecker;
    }

    /**
     * Moves PacMan in the direction of the desired direction
     *
     */
    public void move() {
        updateDirection();
        if (isValidNextMove()) {
            pacMan.setX(pacMan.getNextX(pacMan.getDirection()));
            pacMan.setY(pacMan.getNextY(pacMan.getDirection()));
        }
    }

    /**
     * Checks if the next move of PacMan is valid (i.e., no collision with walls)
     * 
     * @return true if the next move is valid, false otherwise
     */
    private boolean isValidNextMove() {
        double prevX = pacMan.getX();
        double prevY = pacMan.getY();
        pacMan.setX(pacMan.getNextX(pacMan.getDirection()));
        pacMan.setY(pacMan.getNextY(pacMan.getDirection()));
        boolean isCollision = wallCollisionChecker.hasCollision(pacMan);
        pacMan.setX(prevX);
        pacMan.setY(prevY);
        return !isCollision;
    }

    /**
     * Sets the desired direction of PacMan
     * 
     * @param desiredDirection desired direction
     */
    public void setDesiredDirection(Direction desiredDirection) {
        this.desiredDirection = desiredDirection;
    }

    /**
     * Updates the direction of PacMan
     *
     */
    private void updateDirection() {
        if (desiredDirection != null) {
            Direction oldDirection = pacMan.getDirection();
            pacMan.setDirection(desiredDirection);
            if (isValidNextMove()) {
                desiredDirection = null;
            } else {
                pacMan.setDirection(oldDirection);
            }
        }
    }
}
