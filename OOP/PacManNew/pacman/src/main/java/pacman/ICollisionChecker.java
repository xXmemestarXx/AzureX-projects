package pacman;

public interface ICollisionChecker<T extends Entity, U extends Movable> {

    /**
     * Checks if there is a collision between the entity and another movable entity.
     * 
     * @param entity the entity to check for collisions
     * @return true if there is a collision, false otherwise
     */
    public boolean hasCollision(U entity);

    /**
     * Checks if two entities collide using Axis-Aligned Bounding Box (AABB)
     * collision detection.
     * 
     * @param e1 the first entity
     * @param e2 the second entity
     * @return true if the entities collide, false otherwise
     */
    default boolean AABBcollision(T e1, U e2) {
        return e1.getX() < e2.getX() + e2.getWidth() && // e1’s left edge is left of e2’s right edge
                e1.getX() + e1.getWidth() > e2.getX() && // e1’s right edge is right of e2’s left edge
                e1.getY() < e2.getY() + e2.getHeight() && // e1’s top edge is above e2’s bottom edge
                e1.getY() + e1.getHeight() > e2.getY(); // e1’s bottom edge is below e2’s top edge
    }
}
