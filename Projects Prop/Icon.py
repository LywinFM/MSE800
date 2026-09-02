from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(base_size=1024, bg_color="#4CAF50", text="MyApp", font_path=None, output_dir="icons"):
    """
    Creates a square app icon with text and saves multiple sizes for mobile platforms.
    
    :param base_size: The largest icon size (usually 1024x1024 for iOS).
    :param bg_color: Background color in HEX or RGB tuple.
    :param text: Text/logo to display on the icon.
    :param font_path: Path to a .ttf font file (optional).
    :param output_dir: Directory to save generated icons.
    """
    try:
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Create base image
        img = Image.new("RGBA", (base_size, base_size), bg_color)
        draw = ImageDraw.Draw(img)

        # Load font
        if font_path and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, int(base_size / 5))
        else:
            font = ImageFont.load_default()

        # Calculate text position
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        position = ((base_size - text_width) / 2, (base_size - text_height) / 2)

        # Draw text
        draw.text(position, text, fill="white", font=font)

        # Save multiple sizes for Android/iOS
        sizes = [1024, 512, 256, 192, 144, 96, 72, 48]
        for size in sizes:
            resized = img.resize((size, size), Image.LANCZOS)
            file_path = os.path.join(output_dir, f"icon_{size}x{size}.png")
            resized.save(file_path, format="PNG")
            print(f"Saved: {file_path}")

        print("✅ Icon generation complete!")

    except Exception as e:
        print(f"❌ Error creating icon: {e}")

# Example usage
if __name__ == "__main__":
    create_icon(
        base_size=1024,
        bg_color="#FF5722",
        text="AB",
        font_path=None  # You can specify a .ttf font file path here
    )
