package pacman;

import java.util.ArrayList;
import java.util.List;

import javafx.animation.AnimationTimer;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;

public class GameManager {
    private Board board;
    private GUI gui;

    private PacMan pacMan;
    private PacManController pacManController;
    private PacManInputHandler pacManInputHandler;
    private PacManCollisionChecker pacManCollisionChecker;

    private PillController pillController;
    private PowerUpController powerUpController;

    private List<Ghost> ghosts;
    private List<GhostController> ghostControllers;
    private List<MovableView<Ghost>> ghostViews;
    private GhostCollisionChecker ghostCollisionChecker;

    private int lives;
    private int score;

    private final int scale;

    private Group root;
    private Scene scene;
    private VBox endOverlay;

    private boolean powerStateEnabled;
    private int powerStateCountDown;

    private final AnimationTimer gameLoop;
    private final long NANOS_PER_UPDATE = 16666667; // 60 FPS or 60UPS (Updates Per Second)

    /**
     * Constructor for GameManager.
     *
     * @param scale the scale factor for the game
     * @param root  the root Group for the JavaFX scene
     * @param scene the JavaFX Scene
     */
    GameManager(int scale, Group root, Scene scene) {

        this.scale = scale;
        this.root = root;
        this.scene = scene;

        firstLevel();

        gameLoop = new AnimationTimer() {
            private long lastUpdate = 0;

            @Override
            public void handle(long now) {
                if (lastUpdate == 0) {
                    lastUpdate = now;
                    return;
                }
                if (now - lastUpdate >= NANOS_PER_UPDATE) {
                    updateTick();
                    lastUpdate = now;
                }
            }
        };
    }

    /**
     * Starts the game loop.
     * This method is called to begin the game updates.
     */
    public void startLoop() {
        gameLoop.start();
    }

    /**
     * Stops the game loop.
     * This method is called to pause the game updates.
     */
    private void stopLoop() {
        gameLoop.stop();
    }

    /**
     * Updates the game state on each tick.
     * This method handles ghost collisions, updates ghost controllers,
     * moves PacMan, checks for pill and power-up consumption, and updates the GUI.
     */
    private void updateTick() {
        if (lives > 0) {
            handleGhostCollision();
            for (int i = 0; i < ghostControllers.size(); i++) {
                ghostControllers.get(i).update();
            }
            pacManController.move();

            int oldPills = board.pillsLeft();
            pillController.eat();
            int newPills = board.pillsLeft();
            score += (oldPills - newPills) * Pill.pillValue;

            int oldPowerUps = board.powerUpsLeft();
            powerUpController.eat();
            int newPowerUps = board.powerUpsLeft();

            if (powerStateCountDown > 0) {
                powerStateCountDown--;
            } else {
                disablePowerState();
            }

            if (oldPowerUps > newPowerUps) {
                enablePowerState();
                score += (oldPowerUps - newPowerUps) * PowerUp.powerValue;
            }
            gui.updateAllViews(score, lives);

        } else {
            showGameOverOverlay();
            stopLoop();
        }
        if (board.pillsLeft() <= 0 && board.powerUpsLeft() <= 0) {
            nextLevel();
        }
    }

    /**
     * Handles the collision between PacMan and ghosts.
     * If PacMan collides with a ghost while not in power state, it resets the game.
     * If PacMan is in power state, it eats the ghost and increases the score.
     */
    private void handleGhostCollision() {
        if (ghostCollisionChecker.hasCollision(pacMan) && !powerStateEnabled) {
            for (int i = 0; i < ghostControllers.size(); i++) {
                ghostControllers.get(i).reset();
            }
            pacMan.resetPosition();
            lives--;
        } else if (powerStateEnabled) {
            for (int i = 0; i < ghostControllers.size(); i++) {
                Ghost ghost = ghostControllers.get(i).getGhost();
                if (pacManCollisionChecker.hasCollision(ghost)) {
                    ghostControllers.get(i).reset();
                    score += Ghost.ghostValue;
                    ghost.setVulnerable(false);
                }
            }
        }
    }

    /**
     * Resets the maze to its initial state.
     * This method clears the pills and power-ups, resets PacMan's position,
     * disables the power state, and resets all ghosts.
     */
    private void resetMaze() {
        pillController.resetPills();
        powerUpController.resetPowerUps();
        pacMan.resetPosition();
        disablePowerState();
        for (int i = 0; i < ghostControllers.size(); i++) {
            ghostControllers.get(i).reset();
        }
    }

    /**
     * Resets the game to its initial state.
     * This method removes the end overlay, resets the maze, score, and lives,
     * and restarts the game loop after a brief pause.
     */
    public void resetGame() {
        if (endOverlay != null) {
            root.getChildren().remove(endOverlay);
            endOverlay = null; // clear reference
        }
        resetMaze();
        score = 0;
        lives = 2;
        gui.resetLives(lives);
        gui.updateAllViews(score, lives);
        // 2 second pause before game restarts
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        startLoop();
    }

    /**
     * Displays the game over overlay.
     * This method creates an EndView instance and adds it to the root Group.
     */
    private void showGameOverOverlay() {
        EndView endView = new EndView(this);
        endOverlay = endView.getView(scene.getWidth(), scene.getHeight());
        root.getChildren().add(endOverlay);
    }

