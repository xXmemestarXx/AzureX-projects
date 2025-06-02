package pacman;

import java.util.LinkedList;
import java.util.List;

public class FleePathFinder implements IPathFinder {

    // This pathfinding method is a greedy search that chooses the furthest tile
    // from target

    /**
     * Finds a path for the entity to flee from the target position on the board.
     * This method calculates the direction that maximizes the Manhattan distance
     * from the target position while ensuring the tile is valid for movement.
     *
     * @param startIJ  The starting position as an array [row, column].
     * @param targetIJ The target position to flee from as an array [row, column].
     * @param board    The game board representing the current state of the game.
     * @return A list containing the next position [row, column] to move to in order
     *         to maximize the distance from the target. If no valid move is found,
     *         the list will be empty.
     */
    @Override
    public List<int[]> findPath(int[] startIJ, int[] targetIJ, Board board) {
        int[] upIJ = { startIJ[0] - 1, startIJ[1] };
        int[] downIJ = { startIJ[0] + 1, startIJ[1] };
        int[] rightIJ = { startIJ[0], startIJ[1] + 1 };
        int[] leftIJ = { startIJ[0], startIJ[1] - 1 };
        int[][] directionIJs = { upIJ, downIJ, rightIJ, leftIJ };

        int bestDistance = 0;
        int[] bestDirection = null;
        for (int i = 0; i < directionIJs.length; i++) {
            int[] currentIJ = directionIJs[i];
            int currentDistance = (Math.max(currentIJ[0], targetIJ[0]) -
                    Math.min(currentIJ[0], targetIJ[0])) +
                    (Math.max(currentIJ[1], targetIJ[1]) -
                            Math.min(currentIJ[1], targetIJ[1]));
            if (currentDistance > bestDistance && isValidTile(currentIJ, board)) {
                bestDistance = currentDistance;
                bestDirection = currentIJ;
            }
        }
        List<int[]> path = new LinkedList<int[]>();
        if (bestDirection != null) {
            path.add(bestDirection);
        }
        return path;
    }

    /**
     * Checks if the given tile coordinates are valid for movement on the board.
     *
     * @param IJ    The coordinates of the tile as an array [row, column].
     * @param board The game board to check against.
     * @return true if the tile is within bounds and is a valid Tile, false
     *         otherwise.
     */
    private boolean isValidTile(int[] IJ, Board board) {
        boolean inBound;
        if (IJ[0] >= 0 && IJ[0] < board.getTiles().length && IJ[1] >= 0 && IJ[1] < board.getTiles()[0].length) {
            inBound = true;
        } else {
            inBound = false;
        }
        return inBound && board.getTiles()[IJ[0]][IJ[1]] instanceof Tile;
    }
}
