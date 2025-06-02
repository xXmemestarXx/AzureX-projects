package pacman;

public class Ghost extends Movable {

    private boolean vulnerable;
    private boolean chase;
    private final double scatterX;
    private final double scatterY;
    private final double normalStep;
    private final double fleeStep;
    final static int ghostValue = 500;

    /**
     * Constructor for Ghost.
     *
     * @param width    the width of the ghost
     * @param height   the height of the ghost
     * @param x        the x coordinate of the ghost
     * @param y        the y coordinate of the ghost
     * @param scatterX the x coordinate for scatter mode
     * @param scatterY the y coordinate for scatter mode
     * @param step     the step size for movement
     */
    Ghost(int width, int height, double x, double y, double scatterX, double scatterY, int step) {
        super(width, height, x, y, step);
        this.vulnerable = false;
        this.normalStep = step;
        this.fleeStep = step / 2;
        this.scatterX = scatterX;
        this.scatterY = scatterY;
    }

    /**
     * Checks if the ghost is aligned with the grid based on the tile size.
     *
     * @param tileSize the size of the tile
     * @return true if the ghost is aligned, false otherwise
     */
    public boolean isAllignedY(int tileSize) {
        return this.getY() % tileSize == 0;
    }

    /**
     * Checks if the ghost is aligned with the grid based on the tile size.
     *
     * @param tileSize the size of the tile
     * @return true if the ghost is aligned, false otherwise
     */
    public boolean isAllignedX(int tileSize) {
        return this.getX() % tileSize == 0;
    }

    /**
     * Updates the step size of the ghost based on its state.
     * If the ghost is vulnerable, it flees with a smaller step size.
     * If the ghost is not vulnerable and aligned with the grid, it uses the normal
     * step size.
     */
    public void updateStep() {
        if (vulnerable) {
            this.setStep(fleeStep);
            // Modulus to avoid odd alignment
        } else if (this.getX() % normalStep == 0 && this.getY() % normalStep == 0) {
            this.setStep(normalStep);
        }
    }

    /**
     * Resets the ghost to its initial state.
     */
    public boolean isVulnerable() {
        return vulnerable;
    }

    /**
     * Sets the ghost's vulnerability state.
     *
     * @param vulnerable true if the ghost is vulnerable, false otherwise
     */
    public void setVulnerable(boolean vulnerable) {
        this.vulnerable = vulnerable;
    }

    /**
     * Returns whether the ghost is in chase mode.
     *
     * @return true if the ghost is in chase mode, false otherwise
     */
    public boolean isChase() {
        return chase;
    }

    /**
     * Sets the ghost's chase state.
     *
     * @param chase true if the ghost is in chase mode, false otherwise
     */
    public void setChase(boolean chase) {
        this.chase = chase;
    }

    /**
     * Returns the x coordinate for scatter mode.
     *
     * @return the x coordinate for scatter mode
     */
    public double getScatterX() {
        return scatterX;
    }

    /**
     * Returns the y coordinate for scatter mode.
     *
     * @return the y coordinate for scatter mode
     */
    public double getScatterY() {
        return scatterY;
    }
}
