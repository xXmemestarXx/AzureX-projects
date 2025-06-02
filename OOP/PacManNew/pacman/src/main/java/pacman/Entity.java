package pacman;

public abstract class Entity {
    private final double boxWidth;
    private final double boxHeight;
    private double x;
    private double y;

    /**
     * Entity constructor
     * 
     * @param width  width of the entity
     * @param height height of the entity
     * @param x      x coordinate of the entity
     * @param y      y coordinate of the entity
     */

    Entity(double width, double height, double x, double y) {
        this.boxWidth = width;
        this.boxHeight = height;
        this.x = x;
        this.y = y;
    }

    /**
     * Set the x coordinate of the entity
     * 
     * @param x x coordinate of the entity
     */
    public void setX(double x) {
        this.x = x;
    }

    /**
     * Set the y coordinate of the entity
     * 
     * @param y y coordinate of the entity
     */
    public void setY(double y) {
        this.y = y;
    }

    /**
     * Get the x coordinate of the center of the entity
     * 
     * @return the x coordinate of the center of the entity
     */
    public double getCenterX() {
        return x + (boxWidth / 2);
    }

    /**
     * Get the y coordinate of the center of the entity
     * 
     * @return the y coordinate of the center of the entity
     */
    public double getCenterY() {
        return y + (boxHeight / 2);
    }

    /**
     * Get the x coordinate of the entity
     * 
     * @return the x coordinate of the entity
     */
    public double getX() {
        return x;
    }

    /**
     * Get the y coordinate of the entity
     * 
     * @return the y coordinate of the entity
     */
    public double getY() {
        return y;
    }

    /**
     * Get the width of the entity
     * 
     * @return the width of the entity
     */
    public double getWidth() {
        return boxWidth;
    }

    /**
     * Get the height of the entity
     * 
     * @return the height of the entity
     */
    public double getHeight() {
        return boxHeight;
    }
}
