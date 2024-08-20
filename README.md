# Extracting EXIF Metadata from Images

This Python script is designed to extract EXIF metadata from an image. EXIF data can provide additional information about an image, such as camera settings and more, which can be useful for investigations and OSINT (Open Source Intelligence) activities.

## Features

- **Extract EXIF Metadata**: Retrieves and displays the EXIF metadata from an image file.
- **OSINT and CTF**: Useful for OSINT (Open Source Intelligence) tasks and Capture The Flag (CTF) challenges.

## Libraries Used

- **[Pillow (PIL Fork)](https://pillow.readthedocs.io/en/stable/)**: A Python library for image processing, used to open images and access their metadata.
- **[PIL.ExifTags](https://pillow.readthedocs.io/en/stable/releasenotes/4.0.0.html#ExifTags)**: Provides mapping of EXIF tags to human-readable names.

## Prerequisites

- **Python 3.x**: Ensure that Python 3.x is installed on your system.
- **Pillow**: Install this library via pip if it is not already installed.

  ```bash
  pip install pillow
  ```

## Usage

1. **Save the script** to a file, e.g., `recup_exif.py`.

2. **Run the script** from the command line by providing the path to the image from which you want to extract EXIF data. Use the following command:

   ```bash
   python3 recup_exif.py
   ```

   The script will prompt you to enter the path to the image file.

3. **Enter the image path** when prompted, and the script will display the extracted EXIF metadata.

## Code Explanation

The script utilizes two main components: `Pillow` for image processing and `ExifTags` for mapping EXIF tags to human-readable names.

- **`Image` from Pillow**: Used to open the image file and access its EXIF metadata.
- **`ExifTags`**: Provides a mapping from EXIF tag IDs to their human-readable names.

The `extract_exif` function performs the following tasks:
- Opens the image and retrieves the EXIF metadata.
- If no EXIF data is found, it returns a message indicating so.
- If EXIF data is found, it converts the tags to readable names and stores them in a dictionary.
- Returns the dictionary of EXIF metadata.

The script then prompts the user to enter the path to an image, extracts the EXIF information using the `extract_exif` function, and prints the results.

## Example Usage

To use the script, open your terminal and execute:

```bash
python3 recup_exif.py
```

When prompted, enter the path to the image file. The script will display the extracted EXIF metadata or a message if no EXIF data is found.

## Notes

- **Image Path**: Ensure that you provide the correct path to the image file when prompted.
- **Permissions**: Make sure you have the necessary permissions to read the image file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to modify this README to better fit your needs or add any additional information!
