from .image import Image, Color
from .model import Model
from .render import render

def main():
    width = 500
    height = 300
    image = Image(width, height, Color(255, 255, 255, 255))

    # Load the model
    model = Model('data/cow.obj')
    model.normalizeGeometry()

    render(image, model)
    image.saveAsPNG("image.png")

if __name__ == "__main__":
    main()
