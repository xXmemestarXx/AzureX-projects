package pacman;

import javafx.scene.Node;

public abstract class MovableView<E extends Movable> extends EntityView<E> {

    /**
     * Constructor for MovableView.
     *
     * @param entity the movable entity to be represented
     */
    public MovableView(E entity) {
        super(entity);
    }

    /**
     * Returns the Node representing the movable entity in the view.
     *
     * @return the Node associated with this movable entity
     */
    public abstract Node getNode();

    /**
     * Updates the position of the movable entity based on the current scale.
     *
     * @param scale the scale factor to adjust the position
     */
    public abstract void updatePosition(int scale);

    /**
     * Updates the visual representation of the movable entity based on its current
     * state.
     *
     * @param scale the scale factor used to adjust the size and position of the
     *              movable entity's image
     */
    public abstract void updateView(int scale);
}