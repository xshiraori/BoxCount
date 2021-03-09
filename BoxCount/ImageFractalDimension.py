import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageFractalDimension:
    def __init__(self, image_name, SIZE):
        self.SIZE = SIZE
        image = Image.open(image_name)
    
        assert image.size[0] == image.size[1] and image.size[0] == self.SIZE, "Height and Width of the image must be equal."

        image = np.asarray(image)
        self.img_px_array = np.copy(image)

        self.convertImg()
        self.fractal_dim = self.calculate_fractal_dim()

    def convertImg(self):
        for i in range(len(self.img_px_array)):
            for j in range(len(self.img_px_array[i])):
                for k in range(len(self.img_px_array[i][j])):
                    if(self.img_px_array[i][j][k] == 255):
                        self.img_px_array[i][j][k] = 0
                    else:
                        self.img_px_array[i][j][k] = 1

    def calculate_fractal_dim(self):
        self.dimensions = []
        self.filled_boxes = []

        self.img_px_array = self.img_px_array[:, :, 0]

        size = 1
        while size != self.SIZE:
            size *= 2
            filled_box = self.boxcount(size)
            self.filled_boxes.append(filled_box)
            self.dimensions.append(size / self.SIZE)

        return -np.polyfit(np.log(self.dimensions), np.log(self.filled_boxes), 1)[0]

    def blockshaped(self, square_size):
        h, w = self.img_px_array.shape
        assert h % square_size == 0, "Array is not evenly divisible".format(h, square_size)
        return (self.img_px_array.reshape(h//square_size, square_size, -1, square_size).swapaxes(1,2).reshape(-1, square_size, square_size))

    def boxcount(self, size):
        blocked_arrays = self.blockshaped(size)
        counter = 0

        for i in range(len(blocked_arrays)):
            for j in range(len(blocked_arrays[i])):
                if(blocked_arrays[i][j].any()):
                    counter +=1
                    break
        return counter

    def graph(self):
        plt.plot(-np.log(self.dimensions), np.log(self.filled_boxes))
        plt.title("Fractal Dimension : " + str(self.fractal_dim))
        plt.show()
        plt.clf()