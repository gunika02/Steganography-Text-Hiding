from PIL import Image

# XOR Encryption
def xor_encrypt_decrypt(text, key='K'):
    key_cycle = (key * ((len(text) // len(key)) + 1))[:len(text)]
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key_cycle))

# Convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Convert binary to text
def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(b, 2)) for b in chars)

# Hide data using LSB
def hide_data(image_path, text, key, output_path):
    encrypted_text = xor_encrypt_decrypt(text, key)
    binary_data = text_to_binary(encrypted_text) + '1111111111111110'  # delimiter

    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())
    new_pixels = []

    data_index = 0
    for pixel in pixels:
        new_pixel = []
        for value in pixel:
            if data_index < len(binary_data):
                new_value = (value & ~1) | int(binary_data[data_index])
                new_pixel.append(new_value)
                data_index += 1
            else:
                new_pixel.append(value)
        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    img.save(output_path)
    print("✅ Data successfully hidden in image:", output_path)


# Extract hidden data from image
def extract_data(image_path, key):
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())

    binary_data = ''
    for pixel in pixels:
        for value in pixel:
            binary_data += str(value & 1)

    # Look for delimiter
    delimiter = '1111111111111110'
    end_index = binary_data.find(delimiter)
    if end_index == -1:
        raise ValueError("❌ No hidden message found.")

    data_bits = binary_data[:end_index]
    encrypted_text = binary_to_text(data_bits)
    decrypted_text = xor_encrypt_decrypt(encrypted_text, key)
    return decrypted_text
