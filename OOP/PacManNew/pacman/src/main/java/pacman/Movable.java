package pacman;

public abstract class Movable extends Entity {
    private double step;
    private Direction direction;
    private final double spawnX;
    private final double spawnY;

    /**
     * Constructor for Movable
     * 
     * @param width  width of the entity
     * @param height height of the entity
     * @param x      x coordinate of the entity
     * @param y      y coordinate of the entity
     * @param step   step size of the entity
     */
    Movable(double width, double height, double x, double y, double step) {
        super(width, height, x, y);
        this.spawnX = x;
        this.spawnY = y;
        this.step = step;
        resetPosition();
    }

    /**
     * 
     * @param direction direction of the entity
     * @return the next x coordinate of the entity
     */
    public double getNextX(Direction direction) {
        if (direction == Direction.LEFT) {
            return this.getX() - this.step;
        } else if (direction == Direction.RIGHT) {
            return this.getX() + this.step;
        } else {
            return this.getX();
        }
    }

    /**
     * 
     * @param direction direction of the entity
     * @return the next y coordinate of the entity
     */
    public double getNextY(Direction direction) {
        if (direction == Direction.DOWN) {
            return this.getY() + this.step;
        } else if (direction == Direction.UP) {
            return this.getY() - this.step;
        } else {
            return this.getY();
        }
    }

    /**
     * Sets the direction of the entity
     * 
     * @param direction direction of the entity
     */
    public void setDirection(Direction direction) {
        this.direction = direction;
    }

    /**
     * Gets the direction of the entity
     * 
     * @return the direction of the entity
     */
    public Direction getDirection() {
        return this.direction;
    }

    /**
     * @return the step size of the entity
     */
    public void setStep(double step) {
        this.step = step;
    }

    /**
     * Reset position of the movable object
     */
    public void resetPosition() {
        this.setX(spawnX);
        this.setY(spawnY);
    }
}
