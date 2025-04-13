"""
"""
import matplotlib.pyplot as plt
import torch.nn as nn
import torch.optim as optimizer

from loguru import logger

from transformer import ParticleTransformer
from data_processing import training_set_final_tensor, training_set_23_tensor
from data_processing import validation_set_final_tensor, validation_set_23_tensor
from data_processing import test_set_final_tensor, test_set_23_tensor

def plot_losses(train_loss, val_loss):
    """
    """
    plt.figure()
    plt.plot(train_loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Learning curve')
    plt.legend()
    plt.grid(True)
    plt.show()

transformer = ParticleTransformer(
    input_train = training_set_23_tensor,
    input_val = validation_set_23_tensor,
    input_test = test_set_23_tensor,
    target_train = training_set_final_tensor,
    target_val = validation_set_final_tensor,
    target_test = test_set_final_tensor,
    dim_features = training_set_23_tensor.shape[2],
    num_heads = 8,
    num_encoder_layers = 2,
    num_decoder_layers = 2,
    num_units = 16,
    dropout = 0.1,
    batch_size = 8,
    activation = nn.ReLU()
)

epochs = 100
loss_func = nn.MSELoss()
learning_rate = 1e-3
logger.info(
    f"Batch size: {transformer.batch_size}, Epochs: {epochs}, "
    f"Learning rate: {learning_rate}, loss function: {loss_func}."
)

train_loss, val_loss = transformer.train_val(
    num_epochs = epochs,
    loss_func = loss_func,
    optim = optimizer.Adam(transformer.parameters(), lr=learning_rate)
)

plot_losses(train_loss, val_loss)