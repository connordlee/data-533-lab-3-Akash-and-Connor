# Club Tutorial

This page provides a tutorial on basic usage of the Club package.

Contents

* Basic Club Usage
  * Creating and Populating a Club
  * Creating Members and Viewing Member Information
    * Players
    * Staff
  * Updating Member Information
    * Players
    * Staff
  * Creating and Updating Fans
    * Domestic
    * International


## Basic Club Usage
The Club package should be coppied to the working directory for the file that will be using it. Once this is done the Club package will be available in the "club" module. The main object in the club package is a club which has two objects having two sub objects of their own. The structure is listed below:
* Club
  * Members
    * Players
    * Staff
  * Fans
    * Domestic
    * International

### Creating, Populating and Updating a Club
Before creating a club you will need to import the club package which is done as follows:

```
>>> from club import club
```

A club can be initialized empty (no members or fans) or by passing in lists of members and fans, both options are shown below.

**Empty:**

```
>>> madrid = club.club()
```

**With Members and Fans List**

```
>>> madrid = club.club(playerList, staffList, domList, intList)
```

The player list and staff list can be created by creating the players or staff members as discussed in the section on creating club  members (below) and then storing the players in a list of players and the staff in a list of staff as shown below. NOTE: The `asList()` method is required to convert the players and staff to lists.

```
>>> ramos = player('Sergio Ramos', 'Spanish', 15000000, 14, 'Right Back', 15)
>>> benzema = player('Karim Benzema', 'French', 7920000, 10, 'Manager', 9)
>>> zidane = staff('Zinedine Zidane', 'French', 5500000, 9, 'Skipper')
>>> vazquez = staff('Roberto Vazquez', 'Spanish', 3200000, 1, 'Goalkeeping Coach')
>>> playerList = [ramos.asList(), benzema.asList()]
>>> staffList = [zidane.asList(), vazquez.asList()]
>>> madrid = club.club(playerList, staffList)
>>> madrid.displayMembers(salary=True)
           Name: Zinedine Zidane
    Nationality: French
Years With Club: 9
      Job Title: Skipper
         Salary: 5500000


           Name: Roberto Vazquez
    Nationality: Spanish
Years With Club: 1
      Job Title: Goalkeeping Coach
         Salary: 3200000


           Name: Sergio Ramos
    Nationality: Spanish
Years With Club: 14
       Position: Right Back
  Jersey Number: 15
         Salary: 15000000


           Name: Karim Benzema
    Nationality: French
Years With Club: 10
       Position: Manager
  Jersey Number: 9
         Salary: 7920000
```
As seen in the above example members can be displayed using the `displayMembers()` method which has an optional input of salary. If you want to view the salaries of the members you should pass the argument salary=True into the `displayMembers()` method. The same thing can be done with the `displayPlayers()` method which just displays players and the `displayStaff()` which just displays staff members.

Once the club has been created members can be added as follows:

```
madrid.addPlayer('Karim Benzema', 'French', 7920000, 10, 'Striker', 9)
madrid.addStaff('Roberto Vazquez', 'Spain', 3200000, 1, 'Goalkeeping Coach')
```

Members can be added to the club using the `addPlayer()` and `addStaff()` methods which take in the following arguments.
* `addPlayer()`
  * Players Name
  * Nationality
  * Salary
  * Number of Years With the Club
  * Position
  * Jersey Number
* `addStaff()`
  * Staff Name
  * Nationality
  * Salary
  * Number of Years With the Club
  * Job Title

Once members have been added to the club they can be removed using the `removePlayer()` and `removeStaff()` methods as follows.

```
>>> madrid.removeStaff("Zinedine Zidane")
>>> madrid.removePlayer('Karim Benzema')
>>> madrid.displayMembers(salary=True)

           Name: Roberto Vazquez
    Nationality: Spanish
Years With Club: 1
      Job Title: Goalkeeping Coach
         Salary: 3200000


           Name: Sergio Ramos
    Nationality: Spanish
Years With Club: 14
       Position: Right Back
  Jersey Number: 15
         Salary: 15000000
```

Members are updated using the `updatePlayer()` and `updateStaff()` methods as follows.

