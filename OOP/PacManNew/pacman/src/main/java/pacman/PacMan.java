package pacman;

public class PacMan extends Movable {
    /**
     * Constructor for PacMan
     * 
     * @param width  width of the PacMan
     * @param height height of the PacMan
     * @param x      x coordinate of the PacMan
     * @param y      y coordinate of the PacMan
     * @param step   step size of the PacMan
     */
    PacMan(double width, double height, double x, double y, double step) {
        super(width, height, x, y, step);
    }

    /**
     * Resets the position of PacMan to its initial spawn position
     */
    @Override
    public void resetPosition() {
        super.resetPosition();
        this.setDirection(Direction.RIGHT);
    }
}
