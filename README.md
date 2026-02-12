# J*b Tracker

Redoing this to be more straight forward. We are going to make a usable project in python first, then eventually play with it in C++. I can't deal with C++ GUI stuff right now.

I still don't know how to do apps in Python, but I can do scripts. Let's see if that's enough so I can figure out app dev whilst this is happening.

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

These are all the values the user ought to input into the forum. Maybe this will eventually be automated. Below are two tables: the aspects of each attribute of each entity and the const values (keep out of repo for privacy).

| Aspect | Description |
| --- | --- |
| Attribute | An aspect of the entity. |
| Formula | Calculation needed. |
| Default_Value | What is considered 'default' for the attribute in question. |
| Volatile | Can this change, True or False. |
| Type | Kind of data in Attribute. |
| Return | Is the user expecting this attribute to prompt unprompted notifications |
| List? | Boolean value on whether the value is a list and has a distinct options csv (current plan). Has notes on whether on specific details |
| Description | What is the attribute, not noted in program logic at this time. |

### Input Values

| Attribute      | Default_Value | Type    | Description                        |
| -------------- | ------------- | ------- | ---------------------------------- |
| Date           | Today()       | Date    | Date the application was entered   |
| Posted         | Today()       | Date    | Date the job posting was found     |
| Title          | —             | String  | Job role                           |
| Company        | —             | String  | Employer                           |
| Location       | —             | String  | Role location                      |
| Source         | —             | String  | Where you found the job            |
| Link           | —             | String  | URL to the posting                 |
| Wage Range Min | —             | Real    | Lowest pay                         |
| Wage Range Max | —             | Real    | Highest pay                        |
| Pay Frequency  | hour          | String  | ‘hour’, ‘week’, ‘month’, or ‘year’ |
| Hours per Week | 40            | Integer | Work hours per week                |

### Calculated Values

| Derived                       | Formula                                                    |
| ----------------------------- | ---------------------------------------------------------- |
| Days Since Posted             | `julianday('now') - julianday(posted_at)`                  |
| Days Since Entered            | `julianday('now') - julianday(created_at)`                 |
| Current Status                | latest entry in `application_updates` for `application_id` |
| Hours per Year                | `hours_per_week * 52`                                      |
| Hourly Rate                   | depends on pay_frequency and hours_per_week                |
| Weekly / Monthly / Yearly Pay | computed from base inputs depending on pay_frequency       |
