package pacman;

public class PacManCollisionChecker implements ICollisionChecker<PacMan, Ghost> {

    private final PacMan pacMan;

    /**
     * Constructor for PacManCollisionChecker.
     *
     * @param pacMan the PacMan instance to check for collisions
     */
    PacManCollisionChecker(PacMan pacMan) {
        this.pacMan = pacMan;
    }

    /**
     * Checks if the PacMan collides with a ghost.
     *
     * @param ghost the ghost to check for collision with PacMan
     * @return true if there is a collision, false otherwise
     */
    @Override
    public boolean hasCollision(Ghost ghost) {
        return AABBcollision(this.pacMan, ghost);
    }
}
