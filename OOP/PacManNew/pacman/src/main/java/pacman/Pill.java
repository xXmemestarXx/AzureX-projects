package pacman;

public class Pill extends Consumable {

    public final static int pillValue = 10;

    /**
     * Pill constructor
     * 
     * @param width  Width of the pill
     * @param height Height of the pill
     * @param x      X coordinate of the pill
     * @param y      Y coordinate of the pill
     */
    public Pill(double width, double height, double x, double y) {
        super(width, height, x, y);
    }
}
