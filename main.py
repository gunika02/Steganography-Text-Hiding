from stego_utils import hide_data, extract_data

def main():
    choice = input("🔘 Do you want to (1) Hide or (2) Extract? Enter 1 or 2: ")

    if choice == '1':
        image_path = input("📷 Enter input image path (e.g., example_input.png): ")
        text = input("✉️ Enter the message to hide: ")
        key = input("🔑 Enter encryption key: ")
        output_path = input("💾 Enter output image name (e.g., encoded_image.png): ")
        hide_data(image_path, text, key, output_path)

    elif choice == '2':
        image_path = input("📷 Enter image path to extract from: ")
        key = input("🔑 Enter the decryption key: ")
        try:
            message = extract_data(image_path, key)
            print("\n✅ Hidden Message:")
            print("💬", message)
        except ValueError as e:
            print(e)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
