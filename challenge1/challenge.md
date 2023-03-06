
## Round 1: "Hello, Cisco!" 

In this round, your team will develop a very simple bot command to ease you into the competition. The first part will be easy, but each part after that will get increasingly difficult.


Keep in mind:
- For all parts 1 to 5 below, **allow case insensitive input**. The response message can be in any case you like. 
- **Complete all parts in the order they’re written.**
- When implementing a part, **you must retain the behaviour of all previous parts**. We need to be able to test your bot against all parts that you solve.

---

## Challenge 1.1

When the bot receives any message, return the message **“Hello, Cisco!”**.

You can ignore the contents of the input message, for now... 
 
## Challenge 1.2

If the message length is greater than 0, you can assume someone entered their name. Return a message in the format **“Hello, (name)!”**.


If message length == 0, **you should return “Hello, Cisco!”**, or you will lose out on points for challenge 1.1! 
 
## Challenge 1.3

Chuck Robbins is the CEO of Cisco.

If the **input message** equals the string **“Chuck Robbins”**, return the message **“Hello Cisco’s favourite CEO Chuck Robbins!”**
 
## Challenge 1.4

Create any unique message for each member of your team. When the input message equals the **first name of a team member**, return the unique message. 
 
Example: 

- Input: “Ronan” 
- Output: “Everybody loves Ronan!” 
 
## Challenge 1.5

If you got this far, well done! Here is a harder challenge to keep you busy:

An **anagram** is *"a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp."*.

If any name given to the bot is an **anagram of “Cisco”**, return “Hello, Cisco in disguise!”.

However, if the name equals “Cisco”, you should still reply only with “Hello, Cisco!”. 
 
Example: 

- Input: “Oscis” 
- Output: “Hello, Cisco in disguise!”
