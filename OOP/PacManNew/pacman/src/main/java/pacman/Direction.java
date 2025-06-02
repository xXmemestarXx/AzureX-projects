package pacman;

/**
 * Enum representing the four cardinal directions.
 * Provides a method to get the opposite direction.
 */
public enum Direction {
    UP, DOWN, RIGHT, LEFT;

    /**
     * Returns the opposite direction of the current direction.
     *
     * @return The opposite direction.
     */
    public Direction opposite() {
        switch (this) {
            case UP:
                return DOWN;
            case DOWN:
                return UP;
            case LEFT:
                return RIGHT;
            case RIGHT:
                return LEFT;
            default:
                return null;
        }
    }
}