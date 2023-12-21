Just a log of my thoughts and approaches for the solutions!
- Day 1 - Day 4: I learned the importance of regex, and tried to use it in my solves. I also made stupid mistakes which led to long debug hours, after some days though my debug abilities have definitely improved!
- Day 4: I used recursion with memoization and probably overcomplicated it but I am super proud of that solution
- Day 5: Part a was relatively straight forward, part b was extremely difficult. I was able to figure out the logic about the ranges on my own which I'm really proud of, but I couldn't get the code to work, so I copied a redditer's code. Part b of day 5 is unsolved by me. 
- Day 6: Easy Math day :)
- Day 7: My favorite problem cuz its about card games which I really like
- Day 8 - 9: blur I can't remember, but the solutions seem interesting enough
- Day 10: Part b logic I couldn't figure out on my own. I learned about a new alg called for it, and i was able to figure out the code relatively easily after that
- Day 11: Nothing special
(FINALS HAVE STARTED AT THIS POINT SO SCHOOL IS A THING)
- Day 12: Recursion + some pruning, and then used functools.cache for memoization. (kind of lazy but couldn't figure out how to do it without)
- Day 13: Terrible code, cannot figure out a better solution, but it works
    - Reddit Tips after: should have counted differences instead and that would have made the conversion to part 2 extremely easy
- Day 14: PART B WAS SUPER FUN AND INTERESTING. I WAS OFF BY 7 IN MY FIRST TRY. 
    - I wasn't able to figure out part b easily. I knew there was cycle detection involved but I couldn't get it. After reading: @derailed_dash's github repo I understood the algorithm. I will be reading their repo to learn how they did the other problems because they explain their code, and it will be a good learning experience for me. 
    - The algorithm required finding the length of the cycle, the first repeated cycle and the number of additional cycles
    - I had an off by one even after reading the solution, that was because i did not account for the fact that the current node was already found, so I needed to add that. 
    - This is the website that I used: https://aoc.just2good.co.uk/ 
    - really cool, I'm sure i'll be able to recognize this pattern next time! 
- Day 15: Implemented Hashmaps using arrays and linked lists, even though that was not required, my best day in terms of placement
- Day 16: The light beams, I had a stupid error, where I looked at the next value instead of the current value. I was able to figure it out in the end, was quite proud to be able to get the solution
- Day 17: I know this is A* or Dijkstra's skipped it pretty instantly as of now. Will come back to it after Day 18
    - Using this: https://www.redblobgames.com/pathfinding/a-star/implementation.html
    - and the medium article that i used during my old A* stimulation: 
    https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2\
    - basically copying over old code and hoping it works
- Day 18: MANNN OH MAN THIS IS FRUSTRATING. I tried the same principle as Day 10 partb but due to some bug somewhere, I can't figure it out, and it also requies constructing a 2d array so large that it won't work. So I'm gonna try the shoelace algorithm and Pick's algorithm and hope it works
    - update picks theorem worked first try, i feel insanely stupid for sticking so hard with building the 2d array from scratch. 
    - we live and we learn i guess
    - part b was a really easy conversion. 
    - this was a journey. Its really cool how random facts about math can solve real world programming problems (like dig a logoon of lava)
    - my mind is truly blown by the math tho
- Day 19: part 2 seemed doable at first but I think i completely misunderstood the question. I calculated the number of xmas values accepted and then multiplied them. BUT i didn't realize that values of x could be rejected but if paired up with other values of mas, they could be accepted.need to think of all the ranges as one
    - I think looking at other people's methods have helped me understand stuff
    - Tentatively tweaking some things should get me to output, will try it tmrw.
    - this has been immensely helpful while debugging: https://www.reddit.com/r/adventofcode/comments/18mau1e/2023_day_19_why_does_my_solution_for_part_2_not/. Thank you to @1234abcdcba4321 redditer
    - AFTER 3 HOURS OF DEBUGGING I DID IT! 
    - the code wasn't that difficult i was able to imagine the solution, the previous version needed just a few tweeks. 
    - LEARNING: try to print before using debuggers, i think i spent too much time comparing with bare eyes. Espectially cuz i had expected output in front of me. 
    - I definitely owuld not have been able to figure it out without the help of the expected output
- Day 20: advent of reading comprehension too tired to do this


    