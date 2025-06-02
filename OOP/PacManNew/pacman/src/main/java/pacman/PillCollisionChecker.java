package pacman;

import java.util.List;

public class PillCollisionChecker implements ICollisionChecker<Pill, PacMan> {

    private final List<Pill> pills;

    /**
     * Constructor for PillCollisionChecker.
     *
     * @param pills the list of pills to check for collisions
     */
    PillCollisionChecker(List<Pill> pills) {
        this.pills = pills;
    }

    /**
     * Checks if there is a collision between the PacMan and any of the pills.
     *
     * @param pacMan the PacMan entity to check for collisions
     * @return true if there is a collision with any pill, false otherwise
     */
    @Override
    public boolean hasCollision(PacMan pacMan) {
        boolean foundCollision = false;
        for (int i = 0; i < this.pills.size(); i++) {
            if (AABBcollision(this.pills.get(i), pacMan)) {
                foundCollision = true;
            }
        }
        return foundCollision;
    }
}
