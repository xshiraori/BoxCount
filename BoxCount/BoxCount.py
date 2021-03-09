from ImageFractalDimension import ImageFractalDimension

def main():
    sierpinski = ImageFractalDimension('sierpinski_512x512.png', 512)
    print(sierpinski.fractal_dim)
    sierpinski.graph()

if __name__ == '__main__':
    main()