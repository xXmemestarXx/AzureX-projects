package pacman;

import java.util.List;

public class PillController {

    private final List<Pill> pills;
    private final PacMan pacMan;
    private final ICollisionChecker<Pill, PacMan> pillCollisionChecker;

    /**
     * Constructor for PillController.
     *
     * @param pills  the list of pills in the game
     * @param pacMan the PacMan entity
     */
    PillController(List<Pill> pills, PacMan pacMan) {
        this.pills = pills;
        this.pacMan = pacMan;
        this.pillCollisionChecker = new PillCollisionChecker(pills);
    }

    /**
     * Checks if PacMan has collided with any pill.
     *
     * @return true if PacMan has collided with a pill, false otherwise
     */
    public void eat() {
        for (int i = 0; i < pills.size(); i++) {
            Pill pill = pills.get(i);
            if (pillCollisionChecker.AABBcollision(pill, pacMan)) {
                pill.setEaten(true);
            }
        }
    }

    /**
     * Resets the state of all pills to not eaten.
     */
    public void resetPills() {
        for (int i = 0; i < pills.size(); i++) {
            pills.get(i).setEaten(false);
        }
    }
}