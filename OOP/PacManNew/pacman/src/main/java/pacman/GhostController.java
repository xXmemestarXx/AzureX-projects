package pacman;

import java.util.Arrays;
import java.util.List;

public class GhostController {

    private final Ghost ghost;

    private final PacMan pacMan;
    private int[] lastPacManIJ;

    private final IPathFinder pathFinder;
    private final IPathFinder fleePathFinder;

    private final Board board;

    private List<int[]> currentPath;

    // One unit amounts to one update
    private final int spawnTime;
    private final int chaseTime;

    private int leftSpawnTime;
    private int leftChaseTime;

    /**
     * Constructor for GhostController.
     *
     * @param ghost     the ghost to control
     * @param pacMan    the PacMan object
     * @param board     the game board
     * @param spawnTime time until ghost can spawn again
     * @param chaseTime time until ghost can change from chase to scatter mode
     */
    GhostController(Ghost ghost, PacMan pacMan, Board board, int spawnTime, int chaseTime) {
        this.ghost = ghost;
        this.pacMan = pacMan;
        this.board = board;

        this.spawnTime = spawnTime;
        this.chaseTime = chaseTime;
        this.leftSpawnTime = this.spawnTime;
        this.leftChaseTime = this.chaseTime;

        this.pathFinder = new BFSPathFinder();
        this.fleePathFinder = new FleePathFinder();
    }

    /**
     * Resets the ghost's state and position.
     * This method resets the spawn time, chase time, and the ghost's position.
     */
    public void reset() {
        this.leftSpawnTime = 100;
        this.leftChaseTime = this.chaseTime;
        this.ghost.setChase(false);
        resetPosition();
    }

    /**
     * Resets the ghost's position to its initial state.
     * This method calls the ghost's resetPosition method to set its coordinates
     * back to the starting point.
     */
    private void resetPosition() {
        ghost.resetPosition();
    }

    /**
     * Updates the ghost's state and position based on the game logic.
     * This method checks the ghost's current state (vulnerable, chase, or scatter)
     * and updates its position accordingly. It also manages the spawn and chase
     * timers.
     */
    public void update() {
        ghost.updateStep();
        if (this.leftSpawnTime > 0) {
            this.leftSpawnTime--;
        } else if (ghost.isVulnerable()) {
            flee();
            takeStep();
        } else if (ghost.isChase()) {
            if (leftChaseTime <= 0) {
                toogleChase();
                this.leftChaseTime = this.chaseTime;
            } else {
                this.leftChaseTime--;
                chase();
                takeStep();
            }
        } else if (!ghost.isChase()) {
            scatter();
            if (currentPath != null) {
                takeStep();
            }
        }
    }

    /**
     * Toggles the ghost's chase state.
     * If the ghost is currently in chase mode, it switches to scatter mode, and
     * vice
     * versa.
     */
    private void toogleChase() {
        if (ghost.isChase()) {
            ghost.setChase(false);
        } else {
            ghost.setChase(true);
        }
    }

    /**
     * Makes the ghost scatter to its designated position.
     * This method calculates the path for the ghost to move towards its scatter
     * position.
     */
    private void scatter() {
        int[] startIJ = board.getTileIJ(ghost.getY(), ghost.getX());
        int[] targetIJ = board.getTileIJ(ghost.getScatterY(), ghost.getScatterX());
        if (!Arrays.equals(startIJ, targetIJ)) {
            currentPath = this.pathFinder.findPath(startIJ, targetIJ, board);
        } else {
            currentPath = null;
            toogleChase();
        }
    }

    /**
     * Makes the ghost chase PacMan.
     * This method calculates the path for the ghost to move towards PacMan's
     * position.
     */
    private void chase() {
        int[] startIJ = board.getTileIJ(ghost.getY(), ghost.getX());
        int[] targetIJ = board.getTileIJ(pacMan.getY(), pacMan.getX());
        // if no current path or pacMan has changed tile we generate a new path
        if (!Arrays.equals(targetIJ, lastPacManIJ) || currentPath == null) {
            currentPath = this.pathFinder.findPath(startIJ, targetIJ, board);
            lastPacManIJ = targetIJ.clone();
        }
        // on entering a new tile, we remove it from the path
        else if (board.getTileI(ghost.getY()) == currentPath.get(0)[0] &&
                board.getTileJ(ghost.getX()) == currentPath.get(0)[1]) {
            currentPath.remove(0);
        }
    }

    /**
     * Moves the ghost one step in the direction of the current path.
     * This method checks if the ghost is aligned with the grid and updates its
     * position accordingly.
     */
    private void takeStep() {
        if (!ghost.isAllignedX(board.getTileSize()) || !ghost.isAllignedY(board.getTileSize())) {
            ghost.setDirection(ghost.getDirection());
        } else if (currentPath.get(0)[0] > board.getTileI(ghost.getY())) {
            ghost.setDirection(Direction.DOWN);
        } else if (currentPath.get(0)[0] < board.getTileI(ghost.getY())) {
            ghost.setDirection(Direction.UP);
        } else if (currentPath.get(0)[1] > board.getTileJ(ghost.getX())) {
            ghost.setDirection(Direction.RIGHT);
        } else if (currentPath.get(0)[1] < board.getTileJ(ghost.getX())) {
            ghost.setDirection(Direction.LEFT);
        }
        ghost.setX(ghost.getNextX(ghost.getDirection()));
        ghost.setY(ghost.getNextY(ghost.getDirection()));
    }

    /**
     * Makes the ghost flee from PacMan.
     * This method calculates the path for the ghost to move away from PacMan's
     * position.
     */
    private void flee() {
        int[] startIJ = board.getTileIJ(ghost.getY(), ghost.getX());
        int[] targetIJ = board.getTileIJ(pacMan.getY(), pacMan.getX());
        currentPath = this.fleePathFinder.findPath(startIJ, targetIJ, board);
    }

    /**
     * Gets the ghost object.
     *
     * @return the ghost object
     */
    public Ghost getGhost() {
        return ghost;
    }
}