package pacman;

import java.util.List;

/**
 * Finds a path from a starting position to a target position on the given
 * board.
 *
 * @param startIJ  an array representing the starting position [i, j] on the
 *                 board.
 * @param targetIJ an array representing the target position [i, j] on the
 *                 board.
 * @param board    the game board on which the pathfinding is performed.
 * @return a list of integer arrays, where each array represents a position [i,
 *         j]
 *         on the path from the start to the target. Returns an empty list if no
 *         path is found.
 */

public interface IPathFinder {
    public List<int[]> findPath(int[] startIJ, int[] targetIJ, Board board);
}
