package pacman;

import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.Node;
import javafx.scene.paint.Color;

public class PacManView extends MovableView<PacMan> {

    private String[] imagePaths = { "/pacman.png", "/pacman1.png", "/pacman2.png" };
    private Image[] images = new Image[imagePaths.length];

    private int fpscount = 0;
    private ImageView imageView;

    /**
     * Constructor for PacManView.
     *
     * @param pacMan the PacMan entity to be represented
     * @param color  the color of the PacMan (not used in this implementation)
     * @param scale  the scale factor for the size of the image
     */
    PacManView(PacMan pacMan, Color color, int scale) {
        super(pacMan);

        // Load images correctly from resources using getResource()
        for (int i = 0; i < imagePaths.length; i++) {
            var url = getClass().getResource(imagePaths[i]);
            images[i] = new Image(url.toExternalForm(), true); // true enables background loading
        }

        imageView = new ImageView(images[0]);
        imageView.setFitWidth(this.getEntity().getWidth() * scale);
        imageView.setFitHeight(this.getEntity().getHeight() * scale);
    }

    /**
     * Updates the position and size of the PacMan image based on the current
     * entity's coordinates and the given scale. Additionally, updates the image
     * frame to create an animation effect by cycling through the available images
     * every 10 frames.
     *
     * @param scale the scale factor to adjust the position and size of the image
     */
    @Override
    public void updatePosition(int scale) {
        imageView.setTranslateX(this.getEntity().getX() * scale);
        imageView.setTranslateY(this.getEntity().getY() * scale);
        imageView.setFitWidth(this.getEntity().getWidth() * scale);
        imageView.setFitHeight(this.getEntity().getHeight() * scale);

        fpscount++;
        if (fpscount % 10 == 0) {
            int frameIndex = (fpscount / 10) % images.length;
            imageView.setImage(images[frameIndex]);
        }
    }

    /**
     * Updates the view of the PacMan entity by adjusting its position, size,
     * and orientation based on the current state of the entity and the given scale.
     * This method ensures that the PacMan image is correctly positioned and rotated
     * to match its direction of movement.
     *
     * @param scale the scale factor to adjust the position, size, and rotation of
     *              the image
     */
    @Override
    public void updateView(int scale) {
        updatePosition(scale);
        updateImageDirection(this.getEntity().getDirection());
    }

    /**
     * Rotates the PacMan image to face the specified direction.
     *
     * @param dir the direction to rotate the PacMan image to
     */
    public void rotateToDirection(Direction dir) {
        double angle = 0;
        switch (dir) {
            case UP:
                angle = 270;
                break;
            case DOWN:
                angle = 90;
                break;
            case LEFT:
                angle = 180;
                break;
            case RIGHT:
                angle = 0;
                break;
        }
        imageView.setRotate(angle);
    }

    /**
     * Updates the image direction based on the new direction provided.
     * This method sets the rotation of the image view to match the specified
     * direction.
     *
     * @param newDirection the new direction to set for the PacMan image
     */
    protected void updateImageDirection(Direction newDirection) {
        int angle = 0;
        switch (newDirection) {
            case UP:
                angle = 270;
                break; // because image default faces right
            case DOWN:
                angle = 90;
                break;
            case LEFT:
                angle = 180;
                break;
            case RIGHT:
                angle = 0;
                break;
        }
        imageView.setRotate(angle);
    }

    /**
     * Returns the Node representing the PacMan entity in the view.
     *
     * @return the ImageView associated with this PacMan entity
     */
    @Override
    public Node getNode() {
        return imageView;
    }

}