    /**
     * Sets up PacMan with its initial position, controller, and view.
     *
     * @param scale the scale factor for the PacMan view
     */
    private void setupPacMan(int scale) {
        WallCollisionChecker wallCollisionChecker = new WallCollisionChecker(board.getWalls());
        pacMan = new PacMan(board.getTileSize(), board.getTileSize(), board.getTiles()[23][13].getX(),
                board.getTiles()[23][13].getY(), 2.5);
        pacManController = new PacManController(pacMan, wallCollisionChecker);
        pacManInputHandler = new PacManInputHandler(pacManController);
        pacManCollisionChecker = new PacManCollisionChecker(pacMan);
        PacManView pacManView = new PacManView(pacMan, Color.YELLOW, scale);
        gui.drawMovable(pacManView);
    }

    /**
     * Sets up the ghosts with their initial positions, controllers, and views.
     *
     * @param scale the scale factor for the ghost views
     */
    private void setupGhosts(int scale) {
        this.ghosts = new ArrayList<>();
        this.ghostControllers = new ArrayList<>();
        this.ghostViews = new ArrayList<>();

        // Blinky
        Ghost blinky = new Ghost(board.getTileSize(), board.getTileSize(), board.getTiles()[14][12].getX(),
                board.getTiles()[14][12].getY(),
                board.getTiles()[1][1].getX(), board.getTiles()[1][1].getY(), 2);
        this.ghosts.add(blinky);
        ghostViews.add(new GhostView(blinky, scale, "blinky"));
        ghostControllers.add(new GhostController(blinky, pacMan, board, 100, 150));

        // Pinky
        Ghost pinky = new Ghost(board.getTileSize(), board.getTileSize(), board.getTiles()[14][13].getX(),
                board.getTiles()[14][13].getY(),
                board.getTiles()[1][26].getX(), board.getTiles()[1][26].getY(), 2);
        this.ghosts.add(pinky);
        ghostViews.add(new GhostView(pinky, scale, "pinky"));
        ghostControllers.add(new GhostController(pinky, pacMan, board, 200, 100));

        // Clyde
        Ghost clyde = new Ghost(board.getTileSize(), board.getTileSize(), board.getTiles()[14][14].getX(),
                board.getTiles()[14][14].getY(),
                board.getTiles()[29][1].getX(), board.getTiles()[29][1].getY(), 2);
        this.ghosts.add(clyde);
        ghostViews.add(new GhostView(clyde, scale, "clyde"));
        ghostControllers.add(new GhostController(clyde, pacMan, board, 300, 200));

        // Nick
        Ghost nick = new Ghost(board.getTileSize(), board.getTileSize(), board.getTiles()[14][15].getX(),
                board.getTiles()[14][15].getY(),
                board.getTiles()[29][26].getX(), board.getTiles()[29][26].getY(), 2);
        this.ghosts.add(nick);
        ghostViews.add(new GhostView(nick, scale, "nick"));
        ghostControllers.add(new GhostController(nick, pacMan, board, 400, 200));

        ghostCollisionChecker = new GhostCollisionChecker(ghosts);

        for (MovableView<Ghost> view : ghostViews) {
            gui.drawMovable(view);
        }
    }

    /**
     * Sets up the pills on the board.
     * This method creates a PillController and draws each pill on the GUI.
     *
     * @param scale the scale factor for the pill views
     */
    private void setupPills(int scale) {
        pillController = new PillController(board.getPills(), pacMan);
        for (int i = 0; i < board.getPills().size(); i++) {
            ConsumableView<Pill> pillView = new ConsumableView<Pill>(board.getPills().get(i), Color.YELLOW, scale);
            gui.drawConsumable(pillView);
        }
    }

    /**
     * Sets up the power-ups on the board.
     * This method creates a PowerUpController and draws each power-up on the GUI.
     *
     * @param scale the scale factor for the power-up views
     */
    private void setupPowerUps(int scale) {
        powerUpController = new PowerUpController(board.getPowerUps(), pacMan);
        for (int i = 0; i < board.getPowerUps().size(); i++) {
            ConsumableView<PowerUp> powerUpView = new ConsumableView<>(board.getPowerUps().get(i), Color.YELLOW, scale);
            gui.drawConsumable(powerUpView);
        }
    }

    /**
     * Initializes the first level of the game.
     * This method sets up the board, GUI, PacMan, ghosts, power-ups, and pills.
     */
    private void firstLevel() {
        this.board = new Board();
        this.gui = new GUI(board, scale);
        this.lives = 2;
        this.powerStateEnabled = false;
        setupPacMan(scale);
        setupGhosts(scale);
        setupPowerUps(scale);
        setupPills(scale);
    }

    /**
     * Initializes the next level of the game.
     * This method resets the maze and prepares for the next level.
     */
    private void nextLevel() {
        resetMaze();
    }

    /**
     * Enables the power state for PacMan.
     * This method sets all ghosts to vulnerable and starts the power state
     * countdown.
     */
    private void enablePowerState() {
        for (int i = 0; i < ghosts.size(); i++) {
            ghosts.get(i).setVulnerable(true);
        }
        powerStateCountDown = 200;
        powerStateEnabled = true;
    }

    /**
     * Disables the power state for PacMan.
     * This method sets all ghosts to not vulnerable.
     */
    private void disablePowerState() {
        for (int i = 0; i < ghosts.size(); i++) {
            ghosts.get(i).setVulnerable(false);
        }
        powerStateEnabled = false;
    }

    /**
     * Returns the current score of the game.
     *
     * @return the current score
     */
    public GUI getGUI() {
        return gui;
    }

    /**
     * Returns the current board of the game.
     *
     * @return the current Board instance
     */
    public PacManInputHandler getPacManInputHandler() {
        return pacManInputHandler;
    }
}
