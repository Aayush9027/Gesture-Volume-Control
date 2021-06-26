# Gesture-Volume-Control🤏👌
A Hand Gesture Volume Control application made using OpenCV &amp; MediaPipe . In this project I have built an OpenCV application in which a user can control his system's (laptop/pc) volume by making some Hand Gestures.

### Tech Stacks:💻
- OpenCV (for image processing and drawing)
- Mediapipe (for Hand Tracking)
- Pycaw (to link up with the system's volume)

## Prerequisites:
- You should install python version 3.7 or more
- Import all modules required for the project using this command
```
pip install <module name>
```

## Features :
* Can change your computer's volume based on your hand activity
* Can track your hand in real-time

### Working :
* This project is a use case of Hand Tracking technology. 
* As soon as the user shows up his hand in the camera the application detects it & draws a bounding box around the hand.
* According to the distance between user's Index finger and Thumb it displays the volume in the volume bar on the screen
* To set the volume as the system's volume user has to bend his pinky finger simultaneously.

  ![volume-control_f](https://user-images.githubusercontent.com/78357575/123513770-9952ee00-d6ac-11eb-9c55-de3e368c2641.png)

## Note :📝 
Feel free to file a new issue with a respective title and description on the **Gesture-Volume-Control**. If you already found a solution to your problem, I would love to review your pull request! 

## Contribution :📲
1. Clone the repository 
```
$git clone https://github.com/Aayush9027/Gesture-Volume-Control.git
```
2. Check the status of your file 
```
$git status
```

3.For using VScode for editing your files 
```
$git code .
```
4. To directly add your files to github
```
$git add .
```
5. After writing your code commit your changes 
```
$git commit -m  <message>
```
6. To pull your code to reposoitory
```
$git push origin master
```
Thats all about installation and version control with **Git**

