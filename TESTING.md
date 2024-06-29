# Manual Testing

## Home Page

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
| Homepage	| Display |	Homepage is displayed when url is passed into browser |	PASS |
| Logo	| Display|	Logo should be displayed | PASS|
| Nabvar	| Display |	When user is not logged in, only links to "Home", "Menu","About", "Login - Reservation" should be visible | PASS |
| Nabvar	| Display |	When user is logged in, only links to "Home", "Menu","About", "bookings", "Logout "should be visible | PASS |
| Navbar Dropdown	| Display |	It should be visible on smaller screens| PASS |
| Essential Information | Display |Should be displayed	 |	PASS  |
| Footer	| Display |	Should only be visible at the bottom of the webpage | PASS |
| Footer	| Click |Social media links should open a page to each their social media pages |	PASS |
| Navbar| Click | The "Menu" link should redirect to menu.html. | PASS |
| Navbar| Click | The "about" link should redirect to about.html. |	PASS |
| Navbar| Click | The "Login - Reservation" link should redirect to Login - Reservation.html. | PASS |
| Navbar| Click | The "Home" link should redirect to home.html. |	PASS |

## Menu Page

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
| Logo	| Display|	Logo should be displayed| PASS|
| Nabvar	| Display |	Should be visible with the correct information. | PASS |
| Essential Information | Display | We have information about the menus and the prices |	PASS  |
| Footer	| Display |	Should only be visible at the bottom of the webpage | PASS |

## About Page 

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
| Logo	| Display|	Logo should be displayed | PASS|
| Nabvar	| Display | Should be visible with the correct information. | PASS |
| Essential Information | Display | We have information about the opening hours | PASS  |
| Footer	| Display |	Should only be visible at the bottom of the webpage | PASS |

## Login - Reservation

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
| Logo	| Display| Logo	should be displayed | PASS |
| Nabvar	| Display |	When user is not logged in, only links to "Home", "Menu","About", "Login - Reservation" should be visible | PASS |
| Container| Display | Sign In Container with Sign in Form should be visible and a links for Sign up| PASS |
| Sign Up| Click| The "Sign up" link should redirect to sign up form| PASS |
| Login | Input |	User must enter their username, which they have signed up with | PASS |
| Password | Input| User must enter their password, which they have signed up with | PASS |
| Remember Me| Checkbox | User can tick the box to save their log in information | PASS |
| Sign In Button| Click | logs in user. User is redirected to Home, "bookings", "Logout " links should be visible in the navbar| PASS |
| Incorrect Login | Display | Django message The username and/or password you specified are not correct.| PASS |
| Incorrect Password | Display | Django message The username and/or password you specified are not correct.| PASS |
| Footer	| Display |	Should only be visible at the bottom of the webpage | PASS |


## Sign Up

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
| Logo | Display| Logo should be displayed | PASS|
| Container| Display | Sign Up Container with Sign Up Form should be visible and a links for Sign in| PASS |
| Sign In| Click | The "Sign In" link should redirect to sign In form | PASS |
| Username Field | Input | User must enter their username| PASS |
| E-Mail Field | Input| User can enter the e-mail address; only email address possible | PASS |
| Password Field | Input | User must enter a secure password Corresponding to the instructions| PASS |
| Password(again) Field | Input | User must enter the same password, passwords need to match| PASS |
| Sign Up Button | Click |Submits user input and creates new account. User is redirected to Home Page | PASS |
| E-Mail already use| Input |A user is already registered with this email address. | Pass |
| Incorrect E-mail| Input | Warning message assists with correction | Pass |
| Incorrect Password (again)| Input | Message Please field in this field| PASS |
| Empty field | Display |  Message Please field in this field | Pass |

## Bookings page

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
| Logo | Display |	Should be displayed | PASS|
| Add booking | Display| Button should be visible| PASS |
| Essential Information | Display | We have information about the reservation made | PASS  |
| Edit | Display| Button should be visible| PASS |
| Cancel | Display| Button should be visible| PASS |
| Add booking | Click| User is redirected to Make a Reservation| PASS |
| Edit | Click | User is redirected to Edit Reservation | PASS |
| Cancel | Click | User is redirected to Cancel a Booking| PASS |