```
>>> madrid.updatePlayer('Sergio Ramos', nationality="None", salary=100, yearsWClub=100, position="Left Right Out", jersey=0)
>>> madrid.displayPlayers(salary=True)
           Name: Sergio Ramos
    Nationality: None
Years With Club: 100
       Position: Left Right Out
  Jersey Number: 0
         Salary: 100
>>> madrid.updateStaff("Zinedine Zidane", nationality="Home", salary=42, yearsWClub=10000, title="Skipper")
>>> madrid.displayStaff(salary=True)
           Name: Zinedine Zidane
    Nationality: Home
Years With Club: 10000
      Job Title: Skipper
         Salary: 42
```

### Creating and Updating Members
Club members are broken into two categories (players and staff), functionality for each of these categories can be imported seperatly as shown below:

**For Players:**

```
>>> from club.member.membertypes import player
```

**For Staff:**

```
>>> from club.member.membertypes import staff
```

Alternatively functionality for both players and staff can be imported together in one line as follows:

```
>>> from club.member.membertypes import player, staff
```

#### Creating Members and Viewing Member Information
The player and staff objects store information about players and objects for the club to review and update. An explanation of how to create these objects can be found below.

##### Players
Once the package has been imported a players can be created and viewed as follows:
```
>>> ramos = player('Sergio Ramos', 'Spain', 15000000, 14, 'Right Back', 15)
>>> ramos.display()
           Name: Sergio Ramos
    Nationality: Spain
Years With Club: 14
       Position: Right Back
  Jersey Number: 15
>>> print("Player Salary: ", ramos.getSalary())
Player Salary: 15000000
```
Players are created by passing the following information into `player()`:
* Players Name
* Nationality
* Salary
* Number of Years With the Club
* Position
* Jersey Number

A players information (with the exception of their salary) can be viewed with the `display()` method. A players salary can be viewed by printing the result of the `getSalary()` method.

##### Staff
Once the package has been imported a staff member can be created and viewed as follows:
```
>>> zidane = staff('Zinedine Zidane', 'France', 5500000, 9, 'Skipper')
>>> zidane.display()
           Name: Zinedine Zidane
    Nationality: France
Years With Club: 9
      Job Title: Skipper
>>> print("Staff Salary: ", zidane.getSalary())
Staff Salary: 5500000
```
Staff are created by passing the following information into `staff()`:
* Staff Name
* Nationality
* Salary
* Number of Years With the Club
* Job Title

A staff members information (with the exception of their salary) can be viewed with the `display()` method. A staff members salary can be viewed by printing the result of the `getSalary()` method.

### Updating Member Information
All members have name, nationality, salary, and years with the club attributes, and these attributes can all be updated (with the exception of name which should not be updated) the same way regardless of if they are a palyer or staff, as shown below.

```
>>> zidane.updateNationality('French')
>>> zidane.setSalary(7500000)
>>> zidane.newYear()
>>> zidane.display()
           Name: Zinedine Zidane
    Nationality: French
Years With Club: 10
      Job Title: Skipper
>>> print("Updated Salary: ", zidane.getSalary())
Updated Salary: 7500000
```
The methods for updating each member attribute are explained in more detail below:
* `updateNationality()`: Takes in the new nationality as an argument and updates the members nationality
* `setSalary()`: Takes in the new salary as an argument and updates the members salary
* `newYear()`: Does not take any arguments and increases the years with the club for the member by 1

Players and staff also have some independent attributes and functions specific to them which will be discussed in the following two sections.

#### Players
The attributes specific to players are position and jersey number which can be updated as described below.

```
>>> ramos.updatePosition('Center Back')
>>> ramos.updateJerseyNum(4)
>>> ramos.display()
           Name: Sergio Ramos
    Nationality: Spain
Years With Club: 14
       Position: Center Back
  Jersey Number: 4
```
The methods for updating a players attributes are explained in more detail below:
* `updatePosition()`: Takes in the new position as an argument and updates the players position
* `updateJerseyNum()`: Takes in the new jersey number as an argument and updates the players jersey number

#### Staff
The attribute specific to staff is their job title which can be updated as described below.

```
>>> zidane.updateTitle('Manager')
>>> zidane.display()
           Name: Zinedine Zidane
    Nationality: French
Years With Club: 10
      Job Title: Manager
```

A staff members title is updated using the `updateTitle()` method which takes in the new title as an argument and updates the staff members title.

