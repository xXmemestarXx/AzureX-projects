package pacman;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Queue;

public class BFSPathFinder implements IPathFinder {

    private Map<String, int[]> origin;
    private List<String> visited;
    private Queue<int[]> queue;

    /**
     * Finds the shortest path from the start position to the target position on the
     * board using BFS.
     *
     * @param startIJ  The starting position as an array of two integers [row,
     *                 column].
     * @param targetIJ The target position as an array of two integers [row,
     *                 column].
     * @param board    The game board containing tiles.
     * @return A list of integer arrays representing the path from start to target.
     */
    @Override
    public List<int[]> findPath(int[] startIJ, int[] targetIJ, Board board) {

        origin = new HashMap<>();
        visited = new ArrayList<>();
        queue = new LinkedList<>();

        visited.add(Arrays.toString(startIJ));
        queue.add(startIJ);

        // Expanding until no valid route or route to pacMan found
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            if (Arrays.equals(current, targetIJ)) {
                break;
            }
            List<int[]> neighboors = validNeighboors(current, board);
            for (int i = 0; i < neighboors.size(); i++) {
                visited.add(Arrays.toString(neighboors.get(i)));
                origin.put(Arrays.toString(neighboors.get(i)), current);
            }
            queue.addAll(neighboors);
        }

        LinkedList<int[]> path = new LinkedList<>();
        path.addFirst(targetIJ);

        String currentKey = Arrays.toString(targetIJ);

        // Backtracking to find the path from target to start
        while (!Arrays.equals(origin.get(currentKey), startIJ)) {
            path.addFirst(origin.get(currentKey));
            currentKey = Arrays.toString(origin.get(currentKey));
        }
        return path;
    }

    /**
     * Finds the valid neighboring tiles of a given tile on the board.
     *
     * @param IJ    The coordinates of the tile as an array of two integers [row,
     *              column].
     * @param board The game board containing tiles.
     * @return A list of valid neighboring tile coordinates.
     */
    private List<int[]> validNeighboors(int[] IJ, Board board) {
        List<int[]> neighboors = new ArrayList<>();
        int[] upIJ = { IJ[0] - 1, IJ[1] };
        int[] downIJ = { IJ[0] + 1, IJ[1] };
        int[] rightIJ = { IJ[0], IJ[1] + 1 };
        int[] leftIJ = { IJ[0], IJ[1] - 1 };
        neighboors.add(upIJ);
        neighboors.add(downIJ);
        neighboors.add(rightIJ);
        neighboors.add(leftIJ);
        List<int[]> validNeighboors = new ArrayList<>();
        for (int i = 0; i < neighboors.size(); i++) {
            if (isValidTile(neighboors.get(i), board) && !visited.contains(Arrays.toString(neighboors.get(i)))) {
                validNeighboors.add(neighboors.get(i));
            }
        }
        return validNeighboors;
    }

    /**
     * Checks if a given tile is valid on the board.
     *
     * @param IJ    The coordinates of the tile as an array of two integers [row,
     *              column].
     * @param board The game board containing tiles.
     * @return True if the tile is valid, false otherwise.
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