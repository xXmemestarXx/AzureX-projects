package pacman;

import java.util.List;

public class WallCollisionChecker implements ICollisionChecker<Wall, PacMan> {
    private final List<Wall> walls;

    /**
     * Constructor for WallCollisionChecker.
     *
     * @param walls the list of walls to check for collisions
     */
    WallCollisionChecker(List<Wall> walls) {
        this.walls = walls;
    }

    /**
     * Checks if there is a collision between the PacMan and any of the walls.
     *
     * @param pacMan the PacMan entity to check for collisions
     * @return true if there is a collision with any wall, false otherwise
     */
    @Override
    public boolean hasCollision(PacMan pacMan) {
        for (int i = 0; i < this.walls.size(); i++) {
            if (AABBcollision(this.walls.get(i), pacMan)) {
                return true;
            }
        }
        return false;
    }

}
