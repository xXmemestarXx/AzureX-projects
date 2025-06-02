package pacman;

import java.util.List;

public class PowerUpController {
    private final List<PowerUp> powerUps;
    private final PacMan pacMan;
    private final ICollisionChecker<PowerUp, PacMan> powerUpCollisionChecker;

    /**
     * Constructor for PowerUpController.
     *
     * @param powerUps the list of power-ups in the game
     * @param pacMan   the PacMan entity
     */
    PowerUpController(List<PowerUp> powerUps, PacMan pacMan) {
        this.powerUps = powerUps;
        this.pacMan = pacMan;
        this.powerUpCollisionChecker = new PowerUpCollisionChecker(powerUps);
    }

    /**
     * Checks if PacMan has collided with any power-up.
     *
     * @return true if PacMan has collided with a power-up, false otherwise
     */
    public void eat() {
        for (int i = 0; i < powerUps.size(); i++) {
            PowerUp powerUp = powerUps.get(i);
            if (powerUpCollisionChecker.AABBcollision(powerUp, pacMan)) {
                powerUp.setEaten(true);
            }
        }
    }

    /**
     * Resets the state of all power-ups to not eaten.
     */
    public void resetPowerUps() {
        for (int i = 0; i < powerUps.size(); i++) {
            powerUps.get(i).setEaten(false);
        }
    }
}
