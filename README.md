# momentum

## Table of Contents

- [Tech Stack](#tech-stack)
- [Design](#design)
  - [User Stories](#user-stories)
    - [Must Have](#must-have)
    - [Should Have](#should-have)
    - [Could Have](#could-have)
  - [Wireframes](#wireframes)
  - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
  - [Colour Palette](#colour-palette)
  - [Logo](#logo)
- [Features](#features)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Code Validation (W3C)](#code-validation-w3c)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript (JSHint)](#javascript-jshint)
  - [Responsive Design](#responsive-design)
  - [Lighthouse](#lighthouse)
- [AI Augmented Development](#ai-augmented-development)
- [Team Contributions](#team-contributions)

## Tech Stack

HTML, CSS, JavaScript
Bootstrap5, Django,
Python (3.12.8)

### User Stories

#### Must Have

- User Story 1 : As a user I want to be able to create a task list.
- User Story 2: As a user I want to be able to read my tasks.
- User Story 3 : As a user I want to be able to update my tasks.
- User Story 4 : As a user I want to be able to delete tasks.
- User Story 5: As a user, I want to be logged out safely

#### Should Have

- User Story 6: As a user, I want validation on due dates.
- User Story 7: As a user i want the site to look appealing and be - user friendly.
- User Story 8:As a user, I want to expand task details.

#### Could Have

- User Story 9:As a user, I want to filter tasks by category. 
- User Story 10:As a user, I want tasks sorted by due date.
- User Story 11: As a user, I want to see task priority visually. 
- User Story 12: As a user I want to be able to create multiple task lists.

### Wireframes

Wireframes

![Wireframes](<readme images/Hakathon Wireframe 2.png>)

### Entity Relationship Diagram (ERD)

 ![hakathon ERD](<readme images/hakathon ERD.png>)

### Colour Palette

Footer and Header<br>
#366fe9 (Blue)<br>
Background<br>
rgba(248, 249, 250, 1) (off white)

### Logo

![pencil logo](<readme images/pencil logo.jpg>) 

## Design

Website v1

![hakathon website v1](<readme images/hakathon website v1.png>)

Website v2

![hakathon website v2](<readme images/hakathon website v2.png>)

Website v3

![hakathon website v3](<readme images/hakathon website v3.png>)

## Features

![sign up feature](<readme images/sign up feature.png>)
![sign in feature](<readme images/sign in feature.png>)
![add task feature](<readme images/add task feature.png>)
![edit task feature](<readme images/edit task feature.png>)
![delete task feature](<readme images/delete task feature.png>)
![category feature](<readme images/category feature.png>)
![sign out feature](<readme images/sign out feature.png>)


## Testing

### Manual Testing

| # | User Story | Test Case | Expected Result | Pass/Fail |
|---|-----------|-----------|-----------------|-----------|
| 1 | As a user, I want to create a new task | Click "+ Add New Task" button and fill form | Modal opens, form clears, task saves on submit | Pass |
| 2 | As a user, I want to edit an existing task | Click "Edit" button on a task | Modal opens with pre-populated data, form action changes to edit URL | Pass |
| 3 | As a user, I want to delete a task | Click "Delete" button and confirm | Delete modal appears, task is removed after confirmation | Pass |
| 4 | As a user, I want to filter tasks by category | Click category tabs (Work, Personal, Home) | Only tasks in selected category display, tab shows as active | Pass |
| 5 | As a user, I want to view all my tasks | Click "All Tasks" tab | All tasks display regardless of category | Pass |
| 6 | As a user, I want to see task priority visually | View task list | Priority badges show correct colors (High=Red, Medium=Yellow, Low=Green) | Pass |
| 7 | As a user, I want to expand task details | Click accordion button on task | Task description and action buttons (Edit/Delete) display | Pass |
| 8 | As a user, I want tasks sorted by due date | View task list | Tasks appear ordered by earliest due date | Pass |
| 9 | As a user, I want to be logged out safely | Click logout link | User redirected to login page, session destroyed | Pass |

### Code Validation (W3C)

#### HTML

Index html error

![hakathon index html error](<readme images/hakathon index html error.png>)

Index html validation

![hakathon index html validation](<readme images/hakathon index html validation.png>)

#### CSS

![hakathon css validation](<readme images/hakathon css validation.png>)

#### JavaScript (JSHint)

JavaScript error

![hakathon js error](<readme images/hakathon js error.png>)

![hakathon js validation](<readme images/hakathon js validation.png>)

### Responsive Design

Mobile <br>
![phone hakathon](<readme images/phone hakathon.png>)<br>
Tablet<br>
![tablet hakathon](<readme images/tablet hakathon.png>)<br>
Laptop<br>
![laptop hackathon](<readme images/laptop hackathon.png>)

### Lighthouse

![hakathon lighthouse](<readme images/hakathon lighthouse.png>)
![hakathon lighthouse 2](<readme images/hakathon lighthouse 2.png>)

## AI Augmented Development

Our use of AI was very helpful in terms of troubleshooting and at some points rearranging our code to increase its readability. 

We made sure we understood any code it suggested, before we implemented it.
## Team Contributions

Pair programming was the cornerstone of this project. With the main bulk of the project being reliant on different code in separate files, there would have been a multitude of merge conflicts if we had attempted to code individually.  

- **Declan** Allauth, Template HTML
- **Sheena** Models & Forms
- **Ayana** Models & Forms, README content
- **Louie** views.py, CSS, README template