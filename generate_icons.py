from PIL import Image, ImageDraw

def create_icon(size, path):
    img = Image.new('RGB', (size, size), color = '#6f2c91')
    d = ImageDraw.Draw(img)
    # Draw a simple white checkmark-like shape
    points = [
        (size*0.2, size*0.5), 
        (size*0.4, size*0.7), 
        (size*0.8, size*0.3)
    ]
    d.line(points, fill="white", width=int(size*0.1))
    img.save(path)

if __name__ == "__main__":
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    create_icon(192, os.path.join(base_dir, "app/static/icon-192.png"))
    create_icon(512, os.path.join(base_dir, "app/static/icon-512.png"))
    print("Icons created")
