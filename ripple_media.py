
def box_office_data():
    # NOTE: `movies_str` is a string
    movies_str = "House on Haunted Hill,Cruel Intentions,10 Things I Hate About You,My Favorite Martian,8MM,\
        Fight Club,The Matrix,Any Given Sunday,The Thin Red Line,A Bug's Life,For Love of the Game,Instinct,\
        Mickey Blue Eyes,The Best Man,Bicentennial Man,The 13th Warrior,October Sky,Lake Placid,Random Hearts,\
        Mighty Joe Young,Superstar,Mystery Men,The Talented Mr. Ripley,Dogma,The Out-of-Towners,The Other Sister,\
        Baby Geniuses,The Story of Us,Blast from the Past,The Insider,Saving Private Ryan,Mysteries of Egypt,\
        The Wood,Arlington Road,T-Rex: Back to the Cretaceous,The Iron Giant,Edtv,At First Sight,The Faculty,\
        Summer of Sam,The Bachelor,Stir of Echoes,Anna and the King,Man on the Moon,Galaxy Quest,Enemy of the State,\
        Waking Ned Devine,Doug's 1st Movie,An Ideal Husband,Everest"
    # NOTE: `top_50_list` is a list
    top_50_list = [
        'Star Wars: Episode I - The Phantom Menace', 'The Sixth Sense', 'Austin Powers: The Spy Who Shagged Me',
        'Toy Story 2', 'The Matrix', 'Tarzan', 'Big Daddy', 'The Mummy', 'Runaway Bride', 'The Blair Witch Project',
        'Notting Hill', 'The World Is Not Enough', 'Double Jeopardy', 'Wild Wild West', 'Analyze This',
        "The General's Daughter", 'American Pie', 'Inspector Gadget', 'Shakespeare in Love', 'Sleepy Hollow',
        'The Haunting', 'Patch Adams', 'Entrapment', 'Pokémon: The First Movie - Mewtwo Strikes Back', 'Payback',
        'Deep Blue Sea', 'American Beauty', 'The Thomas Crown Affair', 'Stuart Little', 'Blue Streak',
        'The Green Mile', 'Bowfinger', 'Life', 'The Bone Collector', "She's All That", 'End of Days', 'Three Kings',
        'A Civil Action', 'Stepmom', 'Eyes Wide Shut', 'Never Been Kissed', 'Forces of Nature', 'Varsity Blues',
        'Message in a Bottle', "You've Got Mail", 'South Park: Bigger, Longer & Uncut', 'Stigmata',
        'Life Is Beautiful', 'The Prince of Egypt','Deuce Bigalow: Male Gigolo',
    ]

    # 1.1 TODO: Convert the string `movies_str` into a list and assign it to a variable called `remaining_50_list`
    # NOTE: make sure that the commas that separate the titles in the string don't stay in the titles in the list!
    # Print out the `type` of your new variable, then in a separate print statement, the number of items in it (should be 50).

    # 1.2 TODO: Hmm. Looks like `remaining_50_list` contains the movie "The Matrix" which is also in the "top_50_list".
    # Let's remove this duplicate title from `remaining_50_list`. 
    # Let's use our conditional logic to check if "The Matrix" is still in `remaining_50_list`
    # Print `"The Matrix" in remaining_50_list`. It should print out `False`.
    # NOTE: Make sure to double check the list you are removing from!

    # We're down to 49 movies in `remaining_50_list`.
    # 1.3 TODO: Let's add a movie to the end of the list called "Anywhere But Here".
    # Let's use conditional logic again to check if the last movie in the list is now "Anywhere But Here".
    # Use 'indexing' and conditional logic to check.
    # NOTE: if there are 50 movies in the list, what's the index of the final movie?

    # 1.4 TODO: Let's make sure "remaining_50_list" has exactly 50 movie titles.
    # Print out the number of title-strings in the list (count it with code!)

    # 1.5 TODO: Great! Let's combine the two lists into one list called `top_100`.
    # NOTE: Which list should be first when you combine them? The top 50 titles, or the remaining 50?
    # Print out the number of title-strings in the list (count it with code!)

    # 1.6 TODO: Let's print the first movie in our `top_100`list.
    # Use 'indexing' to do this.

    # 1.7 TODO: Print the top 10 movies in `top_100` as a list.
    # Use 'slicing' to accomplish this!


def create_employee_email_address():
    # Production is going well, now you need to hire a sales person!
    # It's typical when you hire a new employee in your company to setup an email address for them
    # You have decided the format of the email should be:
    # ex: FirstName LastName -> firstname.lastname@ripplemedia.com
    # Let's write some code that converts a name into an email id that matches this format

    employee_name = 'Daffy Duck'

    # 2.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name'
    # (use a string method to lower the name). Print out the variable.

    # 2.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list'
    # (use a string method to split the string into a list) Print out the variable.

    # 2.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called
    # `joined_names` (use a string method to join the list into a new string) Print out the variable.

    # 2.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and
    # save it in a variable `email` (use an f-string to combine the username with the email domain)
    # Print out the variable.
