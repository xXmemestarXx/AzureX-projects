package pacman;

import javafx.scene.Node;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class ConsumableView<E extends Consumable> extends EntityView<E> {
    private final Color color;
    private final Rectangle node;

    /**
     * Constructor for ConsumableView.
     *
     * @param entity the consumable entity to be represented
     * @param color  the color of the consumable
     * @param scale  the scale factor for the size of the rectangle
     */
    ConsumableView(E entity, Color color, int scale) {
        super(entity);
        this.color = color;
        // Build a rectangle
        this.node = new Rectangle(
                entity.getWidth() * scale,
                entity.getHeight() * scale,
                color);
        // Position the rectangle
        node.setLayoutX(entity.getX() * scale);
        node.setLayoutY(entity.getY() * scale);
    }

    /**
     * Constructor for ConsumableView with default color.
     *
     * @param entity the consumable entity to be represented
     * @param scale  the scale factor for the size of the rectangle
     */
    @Override
    public void updateView(int scale) {
        if (this.getEntity().isEaten()) {
            node.setFill(Color.BLACK);
        } else {
            node.setFill(color);
        }
    }

    /**
     * Returns the node representing the consumable.
     *
     * @return the rectangle node of the consumable
     */
    @Override
    public Node getNode() {
        return node;
    }
}