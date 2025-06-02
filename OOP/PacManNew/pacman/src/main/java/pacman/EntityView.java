package pacman;

import javafx.scene.Node;

public abstract class EntityView<E extends Entity> {

    private final E entity;

    /**
     * Constructor for EntityView.
     *
     * @param entity the entity to be represented
     */
    EntityView(E entity) {
        this.entity = entity;
    }

    /**
     * Updates the view of the entity based on the current scale.
     *
     * @param scale the scale factor to adjust the view
     */
    public abstract void updateView(int scale);

    /**
     * Returns the Node representing the entity in the view.
     *
     * @return the Node associated with this entity
     */
    public abstract Node getNode();

    /**
     * Returns the entity associated with this view.
     *
     * @return the entity represented by this view
     */
    public E getEntity() {
        return this.entity;
    }
}
