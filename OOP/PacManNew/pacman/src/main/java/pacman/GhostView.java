package pacman;

import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.Node;

public class GhostView extends MovableView<Ghost> {

    private final String[] redSprite = { "/redghost.png" };

    private final String[] blueSprite = { "/blueghost.png" };

    private final String[] orangeSprite = { "/orangeghost.png" };

    private final String[] pinkSprite = { "/pinkghost.png" };

    private final String[] fleeSprite = { "/fleeghost.png" };

    private final ImageView imageView;

    private final String name;

    /**
     * Constructor for GhostView.
     *
     * @param ghost the ghost entity to be represented
     * @param scale the scale factor for the size of the image
     * @param name  the name of the ghost (e.g., "Blinky", "Pinky", "Clyde", "Nick")
     */
    GhostView(Ghost ghost, int scale, String name) {
        super(ghost);

        this.name = name;
        this.imageView = new ImageView();

        // Set sprite list based on ghost name
        String[] spritePaths;

        switch (name.toLowerCase()) {
            case "blinky":
                spritePaths = redSprite;
                break;
            case "pinky":
                spritePaths = pinkSprite;
                break;
            case "claude":
                spritePaths = orangeSprite;
                break;
            case "nick":
                spritePaths = blueSprite;
                break;
            default:
                spritePaths = redSprite; // fallback
                break;
        }

        Image image = new Image(getClass().getResourceAsStream(spritePaths[0]));
        imageView.setImage(image);
        imageView.setFitWidth(this.getEntity().getWidth() * scale);
        imageView.setFitHeight(this.getEntity().getHeight() * scale);
    }

    /**
     * Sets the flee image for the ghost.
     *
     * @param scale the scale factor for the size of the image
     */
    public void setFleeImage(int scale) {
        Image image = new Image(getClass().getResourceAsStream(fleeSprite[0]));
        imageView.setImage(image);
        imageView.setFitWidth(this.getEntity().getWidth() * scale);
        imageView.setFitHeight(this.getEntity().getHeight() * scale);
    }

    /**
     * Sets the normal image for the ghost based on its name.
     *
     * @param name  the name of the ghost (e.g., "Blinky", "Pinky", "Clyde", "Nick")
     * @param scale the scale factor for the size of the image
     */
    public void setNormalImage(String name, int scale) {
        String[] spritePaths;

        switch (name.toLowerCase()) {
            case "blinky":
                spritePaths = redSprite;
                break;
            case "pinky":
                spritePaths = pinkSprite;
                break;
            case "clyde":
                spritePaths = orangeSprite;
                break;
            case "nick":
                spritePaths = blueSprite;
                break;
            default:
                spritePaths = redSprite; // fallback
                break;
        }

        Image image = new Image(getClass().getResourceAsStream(spritePaths[0]));
        imageView.setImage(image);
        imageView.setFitWidth(this.getEntity().getWidth() * scale);
        imageView.setFitHeight(this.getEntity().getHeight() * scale);
    }

    /**
     * Updates the position of the ghost in the view based on its current
     * coordinates.
     *
     * @param scale the scale factor for the size of the image
     */
    @Override
    public void updatePosition(int scale) {
        imageView.setTranslateX(this.getEntity().getX() * scale);
        imageView.setTranslateY(this.getEntity().getY() * scale);
        imageView.setFitWidth(this.getEntity().getWidth() * scale);
        imageView.setFitHeight(this.getEntity().getHeight() * scale);
    }

    /**
     * Updates the visual representation of the ghost entity based on its current
     * state.
     * Adjusts the position and sets the appropriate image depending on whether the
     * ghost
     * is vulnerable or not.
     *
     * @param scale The scaling factor used to adjust the size and position of the
     *              ghost's image.
     */
    @Override
    public void updateView(int scale) {
        updatePosition(scale);
        if (!this.getEntity().isVulnerable()) {
            setNormalImage(name, scale);
        } else {
            setFleeImage(scale);
        }
    }

    /**
     * Returns the name of the ghost.
     *
     * @return the name of the ghost
     */
    public String getName() {
        return name;
    }

    /**
     * Returns the Node representing the ghost in the view.
     *
     * @return the Node associated with this ghost
     */
    @Override
    public Node getNode() {
        return imageView;
    }
}
