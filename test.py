import tensorflow as tf

# List physical devices
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("GPUs detected:", gpus)
else:
    print("No GPU detected.")
