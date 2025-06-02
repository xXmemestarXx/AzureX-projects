package pacman;

public class PowerUp extends Consumable {

    public final static int powerValue = 50;

    /**
     * PowerUp constructor
     * 
     * @param width  Width of the power-up
     * @param height Height of the power-up
     * @param x      X coordinate of the power-up
     * @param y      Y coordinate of the power-up
     */
    PowerUp(double width, double height, double x, double y) {
        super(width, height, x, y);
    }

}
