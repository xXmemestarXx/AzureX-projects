package pacman;

public class Consumable extends Entity {
    private boolean eaten;

    /**
     * Constructor for Consumable
     * 
     * @param width  the width of the consumable
     * @param height the height of the consumable
     * @param x      the x coordinate of the consumable
     * @param y      the y coordinate of the consumable
     */
    Consumable(double width, double height, double x, double y) {
        super(width, height, x, y);
        this.eaten = false;
    }

    /**
     * Marks the consumable as eaten or not eaten.
     * 
     * @param eaten true if the consumable is eaten, false otherwise
     */
    public void setEaten(boolean eaten) {
        this.eaten = eaten;
    }

    /**
     * Checks if the consumable is eaten.
     * 
     * @return true if the consumable is eaten, false otherwise
     */
    public boolean isEaten() {
        return eaten;
    }
}
