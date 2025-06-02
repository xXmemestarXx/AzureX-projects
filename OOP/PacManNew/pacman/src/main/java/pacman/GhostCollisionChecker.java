package pacman;

import java.util.List;

public class GhostCollisionChecker implements ICollisionChecker<Ghost, PacMan> {
    private final List<Ghost> ghosts;

    GhostCollisionChecker(List<Ghost> ghosts) {
        this.ghosts = ghosts;
    }

    /**
     * Checks if there is a collision between any ghost and the PacMan.
     *
     * @param pacMan the PacMan object to check for collisions with ghosts
     * @return true if there is a collision, false otherwise
     */
    @Override
    public boolean hasCollision(PacMan pacMan) {
        for (int i = 0; i < this.ghosts.size(); i++) {
            if (AABBcollision(this.ghosts.get(i), pacMan)) {
                return true;
            }
        }
        return false;
    }
}
