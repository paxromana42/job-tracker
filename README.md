# J*b Tracker

Redoing this to be more straight forward. We are going to make a usable project in python first, then eventually play with it in C++. I can't deal with C++ GUI stuff right now.

I still don't know how to do apps in Python, but I can do scripts. Let's see if that's enough.

## Directory Structure

```bash
Job Tracker
├───j-b_tracker_app // This is my future C++ app, probably really efficient. Empty for now.
├───j-b_pythonista  // My python draft so I can actually use this right now.
└───data            // All the data will go here.
    ├───python      // Python generated data.
    └───real        // C++ data.
```

## Python

WebGUI which will let me input job listings into a real database with logic.

## C++

I have no clue how this is going to work mah dude.

## Common Features

These are all the values the user ought to input into the forum. Maybe this will eventually be automated.

### Input Values

| Date | Posted | Updated | Status | Title | Company | Office | Location | Salaried | Low | High |  Likely | Want | Source | Link |

|  |

### Calculated Values

| ID | Since_Post | Since_App | Should_Email | Distance_Home | Distance_LU | Distance_GF | H-L | H-H | Hourly | M-L | M-H | Monthly | Y-L | Y-H | Yearly |
