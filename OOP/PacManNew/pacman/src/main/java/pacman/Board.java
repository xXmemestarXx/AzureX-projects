package pacman;

import java.util.ArrayList;
import java.util.List;

public class Board {
    // Initializes board with walls, tiles, pills and power ups
    private final int tileSize;
    private final double pillSize;
    private final double powerUpSize;
    private final int height = BoardLayout.boardMatrix.length;
    private final int width = BoardLayout.boardMatrix[0].length;
    private final Tile[][] tiles;
    private final List<Wall> walls;
    private final List<Pill> pills;
    private final List<PowerUp> powerUps;

    /**
     * Constructor for the Board class.
     * Initializes the board with tiles, walls, pills, and power-ups based on the
     * predefined layout in BoardLayout.
     */
    Board() {
        tileSize = 10;
        powerUpSize = tileSize * 0.4;
        pillSize = tileSize * 0.2;
        walls = new ArrayList<Wall>();
        // Tiles are initialized based on the layout provided
        // by the BoardLayout class
        tiles = new Tile[height][width];
        pills = new ArrayList<Pill>();
        powerUps = new ArrayList<PowerUp>();
        int nextTileY = 0;
        // Adds walls and tiles to board
        for (int i = 0; i < BoardLayout.boardMatrix.length; i++) {
            int nextTileX = 0;
            for (int j = 0; j < BoardLayout.boardMatrix[i].length; j++) {
                // Adds tiles to board
                // If the tile is a wall, add a wall to the board
                if (BoardLayout.boardMatrix[i][j] == 0) {
                    Tile tile = new Tile(tileSize, tileSize, nextTileX, nextTileY);
                    tiles[i][j] = tile;
                } else {
                    Wall wall = new Wall(tileSize, tileSize, nextTileX, nextTileY);
                    walls.add(wall);
                }
                nextTileX += tileSize;
            }
            nextTileY += tileSize;
        }
        // Adds PowerUps to tiles according to layout
        addAllPowerUps();
        // Adds Pill to tiles without Power Ups
        addAllPills();
        // Removes pills where they shouldn't be
        removePillsInSpecialZones();
    }

