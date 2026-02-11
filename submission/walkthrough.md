# CIFAR-10 CNN Walkthrough

## Summary
We successfully implemented a Convolutional Neural Network (CNN) to classify CIFAR-10 images using TensorFlow and Keras. The implementation achieved >86% test accuracy, exceeding the 75% goal.

## Key Components

### 1. Data Processing
- **Normalization**: Pixel values scaled to [0, 1].
- **One-hot Encoding**: Labels converted to categorical vectors.
- **Augmentation**: Used `ImageDataGenerator` with rotation, width/height shifts, and horizontal flips.

### 2. Model Architecture
A sequential CNN with:
- 3 Convolutional Blocks (Conv2D -> BatchNormalization -> Conv2D -> BatchNormalization -> MaxPooling2D -> Dropout).
- Fully Connected Layers (Dense -> BatchNormalization -> Dropout -> Dense).
- Total Parameters: ~1.5M.

### 3. Training
- **Epochs**: 50 (with Early Stopping and ReduceLROnPlateau).
- **Optimizer**: Adam.
- **Loss**: Categorical Crossentropy.
- **Result**: Achieved 86.5% accuracy on test set.

## Verification & Fixes
- **Issue**: Attempting to visualize feature maps raised `AttributeError: The layer sequential has never been called` in Keras 3.
- **Fix**: Ensuring the model is built by calling `predict` on a dummy input and accessing `model.inputs` instead of `model.input`.

## Visualizations
The notebook includes:
- Training History (Accuracy/Loss curves).
- Confusion Matrix (Heatmap).
- Misclassified Images.
- Feature Maps (First Conv Layer).

## How to Run
1. Ensure dependencies are installed: `pip install tensorflow matplotlib seaborn scikit-learn notebook`.
2. Open `cifar10_cnn.ipynb`.
3. Run all cells. (If using CPU, epochs will default to 5 unless GPU is detected).
