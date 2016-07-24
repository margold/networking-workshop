# Fragile Knowledge Workshops: Unix/Networking

## What & Why
This workshop takes on fragile knowledge (knowledge without real understanding which makes it hard to use for deriving concepts or solving problems) of the Unix/Networking space. This is the description I use for it:

> Learn about Unix and the Internet in one hour!
> I found that, unlike for web frameworks or machine learning, there aren't really any good, *quick* learning resources for networking and operating systems that give you an overview and some tools to get started. Hence this workshop. We'll cover just enough to make you more comfortable with dealing with the internet, even if (and especially if) you never actually plan to do any lower-level coding yourself.
>
> You should attend if:
> - you heard of/worked with concepts like http/tcp/port/socket/posix/etc a hundred times, but don't quite know what they mean
> - you think that lower-level OS/networking stuff is intimidating
>
> You should also attend if:
> - you want to learn more about how your \*nix operating system works (be it OSX, Linux, or something else)
> - you have written an application that interacts with the internet in a high-level language like Python or Ruby, and want to know how it works under the hood
> - you want to learn about lower-level OS/networking stuff, but don't know where to start
>
> (We will explore what happens between the tcp and http layers using tools like netstat/lsof/telnet/ifconfig and some Python).

## You will need
- a projector
- a whiteboard
- an internet connection to live-code and run tools

## How to run
This presentation uses [remarkjs](https://github.com/gnab/remark), a tool that renders markdown slides in the browser. Due to the current limitations, running it requires [hosting your files using a web server](https://github.com/gnab/remark/wiki#how-it-works):
```
# change into the presentation directory
cd presentation-directory
# run a web server that serves the files in the directory
python -m SimpleHTTPServer 8000
# access the presentation at http://localhost:8000/remark-presentation.html
# access the cheatsheet at http://localhost:8000/remark-cheatsheet.html
```

## How to use
Fragile knowledge is helped by plunking slide after slide of bullet points onto your audience. Fragile knowledge can be combatted by telling a coherent story that ties all that knowledge together into something relevant, and by giving your audience tools they can use to investigate these topics on their own.

Adapt the story to your audience. If they have fragile knowledge of IP addresses, spend more time on tools showing IPs, how a local IP cannot be accessed from the public internet, what the router is doing. If they have done some C programming but has fragile knowledge about the kernel, talk about how the kernel keeps a record of processes and ports. Etc.

In this sense, this workshop consists of
- a handful of slides
- a tool cheat sheet
- extensive teaching notes on story flow and presentation

Things to consider
- The presentation/workshop takes about an hour if you leave out the python sockets server slide and exercise #4 slide, or about an hour and a half if you include writing a simple python sockets server and doing exercise #4.
- I like to put the story points I'm going through on index cards to both be able to talk freely and not get off track.
- The teaching notes give pointers on when it's useful to use the whiteboard or to live-code.
- This workshop has a major flaw - it doesn't integrate security knowledge. If you'll be using it before it's updated, make sure to say a couple words about security with each topic.
- Obviously the notes are simplified. Eg. "the IP packet has a header with an IP, and a payload" should read "has a header with an IP + some other stuff". Etc.

And, last thing: if you're not excited about a topic yourself, leave it out and talk about something else that makes you excited. Or if you think the topic is too important to be left out, find tools or information that can make you excited about it again. Excitement is the best transmitter of non-fragile knowledge, and the best guard against presenting information in a way where it's hard to see why it's relevant in practice.



## Credits
- [System Call Interface and glibc](https://commons.wikimedia.org/wiki/File:Linux_kernel_System_Call_Interface_and_glibc.svg) Shmuel Csaba Otto Traian / [CC-BY-SA-3.0](https://creativecommons.org/licenses/by-sa/3.0/).
- Rendered with [remarkjs](http://remarkjs.com).
- Using the [solarized](http://ethanschoonover.com/solarized) color palette.
