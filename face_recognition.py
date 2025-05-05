import os
import glob
from PIL import Image

def convert_images(input_dir, output_dir):
    """Convert all images to standard PNG format"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    images = [
        f for f in glob.glob(os.path.join(input_dir, "*.*"))
        if f.lower().endswith(supported_extensions)
    ]
    
    print(f"Found {len(images)} images to convert")
    
    for img_path in images:
        try:
            # Get basename without extension
            basename = os.path.basename(img_path)
            name = os.path.splitext(basename)[0]
            output_path = os.path.join(output_dir, f"{name}.png")
            
            # Open, convert and save as PNG
            img = Image.open(img_path).convert('RGB')
            img.save(output_path, format='PNG')
            print(f"Converted {basename} to PNG")
            
        except Exception as e:
            print(f"Failed to convert {img_path}: {str(e)}")
    
    print(f"Conversion complete. {len(os.listdir(output_dir))} images saved to {output_dir}")
    return output_dir

if __name__ == "__main__":
    input_dir = "C:/Users/rafig/Documents/PYOpenCV/sigma"
    output_dir = "C:/Users/rafig/Documents/PYOpenCV/sigma_png"
    convert_images(input_dir, output_dir)