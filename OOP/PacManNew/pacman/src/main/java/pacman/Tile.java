package pacman;

public class Tile extends Entity {
    private Consumable consumable;

    /**
     * Tile constructor
     * 
     * @param width
     * @param height
     * @param x
     * @param y
     */

    public Tile(double width, double height, double x, double y) {
        super(width, height, x, y);
    }

    /**
     * Checks if the tile contains a PowerUp.
     * 
     * @return true if the consumable on the tile is an instance of PowerUp, false
     *         otherwise.
     */
    public boolean containsPowerUp() {
        return this.consumable instanceof PowerUp;
    }

    /**
     * Sets the consumable on the tile.
     */
    public void setConsumable(Consumable consumable) {
        this.consumable = consumable;
    }

    /**
     * Returns the consumable on the tile.
     * 
     * @return the consumable on the tile, which can be a PowerUp or a Pill.
     */
    public Consumable getConsumable() {
        return this.consumable;
    }
}
