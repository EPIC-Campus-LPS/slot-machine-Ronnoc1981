# Lab 12: Slot Machine



https://github.com/user-attachments/assets/1eafe7a2-55d5-4bb3-be6e-dd218d0be836



## Objective

1. Create a button activated "slot machine" using Python. 
2. Distinguish between fair and unfair probabilistic systems. 

## Materials 

1. 1 LED 
2. 1 65 Ohm Resistor
3. 7-segment display or LCD Screen(see options below) 
4. 1 button
## Part 1: LED and Button Setup

1. Create a small program to light an LED when the button is pressed. This should be a repeat of previous labs. 

- [ ] There is nothing to submit for this section.

![image001-1](https://github.com/user-attachments/assets/68528cbb-a019-46e5-a512-5c0ea3430cac)

## Part 2: 7 Segment Display

1.  Get a 7-segment display from the class supplies. *The back of these displays can get hot. If it is too hot to handle, then recycle it and get a new display. It may have faulty internal wiring. Be careful when handling.*
2. Install the necessary library with `pip3 install raspberrypi-tm1637`. See [this](https://pypi.org/project/raspberrypi-tm1637/) for library reference. If pip isn't installed, use `sudo apt install pip`. 
![[7SegmentWiring.png]]
3. Use this [site](https://thingsdaq.org/2022/10/02/7-segment-led-display-with-raspberry-pi/) as a reference to wire your display and for the code. **WARNING: Please wire your display CAREFULLY. If you switch your voltage and ground pins when setting up your display, it will get extremely hot very quickly and begin to burn.**
4. Create a program with the following game loop: When the button is pressed, your program will select 4 random numbers and display them on the screen. If all 4 numbers match, the light will flash for 10 seconds.
5. Take a quick video of your program and upload it to GitHub

- [ ] Upload a video of your working program to GitHub

## Part 2: Hardcore - LCD Display 

1. Instead of a 7 segment display, use a 16x2 I2C LCD screen. There are many different libraries you can use for this. I have used [rpi-lcd](https://github.com/bogdal/rpi-lcd) in the past, but you can use whatever works for you. Remember to enable I2C in the raspi-config menu before starting or your program will not run regardless.
2. Create a program with the following game loop: When the button is pressed, your program will select 4 random characters and display them on the screen. If all 4 characters match, the light will flash for 10 seconds.
3. Take a quick video of your program and upload it to GitHub

- [ ] Upload a video of your working program to GitHub


 ![image009-1](https://github.com/user-attachments/assets/c5a60d73-8f4a-4230-b61e-b867d6e72848)

## Part 3: Rig The Game

1. Using a mechanisms of your choice, create a game mode where the results are rigged in favor of winning. This could be triggered by a second button, a double click, a key on the keyboard, it's up to you! The only requirement is that there is an above average chance of winning. 

- [ ] Upload your program and a video to GitHub

## Deliverables

- Uploaded both videos and your final program to GitHub
- Answers to the following questions 
	- How does your program detect a button press and trigger the game loop?
	- If I ran the slot machine 1000 times and graphed the results on a number line, would the results look like? What would they look like for your rigged version?
	- How did you use randomness in your program? Was it truly random? How could you test it?
	- How did you guarantee the results would favor winning? How did you change your game logic to accomplish this? 

## Rubric 

- 6 points - All required items are present.    
- 5 points - Task was completed, but supplementary materials are weak or missing.    
    - Code is complete, but poorly communicates necessary information
- 4 points - Task was attempted, but is missing major components.    
    - Missing comments, videos/photos, or reflection questions  
- 3 points - Did not attempt or student should reattempt.  
    - Inappropriate use of AI tools.

