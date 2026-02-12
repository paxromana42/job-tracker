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

| Attribute | Default_Value | Type | List? | Description |
| --- | --- | --- | --- | --- |
| Date | Today() | Date | No (Maybe Date input) | Date of creation of App down to millisecond |
| Posted | Today() | Date | No (Maybe Date input) | Date the App was posted on relevant medium. |
| Updated | Today() | Date | No (Maybe Date input) | Last Date App entity was modified. Might be an array of values. |
| Status | Applied | String | Yes | The status of the Application. Used in sorting and other logic. |
| Title | | String | No | Name of Role in question |
| Company | | String | No | Name of Company being applied to |
| Office | In-person | String | Yes | Is this role in-person or some variant of remote |
| Location | | ? | No | Where is this role. Be as specific as desired, though the Distance Formulae won't like broad answers |
| Given | No | Boolean | Yes | Is there a listed wage range. If so, use it, if not, source of wage is GlassDoor or similar source. |
| Salaried | No | Boolean | Yes | Is the work based on a set pay, True, or varies based on shifts served, False. |
| Low | | Double | No | Low end of wage range |
| High | | Double | No | High end of wage range |
| Likely | 5 | Unsigned Integer | ~Yes (Range) | A value from 0 to 10 about how likely this role is attainable. |
| Wanted | 5 | Unsigned Integer | ~Yes (Range) | A value from 0 to 10 about how likely this role is wanted. |
| Source | | String | Yes | What platform did the role make itself known to the user |
| Link | | String | No | Assuming all applications are done online (they are), then here is the hyperlink for the role. This will most likely contain many dead links as roles are removed and closed with the passage of time. |

### Calculated Values

| Attribute | Formula | Volatile | Return | Description |
| --- | --- | --- | --- | --- |
| ID | 0x*Date* | No | No | Representation of the entity. |
| Since_Post | *Post* - TODAY() | Yes | No | How many days since role was posted. |
| Since_Days | *Date* - TODAY() | Yes | No | How many days since app was made. |
| App_Delta | *Post* - *Date* | No | No | How long between *Post* and *Date* |
| In_process | *Status != (Accepted or Dismissed or Rejected)* | Yes | No | Is the application on going. |
| Last_updated | | | | |
| Follow-Up? | *if ('In Process' and max(Date- Update, Updated[n-1] - Updated[n]) >= Long Time) | Yes | Yes | Should user send a follow-up email? |
| Distance_Home | (Location to HOME) | No | No | Distance, either in KM or through maps, from Location to HOME |
| Distance_Uni | (Location to UNI) | No | No | Distance, either in KM or through maps, from Location to GF |
| Distance_GF | Location to GF | No (Maybe) | No | Distance, either in KM or through maps, from Location to GF |
| H-L | | No | No | Low end per hour. |
| H-H | | No | No | High end per hour. |
| Hourly | String("H-L - H-H") | No | No | Diplays to user in a friendly way the hourly wage. |
| M-L | | | | Low end per month. |
| M-H | | | | High end per month. |
| Monthly | | | | Diplays to user in a friendly way the monthly wage. |
| Y-L | | | | Low end per month. |
| Y-H | | | | High end per month. |
| Yearly | | | | Diplays to user in a friendly way the yearly wage. |
