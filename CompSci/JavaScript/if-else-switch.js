// ----- If, Else If & Else Statements -----

let music = "dance";

// ----- String Equals Statements -----
if (music == "classical")
{
    console.log("Oh, how relaxing.")
}
else if (music == "disco")
{
    console.log("Where are my dancing shoes?")
}
else if (music == "dance")
{
    console.log("Where's the party?")
}
else
{
    console.log("Turn it down.")
}
console.log();

// ----- Statement types -----

// ==   Checks if values are equal.
// ===  Checks if values and types are equal.
// !=   Checks if values are not equal.
// !==  Checks if values and types are not equal.
// >=   Checks if parameter 1 is greater than or equal to parameter 2.
// >    Checks if parameter 1 is greater than parameter 2.
// <=   Checks if parameter 1 is less than or equal to parameter 2.
// <    Checks if parameter 1 is less than parameter 2.
// %    Returns the remainder after parameter 1 is divided by parameter 2.

if ( 4 === "4")
{
    console.log(true);
}
else
{
    console. log (false);
}

if ( 4 != "4")
{
    console.log(true);
}
else
{
    console. log (false);
}
console.log();

// ----- Age & Country Activity -----
let age     = 21;
let country = "UK"

if (age > 17 || country == "UK")
{
    console.log("What would you like?")
}
else
{
    console.log("Sorry, but you aren't old enough.")
}
console.log();

// ----- Food Activity -----
let food    = "ice cream";
let hunger  = "full";

if (hunger == "full" && food == "ice cream")
{
    console.log("Of course, who wouldn't?");
}
else if (hunger == "hungry && food" == "ice cream")
{
    console.log("Yes please - I'm starving. Could I also have a pizza?");
}
else if (hunger == "hungry" && food == "sprouts")
{
    console.log("Actually, I can wait...");
}
else
{
    console.log("No thanks, I'm stuffed");
}
console.log();

// ----- Food Activity 2 -----
food    = "chps";

if (food == "ice cream" || food == "pizza")
{
    console.log("Let's eat!");
}
else if (food == "sprouts" || food == "broccoli")
{
    console.log("No thanks.");
}
else
{
    console.log("Sure, why not.");
}
console.log();

// ----- Weekend Alarm Activity -----
let day = "Saturday";

if (day == "Saturday" || day == "Sunday")
{
    console.log("Ah, it's the weekend!")
}
else
{
    console.log("Oh no, work again...")
}
console.log();

// ----- Switch Case Activity -----
food = "sprouts";

switch (food)
{
    case "ice cream":
    case "pizza":
        console.log("Delicious!");
        break;
    case "sprouts":
    case "broccoli":
        console.log("Disgusting...");
        break;
    default:
        console.log("Sure, why not.")
}