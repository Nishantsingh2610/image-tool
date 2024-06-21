from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """
    Encrypt the image by adding the key to each pixel value.
    :param input_path: Path to the input image
    :param output_path: Path to save the encrypted image
    :param key: Encryption key (integer)
    """
    # Open the image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Encrypt by adding the key value
    encrypted_array = (img_array + key) % 100

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)

def decrypt_image(input_path, output_path, key):
    """
    Decrypt the image by subtracting the key from each pixel value.
    :param input_path: Path to the encrypted image
    :param output_path: Path to save the decrypted image
    :param key: Encryption key (integer)
    """
    # Open the image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Decrypt by subtracting the key value
    decrypted_array = (img_array - key) % 255

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)

# Example usage
if __name__ == "__main__":
    key = 123  # Example key for encryption and decryption
    encrypt_image('input_image.png', 'encrypted_image.png', key)
    decrypt_image('encrypted_image.png', 'decrypted_image.png', key)

