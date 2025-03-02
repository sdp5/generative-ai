## Project: AI Photo Editing with Inpainting

In this project we are going to build a little app that allows you to select a subject and then change its background, OR keep the background and change the subject.

The process involves a user uploading an image and selecting the main object by clicking on it. The Segment Anything Model (SAM) is activated to create a mask around the selected object, choosing the most accurate mask generated. The user is shown this result to either accept it or refine the mask further with additional points. Once the mask is finalized, the user gives a text description (and possibly a negative prompt) to specify a new background for the selected object. An infill model then creates this new background, and the final image is displayed. Optionally, the user can choose to invert the mask and substitute the subject while keeping the background, as in the example above.

This little app can be used to swap backgrounds, swap subjects, remove objects, and more!

You will be writing the code that powers the main functionality of the app: calling the SAM model and processing its output, as well as using a text2image diffusion model to generate the new background or subject.


### Project Structure

```bash
.
├── app.py      
├── car.png
├── dragon.jpeg
├── monalisa.png
├── output          # Results by taking screenshots 
│   ├── inpainted-image-1.png
│   ├── inpainted-image-2.png
│   ├── inpainted-image-3.png
│   ├── inpainted-image-4.png
│   └── inpainted-image-5.png
├── README.md
├── starter.ipynb   # Project Work
└── starter.py
```
