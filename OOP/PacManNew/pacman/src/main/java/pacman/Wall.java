package pacman;

public class Wall extends Entity {

    /**
     * Wall constructor
     * 
     * @param width  Width of the wall
     * @param height Height of the wall
     * @param x      X coordinate of the wall
     * @param y      Y coordinate of the wall
     */
    Wall(double width, double height, double x, double y) {
        super(width, height, x, y);
    }
}
