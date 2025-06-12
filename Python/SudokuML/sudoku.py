import cv2
import numpy as np
import tensorflow as tf
import os
import sys

# Constants
CELL_SIZE = 28
GRID_CELLS = 9
GRID_SIZE = CELL_SIZE * GRID_CELLS  # 252
DEBUG_DIR = "debug"

# Ensure debug folder exists
os.makedirs(DEBUG_DIR, exist_ok=True)

# Load your trained CNN model
model = tf.keras.models.load_model("digit_model.keras")

def save_debug(name, img):
    path = os.path.join(DEBUG_DIR, name)
    cv2.imwrite(path, img)
    print(f"[DEBUG] Saved {name}")

def preprocess_image(path):
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(gray, (5,5), 0)
    thresh = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )
    save_debug("01_thresh.png", thresh)
    return gray, thresh

def find_grid_contour(thresh):
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    if not contours:
        raise RuntimeError("No contours found")
    # pick largest by area
    largest = max(contours, key=cv2.contourArea)
    print(f"[DEBUG] Found {len(contours)} contours, largest area = {cv2.contourArea(largest)}")
    return largest

def approx_quad(contour):
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
    if len(approx) != 4:
        print(f"[WARN] Contour approximated to {len(approx)} points (expected 4)")
    return approx.reshape(4,2).astype(np.float32)

def order_points(pts):
    # pts: (4,2)
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1).squeeze()
    return np.array([
        pts[np.argmin(s)],   # tl
        pts[np.argmin(diff)],# tr
        pts[np.argmax(s)],   # br
        pts[np.argmax(diff)] # bl
    ], dtype=np.float32)

def warp_to_square(gray, pts):
    rect = order_points(pts)
    dst = np.array([[0,0], [GRID_SIZE-1,0], [GRID_SIZE-1,GRID_SIZE-1], [0,GRID_SIZE-1]], dtype=np.float32)
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(gray, M, (GRID_SIZE, GRID_SIZE))
    save_debug("02_warp.png", warped)
    return warped

def split_cells(warped):
    cells = []
    step = GRID_SIZE // GRID_CELLS  # exactly CELL_SIZE
    for i in range(GRID_CELLS):
        for j in range(GRID_CELLS):
            y0, y1 = i*step, (i+1)*step
            x0, x1 = j*step, (j+1)*step
            cell = warped[y0:y1, x0:x1]
            # (optional) save a few sample cells for visual debug
            if (i,j) in [(0,0),(4,4),(8,8)]:
                save_debug(f"03_cell_{i}_{j}.png", cell)
            cells.append(cell)
    return cells

def prepare_cell(cell):
    # crop a small margin to avoid grid lines
    h,w = cell.shape
    m = int(min(h,w) * 0.1)
    cropped = cell[m:h-m, m:w-m]
    _, thr = cv2.threshold(cropped, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # check if mostly empty
    white_ratio = np.count_nonzero(thr) / thr.size
    is_empty = white_ratio < 0.02
    # resize back to CELL_SIZE
    resized = cv2.resize(thr, (CELL_SIZE, CELL_SIZE), interpolation=cv2.INTER_AREA)
    return resized.astype(np.float32)/255.0, is_empty

def predict_cell(cell):
    img, empty = prepare_cell(cell)
    if empty:
        return 0
    x = img.reshape(1, CELL_SIZE, CELL_SIZE, 1)
    pred = model.predict(x, verbose=0)
    return int(pred.argmax())

def extract_sudoku(path):
    gray, thresh = preprocess_image(path)
    contour = find_grid_contour(thresh)
    quad = approx_quad(contour)
    warped = warp_to_square(gray, quad)
    cells = split_cells(warped)

    grid = np.zeros((GRID_CELLS, GRID_CELLS), dtype=int)
    for idx, cell in enumerate(cells):
        i, j = divmod(idx, GRID_CELLS)
        digit = predict_cell(cell)
        print(f"[DEBUG] Cell ({i},{j}) → {digit}")
        grid[i,j] = digit
    return grid

if __name__ == "__main__":
    sudoku_image_path = "suduko-test.png"
    sudoku_matrix = extract_sudoku(sudoku_image_path)
    print("\nExtracted Sudoku matrix:")
    print(sudoku_matrix)