    /**
     * Adds all pills to the board by iterating through all tiles and adding a pill
     * to each tile that does not have a consumable.
     */
    private void addAllPills() {
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[0].length; j++) {
                if (tiles[i][j] != null && tiles[i][j].getConsumable() == null) {
                    addPill(tiles[i][j]);
                }
            }
        }
    }

    /**
     * Adds all power-ups to the board based on the predefined layout in
     * BoardLayout.powerUps.
     * Each power-up is added to the center of the specified tile.
     */
    private void addAllPowerUps() {
        for (int k = 0; k < BoardLayout.powerUps.length; k++) {
            int i = BoardLayout.powerUps[k][0];
            int j = BoardLayout.powerUps[k][1];
            addPowerUp(powerUpSize, powerUpSize, tiles[i][j]);
        }
    }

    /**
     * Returns the number of pills left on the board.
     * 
     * @return int count of pills that are not eaten
     */
    public int pillsLeft() {
        int count = 0;
        for (int i = 0; i < pills.size(); i++) {
            if (!pills.get(i).isEaten()) {
                count++;
            }
        }
        return count;
    }

    /**
     * Removes pills in special zones where they should not be present.
     * This includes the left and right sides of the board and the ghost zone.
     */
    private void removePillsInSpecialZones() {
        // Helper method to process one zone
        removePillsInZone(10, 18, 0, 5); // Left side
        removePillsInZone(10, 18, 23, 27); // Right side
        removePillsInZone(12, 15, 11, 16); // Ghostzone
    }

    /**
     * Removes pills from a zone defined by the given row and column indices.
     */
    private void removePillsInZone(int rowStart, int rowEnd, int colStart, int colEnd) {
        for (int i = rowStart; i <= rowEnd && i < tiles.length; i++) {
            for (int j = colStart; j <= colEnd && j < tiles[0].length; j++) {
                Tile tile = tiles[i][j];
                if (tile != null && tile.getConsumable() instanceof Pill) {
                    Pill pill = (Pill) tile.getConsumable();
                    pills.remove(pill);
                    tile.setConsumable(null);
                }
            }
        }
    }

    /**
     * Returns the number of power-ups left on the board.
     * 
     * @return int count of power-ups that are not eaten
     */
    public int powerUpsLeft() {
        int count = 0;
        for (int i = 0; i < powerUps.size(); i++) {
            if (!powerUps.get(i).isEaten()) {
                count++;
            }
        }
        return count;
    }

    /**
     * Adds pill to the center of the tile
     * 
     * @param tile tile to add the pill
     */
    private void addPill(Tile tile) {
        if (tile != null) {
            double x = tile.getCenterX() - (pillSize / 2);
            double y = tile.getCenterY() - (pillSize / 2);
            Pill pill = new Pill(pillSize, pillSize, x, y);
            pills.add(pill);
            tile.setConsumable(pill);
        }
    }

    /**
     * Adds power up to the center of the tile
     * 
     * @param width  width of the power up
     * @param height height of the power up
     * @param tile   tile to add the power up
     */
    private void addPowerUp(double width, double height, Tile tile) {
        if (tile != null) {
            double x = tile.getCenterX() - (width / 2);
            double y = tile.getCenterY() - (height / 2);
            PowerUp powerUp = new PowerUp(width, height, x, y);
            powerUps.add(powerUp);
            tile.setConsumable(powerUp);
        }
    }

    /**
     * Returns the list of tiles
     * 
     * @param x x coordinate of the tile
     * @param y y coordinate of the tile
     */
    public Tile getTile(double x, double y) {
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[0].length; j++) {
                Tile tile = tiles[i][j];
                if (x >= tile.getX() && x < tile.getX() + tile.getWidth() &&
                        y >= tile.getY() && y < tile.getY() + tile.getHeight()) {
                    return tile;
                }
            }
        }
        return null;
    }

    /**
     * Returns the tile at the given coordinates
     * 
     * @param tileIJ array of two integers [row, column]
     * @return Tile at the given coordinates
     */
    public int getTileJ(double x) {
        return (int) x / tileSize;
    }

    /**
     * Returns the tile at the given coordinates
     * 
     * @param tileIJ array of two integers [row, column]
     * @return Tile at the given coordinates
     */
    public int getTileI(double y) {
        return (int) y / tileSize;
    }

    /**
     * Returns the tile at the given coordinates
     * 
     * @param y y coordinate of the tile
     * @param x x coordinate of the tile
     * @return array of two integers [row, column] representing the tile
     */
    public int[] getTileIJ(double y, double x) {
        int[] tileIJ = new int[2];
        tileIJ[0] = getTileI(y);
        tileIJ[1] = getTileJ(x);
        return tileIJ;
    }

    /**
     * Gets the amount of
     * veritcal tiles in the
     * layout
     * 
     * @return int length
     */
    public int getHeight() {
        return height;
    }

    /**
     * Gets the amount of
     * horizontal tiles in the
     * layout
     * 
     * @return int length
     */
    public int getWidth() {
        return width;
    }

    /**
     * Returns the tiles of the board.
     * 
     * @return 2D array of tiles
     */
    public Tile[][] getTiles() {
        return tiles;
    }

    /**
     * Returns the size of each tile in pixels.
     * 
     * @return int size of each tile
     */
    public int getTileSize() {
        return tileSize;
    }

    /**
     * Returns the size of each pill in pixels.
     * 
     * @return double size of each pill
     */
    public List<Wall> getWalls() {
        return walls;
    }

    /**
     * Returns the size of each power-up in pixels.
     * 
     * @return double size of each power-up
     */
    public List<Pill> getPills() {
        return pills;
    }

    /**
     * Returns the size of each power-up in pixels.
     * 
     * @return double size of each power-up
     */
    public List<PowerUp> getPowerUps() {
        return powerUps;
    }
}
