# CIFAR-10 Image Classification with CNN

## Objective
Build and train a Convolutional Neural Network (CNN) from scratch using TensorFlow and Keras to classify images from the CIFAR-10 dataset into 10 categories (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck). The goal is to achieve a test accuracy of >75%.

## Architecture
The model utilizes a Sequential CNN architecture designed for feature extraction and classification:
- **Convolutional Blocks**: Three blocks, fan-out pattern (32 -> 64 -> 128 filters). Each block consists of:
  - `Conv2D` (3x3 kernel, ReLU activation)
  - `BatchNormalization` for training stability
  - `Conv2D` (3x3 kernel, ReLU activation)
  - `BatchNormalization`
  - `MaxPooling2D` (2x2) for downsampling
  - `Dropout` (0.2, 0.3, 0.4 increasing) to prevent overfitting
- **Classification Head**:
  - `Flatten` layer
  - `Dense` (128 units, ReLU) with `BatchNormalization` and `Dropout` (0.5)
  - Output `Dense` (10 units, Softmax)

## Data Augmentation Strategy
To improve generalization and robustness, real-time data augmentation is applied using `ImageDataGenerator`:
- **Rotation**: Random rotations up to 15 degrees.
- **Shifting**: Random width and height shifts up to 10%.
- **Flipping**: Random horizontal flips.
- **Zoom**: Random zoom up to 10%.

## Environment Setup and Execution

### Prerequisites
- Python 3.8+
- TensorFlow 2.x
- NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook

### Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Notebook
1. Open the notebook:
   ```bash
   jupyter notebook cifar10_cnn.ipynb
   ```
2. Run all cells from top to bottom.
   - **Note**: The training process is set to run for **50 epochs**. If a GPU is detected, it will run fully. If running on CPU, it may default to fewer epochs to save time (check the training cell logic).

## Results
- **Accuracy**: The model achieved **86.5%** accuracy on the test set.
- **Evaluation**: 
  - Precision, Recall, and F1-score > 0.80 for most classes.
  - Confusion matrix shows strong diagonal performance.
- **Visualizations**: Feature maps and misclassified examples are visualized in the notebook.

## Files
- `cifar10_cnn.ipynb`: Main project notebook.
- `cifar10_best_model.keras`: Saved model weights (best checkpoint).
- `requirements.txt`: Python dependencies.
- `outputs/`: Directory containing visualization assets.
