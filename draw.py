import numpy as np
import matplotlib.pyplot as plt
global m
def plot_chessboard(ax, queens, m):
    board = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                ax.fill([i, i + 1, i + 1, i], [j, j, j + 1, j + 1], 'lightgrey')
    for n in range(8):
        ax.text(n + 0.5, queens[m][n] + 0.5, '♛', ha='center', va='center', fontsize=15, color='black')
    ax.text(-0.2, 8, f'{m+1}', ha='center', va='center', fontsize=12, color='black')
def draw(Q, k, index):
    fig, axes = plt.subplots(3, 5, figsize=(20, 12))
    m = 15 * k
    for i in range(3):
        for j in range(5):
            ax = axes[i, j]
            if m < index:
                ax.set_xticks([])
                ax.set_yticks([])
                plot_chessboard(ax, Q, m)
                ax.set_aspect('equal', adjustable='box')
                ax.axis('on')
            else:
                ax.set_xticks([])
                ax.set_yticks([])
                ax.axis('off')
                continue
            m = m + 1
    plt.tight_layout()
    plt.show()


