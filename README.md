## Table of Contents
* [Purpose](#Purpose)
* [User Experience Design](#User-Experience-Design)
    * [User Stories](#User-Stories)
        * [First Time Visitor Goals](#First-Time-Visitor-Goals)
        * [Returning Visitor Goals](#Returning-Visitor-Goals)
    * [Design](#Design)
        * [Color Scheme](#Color-Scheme)
- [Features](#Features)
    * [Existing Features](#Existing-Features)
    * [Features Left To Implement](#Features-Left-To-Implement)
- [Technologies](#Technologies)
- [Testing](#Testing)
    * [Validator Testing](#Validator-Testing)
    * [Issues And Resolutions](#Issues-And-Resolutions)
- [Deployment](#Deployment)
- [Credits](#Credits)

# Milestone Project 3 - GitOut, a choose your own adventure game.
## Purpose
This website was created to complete the third Milestone Project for Code Insitute's Full Stack Software Developer course. I built this from the ground up using knowledge I gained from the previous modules. These being Python and User Centric Design. The full list of technologies used can be found in the technologies section further down.

Users of this website are able to play a short story with multiple branching paths leading to either a win or a loss.

![Website Mock Up](assets/readme/welcome.png)

I highly recommend inspecting this 
[Google Doc](https://docs.google.com/document/d/1ghwcjxg73EdyXoCgmjsem6h2mjyTQ0Chwmcv5w3aVCk/edit?usp=sharing) to see the thought process behind creating this project.

You can find the link to the live website right [here](https://git-out.herokuapp.com/).
Please note: To open any links in this document in a new browser tab, please press CTRL + Click.

***

## User Experience Design

### User Stories
#### First Time Visitor Goals
* As a First Time user, I want to easily understand the main purpose of the site.
* As a First Time user, I want a simple but effective way of making my choices while playing the game.
* As a First Time user, I want to know when my inputs are not incorrect and have another attempt.
#### Frequent Visitor Goals
* As a Frequent user, I want to clearly see how my choices are impacting the outcome of the game.
#### Returning Visitor Goals
* As a Returning user, I want to be able to return to see if I can beat the computer again or for the first time.

## Design
#### Color Scheme
Due to this project being a simple terminal based application there was not a lot that I could do regarding the styling. I did however come across Colorama which allowed me to add some colors to parts of the text. These being Cyan, Red & Green.

![Colors](assets/readme/colors-used.png)

*** 

## Features

### Existing Features
*  #### Title Screen
    * This section is the first thing the user is greeted with when opening the application. 
    * It clearly states the main story of the game.
    * The purpose of this is to fulfill the user story:
    > As a First Time user, I want to easily understand the main purpose of the site.

    ![Title Screen](assets/readme/title-screen.png)
* #### Choice Area
    * This section is where the user will be making their decisions.
    * The section will only accept either Y or N as an input.

    ![Choice Area](assets/readme/choice-1.png)
    * Another example of this can be found further into the game.
    * This section will only accept either 1, 2 or 3 as an input.

    ![Choice Area 2](assets/readme/choice-2.png)
    * The purpose of this is to fulfill the user story:
    > As a First Time user, I want a simple but effective way of making my choices while playing the game.
* #### Error Message
    * This section informs the user that they have used the incorrect input.
    * When this happens the function they made the incorrect input on is started again, letting the user have another attempt.
    * The purpose of this is to fulfill the user story:
    > As a First Time user, I want to know when my inputs are not incorrect and have another chance.
    
    ![Error Message](assets/readme/error.png)
* #### Win/Loss Screen
    * This section makes it evident to the user the outcome of the game.
    * In this instance the user has won and "You Win!" is printed to the terminal in ASCII art format.

    ![You Win](assets/readme/you-win.png)
    * This section makes it evident to the user the outcome of the game.
    * In this instance the user has lost and "You Lose!" is printed to the terminal in ASCII art format.

    ![You Lose](assets/readme/you-lose.png)
    * The purpose of this is to fulfill the user story:
    > As a Frequent user, I want to clearly see how my choices are impacting the outcome of the game.

### Features Left to Implement

***

## Technologies

* [GitHub](https://github.com/)
    * GitHub is the hosting site I used to store the code for the website.
* [GitPod](https://gitpod.io/)
    * GitPod is the Integrated Development Environment used to develop the website in a browser.
* [Stack Overflow](https://stackoverflow.com/)
    * Stack Overflow was one of the websites used for resolving issues with code.
* [W3 Schools](https://www.w3schools.com/)
    * W3 Schools was one of the websites used for resolving issues with code.
* [Patorkj](http://www.patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)
    * This was used to convert text to ASCII art for the title, win and lose screen. 

***

## Testing

## Validator Testing

* Python
    * No errors were returned when passing through the PEP8 Online Validator. 
    ![Validator](assets/readme/validator.png)


## Issues and Resolutions

## Deployment

 This project was deployed using Code Institute's mock terminal for Heroku.

* The steps for deployment are as follows:
    * Fork or clone this repository
    * Create a new Heroku app
    * Set the buildpacks to Python and NodeJS in that order
    * Link the Heroku app to the repository
    * Click on Deploy

***

## Credits