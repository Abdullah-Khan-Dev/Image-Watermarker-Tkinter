<h1>Watermark Application</h1>
This Python application provides a simple graphical user interface (GUI) for adding watermarks to images. Developed using Tkinter for the GUI and Pillow (PIL) for image processing, this tool allows users to upload an image, enter watermark text, and save the watermarked image.

<h3>Features</h3>
<b>Upload Image:</b> Select and upload images in JPG, JPEG, or PNG formats.<br>
<b>Add Watermark:</b> Input custom text to be used as a watermark and position it on the image.<br>
<b>Save Image:</b> Save the watermarked image in PNG or JPEG format.<br>
<h3>Prerequisites</h3>
Python 3.x<br>
Pillow library (pip install pillow)<br>
Tkinter library (included with Python standard library)<br>
<h3>Installation</h3>
<b>Clone the Repository:</b>

sh<br>
Copy code<br>
git clone https://github.com/yourusername/watermark-application.git<br>
cd watermark-application<br>
<h3>Install Dependencies:</h3>

sh<br>
Copy code<br>
pip install pillow<br>
Usage<br>
<b>Run the Application:</b><br>
sh<br>
Copy code<br>
python watermark_app.py<br>
<h3>Interact with the GUI:</h3>

Click "Upload Image" to select an image file.
Enter the desired watermark text in the provided text field.
Click "Add Watermark" to apply the watermark and save the modified image.
Code Overview
upload_image(): Handles image file selection and displays it on the GUI.
add_watermark(): Adds the specified text as a watermark to the uploaded image and saves it.
Contributing
Feel free to contribute by submitting pull requests or opening issues for bugs and feature requests.

<h3>License</h3>
This project is licensed under the MIT License - see the LICENSE file for details.