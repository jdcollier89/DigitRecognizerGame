# DigitRecognizerGame

Using the PyGame module, this application allows the user to draw a numeric figure and then attempt to predict what the number drawn by the user was. This is achieved by using a Convolusional Neural Network on the back-end, that has been trained with the MNIST dataset.

![Alt text](/images/screenshot.PNG?raw=true "Screenshot of application")

The user interface has a 28 x 28 grid which acts as the canvas for drawing. If 'Draw' is selected, the grid can be drawn on by holding the mouse down and moving the mouse cursor. Any mistakes can be undone by selecting the 'Erase' button which will change the cursor mode to change each grid cell to the background color.

If desired, the grid lines can be turned off by clicking the 'Toggle Grid: ON' button.

As of Version 1.0, the accuracy of the predictive model is not as good as it could be. Future versions will focus on improving the model performance.

