from PIL import Image

# Load the image
image = Image.open("/home/anon/Documents/Python Code/Todo_List/check.png")

# Define the maximum width and height
max_size = (400, 70)

# Get the size of the original image
width, height = image.size

# Check if the image needs to be resized
if width > max_size[0] or height > max_size[1]:
    # Calculate the new size with the same aspect ratio
    ratio = min(max_size[0] / width, max_size[1] / height)
    new_size = (int(width * ratio), int(height * ratio))

    # Resize the image
    image = image.resize(new_size)

# Save the resized image
image.save("/home/anon/Documents/Python Code/Todo_List/pic.png")
