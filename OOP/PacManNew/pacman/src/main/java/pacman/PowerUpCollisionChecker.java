package pacman;

import java.util.List;

public class PowerUpCollisionChecker implements ICollisionChecker<PowerUp, PacMan> {

    private final List<PowerUp> powerUps;

    /**
     * Constructor for PowerUpCollisionChecker.
     *
     * @param powerUps the list of power-ups to check for collisions
     */
    PowerUpCollisionChecker(List<PowerUp> powerUps) {
        this.powerUps = powerUps;
    }

    /**
     * Checks if there is a collision between the PacMan and any of the power-ups.
     *
     * @param pacMan the PacMan entity to check for collisions
     * @return true if there is a collision with any power-up, false otherwise
     */
    @Override
    public boolean hasCollision(PacMan pacMan) {
        boolean foundCollision = false;
        for (int i = 0; i < this.powerUps.size(); i++) {
            if (AABBcollision(this.powerUps.get(i), pacMan)) {
                foundCollision = true;
            }
        }
        return foundCollision;
    }
}