## Add booking (Make a Reservation)
| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------| 
|Title| Display |Title should appear under the navbar |PASS|
| Booking Container| Display | Booking Form container should be visible| PASS |
| Customer name|Display|The user is asked to enter their name  |PASS|
| Customer name|Input |User enter the name for the booking |PASS|
| Customer name missing |Display |  Message Please field in this field | Pass |
| Party size| Display| The user is asked to enter the number of guest|PASS|
| Party size| Input|User can only submit numbers |PASS|
| Party size missing  |Display |  Message Please field in this field | Pass |
| Party Size (Negative party) |Display | Message The number of customers must be greater than 0. | FAIL |
| Email | Display| The user is asked to enter their email |PASS|
| Email | Input| User can enter an email up to 254 characters |PASS|
| Email missing | Display |  Message Please field in this field | Pass |
| Incorrect E-mail | Input | Warning message assists with correction | Pass |
| Phone | Display |The user is asked to enter their phone number|PASS|
| Phone |Input | User can only enter 15 numbers|PASS|
| Phone missing | Display |  Message Please field in this field | Pass |
| Booking date | Display |The user is asked to enter the date for their booking|PASS|
| Booking date | Input | User can only enter date format dd/mm/yyyy|PASS|
| Booking date missing | Input|Message Please field in this field|PASS|
| Booking date made in the past|Input | Message The booking date cannot be in the past.|FAIL |
| Booking time |Display | The users have the choice between 3 different hours|PASS|
| Booking time |Input|User can only choose any of the times provided|PASS|
| Booking time missing |Input|Message Please field in this field|PASS|
| Table | Display | User can only choose the table |PASS|
| Table |Input| User can only choose the taBLE |PASS|
| Notes | Display| The user can enter some notes.|PASS|
| Notes | Input| The user can enter notes up to 500 characters.|PASS|
| Allergies | Display| The user can enter some allergies. |PASS|
| Allergies | Input| The user can enter allergies up to 200 characters.|PASS|
| Make a Reservation button | Click | If reservation is valid, user will be redirected to the Bookings page, And see this reservation added to the list |PASS|
| Make a Reservation button | Click | If reservation is invalid, user will be ask to change their input accordingly|PASS|
| Make a Reservation button| Click | If reservation is invalid, user will be ask to change their input accordingly except for a past date and a negative number of clients.| FAIL|


    
## Edit a booking 

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
| Logo	| Display|	Should be displayed | PASS |
| Title | Display |Title should appear under the navbar |PASS |
| Edit a past booking | Click |It should not be possible to edit a past booking.|PASS|
| Edit a past booking | display | Cannot edit a booking that has already passed.|FAIL|
| Edit Container| Display | Should contain the name of booking, date & time, number of guest... from the booking form| PASS |
| Save Buttom  | Click | If the update is valid, the user will be redirected to the Bookings page. They will see this reservation added to the list with the correct changes | Pass |
| Customer name| Display | The user should see this name. |PASS|
| Customer name| Input | The user can change this name |PASS|
| Customer name missing | Display |  Message Please field in this field | Pass |
| Party size| Display| The user should see the party size |PASS|
| Party size| Input| The user can change the party size |PASS|
| Party size missing  |Display |  Message Please field in this field | Pass |
| Party Size (Negative party) |Display | Message The number of customers must be greater than 0. | FAIL |
| Email | Display| The user should see this email |PASS|
| Email | Input| The user can change an email up to 254 characters | PASS |
| Email missing | Display |  Message Please field in this field | Pass |
| Incorrect E-mail | Input | Warning message assists with correction | Pass |
| Phone | Display |The user should see their phone number | PASS |
| Phone |Input | The user can change the phone number, up to 15 digits. | PASS |
| Phone missing | Display |  Message Please field in this field | Pass |
| Booking date | Display | The user should see the date for their booking |PASS|
| Booking date | Input | The user can change the date format dd/mm/yyyy | PASS |
| Booking date missing | Input | Message Please field in this field | PASS |
| Booking date made in the past| Input | Message The booking date cannot be in the past.| FAIL |
| Booking time | Display | The user should see the booking time | PASS |
| Booking time | Input |The user can change the time to any of the provided options | PASS|
| Booking time missing | Input| Message Please field in this field | PASS |
| Table | Display | The user should see the table | PASS |
| Table |Input| The user can change the tabLE | PASS |
| Notes | Display| The user should see their notes.| PASS |
| Notes | Input| The user can change the notes up to 500 characters.| PASS |
| Allergies | Display| The user should see their allergies. | PASS |
| Allergies | Input| The user can change allergies up to 200 characters.| PASS |
| Save button  | Click | If the reservation is valid, the user will be redirected to the Bookings page and see this reservation in the list with the modifications made. |PASS|
| Save button  | Click | If reservation is invalid, user will be ask to change their input accordingly|PASS|
| Save button | Click | If reservation is invalid, user will be ask to change their input accordingly except for a past date and a negative number of clients.| FAIL|

## Cancel a booking

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
| Logo	| Display |	Should be displayed | PASS |
| Cancel message | Display |User is asked if they're sure to cancel the booking| PASS |
| Yes button| Click |delet booking and redirected to Bookings page (Reservation List) |PASS|
| No Button | Click |Redirected to Bookings page (Reservation List) |PASS|

## Logout 

| Feature  | Action | Expected Result  | PASS/FAIL  |
|----------|--------|------------------|------------|
|Logo	| Display|	Should be displayed | PASS|
|Sign Out message |Display | User is asked if they're sure to sign out| PASS|
|Sign Out button | Click |User is logged out and redirected to Home Page, "Login - Reservation" should be visible in the navbar | PASS|

# Bugs

## Resolved Bugs

* When asked to enter the booking date, it is possible to enter past dates.
* When asked to enter the size of the party, it is possible to enter a negative number.

## Unresolved Bugs

* Message not displayed as warning when entering a date in the past or a negative number for the party size.
* Message not displayed as warning, when the booking is past.

