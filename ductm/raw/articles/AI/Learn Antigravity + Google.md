00:00:00: Hey, welcome to the definitive course on vibe  coding for beginners. I use anti-gravity,    
00:00:04: Gemini 3.1 Pro, and Claude Code in my life every  day to manage a business that does over $4 million    
00:00:09: a year in profit. I also teach around 2,000 people  how to use technologies just like this to improve    
00:00:14: their lives, both personal and business. So, the  way this course is going to work is it'll start by    
00:00:18: teaching you guys how to set up anti-gravity,  Gemini, and then Claude Code in a simple    
00:00:22: development environment. And then we're going to  jump right into the building. And we'll start with    
00:00:26: simple portfolio sites before working our way  all the way up to full-fledged SAS apps with    
00:00:30: authentication, databases, and so on and so forth.  At every step along the way, I'm going to pause    
00:00:35: and then show you guys some of the principles  behind what I just built. And my recommendation    
00:00:38: is if you want to get the most out of this course,  you'd actually build alongside me. Okay, so no    
00:00:42: fluff. Here's what we're going to cover. We'll  start with the simple toolkit. So anti-gravity,    
00:00:46: Gemini 3.1 Pro, and Claude Code. I'll give  you guys the best development environment    
00:00:49: available in probably around 15 minutes. Then  we'll build your first vibecoded product,    
00:00:53: which in our case is going to be a personal  site designed with anti-gravity and Gemini.    
00:00:56: You'll have this live on the internet, including  deployment in about 15 minutes. After that,    
00:01:00: I'll pause to talk authentication and security cuz  I think it's one thing to build simple portfolio    
00:01:04: sites and stuff, but if you wanted to push that  out to a fullyfledged app with authentication,    
00:01:08: databases, and a back end, a big issue in vibe  coding is security, and I want to make sure    
00:01:12: that we cover at least the 8020 of that. Then  we'll build another product, which will be a    
00:01:15: client-f facing dashboard with authentication, a  database, and a very clean UI. And at that point,    
00:01:19: since we'll have gotten our hands dirty, we  can then cover foundational concepts behind    
00:01:22: modern software applications, including hosting,  databases, the major software design patterns,    
00:01:28: versioning and GitHub repositories, the major  frameworks currently available, then also how to    
00:01:32: use agents to vibe code all this stuff way faster.  I'm then going to give you a design specific deep    
00:01:36: dive, which is how to go from a rough idea to a  polished professional design and anti-gravity.    
00:01:40: Then we'll build our next product, which will be  a lead generation SAS app that scrapes, enriches,    
00:01:44: and then cues up the sending of fully automatic  emails. This is an actual system I use production.    
00:01:48: After that, we'll do an AI based SAS app that  uses AI to generate thumbnails. It's actually    
00:01:52: really similar to the system that I used to create  the thumbnail for the video you're watching right    
00:01:55: now. So, pretty meta. Once we're done with that,  I'm going to teach you guys some debugging and    
00:01:58: iteration techniques. You guys will probably have  seen me do a lot of this and hopefully have done    
00:02:02: a lot of it yourselves by now. But, I'm going  to give you guys a simple framework that you    
00:02:05: could use to steer back Gemini and then claude  code anytime it starts veering outside of your    
00:02:09: uh recommendations. And then finally, we'll build  a content automation SAS app that repurposes a    
00:02:14: single piece of content across multiple platforms.  That's another system that I actually use. Before    
00:02:18: we wrap up, we'll talk about the economics of  vibe coding, which is how to price, package,    
00:02:22: and then sell what you build. And that's important  because I find a lot of people watching this are    
00:02:25: probably going to be doing so not just for their  own hobbies, but for financial reasons. We want to    
00:02:29: make money with the things that we build. Okay, so  I care a lot about making money with this stuff.    
00:02:33: I want to show you guys how to do that as well.  Hopefully that makes sense. Let's not waste any    
00:02:36: time. Let's strap in and get started. Okay, so  how do you actually set up anti-gravity? Just    
00:02:40: head over to anti-gravity.google. They actually  have like the Google domain name, which is    
00:02:44: hilarious. and then just click on this little  download button. If you guys are on a Windows,    
00:02:48: it'll be download for Windows. Since I'm on a Mac  OS, this is download for Mac OS. Now, if you guys    
00:02:52: don't know which one of these to select. It's  pretty easy. Most modern computing applications    
00:02:56: nowadays have the ability to type like about  and then you can just go about this Mac,    
00:03:00: about this PC or whatever. And then it'll tell you  whether or not you are an Apple silicon or Intel    
00:03:05: silicon for instance with this line right here.  If I was on Intel, it would actually say like an    
00:03:09: Intel M whatever. Because I'm on an Apple silicon,  it says Apple M4 Max. And so this is the one that    
00:03:15: I need to download. If you guys are on Windows,  double check to see if it says x64 anywhere.    
00:03:19: If you guys are on Linux, you probably know more  about computers than I, so I'll stop embarrassing    
00:03:22: myself. So I'm going to give this button a quick  click. That is going to download the anti-gravity    
00:03:26: installer. On Mac, what ends up happening is we  get a little thing in the top right hand corner    
00:03:30: here, which is anti-gravity. And then all you guys  have to do is just drag this anti-gravity app into    
00:03:34: the applications folder and then let go. I already  have anti-gravity installed, so I'm not going to    
00:03:38: do that part. But that that's the installation.  It's about that easy, at least on Mac. On PC,    
00:03:42: you're going to have a little screen that pops up.  Just click accept a bunch of times until you're    
00:03:45: done. Okay. After that, what you're going to get  is a page that looks something like this. So, I'm    
00:03:48: just going to zoom in to make things a little bit  more visible. And hopefully my big head doesn't    
00:03:51: get in the way. But basically, um the way that  anti-gravity works is you have to connect to your    
00:03:55: Google account in order to get up and running.  And once you connect your Google account, you    
00:03:58: can also use um you know, Gemini as a model. Uh  the reason why this isn't popping up on the right    
00:04:03: hand side as you see is because we haven't logged  in with Google yet. So, what I'm going to do next,    
00:04:07: I'm going to click this login with Google button.  I'm then going to sign in and click sign in. and    
00:04:10: then it'll successfully authenticate you and then  take you back to the main menu. After that's done,    
00:04:14: you'll see up at the top we have a bunch more  features. In order to open up the AI feature,    
00:04:18: just click on this one on the right. It's  called your agent. There's also a little hotkey,    
00:04:21: which I use pretty often, which is just  um option uh commandB. And by doing this,    
00:04:25: I can make this pop out really quickly and  easily. Obviously, if you're on Windows,    
00:04:28: things will be a little bit different, but it's  not that bad. Now, you're inside of anti-gravity.    
00:04:32: You can actually have a conversation. So, I'm  going to say, "Hey, what's up?" I'm going to    
00:04:35: run through the UX of how to communicate with your  agent in a second, but I just wanted to show you    
00:04:38: guys how easy it is to actually get the AI part  up and running. Um, Gemini 3.1 Pro High should be    
00:04:43: provided to everybody, although with different  usage limits depending on whether or not you    
00:04:47: upgrade their plans and so on and so forth. And  you also have other models too, like 3.1 Pro Low,    
00:04:51: Gemini 3 Flash, Sonnet 4.6, Opus 4.6, and so on.  Okay, cool. So, that's just getting anti-gravity    
00:04:57: up and running. The next thing I want to do is I  actually want to explain the UX. After I explain    
00:05:01: the UX, I'll also talk about Claude Code, which  is the alternative chat window, kind of like this    
00:05:05: little agent chat widget, um, except for the Cloud  series of models that performs really, really well    
00:05:10: in specific applications, which we're also going  to use in conjunction with Gemini in this course.    
00:05:13: So, really, I want you to think about anti-gravity  as being divided into three panes. On the leftmost    
00:05:18: pane, you have basically the explorer. And for  the most part, you're only really going to be    
00:05:22: using the Explorer. You're not really going to  use the rest of these things. In the middle,    
00:05:25: you're actually going to have your file editor.  And right now, we don't have any files open,    
00:05:28: which is why we just see the anti-gravity logo.  And then on the right hand side, you actually have    
00:05:31: like your agent chat, your ability to, you know,  talk to AI. And this is how most like integrated    
00:05:36: development environments are nowadays. Um, I say  most because anti-gravity isn't really technically    
00:05:39: an IDE. There's like a couple of additional  features here, but I don't want to be pedantic.    
00:05:43: For all intents and purposes, this is an IDE. And  this is how it works. So, in order for us to see    
00:05:47: the things on the lefth hand side here, this  explore, we actually do need to open a folder,    
00:05:50: which is why it's asking us to do that. So, I'm  going to click open folder. And then I just set up    
00:05:54: this little demo for a video I recorded yesterday  called website builder. So, I'm just going to open    
00:05:57: that up. Okay. And now hopefully you guys could  see the page is transformed in this middle section    
00:06:01: is our our file explorer. So because I don't  really think files are as important these days    
00:06:06: to explore because AI does most that for you.  I usually make the lefth hand side or the right    
00:06:10: hand side way bigger. A lot of the time I actually  just issue this middle pane entirely actually and    
00:06:15: then just chat with the agent. But I'll I'll show  you guys how that works later. For now let's learn    
00:06:18: this on the left hand side here. As you see this  is just a file explorer like anything else just    
00:06:22: like a finder on your computer or whatever. You  know you have the exact same thing here. So, you    
00:06:27: know, in my case, I'm scrolling through my Mac uh  files and and folders and stuff like that. Well,    
00:06:32: that's basically exactly what anti-gravity does.  It just does it for you in a slightly different    
00:06:35: user experience. And so, folders in this case have  this little folder icon, right? Um specific types    
00:06:41: of files which have different file endings have  other logos and stuff. This is a markdown file,    
00:06:46: which is why it's an M and then it's a down. Uh  this is an HTML file, which is why it looks like    
00:06:50: that. And, you know, you don't actually need to  know a ton of programming in order to get all of    
00:06:53: this stuff. To be honest, um I don't have a formal  programming degree or anything like that. I still    
00:06:58: understood this stuff just fine after spending a  little bit of time inside of this dashboard. So,    
00:07:01: just to prove to you guys that, you know, we're  in a file. Uh if I click on this index.html here,    
00:07:05: you see that I actually have like a website file  set up here. HTML is the um ending for websites    
00:07:11: basically. And uh you know, there's a bunch  of different text here in this middle editor.    
00:07:15: Doc type, HTML head, meta, right? I don't actually  know what most of this stuff means. I just have my    
00:07:20: agent deal with it. But it is important from time  to time to at least be able to poke into the file    
00:07:24: and and do things and stuff like that. Just like  you can do with any file explorer, you can create    
00:07:28: new files here. So I can make like another file  MD. Then I could write stuff. Hey stuff. Okay.    
00:07:34: Um you can also delete files. So rightclick  and then you can you know delete, rename,    
00:07:38: open timeline. You can do all sorts of random  stuff with this. But I just want you to treat    
00:07:43: everything on the lefth hand side as basically  your average run-of-the-mill file explorer. And    
00:07:46: then the stuff in the middle you can almost treat  like like notepad on Windows or like Apple notes    
00:07:50: in the middle. Um it's just because in programming  typically specific character sequences are tied to    
00:07:56: specific pieces of functionality. You'll see here  that like it's quite colorful like link tags look    
00:08:00: a specific way. This thing looks another way. If  I go into I don't know this Tailwind config. You    
00:08:06: see we now have the color purple and and yellow.  Basically they just make it look like a freaking    
00:08:11: rainbow. And that's cool cuz why would I be  working on something gray dull and featureless    
00:08:15: if I could be working on a rainbow instead? On the  rightmost side of the file explorer, you also have    
00:08:19: the ability to like um have like a quick highle  overview of the file. So that's kind of neat.    
00:08:23: I don't know if you guys could tell super well  here, but this is basically like a I don't know,    
00:08:27: it's like a a level of abstraction up. It's like  a window that allows us to scroll up and down.    
00:08:30: This is useful if you're looking for specific  things within the file. Although I'll be honest,    
00:08:33: I mean like nowadays, as I mentioned, I don't  really use the editor too much. And then up at the    
00:08:37: very top right hand corner, this is relevant if  you run any markdown files. If you click on this    
00:08:42: little button here, and by the way, most files  nowadays where you communicate with the model    
00:08:46: are going to be markdown files. Instead of it  looking kind of like dull and drab and you know,    
00:08:51: all this tiny text here, if you click on this  little button here, you'll actually open what's    
00:08:54: called a markdown preview. And then this markdown  preview will actually like make the text the way    
00:08:57: that it's supposed to look. So every time in  markdown, you have this little like number    
00:09:01: sign. What that actually refers to is that refers  to like a heading. And that's like the really big    
00:09:04: heading. If you have two, then that's a little  smaller heading. Then you have like text down    
00:09:08: here. So, most of the time, this is what you guys  are probably more familiar with. And to be honest,    
00:09:11: a lot of the time, if I just want to like take  all this dense stuff and then make it look a lot    
00:09:15: better, I'll go back to um my browser and then  I'll go to Google Docs. And then what I'll do    
00:09:20: is I'll actually paste this in. And then I'll  just change the text color to black. And then    
00:09:25: now everything here just looks like a big Google  doc. And I can read through it. And you know,    
00:09:28: I see like orders of um hierarchy and and stuff  like that. Not super important, but good way for    
00:09:32: you to like quickly take a look at prompts.  Okay, a couple of quick hotkeys here. Um,    
00:09:36: you can go forward just uh with this. You can go  backward with this. It's the exact same hotkeys    
00:09:40: that you use on um, you know, Windows or Mac to  like change tabs and stuff cuz basically what    
00:09:45: we're doing is we're just changing tabs. So,  if you're alt tabbing, you can alt tab through    
00:09:49: files like that. Super easy. And then you'll also  notice that there's just different types of files    
00:09:53: depending on what you're looking at. So, we talked  about markdown. This is a JSX. This is a CSS. This    
00:09:58: one over here though is actually a Gemini specific  one called walkthrough where it runs you through    
00:10:01: what the AI uh basically wants to do next. It  basically teaches you what it's doing. It's kind    
00:10:06: of neat and we're going to cover a lot more about  that later. But there's cool features like review,    
00:10:10: you could submit a comment, you could ask the  model for stuff and and download it as well which    
00:10:14: is kind of cool. Okay. And then finally just to  round out our AD20 on the right hand side we have    
00:10:18: the agent panel. And this is where I'm going to  spend most of my time because as mentioned this    
00:10:21: is where like AI does most things for us nowadays.  And we don't actually have to worry too much about    
00:10:25: the folders or the files or the code. What we  worry about is we just worry about specifying what    
00:10:29: we want in natural language. That's really what  like the vibe and vibe coding is all about. Okay.    
00:10:33: So, starting at the very top right hand corner,  if you want to start a new conversation, you just    
00:10:37: click this button. Now, we don't actually have any  text in our current conversation, so I can't start    
00:10:41: a new one. If I just write a, then I can click  this. Now, I'm in a new conversation. You'll    
00:10:45: also see down here that our history is populated.  And we can see 4 seconds ago, I had the letter A.    
00:10:50: Uh 24 hours ago, I asked some questions about  background images loading and stuff like that.    
00:10:53: really quick and easy way to create a new convo.  Um, you can obviously also just use hotkeys. So,    
00:10:58: command shift L will just automatically pop one up  and then, you know, every time you type, you can    
00:11:02: just make a new one and so on and so forth. Over  here are past conversations and so this will have    
00:11:07: uh basically a list of every conversation I've  ever had with AI. So, refining prompt for website    
00:11:11: generation 47 minutes ago. This is something that  I produced. Uh, when you click on that button,    
00:11:16: it'll say, "Hey, should we open in the current  window? Should we open in a new workspace?" So,    
00:11:19: what I'm going to do is I'm going to open in a  new workspace. It'll open up a new folder. And    
00:11:22: now it'll actually pull through my conversation as  well as the specific file that I had open when I    
00:11:26: did this. In my case, I was preparing a website  uh prompt basically a website generator prompt    
00:11:31: for this course uh which is right over here and I  was just having a back and forth for that. On the    
00:11:36: right hand side, we also have additional options  which allows us to do things like customize and    
00:11:39: MCP servers. Customizations are pretty cool.  Basically what you can do is you can define    
00:11:43: highle rules that guide the behavior of your AI  model. So, we're going to get into ways to steer    
00:11:48: things as I mentioned in the um sort of outline of  this course, but rules are really quick and easy    
00:11:52: ways that you can either set globally or within  the specific folder that you're operating, okay,    
00:11:57: to either control all instances of every line of  code or every conversation you have with Gemini    
00:12:04: or you can do that within a fold. So, you can  see here I technically already have a rule and    
00:12:08: it's called cinematic landing page builder  role. Your role is to act as a world-class    
00:12:12: senior creative technologist and lead front-end  engineer. you build highfidelity cinematic one    
00:12:16: to one pixel perfect landing pages. So this is  sort of like my highle um workspace rule that    
00:12:21: helps constrain the behavior of the model.  And you know this is actually pretty long,    
00:12:25: right? Like you could scroll down this for quite  a while. Um this is one of the reasons why I have    
00:12:28: pretty good vibecoded quality because I basically  put in a lot of style guide and highle information    
00:12:33: to help the model you know make quick decisions on  the fly without having to ask me for stuff. So you    
00:12:37: can define that both globally or a workspace. If  you just click the button then you can enter the    
00:12:41: information right over here. You click this button  and you can just um create your new rule. So maybe    
00:12:45: I want it to be called design guide. Oh, and you  have to use um you know hyphens in between each.    
00:12:50: You can't actually have any spaces. I'm just using  a little voice transcription tool. In this case,    
00:12:54: this one's called whisper flow. Um and then you  know you can basically specify an activation mode.    
00:12:59: Is it always on? Is it manual? Do I set it? Do uh  I leave it up to the model or do I do glob which    
00:13:06: applies specifically to files that match some file  pattern? In practice, I never use glob. I never    
00:13:11: use model decision. I never use manual. I always  use always on. So in this case, I'd say, hey,    
00:13:15: when you design websites, I want you to stick to a  minimalistic, sleek aesthetic. I want you to build    
00:13:19: things that are significantly closer in design to,  let's say, the Apple homepage than anything else.    
00:13:24: And I can populate that. If I wanted to run this,  I would just save this file. And as you can see,    
00:13:27: we've now added that as a rule. Now, I  don't actually want this rule here. Um,    
00:13:31: so what I'm going to do next is I'm just going  to delete this. The way you do so is every time    
00:13:35: you generate a rule, it's now created inside of  agent/ruules folder. So if you want to delete it,    
00:13:40: you just delete that. And now we're back to just  that one rule which is called the gemini.mmd. This    
00:13:44: gemini.mmd is basically just the parent rule that  always applies if you have a file called capital    
00:13:49: gemini.mmd in your workspace. All Gemini models  will just always take that as a rule. Um multiple    
00:13:54: different ways to define rules and stuff like  that as well. Not super important. There's also    
00:13:58: workflows which I think are probably nowadays  better understood as skills where basically    
00:14:02: similarly to rules you can define behaviors or  specific sequences of steps that you want your    
00:14:06: agent to take every single time. So these can  be pretty cool and you can again define them    
00:14:10: as global or workspace. So I could call this I  don't know code review here. I could say this    
00:14:15: workflow defines a code review process that goes  through the code and then maximizes the security    
00:14:20: of the vibe coded app. To start with, I want you  to reference this document. This document includes    
00:14:24: information about all sorts of high ROI security  practices for vibe coded apps. After you're done,    
00:14:29: I'd like you to go through each of these step  by step. Uh make small incremental changes to    
00:14:33: the codebase. Try not to, you know, do everything  everywhere all at once. and then verify with me    
00:14:38: at the end that it works by asking me to test  it before we push to production or anything    
00:14:42: like that. And so, you know, in this case, what  I've done is I've I've built some quick little    
00:14:48: rule here. And then maybe over here is where I  put like my security stuff. And now, you know,    
00:14:53: what I have is I have a quick little workflow  that after I'm done building my vibe coded app,    
00:14:57: I can just say, "Hey, I want you to run the code-  review workflow." and then it'll just go through    
00:15:01: this standard operating procedure, the sequence  of steps, more similar to like the way that a    
00:15:06: business would operate with checklist style  tasks. Again, I don't actually want this. Um,    
00:15:10: so what I'm going to do is I'm going to go  back here. I'm just going to delete this.    
00:15:12: That'll delete the code review customization.  Now, there's also some other customizations    
00:15:16: like MCP servers. I'm going to talk a little bit  more about MCP servers later. But the way I want    
00:15:20: you to treat MCP servers for now is basically  it's just a way to define workflows. It's just    
00:15:25: um workflows that somebody else did for you.  And so these MCP servers essentially allow    
00:15:29: you to connect to different tools and then run  standardized workflows on those tools. So for    
00:15:33: instance, if I wanted to use a server like a  PostgresSQL, there's a pre-existing workflow    
00:15:38: bundle here called CloudSQL for PostgrSQL. This  is a specific database language and specific    
00:15:44: type of database. This basically just defines  a checklist series of steps that the model will    
00:15:48: always do to communicate with us that I don't  know can translate my natural language queries    
00:15:52: into that if I wanted to. Same thing with Looker.  Same thing with GitHub, Neon, Stripe. Basically,    
00:15:58: these just allow us to communicate with different  tools in a very predictable way, which as I'm sure    
00:16:02: you can imagine if you're building high quality  vibe coded apps can be pretty useful. That said,    
00:16:06: there are also some downsides to MCP server.  So, I don't really use them a lot in practice,    
00:16:09: and we'll cover all that stuff later. For now,  I don't want to overwhelm you. Okay, next up, we    
00:16:14: have the title of the current folder. As you can  see, this one's just called website-builder, not    
00:16:17: rocket science. Then, we have the ability to add  some context here to our prompt. So, if I wanted    
00:16:21: to, I could add media. I could add mentions. And  I could also add workflows. Remember the little    
00:16:25: workflow that I put together earlier and then  deleted? If I had workflows, every time I wrote    
00:16:29: slash, I would automatically be able to add them  here. What's cool though is you can also mention,    
00:16:32: and when you type mention or or you just press at,  then you can actually attach files, directories,    
00:16:37: uh, code context items, rules, even terminals,  pre-existing conversations, and then also MCP    
00:16:42: servers into the context. And the reason why this  is valuable is because, you know, I could just    
00:16:47: copy everything in this file and paste it in, or I  could just say, "Hey, I want you to reference this    
00:16:51: gemini.md." And then it would do the same thing,  but as you can see, I'm not really polluting this    
00:16:54: big window. It's very clear and clean. After that,  you have the mode. Now, there are two conversation    
00:16:59: modes available to Gemini 3.1 Pro right now.  There's planning and fast. This may change at    
00:17:03: a certain point in time, but for now, this is more  than enough. In general, you always want to start    
00:17:07: in planning anytime you're designing or building a  new feature. Planning is good because it basically    
00:17:11: allows the model well almost forces the model  to do a lot of thinking before it actually like    
00:17:15: you know stretches its fingers out in the world  and starts manipulating files and stuff. It then    
00:17:19: actually presents you a workflow and says hey this  is what I'm planning on doing. Are you sure you    
00:17:24: want me to do this? And then you can set your own  behavior to either auto approve which is just have    
00:17:28: it run on its own um decided plan or you could  actually stop it and say hey I didn't really like    
00:17:33: what you did here. I want to make a minor change.  Next up you also have fast. fast just allows it    
00:17:38: to execute things directly and go really quickly.  And so this is actually pretty useful if you're    
00:17:42: doing quick one-off tasks. Hey, I want you to  change this file format to this file format. Hey,    
00:17:46: I want you to change this markdown file to a txt  file. Hey, I want you to, I don't know, refactor    
00:17:50: XYZ really quickly with this um, you know, brief  little variable in mind or something like that.    
00:17:55: Okay, so in general, I always start with planning  and then at the end um, you know, when I'm just    
00:17:58: doing one-off tasks and stuff, if I need to, I'll  use fast. Underneath, we have the model picker,    
00:18:03: which I've already covered. includes the specific  one you want to pick and choose and actually have    
00:18:07: in communication with. Remember how earlier I  said the agent is just like a wrapper for the    
00:18:12: um specific model you're talking to. Well, this  is how that works, right? This chat window isn't    
00:18:16: communicating with all models right now. It's just  communicating with one, but I can hot swap them    
00:18:20: anytime. Instead of Gemini 3.1 Pro high, I could  easily choose Gemini 3.1 Pro Low. And you'll find    
00:18:24: that every model has different pros and cons.  If you want a quick example of pros and cons,    
00:18:29: just go to Google and type Gemini 3.1 Pro High  versus Low. And what you'll do is you'll have um    
00:18:34: you know basically benchmarks showing you how high  quality the models are at different things. Uh    
00:18:39: use usually some sort of like graph here that runs  through hey you know highs 44.4% on this benchmark    
00:18:45: lows 39.8% on this other benchmark and so on and  so forth. I will say in general I tend to just use    
00:18:50: like the best models currently available and to be  honest that's usually the most recent model that    
00:18:54: has been pushed out by the big three companies  right now which tend to be Google um OpenAI and    
00:18:59: then Anthropic. Uh I was all about you know claude  uh Opus 4.6. six just last week. Um, now you know,    
00:19:04: Gemini 3.1 Pro High seems to be very, very good  at like design specific applications. So, what    
00:19:09: I'm doing is I'm passing off my design stuff to  Gemini 3.1 Pro High. Then I have Opus 4.6. Kind of    
00:19:14: clean stuff up on the back end. Yeah, this is how  you select through a bunch of different models.    
00:19:17: And as you can see, it's just like Lego blocks.  They're hot swappable. Gemini 3 Flash is super    
00:19:21: super quick. Sauna 4.6 is a really long context  window. A lot of these have pros and cons. Um,    
00:19:26: nobody really uses this in practice though. Okay.  And then finally, um you can click this button to    
00:19:30: replace your texting with basically talking.  So what I'm doing right now is I'm just having    
00:19:34: a normal conversation with it. When I press  this button, um you know, and then I I send it,    
00:19:40: Gemini has a built-in uh mechanism to just  transcribe what I just said and then turn that    
00:19:44: into text. The reason why this is valuable and why  you're seeing a lot of people use voice dictation    
00:19:48: tools nowadays, it's because on average, people  speak much faster than they write. If I'm writing    
00:19:51: at 50 to 80 words per minute, I can speak at like  150 to 200 words per minute. So, it's obviously    
00:19:56: a lot faster and a lot quicker. Now that I've  actually sent a message, you could see how the    
00:20:00: UX has changed a little bit. We now have a thought  little tab. This basically runs you through the    
00:20:04: internal thoughts of the model. The reason why  they make this present and visible to you is    
00:20:08: because if it's making any sort of like egregious  error, you can just quickly dive in and say,    
00:20:12: "Okay, so why did it make that error?" This gives  you some transparency, some accountability, and    
00:20:16: then you can, I don't know, adjust your feature  prompting style to be better to solve that issue.    
00:20:20: It's also good because sometimes the models are  lazy and they don't really respond because they're    
00:20:24: trying to conserve tokens or whatever the heck.  This is a quick and easy way to like make sure    
00:20:27: that the internal thing is not uh the user asked  me this question. I don't really want to spend a    
00:20:31: lot of tokens. So I've decided to give them a much  simpler answer. This is how you can actually just    
00:20:35: figure out what's going on under the hood. The  text that is not sort of this darker thinking    
00:20:39: tab is uh the response. And so in this case to  get started on building a cinematic landing page,    
00:20:43: please please answer the following questions. The  reason why it's running me through that is because    
00:20:46: I've defined that as basically my highle workflow  rule uh or sorry just rule in gemini.mmd. I'm    
00:20:53: saying hey you know I want you to act as a world  class senior creative technologist when the user    
00:20:57: asks something immediately asked exactly these  questions and then it's asking me these questions.    
00:21:02: So basically this is taking everything from that  initial configuration file and then despite the    
00:21:06: fact that my voice message said nothing of any  import uh it just injected that up at the very top    
00:21:11: and now it's trying to you know do my my higher  level rule instructions. Okay so underneath you    
00:21:15: have good or bad. Uh this is just a way that  you can help train the Gemini models on like    
00:21:19: hey I like this response. Hey I don't like this  response. I never really use that in practice.    
00:21:23: And now you can see that there's also a bunch of  additional tabs that I've opened up here. On the    
00:21:26: lefth hand side there's changes overview. if your  request changed any files um you know on your work    
00:21:32: inside of your folder that's actually going to pop  up right here and then you can just take a look at    
00:21:35: them in practice nowadays basically nobody takes  a look at these they're just like oh yeah man you    
00:21:39: figure it out you got it uh next up is terminal  so sometimes Gemini or other models will launch    
00:21:44: terminal instances for you can actually see the  background processes running in that tab artifacts    
00:21:48: or files that are part of the conversation so you  know I added this gemini.md file for instance I    
00:21:53: mentioned it right and then over here we have  the browser and this is kind of neat you can    
00:21:57: actually launch a browser are inside of uh Gemini  nowadays. Um this browser, you know, I'm not going    
00:22:01: to say it's like the highest quality browser on  planet Earth, but it can be pretty cool. If I go    
00:22:05: over here, you could see um we're going to keep  it. We're now opened on the anti-gravity uh docs    
00:22:12: page for browser. And so, you know how some things  in life you can only really do on a browser? You    
00:22:16: can't just do everything via API or you can't  do everything like through a chat window. This    
00:22:20: is basically a quick and easy way that allows you  to do that. And I'm not going to say that this is    
00:22:23: like super super valuable or really really  all that helpful right now, but you know,    
00:22:27: it's pretty cool and obviously they're trying  to push more towards browser automation. Okay,    
00:22:31: so hopefully you guys now know everything about  how to use anti-gravity and then the Gemini series    
00:22:35: of models. What I want to do next is I just want  to give you guys a quick run through of Claude    
00:22:38: Code because we're also going to be using that.  Basically, the Claude large language model lives    
00:22:42: within the Claude code chat software which we also  wrap inside of anti-gravity. And so just the exact    
00:22:47: same thing that we just did with the agent chat,  we can do with the Claude code chat as well. So    
00:22:52: what I'm going to do next is I'm actually going  to exit out of this view. Okay? And then I'm going    
00:22:55: to sign up to Claude. Now, in order to use Claude  Code, you do need an account. So what you have to    
00:22:58: do is you have to go over to claude.ai. That'll  take you to a page that looks like this. And    
00:23:02: then you can enter some information here and then  continue with your email. I don't actually have an    
00:23:07: email called asf asdf asdfgmail.com. If I would,  I'd probably be a billionaire. Um, basically    
00:23:12: what'll happen is they'll send you a link over to  your email. You can click on that link and then    
00:23:16: it'll sign you in. From there, you have a brief  little onboarding that you need to fill out and    
00:23:19: then that'll take you to the most important part,  which is the pricing. Now, the way that the plans    
00:23:24: work for Claude Code is you need to select between  the pro or the max plan. Pro plan is $17 a month    
00:23:31: right now. The max plan starts at 100 and it can  be significantly higher. Unfortunately, right now    
00:23:36: they don't allow you to use quad code within a  free plan. That's just part of the limitations    
00:23:40: of using the cloud family of models and it's just  always a trade-off with these things, right? Like    
00:23:44: if you think about it, Gemini allows you to use  things for free. Uh Google, sorry, allows you    
00:23:48: to use Gemini for free despite not having to pay  any money, but then you have quite limited usage.    
00:23:52: Whereas Cloud Code requires you to sort of put  a certain minimum amount of money, in this case    
00:23:56: 17 bucks a month in order to use it, but then it  tends to be a lot better at specific applications.    
00:24:00: So you don't have to necessarily sign up for  this, but if you did want to sign up for it,    
00:24:04: if you wanted to use um you know, Vibe Coding in  a way that I'm going to show you in this course,    
00:24:08: you would have to have some sort of subscription  ongoing. I don't want to push you guys to sign up    
00:24:12: to anything. I'm not affiliated with, you know,  Anthropic. I'm not affiliated with Claude Code.    
00:24:16: I'm not pushing any specific product on you in  this course. I will just say that I, as a business    
00:24:20: owner, uh, you know, I get a tremendous return on  investment from this stuff. Just a few months ago,    
00:24:25: in order to hire a developer at the level of Cloud  Code or, you know, Gemini with an anti-gravity,    
00:24:30: I would have had to spend 20,000 to $30,000 a  month. I would have had to go down to Silicon    
00:24:34: Valley and find like a super cracked dev and then  hire them on my team. And those people would work    
00:24:39: eight hours a day max. Um, this stuff does 24  hours a day. This stuff you can plug in APIs. It's    
00:24:44: totally automatable. This stuff gets smarter every  day, week or month. And so this is really like the    
00:24:48: technology of the future. Um, I probably get at  least 100x ROI on the money that I spend and I'm    
00:24:52: spending like $200 a month, right? So that's  that for Claude. Once you're done signing up,    
00:24:57: um, what'll happen is we can go back to  anti-gravity, go to this bottom lefth hand    
00:25:01: tab here called extensions, and then click cloud  code for VS Code. Now what this is is just like    
00:25:06: the agent chat on the right hand side is the way  to communicate with the Gemini series of models.    
00:25:10: This is built by Google. Okay, this is built by  Enthropic and it's just a little extension chat    
00:25:14: that you can put into in gravity. And so what I've  done here is I've already installed it, but you'll    
00:25:18: have to install it. When you get it installed,  what you can do is you can click on this little    
00:25:21: button in the top right hand corner. That'll open  up a clawed code window just like this. Okay. And    
00:25:26: as you see, very similar UX to what we had earlier  with the agent chat. Just this time now it's    
00:25:30: sort of like cute and orange and there's a little  space invader over here. So really quickly to run    
00:25:34: you through it, if this is the very first time  you've done this, you do need to go /lo. Okay,    
00:25:39: that'll allow you to log in to your Claude AAS  subscription which you just put together a moment    
00:25:42: ago. You can also sign in through the anthropic  console or these other thirdparty providers. Most    
00:25:46: people for cost purposes are going to choose this  as the cheapest one. After that, you just write    
00:25:50: a message like, "Hey, what's up?" Now, just like  you were communicating a moment ago with Gemini,    
00:25:54: now what we're doing is we're communicating  with a different model. And you can find out    
00:25:58: which model by clicking the bottom right hand  corner and then going to switch model. And so,    
00:26:01: right now, I'm using this default recommended  one, Opus 4.6, most capable for complex work.    
00:26:06: There's also another one, Opus 1 million context.  There's Sonnet, Sonnet 1 million context, Haiku,    
00:26:11: and then uh some custom 4.6 model down here.  I think if you guys are keen viewers, you'll    
00:26:16: probably say, "Well, wait, Nick, didn't we have  the ability to communicate with the Claude series    
00:26:20: of models down here?" And the answer to that is  yes. Uh for whatever reason, I guess just because    
00:26:24: of the nature of their business arrangement, um  inside of the agent chat and anti-gravity, Google    
00:26:29: actually allows you to communicate with the Claude  series of models as well. But in my experience,    
00:26:32: and I don't know if this is because they're  trying to handicap it or something like that,    
00:26:35: but like in my experience, it just doesn't work  as well inside of that agent chat. And the UX is    
00:26:39: actually much better within the Claude chat.  So, what I typically do is I just communicate    
00:26:42: with the Cloud series of models in Claude Code  and then I communicate with the Gemini series    
00:26:46: of models in their built-in anti-gravity agent  chat. And that works really well for me. Um, also    
00:26:51: it doesn't it like simplifies my payments. So, I'm  like paying one provider for one sort of model and    
00:26:55: then another provider for another sort of model.  Obviously, your mileage may vary with that. And    
00:26:58: maybe it's just the vibes and vibe coding that are  getting to me. I much prefer to communicate with    
00:27:01: Claude in the Claude code extension. Anyway,  hopefully it's pretty clear. Same thing. You    
00:27:06: have little text windows, right? This is its  reply down over here. Just like in um Gemini,    
00:27:10: we had a few modes like planning and so on and so  forth. In this one, we have um ask for edits, edit    
00:27:15: automatically, plan mode, and then also bypass  permissions. Uh most Gemini is automatically    
00:27:20: set to bypass permissions now. So, you don't  actually have to like manually set it. Ask    
00:27:23: before edit is just where if you want to change  the pre-existing files on the lefth hand side,    
00:27:27: you need to just like verify with me first. So, if  I say change readme.md to include a snippet about    
00:27:35: Nick Sarif, okay? And then I ask it to do this,  what it'll have to do is it'll have to go find    
00:27:40: some information about Nick Sarif. Then it'll have  to read it. Then it'll have to make some proposed    
00:27:43: adjustments. But do you see how now we have this  little panel that's popping up saying, "Hey, do    
00:27:47: you want to make this edit?" So I could say yes.  I could allow all edits this session. And I could    
00:27:51: say no. Or I could tell Claude what to do instead.  I'm just going to escape out of it. That's how Ask    
00:27:54: Before edits works. Most people are going to use  edit automatically because then you can change    
00:27:58: pre-existing files without actually having to like  do that little, you know, hey, should I change    
00:28:02: this? Uh because nowadays these models just move  so much faster than human beings ever can. There's    
00:28:06: just no need to. And then finally, you have plan  mode, which is similar. It just does a lot of    
00:28:10: thinking. Doesn't actually do anything until  it presents the plan to you. And then finally,    
00:28:13: a bypass permissions, which is uh you know my  yolo mode where I just say do it again and then    
00:28:18: it's not going to ask me for anything. It's just  actually going to go edit the file. Right. So    
00:28:21: now it says built by Nick Sarif. I'm a software  engineer and automation consultant specializing    
00:28:25: in AI powered tools and web applications. Thanks  so much. The software engineering title has never    
00:28:30: been easier to get. Okay, everything else you  are going to learn by doing. Hopefully, this    
00:28:33: has been a comprehensive setup and you guys now  know how anti-gravity works in conjunction with    
00:28:37: the agent chat and then the Gemini 3.1 Pro series  of models. You also know how anti-gravity works in    
00:28:42: conjunction with Claude Code and then the Claude  series of models. And you also understand the    
00:28:47: interface, at least the 8020 of the interface that  we could use to build our very first project. Next    
00:28:51: up, what we're going to do is we're going to build  a highquality, simple portfolio site in just a few    
00:28:56: minutes that I'm then going to push live onto the  internet. I'm doing this because I want to show    
00:29:00: you guys how simple and easy it is to actually  develop like actual web applications and web    
00:29:04: properties with Gemini 3.1 Pro High. And I'm also  going to include all the prompts and everything    
00:29:08: you need to do the same thing on your end down  below in the description. So, just check that free    
00:29:12: folder out. Okay, so the simplest and easiest way  that I have found to set up websites with Gemini    
00:29:17: 3.1 Pro high is you literally just provide it a  simple copy paste prompt which I have down below    
00:29:24: in the description and you guys can use as your  end all be all or you guys could use as a base to    
00:29:28: make your own prompt on top of. Okay, store that  as a gemini.md and then just fire it off. So, what    
00:29:34: I've done here is I basically open up a new folder  called website builder-demo with the gemini.mmd    
00:29:39: with this big long prompt. And I'll run through  the prompt in a second while I'm actually creating    
00:29:42: the website. But then I say build me a website.  Now, what this does is this forces the model to    
00:29:50: act as a world-class senior creative technologist  and lead front-end engineer. Basically, we're    
00:29:55: saying you build highfidelity cinematic 1:1 pixel  perfect landing pages. Every site you produce    
00:30:00: should feel like a digital instrument. You must  eradicate generic AI patterns, including typical    
00:30:05: structural layouts like a standard hero, three  column features, and CTA. Every site you build    
00:30:09: will use a vastly different structural layout,  typographic scaling, and interactive paradigm    
00:30:13: based on the chosen archetype and structural  typology. Kind of a mouthful, right? Now,    
00:30:18: I'm not going to run through all the rest of  these, but basically, to make a long story short,    
00:30:21: this section here is just guiding it through a  brief little Q&A so that you can choose, you know,    
00:30:26: the highest quality website design for you. This  over here has a bunch of different aesthetic    
00:30:30: archetypes depending on what you're looking at  which we can select. Down below we have some    
00:30:35: structural typologies including bento grids,  split screens, infinite horizontal structures,    
00:30:40: linear narratives, and then application shell  which is kind of neat. Then we have some brief    
00:30:45: little rules about different tools to use just  based off of my own understanding of tooling. Um    
00:30:50: as well as um some double-checking protocol down  here. And on the right hand side, as you can see,    
00:30:55: after I entered that little uh message, it's now  asking me for the brand name, the core thesis, um    
00:31:00: aesthetic archetype, structural typologies, three  core pillars, and then the ultimate conversion    
00:31:04: goal. So, all I'm going to do now is I'm going  to close out of this. Okay. Make this way way    
00:31:09: bigger just so I could see like most of it. And  then I'm just going to enter my information. So,    
00:31:15: uh my brand name, just so people are all on  the same page as me, is called Leftclick. And    
00:31:19: basically what we are to zoom way in there because  the website looks like trash right now is we're    
00:31:23: the definitive AI growth partner for fastmoving  B2B companies. This is a website that I actually    
00:31:28: had a real developer like I paid somebody money  to put this together for me cuz I didn't have    
00:31:32: the time. And the whole idea is we're like an  AI automation boutique shop that helps people    
00:31:36: generate revenue using high growth systems. This  is typically stuff like cold email systems. It's    
00:31:41: stuff like speed to lead systems for paid ads  and so on and so forth. So it's pretty neat,    
00:31:45: right? It's pretty sexy. We got the cool photo  with Hormosi and Ovens over here. That's uh won me    
00:31:49: some goodwill for sure. Basically, what I want to  do is I just want to have AI try and generate uh    
00:31:53: this website instead of me. And then I just want  to compare and contrast the results. You'll see    
00:31:57: there's some mild things here like there's a cool  little animation that kind of follows my mouse    
00:32:00: around. That's kind of neat, right? Obviously  the text and the fonts and stuff that those are    
00:32:03: very sexy. So, do you think AI could do as good  of a job? Well, let's find out. I'm going to    
00:32:07: answer some information here. Brand name is called  Leftclick. We help high growth B2B companies scale    
00:32:14: revenue using outbound methods like cold email.  Two, pick best fit. Three, pick best fit. Four,    
00:32:23: super low cost of acquiring a customer. Um, AI  based personalization, which lets us attack at    
00:32:31: both scale and high levels of perceived  personalization. And then trusted vendor.    
00:32:41: We've worked with multi-billion dollar portfolio  companies. And then ultimate conversion goal is    
00:32:48: book a growth mapping call 30 men consult. Just  going to enter this information now. And I'm going    
00:32:56: to have the model do everything else for me. The  first thing that's going to pop up is this little    
00:33:00: thinking tab. And so what it's doing if I scroll  to the very top is it's focusing on refining the    
00:33:04: initial approach particularly concerning file  operations. It's prioritizing the use of more    
00:33:08: specific resources to manage and manipulate  information and so on and so forth. These are    
00:33:12: all of its own thoughts. And basically the way  that this works is at every step it's basically    
00:33:17: like another it's like another run. It basically  takes the prompt, it sends it, it does a bunch of    
00:33:21: thinking and then it sends that back to another  instance and says what's next over and over and    
00:33:25: over and over again. So that's what's happening  down over here at the bottom. Once you're done    
00:33:29: something that requires a fair amount of planning,  it'll actually pop open a planning uh section. And    
00:33:33: this basically runs through the files that were  edited as we saw earlier. Okay. the progress    
00:33:38: updates of that, some additional thinking, and  then finally a task list for what it's planning    
00:33:43: on doing. When tasks lists pop up, they pop up in  the middle over here. And as you can see, we have    
00:33:48: a leftclick dashboard landing page. It's going  to start by scaffolding the application using    
00:33:51: a particular library. Then it's going to install  dependencies, configure Tailwind, then it's going    
00:33:56: to build a core layout, and then, you know, go  through and do things in a really high quality    
00:34:00: way. Okay. So over here, what it's doing now is  it's running a terminal shell. Terminals just look    
00:34:05: like this. uh running background command. Anytime  you see anything like this with this little    
00:34:09: terminal icon, it's basically just doing the thing  in the terminal for you. Um you can actually just    
00:34:13: jump to that anytime you want to. And here you can  actually see like what it's communicating with,    
00:34:18: what it's doing. You can also see the artifacts.  So there's now two artifacts that it's created.    
00:34:22: One's called uh the task and the other's called  the implementation plan. Both of these here are    
00:34:26: basically just resources for you to make things a  little bit more visible. Like logically speaking,    
00:34:31: this model is doing a lot under the hood, right?  writing hundreds, thousands of of words basically    
00:34:35: every few seconds. Um I have no insight into this.  This is all just occurring behind the scenes.    
00:34:39: And so one of the big issues right now with vibe  coded apps is there's just no interpretability or    
00:34:43: accountability about like what the model's doing  underneath um you know behind everything. Well,    
00:34:47: this implementation plan, the whole idea is it  just like shows you behind the scenes what's going    
00:34:51: on. Well, it's decided on some AR aesthetic and  typology decisions like um B2B SAS dense. We want    
00:34:57: gunmetal safety orange steel. The typography is  going to be IBM Plex suns, IBM Plex mono, right?    
00:35:03: These different fonts and so on and so forth. The  application shell is going to look like this. The    
00:35:07: proposed changes are going to look like that. As  you saw a moment ago, we just added a file to our    
00:35:11: folder called leftclick- dashboard. If I give this  button a click, you'll see we now have a bunch    
00:35:15: of files that it's written. The model just wrote  all of this while I was just talking to you guys,    
00:35:19: and it's currently writing more, right? Which is  pretty neat. I don't know how any of this stuff    
00:35:23: works, to be honest. And I don't need to anymore.  I just vibe code. If I like it, fantastic. If not,    
00:35:28: I I'll ask for changes and I'll show you guys  what that loop looks like in a second. But yeah,    
00:35:32: I mean, you know, as you guys see, a big chunk  of this is just shephering AI and making sure    
00:35:36: that it's operating in in the right direction, the  direction that you want, as well as looking over    
00:35:40: things like implementation plans, intermediary  files that are created, and stuff like that to    
00:35:44: just ensure that like everything is going the way  that you initially planned. What I'm going to do    
00:35:47: next is I'm going to go grab a sip of water and  then I'll come back and hopefully this website    
00:35:50: will be ready to go. Okay. And here is the result.  Deploy the growth engine. We build growth systems    
00:35:55: for high- rev B2B agencies. Pure information  density, zero latency scaling. Wow, that's    
00:35:59: cool. Ooh, I love that button. That's really nice.  Uh, if you guys watched one of my recent videos on    
00:36:04: website design, this is the same approach. So,  I actually really like the background image as    
00:36:08: well. And so, I uh turned I basically gave it the  ability like the prompt that you guys are going to    
00:36:12: use if you copy the prompt and use it in your own.  Basically gave it the ability to like find stock    
00:36:17: image websites and stuff like that. And that's how  we end up with like this really nice clean like    
00:36:21: glass ISO form thing up at the top. then have some  cool uh you know sections here. Rapid revenue,    
00:36:28: lowest cost, proven vendor. That's really cool. We  focus on systemic growth. I like that. I like the    
00:36:32: blue this time. We got some cool animations and  stuff like that. You will find, you know, because    
00:36:37: we're using the same icon libraries and stuff,  some of these animations will be pretty similar.    
00:36:40: If you redo this five or six times, but yeah, I  mean like we just we just one-shoted a really cool    
00:36:45: website, right? Um I'm just going to do the same  thing now a couple times just to show you guys    
00:36:48: that you don't have to stick just to the style.  You could do it in a bunch of different ones,    
00:36:51: too, if you wanted to. Okay. So, I'm just going  to open up a new folder here. And then I'm just    
00:36:54: going to make one website builder new. And then  I'm just going to operate inside of this folder.    
00:37:00: Okay. This is another rendition. So, I think this  is supposed to be like kind of earthy and healthy,    
00:37:05: which is why it says leftclick with the globe.  That is definitely not our brand, but what are    
00:37:09: you going to do? We're the architect of outbound  scale. We weaponize personalization by designing    
00:37:14: and deploying outbound architect for multi-billion  dollar portfolios. Kind of really like that    
00:37:18: section too much. Here's probably the weakest bit,  though. This stuff looks really cool. Like like I    
00:37:22: I really like this. Look at that. This looks nice  as well. You know, it's like something it came up    
00:37:27: with to showcase how we're verifying decision  maker profiles. We're trusted by the best. You    
00:37:31: know, we're architecting the revenue engine. So,  this is a great example for me to show you how    
00:37:34: you can change websites to make things better  or uh I don't know, you know, include sections    
00:37:38: that you want. So, what I have here is I have a  voice transcription tool. And you know what? I    
00:37:42: I I don't really like I don't know, I just don't  really like the layout here. I think personally    
00:37:46: the navbar is kind of an issue. So, what I'm  going to do is I'm going to go and I'm going    
00:37:50: to see if I could find a navbar from something  else and I'm just going to include a screenshot.  
00:37:57: So, like this navbar is actually really  cool, right? Like this this is clean. So,    
00:38:00: why don't I just take this navbar from my former  site? Okay. And then why don't I also just create    
00:38:06: a big voice prompt about all the things I want to  change. Hey, I have a navbar that I've supplied    
00:38:11: you with. I want you to make it that sort of  pill style because I think it's really high-end    
00:38:15: and clean. I don't need the Earth logo next to  left click. You can just use uh left click. Um,    
00:38:20: we should have buttons on the hero header. Also,  just make the hero header way bigger. I want it to    
00:38:24: be like huge. I want the content in there to  just pop and and explode. There's some weird    
00:38:29: numbers next to the hypereefficient acquisition  graph. Um, they're outside of the bounds of that    
00:38:34: little box. So, let's fix that up. Um, let's add  another section between scale without compromise    
00:38:40: and trusted by the best. That just talks about  me. My name is Nick Sarif. I run Leftclick. I've    
00:38:46: helped uh I don't know over 400 500,000 people  now use AI automation and then outbound methods    
00:38:53: to improve their lives and their businesses.  Um you can do a quick little Google about me as    
00:38:57: well if you want. And then down at the bottom, um  let's just add a footer in addition to the CTA so    
00:39:03: that it's just a little bit thicker and there's  more going on. Okay. And then I'm just going to    
00:39:06: dump that right here. And I'm just going to dump  that right here. So boom. Let's just remove that.    
00:39:12: Uh and then Yeah. And then I'm going to paste.  I guess I got to paste the image, right? Yeah.    
00:39:15: There you go. Cool. So, now that I've I pumped  all this stuff inside, um I'm just going to wait    
00:39:19: for it to finish the change and then I'm going to  double back. Meanwhile, I designed another website    
00:39:23: simultaneously uh for my content writing business.  Once I can copy. So, I like this. This is really    
00:39:28: clean. We then have that little pillow up top  with similar three card design here with some    
00:39:32: text. That's neat. Uh we also have these cards  that kind of come up. I really love these cards.    
00:39:36: These are really clean. And then down over here at  the bottom, we have some pricing. So, that's nice.    
00:39:42: Anyway, I just wanted to show you guys that while  we're waiting for the other leftclick site. Okay,    
00:39:45: and I can see it's saying the dev environment  is still running. So, I'm just going to copy    
00:39:49: this. Go back here and paste this in. And this  is way bigger. Look at that. This is huge. Nice.    
00:39:56: This is significantly better. I'd say that's  about the size that I wanted. And then up here,    
00:40:01: I think it's basically just one for one copied the  font. So, I'll just make one more change, which    
00:40:05: is to make sure that the style of this aligns with  the style of the site. Hey, just want to make sure    
00:40:08: the style of the pill navbar aligns with the rest  of the style of the site. Super clean. Nice job on    
00:40:15: everything else. Oh, and I'll supply you an image  that you could use. Um, for me, that will help.    
00:40:21: Really like the footer as well. It's pretty clean.  Let's make the green just a little bit darker,    
00:40:26: actually. Um, that's probably the last thing that  I want to change. Everything else here looks nice,    
00:40:30: though. Man, there's a lot of images of me out  there. We'll go large. What makes sense? Which    
00:40:34: one makes me not look like a seven-year-old?  probably this one. Let's just do that. So, I'll    
00:40:38: go here. I'm going to copy both the image and the  agent, I think. So, we'll just dump that in. So,    
00:40:45: I'm just going to copy this here, and then I'll  paste this in. Okay. And then, yeah, I should be    
00:40:51: good. And this is the finished product. Uh, what I  like is when I load it, there's that little bubble    
00:40:56: that goes out. You know, it expands at scale. Uh,  navbar is looking nice and clean. When we mouse    
00:41:00: over it, it's green. We have everything that I  asked for, including a picture of myself with    
00:41:04: like slightly darker green. And yeah, I mean,  like, you know, is this again going to win any    
00:41:08: awards? Probably not, especially since website  design is so commoditized these days. But now    
00:41:12: that I've showed you how to build sites, not just  one site, multiple sites, by the way, and probably    
00:41:16: a hundth of the time it would have taken you to  do uh websites the old school way. And I know    
00:41:20: that cuz I used to be a website designer. I used  to get paid for stuff like this. Melts my heart.    
00:41:24: Let me show you how to deploy it and how easy it  is to actually get a website like this up live on    
00:41:27: the internet uh with Vibe Coding. So, basically  what you're going to need is you're going to need    
00:41:31: a hosting provider. Now, I use Netifi because it's  simple. It's uh free for a couple of sites anyway,    
00:41:36: but you can also use Verscell and there are a  few other ones that are like this. Basically,    
00:41:40: what happens is they just take these sites that  we just put together. Okay, so whatever this,    
00:41:44: you know, link is here that I'm opening up  and then it takes the static files on your    
00:41:50: computer that you're currently accessing at  localhost 5173 and then it just like puts    
00:41:54: them on a web accessible URL. So, we're going to  have something like gentlebeaver uh.netlifi.com    
00:42:01: and we don't need to spend any money in order to  get that done. It's completely free for us. Um,    
00:42:05: it'll only cost us money if we require like a  custom URL like leftclick.ai for instance. So, I'm    
00:42:10: going to go over to netifi.com. Uh, and then I'm  going to, you know, if it's your first time there,    
00:42:15: sign up. I'm just going to click login. And I  have a bunch of different projects down over here,    
00:42:18: um, that I've hosted on Netlefi before, right?  So, make money with make reply robot leftclick    
00:42:23: go one second copies. You can see I've had quite  a few startups that have failed. Uh, and what I'm    
00:42:29: going to do now is I'm just going to click add new  project. And then uh you know I'm going to click    
00:42:34: deploy manually and then I can just drag my drop  drag and drop my project folder here. So simply    
00:42:41: put I'm going to go back to my um anti-gravity  and then what I want is I just want to rightclick    
00:42:45: this and say reveal and finder. I'm just going to  drag this whole file in. Okay, this whole thing.    
00:42:51: And what it's going to do is it's going to try  building and deploying. Now the probability this    
00:42:54: is going to work the very first go by the way is  pretty low actually because we're not giving it    
00:42:58: any additional settings or anything like that. So,  I mean, I'm going to look for it, but I doubt that    
00:43:02: it's actually going to oneshot it. If it does,  I'd be quite surprised. Wow, that's so funny. It    
00:43:06: just did. Uh, that's hilarious. I wasn't expecting  that. I was going to expect communicating with an    
00:43:10: agent to get it done. But anyway, yeah, we just  drag and drop the folder in Endearing Salyaki.    
00:43:14: And as you can see, our whole website is up. It's  actually up on the internet now. It's not up um,    
00:43:18: you know, where it was before. So, I'm just  going to open an incognito window just so    
00:43:21: you guys are 100% confident that it is on the  internet. I just accessed this. Why don't I um,    
00:43:26: load this up on my phone, too. endearing. Okay.  And I don't know if you guys could see this,    
00:43:32: but like that's the website. It's just on my  phone now. It's on a totally different um you    
00:43:37: know device. So yeah. Hey, I'm uh Nick Sarif and  today I'm going to show you how to get a website    
00:43:43: up on the internet in like a 45 seconds flat. Kind  of neat, huh? So this is more or less going to    
00:43:49: be the approach that I'm going to use to push all  of our apps to production just because, you know,    
00:43:52: I don't want us to have to spend a ton of money in  order to like actually run server infer and stuff    
00:43:55: like that. But yeah, in general, like you know,  if you're using a predictable library like this,    
00:43:59: it's pretty straightforward. Obviously, not every  single time is going to go that easily. And I'm    
00:44:03: going to show you guys what like more complex app  pushes look like. In general, what I do now is I    
00:44:07: just give my agent um an API key to the service  like Netlify. And then I just say, "Hey, you know,    
00:44:11: push this." And then it'll actually go through  and then do all of the work. Um but hopefully    
00:44:14: you guys see how easy it is to oneshot a website  with Gemini 3.1 Pro. Cool. So that's how to design    
00:44:20: a website. The issue with websites is websites  are really simple. They have no authentication.    
00:44:25: They have pretty cool UX as you can see and you  can get progressively more complicated as the    
00:44:29: models get smarter. Um, but there's no like actual  like like security or or data transmission that's    
00:44:34: really required, right? There's no interactivity.  So when we migrate from uh you know websites to    
00:44:41: apps, what we need to do is we need to understand  a couple things about security. And if we don't    
00:44:47: understand things about security, what'll end  up happening is the same thing that happened to    
00:44:50: some pretty popular libraries. You guys might be  familiar with like OpenClaw pretty recently or a    
00:44:54: Claudebot is what it was called before its 40th  rebrand. And the reason why part of the reason    
00:44:58: why I rebrand it so much is because there's just  so many security problems with it. Like people    
00:45:01: had 25,000 API keys leaked. API keys being like  basically the equivalent of like a password to    
00:45:06: a service. That's pretty important. Uh not to  mention, you know, API bills that were run up    
00:45:10: because hackers and stuff like that got access to  it. Or just like leaked data from users that use    
00:45:16: a specific thing. Never a good situation to be in.  So, I don't want to pretend like I can solve 100%    
00:45:21: of all security wos for you. I can't. The reality  is everything on planet Earth is hackable. It's    
00:45:26: just a question of how hackable. And the whole  idea of like 8020ing security is just to get    
00:45:32: your point get to a point where your app is less  hackable than the amount of effort that it would    
00:45:37: require to do it. And so almost like anybody  could theoretically break into anybody's house,    
00:45:43: but we don't because there's just like a little  bit more effort is required to like, I don't know,    
00:45:47: break my window than just walk into my front door.  Um, if you just like do some 8020, I don't know,    
00:45:52: put a fence in, have some camera outside your  front door or something, you'll eliminate the    
00:45:55: vast majority of like lowhanging fruit. Okay,  so I just want to run through the 8020 here. 80%    
00:46:01: of security problems in vibecoded apps will come  from five things. The first is exposed environment    
00:46:06: variables and API keys. The second is missing or  broken rowle security RLS on your database. The    
00:46:12: third is no server side validation which is  where you trust the front end for all of the    
00:46:16: validation steps. So verifying that a password  is a password and email is an email. Verifying    
00:46:20: your logic and your math and stuff like that. The  fourth is using outdated or hallucinated packages.    
00:46:25: Very important. And the fifth is not having what's  called proper authentication middleware. Now again    
00:46:30: you don't need to be a computer programmer to get  all this stuff. I'm going to explain it while we    
00:46:33: talk about it. What's really important is when  you actually go through and develop, you know,    
00:46:37: like a like a database for the most part, you just  like click the RLS button. Um, when you set up an    
00:46:43: app, you just tell Gemini 3.1 Pro High or, you  know, Claude, hey, you know, I don't want you    
00:46:48: to do server side validation. What's important  is that you just have it run through all of its    
00:46:52: packages afterwards or say, hey, do we have proper  authentication middleware on every page? You know,    
00:46:57: hey, are our environment variables and API keys  exposed publicly? And so I guess what I'm trying    
00:47:02: to get at is it's actually not that difficult to  like hit the AD20. You literally just like create    
00:47:05: one prompt and then you just feed it in as sort  of like a postbu workflow similar to what I showed    
00:47:10: you with the code review initially. So we can just  pass all the stuff in as a prompt and I'm going    
00:47:14: to do that and give you guys the prompt later and  it'll do pretty good. But obviously you know it's    
00:47:19: not perfect. No security ever is. This should just  allow you to launch apps without feeling like a    
00:47:22: fraud or needlessly endangering other people's  credentials. So let's chat about the first    
00:47:26: which is environment variables and then secret  management. For those of you guys that don't know,    
00:47:30: in computer programming, you typically have to  deal with the equivalent of a password. And so    
00:47:34: we call these passwords various things, tokens,  authentication credentials, environment variables,    
00:47:38: API keys, whatever. But they all sort of like come  to the same idea, which is that it is something    
00:47:43: that if uh a user has access to it, they can  typically access a bunch of features of their    
00:47:49: account and not somebody else's. And so the issue  with vibecoded apps is a lot of people with their    
00:47:55: agents actually hardcode authentication tokens  and secrets and environment variables into their    
00:48:02: code. And the way that I see it is this is kind of  like putting a sticky note with your password on    
00:48:06: the front of your monitor like you see in a lot of  like older school cubicles where it's like Gmail    
00:48:10: password 1 23123 Nick is super sexy.com whatever  and like anybody that walks by will see that and    
00:48:17: they will know your password. It's kind of like  that with um exposing environment variables and    
00:48:22: secrets inside of like a a front end. So, also  a lot of hackers will go through the website and    
00:48:28: app code and then just look for hard-coded  mentions of a specific string like next_pub    
00:48:32: uh you know whatever key or secret key or what and  that's a common string prefix. And what I mean by    
00:48:37: that is like you know if you load up the website  that we just had a moment ago which I don't    
00:48:40: actually remember the password I don't actually  remember the thing. So one sec. Yeah. Yeah. So,    
00:48:44: if you go through this website, we can actually  like right click, we can press inspect. And uh    
00:48:47: as we scroll through, we'll actually be able to  like command F different elements on the page. So,    
00:48:52: weaponize, for instance, is actually like  written in the code of the page. I guess you    
00:48:55: guys can't see cuz my fat head is in the way.  You guys see how down here I just command F    
00:48:59: weaponize and then we actually found the specific  segment. What if we do personalization? Right,    
00:49:03: that's there. How about initialize sequence when  I'm selecting this element? So what I mean by uh    
00:49:09: exposing your credentials is basically a lot of  the time somewhere on the front end people will    
00:49:13: write code so that when you click the map growth  button up here which we just found down over here    
00:49:18: um there'll be some additional thing like like  I don't know on click equal and I don't even    
00:49:24: remember like the actual function definition  for this but uh whatever you know fire my API    
00:49:29: key you know to whatever the website is and  then I actually like expose my API key which    
00:49:36: is right over here and so basically we is we just  want to avoid situations where I actually have,    
00:49:41: you know, on click fire my API key to this  location and here it is in plain text. Um,    
00:49:46: we also want to avoid the loca uh situation where  you have something like next public key equals    
00:49:52: whatever because if you have either of what I just  mentioned, somebody can just go on your website    
00:49:56: and then do the equivalent of like a command F  or control F and just type in like next public    
00:50:00: key and then they'll find something. It's really  dumb, but um you'd be surprised at how many really    
00:50:05: like high-profile libraries it's happened.  That's one of the issues that I've had with    
00:50:08: uh well anyway I'm not going to name any specific  names but yeah I've had some issues with some some    
00:50:12: recent vibe coded products because of this. So  what do we do instead? Well basically you put    
00:50:16: them in a file like av and then you just reference  them using imports or you tell the model like hey    
00:50:20: you know I want you to look in the specific place  for all of my API keys and credentials. And so if    
00:50:24: I show you guys a practical example just using  you know anti-gravity basically what you do is    
00:50:28: somewhere in the core of this you'd go env uh key  and then it would look like this and then no like    
00:50:36: um anthropic private key and then it would look  like this right and so basically what you do is    
00:50:42: you'd say hey what's my um enthropic key and uh  if you ever needed to use it to like construct    
00:50:49: something the model would instead of looking  through your your code base here and finding    
00:50:53: it like just written directly in a codebase.  It would do like a command f through the entire    
00:50:58: thing. It'd look for something like an enthropic  key or something like that and then it would go    
00:51:02: and it would actually find that it's 3 if4 and as  you can see it's analyzing the specific file to do    
00:51:06: so. So this is just like a programming convention.  Just keep all your passwords everything like that    
00:51:09: inside of av. Another benefit is you usually  don't push keys to like an a repository on the    
00:51:15: internet. Normally you just keep that locally on  your computer and then you give that to whatever    
00:51:18: like the app user or whatever to upload their own  keys. Pretty simple stuff. Not rocket science. The    
00:51:22: issue is just nobody actually does this. Nobody  actually asks their agent to make sure that all    
00:51:25: this stuff is done. The second is this idea of  rowle security. So um as you guys are going to    
00:51:29: see in the next project, we're going to use a  database and the database that we're going to    
00:51:32: use is going to called superbase. It's very very  popular with most vibe coder projects right now.    
00:51:36: And basically it's like the single most important  security feature on planet earth. But um you know    
00:51:40: these databases out there just don't enable this  by default because it's just not something that    
00:51:45: you know is enabled by default. I don't know.  I'm not a super in-depth computer programmer.    
00:51:49: but it changes a couple of things and some people  don't want to use a database like that. Basically,    
00:51:53: what this means is if you don't have this  feature enabled called RLS, anybody who has    
00:51:57: the Superbase URL and then what's called the anon  key, which is public by design, can read, write,    
00:52:01: and delete every single row in your database. And  that's just how Superbase works by default. And so    
00:52:05: some very popular vibe coded projects here did not  have level security. And basically anybody that    
00:52:09: signed up for them was given a key, sort of like a  password, and then they just use that password to    
00:52:14: search up all of the data about every other person  on it. And that led to like a massive massive,    
00:52:19: you know, issue. Try not to swear in these  videos, but it was a cluster. And uh, you know,    
00:52:24: that ended up with people's ability to delete  rows and databases, which was stupid. All RLS's.    
00:52:30: Basically says like, hey, user A can only see user  A's data. User B can only see user B's data. Like,    
00:52:36: obviously, it's not rocket science. Uh, but if you  just turn this on, you'll fix like 90% of errors.    
00:52:40: Okay, so 83% of exposed superbased databases  involved RLS misconfigurations. uh 83%. That    
00:52:46: means like only 17% of exposed superbase issues  were not related directly to this one thing that    
00:52:51: I'm telling you about that is basically just a  button. So we're just going to click enable and    
00:52:54: it'll be fine from now on. But just make sure to  know RLS is like the main lowhanging fruit. Next    
00:52:58: is something called serverside validation and um a  big problem with that is like you know how we just    
00:53:03: developed a website, right? Well, let's say on  their website there was some form and the form was    
00:53:07: um I don't know it was like a sign up form and it  said you know enter your email here and then enter    
00:53:11: your password and then let's say obviously in  order to implement any sort of sign up mechanism    
00:53:15: what we kind of have to do is we have to check to  see does the email already exists in our database    
00:53:18: and so what the server side thing what the front  end thing would do is it would basically say okay    
00:53:23: let's match the email to something in our database  well um when you do this sort of ser uh front-end    
00:53:28: validation where you validate like all of the  logic on your on your website um it's massive    
00:53:34: security risk because as you just saw a moment  ago, anybody can jump into the code of any website    
00:53:38: and then immediately change it. Like I could  go to google.com and then I could, you know,    
00:53:44: um hold command shift C or rightclick and then go  inspect element and then I could select anything I    
00:53:50: want on the page like this Google search button.  Then I could actually change it from uh I don't    
00:53:55: know this input class which is called Google  search and I could change it to nick search.    
00:54:01: And now I've just changed Google's website, right?  Accordingly, what I could also do is if there's    
00:54:05: some form here when I put my information in that  does my email or whatever, I could actually like    
00:54:10: have it go through a bunch of email addresses or  a bunch of passwords and then it would change the    
00:54:15: email and password that is being done the valid  accordingly. If I had a forum and this forum,    
00:54:20: you know, was like checking emails or checking  passwords or something, I could actually go    
00:54:23: through and then I could like see the data, see  the function that is actually doing the checking    
00:54:26: and then I could like look at it and I could be  like, wow. So the logic that that guy is using    
00:54:29: to check if passwords exist is he's checking to  see if it's over uh I don't know three characters    
00:54:34: and the maximum password length is 10 characters.  That means that uh you know I could theoretically    
00:54:39: enumerate through all passwords between three  and 10 characters and then I'd be able to find    
00:54:43: out anybody's password. You know it's like this  just gives attackers way too much information.    
00:54:47: Likewise, it also allows them to do things like,  you know, if uh a specific email address already    
00:54:52: exists in the database, what you could do is you  could use that same email address, but you could    
00:54:56: change the request that's being sent. You could  sign up a million different email addresses using    
00:55:00: some script. It's just not very scalable, I would  say. Um, and it's not very intelligent to do. So,    
00:55:06: instead, what we do is we actually do server side  validation. And what that means is like basically    
00:55:10: we have our site right over here. And our site in  general communicates with some server. And instead    
00:55:17: of doing all the validation over here, okay,  what we do is we say, "No, what I want to do    
00:55:23: is basically every time somebody tries to create  a new account, I'm not actually going to check    
00:55:26: on the site. What I'm going to do is I'm going to  send a request over to another backend somewhere,    
00:55:29: some server. The server is going to be much more  secure. And then because it's not on the site,    
00:55:34: nobody can like jump into the server and then  make minor changes to, you know, check out the    
00:55:38: logic and stuff like that. The only thing that  an attacker would actually ever see is just the    
00:55:42: fact that, oh, the site sent a request to the  server. uh but you know the server is like super    
00:55:46: password gated and you know requires specific  authentication. It's not anything that you know    
00:55:50: a person could actually use. So that's kind of  easy. You just ask your AI model, hey you know    
00:55:54: make sure to server side validate everything. Hey,  is anything here not being serverside validated?    
00:55:58: Okay, we'll make it serverside validated. And that  takes me to number four, which is dependency and    
00:56:01: package security. Um so when AI generates code,  sometimes it references packages that don't    
00:56:05: exist as in your AI will literally just make up  a package name. In case you guys didn't know what    
00:56:09: packages are. Basically inside of most folder  most coding uh projects nowadays you have like    
00:56:13: a node modules folder or something. And these are  all the services that this um repository is using    
00:56:19: in order to like build my website. And so it's  using witch word zod yto q prelude puny code    
00:56:26: react and so on and so forth. And so as you can  see like most websites nowadays are actually like    
00:56:30: very very heavily based on pre-existing libraries  that other people have built which kind of makes    
00:56:34: sense cuz like you know the longer the internet's  around the more people have built libraries that    
00:56:37: handle specific features and like obviously you're  going to want to just use somebody else's solution    
00:56:40: rather than build your own wheel and so that's  what a lot of people here are doing. Tailwind    
00:56:44: CSS for instance is a big design library that just  does a lot of the design for you. Arg parse just    
00:56:48: handles arguments and it's like a simple and easy  way to you know do bash scripts and functions.    
00:56:53: And so the issue is AI just came up with all  this stuff, right? But sometimes it'll actually    
00:56:58: download or it'll create a name of a module that  doesn't actually exist. So for whatever reason,    
00:57:04: I mean the training data or whatever or  just because of the way statistics works,    
00:57:08: maybe it'll create a folder here or uh whatever  called acorns and it'll try and download a library    
00:57:13: called Acorns and it turns out the library it  wanted to download is actually called Acorn, but    
00:57:17: instead it tries downloading Acorns. Now, people  that have done a lot of stat stats and stuff like    
00:57:21: that have like done a lot of this to see, you  know, what libraries the um AI models typically    
00:57:26: screw up on. And so, if it sees like, oh, you  know, this always says acorns instead of acorn,    
00:57:31: what it'll do is it'll actually these attackers  will go through and they'll make a big list of    
00:57:35: all these fake packages. And then they'll actually  create packages on the internet that correspond    
00:57:40: to these. And then these packages will just be  malware. So, instead of you downloading Acorn,    
00:57:45: now you're downloading Acorns. instead of it  being empty and being nothing because it's fake,    
00:57:49: now you're downloading somebody's package that  actually has like a string in it that says, "Hey,    
00:57:53: you know, when you download this package, I want  you to send all of the API keys to this service."    
00:57:57: They as like, "Oh, yeah, that makes sense. I'm  downloading this package. This package is legit.    
00:58:01: Let's do it." And then it sends all the API keys  to the service. So, I mean, like in practice, it's    
00:58:04: not anywhere near as big of a deal as just like  server side validation um issues or RLS, but yeah,    
00:58:10: I mean, like it can be a problem. Another issue  is AI will typically download like older versions    
00:58:14: and stuff like that if it's not constantly  instructed not to which means you might be    
00:58:18: pulling in a package with a security vulnerability  that you know actually got patched months or years    
00:58:22: ago. So in general the recommendation is ensure  you get the most updated packages as possible    
00:58:26: as opposed to like you know older ones. And then  finally this authentication middleware bit. Um in    
00:58:31: case you've ever accessed like an authenticated  service before typically the way that it works    
00:58:35: is you'll have some thing. So I'm just going to  open up a new thing and I'll go cloud.ai. Um,    
00:58:40: I don't know, slashnew. When I click on this, do  you notice how it just immediately jump me back    
00:58:45: to sluggin? Claw. New is like how you make a new  thread, right? Well, there are some apps out there    
00:58:51: where you'll pump in like claw.ai/ um I don't  know, maybe chat or something like that. Okay.    
00:58:58: And then basically you'll be able to act despite  the fact that you're not logged in, you'll be    
00:59:02: able to access chat if you just know that like  the URL is chat. Now obviously these guys are a    
00:59:07: major billion dollar maybe even trillion dollar  company by now. So every time I try and access    
00:59:11: this it immediately jumps you back to login. But  this is behavior that is handled by this thing    
00:59:15: called authentication middleware where basically  when you try and access routes that aren't your    
00:59:18: routes okay like settings and general and new and  and chat u it just knows that okay well you're not    
00:59:24: actually logged in so I can't show you that. I  need to get you back to the login page first.    
00:59:27: And so you know poor app design includes people  forgetting to put in authentication middleware um    
00:59:32: and then people have the ability to access pages  they shouldn't. And then sometimes it like allows    
00:59:36: them to manipulate things, rack up API usage uh  calls and stuff like that. So you can fix this by    
00:59:42: just ensuring middleware secures all routes. Okay,  so like I didn't want to make this little module    
00:59:46: here because it's boring as hell, but just know  that you know most people that build vibe coded    
00:59:51: apps will miss one of these five features and  then vibe coding in general just gets a really    
00:59:54: bad name because people just don't secure their  [ __ ] right? The reality is like nothing is 100%    
00:59:58: secure as I said, but if you just do these five  things and then um you know ask your AI models    
01:00:03: to fix them, uh you know, it'll do a reasonably  good job and I'd say about 80% of your security    
01:00:07: issues are going to be handled, especially that  rowle security thing. So what I've done is I've    
01:00:11: actually gone through and I've created a massive  prompt for all of you guys that you can use    
01:00:14: right over here. It's called the security audit  prompt. You just copy everything below this line,    
01:00:18: okay? And what you do is you give it to your model  and you say, "Hey, you know, I want you to check    
01:00:23: to see if all of this stuff is done." Then after  you're done, um, you know, flag all of your issues    
01:00:29: and then ask me what you want me to do about all  these issues. So, hypothetically, I mean, I'm just    
01:00:33: going to paste this whole prompt in, and I just  did to our website. Um, the issue with the website    
01:00:38: is obviously there's no real authentication going  on, right? So, it's not like it really matters too    
01:00:42: much. Uh, but still, you know, it's a reasonable  way for us to at least run through this. And now,    
01:00:47: uh, Gemini 3.1 Pro High, and I always recommend  using the smartest model for this stuff, is now    
01:00:51: just going to like take this prompt, pump through  literally everything, and then just say like,    
01:00:54: "Hey, this is good. Hey, this is bad. Hey, this  is good. Hey, this is bad." And then we're going    
01:00:58: to secure it by basically just saying, "Okay, fix  everything that's bad." Okay. And now it's given    
01:01:02: us a big returned checklist. It's saying that the  codebase is a classic static front end. Here's    
01:01:08: the systematic audit. No hard-coded secrets, no  API keys, and so on and so forth. No git ignore,    
01:01:15: which is something that they typically recommend  to um prevent you pushing yourv, no console log    
01:01:21: statements, you know, a bunch of things. And it  looks like, you know, we didn't actually have    
01:01:25: any to go off of for most of this. If you scroll  all the way down, it'll actually show you like    
01:01:29: here's the big checklist summary. Uh because this  isn't an app with any authentication, right? So,    
01:01:33: it's just like a website. And so, because of that,  only these checklist features are the only things    
01:01:36: that are relevant. But we did fail two. So, I'm  going to say is fix the two that failed. And then    
01:01:43: uh it's just going to go through. It's going to  add the git ignore. It's going to add a couple    
01:01:45: other things. You know, this takes time, right?  I mean, it it's going to take me some token costs    
01:01:49: as well. I'm going to spend some money on this  essentially. So, unsurprisingly, people don't want    
01:01:52: to do this and uh that people typically forget  it. But, you know, this is an 8020 pass. It's    
01:01:57: not going to fix everything, but it's going to fix  the low hanging fruit, which is to be honest what    
01:02:01: most people really just care about. When you vibe  code an app and you publish it and then it starts    
01:02:05: scaling and you start making some money from it  obviously then you can take some of that money use    
01:02:08: it to hire maybe an actual security engineer and  have them audit your project and stuff like that.    
01:02:13: Okay. And here you go. It did. So it updated this  to add the get ignore and then it updated this to    
01:02:18: um update eslint and resolve all four high high  severity mini match vulnerabilities which is    
01:02:23: cool. So yeah, looks like we are now solid. Let's  move on to something a little more interesting,    
01:02:27: which is taking everything that we now know about  how to build a beautiful front end and then how to    
01:02:31: do security audits and stuff like that and  then combine it into a full stack app. So,    
01:02:36: next up, we're going to build a fullyfledged  SAS app. The app that I want to build today    
01:02:40: is a client dashboard platform for a hypothetical  content writing company. And so, like any typical    
01:02:47: client dashboard, we're going to want to be able  to create orders, um, view pending orders. We're    
01:02:52: going to want to have like a nice sexy dashboard  which gives us an overview of everything,    
01:02:56: our stats and so on and so forth. Then we're  also going to want some sort of like settings    
01:02:59: or configuration page. Then on top of that, we're  going to need some sort of login naturally. And    
01:03:04: then I think at the very end, I'm also going to  produce a nice sexy landing page just to tie it    
01:03:07: all together. And then I'm going to push it uh  live to production as well, just so you guys could    
01:03:10: see how it all interacts. Before we actually do  the building, I just want to run you guys through    
01:03:14: what I consider to be the uh basically major vibe  coding design loop as of right now. And obviously    
01:03:20: there's a bunch of different ways to build apps.  And I don't want you guys to think this is like    
01:03:24: the the end- all beall. There are many many  different ways to do this. But in my experience,    
01:03:28: this is like one of the one of the good ones  right now. And if you follow this sort of flow,    
01:03:32: um you'll save yourself a fair amount of time  later on just in terms of like the design and    
01:03:35: then also security because um as I talked about  in the security module, there's a fair amount    
01:03:40: that goes into designing like a wellsecured  app. So the way that this works in general is    
01:03:44: we start with some sort of inspiration design.  And so there are a variety of different places    
01:03:48: you can go to for these inspiration designs, but  in general, I like going to um this website here,    
01:03:53: Dribble with threebs. I like going to this  one called godly uh website. And basically,    
01:03:59: there are a bunch of these sources on the internet  that compile really high quality designs. And like    
01:04:04: logically speaking, I'm not a designer, right? I  haven't spent all the time and energy necessary to    
01:04:09: know the right padding and the right color  schemes and all that stuff. So it's like,    
01:04:12: why would I worry about coming up with all that  stuff myself? instead I could just borrow somebody    
01:04:16: else's and then we can make some changes to it  and then once it's all changed and and and all    
01:04:20: nice and pretty. Um you know like we will have  taken the design fundamentals that somebody spent    
01:04:25: a lifetime putting together and then we could just  work off of that instead of spending god knows how    
01:04:29: long trying to figure out like the total amount of  margin on the left and the right hand side of the    
01:04:33: uh the elements. It's crazy stuff. So as somebody  that's like been doing a fair amount of design,    
01:04:38: I got paid for design. Uh it's not worth the time  and energy that it goes into learning all that    
01:04:41: stuff. So we start with an inspiration design. I'm  going to grab a couple of these. And then you have    
01:04:46: an optional step here which a lot of people are  starting to do now where you animate. So the idea    
01:04:50: is since Vibe coding now makes uh the ability  to like replicate designs and have high-end    
01:04:54: designs really really easy. You know you need  a way to stand out. And so the way that people    
01:04:58: are standing out now is through animations through  um like kind of videos that are playing. The idea    
01:05:02: being that you know a still can't make video based  stuff super super high quality. So you could still    
01:05:06: um stand out as like human created content or  uh designs with something like that. I'm going    
01:05:11: to show you guys how to do that. Anyway,  uh this does cost a little bit of money    
01:05:14: because there's some models out there that  you need that can convert images to videos,    
01:05:17: but I'll I'll run you guys through what that  looks like um for the landing page. After that,    
01:05:20: we need to build in the main functionality, which  is always going to be the dashboard. It's going to    
01:05:24: be things like, you know, your various widgets,  your various pages, and stuff like that. Then,    
01:05:28: we're going to do local testing and iteration.  Local testing, just so we're all clear,    
01:05:32: just means testing it on your device, and it also  means testing it with uh without a database. So,    
01:05:36: we're just going to do all the file and then, you  know, uh, data and stuff like that in like a JSON    
01:05:41: and then we'll just test it all locally, make sure  that it works. Once we've made sure that it works,    
01:05:45: we'll then push our data to a database. And then,  in our case, we're going to use superbase. I'll    
01:05:49: talk about that in a sec. But then, um, we'll  test it all basically with the database. Once    
01:05:53: we're done with that, then and finally then do  we create an authentication page. And I find um,    
01:05:57: doing O at the end is way better than doing O  at the beginning because if you guys remember,    
01:06:00: I mentioned like middleware, right? Well, like  a big issue with the middleware is you'll just    
01:06:04: like the low hanging fruit is you'll do the O  first, then you'll make the pages and then the    
01:06:07: O will only secure the first page that you do.  So instead, we're just going to do our O at the    
01:06:11: end and then the model will already have all  the context to like produce um you know good    
01:06:15: authentication middleware for all the pages and  then at the very very end we're going to deploy    
01:06:19: and then obviously the issue with you know testing  back here when it's sort of on your machine and    
01:06:24: then deploying is like you you need to test it  again. So we're going to do some end toend tests.    
01:06:28: We're going to do some miscellaneous designs and  I'll probably just throw in the landing page there    
01:06:31: since obviously the landing page doesn't really  have much functionality to speak of. And uh yeah,    
01:06:35: that's that's more or less the loop. And then  you know like when you're ready what you do is    
01:06:38: you just do the exact same thing. You just  make a new product and then you start with    
01:06:41: the inspiration design. Um you can do some video  animations if necessary main functionality local    
01:06:46: testing database testing off deployment and end  tests and then landing page. Then my inspiration    
01:06:50: design animate and so on and so on and so on  and so forth. So I do this on basically all my    
01:06:54: vibe coded apps and uh yeah works pretty well.  So the common vibe coding stack which I'm just    
01:06:58: calling the usual suspects here are going to  be a combination of Nex.js for the front end    
01:07:02: a superbase for the database and the off and  then some sort of serverless backend which    
01:07:06: um in our case is going to be netifi but you  can use netlifi versell and a bunch of these    
01:07:10: other tools but this is just what people mostly  use because it's just very easy to spin up. So,    
01:07:14: to make a long story short, in case you know, we  have people here that aren't familiar with the    
01:07:17: idea. Um, you know, when you sign onto a website,  obviously this is my really crappy rectangle. Um,    
01:07:23: and this is our browser with the three little  dots, maybe the URL bar and stuff like that. And    
01:07:26: you have like the app over here and I don't know,  some sidebar. And then here's some other stuff,    
01:07:31: you know, like what what you're seeing, what's  rendered here is is the front end. And um there's    
01:07:37: already different front-end languages, right? I  mean, like HTML is hypertext markup language. It's    
01:07:41: usually used to create the structure of the page.  If you have CSS, which is cascading stylesheets,    
01:07:45: that's usually used to like make the the  rendered elements really pretty. And then,    
01:07:50: you know, if you want functionality on top of  that, you will use JavaScript and, you know,    
01:07:54: TypeScript. And there's there's all these  different languages, right? Well, basically    
01:07:57: what happens is um using all these languages,  there's just so many different ways you could    
01:08:01: use them that all the developers were using them  slightly differently. Some were more efficient,    
01:08:04: some were less efficient. What people ended up  doing is they created uh front-end frameworks.    
01:08:09: Okay. Well, not even just a front-end framework.  NexJS is technically also like it's like a full    
01:08:12: stack framework but um they made frameworks which  just encapsulate all three of these into you know    
01:08:18: this thing next.js and so what this is this is  basically like a full way to manage your HTML    
01:08:24: CSS your JavaScript all these other programming  languages and then builds they build it in a    
01:08:28: very opinionated way that consistently produces  similar outcomes and you know follows a consistent    
01:08:33: and predictable pattern so that most developers  can just spin up a site really quick. This is    
01:08:38: doubly important in the age of AI where you know  when if things aren't standardized there's like a    
01:08:42: million billion different ways that an AI model  could make a site and because usually there's a    
01:08:45: lot less supervision when you're viing than um you  know like a traditional development process. A lot    
01:08:49: of these ways just like aren't really well thought  out. You know AI just picked the simplest lowest    
01:08:53: hanging fruit and went with it. So I recommend  using these frameworks and stuff like that just    
01:08:56: both to economize your work but also just to  make sites predictable. If you ever hand them    
01:09:00: off to anybody if you're doing these for clients  and stuff like that you know next.js is the way    
01:09:03: to go. Okay. So that's the front end. Um you know  Superbase is going to be our database. So, I mean,    
01:09:07: just think of it as like a big Google sheet with  like a bunch of different tables and columns. Wow,    
01:09:11: my drawing skills have gotten worse recently.  Uh, but to make a long story short, you know,    
01:09:16: the stuff that is visualized on our front end,  like our bar charts and our little widget apps and    
01:09:20: stuff like that. Obviously, we need to pull the  data from somewhere, right? So, it doesn't make    
01:09:23: sense to keep all the data like on the site cuz  it's always changing. What we do is we're going    
01:09:26: to pull from a database and then like use that to  actually go and and change features. Obviously,    
01:09:31: we're going to need a login screen, right,  with like a little user uh portal and then    
01:09:35: like a little password portal. Um, let's round  that off so it quits looking phallic. And uh,    
01:09:41: Superbase is going to help us with that as well.  And then finally, you need what's like called a    
01:09:45: backend, which is basically just like a server.  And this server is actually going to manage the    
01:09:49: interactions between our database, our front end,  our off, and and you know, a lot of stuff. So, you    
01:09:54: know, that's a little bit more cloud-based. You're  not really going to fully I can't really just draw    
01:09:58: something that makes sense there. But suffice  to say, all these four components are going    
01:10:01: to interact together really nicely. And then the  stack that basically all the tools use is Nex.js,    
01:10:05: JS superbase and then some sort of what's called  serverless um back end. Okay, so we could go    
01:10:11: into that or we could just build it and I'd much  rather just build it and then you guys could learn    
01:10:14: through the doing. So let's start with the very  first step which is finding an inspiration design    
01:10:18: and I'm going to immediately jump on dribble for  that. So dribble for those of you guys that don't    
01:10:23: know but just go on the website. It's basically  just a big list of like different designs that    
01:10:27: people have made and it's cool. It was it was  initially meant to be like a way for designers to    
01:10:32: create a portfolio and show off the work and stuff  like that, which is pretty neat. Now, you know, to    
01:10:36: be honest, I think a lot of people are just using  this to source AI designs. I don't know how much    
01:10:39: longer we're all going to have access to dribble,  but uh we'll see. And, you know, in our case,    
01:10:44: what we're looking for is we're looking for some  sort of like client dashboard, right? So, I'm just    
01:10:48: going to type client dashboard in here. Basically,  what you'll see is a bunch of people have created    
01:10:52: these really sexy client dashboards. So, I'm  just going to click on a couple of these. Um,    
01:10:56: yeah. So, I I already opened that one. So, let's  click on this. Let's click on that. This one's    
01:11:01: actually pretty nice. And then, hm, why don't I  open up? No, I don't really like that one. That    
01:11:05: one looks kind of dumb. This one here looks cool.  Okay. And as you can see, you know, I now have    
01:11:10: um like a list of, in this case, all clients on  the lefth hand side. You know, this sort of like    
01:11:14: nice gray pattern, and that's that's kind of cool.  I don't really like this one a ton, though. So,    
01:11:18: I'm just going to keep looking until I find one  that I really really like. Um, what you'll find is    
01:11:22: a lot of these are now videos as well. And there  are a couple reasons why they're doing videos. One    
01:11:26: of them is that they don't really like when people  screenshot them like I'm about to. That design's    
01:11:31: cool. Okay, this is reasonable. Um, this one's  pretty interesting. But the one that I initially    
01:11:37: picked that I just liked the look of was this  here, which is super simple and it's very like    
01:11:43: extensible and you guys can add on whatever the  heck you want, right? So, I think I'm going to    
01:11:46: use this. And uh, basically what we're going to  do is I'm going to create a screenshot of this    
01:11:51: and then I'm going to use the model to try and  replicate this as closely as humanly possible.    
01:11:55: And I have a prompt set up that I'm going to I'm  going to send it to and stuff like that. And then    
01:11:58: from this we're going to get like a really high  quality design. And then I think I'm also going    
01:12:01: to do the same thing for the landing page. Um you  know this design is different from this design but    
01:12:06: uh you know I'm just going to find a way to like  meld the two together. And then I think at the    
01:12:09: end we're going to have something that like has  the color scheme of this but it actually has like    
01:12:13: the design of this if that makes sense which is  ultimately what I'm going for. I like that design.    
01:12:16: I like this um I guess this is sans ser but I  really like this font. So yeah let's uh let's    
01:12:21: give it a go. So what I'm going to do first  is I'm gonna head over to anti-gravity. Okay.    
01:12:25: And then I'm going to open up a new folder. And  I'm just going to call this full actually let's    
01:12:31: go lowercase full stack client dashboard. That's  going to be my very uh first full stack app with    
01:12:38: you guys. And then what I'm going to do first is  I'm going to talk a little bit about the different    
01:12:42: types of models that we have available to us.  Remember how before we designed our landing page    
01:12:46: entirely using Gemini? Gemini 3.0 Pro is awesome,  but personally I find that actual like system    
01:12:50: plans and system designs are better done through  Opus 4.6 right now. So, what I'm actually going to    
01:12:54: do is I'm actually going to do the planning in  Opus 4.6. I'll show you how to do that. First,    
01:12:58: let me zoom in because this is pretty far out. And  then I'm just going to go to um plan mode here. If    
01:13:03: you just keep on cycling through, eventually  it'll get to it. It's the one with the little    
01:13:05: pause sign. And then I uh created a prompt here  that I just want to go through with you guys. So,    
01:13:10: the prompt says, "You're a world-class website  designer with 15 years of experience designing    
01:13:14: high quality, award-winning websites for Apple  and Dribble. We'd like to build a full stack    
01:13:18: SAS client dashboard app for our content writing  business. It's very important that you get this    
01:13:22: right. our career depends on it. This is a little  hack that I picked up from um I think it was like    
01:13:26: a former OpenAI dev or something, but they found  that when uh you make it really really important,    
01:13:31: like our career depends on it, the output quality  actually goes up just by a few percentage points,    
01:13:35: nothing major. And my prompt is not winning any  awards here. So, uh anyway, I'll take every win    
01:13:40: that I can get. As a client, we want the ability  to view all pending content orders and progress    
01:13:43: in a beautiful dashboard. We also want the  ability to create new content orders using a    
01:13:47: highquality but simple form. Let me just run this.  We want the ability to configure various settings,    
01:13:52: modes, etc. And we also want anything else.  Your usual SAS app like this would include    
01:13:56: the dashboard. SAS app should use superb. I said  superbase here. What I meant to say was superbase,    
01:14:00: but I was using a voice dictation. So, what are  you going to do? Next.js and then tailwind.css.    
01:14:05: And we will deploy using netlifi. I'll define the  UX via screenshots. So, don't worry about design    
01:14:11: particulars. The flow will be first we'll build  the main functionality, which are the parts I    
01:14:15: talked about above using a screenshot inspiration.  You'll take the design style from the screenshot    
01:14:19: and then use it to build all of the signed in  pages. Then we'll make it interactive with local    
01:14:23: data and ensure routes work. Then we'll add O and  DB with superbase. Then we'll make a landing page    
01:14:27: and finally do an endto-end sweep to ensure  everything works including off, middleware,    
01:14:30: security, testing, etc. Then deploy and retest.  Then I'm saying think extremely hard and generate    
01:14:35: a great plan. Once you've developed one that is  comprehensive, report back here and I'll supply    
01:14:39: some screenshots. That's how we can start the  design process. Okay, so I gave it a fair amount    
01:14:43: of context and you can see it's already done some  thinking, right? put the text stack and looks like    
01:14:48: it corrected my little issue there with superbase  phased approach right they want me to plan this    
01:14:52: out comprehensively there's nothing in the current  um working directory so it looked it couldn't find    
01:14:57: anything green field project and now it's actually  going to go and create the architecture and that's    
01:15:02: what's that's what it's doing right now that's why  it's in plan mode now I should note here in the    
01:15:06: bottom right hand corner you guys probably I don't  know if you guys could see that's pretty small we    
01:15:09: got this little lightning um what I've done is  I've enabled this thing called fast mode just    
01:15:13: because Opus 46 supports it and that allows it to  go two and a half times is faster approximately    
01:15:17: for I think like 3x the price. So little bit of  an arbitrage there. Um I think the price is going    
01:15:22: to jump up to 6x pretty soon. So it may not be  available when you guys are on it. But personally    
01:15:26: I find for building really comprehensive plans  awesome tool and an awesome model. Okay. And    
01:15:31: then uh basically what I wanted to do is I wanted  to like produce this big plan and then I'm going    
01:15:35: to pass off this giant plan over to Gemini who I  think is actually just a better designer. Okay. So    
01:15:40: once the uh thing is super comprehensively planned  um then I can just pass all this stuff to Gemini    
01:15:45: with the screenshots. But sometimes claude code  will actually ask you or rather Opus 4.6 will use    
01:15:50: cloud code to ask you questions and so that's  why I'm doing all this planning and stuff like    
01:15:54: that here just in case it asks me some questions  for clarification. Okay. So I'm going to press    
01:15:58: escape because uh it's basically like hey do you  want me to start? Then here it's going all the way    
01:16:04: to the top here. We want to build a full stack  SAS dashboard. Here's the tech step. Here's the    
01:16:09: phase one project setup in UI shell. And um I'll  be honest, like I'm I'm usually not reading this    
01:16:13: entire thing. What I'm doing is I'm skimming.  I'm just making sure there's nothing that just    
01:16:16: jumps out to me as stupid. Like what I want is I  basically just want to see, hey, are there way too    
01:16:20: many pages? Is this way too complicated? Is this  model completely misunderstood what I want it to    
01:16:24: do? And so what I'm seeing is there'll be like  an app page, there'll be um a dashboard page,    
01:16:30: orders, a new page, a settings page, notifications  page, and that looks pretty reasonable, right?    
01:16:35: There'll be a components page where it'll actually  store all the components. Library page. Okay,    
01:16:39: this looks pretty good. This looks pretty  good. Interactive local data. So after that,    
01:16:44: we'll define some types. Yeah, I don't even know  what the hell that really means to be honest, but    
01:16:47: that's okay. And then we have those actual pages,  which look good to me. All of these are pages    
01:16:51: that I would realistically want my app to have. Is  there anything else I'd want? H dashboard orders.    
01:16:55: No, I think I think this is fine. After that, we  have the superbase off. So here, I'll like set    
01:17:00: up the superbase, but that's okay. That's not for  now. That's later. We'll finally have the landing    
01:17:04: page which is going to be really nice and sexy and  then we'll have some key architecture decisions.    
01:17:10: Okay, cool. I mean, this seems pretty reasonable  to me. I don't think there are any problems    
01:17:13: here whatsoever. So, what I'm going to do is I'm  actually just going to copy this whole plan. Okay,    
01:17:18: this whole thing that this just created for me.  I'm going to paste it into this now. Okay. And    
01:17:24: then I'm also going to provide some initial  screenshots of what I want the dashboard to    
01:17:27: look like. So, I'm just going to command um you  know on a Mac you can command shift control. So,    
01:17:34: command shift control 4 and then I'm just going  to go select this. Okay. And that'll actually    
01:17:40: give me like a pretty high quality screenshot.  I'm going to feed this in. Okay. And so now we    
01:17:46: have the image of the dashboard and then I'll say  design using this style as inspiration clean and    
01:17:53: minimal. Okay. Okay. So, what I've done is I've  now split the work up between these two agents.    
01:17:58: I had um Claude Opus 4.6 design me the really  comprehensive plan because as I mentioned I    
01:18:02: think it's a little bit better at planning  at least as of the time of this recording.    
01:18:05: Then I'm going to hand off all of like the design  and then you know basically just like grunt work    
01:18:11: over to Gemini 3.1 Pro High, which I think is way  better at actually like wiring up the components    
01:18:15: and then putting together like that that really  high class design. And uh you know at this point    
01:18:20: all we really have to do is just wait for it to  build. And this is realistically because it is,    
01:18:23: you know, going to be a pretty comprehensive app.  This isn't something that's going to happen in a    
01:18:27: couple minutes. You're probably gonna be good to  like go step away, have a coffee, come back. By    
01:18:31: the time all that stuff's ready, this will have  given you some sort of result. But it's always    
01:18:36: good before you do that just to like wait for,  I don't know, 30 seconds or so because sometimes    
01:18:40: it'll give you a plan and then you can just review  the plan um and just double and triple check that    
01:18:44: it didn't do something super stupid or super  terrible. And I don't think it has. Everything    
01:18:48: here looks good to me. So, I think it can just  go ahead and commence the project. Cool. So,    
01:18:54: I'm actually going to go grab a coffee and I'll be  right back. Okay. So, now it's telling me it's now    
01:18:57: completed phase 2 interactive with local data. So,  we should now have a site up and running with some    
01:19:01: sort of local data. Immediately after I said let's  open it. So, it's opened it. I tried doing some    
01:19:06: initial debugging and stuff like that on its own.  It it didn't end up doing so because there was an    
01:19:10: additional error which I'm going to talk about.  And just on the uh I guess concept of errors    
01:19:15: when you create a full-fledged SAS app like one  that has like back and forth and stuff like that,    
01:19:18: not just a website where there's no interactivity,  you know, you're going to have errors. And so it's    
01:19:22: not about like will I screw up at some point.  Will the model get this wrong? Just a matter    
01:19:27: of when and then what you're going to do when uh  it screws up. So basically what I've done is it    
01:19:32: started the development server and opened this in  my local browser. So I just click this open and    
01:19:36: as you can see here we have the app set up, but  the app looks a little funky. We don't have any    
01:19:40: styles. Just looks like crap. So obviously this  isn't what we want, right? What I'm going to do    
01:19:44: instead is I'm just going to take a photo of this  and then I'm just going to send it back. And then    
01:19:47: I'm going say I don't think styles are loading  also because I'm pretty sure there was some issue,    
01:19:53: right? I initially got this problem as well where  it said missing HTML and body tags in the root    
01:19:57: layout. So I'm also going to copy this in. Also,  I got this error. I'm going to paste that in. So,    
01:20:03: you know, at least initially before you even  get to be able to play around with the UX,    
01:20:07: you may have some like initialization problems and  config problems and stuff like that. And that's    
01:20:11: okay. Basically, what you do, um, if I just show  you guys sort of how I think about vibe coding    
01:20:16: these things is it's almost like I don't know,  you're in a cave. Uh, have you guys seen like the,    
01:20:22: you know, mining meme where you're like mining  for gold? Okay, basically you're in a cave and    
01:20:27: every single time you run the thing, you're like  this fella here. You just get a little bit further    
01:20:32: and a little bit further and a little bit further  and you know this fell here can't see anything.    
01:20:38: It's just darkness in front of him, right? So  every time he mines, he goes home and he's like,    
01:20:42: "My god, I didn't make any progress today." But  obviously if he just continues going, eventually    
01:20:46: he gets to the point where there's a bunch of gems  sort of on the other side. And so that's basically    
01:20:49: what we're doing. We're just going to work through  this initial sludge with initialization errors by    
01:20:53: copying and pasting um any problems and then just  giving it directly to uh the model until we get    
01:20:58: to that little gold gem. Once we're here, we can  actually start making real changes to our app. Um,    
01:21:02: and all of that is reasonably well expected. Okay,  speaking of which, it just modified some of the    
01:21:06: CSS after I sent it this message. And as you  can see, we now have a little dashboard set up,    
01:21:10: one on the left hand side. So, we've already made  some some reasonable progress. I'm just going to    
01:21:13: dashboard, see if there are any issues. Okay, I'm  not seeing any issues at all. So, we have five    
01:21:16: total orders, one in progress, two completed.  This is just some fake data made up. So,    
01:21:20: you can see we can now mouse over each of these  three things or uh five things. SAS growth guide,    
01:21:25: Q3 newsletter, so on and so forth. So, these are  all the orders that we have submitted as clients.    
01:21:30: There's a little notification toggle. Um, if I  click on the orders page, we're now here. So,    
01:21:35: you can actually see the orders better. I'm just  curious if I click new order, what happens? Okay,    
01:21:40: so we're now on a new order page where I can  actually add info. So, I'm going to say this    
01:21:44: is an example. New order, content type, landing  page. Hey, I want to build a really cool, sleek,    
01:21:50: sexy landing page. And then, you know, I want some  stuff here. And then here's my requested deadline.    
01:21:57: I don't know. We'll say March the 1st. We want  to add SEO meta tags and then require approval.    
01:22:02: I'll click save order. Okay, cool. And it looks  like it's got the functionality. And so I can now    
01:22:06: actually add orders. If I go to settings, what  do we got? Demo user, Acme Corp, email address,    
01:22:11: cool preferences, email notice, weekly digest.  Okay, so these aren't working. At least the    
01:22:15: weekly digest isn't. But that might be intentional  just because we don't have um access to, you know,    
01:22:20: some sort of email. But yeah, I mean like to  be honest, like the the core functionality    
01:22:23: of the app's already made. So although the  design is still pretty shitty, I would say    
01:22:27: and obviously I'm going to want to fix that up.  Um core functionality is done. We basically have    
01:22:31: like I want to say a REST API, but we have like a  little CRUD app here. We can create, we can read.    
01:22:36: Um I don't actually know if we can update. Doesn't  look like we can go to the specific order page to    
01:22:41: update yet. So maybe I'll make a note of that. Um  but we can presumably also Oh no, I don't think we    
01:22:46: can delete either. Okay, cool. Anyway, this notice  page also has notice. That's kind of neat. Um,    
01:22:50: I think what I'm going to do now is I'm just going  to voice dump in all of the problems that I see.    
01:22:54: And then we're just going to go back and forth  until we can eliminate just the minor little    
01:22:58: errors like styles and stuff. And then once we've  tested and confirmed the functionality here, then    
01:23:02: I'm going to do a big stylistic upgrade. After  we've done the stylistic upgrade, I will uh then    
01:23:07: make this database friendly. And then once it's  on the database, then we can actually push. Hey,    
01:23:11: this is really well done. Nice job. When I click  on a new page, there's initially some there's a    
01:23:17: there's a brief initial load where it says loading  orders or loading settings or a loading dashboard.    
01:23:23: I'd like you to remove that. I don't want any sort  of loading um widget here because it just makes it    
01:23:28: look lower value. Instead, I want you to maintain  the structure of the page and just leave all of    
01:23:33: the various sections blank. So, for instance,  if I were to click on orders, rather than it say    
01:23:39: loading orders before it populates the rest of the  page, uh where it shows me the table and stuff,    
01:23:43: I just want you to present the table to me  immediately and then just leave it blank. That    
01:23:47: way, we could fill in the text um afterwards. Um  right now the navigation text is in light gray.    
01:23:58: I'll take a screenshot and I'll show you what  I mean. But on the orders page, for instance,    
01:24:03: um the text that says orders at the top lefthand  corner is very similar to the background color.    
01:24:08: So that's annoying. I'd like some sort of graph  on the main dashboard page cuz right now I don't    
01:24:12: have any. I'd like a way on the dashboard page  to click into the recent orders as well. Uh    
01:24:16: right now I am capable of mousing over them and  something changes, but it's just a style effect.    
01:24:21: I actually want the ability to click on them. In  addition to being able to create, I also want to    
01:24:25: um be able to click on each individual article  on the orders page and then view it. Right now,    
01:24:31: when I click view, it says either order not found  or it takes me to some error page, which is not    
01:24:38: what I want. The notifications page has a mark all  red button that is currently grayed out. When I    
01:24:44: click on the notifications at the top right hand  corner, that little icon, nothing happens. So,    
01:24:49: I'd like that to just take me to the notifications  page. There's also nothing that happens when    
01:24:52: I click on my little profile picture in the  top right hand corner. Under settings, when    
01:24:58: I toggle weekly digest, nothing happens. Email  notifications works, but the weekly digest toggle    
01:25:03: doesn't. There's a nextjs error here called param  property was accessed directly with params.id.    
01:25:09: Params is a promise and must be unwrapped with  react use before accessing its own properties.    
01:25:14: Nothing happens when I click on the little demo  user button in the bottom lefthand corner either.    
01:25:20: This is quite a promising start. We just have  a few adjustments that we have to make. Uh so    
01:25:24: that functionality is perfect. Once you're done  with that, let me know and then we can proceed.    
01:25:28: Cool. So I've just added all this context and  I'm just going to take a screenshot now of that    
01:25:32: issue that I talked about where the orders  text was um you know kind of gray. That'll    
01:25:38: provide some more context. I'm keeping this small  intentionally because every new pixel is like    
01:25:43: more tokens than I'm consuming, right? There's  some other minor stylistic changes and stuff,    
01:25:47: but for now I'm not going to worry about the  style. And the another reason why is because    
01:25:50: um once you have an app that's like up and running  like where all the functionality is right then you    
01:25:54: can just like open a new Gemini instance and not  have any context and then just say like hey here's    
01:25:58: my app I just want you to change a design and then  it can just go into the style sheets and stuff    
01:26:01: like that make it really sexy. Uh whereas if you  try and mix all of this stuff into one big long    
01:26:06: context window sometimes it can get messed up. So  you know I just want this specific chat right now    
01:26:11: to focus on the main functionality and then we  can worry about the design afterwards. Anyway,    
01:26:14: let me just make sure I didn't add in any  additional information. Cool. Cool. That looks    
01:26:18: good. Grade out. Okay. Why don't I do this? There  you go. Cool. So, now deliver that information.    
01:26:26: And just like um last time, uh I'm just going to  sit tight and wait for it to relaunch. Okay. It's    
01:26:30: telling me that it's now updated everything.  I'm just going to click accept all. And then    
01:26:33: we'll go back to the specific page. Let me click  on settings. Cool. We don't have any issues there.    
01:26:38: Um everything there looks fine. Oh, you know, I  think there's one thing I forgot to point out,    
01:26:43: which is this um notifications button. I think  that's going to be okay because we're probably    
01:26:47: just going to massively change the style here. But  yeah, that looks fine. Let's actually click on a    
01:26:51: specific order. Nice. This is now pushed all the  way to the left. The order um arrow looks really    
01:26:54: nice. I don't know if there's a way for us to  uh mark this as completed now, right? Okay,    
01:27:00: cool. It also says start work. That seems kind of  odd. I wonder why it says start work. Um yeah, I'm    
01:27:05: noticing that as well. So, I think we're probably  going to have to remove that. The model might like    
01:27:08: fundamentally misunderstand what I want. What I  basically want is I just want the client to have    
01:27:11: like a dashboard where they could see it all. Hey,  I'm noticing there's like a start work button. Um,    
01:27:16: just to be clear, this is a dashboard for a client  to look at the work that is currently being done    
01:27:21: by the agency. So, they don't have the ability  to start work or anything like that. Just go    
01:27:26: through and fix this. So, if there are any other  idiosyncrasies, um, those are taken care of. Okay,    
01:27:30: cool. We got that last change here. And it looks  like everything is now super clean. Um, no major    
01:27:35: issues whatsoever. If I click on this button,  uh, we only have readon access. Essentially,    
01:27:40: clients can't make any changes. they can only  download stuff and the HC is what initiates that.    
01:27:44: So that's what I wanted. From now on, what we're  going to do, rather from here on, what we're going    
01:27:47: to do is we're going to redesign this because  I think the design is kind of elementary at the    
01:27:50: moment. And I'm going to use that same approach  that we talked about earlier. We're going to find    
01:27:53: a really high quality pre-existing design and I'm  going to have Gem and I basically go through and    
01:27:57: then modify this to match. Um, and the idea is it  should be able to modify this to basically be like    
01:28:01: almost pixel perfect. Uh, we're just going to like  change the fonts and stuff like that. Okay. So,    
01:28:06: I'm going to go through dribble again. And I mean,  I like this idea of like a light mode dashboard.    
01:28:11: Uh, I really do. Uh, what we had before is kind of  mid. So, I don't want that. I do like the idea of    
01:28:19: like something dark on the left hand side, though.  Kind of break it up a bit. So, I'm going to see if    
01:28:24: I could find something that is dark. Let's take a  quick peek at this one. This one looks all right.    
01:28:30: You know, I really, really like this one. This  one looks super clean. Check that out. Okay. So,    
01:28:34: I'm a big fan of this. Super big fan of that. I  think what I'm going to do now is I'm going to    
01:28:39: take this screenshot. Okay, copy that in. And then  I'm going go back to Gemini. I'm going to paste it    
01:28:46: and I'll say, "Hey, this is great. I'd now like  to change the design significantly. You should    
01:28:51: do the vast majority of your work in Tailwind  or whatever stylesheets that you're currently    
01:28:55: using to build this." Um, in short, I think the  design right now is very basic and super simple.    
01:29:01: I want you to add significantly more  complexity um using things like cool    
01:29:06: mouseover effects on navbar elements on the lefth  hand side. I want you to add really highquality    
01:29:12: icons. I'd like you to modernize the design  significantly. I want you to try different fonts,    
01:29:17: higher quality fonts. I want you to use like  cutting edge um new ones that are on Google fonts,    
01:29:23: etc. I want you to use some placeholder images  so that the design feels alive. And I also want    
01:29:28: you to significantly upgrade the graph. What I've  done is I've given you a screenshot from a similar    
01:29:33: design that I like a lot and I want you to mimic  more or less everything that you see here just as    
01:29:38: a uh just as a start point. I'll modify the design  slightly afterwards, but try and really nail the    
01:29:46: font colors. Uh try and mimic the font styles. Try  and mimic the um encapsulation, the border styles,    
01:29:53: cards, etc. Okay, this is looking a lot cleaner.  I'm loving how it did this design. You also see    
01:29:59: way higher bar charts, way cooler bar charts. Um,  this takes me to what looks like a mini landing    
01:30:04: page that I put together. That's interesting.  I wasn't even like looking for a landing page,    
01:30:08: but it's nice that it did. So, and we even have  like a little look at that. It's like a little    
01:30:11: notion um avatar up top. Cool. Um, my tasks  are still the same. When I click this button,    
01:30:16: you see we do have that higher quality design,  which is nice. And nothing pops up for calendar.    
01:30:22: Nothing pops up for reports. Nothing pops up for  portfolio. Nothing pops up for these buttons.    
01:30:27: Neither does it pop up for those buttons. Let me  just check the bottom. Okay. And then yeah, the    
01:30:31: settings work. So, basically, it's just populated  this with a bunch of additional buttons that we    
01:30:34: don't need. I'm just going to tell it to remove  all the stuff that we don't need. And then I'm    
01:30:37: also going to have it adjust the font a little bit  cuz I think the font's the same. Hey, this looks    
01:30:41: much better. Fonts are the same though. So, I want  you to adjust the fonts. Um, I'd also like you to    
01:30:47: change all of the major titles from title case to  sentence case. For instance, task completion over    
01:30:54: time should be sentence case. Apply this to all  other elements and boxes. I'm liking the design    
01:31:00: quite a bit. Nice job on the avatars. I think  you should add borders rather than shadows around    
01:31:06: things to better match the task beto design. I'm  also noticing that you put a bunch of additional    
01:31:11: buttons that we don't need. Like for instance,  calendar, reports, portfolio, product management,    
01:31:15: project management, real estate website, my first  portfolio, all team product team, invite team,    
01:31:21: supports, that little thumbtack icon, the play  icon, the integrate icon. These aren't things    
01:31:30: that we actually need because there's no pages  that will address them and I don't plan on making    
01:31:34: them. So, I'd like you to remove all elements  for whom we don't have pages because that's    
01:31:38: not really relevant. um make the search bar apply  to our current list of orders and then update the    
01:31:47: design of the settings page because right now it  looks the same as it did before. And then finally    
01:31:52: in inbox the button that says mark all as red  is um almost completely transparent. It's very    
01:31:58: difficult to see unless you mouse over it. So fix  that as well. I think that's more or less the last    
01:32:03: round of edits and then we can get into publishing  this. Cool. And this is the final result. I have    
01:32:07: a very clean dashboard. You see with that scroll  on the right hand side, we don't have any issues.    
01:32:12: Down at the bottom, we have only the pages that  are actually relevant to us. Now, of course,    
01:32:16: I could add like a million pages here if I wanted  to, but I don't really. I mean, like this is just    
01:32:19: the purpose of the app, right? I think in our  uh crazy vibe coded economy, you're going to    
01:32:24: find that like a lot of apps are going to have  unnecessary features and whatnot just because they    
01:32:27: can. I think simplicity is actually going to end  up being quite the moat. So, yeah, I'm going to    
01:32:31: keep things as simple as humanly possible. Uh but  yeah, everything works, which is really nice. So,    
01:32:35: you know, if I click on this app, uh, sorry, if  I click on this specific content page, you know,    
01:32:39: you can see that I'm I'm here. Content's being  written and stuff like that. I don't have the    
01:32:42: ability to modify like I had last time, you know,  I can download stuff if necessary. If I go back to    
01:32:46: the dashboard, this um graph is interactive. Uh,  you know, and I I can jump into this anywhere I    
01:32:52: want, which is kind of neat. And then down at  the very bottom, which you guys can't see cuz    
01:32:56: my fat head's in the way, I have the settings  page, which is pretty neat. Um, and then, yeah,    
01:33:00: we also have the ability to search tasks up here,  which is really, really cool. Um, I could type SAS    
01:33:05: growth guide and then that's an initial piece an  additional piece of functionality that was added.    
01:33:10: Okay, so I'm just going to clear that notif. And  now that we've like really basically built this    
01:33:14: whole app directly on the computer, it's time to  take this to the cloud. So, what I'm going to do    
01:33:19: next is I'm going to go to anti-gravity and just  before we proceed with our next step, I'm going to    
01:33:24: ask it to save everything that it's done so far  into a gemini.mmd that effectively encapsulates    
01:33:30: what this app is, everything we've done so far,  and then provides instructions for future models    
01:33:33: in case we need to pass this off. And the reason  why I do this is because you might actually run    
01:33:38: out of like context. Um, that happens pretty  often. For those of you guys that don't know,    
01:33:41: there's only a certain number of tokens that you  can actually fit into one conversation with an AI    
01:33:45: model these days. Whether it's like Opus 4.6  six with a 200,000 context window. They have    
01:33:50: a 1 million context window option as well.  Whether it's, you know, Gemini 3.1 Pro high,    
01:33:54: I think I think it has a 200k context window,  might have a million. The point I'm making is    
01:33:58: like a lot of that context just used up by the  internal thinking of the model as it does tasks,    
01:34:02: right? So, in my case, like I I just don't want to  risk it. I don't want to like get the thing to the    
01:34:06: point where it's gone a little too far and then it  barely remembers what we talked about initially.    
01:34:10: Instead, what I want to do is I basically want to  like have this almost like a backup of where we    
01:34:14: are right now. This gemini.mmd file which uh you  know in my case is just a very highle summary that    
01:34:19: talks about where we currently are in the process  and you know what we need to do and stuff like    
01:34:23: that and then also gives instructions for you know  where to go from here. So once we're done with all    
01:34:29: this and now we have this which is sort of like my  fallback what we can do is we can um move on with    
01:34:34: the next step. So I'm going to say fantastic the  current design looks great. What I want to do next    
01:34:38: is I want to ensure that it works not only locally  but with Superbase as our database. Walk me    
01:34:45: through everything I need to do. In case you guys  didn't know, Superbase being our database. Um,    
01:34:49: this isn't something the model can actually set  up entirely for us. Instead, what we're going to    
01:34:53: do is I'm just going to ask it to walk me through.  And that's what it's done. Create a new Superbase    
01:34:57: project up here. Set up the Superbase client  and so on and so forth. Create the database    
01:35:01: schema. Enforce RLS. That's really important  like we talked about. Then replace hooks. and    
01:35:05: we're actually going to have it do some of this  stuff, but we'll start with database.new. So, I'm    
01:35:09: just going to jump over there. It'll now ask us to  create a new project. Now, in my case, I'm already    
01:35:13: signed into Superbase. So, I can just click that  button and then boom, it's done, right? They own    
01:35:16: the freaking domain name database.new. They got  a lot of this, right? And they've streamlined the    
01:35:21: setup to match. But, uh, if you don't already have  a Superbase account, just open up an incognito    
01:35:25: window and then just go to superbase.com and then  just click start your project in the top rightand    
01:35:30: corner and then just enter your information down  over here. email, password, you can continue    
01:35:34: with GitHub, SSO, whatever, and just make an  account. They're fantastic. This is like a really,    
01:35:38: really solid app, and uh it simplified the  development of like vibecoded sites 100x over. So,    
01:35:44: once you're done with that sign up, um you'll be  at a page like looks like this. I'm just going to    
01:35:47: type I don't know, Nikki Poof. I really got to get  more mature names for these. Uh okay, why don't we    
01:35:55: do I don't know. We'll just do client dashboard  app. Next up, we need a database password. So,    
01:36:02: I'm actually just going to make like a my own fake  one and then I'm going to copy it over. Actually,    
01:36:07: maybe we'll just generate one. The generated  one's weaker. So, I'm just going to copy that.    
01:36:12: We'll enable the data API. This stuff looks good.  Then I'll click create a new project. Okay. So,    
01:36:16: we have our database passwords right here. So,  just so that I don't lose this, I'm actually    
01:36:19: going to give it the password right here. And  then I'm just going to have some additional    
01:36:24: other lines. So, boom. It's now created the um  thing for me. And then I think what I do next    
01:36:31: is I have to go to project settings. There's a  project ID over here. So I'm going to copy this    
01:36:36: over and then I'll go project ID. Paste that in.  And then I need the superbase superbase URL as    
01:36:43: well. So I don't actually know exactly what that  URL is, but I'm just going to copy the dashboard    
01:36:48: name as well. So the project name, paste that  in. Let me just see if there's anything else.    
01:36:52: Project URL and on public key. So I think we need  to go to API, which might be over here. API keys,    
01:36:58: which is right over here. We're going to create  a publishable key. That's one that we want. And    
01:37:03: then I'm going to copy this. And then I'll say  publishable key. I'm just going to paste that in.    
01:37:11: Okay. So now this should be everything the model  needs. I'm not entirely sure. I think it is. So    
01:37:15: we're just going to give it all that information.  We're going to have it do the rest of this for us.    
01:37:20: Um and then cool. Looks like this is going to  take care of that. That's going to take care of    
01:37:24: the database schema. Oh, sorry. We need to take  care of the database schema as well. So anyway,    
01:37:28: I'm just going to give this its information and  then we'll have it tell us what to do next. And    
01:37:32: now we'll have edited an ANEV file, which is  pretty clean. It's going through and it's adding    
01:37:36: the information that we just gave it a moment ago.  And now what it's going to do is it's going to    
01:37:40: give us what's called an SQL schema, which is just  like the next step. And I imagine it'll just ask    
01:37:44: us to copy and paste something. It's also doing  things like wiring up the login and signup forms    
01:37:47: to Superbase O, which is super cool. So I mean, we  should have basically everything good to go aside    
01:37:52: from the landing page after this is done. Okay.  Okay. And then it's told us to go over here to SQL    
01:37:55: editor and then paste this giant file in. Um, so  I just did that. Since these are comments, this is    
01:38:00: just going to run a bunch of these simultaneously.  So I'm going to click run selected. Okay. And then    
01:38:03: it told me to go over here and then paste all the  stuff in and then just press run. So that's what    
01:38:07: I'm going to do. This will basically create us a  bunch of um tables and whatnot in our database.    
01:38:13: So if I go to database now, we we're going to have  a bunch of different tables and they're all going    
01:38:16: to connect in a specific way. And this is now  taking us to a signup page here. We obviously    
01:38:20: still have some changes that we need to make.  So, I'm going to do that after I verify whether    
01:38:23: or not this works. Now that it says signing up,  account created successfully. Please check your    
01:38:26: email to confirm your account. I don't know if um  we're going to get that because sometimes we have    
01:38:30: issues receiving emails. So, let me just pump  over to my own Gmail real quick. Okay. Yeah,    
01:38:34: looks like we did. So, I can now confirm my  mail. Um that's taken us to I think like this    
01:38:38: hastily putting together landing page, which is  not actually the page that we want. So, I'm going    
01:38:43: to click sign in. And then I think my email was  this. I'm not entirely sure. And then my password    
01:38:48: was that. Let's click sign in. Okay, cool. Yeah,  we actually did sign in. That's wonderful. Um,    
01:38:53: perfect. Now we have this dashboard, which is  kind of neat. My tasks. Uh, cool. We can click    
01:38:57: new task. Now we can create a new content order.  So, I'm going to go example content order. Make    
01:39:03: XYZ. Cool. And then we may have to change the  order options here, too, cuz I don't think I uh    
01:39:09: included that. Let's just select that. Click save.  Okay. Let's just make more characters. Okay. So,    
01:39:16: there's some issue with the database because  it's not refreshing. So now what I'm going to    
01:39:21: do is previously we're just testing the design  and then iterating on that. Um now I'm going to    
01:39:24: discuss like functionality. Hey, this looks great.  I created a new task using the new task button,    
01:39:30: but when I went back to check the list of tasks,  I didn't have a content order in the database.    
01:39:34: So I'd like you to double check why that is. It  may be an issue with the adding to the database    
01:39:39: or it may be an issue with the pulling from the  database. If there's a table problem or something    
01:39:42: like that, let me know. While I was doing that,  I noticed that there was an order options section    
01:39:47: on the right hand side of um the new orders page.  It looks like uh there aren't buttons or anything    
01:39:52: here. Like I can't really toggle this on or  off. So just refactor that so there's toggles    
01:39:57: um and those toggles actually do something and  they're meaningful. And then also make sure that    
01:40:02: whatever we're seeing in this chart, it accurately  reflects the data in the database. And then I also    
01:40:09: noticed when I tried oh on the landing page here  it's a mixture of orange and purple designs. I    
01:40:15: just want you to make everything here purple. The  signin button is um almost transparent. It's very    
01:40:21: difficult to see. And I'm noticing that there's no  way to log out once you're logged in. So just add    
01:40:25: that functionality as well. I need to be able  to log out. Can't just stay logged in forever.    
01:40:30: Cool. So I'm just going to pump all that stuff  in and then I'm going to go. So we're getting    
01:40:35: closer and closer to the end result. Cool. also  just made some additional changes. I'm just going    
01:40:39: to head over to new task. I'll say five ways to  increase XYZ. See in the right hand side we now    
01:40:44: have some toggles which looks nice. And I'm just  going to add some keywords. I like the idea that    
01:40:49: we could pick those. So I'll click save. And I'm  still not seeing it in the database, which is kind    
01:40:54: of annoying. Uh must be some problem. Okay. And  I'm just retesting this now. Create new content    
01:40:59: order. Blah blah blah. I'm click save. And looks  like we actually got it in. There is still some    
01:41:04: fake assignees, I think. So, I'm going to  I'm going to have that fix that. However,    
01:41:08: if I click on this now, you can see that we have  the brief and then we also have some keywords,    
01:41:12: which looks really nice. And then we have  some really nice formatted stuff on the right,    
01:41:14: like details, format, word count, deadline, and  so on and so forth. So, big fan of that. We see    
01:41:19: the ID of the order up ahead, which I guess could  be useful if I'm trying to contact my agency. Hey,    
01:41:23: I can't see a thing on my dashboard. Yeah, what's  the ID? Then, when we go to dashboard, we can now    
01:41:28: see this has been updated. And it looks like it's  using some sort of mathematical formula here to    
01:41:33: divide this so that the top of this is always  going to be equivalent to the total number of    
01:41:38: maximum orders in a in a certain period. So that's  pretty neat. I like that. What else did we need?    
01:41:43: Uh we didn't have the ability to sign out. So I'm  just going to double check. Do I have the ability    
01:41:47: to sign? Oh yes, I do. It's just hiding behind  my head again. So at the very bottom lefth hand    
01:41:51: corner, I click log out. Okay. Now I'm back to the  client dashboard, which is nice. Uh what I'm going    
01:41:56: to do is I'll go back to sign up. Okay. And then  that looks pretty cool. And then I'm just going to    
01:42:00: try go back to the actual landing page. Nice. So  it actually did fix this up. Although this landing    
01:42:04: page needs a lot of work, which we're going  to fix up in a moment. Uh and then cool. Yeah,    
01:42:09: we have the ability to sign up. We have the  ability to sign in. I mean, this is pretty    
01:42:11: solid to me. I don't really think much else needs  to occur. I'm going to modify the design on both    
01:42:17: the signin pages, sign up pages, and the landing  pages. I'm going to make the landing page really    
01:42:21: sexy uh just to wow you. And then yeah, I  think I think that's more or less it. Oh,    
01:42:26: I guess what we should finally do is we should  check to see if we if we have middleware. So,    
01:42:30: what happens when I go slash orders? Notice how  it immediately jumps back to the login page. How    
01:42:35: about if I go /dashboard? Nice. How about if I go  orders new? How about if I go settings? How about    
01:42:41: if I go what else did we have? Notifications. We  got notifications. Nice. So, it looks like our off    
01:42:47: middleware is pretty good right now. Um although  I'm obviously going to have to double check that    
01:42:50: with that big prompt that I talked about earlier.  Now, why don't we modify the design? And once the    
01:42:54: design's ready, we can actually push this and make  this public. And then once this is finally pushed    
01:42:58: and made public, we can um round out the the  end of our site and it'll be really high-end and    
01:43:02: really clean. So again, for design, I'm going to  go to dribble and then I'm going to find a really    
01:43:07: nice high quality uh let's just see if we can  find some really nice high quality screenshots.    
01:43:12: I just want like a super sexy hero header, you  know? I want it to just be insane. So why don't    
01:43:16: we go landing page? I just want this to be the the  best thing ever. This is really neat. Elevate your    
01:43:24: trading experience. Liquid brokers. H I think I'm  probably going to want a white mode thing though,    
01:43:30: like a light mode as opposed to a dark mode. Cuz  if I go dark mode, it'll just seem kind of weird.    
01:43:37: So, I think what I'll do is this section over  here that says AI powered adwords that find lead.    
01:43:43: I think I'm going to roll with this. And then I'm  going to try and have some cool animated section    
01:43:47: over there on the right. So, unfortunately,  I think this is about as big as it gets. Um,    
01:43:52: sometimes, again, they don't want you to uh like  I don't know if you can tell, it's kind of blurry    
01:43:57: here. Sometimes, as I mentioned, they don't want  you to uh copy these designs a ton. I'm still    
01:44:01: going to give it my best effort, though. So, I'll  go back here. I'll paste this in. Excellent. Um,    
01:44:07: what I want to do next is modify the landing  page, the sign-in page, and then the sign up    
01:44:13: page. I'm going to attach some screenshots of the  design. In addition, I'm also going to provide    
01:44:18: you a an animation that you could use to run in  that right-hand side pane. What I'd like you to    
01:44:24: do is I'd like you to combine our design with  the design in the screenshot. I want it really    
01:44:29: clean on the left hand side. I want my main value  proposition. I want some hypothetical logos um in    
01:44:36: the center. You could just use some some plain  text for that. You don't need images. Um, I want    
01:44:41: a relatively long landing page here with sections  for product, sections for pricing, hypothetically,    
01:44:48: uh, and then obviously a button up at the top that  says sign in. And then for the video, I want you    
01:44:54: to use this URL. Now, what I'm going to do is I'm  going to paste this in. And then I'm going to go    
01:44:59: back here. And what I want is I basically want a  cool asset. And then I want to like rotate it with    
01:45:04: AI. And I'll show you what I mean here. Uh, but  basically I just want some sort of asset. Let me    
01:45:08: see what can we get from dribble that looks really  clean. Okay, so for that I'm going to go over to    
01:45:12: dribble and go 3D shape. Um, I really like one  of these shapes, but I think I want this on like    
01:45:20: a white background. Let me see if we could get  something that might make more sense. H organic    
01:45:26: 3D shapes over here. This is cool. Round egg 3D  shapes. That's kind of neat. Feel like this would    
01:45:32: be nice if we could get a white background on it.  So, why don't we give this a try? What I'm going    
01:45:37: to do is I'm going to take an image of this. Then  I'll go over to Google video. Actually, sorry. Why    
01:45:45: don't we start with Nano Banana? So, I'll go to  AI Studio.google.com. You can sign up for this    
01:45:52: um you know, it's the same account that you  would use for whatever credits you utilized for    
01:45:57: um Gemini and anti-gravity. Then I'll say, let's  see, playground. And I want to generate images.    
01:46:03: I'm going to paste this in. So, I create me a  new organic shape that looks like this except    
01:46:10: with a fully white background. It should look  very sexy and have a purple blue hue to it. And    
01:46:20: then the aspect ratio, I think, is going to be 34,  which is three wide and then four high. And we're    
01:46:25: going to go 2K for the resolution and press enter.  Okay, just ran out of token, so I had to go to a    
01:46:31: different account here. But it's important that  the aspect ratio is 34 and the resolution is 2K    
01:46:35: because that's approximately the same height of  the design that I wanted to copy a moment ago,    
01:46:39: right? Like this one is clearly taller than it is  wide. And I think that's going to be important.    
01:46:43: Okay, so we have this organic looking image,  which is kind of cool. What I'm going to do is    
01:46:46: I'm going to save this image as. So now this is  like our own image. Then I'll head over to VO3,    
01:46:50: which is a state-of-the-art um image to video  generation model. And then what I'm going to do    
01:46:56: is I'm just going to do the same thing. So let  me just switch the accounts here. And then I'll    
01:47:00: link the API key. Cool. And then what I'm going  to do is enable Google Drive access as well.  
01:47:08: And then I'm going to paste in this  image, one that I just generated a    
01:47:11: moment ago. We'll go 9 by6. Just copy this  image. And then go back here. Paste this    
01:47:18: in which I just downloaded. Okay. And  then I'll say uh rotate this slowly. I    
01:47:26: think 6 seconds is probably fine. So that  the last frame is like the first frame.  
01:47:34: Perfect. Uh 100% white background. Okay. I'm going  to press enter. And now V3.1 is generating me    
01:47:42: uh video. Just playing this. Now we have this cool  organic undulating rotating shape which is really    
01:47:47: neat. So I like that a lot. I'm going to download  this. And now I have the video. I'm going to grab    
01:47:52: this. And then I'm just going to dump this into  public. And then I'll say hero header video.mpp4.    
01:47:57: Okay. And then um I initially said URL, but I  guess what I really meant was like inside of my    
01:48:04: folder. public/hero header video.mpp4. Also put a  dot here. Uh cool. I'm just going to press enter.    
01:48:15: And then I'm going to give it some time and let  it go on its way. Okay. Landing page design is    
01:48:19: looking all right so far. I'm not a big fan of  this video now that I'm looking at it. Like I I    
01:48:23: would love it if it just blended in seamlessly,  but for whatever reason, the background is not    
01:48:27: white. We could remove the background and then  we could remove that border and I think it would    
01:48:30: look a lot sexier. I'm partial. I mean, I might  play around with it a bit. Um, we got the logos    
01:48:36: down here. Sign in button top rightand corner.  That's nice. I think we just need to align uh    
01:48:41: what's on like the the left hand side and stuff.  So, yeah, I'm going to do that in a second. Sorry,    
01:48:45: I just realized I was dictating. And then I'm  just going to give it some instructions. Hey,    
01:48:49: this looks solid. Why don't we align all content  to the hero header? Because right now some of the    
01:48:56: sections are really tight. So push it out so that  everything's at the same width as the hero header.    
01:49:05: Um I'm loving the colors. Something with the graph  under the why they prefer Taskbo section looks a    
01:49:12: little bit weird. I think the numbers on the cards  of the maximize your traffic with the content    
01:49:19: engine that generates section um are broken or  something because they're being cut off. So fix    
01:49:25: those. And then everything else looks really  solid. Just update the business name from taskb    
01:49:31: to content hamster as well. Uh and just do that  across the entire app. And then while I'm at it,    
01:49:39: I'm going to see if I could find something that  looks a little bit better for that section here.    
01:49:43: Okay, I found this video and I really like  this. I also think probably because this    
01:49:47: is already optimized, like the file size isn't  really big, I'm probably just going to use it.    
01:49:51: This is not a live SAS app. So, Ashkat Ash Moana,  great job on said design. Um, we're just going to    
01:49:56: be using this as a a demonstration purpose. Um,  it looks like he also allows you to explore or    
01:50:02: tweak this scene by checking it out in his spline  community page. I don't even know what that means,    
01:50:07: but I think it's like a way you can share designs  and stuff like that. So, that's kind of neat. Oh,    
01:50:11: wow. I can actually revolve it. That's so cool,  dude. Wow. So, I guess you could probably run    
01:50:15: this as 3D in your browser. Anyway, we don't want  to do that. That's just a little too much. Um,    
01:50:19: but I'm going to instruct the agent to use that  image and then make sure the orb doesn't get    
01:50:24: cut off weirdly. Also had a couple of sleek  cards placed on top of the video with a glass    
01:50:27: isomorphism effect. So, something to break it  up a bit. And then I'm just going to jump back    
01:50:31: over to our app here so we can see um as it's  actually being developed in real time. You can    
01:50:36: see we changed the name to content hamster.  Kind of silly, but uh whatever. This has now    
01:50:41: done everything perfectly with left-hand side  um margin match up which is nice. Why they    
01:50:46: prefer content hamster? This has now been spread  out. So the graph is no longer all weird. Again,    
01:50:50: perfectly margin aligned. Something with the  numbers is still off. So I'm going to have it fix    
01:50:54: that as well. Let's just do that before I forget.  Hey, numbers on cards are still a bit weird.  
01:51:04: Screenshot for reference. Then as I scroll  through, is there anything else? plus premium.    
01:51:10: Okay, ready to level up your process. Cool. And  then we also have a bunch of buttons down at the    
01:51:16: bottom here that obviously don't really work.  Okay, cool. This looks really clean. I'm liking    
01:51:19: this. I'm liking this a lot. Um, I'd say the only  thing that's missing is probably like the coloring    
01:51:24: across the board. Um, what I'm going to do now is  I'm just going to match all of the colors to this    
01:51:30: because I just love the way that that looks. Uh,  I'm just going to take a screenshot here and then    
01:51:35: I'll say colorfinder online and I'm just going to  paste in this color. And as we see here, there's    
01:51:45: this hex code. So, I like that a lot. And what I'm  going to do is I'm just going to paste this in as    
01:51:48: well. Also, I want you to update the primary color  scheme across the entire application so that it is    
01:51:55: that shade of baby aqua blue. Looks really cool.  use slightly darker shades of blue as accents,    
01:52:02: etc. And then for the accents, I guess I'll  just go back to this. Screenshot it. Paste    
01:52:11: this in here. And then we can use stuff like this  as well. Um, and let's go a little lighter here.  
01:52:21: We'll go this dark. Darkest. Cool. And now it's  going to go through the entire app and just change    
01:52:26: it to reflect like the background colors of this  which I think are going to be really cool. Um,    
01:52:31: obviously I don't want, you know, us not to be  able to see the text. So I am just going to be    
01:52:34: around like, you know, if this is that color, it  will seem kind of weird. Right now we obviously    
01:52:38: have a cool purple thing going on with all the  highlighted text being purple and then these    
01:52:41: things being purple. I do think it would just  match really really nicely and seamlessly if we    
01:52:45: had that. So we'll give that a try. All right,  this is looking way better. I'm loving how the    
01:52:48: baby blues actually reflect what's going on here.  Let's click try out for free. Um, actually I guess    
01:52:53: I already have an account, so I'll just log in.  But we are going to test that out in a second.    
01:52:57: Looks like those numbers have been fixed, which  is cool. We got that slight zoom in on each card    
01:53:01: as well, which I really like. And then baby  blue effect everywhere. That's gorgeous. Um,    
01:53:05: this little content output graph is still purple.  So I'm just going to see if we change that. One    
01:53:09: thing I didn't really talk about was mobile  optimization, but um, Gemini Mobile optimizes    
01:53:13: everything really, really well just out of the  box. Obviously, we do have some minor issues    
01:53:16: with the bounding boxes of this um, like video,  the border. Uh, but this is something that would    
01:53:21: probably be better done by actually replacing the  core underlying asset because the resizing of the    
01:53:25: border box occurs basically perfectly. Um, but  just giving you an example of what it might look    
01:53:30: like on a tablet. As you can see, everything  is still basically perfect. I haven't ran into    
01:53:34: major issues so far. Even the numbers and stuff  like that are visible. And if we scroll all the    
01:53:37: way down, the biggest problem is just there's this  little black overlap. I want you guys to know that    
01:53:41: I haven't even done mobile optimization yet, which  is typically just like a line in the prompt. Um,    
01:53:45: really, really wild that it does this good of a  job without me even having to tell it. Cool. And    
01:53:49: now we have everything changed. So content output  is nice and changed. Uh you know the the the look    
01:53:54: of the little bubbles here goes up. I mean this is  basically exactly what we wanted. I also changed    
01:53:58: the name to content wheel obviously. So why don't  we now sign up and go Nick Sarif. We'll call    
01:54:04: myself Leftclick Inc. We'll just use a slightly  different email this time just so we could retest    
01:54:08: the sign up. Uh let me just make sure this is a  simple ass password. That'll always be the same.    
01:54:13: Cool. We're going to click sign up now. Account  created successfully. Please check your email to    
01:54:17: confirm your account. Uh, I'm now going to sign  into the specific mailbox that gave me that. So,    
01:54:22: let's go here. You can see it's saying to confirm  my sign up here. So, I'm just going to go back and    
01:54:26: then I'll now be able to sign in with the specific  email that I just put in. We'll click sign in.    
01:54:32: Just delete all this stuff. Cool. And I'm just  going to zoom in a bit so we can see. Obviously,    
01:54:35: I have a really big desktop so it won't always  look like that. Um, cool. We have total tasks.    
01:54:40: You can see the styles been updated a little blue  here because I just wanted it to be blue. Um,    
01:54:44: task completion is still purple. So, I think I  may update the graph. I don't really know to be    
01:54:48: honest. It might be okay. My tasks inbox. Cool.  All that stuff looks good. So, we'll now test    
01:54:53: the new task. I'll say, "Hey, this is an example.  Here's my example brief ABC." And then over here,    
01:55:02: we'll go 13. I'll click save order. Cool. We now  have it in our database. It's now a draft. So,    
01:55:08: content is being written. Your writer's currently  working on it. You'll see it when it's ready.    
01:55:11: Inbox. Cool. Um, awesome. I mean, this looks  pretty solid to me. I don't see any major    
01:55:15: issues. So, we'll go to settings. We can update  things. I don't know if this got saved, that    
01:55:20: little leftclick thing. Yeah, it doesn't look like  that did. So, now that we basically have like the    
01:55:25: whole app ready to go, we just need to make a few,  you know, minor changes before we deploy. Hey,    
01:55:31: uh it doesn't look like the company. Okay. And  then after a full endto-end check, this website    
01:55:36: and app is now ready to be pushed um and actually  deployed. That deployment is going to occur on    
01:55:41: Netlifi like I talked about earlier. And I'm going  to give you guys a simple simple process that you    
01:55:45: guys could use in order to actually push that out.  For now, I'm going to go grab some lunch since I'm    
01:55:48: pretty hungry, but I'll BRB. So, the strategy  I'm going to use in order to push this site and    
01:55:52: make this web accessible just like we did with our  old website is to use Netlefi. And in order to do    
01:55:59: that, we're going to use Netlefi CLI and then give  the vast majority of the work to the model. Um,    
01:56:06: so Netlefi CLI is basically just a command line  interface. That's what the CLI stands for. That    
01:56:12: lets previously people like you and I, but now  mostly agents interact with the Netlefi API,    
01:56:17: which is like their little application programming  interface. The way that you uh do various actions    
01:56:23: on Netlfi using HTTP requests autonomously for  you. They can actually do most of it. So what I've    
01:56:29: done here is I've actually just said, hey, I want  you to build this and then I want you to push it    
01:56:33: on Netlfi. We've gone through the whole build.  We've gone through phase one, two, superbase,    
01:56:38: you know, phase three and now what we're doing  is we're doing this final production deployment    
01:56:42: and this is uh you know just uh part and parcel  more or less the final step of getting this thing    
01:56:49: on the internet. Now, I should say that when you  actually push things to production, that's what    
01:56:54: that's called, typically there are some issues  because the development environment that you run    
01:56:59: on your local computer is always going to be a  little bit different than whatever the heck the    
01:57:02: server is using. And so, sometimes you have  to make minor changes to the site. Sometimes    
01:57:06: you have things that work on your device, but then  don't work obviously on the production server. So,    
01:57:11: you have to, I don't know, modify like the the  way the database works, some of the permissions    
01:57:15: and stuff. And that's just part of dealing  with any sort of full stack application.    
01:57:19: wasn't a big deal with our website because our  website was obviously not super interactive. It    
01:57:23: was just a bunch of uh links. But this has some  back and forth and that's what's important. So,    
01:57:27: as we scroll up here, we can see this has actually  gone through the build process, which is basically    
01:57:33: taking our website or what our website should  look like and then turning it into like an    
01:57:37: actual instantiated version of the site. That's  what that is. Um, and now it's going through the    
01:57:41: installation process for the actual Netlifi CLI,  which is a little package. And now it's going to    
01:57:45: communicate with the Netlefi CLI. And all we  have to do is we just have to authenticate. So    
01:57:50: assuming we have an account set up and stuff  like that. And what we have to do is we have    
01:57:52: to go and actually log in. So what I'm going to  do is I'm going to open this up. So I'm going to    
01:58:00: um give it a new terminal tab which is what it's  asking for. You can do that by going control shift    
01:58:06: um tilda I think it's called. It's like that  little thing in like the top leftand corner.    
01:58:11: It looks kind of like this. Uh you should also be  able to do this by going up to the top and then    
01:58:16: going terminal and then going new terminal. And  then I'm just going to paste this Netlefi login    
01:58:21: command. And in my case, you know, I've already  done this on my machine a bunch of times. So it'll    
01:58:25: say it's already logged in. In your case, uh you  know, if you haven't done this login before, it'll    
01:58:29: just pop up a little Netlify panel and then you  can do it there. So I'm going to say done. And now    
01:58:33: it's going through the various building procedures  and so on and so forth. So, my expectation is I    
01:58:38: mean there's like a 50% chance we oneshot this  because we are using a pretty standardized    
01:58:41: framework called next.js. Uh there's a 50% chance  that we're going to have to go back and forth.    
01:58:46: It's saying the deploy is live. I'm just going  to refresh this and check for myself. Okay. And    
01:58:50: you can see we did push the actual website side  of things up. So, that looks good. Just exit out    
01:58:55: of this so we can get like the the full glory of  the site. And I'm not seeing any major problems    
01:59:00: here versus the one that was on my machine, which  is cool. You know, we got these little buttons.    
01:59:06: premium get started now. Okay. And I mean, we  haven't added links to all these yet, which is    
01:59:09: why these aren't actually popping up. Uh like  changing my um little cursor when I mouse over,    
01:59:14: but that's okay. And now what I'm going to try  is actually the interactive component. Cool. So,    
01:59:18: we have the account created successfully modal.  And that's great. I'm now going to head over to    
01:59:23: that specific email address and just check if we  have the email confirmation message. Okay, we have    
01:59:27: this right here. So, I can confirm my mail. And  now we're starting to see one of the issues. So,    
01:59:32: error parsing package.json JSON file. And it looks  like the reason why we're getting that is notice    
01:59:37: the URL up here. The URL is not actually uh the  publicly accessible URL. It's this localhost 3000.    
01:59:44: And so the way that you know user signups usually  work is basically there'll be some URL here slash    
01:59:50: some code and then the agent will configure your  Nex.js or whatever full stack app framework you're    
01:59:56: running to like accept this code and then  use that to verify the account. But basically    
02:00:00: what's happened here is the default sends us to  localhost 3000. And so I know what the issue is,    
02:00:05: but just for the purposes of like debugging and  stuff like that, I'm actually going to just take    
02:00:08: this to my agent and I'll see what the agent says.  We have to go back into our Superbase settings    
02:00:12: and then alter it. But I do just want you guys to  know like how this works if you guys are actually    
02:00:16: debugging it. So I'll say I received this error,  this um call back when setting up my account.  
02:00:27: this isn't the right URL. What should I do? And  you'll see here it'll instruct us to go to our    
02:00:34: Superbase and and make some minor changes. And  then it's going to tell us to update our Superbase    
02:00:38: dashboard settings. So, go back into my dashboard,  which is right over here. And then there's going    
02:00:44: to be an authentication page right over here on  the top left. And then it's either going to be    
02:00:49: an email or somewhere else. Like we can actually  turn off the um confirmation completely. This is    
02:00:54: the email that Superbase sends them. That's why  it looks a specific way. And I don't know, to me,    
02:00:58: it kind of looks a little ugly. So, obviously, if  I were running a full production app and I were    
02:01:02: making all those uh little bells and whistles, I'd  make this look really pretty. But I think there's    
02:01:07: actually a way to change the URL. Okay, here  it is. It's right under URL configuration. It's    
02:01:12: a site URL. And so, what I'm going to do instead  is I basically just want to get the the live URL,    
02:01:18: which is this one here. Just going to paste that  in. Okay. And I'm going to remove that back slash.    
02:01:24: So now this is going to be the URL that it uh  basically redirects us to on Superbase's side    
02:01:29: cuz Superbase handles the the signups and stuff  like that. And now when I go back to the app,    
02:01:35: I don't even have to actually make any uh major  changes like I don't have to rebuild the app or    
02:01:39: anything. Then I can give it an email. I click  sign up here. And now we have another email sent    
02:01:48: to another one of my addresses. There you go. It's  right here. When I mouse over this, you guys can't    
02:01:52: really see in the bottom lefthand corner, but  I'm no longer going to localhost. And you can    
02:01:57: see if I click on this, takes me to contentorb  dashboard.netifi.app/lo. So here I can actually    
02:02:06: um now jump in and log into the app. Cool. So  that's one of the first changes I would say if    
02:02:13: you're building something on production versus  doing something locally. We just have to change    
02:02:16: the URL that the authentication goes to. So  we just did that. Now it's nice and clean.    
02:02:20: And I'm scrolling up and down here, making sure  there are no major issues that are egregious. I'm    
02:02:26: not seeing any problems. I guess the company isn't  filling in. So, we can change that. Well, I write    
02:02:31: this. Save. Give this a refresh. Yeah, looks like  the company in the profile details isn't filling    
02:02:35: in. So, I'm just going to take a screenshot  of this and then I'll paste this in. And then    
02:02:39: while I'm like before I actually send this, cuz I  prefer just to do a bunch of stuff, not just one,    
02:02:43: let me test the new order. This is a new order.  What's up? And then over here, I'm going to go  
02:02:54: one word and then I'll save. Okay. So, yeah, this  is actually in my database now, which is pretty    
02:02:58: cool. I can click on this. Looks like the rest of  this stuff is is here, which is nice. Anything in    
02:03:04: my inbox? Nope. That's cool. And then my actual  orders do populate, which is nice. And we don't    
02:03:11: actually have like the ability to like we don't  have any people on our team, but obviously we    
02:03:14: could have added some, which is why we still  have those little um little fake Notion-esque    
02:03:18: people there. I wonder where they're getting those  images from. That's kind of cool. Okay, so uh we    
02:03:23: have dashboard. Did we I think we checked settings  as well. Yep, that looks pretty good. And I think    
02:03:29: every other toggle here probably works. Let me  just try searching the tasks. So I'll just go O  
02:03:38: H. Okay, so yeah, clearly it's just searching  based off the letters. If I type in new order,    
02:03:43: if I type in old order, then it won't be.  Okay, cool. So if we had 20 in here, you know,    
02:03:46: that might actually be useful. And let me just  check the sign-in page. Okay, cool. So, we're    
02:03:51: immediately being logged in when we click the  signup page. And then, you guys can't see this,    
02:03:54: but in the bottom left corner, I'm just going  to click log out and see what happens. Okay,    
02:03:57: so when you click log out, it takes you straight  back to the login page, which is the desired    
02:04:00: expected behavior. And then nothing is prefilled.  Let's now check all of our routes. So, I would    
02:04:06: always recommend going through every single one.  So, that's dashboard. This is settings. This    
02:04:10: is orders. This is orders. um I think and then  slash new and then there's also a notifications.    
02:04:17: So notice how none of these are automatically  signing in which means some of our off uh is    
02:04:21: fine and you know all of our animations and stuff  like that look really clean and uh there there are    
02:04:26: no problems on that end. Okay. And then I'm just  going to do a final spot check because although I    
02:04:31: told it to um you know mobile optimize the site, I  do want to make sure that it is mobile optimized.    
02:04:36: This looks really clean. You know the only issue  here is with this little background not being    
02:04:41: necessarily the same as that. I guess we could  just change the background color of this whole    
02:04:44: element. That might actually help. So, yeah, why  don't I do that? That's a really cool thing. Um,    
02:04:48: why don't we adjust the background element of our  little orb to this? Adjust the background color of    
02:04:58: the element that contains the animated orb to be  the same as that background color of the orb. This    
02:05:02: should be our light aqua baby blue. Okay, that  looks nice. And then just scrolling through here.    
02:05:08: Any other issues with the mobile optimization?  Just make this really nice and small. Be 100%    
02:05:14: sure. Nope. Everything here looks like Oh, you  know, there is one. Looks like this learn more is    
02:05:20: not immediately underneath the get started now.  So, that's one final thing that I'll do. I'll    
02:05:26: finally say also the learn more button is not um  underneath the what was the name of that button?    
02:05:33: Get started now button. So, I'd like you to line  them up on mobile. Now I should know because    
02:05:37: this is no longer local on our computer. It's on  netlefi the uh debug in an iteration loop takes a    
02:05:44: little bit longer. Naturally when we were just on  our computer anytime we'd have an issue we would    
02:05:48: just say hey rebuild it. It would rebuild it and  then we'd immediately have access to it. Right?    
02:05:51: But here we actually need to make the changes  locally on our computer push them to Netlefi    
02:05:55: have Netlefi do the build and because Netlefi is  sort of doing free server space takes longer and    
02:06:00: then we actually have to go online and then um  you know take a peek at the website. But anyway,    
02:06:04: I'm uh just going to open this up now. This is the  production version. I should be able to see the    
02:06:10: background and everything like that. Nice. And now  we have more or less my exact desired behavior,    
02:06:15: which is how that orb just looks like it's  floating. And it doesn't matter how big or    
02:06:19: small the website is. It's just like perfectly  contained within those bounding boxes. Super    
02:06:24: clean. Um and then I just had a couple of those  other changes. Just going to verify that those    
02:06:28: are good. The last thing I'm going to do is I'm  just going to go down to my security audit prompt.    
02:06:32: scroll all the way down to the bottom. And  there's just a little bit of nuance here. Um, I'm    
02:06:36: not actually going to do this in the same thread  that I launched and built the entire website. So,    
02:06:40: I'm going to use Claude Code for this instead of  Gemini. And the reason why I'm doing it is cuz I    
02:06:44: don't want any context. I basically want the model  to look at this entire codebase as if it's new,    
02:06:48: fresh, and not mine, like somebody else's. And I  want it to like run through this whole checklist    
02:06:52: and to end and tell me whether or not it's  configured. Okay, so I just copied this all.    
02:06:57: I'm going to head back to anti-gravity. Close  these tabs. And I should just be able to do so    
02:07:01: by clicking close all. Let's make this smaller  because we're going to have clawed code instead.    
02:07:07: And then what I'm going to do is I'm going to  paste this in. Then I'm going to say don't make    
02:07:12: any changes. I just want the audit. Okay. And I'm  going to pump this in. And now cloud code is going    
02:07:19: to go pass one discovery map the full architecture  and then more or less tell me, you know,    
02:07:24: what's good, what's bad. And I'm doing this for a  couple of reasons. Um, obviously I want no context    
02:07:29: as mentioned, but I also think that Claude is a  lot more interpretable than Gemini right now. If    
02:07:33: you guys check out the thinking tabs here, and  if you compare them with the thinking tabs of,    
02:07:38: you know, Gemini, Gemini uses language that just  doesn't really make much sense. Um, you know,    
02:07:42: when you look at it, it's not as interpretable.  I'm now taking action to apply the color    
02:07:45: adjustments as previously decided, focusing on  the background's visual look. I'm now proceeding    
02:07:48: by updating the styling to use desired hex code.  You if you look at it and just compare it to this,    
02:07:53: this is a lot more interpretable. I now have a  comprehensive understanding of the codebase. Let    
02:07:56: me compile the architecture summary and then  work through every checklist item. They give    
02:07:59: it to me sort of in plain English. And so the  interpretability is pretty important when you're    
02:08:03: talking security, right? Um in addition, you  know, I just think Claude is a little bit better    
02:08:07: at like security based stuff right now. Okay,  so I'm I'm reading through everything here. It    
02:08:12: looks like most of our audits are correct. We  do do console. Calls, which is important. Um,    
02:08:18: this is basically a way to minimize the attack  surface uh and then minimize or maximize    
02:08:23: operational security. We're not really giving  away how our underlying tool works. So that'll fix    
02:08:28: that. Startup validation. Okay, so we need some  sort of startup validation here. It looks like  
02:08:36: we can't tell whether or not the RLS is enabled  um because we don't actually include the files in    
02:08:40: the codebase, but that's okay. We are actually  good on RLS. Uh that's why it's giving us this    
02:08:44: warning message as opposed to a no. We're good on  SQL injection, security definer functions, same    
02:08:49: thing as uh previously. So we could have um claude  like connect to our superbase instance via API if    
02:08:55: we want. And I'm just going to take all of this  default deny routing fails. This is important.    
02:09:02: Remember how I talked about O middleware? This  basically just immediately denies all requests    
02:09:05: that don't have some form of authentication. Right  now our app doesn't do that. And you know, at the    
02:09:11: end of the day, we while are okay on most things,  we're still missing some uh some things there. So,    
02:09:17: I'll say excellent execute all of the changes.  Okay. So, I'll say um the SQL stuff was already    
02:09:27: taken care of. RLSTC, but thanks for pointing  that out. Execute all of the remaining changes    
02:09:35: and change SQL checklist items to green. And now  it's going to go through and then work through the    
02:09:42: fix the systematically form. And just to give you  guys some more visibility in the security side of    
02:09:45: things, you know, previously we had a line in our  code that said if there's an error, we actually    
02:09:49: add all of the superbase insert error details  here. This is actually just like gives a bunch    
02:09:53: of information about the way that our superbase  database is configured. And that's just because    
02:09:56: Jeem and I wanted to write it in the way that was,  you know, debugable for us if you guys remember.    
02:10:00: Well, this now went through it identified that  and it changed that to fill to create order,    
02:10:04: which is just much more general. And um that both  gives us the ability to quickly see if there is an    
02:10:08: issue, but then it doesn't expose any of our  underlying in infrastructure architecture if    
02:10:14: somebody actually wanted to attack us. As you  can see, we have most of the changes that we    
02:10:16: talked about before. We have allow list routing.  We have client side user ID filtering. Okay,    
02:10:20: server side validation. We added what's called  an off call back route. Um we have environment    
02:10:25: variable validation. And we also had some console  leaks that we've since cleaned up. And just    
02:10:30: scrolling through to get to that checklist,  you know, the vast majority of these are now    
02:10:34: green. all the issues that we had previously have  been taken care of. And so 5.1 which was a dev    
02:10:39: dependency and then 6.2 which was some built-in  rate limiting. You know, we don't have control    
02:10:44: over that. And these aren't really large security  issues as well, which is why they're in this    
02:10:48: yellow little warning label instead of the X. Um,  you know, we're now good. We've basically solved    
02:10:52: for the 8020. The vast majority of lowhanging  security fruit do no longer apply to our app.    
02:10:58: And while I probably wouldn't scale this to like a  million users without at least having some sort of    
02:11:02: security person look this over, it's pretty dang  good. I just did a final walkthrough of the site.    
02:11:06: We have the animation, which was previously  hidden because of that middleware update. Um,    
02:11:10: some of our icons are missing as well because  of that same thing, as well as the login uh and    
02:11:14: signup routes, as well as every other feature in  our network. So, this is an example of like that    
02:11:18: extra step at the end that a lot of people don't  want to do because obviously it takes, you know,    
02:11:22: an additional 15 or 20 minutes. It's about how  long it took me, but I highly recommend it if    
02:11:25: you do plan on making your app live. and actually  launching it to more than just yourself and your    
02:11:30: close friends and family. But congratulations,  we have now built an endto-end full stack app    
02:11:35: with login, authentication, signup. We have a  database where we store records and queries and    
02:11:40: then also a pretty sexy landing page. You guys  now know everything that you need in order to    
02:11:44: basically take this knowledge and then go out and  actually just vibe code an app. What I want to do    
02:11:47: next though is I don't just want to vive code any  app. I want to take you guys to a higher level of    
02:11:52: understanding of modern software engineering  principles cuz I think it's one thing to be    
02:11:55: able to just use natural language to, you know,  communicate with agents and have it do something.    
02:11:59: But some of these architectural decisions that  the agents are making are actually controllable    
02:12:02: by you. And if you know even 10% more than  the average Vibe coder, you can, you know,    
02:12:07: rather than this process takes 2 or 3 hours, you  can basically just build like your little starter    
02:12:12: kit with um your preferred stack, your preferred  tooling, and then some preferred examples.    
02:12:17: you can get to the point where you could actually  just like oneshot uh an app like this. Maybe not    
02:12:20: completely oneshot but like 1.5 shot it. Take uh  app creation which previously might have taken    
02:12:25: a very very long time because of all these  small little decisions that you and I have    
02:12:28: to make and then get it to a point where it's  it's much faster. And not only that, I think    
02:12:32: you'll probably gain a lot more appreciation for  software engineering as a whole and then become a    
02:12:36: better developer um whether or not you're working  in conjunction with agents. So let's do that next.    
02:12:41: Now, I should know that this isn't going to  be a comprehensive software engineer degree    
02:12:46: or anything. In fact, I know there are going  to be some software engineers in the comments.    
02:12:50: They're going to look at what I'm talking about  and probably laugh. They're going to say, "That's    
02:12:53: not how to actually host. That's not how databases  work or whatever the heck." The reality is, you    
02:12:59: don't need to know all of the internals of how all  of these different things were put together. These    
02:13:04: are essentially things that were built over the  course of the last 50 or 60 years. And nowadays,    
02:13:09: even the most competent developers typically  just stand on the shoulders of giants. And so,    
02:13:13: I'm going to give you a very high level overview  here. And this high level overview will, like the    
02:13:16: rest of the course, be the 8020 that allow you to  dive deep into specific parts if you so want to.    
02:13:22: Um, but you won't necessarily need to hear me  yap on for 700 hours about different database    
02:13:26: architectures. Okay, so we're going to start with  hosting. To make a long story short, hosting is    
02:13:31: just the technical term for running your web  application on a server. works on my machine    
02:13:37: is the scariest thing a developer could say. So,  it's important to do this right. You know how a    
02:13:42: few minutes ago when I was developing that app  and then pushing it live, there were immediately    
02:13:46: some problems. Well, what a lot of developers will  do is they will develop entirely locally and then    
02:13:51: they'll say, "This works fantastic, amazing." And  then they'll leave the pushing and the deployment    
02:13:55: and and you know, all the hosting and stuff like  that is sort of an afterthought. And then when    
02:13:59: they actually do push it, then there's a bajillion  problems and the app doesn't really work. And then    
02:14:03: as you saw there's also a longer feedback loop  because now this is live on the internet it's not    
02:14:06: on your machine and that longer feedback loop can  make you know that last mile problem where you've    
02:14:10: done 99.9% of the work uh of your app but then  that.1% takes like 100 times longer just because    
02:14:15: of the nature of your your prepare preparation  or lack thereof. So in order to really get this    
02:14:21: we just need to give a brief highle walkthrough  of how communication um on networks tends to work    
02:14:27: or like on apps. Basically on the left hand side  here we have a client. And for all intents and    
02:14:32: purposes, let's just say this is um your browser.  Okay. Now client is just such a silly name. I    
02:14:38: would say not a lot of people really understand  this, but I just replace basically all instances    
02:14:42: of the term client with just your browser for  now and everything will make more sense. Now your    
02:14:46: client, okay, it's just your browser. It needs  to communicate with a server in order to have    
02:14:52: some sort of back and forth. And so this server,  okay, could actually be like your um computer if    
02:15:00: you're developing locally or if you know you're  pushing to some, you know, service or whatever,    
02:15:07: it could be something like well maybe Nellifi  isn't the right example, but I don't know. Yeah,    
02:15:10: I don't know if you guys ever used Hostinger for  instance, not affiliated with them, but um that's    
02:15:14: a good example of one. Or let's just see Hostinger  alternatives. Blue Host, if you guys have ever    
02:15:21: developed a WordPress website or Cloudways or Site  Ground or Insta. Basically, these are services out    
02:15:28: there that run computers just in the cloud that  you can then access in order to like push stuff on    
02:15:34: it. Okay? So, what happens is your client, okay,  your browser will communicate with the server,    
02:15:39: which if you're running stuff locally is either  just your computer or it's somebody else's    
02:15:43: computer on hosting or site ground or whatever  other service. And then it'll send initially some    
02:15:49: very simple and brief requests, okay, for things  like um you know site HTML. It'll send uh requests    
02:15:57: for things like uh database data and whatnot.  And so your server has the ability to do a lot    
02:16:02: of its own logic and whatnot. And so in general,  what clients um are for are they're just for like    
02:16:08: presentation. And then what servers are for is  they're more for like the heavy lifting and the    
02:16:12: logic and the validation and stuff like that.  That's why server side validation is much more    
02:16:15: important than client side validation. That's why  it's a big security risk. The thing is in addition    
02:16:19: to the server, there's like a third piece called  your database where we actually store like a    
02:16:24: row or tabular data. And you know, for all intents  and purposes, your database is just one big Google    
02:16:29: sheet. There's like an ID column, there's like a  date created column, there's like a I don't know    
02:16:34: value column, and then there's uh just a bunch of  stuff here. um where basically what your server    
02:16:41: does is it will make a request to this database  to receive specific pieces of data that the user    
02:16:46: has requested. So if the user has an ID of 23 foi  whatever, okay, and then you know the request is,    
02:16:53: hey, I just want you to grab the value. What it'll  do is it'll return 2 3 4 2 3 4 um over and over    
02:16:57: and over and over again. Okay, so that's that's  pretty cool. Um the reason why we split these two    
02:17:02: up is just servers are obviously computers. This  is obviously just data. Data are not computers,    
02:17:07: although computers can contain data. You could  theoretically contain a bunch of information on    
02:17:10: your server, but why would you pay for all that  when you could just use like a highly optimized    
02:17:14: service that just stores a bunch of records and  then communicates really quickly. So anyway, let's    
02:17:18: say our client is requesting some data. Like if  you if you go back to our app, um it's requesting    
02:17:23: that like little dashboard data. Let's see how  many orders do we have in the database. What it'll    
02:17:28: do is, you know, we we'll first we'll sign onto  our app. We'll initially make that request to the    
02:17:32: server. It'll return a bunch of HTML and um any  pre-existing or cache data, okay? And then it'll    
02:17:36: visualize it. And then after, you know, you the  user will navigate on the website and you'll say,    
02:17:40: "Hey, you know, I want to, you know, you'll  you'll click uh the dashboard button and then    
02:17:44: that'll be like, hey, you know, I want to go grab  this data and see how many records I have." So,    
02:17:47: what'll happen is we'll send that request  over to the server. The server has a bunch of    
02:17:51: um pre-built logic basically that says, "Hey,  when a user requests a specific dashboard data,    
02:17:58: I want you to call the database using this format  and then retrieve it." And then we'll say, "Hey,    
02:18:02: you know, we want the dashboard data." It'll  do this in a slightly different language,    
02:18:07: typically SQL, although there are no SQL databases  as well. And then it'll return, you know, that    
02:18:12: dashboard data. The server will do some additional  validation if it needs to, and then it'll just    
02:18:17: return that to the client. And so this is just a  loop that goes on over and over and over and over    
02:18:20: and over again. If the client updates something  like let's say we create an order, well, it's the    
02:18:24: exact same thing. We'll just send a request to the  server. The request will say create order. Server    
02:18:29: will be like, okay, cool. So here's how I create  an order. Then it'll take that request and send    
02:18:33: it to the database which will then add a new order  to like your orders table. So very very high level    
02:18:38: um overview of how basically these modern web  apps work. And I'm going to talk a little bit more    
02:18:42: about like the prevailing frameworks in a second  because there are now apps out there kind of like    
02:18:46: this service I'm using right now called Excaladraw  which does things both online but also locally.    
02:18:50: And you can really dive deep into that rabbit hole  if you want. But um without further ado, what's    
02:18:56: the actual development process look like? Well,  for us it's basically we just start local. So when    
02:19:00: we start local, we run both our client and our  server on the same computer, right? Our client is    
02:19:04: like our browser and then our server is just like,  you know, your your your computer running that    
02:19:08: process. Then we test and verify just like I did  a moment ago for my app. And then once we're done,    
02:19:14: we push to what's called a staging server, okay?  Which is sort of like an intermediary between    
02:19:19: um having everything on your machine and then have  everything accessible to your customers. Once it's    
02:19:23: on a staging server, we then test and verify.  And then once we're done testing and verifying,    
02:19:27: then we and only then do we actually push to  production, which is like the thing that um    
02:19:30: customers and and users can actually use. And so  the process is basically always just like um local    
02:19:37: staging production. And this is not super relevant  for our last step, but it'll become more relevant    
02:19:44: when we use things like GitHub repositories and  version control because there are changes that    
02:19:49: you can make locally. other people can be working  on changes on the staging server and then other    
02:19:53: people can be working on changes even on like  the production server. Although ideally you    
02:19:56: don't make live changes because a single live  change can like screw up your your whole work    
02:20:00: um like your whole app like you saw earlier. Uh  and then you can actually just spread it across    
02:20:04: have multiple people working on multiple things  simultaneously. So that in a nutshell is basically    
02:20:08: everything you guys need to know about hosting.  Um you do obviously need to pay for hosting for    
02:20:12: most services like you know you're not going to  be able to sign up to hosting or or site ground or    
02:20:16: whatever for free. This is basically you renting  a computer for the purposes of hosting your    
02:20:21: application on it and then having users interact  with it. And obviously every time some user goes    
02:20:25: to a website or whatever and there's a request  made to the host, the host consumes a little bit    
02:20:28: of electricity. There's like a little bit of of  a cost back there. So they um they arbitrage that    
02:20:33: and then they charge you some big multiple. And  there's like a bajillion hosts out there. There's    
02:20:36: like VPS's, virtual private servers. There's like  dedicated um computers or dedicated servers you    
02:20:42: could buy. There's like whole computers basically  or whole servers that you could buy. Or what they    
02:20:47: do is they take one server and they divide it into  like 50 servers and then slowly partition it out.    
02:20:51: There's like so many different ways of doing this  that it's not really worth us getting into. But    
02:20:54: suffice to say, this is just like the basic model  of um communication. Another thing that's really    
02:20:57: important to understand are databases. Now, for  all intents and purposes, like I talked about,    
02:21:01: these are basically just like a Google sheet.  If you guys have ever used a Google sheet or    
02:21:04: you ever used Excel or anything like that, the  best mental model I found so far is just to    
02:21:08: treat every database that you use like um a Google  sheet. So, just like a Google sheet, you'll always    
02:21:13: have like header row, uh, a header row, which is  basically just like the titles of every single    
02:21:19: column in your database. So, in this instance,  for instance, our table, which I just move my    
02:21:24: big head out of the way, is called sheet one down  here. Okay? And sheet one, okay, is just one of    
02:21:30: many possible tables in our database. We can make  100 more tables if we wanted to, but they're all    
02:21:35: going to be divided into like sheet one, sheet  two, sheet three, or whatever the heck we title    
02:21:38: them. Now inside of sheet one um we have uh three  columns here. The first column has a header name    
02:21:44: or a key of id. The second has a header name or a  key of date underscore created and then the third    
02:21:49: has a a header name or a key name of value. Now  underneath this sort of initial row which just    
02:21:56: defines the names of all of the various fields. Um  we then have the values themselves. And so this is    
02:22:01: a database for instance that contains a one record  or one row. If I duplicated this a bunch and then    
02:22:08: I don't know wrote some other IDs here because  this is going to be important. You can see now we    
02:22:12: have a database um with one table called sheet one  that now consists of four rows. Okay, the thing    
02:22:18: is depending on the type of database that you're  using. Okay, you need what's called a primary key.    
02:22:24: And a primary key is just something that's unique,  one column that is basically always unique from    
02:22:29: row to row that basically defines that row or  that record as like being super unique and not    
02:22:34: existing anywhere else. And so for the purposes of  this database, the primary key is going to be the    
02:22:41: ID because the ID is always going to be different  between each record. If you have two records with    
02:22:46: the same ID, obviously there's a conflict. If you  think about it logically, the reason why we need    
02:22:49: it structured in this way is because if we have  instructions in our server and the instructions    
02:22:53: are to pull a specific record from a database and  it's like, hey, I want you to grab the record with    
02:22:58: the ID 23FI23F2 and it turns out there's like 10  records like that. You'll return 10 records and    
02:23:05: how are you supposed to visualize 10 records? Like  that's going to, you know, it's going to screw up    
02:23:07: whatever your logic is unless you specifically  handle for that. And so these databases for    
02:23:12: the most part, most people that vibe code apps  suffered using the SQL database with um separate    
02:23:16: primary keys are typically organized in that way  where you have one sort of like starred column.    
02:23:21: And so I'm just going to make this one the starred  column. It's the yellow one. And then these here    
02:23:24: can be the exact same. Like you could technically  have 100 records all created in the same day,    
02:23:27: but since they have different IDs, they're all  different records, right? Same thing with the    
02:23:30: value. Okay? So just like in a Google sheet or an  Excel file, you can actually like filter things    
02:23:35: out. Um you can do the same thing inside of a  database. So if I go back to our little example    
02:23:39: here and then um I add a filter which I can do on  sheets really easily just using a little hotkey.    
02:23:44: You can also just go to data and then you could  click on create a filter if you wanted to follow    
02:23:49: along this demonstration. What you can do is  if you click on this little filter button you    
02:23:52: can see that you can now just filter specific  records. Like I could for instance only grab    
02:23:57: um you know this record here 23FI. Okay. And if  I did so it would remove all of the additional    
02:24:02: records here and then I'd only be looking at this  data. And so every time that a server makes a    
02:24:06: request to a database, that's basically what it's  doing under the hood, it's just doing this in like    
02:24:09: a fully automated fashion. Likewise, I can filter  based off of fields that are not my primary key.    
02:24:13: So maybe in date created, what I wanted to do is  I wanted to grab all records that have 2025-10-3.    
02:24:19: So as you can see here, now I'm grabbing multiple  records, okay? But each of these have different    
02:24:22: primary keys. And this is just a way that I could  filter stuff. It's just like using a search bar,    
02:24:26: right? You can do the same thing for value, do the  same thing for whatever the heck else you want,    
02:24:30: um, you know, in your database. So basically  every time that you send a request from you know    
02:24:34: your client your browser by clicking a button  you send that request to the server the server    
02:24:38: interprets it. What it's doing is it's sending  another request to a database which um you know    
02:24:42: is basically just acting like a big Google Sheets  filter. Now the cool thing is there's two major    
02:24:47: types of databases right now. The first is called  SQLbased. So SQLbased is divided into a bunch of    
02:24:53: different popular versions. I mean really there's  like a thousand but three most popular ones right    
02:24:56: now are my SQL postgrql which is probably the  most popular one and then SQLite and then you    
02:25:01: also have what are called NoSQL databases like  MongoDB and Cassandra. How I've always worked with    
02:25:06: the differences is SQLbased databases basically  fix the column headers and so it's always going    
02:25:13: to be the same column headers for all the data  and all of the records that go into a database.    
02:25:18: And so just like here we have those three column  headers ID, date created and value. Basically,    
02:25:22: every single record in this database will always  have an ID because it's the primary key and can    
02:25:27: optionally have either a date created or a value  or it could have both. And so, um, you know, for    
02:25:32: instance, you might get something that looks like  this with a date created and then no value. And    
02:25:37: that is what's called a valid record. Likewise,  you can get something that looks like this with no    
02:25:42: uh, you know, obviously the IDs are going to  be different. No date created, no value. And    
02:25:45: you can also have something that looks like this.  Okay? And you know as long as you have a primary    
02:25:51: key which denotes that this is a separate record  um every other field is optional but it has to    
02:25:56: stick to this structure. Now no SQL databases are  a little bit different in NoSQL I'm just going to    
02:26:02: create a new sheet here. Basically what we have  is rather than having just like one header row up    
02:26:07: at the very top I want you to pretend that every  single item in your database has its own header    
02:26:13: row. And so the first record here will have ID,  date created and values. So let's say the ID is    
02:26:19: this, date created is this, and then the value is  this. Okay? Or I don't know, let's just make it a    
02:26:25: little bit easier. Let's just call this uh we have  a record here called first name. Probably makes    
02:26:30: more sense. And then this one's Nick. So um you  know what we have here is we have one record with    
02:26:35: an ID, a date created, and a first name. Well, for  the next record, instead of just like sticking to    
02:26:40: this format, you could have whatever the heck you  wanted. So I'm actually just going to paste this    
02:26:44: down here. And then I'll say this record actually  has um a last name instead. It has a date created    
02:26:56: column and then it also has a date modified  column. Maybe this date modified as 29th. If I    
02:27:03: added another record here, okay, maybe what I have  here now is I have a full name. This one's Nick    
02:27:11: Sarif. Then I also have my little date created a  little bit over to the right. and maybe there's    
02:27:15: no date modified. And so basically what occurs in  a NoSQL database is every single record has its    
02:27:22: own data structure rather than everything being  100% fixed and looking the exact same like we    
02:27:29: had with our previous uh SQL database. You know,  every record will have an ID. Then it's optional    
02:27:34: whether they have date created or value. But  it's not like they could have another, you know,    
02:27:37: it's not like this row could have another value  called uh first name called Nick, right? Unless    
02:27:42: we explicitly define that up here as a value  or a header that exists on all. Okay. Whereas    
02:27:48: this would be empty empty empty empty empty empty  empty and then this would be nick. Okay. It's not    
02:27:52: like we can just add additional um features or  or types of data. In a NoSQL database you have    
02:27:58: total freedom and flexibility. And it's a lot more  like like a Google Drive folder where you're just    
02:28:02: storing a bunch of different documents and every  single document could look a little bit different.    
02:28:07: Now, obviously for our purposes, we want a simple  way to like call a database and then retrieve all    
02:28:12: records that have a first name Nick Sariah or that  have an ID of of something. Um, you know, we're    
02:28:16: going to use SQL for the most part. But there are  some instances where NoSQL makes more sense. Um,    
02:28:21: and if you want to look more into that, just look  for the difference between like relational and a    
02:28:24: non-reational databases. Um, and then maybe  you could have your agent tell you. Next,    
02:28:28: I want to chat languages and frameworks for people  that might not be super familiar with them. So    
02:28:34: there are three basic languages used these days in  modern SAS app um sort of development engineering    
02:28:41: and I'm going to draw them as little bubbles and  I'll show you how they all interact. The first    
02:28:45: is probably the oldest which is hypertext markup  language. The next I just copy this is a little    
02:28:53: bit newer and it basically took the internet from  just a bunch of ugly static web pages to pretty    
02:28:58: dynamic and interesting web pages CSS. And then  the third is how we got interactivity in the web,    
02:29:05: which is through JavaScript. Now, I'm not going  to give you guys a big historical lesson on each    
02:29:09: of these because to be honest, I mean, I just  be googling this stuff anyway. Um, but suffice    
02:29:13: to say, HTML is actually like basically the only  thing that you need in order to run a website. CSS    
02:29:20: is sort of the design layer that makes things  really pretty. And then JavaScript is just    
02:29:24: what allows you to build interactivity into pages  like you clicking a button and then a new element    
02:29:29: appearing or something. And so to show you guys  this HTML side, if you head over to info.sern.ch,    
02:29:35: you can actually see the very first website ever  made. And that website is called the worldwide    
02:29:40: web. This is literally describing the worldwide  web. You know how all websites or many websites    
02:29:47: have www preended? That stands for worldwide web,  which is a framework that people put together god    
02:29:52: knows how long ago now. probably at least 40  years ago. And so basically this explains how    
02:29:56: the internet works. Okay. Now obviously you don't  need to have gone to this website to know how the    
02:30:01: internet works more uh fundamentally speaking.  I think every kid just inherently gets it when    
02:30:05: they are given their first iPad with Coco Melon  on it. U no jokes aside uh the worldwide web is    
02:30:11: is a website that's entirely built in HTML. And  you can see because the file ending up here is    
02:30:14: HTML. If I open this up you'll see the actual code  of the website down here. And it's very simple.    
02:30:19: There's a body, there's a header, there's an H1,  which stands for worldwide web, an AT, which is a    
02:30:25: bunch of links, and then P tags and and stuff like  that. Now, worth noting that this is a website    
02:30:30: with no CSS, which is sort of the next level up.  Now, CSS is how you change the style of the page.    
02:30:36: It's how you make things bigger or smaller or  or sexier or whatever. So, if I go style here,    
02:30:43: I can actually change the font size to like 300  pixels and I can make that bigger. This HTML is    
02:30:51: just that core fundamental um kind of structure,  the scaffold of the page. This style is now CSS    
02:30:57: and it's where I'm like applying some additional  information to change the size. I could change    
02:31:01: the color and I could do so on and so forth. I  could I could change things quite a bit. Now,    
02:31:04: there is that one final piece which is JavaScript.  And JavaScript nowadays is done mostly through the    
02:31:10: console. Inside of the console, you can actually  run um JS. So what I could do is I could go    
02:31:15: document query selector and then I could look  for all all H1's elements and then what I could    
02:31:21: do actually remove this from the page um just by  clicking or writing document.query selector H1-E    
02:31:28: and this is an example of that interactivity that  I was talking about. Basically with JavaScript    
02:31:32: what you can do is you can I'm realizing that  my head's in the way here so you can't see that    
02:31:36: most recent function. Um basically what JavaScript  allows you to do is allows you to select specific    
02:31:41: elements on the page and do whatever you want with  them. You can make them bigger, you can make them    
02:31:44: smaller, you can apply styles, you can create new  HTML. I mean, there's like a bajillion different    
02:31:48: things you can do. Okay, so those are the three  programming languages. And hopefully we're all    
02:31:51: on the same uh page about how these two or three  interact with each other. The thing is, obviously,    
02:31:57: if you design a website or a web app using HTML,  CSS, and JavaScript, there's like a million    
02:32:03: different ways you could do so, right? You could  write whatever website you want, apply whatever    
02:32:06: styling you want, and then obviously apply  whatever interactivity you want, and that's great.    
02:32:10: But the internet thrives off standardization,  which is where things are done in a repeatable    
02:32:15: and sort of consistent way. Because of this,  the more standardized the internet tends to be,    
02:32:21: the better solutions that people can build on top  of pre-existing solutions. And that's really the    
02:32:25: whole idea of programming languages in the first  place. So in addition to this idea of you know    
02:32:30: languages as um standardization you also now have  this concept of frameworks as standardization. And    
02:32:41: so frameworks are a level of abstraction that  are built on top of languages. And what we do    
02:32:46: is we actually just take these three sort of Lego  blocks and we just construct them in a specific    
02:32:51: way essentially. Okay. And right now there are a  bunch of different frameworks out there. The most    
02:32:57: popular ones I would say are next.js which is the  framework that we just used to define and build    
02:33:05: our current app. And you can see that that include  a lot of that included a lot of opinionated    
02:33:10: um framework based stuff for like the folder  structure and components and hooks. These are all    
02:33:15: things that are basically a handme-down directly  from our framework. You also have um vit right    
02:33:21: now is super popular and you'll see a lot of apps  created with vit and then on the other side you    
02:33:26: also have view or really like nux.js and there are  varying levels of abstraction here like nux.js is    
02:33:32: actually an it's like a second framework built on  top of another framework called uh react which is    
02:33:37: kind of funny. Um nux.js is built on top of view.  Uh you know there are a lot of like dependencies    
02:33:43: and stuff and if you guys remember earlier I said  we stand on the shoulders of giants. really do uh    
02:33:47: because everything nowadays is built off of  something somebody else built which was built    
02:33:50: off something somebody else built all the way  down to where we were programming computers    
02:33:53: with little ones and zeros on pieces of tape. And  so in addition to you know our chosen tool and    
02:33:58: this is the tool I'm going to be using for the  most part throughout this course. NextJS being    
02:34:03: essentially the way that we coral these three  programming languages together. Nex.js JS is also    
02:34:09: an opinionated framework that um you know helps  us organize things like hosting, helps us organize    
02:34:16: things like how to do you know database calls and  whatnot in a standardized way. You guys remember    
02:34:22: earlier we talked about middleware authentication  middleware uh has a standardized interface for    
02:34:26: authentication middleware is a standardized way  to put together routes which are just the names    
02:34:31: of like um website endings. So excalagger.com/ I  don't know settings that's a settings route for    
02:34:36: instance and so on and so forth and what's really  cool is because a lot of people have used these    
02:34:41: frameworks before you know like NexJS isn't Neo  was developed at least half a decade ago if not    
02:34:45: more I built tons of projects with it before we  had the luxury of agents to do that for us because    
02:34:50: of all this we had a lot of pre-existing projects  out there on the internet that were built with    
02:34:53: this and these were all used in the training sets  of these large language models like you know opus    
02:34:58: gemini and so on and so forth which means make  a long story short If you use a framework, you    
02:35:03: usually get significantly higher quality results.  Now, frameworks obviously have some baggage as    
02:35:07: well. The more opinionated things you put into uh  you know a design system or whatnot, obviously the    
02:35:14: more lag that you can have, the bigger the files  can be and and so on and so forth. But for the    
02:35:19: most part, these are a good balance of like  speed, stability, reliability, and then also    
02:35:23: security. You know, because these frameworks have  existed for a while, people have put together some    
02:35:27: pretty simple and easy ways to economize um our  security and our ability to build apps. Okay. So,    
02:35:32: am I saying that you have to like go and  learn every single thing in HTML? No. CSS? No.    
02:35:36: JavaScript? No. Um, do you have to read through  all the NexJS docs? No. Although they are they    
02:35:40: are pretty cool if you wanted to. None of these  things will necessarily make you like a better    
02:35:44: vibe coder. But I think it's important to at least  be able to like look at the Lego blocks and see    
02:35:48: how they fit together because if you don't, then  you're a lot more liable to produce what I think    
02:35:52: a lot of people nowadays are terming as sloop  out there on the internet, which are like simple    
02:35:54: vibecoded apps that aren't really well thought out  and then interact with the rest of the internet in    
02:35:59: pretty stupid ways. The last thing I want to talk  about is version control. And to make a long story    
02:36:05: short, version control just answers the question,  how do I store successive updates of files on a    
02:36:13: server as efficiently as humanly possible? Let me  give you a brief little example. I'm sure you know    
02:36:18: back in high school or college or whatever, those  of us that have gone there in the last few years,    
02:36:23: you've run into situations where, you know,  you're tasked with writing an essay. And so,    
02:36:28: you know, you write your essay probably really  late in the middle of the night with a bunch    
02:36:31: of Cheetos beside you. At least that's how I  used to do it. And then, um, you save it as,    
02:36:35: I don't know, essay docx, let's say. You know,  it's like a it's like a Google doc or something    
02:36:39: like that file. And you do it locally in your  computer, maybe Microsoft Word, okay? And then,    
02:36:44: um, the next day, you know, you wake up and then  you give it to your friend, and your friend gives    
02:36:49: you some feedback or something like that. Okay?  So what they do is they they download the file    
02:36:53: and then they give it back to you and then it's  called essay with feedback.docex. So what you do    
02:37:00: is you take that file but not wanting to lose the  previous two files what you do is when you make    
02:37:05: your updates to it okay you don't save it as essay  with feedback you call it essay 2.d dox and then    
02:37:12: the cycle just repeats itself three or four times  then you have essay 3.d dox you have essay 4.x doc    
02:37:20: x and so on and so on and so forth until you have  essay final superfal important docx. Okay. And    
02:37:29: before you know it, you know, your whole downloads  folder is a mess. I'm sure we've all probably had    
02:37:33: situations like this before. Um I know, god  forbid, I I used to have situations like this    
02:37:37: all the time. Now, that's for writing things like  essays. I want you to imagine instead of essays,    
02:37:43: what you're doing is you're working on an app like  we're doing. You'll have app one dot whatever,    
02:37:48: app two dot whatever, app three super important  final whatever. Obviously, these things can get    
02:37:53: out of control really quickly. What compounds  the issue is this idea of needing to share files    
02:37:57: because this super janky ass method, this could  work if it's just you and you understand how you    
02:38:01: name your files and stuff. You could build like a  naming convention, right? But what if you want to    
02:38:04: share this with like 20 other people and 20 people  all simultaneously need to be able to work on the    
02:38:08: file that is the most updated without causing  conflicts and stuff like that and so on and so    
02:38:12: forth. That's really the whole idea behind what  initiated version control. And so what we do is    
02:38:17: we basically have again standing on the shoulders  of giants um built systems out there that store    
02:38:24: not only the file itself but store the changes  between files and then just let you access them    
02:38:30: by you know calling a little URL or something and  then pulling the file as well as a list of all the    
02:38:35: changes um that have historically occurred. So  that at any point in time, you know, you could    
02:38:40: download, let's say, this original file, but  then you could jump over here if you wanted to,    
02:38:43: jump over here if you wanted to, jump over here  if you wanted to, jump over here if you wanted to,    
02:38:46: and so on and so forth, all without just needing  to like pollute your, you know, file system and    
02:38:50: stuff like that. What's more, at any point you  could also branch out and make additional changes    
02:38:54: here, however much you want, called, I don't know,  new essay. And then you could share that new essay    
02:39:02: uh with other people. Okay? Or what you could do  is you could make the changes here and then you    
02:39:08: could actually take these changes and then merge  them with another pre-existing file to get some,    
02:39:13: you know, new better essay hypothetically. Um, you  could do that with apps, you could do that with    
02:39:17: essays, you could do that with everything.  People use version control to literally do    
02:39:20: everything nowadays, research papers and so on  and so forth included. So the major place where    
02:39:26: most version control happens now is on GitHub. And  what we do is we've taken this concept of like a    
02:39:32: folder or a workspace and we've standardized it  into one called a repository. And so this idea    
02:39:38: of a GitHub repository is very popular. You go  into github.com. This is what the website looks    
02:39:43: like. Okay. And you can see on the left hand side  I'm signed in here. I have a bunch of different    
02:39:49: um repositories. I didn't even realize, but  I have a bunch of people here that are like    
02:39:51: starring my repos and stuff. That's hilarious.  Um I have a bunch of different repositories    
02:39:55: here like worklog make money with make gyro  app.1c.copy.com copy.com, proposal generator,    
02:40:00: and so on and so forth. And these are all  basically different projects that I've built. Now,    
02:40:03: what's cool is if I click on any one of these,  okay, you can actually see every change that I    
02:40:08: have made to this over the course of god knows  how long. This is basically over the course of I    
02:40:13: don't know 346 different changes. If I click this  button, the wildest thing, so I can actually go    
02:40:18: through and I can see literally every change I've  ever made to this thing. And at any point in time,    
02:40:23: okay, I can actually open up the details and then  the code itself to adjust what's going on. I could    
02:40:30: uh restart my, you know, project from here. I I  mean, I could do anything. I could share this with    
02:40:35: other people really easily. Um, and so on and so  forth. So, I say this not because I want this to    
02:40:40: be a comprehensive guide to GitHub. Obviously,  it isn't. I just like gave you guys a very high    
02:40:43: level overview. Um, but in a nutshell, all this  is is just a way to store and and and save files.    
02:40:48: And so whereas with our last couple of projects  with our portfolio site and then the um app that    
02:40:53: we just built, I wasn't using GitHub for any of  it, from now on, what we're going to do is we're    
02:40:57: actually going to take our big file structure  that we're developing locally and we're going    
02:41:01: to constantly push it to GitHub so that we both  have like a saved version over there if anything    
02:41:05: locally occurs, but also we have the ability to  um share it with others. And then services that    
02:41:10: do deployment nowadays like Netlife, Versel, and  and other platforms out there, they can often just    
02:41:15: pull directly from the GitHub. So I don't have to  like drag my folder in. I could just say, "Hey,    
02:41:19: here's my GitHub repo." And then it'll just do all  the math and stuff for me. And then I don't even    
02:41:23: have to like rebuild it on Netlefi. What I could  do is I could just push it to this repo, make a    
02:41:27: couple of changes, and then Netifi will have  like a little hook that automatically rebuilds    
02:41:30: the site every time a change occurs. And this is  how you get like different pipelines set up with    
02:41:34: like production, staging, local, and so on and  so forth. You can also create different branches    
02:41:38: branches. I guess I have one here called chest day  workout. That's pretty funny. Must have crushed    
02:41:42: that chest day. Um, and then just have agents  manage like everything to do with uh with whatever    
02:41:47: project you have. So, for instance, this is like a  little work log that I set up that basically just    
02:41:51: like a list of things that I've done. I use it to  track my own my own work. And uh I developed this    
02:41:55: in just a few minutes with uh with claude code  I think like two months ago essentially. The    
02:42:01: last thing I'm going to mention here is everybody  gets a GitHub profile. And so there are a lot of    
02:42:04: people out there that are have very popular GitHub  profiles. This is usually where most open source    
02:42:08: lives. So, you know, if you develop a really cool  new idea or new framework or something, you make a    
02:42:12: GitHub repository and then you share it with other  people and then other people can also make changes    
02:42:16: and then improve it over time. Um, that's what  a bunch of really popular repos tend to do. If    
02:42:20: you guys have checked out like the open claw one  and and stuff like that, that's where they were    
02:42:24: getting um most of this this from. And then with  agents, what you could do is you could actually    
02:42:27: just have parallel instances of like 10,000  operating in the background, constantly scanning    
02:42:32: the workspace and then making micro adjustments  and edits in a very interpretable and accountable    
02:42:36: way. So the future of software development is  basically that decentralized GitHub repo pushing    
02:42:40: and pulling and stuff. Okay, cool. I think we've  now done enough of like the traditional software    
02:42:44: engineering concepts for you guys to know a lot  more about how to build these things efficiently.    
02:42:48: Um, what I want to do now is just talk really  briefly about a couple of the different ways you    
02:42:51: could use agents to streamline your work. I know  we touched on this briefly with the repo stuff a    
02:42:55: second ago, but I just want to zoom out a bit and  then just look at anti-gravity and look at some of    
02:42:59: the the potential and the functionality there in.  Okay, so if I just go back to anti-gravity here,    
02:43:03: you know, I still have that old site set up. Um,  I should be able to clear this just by going to    
02:43:07: new. Um, one of the simplest and easiest ways to  multiply your ability to work on a specific repo,    
02:43:14: which is just what I'm going to call our workspace  or file folders from now on, is basically just    
02:43:20: running multiple different separate functions  simultaneously. And so, you know, I could say,    
02:43:26: hey, do XYZ, and then I could just wait until this  whole thing is finished. And then I could give it    
02:43:31: some more instructions. Hey, thanks. Let's now do  ABC. Or what I could do is I could make use of the    
02:43:38: ability to start new conversations. And I could  actually run multiple of these um simultaneously.    
02:43:47: So I think we're all familiar with just using the  little agent tab on the right hand side. But in    
02:43:52: order to parallelize your work and then work a  lot faster, what we can do is we can zoom out of    
02:43:56: a specific workspace and then actually just look  at like 3 4 5 10 100 agents working simultaneously    
02:44:01: for us and then just orchestrate their actions.  This can sound pretty bonkers if it's the first    
02:44:05: time you've done something like this, but this  sort of functionality is actually built into    
02:44:08: anti-gravity and uh it's also built into things  like cloud code and and stuff like that as well.    
02:44:13: The way you do so is with this agent manager in  the top right hand corner. So if I click the agent    
02:44:17: manager, what we've done now is we've zoomed out  of a particular workspace. We actually have all    
02:44:21: of our workspaces here listed on the lefth hand  side. And you can actually see every conversation    
02:44:26: you've ever had inside of each workspace as well,  which is really handy. So, this one's improving    
02:44:30: dashboard UX. This one's listing directories and  stuff like that. Here's a search I just said a    
02:44:34: moment ago, or I'm pretty sure I just said like  do ABC or something like that cuz I wanted to like    
02:44:38: have a bunch of these that I could quickly jump  through. You can see in this case just ask me,    
02:44:41: hey, what the heck is ABC? What are you crazy? And  so on and so forth. This is some other thing that    
02:44:46: I've developed here. This is some other thing  that I've developed. And so on and so forth.    
02:44:49: So, I mean, like, you know, this is kind  of cool, right? You basically can just go    
02:44:51: top to bottom and then see at a bird's eye view a  bunch of different conversations that you've had    
02:44:55: with different agents. And you can do this across  workspaces. You can start new conversations across    
02:44:58: workspaces. You can jump into a specific workspace  using the editor, right? Um, and so on. The really    
02:45:04: cool thing though is if you go to this inbox in  the top lefthand corner, what you can see is you    
02:45:09: basically get a list of all of the messages that  AI is sending you. And the reason why this is so    
02:45:14: valuable and so cool is because if you make use of  the pending feature, which is basically where you    
02:45:21: don't let AI do something unless you've cleared  it, what you can do is you could use this little    
02:45:26: pending filter and then just have a giant list of  things that like 20 different agents are working    
02:45:31: on simultaneously and then they're just like  serving you um you know the results and asking    
02:45:35: you, hey, do you want me to do X, Y, and Z? Okay,  so let me show you a really quick and and simple    
02:45:39: example. So earlier I had this website builder  repo, right? If I just open the editor here,    
02:45:44: I had this big Gemini.MD where I was basically  showing you guys how to create a website and    
02:45:49: then I pumped through like two or three of them  simultaneously. And I hid this from you at the    
02:45:53: time because I didn't want you to obviously get  super overwhelmed. But if you open the agent    
02:45:57: manager, okay, you can see that you can now start  new conversations in what's called a playground,    
02:46:02: which is an independent workspace, perfect for  quick prototypes or following curiosity. Then you    
02:46:06: actually just paste in this multiple times. So you  could start a conversation by going in, paste this    
02:46:13: in, start another conversation by going in, paste  this in, and start another conversation by going    
02:46:18: in, paste it in. And now in the playground side of  things, okay, you now have multiple conversations    
02:46:23: that are occurring where it'll basically just ask  you a bunch of information. I'm just going to say,    
02:46:28: um, choose all of this yourself, high-end SAS,  for a demo I'm making. You can just paste this in.    
02:46:38: You could paste this in. You could paste this in.  And then you could paste this in. And what I have    
02:46:44: now, okay, is I have multiple agents that are all  operating simultaneously and independently for me.    
02:46:51: This first one here is called cinematic landing  page build. The second one here is called building    
02:46:54: cinematic landing pages. And then you guys can't  see these other two, but it's cinematic landing    
02:46:57: and cinematic landing. And basically what they're  going to do is presumably they're going to create    
02:47:01: different folders for each of these and then build  all of these websites simultaneously in parallel.    
02:47:07: Right now what I have think about it is I've  made one command up here and it's split rather    
02:47:13: I've made four different commands up here but  basically what I've done is I've split and now    
02:47:16: we have these agents all running simultaneously  and inside of this playground I have the ability    
02:47:21: to like get a highle overview what of what um  they're all doing just by mousing through each    
02:47:26: okay and you know sometimes you're either going to  run into token limits or there's going to be some    
02:47:31: issue so agent terminated due to error here when  this sort of thing occurs you can reply and you    
02:47:36: can also just use this agent conversation for it  to show you more or less like what it's currently    
02:47:40: working on. So, you know, if I go to inbox here a  moment ago, it basically said, "Hey, like what do    
02:47:44: you want me to do?" That that that was a message  that the agent sent to me asking me for approval,    
02:47:48: right? I can actually just see all these things  at a very high level overview just by constantly    
02:47:52: being on this page. And then essentially all I'm  doing is instead of like me being responsible for    
02:47:57: shephering one agent simultaneously, sorry, one  agent through a process, I can shepherd multiple    
02:48:01: simultaneously. And this is the difference between  somebody that's like building one project and then    
02:48:05: somebody that's orchestrating multiple projects.  You do run into some issues with like context    
02:48:09: switching, which is a productivity term that  basically applies to when you're trying to do    
02:48:12: multiple things simultaneously or a little bit  less efficient at um every one individual one,    
02:48:16: but it's sort of like monitoring like three or  four different CCTV uh uh pieces of footage if    
02:48:22: you're like a security guard or something in a  mall. You're basically just zooming out. You're    
02:48:25: watching three or four of these things and  you're stepping in anytime that a particular    
02:48:29: person needs you. Alternatively, it could be like  you're a manager at some big office with a bunch    
02:48:34: of cubicles that you're just walking up and down  the halls. When somebody needs you, they're like,    
02:48:37: "Hey, you know, Nick, can you help me with X, Y,  and Z?" And so, in this way, you're capable of    
02:48:40: orchestrating significantly more total output or  work than you would be able to do yourself. So,    
02:48:45: it's really worth using hotkeys um if you  wanted to start building things in this way. And    
02:48:50: uh generally speaking, believe it or not, instead  of just building one app, I will usually build two    
02:48:54: or three apps simultaneously now with something  like the agent manager and an inbox. and then    
02:48:58: I'll just like have them all run in parallel.  Um, the reason why is because then that way I    
02:49:02: could build multiple versions and then I can  just pick the version I like the best. Once I    
02:49:05: pick the version I like the best, I drop the other  ones and then I just proceed with that one. Um,    
02:49:08: but yeah, hot keys are pretty important. So you  can find those just by mousing over each of these    
02:49:12: buttons. So inbox is command I for instance,  uh, if you scroll down to playground here,    
02:49:17: you can create a new instance just by holding  controlN. And so a lot of the time I'm just    
02:49:21: jumping between new conversations and then my  inbox over and over and over and over again.    
02:49:25: Um, you can also jump back to that editor like I  talked about earlier just by going command E. This    
02:49:29: will jump you into the particular folder where  the conversation and kind of work is happening.    
02:49:32: So this one's called glowing cosmos for instance.  At any point in time if you're operating inside    
02:49:36: of this playground, you also have the ability  to um move this into a specific folder. And so    
02:49:40: this is occurring right now in like a temporary  folder that uh Gemini and anti-gravity just puts    
02:49:45: together anytime you do this sort of thing.  But you can also just click this button and    
02:49:48: then you can select a destination folder for all  the files in your project. So I could, you know,    
02:49:53: use the playground to sketch out three or four  different ones and then when I find one that I    
02:49:58: really like, I could then use the um create a new  folder thing to like actually go in add a folder    
02:50:02: and then just work in like a dedicated workspace.  They also have a feature called follow along with    
02:50:06: agent in the top rightand corner. So if you  follow along with agent um basically it'll    
02:50:10: pull you back in to what the agent is doing at  every step and then allow you to see the various    
02:50:14: um you know pieces of work that that agent it's  worth keeping this page pretty clean. So, I'm just    
02:50:19: going to proceed with whatever the heck it asked  me for. And then over here, now I basically have    
02:50:23: these two main threads that I'm running. You can  see the same thing's occurring back here and then    
02:50:29: also back here. And although kind of per unit,  it'll still take the same amount of time to get a    
02:50:34: website out because, you know, this is operating  at the speed of um whatever Gemini 3.1 Pro is,    
02:50:39: if you think about it, I'm technically doing four  times the amount of work um simultaneously across    
02:50:44: all four. I don't usually recommend having  more than two or three of these operating. I    
02:50:49: just wanted to show you guys how cool it could  be if you have four. I actually have five now    
02:50:52: cuz I'm proceeding with some um agency operation  thing I did a while back. Uh just because I find    
02:50:57: like your attention gets pulled away a little  too much. But um yeah, you can see here in the    
02:51:00: top rightand corner because I'm following this  anytime it'll make a substantial major update. I    
02:51:03: can actually see the code that it's working with  and so on and so forth. I usually don't actually    
02:51:07: click that though. I just go to my inbox and then  I seem you know do you need anything from me? if    
02:51:11: there's any specific feature or whatever that  they want, then I can I can jump right in. So,    
02:51:15: let me run this for a couple more minutes, get  a bunch of websites, and I'll just show you    
02:51:17: what they all look like. Okay. And our landing  pages are now starting to um be finished. So,    
02:51:22: we could actually access the Vit server. This  one's using a different framework called Vit that    
02:51:26: I covered earlier just by pasting this in. You  can see we now have one of the websites. Now, I    
02:51:31: should note that this looks pretty similar to the  1se secondond copy website I had set up because    
02:51:35: uh I think I just asked it to build something that  was like very very similar visually speaking. So,    
02:51:38: we had that little heartbeat. we have this little  thing, but you know, I'm like trying to build    
02:51:41: it with a particular template, right? So, I'm  just going to instantiate a bunch of versions    
02:51:44: of this template, and if I like them, then I'll  go with that. This second one here is done. Um,    
02:51:48: because I didn't specifically say, "Hey, I want  you to run the server and then open it." You know,    
02:51:51: this one's asking me to do this terminal command,  npm rundev. Um, so I'm just going to have it do    
02:51:56: it by saying run it and then it'll open it  for me and then I can take a peek. Here it    
02:51:59: is. Let's copy this over. Paste this in. Cool.  And now we have another one called Aether Core,    
02:52:04: which is very clean. I really like this one. Damn,  that's really, really sexy. You know, there are    
02:52:09: some issues here with some of the fonts and stuff,  but hopefully you guys see like I was capable of    
02:52:12: generating four of these simultaneously. This one  here is still under development. As you can see,    
02:52:17: there's a hero section and it's scrolled down, but  it is running live on a server and it does have    
02:52:20: that cool little bar up top. And this one here had  probably my perfect instantiation or my favorite    
02:52:25: of like this slow scrolling card like that to me  looks really sweet. Um, it's just rerunning it    
02:52:29: because it's making some additional changes, but  yeah, pretty cool, huh? So, you can actually build    
02:52:33: multiple apps simultaneously. And in this case,  you know, I gave it some pretty static resources.    
02:52:37: And I was like, "Hey, I want you to use like  this kind of noise layer in the background and    
02:52:39: stuff like that." You could also just have all  of them be different. And the way you do that    
02:52:42: is you just provide like a prompt that has some  inherent randomization. Basically says, "Hey,    
02:52:46: I want you to randomly select like, I don't know,  a background from this online background service."    
02:52:51: And then it'll use different backgrounds. Hey, I  want you to automatically select a different type    
02:52:54: of style using this thing. You know, instead of  high-end SAS, I just want you to come up with a    
02:52:58: different one every single time. And then it'll  come up with like a 100. So yeah, in this way    
02:53:01: I've I've uh successfully built something like  15 websites simultaneously at the same time. I    
02:53:06: found like the top two or three that I like. I've  proceeded with those. I filtered out the ones that    
02:53:10: I didn't and then I've had like a really really  high quality product. And I've done all that stuff    
02:53:13: in like 10 maybe 15 minutes or so. Um obviously be  careful with token usage here because it's always    
02:53:20: going to be a trade-off between the time it takes  to build something and the total cost on your end.    
02:53:24: This is just a pretty straightforward money for  time trade, but running multiple agents in this    
02:53:28: way um simultaneously can be pretty cool.  Okay, now that you guys know more or less    
02:53:31: everything you need to know about both modern  software development, um, hosting, databases,    
02:53:35: frameworks, and all that stuff, plus how to use  agents to pour fuel onto the fire, let's build    
02:53:40: product number three, which is a lead generation  SAS app that scrapes, enriches, and even queue up    
02:53:44: um, the sending of fully automated emails. This  is very similar to a structure that I use in    
02:53:48: production myself in my own business, Leftclick.  We work with multi-billion dollar portfolio    
02:53:52: companies and essentially connect to the outbound  systems on a team to help them send emails,    
02:53:56: scrape uh contact details, and then personalize  outreach at scale without needing like a million    
02:54:01: bajillion hires in order to do all that for us.  So this time, instead of just diving right into    
02:54:06: the app development via prompt, I wanted to take a  few moments to sketch out what an actual app might    
02:54:11: look like. And there are variety of different  names for this sort of thing. Um, in my case,    
02:54:15: I'm just going to call it planning. You could  call it some form of like UX or site design    
02:54:19: or navigation design or whatnot. In short, um I  know for sure this app is going to need a landing    
02:54:25: page. So here I just said landing page sexy on  it. We're going to want some navbar, some main    
02:54:31: value proposition, a social proof section, some  how it works section, some case studies, a CTA,    
02:54:37: and then a footer. This is pretty standard, right?  It's basically the exact same thing that we did    
02:54:41: with Content Orb. After that, we're going to want  some sort of login and/or signup page. And so this    
02:54:46: is the O form in Superbase where you enter your  email, enter your password, and then it signs you    
02:54:50: up. Now, what I imagine will probably happen after  is once you're signed in, um, we'll need some form    
02:54:57: of configuration page cuz I want this app to be  able to be usable by people like you, people that,    
02:55:02: um, you know, I don't want to have to necessarily  build for. Instead, I want there to be a space for    
02:55:05: your instantly API key, your anthropic API key,  your OpenAI API key. Uh, I want you to be able to    
02:55:11: configure the prompts that are being used by the  AIS to do personalization as well as have defaults    
02:55:15: and stuff like that. And basically, I just want  that to be like your onboarding. It's like, hey,    
02:55:18: do you want to get started with the scraping?  Just enter your API keys here. And there are a    
02:55:22: couple of other API keys that I'm going to need,  actually. But, um, in addition to that, I also    
02:55:26: want like brief little one-click guides to show  people how to do all of those things. And then    
02:55:30: finally, I want the actual scraping page itself,  which is just going to be a form where you put in    
02:55:34: some basic parameters. And the way this is going  to work, for those of you guys that don't know,    
02:55:37: there's a scraping service out there called  Appify. And we're basically just going to wrap    
02:55:39: around Appify. If we can't find enough leads, then  we're going to scrape Google Maps. And then we're    
02:55:45: basically going to combine both of these into some  sort of like enrichment personalization flow. Um,    
02:55:50: and assuming that, you know, we've enriched and  personalized, which, you know, may not necessarily    
02:55:54: mean something to you guys if you guys aren't in  the marketing space, but I'll run you guys through    
02:55:57: it all um throughout this demo, then you'll just  get all the leads that you just scraped in a    
02:56:01: simple CSV with some additional column that has AI  based personalization. So, we're going to need the    
02:56:07: first name and email at minimum. And then I think  the last thing to talk about is that orders page    
02:56:10: or just going to be like a like a history page  where you could see all the orders that you've uh    
02:56:14: scraped and sent before. And then maybe I'll also  do plus specific order pages for each that have    
02:56:20: like I don't know a bunch of descriptions on them.  Okay. So, you know, I think uh probably a real UX    
02:56:25: designer would crucify me uh in terms of the ways  that I've laid all this stuff out, but you know,    
02:56:29: seems to work pretty reasonable for me. Um, what  I do next is I basically just take a screenshot    
02:56:33: of this and then I always have this on hand  cuz you know I want to like know what my app's    
02:56:38: going to look like. Then I go into anti-gravity  and then what I do is I um say something like,    
02:56:41: "Hey, I'm making an app that helps people scrape  leads. Turn this into a brief description of an    
02:56:45: app that includes all the important components  and I actually just screenshot and I send it to    
02:56:48: them." This is back when I had it like vertical.  I've since made it horizontal. Then scrolling down    
02:56:53: a little bit, you can see we've now changed  it into the description. Okay. And then over    
02:56:56: here we have the updated description with just a  bunch of, you know, plain text language here. So,    
02:57:01: we're probably going to need more. I mean, like,  it's not that big of a deal. Then I made a couple    
02:57:05: of changes and I said, "Hey, here's some scrapers  that I want you to wrap around." Okay. And now my    
02:57:09: claw code instance has generated this prompt.  So, that's good for now. What I want to do next    
02:57:13: is open a new folder cuz I've copied this and I  want to call this lead scraping SAS. I'm going    
02:57:18: to create and I'm going to open. Now, in our  anti-gravity instance, we have a plain folder    
02:57:22: here, lead scraping SAS. And so what I want to do  next is two things. First, I'm going to need to    
02:57:29: feed in that prompt. And second, I want to feed  in um a description, sorry, an example that we    
02:57:34: could use to basically inspire Gemini. Now, I went  on dribble and I found something that looks like    
02:57:39: this. This looks pretty reasonable to me. Um keep  in mind like the design and stuff like that is    
02:57:43: pretty sleek, but obviously they have a lot more  components here. Data transfer. I mean, I don't    
02:57:47: really know why I would ever need a data transfer  component, but you know, there's like a bunch of    
02:57:50: buttons here and stuff. And I think we could make  this work. Um, you know, our graph may not look as    
02:57:55: nice, although I think we could actually make it  look as nice if we really wanted to. But for now,    
02:57:58: I'm just going to copy this image. I'm going to  go back over here. I'm gonna start by pasting that    
02:58:02: in. Okay. So, we're going to start just by pasting  in um this image. It looks like we're copying    
02:58:08: this, but it's not actually making it all the  way to our dashboard. It's kind of annoying. So,    
02:58:11: I think I'm going to have to take a screenshot  of the actual app itself. I think sometimes    
02:58:14: Dribble does like anti-creenshot protection or  something. Keep in mind that we're not stealing    
02:58:19: this or anything. We're just going to use this as  like inspiration. That's all. go back here, paste    
02:58:22: that in. Then I'm going to say um I'm going to  head over to Google, say cold email lead scraping,    
02:58:28: and I'm just going to find some links here.  Basically, I just want like a brief description    
02:58:32: of what cold email lead scraping is. So, let me  see if maybe instantly has some information on    
02:58:35: their site. Um, this is like a full endto-end cold  email sending platform. Uh, probably not what I    
02:58:44: want. I just want like some lead scraping.  This looks pretty good. I like this. So,    
02:58:49: I'm just going to copy this. I'm going to head  back here. I'm going to paste this in. I'll say    
02:58:53: this is an example of the sort of thing that we're  about to build. I'm going to paste this in just so    
02:59:00: it has context and so it can write my landing page  for me. And then next up, obviously, we need that    
02:59:05: um prompt that we just copied over. I'd like  to build an application. I want it designed    
02:59:09: according to the screenshot that I sent over. The  specifications and the stack is um in the middle.    
02:59:15: And then I've also given you a description of  another website that does something similar that    
02:59:19: I'd like you to emulate for the copywriting  and content and so on and so forth. Okay,    
02:59:25: we're going to stick that in. And uh this is most  likely going to end up using like a next.js stack,    
02:59:30: although I did not this time necessarily want  to be opinionated cuz I wanted to see what the    
02:59:34: app was going to do. Uh when it ends up creating  files, it'll do so over here. Keep in mind that    
02:59:38: we are in planning mode as per usual. So that's  what's going on down here. And it looks like we're    
02:59:42: using Oh, actually we're using Vit, which is good  because that'll give us a the ability to maybe    
02:59:47: use a different framework here. To be honest, I  don't really care about the specific framework,    
02:59:50: right? We talked about how there were multiple  uh in the previous section. So, whatever works    
02:59:54: is going to work. Um, you know, as long as it's  fast and performant. Okay. So, at this point, I'm    
02:59:59: just going to sit back and let it do its thing.  Awesome. So, I just got a notification saying that    
03:00:02: it's done for Leadzo, which is the name that uh I  decided I would give our cute little app. And now,    
03:00:08: what I'm going to do is I'm going to say run  it. The reason why I'm going to do that is    
03:00:11: because in order to access this application,  we're obviously going to need like some server    
03:00:15: running at the back end. Our browser is going to  end up being the client and then that's how we're    
03:00:19: going to communicate with that. So, our server  is going to be on our computer for now since it's    
03:00:22: all local. Let's see how it goes. So, we got the  Vit server set up. This is the landing page. Uh,    
03:00:27: super clean. I like it. Okay, so we have like  some weird spacing here. That's fine. This is    
03:00:33: really nice. I like this AI personalization  prompt. Very clean. Very clean. Nice. 100    
03:00:38: free credits. Okay. So, what happens if I click  get started? I go over here, which is nice. Um,    
03:00:44: I'm just going to ask it. Oh, it looks like it's  actually recording a browser session of me testing    
03:00:49: this. This is wild. It's Nick Nikki Wiki. Then,  Nikki Nikki Nikki. Let's sign up. Okay, we're now    
03:00:57: inside. We have some workspace settings on the  lefth hand side here. API integrations. On the    
03:01:02: right, we have some prompt engineering. So, define  the rules leader should follow and generating the    
03:01:05: personalization column for each lead. Cool. Does  this actually fill in? Okay, we just have some    
03:01:10: placeholders for now. What happens if um Cool. So,  it went it actually went it found the uh specific    
03:01:15: API keys and stuff. That's fine. Scrape leads. So,  we need a job name, LinkedIn Sales Navigator URL,    
03:01:21: max leads, then default icebreaker. I think what  we want is basically are going to want to be able    
03:01:27: to just say uh I don't know like HVAC companies in  the United States and then we want it to actually    
03:01:35: go and find that for us. We're not going to need a  LinkedIn sales navigator URL because the appy the    
03:01:39: specific service that we're using doesn't actually  um use that. So, it's going to be okay. Then here    
03:01:43: we have some fake order history which looks  really clean. We can, you know, open it up in    
03:01:46: a new window or whatever. Awesome. Awesome. Cool.  So, let me just check the bottom. You guys can't    
03:01:51: see this, but there's a little button that says  log out. So, click this log out button. Nothing's    
03:01:54: going to happen since obviously we don't have  the off set up. Yeah. I mean, like in a nutshell,    
03:01:57: this is more or less what I what I wanted. Um,  anything else that we need? So, new scrape job    
03:02:01: orders configuration. I think that's basically it.  Now, now what we have to do is we basically have    
03:02:06: to test this. Uh, cool. So, what I'm going to do  next is I'm just going to run through a couple of    
03:02:11: these services that we're using just so we're  on the same page. Otherwise, I think it'll be    
03:02:14: kind of intimidating for you guys to see what I'm  doing. But in reality, most apps nowadays are just    
03:02:19: like wrappers, as in they just wrap functionality  around some other app. Of course, you could build    
03:02:23: your functionality yourself if you really wanted  to, and I can help you with that. But in my case,    
03:02:27: you know, for the purpose of this demonstration,  I'm just going to do what I normally do,    
03:02:30: which is I use a three a thirdparty service called  this leadsfinder on a uh which basically allows    
03:02:34: you to put in some parameters and then get some  leads. So, it generates targeted B2B contact list    
03:02:38: using advanced filters. Now, this isn't the best  lead scraping service out there. I should note    
03:02:42: that like it's actually quite poor in terms of  quality now because uh the leads are cached and    
03:02:46: they haven't been around for quite a while. So,  I use this as an example in Make Your School,    
03:02:51: my community all the time. But, let's say I'm  scraping some dental clinics in Canada. I want    
03:02:54: to scrape a thousand. What I do is I basically  just put in a bunch of job titles here. Owner,    
03:02:57: practice owner, principal dentist, lead dentist,  so on and so forth, and then locations to include,    
03:03:03: which in my case is Canada, locations to exclude,  what sorts of emails I want to get. So, validated,    
03:03:08: not validated, unknown. So, I I actually just want  validated emails, what sort of company website if    
03:03:13: I have them. Um, we can use to narrow down the  search. The size of the uh resulting company,    
03:03:19: so 1 to 10, 11 to 20, 21 to 50. the industries  that I'm looking in. So, health, wellness,    
03:03:24: and fitness, hospital, and healthcare. And then  which ones not to look for some keywords, dental,    
03:03:28: dentist, and then I'm also excluding some down  here. Then we have revenue, and we also have some    
03:03:32: funding. So, let me just make this smaller because  I just want to show you guys how this actually    
03:03:36: works in practice. I just click save and start.  And basically, this thing goes on this service,    
03:03:40: Appify, and then goes and it scrapes it  for like some small little piddly fee. So,    
03:03:44: it's cooking up some data magic. Uh, let's just  wait until we see the very first result, which    
03:03:49: should be about 100 leads or so. And as we see  the first rung here has found a bunch of different    
03:03:53: leads from specific companies, company websites,  LinkedIns, their full names, their job titles, and    
03:03:58: so on and so forth. This is pretty cool, right? I  mean, this is just like a service that I'm using,    
03:04:01: and it returns a bunch of leads. And so, for  the purpose of this demo, I'm going to assume    
03:04:04: we're only using like simple services like this.  We're not actually rebuilding the wheel. Although,    
03:04:08: I should note that you totally could rebuild the  wheel if you wanted to. It's just uh, you know,    
03:04:12: it's not super easy, right? Like, this is really  the moat nowadays. It's not the app interface    
03:04:16: that you build. Sorry, that's the wrong one. Uh,  where are we? right over here. Okay, so basically    
03:04:22: in order to run this, right, logically what we're  going to need is we're going to need an API token    
03:04:26: and then what'll happen behind the scenes is this  Appify API token will plug into this search. Okay,    
03:04:32: then it'll use some data with an input like  this via API and then it'll find us a bunch of    
03:04:39: of stuff. And then on the back end, we're going to  do is we're going to enrich emails using a service    
03:04:44: like this. Basically, not all of the emails  that come from this service are going to have    
03:04:48: um like all of the information laid out. So, we  can actually use another service called an email    
03:04:52: finder to enrich that. And then over here, um  we're going to pass in either our open AI key or    
03:04:57: anthropic API key, whatever one works, honestly,  and then use that to generate personalized    
03:05:02: snippets of text that basically are going to allow  us to personalize the emails that we send. So,    
03:05:08: hopefully we're all now on the same page.  This is a pretty niche service, but you know,    
03:05:11: the best SASes do tend to be pretty niche and um  you know, that's more or less what we're putting    
03:05:15: together. We also have an instantly API key for  one-click campaigns, which are basically where    
03:05:20: we'll just upload the leads automatically. I  don't actually know if I'm going to do this    
03:05:23: cuz the instantly API had a bunch of issues last  time I tried, so I might not. And then over here,    
03:05:27: we have the actual prompt engineering. You know,  I want to generate like a highly personalized var    
03:05:32: uh uh email, right? I want to say like, "Hey Pete,  been following you for a long time. I love what    
03:05:35: you're doing at XYZ company." because those emails  that I send when they're highly personalized    
03:05:39: like that tend to land a lot better. So here's  where you can actually define the prompt that    
03:05:43: we're going to use inside of the app in order to  generate these ice breakers. So you're an expert    
03:05:47: sales SDR. Your job is to create a highly relevant  one or two sentence icebreaker so on and so forth.    
03:05:50: This is this is everything here and the idea is  you'll get to change this over time and then you    
03:05:54: know save and then see your new orders and stuff  like that. Okay, so hopefully now we're all on    
03:05:59: the same page and I've created this demo. This  is basically like the vision of the app. What    
03:06:02: I'm going to do now is I'm going to go through  and just make a bunch of changes. Um, I'm also    
03:06:07: going to feed in like the API documentations or  the services that I want to scrape and use. And    
03:06:10: then my agent should do a pretty good job to  start. This is great. The Appify scraper that    
03:06:17: I'm using to generate leads doesn't require a  LinkedIn sales navigator URL. I'll give you the    
03:06:22: Appify API below as well as everything that  you need in order to make this request, but    
03:06:27: you'll have to modify the new Scrape job form to  reflect that. What we'll do is we'll pass in a job    
03:06:33: name and then we'll have AI convert that job name  into a list of filters that work with the specific    
03:06:40: um Appify scraper that we're using. We also need  a way to be able to click into the orders under    
03:06:46: order history and then open them in sort of a  sidebar. Also, right now nothing happens when    
03:06:50: I click those three little dots or the download  button. Obviously, we're going to need to download    
03:06:54: these CSVs. Under the configuration section, let's  start with the Appify API token up at the top.    
03:07:01: Then let's do the Anthropic and OpenAI API tokens  underneath. And then let's remove the instantly    
03:07:06: API token completely and have the any mail finder  down below. The idea is going to be our Appify    
03:07:11: actor is going to return most of the information  that we need rather than treat OpenAI's API key    
03:07:19: as a fallback. Let's just treat it as another  option they could go through and then let's    
03:07:22: just prioritize anthropic. For instance, if both  the anthropic and open AI API keys are filled out,    
03:07:28: the model should automatically choose anthropic.  If anthropic is empty and open AAI is uh present,    
03:07:33: then we should automatically choose open AAI.  And we'll just proceed in that manner. And then    
03:07:37: for prompt engineering, I'm actually going to  give you a big long prompt that you could use to    
03:07:41: significantly improve the quality of the output. I  want you to incorporate this. Once we're done with    
03:07:46: the front end, we obviously need to work out the  back end and have all these functions available.    
03:07:51: So, what I'm going to do is I'm going to create  av and then I'm just going to paste in all my    
03:07:54: API keys for you so that you have them. You  can use this as demos to basically test the    
03:07:58: backend functionality and we could use these  and store them um in a static database for now    
03:08:03: just in like JSON files or or whatever. When we  eventually push to our database and use superbase    
03:08:09: um then we can make these more dynamic. I think  you have everything that you need. If you have any    
03:08:14: uh questions or misunderstandings or  whatever, just give me a shout. Cool.    
03:08:17: So now I'm just going to go through and then give  it everything that I promised. So the appy API is    
03:08:23: going to be here. It's going to go right into  the app API docs. Now what we want is we want    
03:08:30: to run the actor synchronously with the input and  return the output. I believe return the data set    
03:08:40: items rather. So I'm just going to see if I could  copy this whole page. Can I copy this whole page?    
03:08:45: Sometimes Appify has the ability to copy the whole  page for AI. Yeah, it does. So, copy for LLM.    
03:08:50: Paste that in. See how long that is? That's super  long. Yeah, it's pretty long. And then I also want    
03:08:57: to paste in the specific stuff about the actor.  So, this is the specifics about the actor. Input    
03:09:05: schema for actor is here. And then, um, I also  promised that I'd feed it in a big long prompt.    
03:09:14: So, I'm going to go over to Maker School wrapped,  which is massive document that I put together that    
03:09:19: basically guides everybody through how to write  like super high quality cold emails. And then I    
03:09:24: have a little prompt here that actually you guys  could use as personalization. So, what I'm going    
03:09:29: to do is just going to type personalization and  start down at the bottom. There we go. And this    
03:09:37: is going to be the prompt which I'm going to feed  in right here. Here's a personalization prompt.  
03:09:46: For the personalizations, use Claude Sonnet 4.6  or uh uh GPT 5.3. Check out both of their docs.    
03:10:00: Okay. And then I think that has everything  that I told it that I would give it. I mean,    
03:10:04: this is pretty long, right?  Just make sure. Okay. So,    
03:10:06: I'm going to create av and then um paste in  all my API keys for use. That makes sense.    
03:10:12: So I'm going to go over here and then just go env.  And then I'm now going to go find a bunch of API    
03:10:17: keys on all the services that I promised it and  then just paste them all in. So this is going to    
03:10:21: be my enthropic API key right over here. Then go  apply API key. So I head over to appy, go to my    
03:10:29: console. There's always a way for us to grab our  API key from whatever service we're using. So I'll    
03:10:37: go up here to API and integrations. We'll create  a new personal API token and I'll call this for    
03:10:42: SAS app. Should I limit token permissions?  Should I set the expiration date? H yeah,    
03:10:49: I'll set an expiration date just in case I forget  to delete it. Okay, this one's expiring tomorrow.    
03:10:54: That's all good. I'm going to copy this now. Paste  that in. Uh I need my open AI AP. Actually, do I    
03:10:59: need my open APK? No, I don't because I'm going to  use the anthropic one. Ah, I suppose uh the other    
03:11:04: services that I need, I can find them by looking  at my Vit app right here. Any MailFinder API key,  
03:11:15: paste that in. So, we'll go to any mailfinder,  log in. I'm going to go up to the API and I'm    
03:11:20: just going to copy this token right now. Go back  to anti-gravity. Feed that in. And we should now    
03:11:24: have everything. So, I'm going to press enter. And  I think this is now going to be able to develop    
03:11:28: the rest of our app, at least for now. Uh, this  is going to be like kind of what we see above the    
03:11:34: fold. Let me just be smart about this. Don't  just paste the prompt in verbatim to the user    
03:11:38: editable section. Obviously, it's pretty long. All  right, we've made a couple of changes here. Now,    
03:11:43: we have find me VP sales and practice owners at  dental clinics in Canada. I want companies with 11    
03:11:47: to 50 employees. That's kind of cool. If we go to  orders here, can we actually click on these? Yes,    
03:11:51: we can. As you can see, we now get a little  sidebar. Um, the sidebar is kind of small,    
03:11:55: so I'm going to adjust that in a second, but  it is still pretty neat. I mean, I can click    
03:11:58: the download verified CSV button here. So, it's  pretty nice. I like this. I really like the fact    
03:12:02: that we have this little job. It also pumps up so  quickly. It just makes it seem really snappy. And    
03:12:08: here is the prompt engineering. So, the prompt is  just pasted entirely in now, which is nice. Yeah,    
03:12:14: it's basically perfect. We do have um what looks  to be no training examples, but that's okay. These    
03:12:20: prompt variables are going to be injected as  the first name to lead, last name of the lead,    
03:12:22: headline, industry, organization name, location,  even their email address. That's going to be cool.    
03:12:26: And then we also have our uh our tokens in. So  now it's just time to actually give this a try.    
03:12:29: So I've just added the API keys right over here as  mentioned. And now we're basically good to go. I'm    
03:12:35: going to wait for this thing to relaunch the dev  server and then we're actually going to test out    
03:12:39: the flow. I should note that, you know, because  we are testing out what is essentially going to    
03:12:44: be the core function of our app, just like with  a full stack app, like the probability it'll work    
03:12:48: on the first try is pretty low. I found it kind  of interesting because a lot of people like they    
03:12:52: judge AI by its ability or inability to do things  in one go. uh human beings rarely do things in one    
03:12:57: go as well. The difference between humans and  AI models is silicon thinks at something like    
03:13:01: 10,000 times the speed. So you could just try  it 10,000 times faster. So you know whether or    
03:13:06: not this works in one shot is okay. We're just  going to go back and forth until it it works    
03:13:10: reliably. Um and then from there we're going to  pump this up to netify just like I had before.    
03:13:14: And then app number two, full stack app number  two, but total uh web app number three is going    
03:13:21: to be completely cool. I've just done this. Now  it's storing what's called local storage since    
03:13:24: of course we're always doing our our first jobs  uh or our first check statically. So let me exit    
03:13:29: out of my cloud API keys. Thank you very much.  Go right over here. Just relogged in and then    
03:13:34: I'm just going to go scrape leads. So I'm going  to say and I imagine there are going to be some    
03:13:37: issues here. Find me VP sales at dental clinics in  Canada. I want companies with 10 employees. Okay.    
03:13:47: And why don't we do I don't know 200 leads. And  then we'll go laconic or lassic. I don't actually    
03:13:54: know how to say that. Um and then we'll go error  executing leads workflow. Check console. I'll head    
03:14:00: back to console and then I see that we now already  have some issues not found. So what I'm going to    
03:14:06: do is I'm just going to scroll through this then  feed back to our agent. All right. After some    
03:14:13: back and forth, it's now telling us it's good  to go. I'm not entirely sure if this is true,    
03:14:17: but we are going to give it a try together. Uh,  I think it'll probably be over here. And then I    
03:14:22: go slash scrape. Find me some practice owners at  dental clinics in Canada. One to 20 employees.    
03:14:30: Cool. I'll press 100 max leads. We'll run the  workflow. We see here it's now doing what it's    
03:14:35: saying is a search extraction. And it looks like  it hasn't finished it successfully successfully    
03:14:41: because we're immediately getting a return  saying it's it's completed successfully,    
03:14:45: but it isn't. Let me just paste this back. I  ran this on localhost 888/scrape returned this    
03:14:52: and then I'm just going to paste it in. I'm also  going to uh paste in my um input as well just so    
03:14:59: that I could, you know, monitor this and also  maybe have a little bit more meaningful of a    
03:15:03: back and forth. Um but anyway, let's see what it  has to say. just as a form of parallelization.    
03:15:09: While this is debugging whatever the appy issue  is that's leading to um inconsistent output,    
03:15:14: I'm actually just going to have it adjust  the copy on the landing page as well. So,    
03:15:18: let me see here. Hey, this is fantastic. I'd like  you to change the copy on the landing page that    
03:15:24: it's a little bit more geared towards outbound  cold emails specifically. Um, also there are some    
03:15:31: minor graphical issues like the start for free  buttons arrow is on the same is on a different    
03:15:36: level than the text. I'm also seeing that there  are four cards under built for performance,    
03:15:42: but the fourth spills out onto the second row.  Let's do six cards instead. The main value    
03:15:48: props here are the breadth of contacts, the high  quality database, the high quality of enrichment,    
03:15:55: um the simplicity of the tool, the affordability  of the leads relative to most other people. For    
03:16:04: the AI personalization section, um under AI  personalization prompt, remove the export to    
03:16:11: oneclick instantly campaigns and then change  the language so it's not start for free.    
03:16:17: You just start. I'm also noticing that there's  no pricing section. Update it so that there is a    
03:16:21: pricing section. And make sure that everything in  the navbar is like perfectly centered. Right now,    
03:16:26: it's a little bit off, or at least it seems to be  off. Add a pricing section that is on average 0.05  
03:16:35: per credit. Every credit returns one verified  email. And then offer some higher and lower plans    
03:16:42: um that scale with price. Obviously, when  you purchase more, you should get more of    
03:16:46: a discount. Cool. So, I'm going to pump that in.  And then I'll say only modify the landing page.    
03:16:52: There are other agents currently working on other  sections of the website. Do not modify anything    
03:16:56: that is not the landing page. Also, don't you  don't need to rebuild. Okay. So, I'm going to    
03:17:00: have that operating at the same time as our other  tool, which is fixing the appy scraper. And then    
03:17:06: I can monitor this just by going back to command E  and checking out the agent um kind of conversation    
03:17:12: here. If I go to under inbox, you can see my  two open conversations. There's this one here,    
03:17:16: and it looks like we're still building or fixing  whatever the specific Appify problem was. Looks    
03:17:21: like it has to do with like hash IDs or whatnot.  Okay, so this is a good summary of where it's at    
03:17:25: right now. And then the landing page copy  builder is now doing some things. Cool. So,    
03:17:31: it's analyzing the landing page. And now it's  going to go through and actually write it.    
03:17:36: Looks like this search worked now on the uh  curl command that it created and it just did    
03:17:42: this to validate without me actually having to go  through and then do it all myself on the website.    
03:17:46: It's also reporting the specific issues. So there  was some location, some swallowed exceptions and    
03:17:51: so on and so forth. That's cool. And it also ran  the live test and it's asking me to do it again on    
03:17:56: um you know 888. So that's a different server.  Then I'll go what are we doing? Scrape. return    
03:18:03: me owners of HVAC businesses in Texas. Okay, we're  still getting the zero completed. So, let's go and    
03:18:11: debug Y. This is my input. Just go into the new  landing page update. We've now changed this to six    
03:18:17: rows, which is cool. This looks kind of silly.  So, I'm just going to go back here and say is    
03:18:23: currently on three lines. The on though the N  looks odd. Everything else here does look pretty    
03:18:32: solid though. I like that we now have a growth and  pricing plan with the same style. 49.99 and then    
03:18:40: 249. Super cool. And I'll just say let's dress  up that final CTA card down at the bottom. Cool.    
03:18:51: We'll go back to our appy scraper, see how this  is going. Just shut over a request here. And it    
03:18:55: looks like we are actually doing something which  is nice. Um, normally this would have immediately    
03:19:01: errored out, but it's either hanging or it is  doing what I asked it to do. I think this is hung,    
03:19:06: which is why nothing is occurring. If I  refresh this, I think the server probably    
03:19:10: went down halfway through. The good news is we  are populating the database, although either    
03:19:14: some design issues have occurred or something  is broken. But as you can see here, we have the    
03:19:19: status, the date, and then the verified emails as  well. I'm seeing no problems in the configuration    
03:19:24: side as well. So, it really is just the scrape  leads hangup. What I think I'm probably going to    
03:19:28: do given that this has taken me like 10 minutes or  so just behind the scenes is I'm probably going to    
03:19:32: go and just give it a bulletoint list of what it  needs to do. Like basically if you think about it    
03:19:37: um it needs to interpret my request. it needs to  convert that into an input friendly JSON object    
03:19:49: using um you know like a location table UTC.  Then it needs to send the request to um some    
03:19:58: big long URL which is going to look something  like this just with a different appy token.    
03:20:03: And then it needs to return to user alongside  CSV etc. I also think I might just simplify    
03:20:13: the number of steps so that all we're doing is  the appy search extraction then any mail finder    
03:20:16: enrichment for now. Um so I'm going to do that  next. Just heading back over here. Just going to    
03:20:22: paste all this in. I'll say let's adjust the logic  to the following. Okay. So I ended up running out    
03:20:28: of tokens halfway through this build. Let me just  show you guys what that looks like and then how    
03:20:31: you can solve it. So, basically, if you use Gemini  3.1 Pro, that obviously being the most in demand    
03:20:36: model right now, given the fact that it's, you  know, new, really good at UX and stuff like that,    
03:20:40: eventually you will probably run into some rate  limits. This case, this rate limit occurred after    
03:20:44: about an hour of this working independently on its  own to solve some problem with some rate limit.    
03:20:48: I just went and I walked away and then I came  back and then I saw that um sorry, with the uh    
03:20:53: with the app scraper. And so essentially how you  proceed from here, at least my recommendation is I    
03:20:58: would use a different model using the agent chat  UX. So I went down to claude opus 4.6. And then    
03:21:05: I said first generate a comprehensive prompt that  includes everything that we've talked about so far    
03:21:09: so I can paste it into another version of CC. CC  being cla. I'm now going to copy this. Okay. Then    
03:21:16: what I'm going to do is I'm going to open this  up in claude code. And not only am I going to    
03:21:21: open this up in cloud code, I'm also going to do  something called fast mode because claude has an    
03:21:25: additional piece of functionality that uh Gemini  does not currently possess. That is the ability    
03:21:29: to go very very quickly. I'm then going to double  check my extra usage. Looks like I'm 600 bucks in.    
03:21:36: So I'm just going to go extra- usage. Keep in  mind you guys aren't going to be spending $600    
03:21:40: and stuff on cloud code usage. Why don't I just  change this to 700? Um I just use a I use this for    
03:21:45: like so many different things, right? juggling  five or 10 projects simultaneously. So for me,    
03:21:50: 700 bucks in additional usage might be I don't  know an additional 20 or 30 bucks per project.    
03:21:56: Then I'm going to set that monthly spend limit.  Going to give that a little refresh here. Now    
03:22:01: it's up to 86% use. So I have 14%. Okay. And then  I'm just going to exit out of this and then go    
03:22:06: to a new one. I'm just going to paste all this in  now. I'll say proceed. And now there will be this    
03:22:14: little lightning icon down here which denotes that  it's in fast mode. And then I get to make use of    
03:22:18: um you know claude code or claude opus 4.6  thinking I should say on fast mode while I wait    
03:22:23: for my Gemini usage limits to come back. Now you  don't have to do this. If you don't want to you    
03:22:28: know juggle multiple models like I'm doing right  now. If you're happy to trade a little bit of time    
03:22:32: for speed then by all means absolutely go ahead  and just use like the claw opus 4.6 built into um    
03:22:38: the Gemini or agent chat inside of anti-gravity.  In my case, I want this to work as quickly as    
03:22:43: possible since on kind of a time crunch here. I'm  going skating with my girlfriend. So, we're going    
03:22:48: to see how much of this we could do in 15 minutes  just using the fast mode. And I'm happy to make    
03:22:52: that time money trade um as necessary. What you'll  see about Claude is it's just significantly I want    
03:22:59: to say more verbose with its notifications and  the information and it's also a lot easier to    
03:23:04: follow along. That's one of the downsides of the  Gemini series of models, just like a little less    
03:23:08: interpretable. Um, the thinking tabs and stuff  like that here are basically just in natural    
03:23:12: language and I can follow along with them almost  as if it's me doing the thinking. Uh, which is    
03:23:17: one thing I appreciate. Obviously, you do have to  weigh each of these minor pros and cons against    
03:23:22: uh, you know, the model's ability to do things  like do front-end UX is really pretty and and so    
03:23:26: on and so forth. Cool. So, this looks pretty solid  to me. We now have the server. It's going to test    
03:23:32: the API endpoint directly and it looks like we  have some internal server error. It's now just    
03:23:36: going to go through and then update model ids and  make minor terminations um as to what the error is    
03:23:41: until we're we're good to go. And it's telling  me that it is currently running an appy actor    
03:23:46: run. So I'm going to take a peek at this right  here. Looks like we ended up finding five leads,    
03:23:51: which I think was initially what we asked for.  Going to head over scrape here and I'll say HVAC    
03:23:55: owners in Texas. Let's do 100 leads. We'll run  the workflow. Looks like we've now generated the    
03:24:00: filters right down below. So, it's now scraping  leads with this poll. And um this is just for I    
03:24:05: guess our own our own purposes essentially. You  know, if we ever want to modify what the target    
03:24:09: audience is or our job name, we can do so just  by maybe being a little bit more descriptive or    
03:24:14: maybe being a little less descriptive. Okay,  we've now completed the job. We have the CSV    
03:24:18: over here and I can actually open it and you  can see all these leads are now scraped. So,    
03:24:22: we were basically like 99% of the way there right  before I ran out of tokens. Just needed uh another    
03:24:26: model to get it over the line. This looks great.  Now let's re add the personalization workflow.    
03:24:34: Use claude sonnet 4.6 as well. Okay. Now I'm going  to do the exact same thing. HVAC owners in Texas.    
03:24:42: We're going to test the lead scraping. We can also  test the AI personalization as well. I'm doing 100    
03:24:46: leads. So this should occur reasonably quickly.  Should be another five or 6 seconds. Okay,    
03:24:51: looks like we're done with that. Now we're  doing AI personalization. So Claude in this    
03:24:54: case is generating personalized ice breakers  for all of the leads that are in our database.    
03:24:58: Something I'm noticing here is the AI  personalization is taking more than five    
03:25:02: or 10 seconds. I imagine this is probably because  we're passing 100 rows sequentially or serially.    
03:25:06: If you think about it realistically, you don't  need to do that sequentially or serially. You    
03:25:09: could do that parallel in a parallel and send 100  requests simultaneously, whatever the the rate    
03:25:14: limits are. So, I'm going to ask it to do that.  I'll say batch the requests. Make do whatever    
03:25:19: you have to do to make it faster. Okay. I'm then  going to rerun this. We'll go I don't know HVAC    
03:25:25: owners in Canada instead of Texas. Let's just  make sure that lead generation uh filter thing    
03:25:31: still works. So, this is now Canada. We still  have a bunch of size filters down here as well,    
03:25:34: which is cool. Because I'm only doing 20, this  should occur significantly faster. We're now    
03:25:39: moving on to the AI personalization step. And  then at the end, we're now at completion and    
03:25:43: export. That looks great. We're going to download  the CSV. Just going to open this up again. Make    
03:25:47: sure we have that personalization column. Where  is that personalization column? Here we go.    
03:25:53: Hey, Jean Michelle. Revolutionizing luxury best in  77 is no small thing. Bane Ultra's legacy speaks    
03:25:59: for itself. Wanted to run something by you. So,  I'm not really liking how this is looking. It's    
03:26:02: just a little too much right now. So, I'm going  to want to make this significantly more casual    
03:26:05: and cleaner. I'll head back to configuration.  Okay, these are looking a little better. Still    
03:26:10: probably not the best personalizations we could  be doing, but I think just for the purposes of    
03:26:13: demonstration, I'll leave it there. Hey Kate, love  what you're building at Posh, also in engineering    
03:26:17: services. Wanted to run something by you. I  can see that work reasonably well as an email    
03:26:20: icebreaker. So, let's just exit out of this. We'll  close this older one. And uh from here on out,    
03:26:25: all we really need to do, if you think about it,  is we need to fix this UX problem. Um we need to    
03:26:31: add authentication with Superbase. And then we  need to take this puppy live. So I'm just going to    
03:26:35: do a big voice dump here and get it to the point  where the quality is significantly improved. I'm    
03:26:39: going to do that as taking a screenshot of this  section. And then coming back to Claude, we'll    
03:26:45: paste this in. Then I'll say, "Hey, the current  app looks great. There's just a few issues.    
03:26:52: The order history page looks really squashed and  not at all like the rest of the pages. I want it    
03:26:57: in that nice clean style um similar to the scrape  page and the configuration page. We also need to    
03:27:06: put this live and uh get this on superbase. So  I'm going to set up a superbase instance and I'd    
03:27:12: like you to assist me in the connection of that.  We need all of the fields of relevance including    
03:27:20: um database fields for the configuration, the  prompt engineering, API integrations, basically    
03:27:25: whatever you've done locally just applied to um  you know a database instead. Last but not least,    
03:27:32: when you click on an order in order history,  it opens up this nice side modal, but it's    
03:27:37: not very tall at all. I want it stretched out to  contain such that I don't have to scroll through    
03:27:44: um the div containing all of the information. If  that's unclear, just let me know and I'll clarify.    
03:27:51: I'm going to dump this in and then I'm also going  to just because I'm using a new instance of cloud    
03:27:56: code here. Just going to go back and then I'm  going to copy all of this. And I'm doing that    
03:28:03: because I want to give it context, but I also  don't want it to like go ahead and redo stuff on    
03:28:06: the app ify scrape and so on and so forth. While  that's occurring, I'll head over to Superbase.    
03:28:10: And then we'll click start your project. I already  do have a couple of apps set up. I think what I'm    
03:28:15: probably going to do is just delete one of these.  H probably delete the proposal generator app and    
03:28:22: then set up a new one just because I think you're  only allowed two on a free plan. And um I want to    
03:28:26: show you guys how easy it is to set all the stuff  up. So just going to delete that. And then I'll    
03:28:30: go new. I'm going to call this one um let's go  Nick J Wellsorg. We're going to call this leadso    
03:28:38: DB. I'm just going to do a strong password  automatically here. Copy that. And then I'll    
03:28:43: enable the data API. Click create new project.  I'm just going to give it all the information    
03:28:48: that uh it needs in order to set up this database  just like I did last time. Okay. So, first thing    
03:28:54: is head back to anti-gravity. I'm just going  to paste this in. That's my DB password. Then    
03:29:01: I'll head over to this left hand side here where  it says project settings. I'll go project name  
03:29:11: and then we'll also go project ID.  
03:29:17: I think there's one more. We just  need the API key so we could do a    
03:29:20: lot of that work for us. So we'll go secret key.  
03:29:28: And then we'll also go superbase public key.  We'll copy that as well. And this should have    
03:29:35: everything that we need. I think what it's  going to do now is probably just set up O for    
03:29:39: us. So head over to authentication where it says  email. And this time I don't actually want it to    
03:29:44: confirm the signup. So I'm just going to go back  to emails and then where I click on sign on signin    
03:29:50: providers. I'll just turn off confirm email. That  way I can make an account without having to do    
03:29:54: that back and forth. Great. set up superbase and  off. I'll give a bunch of information here. So,    
03:30:02: I think this is probably everything that it  needs and then we're just going to head over to    
03:30:06: um SQL editor where it's going to give us  a bunch of SQL for us to paste in. Now,    
03:30:10: my Gemini usage limit resets just in a few  minutes here. Um just because I have all of    
03:30:14: the context inside of Cloud Code and it's going  through and doing this work, I'm probably just    
03:30:18: going to continue in this Cloud Code thread  at least until I'm done this migration.    
03:30:22: um then I can start up another agent chat  uh using you know anti-gravity's built-in    
03:30:26: functionality and then have a conversation with  it. Uh in general you don't really want to jump    
03:30:30: around between one model and the next unless you  can either fully export the conversation history    
03:30:34: or you could do some sort of midway summary like  I just did a moment ago um from the anti-gravity    
03:30:38: to claude or sorry from the agent chat to Claude  code direction. If I were to go the other way,    
03:30:44: I'd do the exact opposite. I asked Claude to give  me a detailed project description of everything    
03:30:48: that is currently occurring and all of its current  context. So I could immediately just segue that    
03:30:52: into um the the conversation with Gemini 3.1 Pro  high. Okay, it's given us a plan and I've already    
03:30:58: enabled this plan and let it go. So we have the  superbase URL, the anon key, service ro key and    
03:31:03: and so on and so forth as well as a bunch of  other information here. It's going to start    
03:31:08: with the environment variables, give me an SQL  migration file, do some client updating, add a    
03:31:13: bunch of protected routes using authentication  middleware, finish the login and signup pages,    
03:31:17: have a log out function as well, set up the config  page, do the orders page, do the scrape page, um,    
03:31:23: set up the API layer, and then connect that to  Netlifi functions before finally building and    
03:31:28: verifying. There's going to be some back and forth  there for sure. Um, but just like we did this with    
03:31:32: Gemini 3.1 Pro High, we'll do the same thing  here. So, I have the migration right over here.    
03:31:36: I'm just going to copy all of this in. And then  we're just going to remove these little comments.  
03:31:47: And then what I'm going to do is just click  run. This will go through and then set up    
03:31:51: our database. You can now see this in database  because we have a scrape jobs table with all of    
03:31:56: these fields. The user configs table with all  of these fields as well. Any mailfinder key,    
03:32:00: system prompt, instantly key, and so on and so  forth. And these are all going to be um sort of    
03:32:04: fed into this authenticated user. So this is what  the authenticated user will sort of have access to    
03:32:09: when they go from one route to the next. At the  same time, it's going through and then updating    
03:32:13: everything that it's set up to do locally using um  JSON and JSL files to work through, you know, API    
03:32:19: requests to the Superbase PostgresQL server to the  Superbase Postgrql database. And this is actually    
03:32:25: a really good use case of using two different  models. The first is to build and the second is    
03:32:30: to basically spot check what the first model did  without full context. The reason why is because    
03:32:34: when you don't have the full context, your uh  opinions aren't really like polluted by the fact    
03:32:38: that you're the one that spent all this time and  energy working on it. Just like you always have    
03:32:42: like empirical or peer reviewers in papers and  and studies and research and stuff like that. So    
03:32:47: too do I recommend doing this with models as well.  Having an unbiased third party review our code is    
03:32:52: what is ultimately going to make our code and our  app significantly higher quality. Funny how models    
03:32:57: are kind of like people in that way. We could  theoretically go back and forth and back and forth    
03:33:01: with Claude Opus 4.6 designing something, Gemini  3.1 Pro High designing something else. Um, but I    
03:33:07: think just one of these passes is good enough. And  in a way, that's what we're already doing with our    
03:33:11: security audit if you think about it. Okay, it's  asking me to run the migration. I already did. So,    
03:33:14: I'm saying done. Let's test it. It's now going to  launch this live. And imagine there'll probably be    
03:33:19: some back and forth just like there was before.  Why don't we click get started? I'll say nick    
03:33:23: sarif nick atniki.com and then we'll go I don't  know nikki nikki. Click sign up. Okay, we are    
03:33:32: now being automatically taken to that config page  just like I wanted to. So here is where we'd set    
03:33:36: up our keys and then we have that prompt which is  automatically set up. That's kind of cool. Okay,    
03:33:41: I think what we need to do is we actually need to  modify this prompt to make sure it it's actually    
03:33:44: like being reflected in the end result. Um and  then obviously we need a way to stick our tokens    
03:33:49: in there. So, what I'm going to do for now is I'm  just going to go grab the ENV file here. I already    
03:33:55: have my token. So, I'm going to copy this. I'll go  this API. Okay. Paste that in. Annie Mailfinder,    
03:34:01: we'll paste that in. Enthropic. We will paste  that in. Okay. Now, I want to save changes.    
03:34:08: Just reflect that this actually works. So, it  says saved. If I refresh this, I'm seeing that    
03:34:13: the state is the same, which is good. If I make  a spelling mistake here and save, I'm seeing that    
03:34:18: the changes are reflecting here as well, which  is good. I go to orders, there's nothing. Okay.    
03:34:23: If I go to scrape leads now and I say, find me  a bunch of HVAC companies in Canada, owners of    
03:34:29: HVAC companies in Canada, and I go 20 leads, and  I run this workflow, is this going to work? So,    
03:34:34: it's gone through and it's generated the filters.  Let's just see what it's saying here. It's now    
03:34:39: scraping the leads. Now, we're doing some AI  personalization. And I'm just playing around the    
03:34:43: UX here. This is nice. This is nice. and smooth.  I like this a lot. I also like these cute little    
03:34:48: animations and whatnot that it's decided to put  in. Okay, job completed successfully. I also like    
03:34:52: how on the lefth hand side it's renewed. I don't  like how this little um scroll wheel animation on    
03:34:57: completion and export continues. So, I'm just  going to head back, turn off the scroll wheel    
03:35:01: animation on completed when the job is scraped.  When the job scrape is complete, completion.  
03:35:13: Okay, that'll be good. But for now, let's actually  download the CSV. We got our leads up here. Just    
03:35:18: going to take a peek at them. Same thing I did  before. Okay, icebreaker is looking great. Love    
03:35:22: what Proparts doing in modular construction. Also  work in the space. Love the tutor teach model.    
03:35:25: Connecting educator students is no small fee.  That's reasonable. So this clearly inherited our    
03:35:29: good um result. Then finally, if I go to orders,  we can see this is now populating our database    
03:35:34: successfully. What happens if I click? Awesome.  We have all of the data. Looks really clean. We    
03:35:38: have the parsed filters. We have the profile  scrape. You can actually download the verified    
03:35:41: CSV here as well. That's clean. Very nice. Okay,  the last thing I'd say is this three. These three    
03:35:47: dots don't do anything. Also, the three dots to  the right hand side of an order in order history    
03:35:56: do nothing right now. Okay, that's clean. And  then if I go down here to log out. Okay. Well,    
03:36:05: let's just quadruple check everything else  is good. Looks like it. We're back here.  
03:36:13: I think it was nikki.com, right? Yeah.  Okay, cool. Awesome. And I'm just going    
03:36:17: to head back out and then test the rest  of my routes. So, if you guys remember,    
03:36:20: there was scrape. Okay, that doesn't work. There  was config and there was also orders. Okay,    
03:36:25: so all of the off middleware  here is working correctly. Um,    
03:36:28: how's our landing page? It's looking pretty  clean. We don't have payment functionality yet,    
03:36:32: which I'll cover in a second. This looks pretty  clean. If I click start, we go back. Nice.  
03:36:39: Also, dress up the footer a little bit more. It's    
03:36:41: quite small right now. That's on  the landing page specifically.  
03:36:47: Okay, this is cool. I like that little like light  effect that we got in the background. Real clean.    
03:36:51: Real clean. Um, product goes to product.  Pricing goes to pricing. Resources. Oh,    
03:36:56: there is no resources link. So, we don't really  need that. Uh, I suppose we could probably make    
03:36:59: a cute little logo. So, why don't we head over  to asstudio.google.com and just do that while we    
03:37:05: can. I'm just going to see if I could link an API  key. Okay, I need a different account for that.    
03:37:10: And over here, let's see if we can link a key.  And heading over here, let's see if we can link    
03:37:13: a key. Cool. Generate me a simple square  logo, minimalistic, uh, straightforward,    
03:37:20: but immediately interpretable and high-end for a  lead scraping SAS called Lezo. And then over here,    
03:37:26: the aspect ratio is going to be 1 one. And we're  going to see if we can generate a 2K um, result. I    
03:37:32: should also probably find some inspiration logos.  This looks pretty good just because it's simple,    
03:37:38: straightforward, and obviously it's sort  of unique. If this gives me a bad result,    
03:37:42: then I'll say something along the lines of that.  No, sorry. Flat icon style. Look at the below for    
03:37:49: inspiration. Mimic this. Okay. And then going  back to our landing page at the very bottom,    
03:37:53: you can see we have significantly more context  including the logo, bunch of information down    
03:37:57: here, and so on and so forth. I've also been told  that we should be good. Um, I just sign in here    
03:38:07: on this little orders panel. This looks like it's  opening up something, but it's not showing up. So,    
03:38:12: I'll just have to clarify a little bit more  what's going on. When I click the three dots,    
03:38:19: it looks like the menu is being hidden within  the div. Then, if I go back to AS Studio,    
03:38:27: we see we have this. This isn't bad, to be honest.  Great. Remove the text. Let's just keep the shape.    
03:38:32: Okay. And I don't know if you guys could see  this, but at the very top right hand corner, we    
03:38:35: now have our little custom logo put in. Um I mean  like I think this could probably be a little bit    
03:38:40: bigger. So why don't we make the background color  a little lighter gray? Looks good. Why don't we    
03:38:44: make the background color a little lighter gray?  Okay. And then if I go to get started, you can    
03:38:49: see that we now have that little new Leadzo logo.  And the colors here match the uh sign up button.    
03:38:54: So I mean, is this going to win any awards for  its design? Yes, of course. It's it's gorgeous.    
03:38:59: No. Uh, jokes aside, you know, maybe I had a real  logo designer come in here or maybe I iterated a    
03:39:03: little bit more on the logo, we'd have something  that looks a little bit better. But the rest of    
03:39:06: it looks real clean. I mean, if I don't know, this  was an Nvidia logo or something. I probably think    
03:39:10: this is like an Nvidia style interface. It's  wonderful. Um, so looks great. Let's launch    
03:39:15: this thing. Now, because we've done a fair amount  of work on Netlefi already, we had to use Netlefi    
03:39:20: to like do the backend functions or whatever. That  was the design um pattern that the agent decided    
03:39:26: on. This is already on Netlefi. All we really have  to do is just change the URL and then create the    
03:39:31: site itself. Just jumping into Netlefi here. There  is now a leadso project created a few seconds ago.    
03:39:36: Um that is manually deploying. I don't want it to  manually deploy. I just want to show you guys how    
03:39:40: you can link it with GitHub. So I'm just going  to pause this and say set up GitHub as well and    
03:39:44: then link the two. And so this now apparently is  online. If we go here we have leadzo.netifi.app.    
03:39:52: So this is actually on like a real URL. So we  could see up top. Um, I think this might have    
03:39:56: made the uh logo a little bit brighter than I  was initially anticipating, which is cool. But    
03:40:00: remember that I want this to be um, you know, on  GitHub as well. So, that's what we're going to    
03:40:04: do next. First, it's going to initialize the  Git repo. It may ask you to sign in if it's    
03:40:07: the very first time you've done this before.  I've done this many times before. So, my um,    
03:40:11: anti-gravity instance is basically already linked  to my specific GitHub account. It's now going to    
03:40:15: do what's called git ignore, which is take a bunch  of these files that probably shouldn't be pushed,    
03:40:19: like all of my API keys, then ensure that those  don't actually go live. Now it's creating the    
03:40:24: actual thing and then linking it to Netlify. It'll  handle whatever errors it has in its own syntax    
03:40:29: mostly autonomously. Just checking for mobile  optimization as well by making my browser window a    
03:40:34: little smaller and then dragging it all the way to  the left. This looks pretty clean to me. I don't    
03:40:37: see any major issues. Nothing so far. Nice. Cool.  All of these are arranged the way they should    
03:40:44: be. Pricing. Excellent. Okay. Get started today.  Beautiful. Now, how about the actual login page?    
03:40:52: Yep, that looks good. Then how about Nikki? Nikki  is the password. Okay, so the actual app page not    
03:40:59: super mobile optimized. Everything else is. So  what I'm think I'm going to do, which is my final    
03:41:03: command essentially, is excellent. The landing  page and a sign-in pages look great, but the um    
03:41:11: dashboard stuff after you sign in is not optimized  for mobile. Make sure that it works on mobile    
03:41:17: displays as well. And while all that stuff's  going on, I'm also going to do our security audit.    
03:41:20: What's cool is I could do a lot of these things  in parallel side by side. So whereas previously    
03:41:25: I had Cloud Code do the security audit, I'm not  just going to paste this big security prompt into    
03:41:28: Gemini 3.1 Pro High for a couple of reasons. One,  I've already used like $800 of my Cloud Code limit    
03:41:34: at this point and I don't want to spend anymore.  Um, another is that the Gemini model uh rate limit    
03:41:38: runs out at a specific time and then like it's  usually back within an hour or so. I think they    
03:41:42: do it like every 2 hours or 3 hours or something.  So yeah, I just uh Oh, and the third is I just    
03:41:47: want to test how it is compared to the Cloud Code  experience. So, we're going to allow this whole    
03:41:51: conversation here and then it's just going to  run through top to bottom and do that security    
03:41:54: audit. Um, what's cool is now we're pushed to  GitHub, right? Because we're pushed to GitHub,    
03:41:59: we can actually do a lot more of the um kind of  like uh version control based security things that    
03:42:04: we couldn't do that last time because it was more  of like a because we had just dragged and dropped    
03:42:07: the folder directly into NFI. So, it looks like  it's doing pretty well mapping out the front end    
03:42:12: and backend LFI functions entry points, checking  ignore for secret management. I'm just going to    
03:42:16: let this go on its own and then uh along with the  designed components and stuff like that, we can    
03:42:21: get to that um when it's all done. Heading back  to the app, which is now online, I'm actually just    
03:42:27: going to do one final mobile optimization check.  So, that looks really nice and solid. I'm now    
03:42:32: going to sign in. We'll go nickniki.com. And then  I think the password was like Nikki Nikki. Um this    
03:42:40: new scrape job here is looking really clean. As  you can see, we actually have that functionality.    
03:42:44: Let me just move my head. We actually have that  functionality now where all of it is contained    
03:42:48: within like a mobile browser um view which is  really cool. And then we also have that little    
03:42:54: navbar. So I'm going to head to orders. Orders you  know it's going to be a little tougher by nature    
03:42:58: I think but uh included this little horizontal  scroll wheel. And so I'm still technically going    
03:43:03: to call that mobile optimized. I guess we could  just like redo the whole structure and have job    
03:43:07: ID here, target request here, profile scraped  here, but it'd be a little bit annoying to do    
03:43:11: that. And I kind of like having a table. Tabular  data is um notoriously different to turn into like    
03:43:16: mobile optimized form when you're working with  tables and HTML. So I think I'll just leave that    
03:43:21: there. This page looks really clean. I really have  no issues. Um I'm I'm honestly quite pleased with    
03:43:26: the performance of Gemini and Claude Code together  on this app. So 10 out of 10 would do again. Um,    
03:43:32: we do have one more feature I guess which is that  feature that I talked about earlier where um,    
03:43:37: you know, if it doesn't scrape the leads through  Appify, uh, sorry, the Appify codec crafter actor,    
03:43:43: then I wanted to pass that off to Google Maps.  Uh, I think for the purposes of demonstration,    
03:43:48: like we're pretty close to just wrapping up the  app. And the purpose of this was not to do like    
03:43:51: some super crazy endto-end uh, like 500 different  platform scraping flow. The purpose is to show you    
03:43:56: guys how to wrap around an API and how simple that  is. So, I think I'll probably just leave that as    
03:44:00: that actor for now. But uh rest assured you could  very quickly and easily weave in uh you know logic    
03:44:05: like hey if this thing returns zero leads then I  want you to use this other approach. Um yeah that    
03:44:11: looks pretty good to me. I guess we could also add  that post any mailfinder step. H I might just do    
03:44:17: that instead once we're done the security audit.  Um generally speaking though you do want to do    
03:44:22: the security audits at the very end. So might be  skipping a step here. Not that big of a deal. Just    
03:44:26: wanted to make sure we're all on the same page.  On the security side, if I just open up this agent    
03:44:29: window, you can see that it has actually found  some major issues. Found major off bypass in the    
03:44:33: API routes. It also found a hallucinated enthropic  package dependency. So, it's preparing some final    
03:44:38: checks. That is a big deal, right? Um, you know,  it's done more or less exactly what I've asked it    
03:44:44: to do. Go through with a fine tooththed comb and  see whether or not we can access routes without    
03:44:49: actually having any sort of credentials. I can  open up the task right over here. And, uh, this is    
03:44:53: where we're at. The first phase was where it was  just identifying and running through the codebase.    
03:44:58: And the second is now where it's running through  every single step here sort of like a tabular way.    
03:45:03: It's now finishing up the report generation.  We're going to take a look. So this looks like    
03:45:08: it's quite critical. We have authentication bypass  and paid API routes, some hallucinated malicious    
03:45:13: package dependencies, missing with check clauses  and so on and so forth. So, what we can do is we    
03:45:18: can actually go through this whole thing and  not have this hallucinated anthropic package,    
03:45:23: but instead use the atanthropic-ai- SDK. So, I  think what I'm going to do is we're probably just    
03:45:30: going to push it. Okay, great. Do the security  fixes, make sure the app still works, of course.    
03:45:39: And now we're going to run through this big list  of detailed findings and fix it. Of note, this is    
03:45:43: significantly less secure than u the other app.  just off the get-go. And it's probably because    
03:45:48: we have some additional functionality where  we're basically like piping through API requests    
03:45:52: and whatnot, right? We're also using a slightly  different framework. We're using Vit instead of    
03:45:56: Nex.js, which I think solves a few of these. Um,  in total, I think the score is like something like    
03:46:01: 70% or so, whereas the previous app, I think,  was a little bit higher. But yeah, you know,    
03:46:05: some of these are quite quite severe. The fact  that you could bypass um the authenticated user.    
03:46:10: So if they're not authenticated, it skips the  check entirely and proceeds to use the fallback    
03:46:14: process API keys to execute the scrape. Any  visitor can hit this endpoint via curl or postman    
03:46:19: without authenticating and your server will gladly  run expensive API ampy jobs, open a analysis or    
03:46:23: anthropic calls all build to my personal account.  This is the same sort of issue that um I think    
03:46:28: there was with OpenClaw at the time where um  you know you could just like bypass one of    
03:46:32: the routes entirely, go on like their dashboard  and then if they had some little server bypass    
03:46:38: uh setting or flag not like explicitly opted out  of then you could actually just use their own    
03:46:42: keys. And so in this way a lot of people had their  keys used not only leaked but also used and run    
03:46:46: up something like 25,000 people. It's yeah quite  a big deal. Looks like we're now installing some    
03:46:51: input validation libraries and stuff like that  and it's fixing the bypass. I'll get back to you    
03:46:55: guys when all this stuff is done. Excellent.  Looks solid. We now have everything that we    
03:46:59: need. I'm just going to take a quick peek at the  final version of the app. Make sure everything    
03:47:03: here works the same way that it did initially.  Opening up another list here. And this looks    
03:47:07: solid. Excellent. So hopefully you guys now see  how you guys could use Gemini in conjunction with    
03:47:13: cloud code and anti-gravity to build an app not  only that has full stack database authentication,    
03:47:18: everything else, but that also wraps around like a  pre-existing API. As mentioned, a lot of fantastic    
03:47:23: um SAS apps nowadays will either incorporate a  wrapped API as like their main functionality or    
03:47:28: they'll like include this as one of the five  or 10 or 15 different things. Realistically,    
03:47:32: like the software is no longer the moat. It's not  really that like, you know, you're going to build    
03:47:36: something super incredible that solves a problem  that nobody else has ever solved before and then    
03:47:41: you're going to package it in a beautiful UX that  nobody has ever put together before and then, you    
03:47:45: know, put it on the internet and then that is what  is going to distinguish you out from from somebody    
03:47:49: else. And so in this way, you know, there are a  lot of short-term opportunities you could take    
03:47:52: advantage of through app creation just by wrapping  pre-existing APIs that already do most of the    
03:47:57: heavy lifting for you. And hopefully this Appify  example um was was a a good show of what that    
03:48:02: might look like. And by the way, just so we're on  the same page here, this is just one tiny little    
03:48:06: actor of like thousands of different scrapers that  you could use. Just scrolling through Appify here,    
03:48:11: you guys see there's stuff like uh Trip Advisor  review scraper, DraftKings Scraper, there's    
03:48:15: Instagram scraper, website content crawler,  tweet scrapers off Twitter, land.com search,    
03:48:20: Instagram comment bots, and so on and so on and so  forth. You could build whatever functionality you    
03:48:24: want just by wrapping them around this service,  which is quite affordable um and you know,    
03:48:29: straightforward and easy to use. And there also  a bunch of other services out there that are like    
03:48:33: this that do um similar things. So, I'm not going  to tell you how to use one service or another,    
03:48:37: but yeah, like this Appify or API wrapper game  is super super powerful and it's blowing up right    
03:48:43: now. The one thing that we didn't build today,  obviously, was the payments integration, which is    
03:48:47: sort of like that final missing piece. Um, so I'm  going to talk a little bit about payments now and    
03:48:50: then after I'm done talking about payments, we'll  actually go through and build our next app, which    
03:48:54: is going to be one that allows us to go uh allows  users that use our app to go from everything from    
03:48:58: like going on a landing page, clicking buy, buying  the product or service, having some tokens added    
03:49:03: to their account, credits, and so on so forth,  going through like a full-fledged onboarding,    
03:49:07: and then once the onboarding is done, basically  being able to use the app. And in this way,    
03:49:10: we've successfully built up both our understanding  and then our capability from plain old websites to    
03:49:16: um what will finally be like full stack apps that  combine everything that we've talked about here.    
03:49:20: Okay, so let's have a brief conversation about  payments. We've obviously set up authentication.    
03:49:25: We know what like the the general flow looks  like. When somebody signs up to your app, they    
03:49:28: can either get some sort of email notification  that they can verify after they're done with    
03:49:31: that. Then obviously they get they get access.  A lot of this is handled through authentication    
03:49:35: middleware and routes and stuff. Um, but basically  in our case with payments, we're going to add one    
03:49:40: final step. So, basically the user is going to  start by signing up, right? So, we already know    
03:49:44: how to do this. It's pretty straightforward.  It's off. After they sign up, they're going    
03:49:47: to be taken to their own private payment page  where they can pick a plan or buy credits. Now,    
03:49:52: if you're doing like a thumbnail lead gener a  thumbnail generator app, for instance, obviously    
03:49:56: it's probably going to be credit based. Um, if  you're doing something that maybe provisions    
03:50:00: access to like a subscription service or something  where it's like, you know, you pay once and then    
03:50:03: you do it monthly, then we'll probably do a plan.  um after the payment occurs, they'll get access,    
03:50:08: which is referred to as entitlement. They'll  use the app, which is called consumption,    
03:50:12: and then in some cases, like if you're using  credits, they may run out, in which case they go    
03:50:15: back to the payment. That's sort of how it looks  under the hood. In terms of like what's going on,    
03:50:21: um we're not going to do the payment processing  ourselves. Basically, everybody on planet Earth    
03:50:25: now just uses pre-existing options like Stripe.  And the whole idea is when a user clicks subscribe    
03:50:29: or buy credits or whatever um we just have an  agreement with Stripe where via API we redirect    
03:50:35: them to a Stripeh hosted checkout page. Stripe  already has all the language and handles the card.    
03:50:39: They do things like advanced fraud detection.  They do things like you know handle your tax    
03:50:43: obligations like receipts and stuff like that and  then they just send all of that stuff to the user.    
03:50:48: We never touch a credit card number. We just get  paid you know in return for doing this. Stripe or    
03:50:53: these other payment processors they usually make  like a couple percentage points. I think Stripe    
03:50:56: right now is 2.9 plus 30 cents per transaction  or something. Um, I'm very happy to pay the    
03:51:00: 2.9 cents not to have to deal with this because  in addition to this being like a real cluster,    
03:51:05: you know, don't want to swear too much on this,  but in addition to being a real pain in the ass,    
03:51:09: uh, it is also kind of like a liability legally.  And, you know, as app developers, I want to    
03:51:13: focus on building the app and marketing it and  stuff. That's what 99% of my work needs to be,    
03:51:17: not handling the legalities. So when the payment  succeeds, and it will if you know the the card    
03:51:23: is not fraudulent, if they cross their tees and  dot their eyes, Stripe will send our backend a    
03:51:29: web hook, which is basically just like an event  notification that says, "Hey, this user paid,    
03:51:34: this user that you've already signed up for."  So we have all their information and so so on    
03:51:38: and so forth. Their ID um is good to go. Then your  backend will receive that. It'll update a field on    
03:51:43: the user's record in your database. So in our case  our superbase that'll be something like plan is    
03:51:47: now pro or credits are 50 and then your app knows  what it's allowed to do and then you know as it    
03:51:52: uses and consumes those credits every single time  it'll basically make a request to the database    
03:51:55: just reducing that a little. Um and then you know  because it's like this you can now do a variety of    
03:52:00: of cool features. You could provision additional  app um credits or usage if you want. You have the    
03:52:06: ability to like upgrade people, downgrade  people, moderate your app and everything.    
03:52:09: So, three models are onetime purchase, which  is basically where you pay once, you get    
03:52:13: access forever. It's really easy to do. You're  basically just selling a service, right? So,    
03:52:17: you just flip a boolean on their account. Um, they  sign up via the Superbase O function. Now, they    
03:52:23: have like a little like user table. Inside the  user table, there's a field that says subscribe,    
03:52:28: question mark, and then it's either true or false.  In subscription, it's pay monthly and then the    
03:52:32: access continues. Stripe has a bunch of features  inside of it that manage recurring subscriptions    
03:52:36: or billing um on let's say a monthly or a weekly  or an annual basis. And basically what happens    
03:52:40: is once you have the payment success or payment  failure um you'll receive a web hook and then    
03:52:45: you just toggle that access and then Stripe will  manage that for you every single month. Basically    
03:52:49: uh whenever a a successful payment comes in,  you'll keep it. If a payment failure comes in,    
03:52:53: then you'll flip it. And then finally that  credit based usage where you basically just    
03:52:56: buy a bucket of different um tokens or credits or  whatever the heck. every time they hit your API    
03:53:01: to generate a thumbnail or scrape your leads,  you decrement the balance. When it hits zero,    
03:53:04: you will send them back to checkout and then  force them to do it again. So, all of the apps    
03:53:07: that we built in this course can use any of  these. Uh, if I was doing lead scraping, I    
03:53:10: would probably do either like a monthly plan with  credits built in or I just do credits. Um, for    
03:53:15: our thumbnail generator, we're just going to do  credits. But, you know, you you can use whatever    
03:53:19: combination of these you want as well. The three  things we're going to need in our codebase,    
03:53:22: and keep in mind like our models are going to  handle this for you. You don't have to do this,    
03:53:26: but basically we need an endpoint that creates  a Stripe checkout session and then redirects the    
03:53:30: user. So after the user signs up, they're going to  have to immediately go to this endpoint maybe with    
03:53:34: three maybe a page with three different pricing  plans or something. Then when they click on that,    
03:53:38: it'll redirect them over to Stripe with their  information. Then we need a web hook endpoint,    
03:53:43: which is just like a little um route on our  server that basically waits to receive a payment    
03:53:49: succeeded event from Stripe. Then it'll update our  database. And then finally, we need some way to    
03:53:53: check inside of our app before doing the expensive  thing like generating a thumbnail or whatever,    
03:53:58: does the user have valid uh plan? Do they have  valid credits? So that's exactly what we're    
03:54:02: going to do in the next product build. You guys  are going to see this hands-on. I just want you    
03:54:06: to know that basically this just stands between  like the authentication step, okay, and then the    
03:54:12: um like usage step. Basically now there's just  going to be an additional one which is payment.    
03:54:18: Before obviously I let people use their own API  tokens and stuff like that in the app. So we sort    
03:54:23: of bypassed this alto together. Now it's going to  be you know like us doing the thing and therefore    
03:54:27: we're going to want to make some arbitrage. You  know they're going to pay I don't know $10 and    
03:54:32: then every usage is only going to cost us $1. And  so in that way we're going to basically make uh $9    
03:54:37: in profit. That's more or less how any meaningful  SAS business will operate. Okay. So hopefully you    
03:54:41: guys are as excited as I am. Let's dive into  it. So, in order to make any of this work,    
03:54:46: you are going to have to go to stripe.com and set  up an account. Um, I want you guys to know that    
03:54:51: if you don't have, you know, like an account on  Stripe set up, you're not really going to be able    
03:54:55: to follow along with me. But, at the same time, I  know that depending on where you are in the world,    
03:55:00: um, different people have different levels  of access to Stripe. They're not available    
03:55:03: in every country. So, if you guys aren't capable  of using whatever, you know, the specific solution    
03:55:08: I'm going to do, I recommend just use whatever  you guys have access to. Like, there's Payaneer,    
03:55:12: uh, I don't know, there's like PayPal. While these  services are not as clean and as good as Stripe,    
03:55:16: they don't handle as much of, you know, literally  global GDP at the moment. They're up to 1.6% which    
03:55:21: is insanely bonkers. Uh they're still pretty solid  and, you know, there's a lot you can do with them.    
03:55:25: Just trying to replace everything I'm about to  tell you with with that. So, you're going to    
03:55:28: have to go through some prolonged signup process  obviously and some of the stuff is going to take    
03:55:32: a while to implement. You're going to have to, you  know, verify your identity and stuff like any good    
03:55:35: payment platform. Um, but this is really clean  and it's it's a really good service. After that,    
03:55:39: you'll be taken to a dashboard that looks  something like this. in the top right hand    
03:55:42: corner there'll there'll be a little test mode  toggle which I'd recommend turning on. If you    
03:55:46: head to the top lefthand corner you can then go  switch sandbox and then click create sandbox.    
03:55:50: That's what we're going to do. Um when you go  through that little prompt uh create it or model    
03:55:53: it after you pre-existing Stripe account and then  you'll have an account that looks like this which    
03:55:57: basically will just model over your real account  and then give you the ability to like collect    
03:56:02: u publishable keys or secret keys at a  button. Make sure not to reveal these.    
03:56:06: These are super important if you did reveal like  your your real keys, not your sandbox keys. Um,    
03:56:11: a developer would basically have full access over  literally everything ever, which is kind of crazy.    
03:56:16: So, don't ever do that unless you want a random  $10 million bill in your Stripe account. They'd    
03:56:21: probably cap it after a few thousand, but yeah,  would not want that to happen to you. And then    
03:56:25: once you're done with this, you're you're actually  pretty good. We're just going to give our agent    
03:56:27: the publishable and secret keys, and then it'll  like handle the rest of the payments for us. Okay,    
03:56:31: so that's step number one. Step number two, I'm  just going to go back to anti-gravity. And then    
03:56:34: now, let's exit out of this lead scraping SAS. go  open folder and I'm going to call this thumbnail    
03:56:40: generator. Open this puppy up. And now we are  basically in a fresh uninitialized workspace    
03:56:47: here with just the folder name. And just like we  did the first couple of times uh to develop full    
03:56:52: stack apps. We're going to do more or less the  same idea. I'm going to go find a screenshot of    
03:56:56: something that I like that I think looks really  clean and that I want to model my app around.    
03:57:00: And then I'm just going to like voice dictate  give it a big dump of what it is that I want it    
03:57:03: to do. And then I'm just going to have it like go  and give me its demo. Um, once we have that demo,    
03:57:08: we can like in that little mining gif, uh, or  sorry, mining meme, we can like progressively    
03:57:13: mine all the BS until eventually we hit gold.  And once we've hit that little gold cavern,    
03:57:17: then we can actually do some work and make our  app better and better. Um, at a very high level    
03:57:21: though, uh, let me show you guys how I'm thinking  that this app is going to work. So, basically,    
03:57:26: um, just like we had before, you know, we want  a landing page. That landing page is going to be    
03:57:31: like any relatively simple marketing page, right?  What's going to occur is there'll be a little    
03:57:36: payment section. When they click on this payment  uh button or whatever, basically what's going to    
03:57:41: occur is they'll be taken to the authentication  or a sign up. Um after they sign up, they'll be    
03:57:46: taken to the ability to pay and that'll be  like the one click that takes us to like the    
03:57:50: Stripe checkout. We're going to do this based off  credits. So after they pay, we'll then provision    
03:57:55: access to the app. What's the app actually going  to look like on the internal side? Um well,    
03:58:00: it's going to be pretty straightforward. You're  going to have a dashboard which allows you to see    
03:58:03: all of your generated apps, uh, sorry, generated  thumbnails and everything like that. You're    
03:58:07: going to have like a config page similar to the  scraper that allows you to do things like upload    
03:58:12: images of yourself. Um, when you upload images of  yourself, uh, you'll be able to basically have the    
03:58:16: model generate thumbnails for YouTube or other uh,  content platforms that include you. Uh, and then    
03:58:22: we're also going to have like the generate page.  And this generate page is where we're going to    
03:58:26: be able to, you know, put in some some prompts  and and stuff like that. and then it'll pass    
03:58:30: through. And the idea is what we're going to do  is we're going to pass through using nano banana.  
03:58:38: And the way it's going to work is we're going to  feed in um like an inspiration thumbnail. And then    
03:58:46: in addition, we're also going to feed in a prompt  with changes. And then it'll do its best to model    
03:58:52: that. And it's not just going to do it once, it's  going to do it, I don't know, like three times.    
03:58:56: And then it'll spit out, you know, three potential  options, A, B, or C. And then you just pick one.    
03:59:04: And this is going to be the one that gets saved.  This is going to use our Nano Banana Pro key. And    
03:59:08: so in that way, it's going to be consuming our app  credit usage. Um, we're not going to go through    
03:59:12: the process of like signing up a developer app or  anything like that to to let that happen because    
03:59:17: sometimes some of these platforms are like, hey,  if you want to resell our tokens or if you want    
03:59:20: to resell credits, you need to go through  some additional steps. Um, but basically,    
03:59:23: in a nutshell, that's going to be your completed  one. And then this is going to show up in orders.    
03:59:27: And then every single time we do that, if you  think about it, we're also going to um consume    
03:59:31: some credits that they have because they're  buying based off of credits. So I don't know,    
03:59:36: maybe every time we generate we'll consume three  credits and then I don't know, maybe like it'll    
03:59:40: be like $1 equals 10 credits or something. We'll  keep it really simple obviously, but if you were    
03:59:46: a business, you'd actually want to run through  like the economics of pricing and stuff like that.    
03:59:50: Okay, so pretty straightforward, pretty simple.  Um why don't we start with that first step which    
03:59:54: is finding some design inspiration. Then I'm going  to do a big voice dump. After we're done with the    
03:59:57: voice dump and the design inspiration, we're going  to produce it locally. Once we produce it locally,    
04:00:01: we'll iterate test. Then we'll push it um to like  actual databases. We'll iterate test. Then we'll    
04:00:06: make it live on Netlefi. Iterate test. Then  finally, we do a security audit. Same thing    
04:00:10: that we did before. Just going to head over here  and I'll type web app because a lot of these are    
04:00:14: mobile based and I just want this one to be  not mobile based for now. I want this to be    
04:00:19: really clean. In fact, I want this to be like the  cleanest, sexiest app that we've developed so far.    
04:00:23: So, I really like this design. That looks really  clean, but obviously it's not like a like an app,    
04:00:28: per se. I also really like this design. Okay,  that's really sexy. I'm liking this like dark    
04:00:35: kind of like glass. I don't know what it's called.  Isomorphism. Like, this is crazy. Activating new    
04:00:41: brain paths. Look at how sexy that is. So,  we're going to go over something like that.    
04:00:45: This one's really, really good. This guy Jack R is  a freaking genius here. He actually included the    
04:00:50: font down below as well as the color palette and  everything like that. Um, this is for like some    
04:00:54: app that supposedly monitors your brain waves,  which is wild. Uh, we're obviously not making    
04:00:59: an app that monitors brain waves. We're making an  app that uh gets me more subscribers on YouTube,    
04:01:03: but still super clean. I like this. And the fact  that he provided the fonts and stuff means that    
04:01:07: I'm going for it. So, I'm just going to take this  image here, copy it, paste that into thumbnail    
04:01:13: generator, and then I'm also going to feed in  just some design information. I'll say font lufka    
04:01:22: um primary F4 E18E secondaries, and then I'll go  D6, D6, D5, and then D. Is that a B or an eight? I    
04:01:35: think that's a B. DB DB DB. Uh, anything else that  we need? We also have the white is going to be E3    
04:01:44: E3 E3 and then the black is going to be 043. Cool.  I'm just copying these over. I mean, obviously I    
04:01:50: could just provide a screenshot, but I don't want  to consume that many tokens for what ultimately    
04:01:53: amounts to just a few characters. Um, cool. This  looks really, really clean. I I like this. So,    
04:01:57: we'll see how this goes. I mean, I don't know if  it'll be able to replicate the glass eomorphism,    
04:02:00: but that's fine. Um, and then we'll close out  of these for now. Now that we're done with that,    
04:02:04: I'm just going to give a big voice dump of more  or less everything I've already told you guys. So,    
04:02:07: I'm not going to include this in the video so  you guys don't have to waste another few minutes    
04:02:10: hearing me talk about it. But, I'm just going to  go back here, double click my voice transcription    
04:02:13: tool, and then go for it. Hey, I'd like you to  help me build a full stack application. I will    
04:02:18: provide you with all the relevant API keys down  here for now. Build this so it works locally using    
04:02:25: JSON files as a standin for the DB. Later we'll do  the actual superbase etc setup. Cool. That looks    
04:02:35: pretty good. Um quite the long prompt here. That's  one of the reasons why I really like these voice    
04:02:38: dictation tools. You can just bang out, you know,  10 times the number of words. And what's cool    
04:02:44: is models are pretty capable at extracting your  meaning. Better just to talk like you're talking    
04:02:50: to a human being. Spit out whatever you can and  then the model will extract the important bits. So    
04:02:55: that's more or less what I did over here. It's now  going through this. It's generating um you know,    
04:02:59: a file structure using uh next.js, which  is what I asked it to use. Um and then,    
04:03:05: you know, I'm going to give it all the API keys  and everything like that after it's scaffolded the    
04:03:09: base structure. Okay. So, from here on out, we're  just going to sit around and wait for this thing    
04:03:12: to do its magic. Awesome. So, it just wrapped up  and I now have this live on npm rundev. I then    
04:03:18: navigate localhost 3000 and this is what it looks  like. So, this is unfortunately just calling it    
04:03:23: nano banana. I think it probably misunderstood  what I was saying, but that's okay. No big deal.    
04:03:26: Just going to refresh this here. See that we  have a bunch of the social proof pieces here.    
04:03:31: Global tech nexus, Nebula, and so on and so  forth. Professional thumbnail. Zero Photoshop    
04:03:35: skills required. That looks pretty clean,  honestly. Simple, pay grow. Pricing. I like    
04:03:39: that. Ready to blow up your channel. Create your  first thumbnail. Okay, so let's see what happens    
04:03:43: when I do get started. Takes us to this page.  I'll just say nikki.niki@gmail.com. Continue with    
04:03:50: email. Now we're being taken to a payment page.  This is really clean. I like this. Um hm. Going    
04:03:56: to click pay $10 here. It's empty, but we should  still be good. And now we're on the thumbnail    
04:04:01: uh generator side. So look at this generation  activity. Number of thumbnails generated per day.    
04:04:06: No generations yet up here. Generate new will take  us to this page. And we actually have a pretty    
04:04:10: clean UX. We have a generate magic inspiration  thumbnail. Generation prompt generated options    
04:04:14: 1 2 3. These are what are going to generate.  We have the number of credit cost. We have a    
04:04:19: settings page here with a reference face. We're  going to need multiple files. So I'm going to    
04:04:22: have to make that adjustment. And then you guys  can't see this because my face is in the way,    
04:04:27: but if I make this a little bit smaller, you see  how on the bottom left hand corner, we also have    
04:04:31: a credits available with a top up button. This top  up button is going to bring us back to this little    
04:04:35: payment page. Okay, so it's really clean, very  sexy, and pretty straightforward app. That said,    
04:04:40: I don't like the design. The design is sort  of like a big issue for me. So, I'm going to    
04:04:45: have it generate um a new design because I don't  like this. There are also some minor changes that    
04:04:49: I think need to be made. Notice how the margin  on the left moves around every time. Obviously,    
04:04:54: we have some minor UX changes as well, aside  from the design that I like to make. And uh yeah,    
04:04:59: why don't we pick a name? Why don't we call it  Thumbly? I think this is actually the the name    
04:05:03: of one of my startups now that I'm mentioning  it. It used to literally be called Thumbly,    
04:05:07: and it was something similar. I was like creating  uh thumbnails for people. Oh yeah, look at that.    
04:05:11: That's wild, man. I made this thing like probably  five, six years ago. That's a friend of mine,    
04:05:15: Zach, that since worked with Scaling with Systems  and a bunch of other people. Anyway, super clean,    
04:05:20: huh? Not gonna lie. Okay. Okay. This is how  it works. You basically basically generate    
04:05:25: thumbnails and then you can select them. Man, I  coded this by hand back in the day. Uh, okay. So,    
04:05:29: let's call this thumbly. And then let's also  make a bunch of changes. I'm just going to do    
04:05:34: some voice dictation. And then I'm also going to  like have it really push for that high-end white    
04:05:38: design style cuz I don't like this first demo. So,  I'm going to say let's call it thumbly feedback.    
04:05:45: And now I'm going to give it a bunch. The design  needs to be heavily modified. It does not reflect    
04:05:52: the provided image at all, unfortunately. On the  overview page, I'd like you to remove the average    
04:05:58: CTR impact section and then replace it with  something else that we would realistically have    
04:06:03: access to. The generation graph looks cool. When  I go between overview, generate, and settings,    
04:06:09: I'm noticing that the left hand margin of the  generated of the um elements on the right hand    
04:06:17: side are slightly off. I just want you to fix  them all so they're the exact same width. On    
04:06:21: the generate tab, auto prefill the generation  prompt with the user's templated prompt. Add    
04:06:26: a section under inspiration thumbnail where I  could just paste an image URL and then it goes    
04:06:30: and automatically populates it. Under settings,  we'll need to upload multiple reference faces. So    
04:06:36: have a ability to upload more than one, not just  one. And then in the default prompt instructions,    
04:06:41: this is where you'd automatically insert some  generated prompt in the generate page. So    
04:06:46: whatever the user writes here, I want reflected  in the generate page by default. And then the    
04:06:50: user can modify that slightly as necessary. On the  landing page, remove all references to nanobanana    
04:06:55: and replace with thumbly as mentioned. Add more  social proof here because we're running out of    
04:07:00: them pretty quickly as the business names scroll  to the left. Make the website landing page around    
04:07:07: twice as long in general. Finally, I'll say the  app needs a major redesign. Focus on the light    
04:07:11: theme as provided in the images above. Ensure  you're using the right font etc. We want light,    
04:07:21: not dark. Soft glows and futuristic glass style  aesthetics. Cool. I'm now going to give it some    
04:07:32: more time to make the required changes and  then I'll check back on the app. We're at the    
04:07:35: next leg of that redesign. So, I'm just going  to take another peek at localhost 3000. Well,    
04:07:40: it's definitely looking a lot brighter, which is  nice. Kind of weirdly yellow and green, which I    
04:07:45: don't really know how much I like. Uh, let's go  to the dashboard. Ooh, this is much better. Much    
04:07:48: better. I see that it's taking the inspiration  more on the actual dashboard side of things than    
04:07:53: it did on the landing page. And that's okay. Okay,  cool. It also fixed that margin issue that we had    
04:07:57: earlier. Um, I actually really like this. I'm just  going to zoom in a bit. Okay. I think what we need    
04:08:02: to do is we need to just widen it a bit. So, I'm  going to do the same thing. Hey, this looks much    
04:08:07: better. Could you widen the um elements in the  dashboard, the generate page, and the settings    
04:08:13: page? I feel like they're not very wide right  now, and that just looks silly. Um also, what font    
04:08:20: are we using? Are we using that provided font?  Some of the colors are a little too light now,    
04:08:26: I would say, like the highlight uh color on  the left handmost navigation elements. That    
04:08:33: light green or whatever it is, that neon color  is a little rough. So, I think we're probably    
04:08:39: going to have to reduce that just for contrast  purposes. Um, are we using real glass isomeorphism    
04:08:44: here? If you don't know what that is, um, I can  provide significantly more context. Anyway, uh,    
04:08:49: we do have some major issues on the landing page  side of things. This looks pretty poor. I think    
04:08:53: what I'll do is I'll just provide you a landing  page that I want you to copy verbatim like word    
04:08:57: for word because just the way that you're using  shadows and stuff like that looks really silly    
04:09:01: right now. Aside from that though, um, pretty well  done. I like this. I'll provide you that landing    
04:09:06: page and then you can try copying it verbatim  u to start and then we can make some other    
04:09:10: modifications afterwards. Here's the landing page.  Okay, that looks pretty solid. I'm just going to    
04:09:15: go and I'm just going to find a really classy  isomorphism glass. Okay, glass morphism, I guess,    
04:09:24: landing page. That makes more sense. Okay, we  just want one that like actually looks like a    
04:09:30: like a real app, you know, not one that's BS. So,  let me take a look what has like that light theme.  
04:09:39: Okay, I like this. This is pretty good. You know,  one of my favorite things to do is just to open    
04:09:43: up the local dev server and then just watch  as it slowly but surely updates the page and,    
04:09:49: you know, incorporates your device. It's kind  of neat. So, it's just done that up here. Um,    
04:09:53: it's just using some fake logo here to try and  mimic it, but obviously it's not the same thing    
04:09:57: as the actual logo. It's like adding small little  elements here or there, changing like the colors    
04:10:02: and the background and and stuff like that. Um,  so that's that's pretty cool. Quite sexy. I really    
04:10:07: like um being able to see that. It's doing the  same thing underneath with like the soft gradients    
04:10:11: and then obviously changing the uh the colors  and stuff because some of the elements have not    
04:10:16: been adjusted yet. Obviously, the background  in this case and the text is black. But yeah,    
04:10:20: as it continues, it'll just get closer and  closer and cleaner to that actual pixel perfect    
04:10:24: uh uh generation. Website's slowly getting  better and better. It's getting cleaner. Um    
04:10:28: all these elements now are starting to match  color-wise. We even have that little down CTA    
04:10:34: with that light blue. So, this is a much better  approach, I would say. Some other adjustments    
04:10:38: I went through and then in uh a lot more detail  basically deconstructed everything that I wanted    
04:10:43: changed. So I wanted to make the nav bar a little  bit square. I wanted to fill out the rest of the    
04:10:47: dashboard underneath the hero header, make the  social proof section infinitely revolving and so    
04:10:51: on and so forth. And the idea here is we just  want to get the app as close as uh possible    
04:10:55: to basically perfect aesthetically speaking  before I do all the rest of the work. Okay,    
04:10:59: we got the website right over here looking really  clean. Notice how we've gone through and then    
04:11:03: actually adjusted the dashboard down here. That's  really, really sexy. Um, I'm not liking the slight    
04:11:08: difference in Oh, actually, no. That's basically  perfect. Why don't we just, um, I think I'll    
04:11:13: probably square out all the buttons everywhere.  But anyway, this stuff's looking real clean. We    
04:11:17: have the pricing down below, ready to blow up your  channel. I'm just going to go to dashboard. Let's    
04:11:22: just see how the actual functionality of the app  is. This looks pretty good. Um, I don't really    
04:11:27: like the light blue in the back, so I'll adjust  that as well. But everything else is looking good,    
04:11:30: right? Like the margins are basically all the  same. Um, we also have emphasize contrast. So    
04:11:35: now the generation prompts are autopop populating.  And yeah, I mean, I'd say this is pretty great. I    
04:11:40: don't like the background blue on the um inside  of the app page, like the dashboard to generate    
04:11:47: the settings. That component looks weird to me.  I'd like some collection of soft gradients on the    
04:11:54: background of the hero header in the landing  page. And then I'd like you to turn all pill    
04:12:02: shapes right now into those rounded squares  instead. I think that just looks a lot better.    
04:12:08: For instance, the signup button in the navbar,  the real-time generation from your prompts widget,    
04:12:15: and the dashboard in the hero header um image. I  want all of those little pill shapes converted.    
04:12:24: Aside from that, change define to thumbly. I  want you to make sure that those two buttons,    
04:12:30: filter by CTR and plus new thumbnail, are just on  one line. Right now, they're both on two. Adjust    
04:12:35: the verbage if necessary. And then everything  else looks really clean. Yeah, that's about    
04:12:44: it. All right, this is looking a lot cleaner. We  have everything that we need on the landing page.    
04:12:49: Um, I like the fact that the cards no longer  look that ugly, atrocious blue. At this point,    
04:12:54: all we really have to do is provide  all of our API keys and tokens. So,    
04:12:58: as mentioned, I basically want to reproduce  the functionality of AI studio.google.com,    
04:13:02: except I want to be able to provide a thumbnail  and then a bunch of my own faces and then just    
04:13:06: have it replace the image in the uh thumbnail, or  rather replace the person's face in the thumbnail    
04:13:11: with my own. This is a pretty common thing to do  on YouTube nowadays. Basically what you do is you    
04:13:15: find like outlier really high quality thumbnails  and then you just replace them and make some minor    
04:13:19: adjustments. Um I'll show you guys what I mean.  If you head over to this app here, one of 10, and    
04:13:24: then you go down to, I don't know, videographer or  something, and you know, just look for something    
04:13:31: like this by this fella here, Kristoff Oliver. I  mean, like, is this the best thumbnail? Actually,    
04:13:36: no. Let's use this one. This one's probably  nicer. So, you see how there's like, you know,    
04:13:40: some fella here in the middle and then there's the  text around it and then there's some little image.    
04:13:43: So, I mean, like, you know, I think you'd probably  design something better than this, but still. I'm    
04:13:46: just going to save this image. Head over to AI  Studio. I wanted to just switch my account to    
04:13:51: one that actually has credits. What I'm going to  do is I'm going to stick this puppy inside. Then,    
04:13:56: I'll say replace the man in the thumbnail with  the man in the profile picture provided. Then, I'm    
04:14:05: going to look for a picture of myself. I like this  one. This one's pretty funky. So, I'm going to    
04:14:10: say replace the man in the thumbnail that includes  how to build a portfolio with a man in the profile    
04:14:17: picture holding a trophy. Okay. So, what I want  basically want to do, what I'm instructed to do is    
04:14:24: to take this and then just swap it out for this or  something close to that. So, I press enter. You'll    
04:14:29: see that it's not going to do the most amazing  job right off the bat, but it's going to do an    
04:14:32: okay job. And basically the whole idea is we're  just going to run this multiple times until we get    
04:14:37: like three or four options. And then we're just  going to present them to the user and then they    
04:14:40: can just select one that they really like. And  scrolling down here, you can see that we've since    
04:14:43: replaced that man just with me holding my trophy.  So it didn't get like exactly what I wanted to do.    
04:14:48: Obviously I don't actually want to be holding the  trophy, but you can see that I'm in this fell's    
04:14:52: room. And for the most part, it looks like me. I  mean, there's some minor little changes in terms    
04:14:55: of the skin texture and stuff. Um I think my skin  texture is worse and it's like done some done some    
04:14:59: touch-ups, but you know, it's got my hair. It's  got me holding the trophy. didn't add any extra    
04:15:04: AI fingers. And yeah, that's more or less what  we're doing, right? So the question is, how do    
04:15:08: we actually do this in our app, not inside of this  as studio.google.com thing and it's pretty easy.    
04:15:13: There's just like a bunch of API routes for image  generation. We just basically need to reproduce    
04:15:17: the same flow that I just did here over there. And  then we need to um connect API keys and tokens and    
04:15:22: stuff like that. So I have an API key over here.  Uh I'm just going to I don't know. I guess I need    
04:15:27: to find a way to copy this API key. So why don't  I go to get API key here. We'll create a new one.    
04:15:31: And I'm just going to call this um thumbly. Going  to click create. We're now going to have the key    
04:15:38: generated right over here. Okay. And I'm just  doing this in a new one because I want to be able    
04:15:43: to turn it off. I'll then go back to anti-gravity.  And then, okay, it's just done some changes for    
04:15:49: me. I don't know exactly what. Then I'm going to  open up av file and then I'm going to say Gemini.    
04:15:55: I think this is Gemini, right? What is this one  technically called? uh maybe like nano banana API    
04:16:02: key and I'm going to paste that in. Um there are  a couple of other things that we need if you think    
04:16:07: about it. So this is not enough. We obviously have  to go through the whole superbase spiel and then    
04:16:12: get a bunch of images. Sorry, I get a a database  from there. So I'm going to set up a database on    
04:16:17: Superbase just like I've done before. Head over to  superbase.com or rather I think it's database.new    
04:16:23: is even faster, right? Yeah, there we go. I'm  going to do it inside of proposal generator.app    
04:16:28: maybe gyro. Okay, never mind. I need to go and  delete one of these old ones, so bear with me    
04:16:31: one second. This is in the leado database, right?  So, I'm just going to delete this project. Leadzo    
04:16:36: DB. Cool. Thank you. Delete. Um, and then  I'll go to database new. Once that's done,    
04:16:44: now it's going to say, hey, let's make one. I'm  going to call this one um Thumbly DB. Again,    
04:16:50: I'm going to generate a password. Copy that  password over. Enable. Oh, cool. They also now    
04:16:55: have automatic RLS, which is cool. So, I'm going  to create a new project there. And what I want is    
04:16:59: I basically want to um paste in my database  password. Let's say superbase DB password.    
04:17:08: Paste that in. Um I don't know, superbase  project URL. Paste that in. Previously, I    
04:17:14: did this just directly inside of the um you know,  agent chat, but this time I'm actually going to    
04:17:17: copy and paste it over to the CNV. So, Superbase  publishable API key. I'm going to paste that in.    
04:17:26: I think there are a couple other ones. You know,  I just want to give it my API key as well. So,    
04:17:31: we'll go superbase project ID. Paste that in.  You can see it's the same thing as in my URL. So,    
04:17:38: basease project name I'm just coming up with all  excuse me, I'm just coming up with all this stuff    
04:17:45: um myself. Like I'm coming up with these names  myself. Um these aren't really important. The    
04:17:49: model can understand the context themselves.  Okay. So, I I have more or less all of that,    
04:17:54: which is cool and pretty clean. Um, and then yeah,  now it's just provisioning my database and API    
04:17:59: input. It's actually creating them for me. So once  all that stuff's good to go. I'm just going to    
04:18:04: paste that in. Any other additional functionality  we need? I don't think so. So I'm going to say is    
04:18:09: I've added a bunch of uh credentials for nano  banana and then superbase um into the env file.    
04:18:17: You now have everything that you need in order  to actually build out the functionality of the    
04:18:20: app aka the API calls. I'll go call or find the  um specific endpoint to reference. But basically,    
04:18:26: we're going to be replicating the functionality  of um Google's AI Studio just inside of my app.    
04:18:33: Let's see. ENV. Cool. And then, you  know, there should be the ability  
04:18:43: to grab the code. Okay, cool. And there  is. So, I can grab this code. And then    
04:18:48: we're just going to go rest here. And  then what I want is I basically just    
04:18:54: want to copy all of this stuff. And  then I'm just going to paste this in.  
04:19:05: Here is some REST code straight from their  dashboard. And then I'm just going to paste    
04:19:10: this in, which should be everything that they  need in order to actually like generate the    
04:19:13: the thing. Keep in mind we're going to  be supplying two inputs. The provided    
04:19:20: thumbnail image and our prompt uh I guess  three inputs. The provided thumbnail image    
04:19:29: um images of the person's face and then a prompt  
04:19:39: check there. Let me see. Are there any docs  or something like that I could use to give    
04:19:43: me more data? Okay, check their docs if  you need more on how to do this. First,    
04:19:51: test all of this via curl to make sure it  works. And then once it works, you can put it    
04:19:58: on the app. And then finally, I'm going to just  provide some base um data here. So, you know,    
04:20:04: earlier I had that portfolio builder image. So,  I'm actually just going to supply these images.    
04:20:08: Um, so this is going to be one image. I think  we can just open this in a new tab. Okay. No,    
04:20:14: I guess we can't. So, let me just save the  image. This is going to be the supplied. Okay,    
04:20:23: this one over here. Then I'm going to move into  anti-gravity. Just upload this to the agent. I've    
04:20:30: provided you three things. supplied the image to  insert a face into um face the image to get the    
04:20:46: face from and then prompt and the prompt is going  to be here. Let's just save this too. Uh this is    
04:20:56: pretty big actually. I don't know if we'll be  able to feed all this stuff in. Let's say face  
04:21:05: And uh it should be able to pull all  of this data up from just the names.  
04:21:11: Okay. In case like unless we get blocked, we  should be good. Just going to double check this    
04:21:17: because we we have supplied like a lot of image  files here. I mean this was like 4 megabytes.    
04:21:21: This here was like I don't know megabytes. So  in total it's going to be like five or six megs    
04:21:25: which is actually pretty chunky. Maybe they like  automatically resize the images or something so    
04:21:29: it's not taking up a massive amount of tokens. But  um you know I always do kind of worry like oh am I    
04:21:33: going to run out of usage and stuff. Okay. So I'm  gonna allow this conversation. It can do more or    
04:21:37: less whatever the heck it wants. And then um just  double checking thumbly. Yeah. I mean like this    
04:21:46: honestly looks really clean. I'm liking this quite  a bit. Nice. And then we have like this infinitely    
04:21:50: revolving social proof section here which you know  you stick your own social proof in. And then all    
04:21:55: of the um buttons and stuff like that are square  now which is cool. And everything is just a little    
04:22:00: bit more squared off. I don't actually like this  shadow. There's a slight shadow in the background    
04:22:03: here, which hurts, but not the end of the world.  We have the ability to change this. This is nice.    
04:22:08: Cool, cool, cool. Awesome. I mean, like, you know,  I think this is basically like the the MVP of    
04:22:13: um a high quality app with the landing page. So,  wonderful. I'm just going to wait and then um let    
04:22:18: you guys know when we're done this next step.  Looks like it's already making API calls, which    
04:22:22: is cool. Just using everything that I provided it  below. Generative language. Google APIs appears    
04:22:27: to be the endpoint. That's pretty nice. And  so it's gone through and actually verified    
04:22:30: that this works and it's created um another step  inside of implementation plan. So now it's going    
04:22:35: through and then integrating this directly into  the app. So it's not just going to be doing it    
04:22:39: via its own curl requests, but I'll be able to do  it via uploads files and stuff like that. Okay. So    
04:22:44: just signing in here. We've now integrated the  um database functionality. Going to go over to    
04:22:49: generate and see if we can do this. So you know  I can obviously add images and we just did. So    
04:22:54: now we have this cool little blur effect which is  really nice. Let me see. Keep the style identical    
04:22:59: to the inspiration image. Make the main subject  highly cinematic with dramatic neon backlighting.    
04:23:03: Contrast. So no, I'm going to say but replace  with the user. Oh sh uh crap. I need to actually    
04:23:09: provide images, right? So let's upload some faces.  Let's do face. This is now me. Okay. And then here    
04:23:17: inside of the default prompt instructions, I'll  say replace the thumbnail image with the supplied    
04:23:24: user cinematic. and I don't know dramatic lighting  on the face. Replace the face of the person in the    
04:23:36: provided thumbnail image with the face of the  supplied user. Cinematic and dramatic lighting    
04:23:42: on the face. Let's save the config. I'm just  going to refresh this. Has that been saved? Okay,    
04:23:46: it is. This has been saved as well. Okay, that's  great. You know, might as well test one additional    
04:23:51: piece of functionality here, which is if I could  just paste the URL in. So let's go back here,    
04:23:57: paste that in. Okay, cool. So we've actually  we've actually now got this in the URL, too,    
04:24:00: which is clean. I'm going to click generate  variance. And this is really like the test    
04:24:05: of the functionality. So I'm going to give  it a few seconds. Then I'll double back with    
04:24:09: um you know, changes if it didn't work, and  then maybe some next steps if it did. Okay,    
04:24:13: we've actually generated one of the options here,  and it looks interesting. Um for whatever reason,    
04:24:19: look, it's like the background's kind of white. I  don't know. And we've only done one, so we want to    
04:24:23: do three, right? Obviously, we're going to want  three. I see there's some click functionality,    
04:24:27: which is kind of cool, but um yeah, we're going to  have to do more. So, the first thing I mean, the    
04:24:32: dramatic lighting looks freaking badass. Like, you  know, it's not exactly my nose, to be honest. It's    
04:24:37: a little bit different for me, but still really  cool. Hey, we've um generated only one, not three.    
04:24:43: So, just double check and make sure that there  was no issue in the background that prevented us    
04:24:47: from doing um all three simultaneously because we  want to populate that with three thumbnail images,    
04:24:52: not just one. Also, when the images came out, they  had this sort of like white sheen or overlay. They    
04:24:59: looked kind of transparent. I just want you to  remove that. Um, so that I just can see the actual    
04:25:04: image immediately. Uh, and yeah, I think that's  about it. What's interesting is while it did that,    
04:25:10: it consumed three credits. Okay, so the credit  consumption functionality is there. However,    
04:25:14: when I saved this, it saved it twice. So, that's  another thing we'll have to change. This time    
04:25:19: we're going to do the same thing just with the  supplied version instead. And then I should just    
04:25:24: be able to click generate variance and we should  be able to do three, right? Since we're generating    
04:25:28: three times. So credits available um on the left  hand side, which you guys can't see. Say 197 right    
04:25:34: now. Okay, now we have three provided variants.  These all look awesome. I'm loving this. Loving    
04:25:39: the the really badass lighting on the face. That's  neat. Um so now what I'm going to do is I'm just    
04:25:42: going to select one of the variants that I want  to keep. So why don't I select this one? That one    
04:25:45: looks probably the most realistically me anyway.  And then I'll click keep selected thumbnail. It    
04:25:50: says thumbnails saved to your gallery, which is  awesome. Okay. And then we go back to overview.    
04:25:54: And then we can see this new one here. Beautiful.  Okay. So, I guess what else we need? Like the    
04:25:58: first thing comes to mind is we just need a way to  like delete these, right? Provide a way to delete    
04:26:03: um the thumbnails under recent generations.  Basically, I want to be able to delete ones    
04:26:07: in my gallery so that I don't have to see them in  the database anymore. Um aside from that though,    
04:26:11: everything looks like it worked really clean. Oh,  um, instead of like the alert that comes up, um,    
04:26:16: just make like a nice modal, a nice toast message,  um, that then allows you to, um, I don't know,    
04:26:23: open it in a new tab or download the image or, uh,  go back and generate a new one. Also, just little    
04:26:28: things. I mean, these intelligences are so dang  good. Notice how in this one here, I don't have    
04:26:32: the O behind my neck, but in this one, I I do.  Like, it's, you know, it knows the placement of    
04:26:37: the O and where it should be and stuff like that.  But yeah, um now that we're done with all this,    
04:26:41: what we're also going to do is we're going to  uh like after we get the little X functionality,    
04:26:46: we're going to hook this up to Superbase and then  it's just going to give me that migration script    
04:26:50: so that I could use this in like real production  scenarios. Then on from there, it's connecting    
04:26:55: it to Stripe so that the payments work and then  yeah, everything's just going to be 100% live,    
04:26:58: which I'm really excited for. Speaking of Stripe,  I forgot, but I do need to provide the keys there    
04:27:02: as well. So, let me head over to Stripe, sign  into that sandbox. It's right over here. And then    
04:27:07: I'll give both the publishable key and then secret  key. So stripe publishable key, stripe secret key.  
04:27:18: Then I'm just going to save this and say, hey,  I've also added the Stripe publishable key and    
04:27:22: Stripe secret key. I want you to connect the  payment feature as well. You may have to adjust    
04:27:29: the SQL migration script. So um do this first.  Okay. And the really cool thing is I can just    
04:27:36: queue up messages. So even if I change my mind  or do a bunch of things, I can have this message    
04:27:40: sent. I can then read that message and then just  um incorporate it in the flow. I don't actually    
04:27:44: have to wait until it it all finishes. So that's  pretty clean, huh? Pretty stoked about that.    
04:27:48: While we're waiting, why don't we test this on  another thumbnail? So I'm going to head back over    
04:27:52: to generate and then I'm going to paste this in.  Going to set that. I'll say replace the face in    
04:27:57: the provided thumbnail which is the face applied  to use cinematic and dramatic landing the face.    
04:28:00: Also replace 100 to 1,000. Let's see if maybe we  could get um a slight little variant of the actual    
04:28:08: number in the background as well. Generally  speaking, my experience with these AI models,    
04:28:12: you only really want to suggest one major change  at a time. So maybe what I could also do is add    
04:28:16: like a little tips feature or something like that  so that people know um how to prompt these things    
04:28:20: and get the best results. Nothing like clean work.  This one here looks real good. I like it. We have    
04:28:26: the 1000 in the background. Also dramatic lighting  on the face. That's cool. And this one has    
04:28:30: dramatic lighting on the face with my actual skin  texture. Thank you, Rosa. Um, honestly, I think    
04:28:35: all all three of these are really badass. So, I'm  going to keep this one. And as you can see, I'm    
04:28:39: going to have a toast message instead. So, I can  download this image. I can open in a new tab. Uh,    
04:28:44: that one doesn't seem to work, so I'm going to  have to modify that. And then I can also click    
04:28:47: generate another. It'll take me back to this page.  So, really, really clean functionality. I mean,    
04:28:50: this is basically exactly what I wanted. Just  wish it could be packaged in a slightly better UX,    
04:28:54: but we'll we'll solve that later. It's now going  through and just doing a bunch of Stripe stuff.    
04:28:57: So, creating API routes, resolving TypeScript  errors, and so on and so forth. I'll let it go    
04:29:01: and just do that thing. um as it wills and then  we'll double check how all that works with SQL    
04:29:06: and we're done with that. Okay. Now I'm going to  use the uh big thing inside of Superbase schema    
04:29:12: migration script the file that it created for  me. Then just hold command and press enter. I    
04:29:18: realize I used to think that you couldn't have  comments in here but uh you can. It's just the    
04:29:21: comments that the previous model did for me  were I think like with two hashtags instead of    
04:29:26: um two dashes. As long as there are two dashes,  you can basically pump this whole thing in and    
04:29:30: there are no problems. And it's always good  once you're done with that just to go back    
04:29:32: to database and then you can see how everything  interacts. So see the model here is set up ID,    
04:29:36: user ID, original image base 64, prompt, generated  URL, selected URL, and created at as well as ID,    
04:29:42: email, credits, Stripe, customer ID, subscription  ID, default prompt, face images B 64, and then    
04:29:48: created at. This is where we're basically going  to store their status. Okay? And then over here is    
04:29:54: where we're going to store the number of credits  that they have. So if they have a subscription ID,    
04:29:57: then they will have been signed up. Um,  obviously if they have credits, any credits,    
04:30:01: then we'll populate that. That's where we're going  to get this from. Um, and then if they're at zero    
04:30:05: credits, then when they attempt to make a thing,  it'll check their credit balance. And, you know,    
04:30:09: because they don't have any credits, that won't be  able to uh work. The primary key of thumbnails is    
04:30:13: ID. Primary key of users is ID. These two things  are sort of mapped together. And then, yeah,    
04:30:18: everything else here looks pretty solid to me.  So, just heading back to anti-gravity. Right now,    
04:30:21: what it's doing is just finishing up that little  migration from uh mock routes, which are when    
04:30:27: you store all of the database files and like, you  know, your your local computer to ultimately like    
04:30:32: live supabbase instances. And it's just doing a  build right now to verify that everything works    
04:30:37: uh the way that we told it to do it. And as you  can see, I've just signed into this supposed new    
04:30:42: account here and uh we are now at zero credits  available. So, it's pulling it directly from the    
04:30:47: database. Meaning if we want to run the full flow,  we now have to go through create a new account    
04:30:52: and then run basically the entire signup flow.  So I'm just going to go back to anti-gravity,    
04:30:58: verify that everything is good. Awesome. Live  database has now replaced our prototype API    
04:31:03: structure. I've now done it all. So we should be  able to test this. Just going to head back first    
04:31:09: to Superbase and then I'm going to turn off the  feature of authentication that forces us to um    
04:31:14: confirm our email. So you can do that in signin. I  just do that because it's a little bit faster. And    
04:31:18: I realized after that first build, I was spending  just as much time, you know, signing up as I was    
04:31:23: doing everything else. Now I'm going to click  sign up. And this is sort of the desired user    
04:31:26: flow. So we'll go nick@niki.com. Continue with  email. Let's see what happens. Just says signing    
04:31:31: in. There's no password. So this is a problem. Um,  notice how before we always had an email address    
04:31:35: and a password. Now we just have this like email.  So I think this is probably a blind spot where it    
04:31:40: didn't really realize, oh, okay, we're connected  to Superbase. Now we have O. So we're going to    
04:31:43: need an actual like login page. Hey, the login  right now only requests an email, but I need to    
04:31:49: authenticate with Superbase. I'm pretty sure we'd  need an email and a password. No, I just tried    
04:31:53: to create one and it didn't really work. There  were some errors. Okay, so now going to see if    
04:32:00: maybe I'm already logged in or something.  We go to payment. Yeah, no, we can't. So,    
04:32:05: I mean like the middleware routes are working as  we could tell with dashboard and stuff like that.    
04:32:08: Everything redirects us to login. It's just the  actual login doesn't seem to be um set up yet. So,    
04:32:13: we'll double click that. We'll double check that.  Um, it looks like we also added some additional    
04:32:18: landing page stuff here, which is super cool. So,  this added a whole new section based off what we    
04:32:22: added. AI power generation, AB testing, clean  modern aesthetics, and so on and so forth. We    
04:32:27: also have some FAQs here based off how it works.  So, that's really cool. And then we have the ready    
04:32:32: to blow up your channel. Um, Gemini will do this  from now and uh every now and then. I don't really    
04:32:38: sometimes it's sort of annoying when it acts  without necessarily asking you, but in this case    
04:32:42: it was what I wanted because really really early  on in the prompt I said, "Hey, I want you to make    
04:32:46: this longer." And then it said something like,  "Oh, I don't have enough context to make this    
04:32:49: longer." So I guess it just like generated its own  context based off of our conversation history. One    
04:32:53: thing I really like about this app is just how  fast it is. I mean, each of these routes are what    
04:32:58: are called preloaded or pre-filled. And so this  is me like really quickly going from one page to    
04:33:02: the other. And just notice how this whole page is  just like automatically done. Um, I also really    
04:33:06: like these brief little animations where you, you  know, start at the top and work your way down,    
04:33:10: loading each element slowly in succession. You  just get the, uh, visual appearance of very fast,    
04:33:15: very performant website. Okay, we have some  new superbase schema. So, I'm just going to    
04:33:19: jump over here and then what this is going to do  is go through and then add the rest of our users,    
04:33:25: tables, and stuff like that. So, back to SQL  editor, paste this in, run. Okay, the updated SQL    
04:33:31: script seems to have worked. So, I think we just  added one or two additional records here and then    
04:33:36: allowed it to add like the email and the password.  Heading back to Thumbly, if I go click sign up,    
04:33:42: we're running into Superbase URL is required.  So, they do have some runtime error. Now, I'm    
04:33:47: just going to paste all of this in. Okay, this new  signup page seems to work. We'll go nickniki.com.    
04:33:54: Then, Nickniki. Um, I'm going to click sign in.  Invalid login credentials. The reason why it's    
04:33:59: telling me this is because we obviously don't have  an account. So, I'm going to go back to sign up    
04:34:02: instead. I like that it keeps the email address  and the password. I don't have to redo it. Okay,    
04:34:07: we now have the secure checkout with the starter  plan with 100 thumbly credits. So, now what I    
04:34:11: can do Okay, because we're we clicked the starter  plan. So, I can go Oh, actually, did we click the    
04:34:17: starter plan? Hold on one sec. I don't necessarily  just want to buy the starter plan. I might want to    
04:34:22: buy pro. Let me try agency, actually. Okay, we'll  go nickniki.com. And do we have the account? Oh,    
04:34:30: you see because we exited out of the um payment  flow, it immediately jumped us into dashboard, but    
04:34:40: it selected the starter plan automatically. So, I  need to change that. Right now, it's automatically    
04:34:45: selecting the starter plan. You should allow the  user to select which plan they want on the payment    
04:34:50: page. It should also take into account which  button they click on the landing page because    
04:34:55: there are three different payment options there  as well. Just going to enter this in and then    
04:35:00: I'm going to proceed to check out just to see  what happens. When I click proceed to checkout,    
04:35:05: nothing occurs. And I think the reason why is  there might be some problem here. Additionally,    
04:35:11: when I click proceed to payment, nothing occurs.  Do we need to open up a Stripe checkout window or    
04:35:16: is the payment occurring locally on the platform?  Keep in mind, I'm using a Stripe sandbox, so we    
04:35:21: should be able to test the payment and have all  of the events and stuff like that run true. Hey,    
04:35:25: more pointedly, um, since I am now signed in, I  should be able to go to the dashboard even though    
04:35:28: I haven't done the payment. If I go to overview  and then click generate new and then actually go    
04:35:34: down to settings, can I upload my face? So, we go  supplied face. Okay. And I'm just going to refresh    
04:35:41: this. Am I still here? Okay. So, I'm not actually  keeping the reference faces in. And this could be    
04:35:46: because my account is not like set up yet because  the payment hasn't gone through. I'm not entirely    
04:35:50: sure. Let me just make sure everything else works  here. So, face that goes through. All right.    
04:35:54: If I click generate variance, what's going to  happen? Please provide an inspiration image and    
04:35:58: a prompt. So I have the inspiration image here.  The prompt is right over here. So we also have an    
04:36:04: erroneous error message where it says please  provide an inspiration image and a prompt. Hey,    
04:36:08: I provided an inspiration thumbnail and a  generation prompt. And I clicked generate    
04:36:12: variance, but I'm getting an error called please  provide an inspiration image and a prompt. I think    
04:36:16: this is occurring because I don't have a reference  face. However, that error is not representative of    
04:36:22: the real problem. If this are if this is the case,  I've also noticed that when I click upload face on    
04:36:27: reference face, then I click save configuration,  nothing happens. And then if I refresh,    
04:36:33: my reference face is gone. So make sure that  the save configuration button works. If it's    
04:36:38: not working because of some frontend error,  fix that. If it has to do with superbase,    
04:36:45: let me know if there's anything I need to do on my  end. And I'm just going to continue going through    
04:36:48: this and seeing if there are any other errors  that I could spot. Obviously, I'm going to sign    
04:36:52: out again because I'm on a local dev server. This  is all occurring in real time. So, any updates I    
04:36:56: make to this is going to be reflected. Um, but we  do need to make sure that if credits available are    
04:37:01: zero that we immediately jump back, right? So,  some other design decision. If a user has zero    
04:37:05: credits upon signin, we need to redirect them to a  payment page where they could select um, you know,    
04:37:10: how many credits to purchase and stuff like that.  That should occur every time a user is at zero.    
04:37:15: Now, if you're noticing, I'm not actually  just like doing waiting, checking the feature,    
04:37:21: and then proceeding to the next one. I'm now  at the point where I'm just dumping in a bunch    
04:37:24: of changes. And the reason why is because most of  these changes are relatively minor. Uh, you know,    
04:37:28: it's probably just some slight little database  misconfiguration or whatever. And so, I can    
04:37:31: actually proceed in this way. Um, have it working  on a change while I'm like modifying the rest    
04:37:36: of it. On the landing page under everything you  need to win the click, I don't like the shadows    
04:37:43: in general. I'd actually like you just to remove  shadows across the entire UX of the website. It    
04:37:47: they just seem a little bit off um given the fact  that most of the website does not have shadows and    
04:37:52: does not use them. Under the frequently asked  questions where it says how does thumbly insert    
04:37:56: my face? Can I use any images inspiration etc. The  title text is good. So how does Thumbly insert my    
04:38:04: face? Is written in like this nice black text,  but the subtext that says when you upload your    
04:38:09: reference photos in the dashboard settings, our  models learn your facial features. That's a little    
04:38:14: too dark. Can you lighten that just by 10% or so?  In this way, I'm sort of arbiting the time between    
04:38:19: the changes that are occurring here and then um  you know my testing. So, signing in, going back    
04:38:24: to the dashboard. Let's go to top up. Okay, cool.  And now we have the ability to select these three    
04:38:28: different plans, which is cool. Okay, so why don't  we pretend I'm doing pro. And then every time I    
04:38:32: click redirecting to Stripe, looks like there's  this problem which pops up. So, I'm actually going    
04:38:35: to copy this over then say every time I try making  a payment by clicking the proceed to checkout    
04:38:41: page, this error occurs. But I mean like you know  we could also parallelize this and do a bunch of    
04:38:45: them simultaneously. No real need. Um but yeah I  mean like you know we're getting closer for sure.    
04:38:50: One other change it just made is when I click on  starter you see it goes payment question mark plan    
04:38:54: equals starter. So I'm actually on starter but if  I go pro it actually opens up this page to pro.    
04:39:00: So these links do something now which is kind of  cool, right? I can actually click get started and    
04:39:04: then go to a specific payment page. I'm unsure  if this is because I'm logged in or logged out    
04:39:09: though. I'm going to click sign out. Then I'll  go back here and then see what happens. Okay,    
04:39:13: so login question mark plan equals pro. That  means it's actually going to keep and conserve    
04:39:18: this query parameter as I browse through the  rest of the website, which is pretty neat. Okay,    
04:39:21: now the redirection script has changed. It's  pretty clean. The way that this always works is    
04:39:25: you can just put in whatever um numbers you want  so long as your card details are 4242 repeating.    
04:39:30: So I'm just going to click pay. Please do not save  this card because it doesn't work or exist. And    
04:39:37: it looks like after the payment, we're being sent  back to the main page. So, I'm just going to say,    
04:39:41: "Hey, it looks like the Stripe Checkout payment  um went through, but then it redirected me to the    
04:39:47: slash payment route." Uh, if I go to dashboard, it  continuously pushes me back to that route despite    
04:39:54: the fact that I've already made the payment. So,  we just need to find a way to validate that the    
04:39:58: user's actually done the payment. That seems to  be the main block right now. Okay, it's telling    
04:40:02: me that it's finished this, which is cool with new  secure endpoints and session IDs and stuff like    
04:40:06: that. Okay, I'm just going to try a new account  here and see if maybe there's a problem with    
04:40:10: that. Maybe it just has to do with the fact that  I had an old account and it's redirecting me based    
04:40:15: off some old flag. Then I'll click processing  there. That payment looks good. No, it must be    
04:40:20: a more broad issue. So, check out Stripe here.  It looks like we are receiving the payments. So,    
04:40:26: that's going through. Um, for whatever reason,  we're not actually capable of connecting that back    
04:40:30: to a person. This is my fake card, nick@niki.com.  I've made tons of payments. Uh, I'm just going to    
04:40:36: relay this information over to my agent. If agents  have a hard time dealing with stuff like this,    
04:40:41: it's best just to give them as much context as  humanly possible so they don't get stuck on one    
04:40:44: loop over and over and over again. Okay, looks  like I've finally made it into the dashboard. So,    
04:40:49: we finally solved that persistent error um to do  with payments. As I'm sure you guys can imagine,    
04:40:53: you know, adding payments is like adding  another whole u problem that you have to solve,    
04:40:57: which is why I wanted to push it off as long as  possible. But, uh, now that we have I'm seeing    
04:41:01: that the credit monitoring is good, settings  look good. But I'm going to try uploading    
04:41:05: faces. See if we could um diagnose any issues  there. The saving configuration button looks    
04:41:11: like it works if I refresh this now. Okay.  No. So, it's telling Oh, okay. Cool, cool,    
04:41:17: cool. I got worried there for a second, but I  guess we had a bit of a lag. Um, that's okay.    
04:41:21: Okay. Going to take a peek at an example. Why  don't we just go to thumbnail generated? Oh,    
04:41:29: no. That's uh that's me from before. Let's do this  one here. And then um it doesn't look like we're    
04:41:36: saving the prompt variants. That's one change. I'm  also noticing this is significantly laggier than    
04:41:41: it was before. Uh make the main subject highly  cinematic. Replace the face with the face of    
04:41:52: the supplied face of the reference image. Use  dramatic cinematic lighting on the face. Okay,    
04:42:01: let me try saving this configuration. Just seeing  if maybe it's an error or if maybe I didn't fully    
04:42:06: understand what this is doing. If I refresh this  now, do we have that default prompt down below or    
04:42:13: does that need to be dealt with as well? And why  is it so laggy? It may just be my computer. I am    
04:42:18: editing a bunch of videos. So, okay, that doesn't  look like that filled in, which is unfortunate.    
04:42:23: Um, why don't we do supplied here? Generate new  variants. Okay. Make sure the generation prompt    
04:42:31: auto prefills with the default prompt in settings.  Right now it isn't. It should pull directly from    
04:42:38: the default prompt instructions. It's also  a little laggy. The app takes significantly    
04:42:44: longer to load now than it used to. Diagnose  whether this is because of some persistent error    
04:42:50: behind the scenes or some issue with prefilling  or something else. Okay, taking a peek at this.    
04:42:56: It did give me a very sexy beard. Let's be real.  Nick definitely can't grow that level of facial    
04:43:01: hair. But now like the internet will be able to  tell the difference. Cue that one up. Thank you    
04:43:06: very much. After the save, it's going to pop up  this little thumbnail saved. Um let's download the    
04:43:16: download the image and just see how that looks.  See if there are any problems there at all. Nope.    
04:43:20: That looks like definitely fake Universe Nick,  which is what we wanted. I'll go back to generate    
04:43:25: another. Now I can do more. Okay. And it looks  like this is taking some time to load. I mean,    
04:43:30: it's saying zero. Okay. Now it's saying 97. I  think I know the problem. I think in order to    
04:43:34: fix whatever payment BS that it had to do, it's  now fetching data from the database on every page    
04:43:40: load, which is adding a fair amount of latency and  then causing the app to lag a lot more. So, it's    
04:43:45: obviously not what we want, but it's what's going  on. That's why every time I load settings, it    
04:43:49: takes a second before this comes in. Ideally, what  you want to happen in a full stack app like this,    
04:43:54: at least a modern full stack app, is when you sign  in, you want it to automatically cache and then    
04:43:58: like like pull all the data and then cache it.  Um, and then that way everything is pre-filled,    
04:44:03: all the images are prefilled, the credit amounts  prefilled, so on and so forth. And then instead,    
04:44:06: what you want is you basically only ever want that  to change if you materially change the database.    
04:44:11: So when you change a database, then it says,  hey, you know, you should probably grab the new    
04:44:15: data as well, just uh just to be 100% sure. And in  Nex, they manage this through a variety of means,    
04:44:20: but a big one is like mutating the database um  or or setting like mutations or or whatever as    
04:44:25: opposed to always fetching totally new data. So,  I think that's what's going on. I'm just going    
04:44:29: to instruct the agent, see if we could fix that,  and then assuming that there's no other changes,    
04:44:33: I'm just going to push this puppy live. Okay,  looks like it's loading significantly faster now,    
04:44:37: which is nice. We can jump around from settings  to generate to overview, and we don't have that    
04:44:41: like really persistent lag like we had before.  Um, we also have the ability to, you know,    
04:44:45: delete if we wanted to. I think what I'm going  to do is I'm just going to open this in, well,    
04:44:50: not an incognito window. I guess I'll just open  it in a new tab. And then what I want to do,    
04:44:54: whoa, I don't know what the hell just happened  here. No, thank you. Let's not do that. Thank    
04:44:58: you. Thank you. Um, I think what I'm going to do  is I'm just going to try the mobile features now    
04:45:03: on the dashboard because mobile optimization is  pretty big, right? Just want to make sure this is    
04:45:08: going to work. And it looks like it is. We have um  we have a little nav bar down at the bottom now,    
04:45:13: which is kind of cool. And we can jump back and  forth between these three. So, that's nice. I am    
04:45:18: a fan. Thank you. And now, let's just exit out  of the dashboard, go back to the landing page,    
04:45:23: and just see what we're looking at. So, looks  like that mobile optimization prompt worked in    
04:45:27: so far that, you know, the um little section here  is mobile optimized. And then all this stuff's    
04:45:34: mobile optimized. I'm just going to pretend sign  in now. Okay. Okay. And then yeah, we immediately    
04:45:39: jump to dashboard where we have functionality.  Let me just try deleting this. Yeah, I want to    
04:45:43: delete it. And then if I just refresh this puppy,  is it gone? No, it's not gone. So that's the final    
04:45:50: change we need to make. And then uh yeah, I'm  pushing this puppy live. In addition, I've also    
04:45:55: set this up. So it's now at thumbly-g.netfi.app.  I just said, "Hey, put this puppy on GitHub and    
04:46:00: Netlefi. Let's do this thing." And uh yeah, this  is actually working really, really good. So,    
04:46:05: I'm just going to go over to sign up here and I'm  going to go nicholas@gmail.com. Would be a hell of    
04:46:10: a name if I could pull that up, though. And then  we'll go proceed to checkout and I'm just going to    
04:46:15: enter some info. Apparently, my card holder name  is 234234. Take that, Nicholas. This has jumped    
04:46:21: us directly over to dashboard and now I have the  ability to do everything. So, I'm going to upload    
04:46:26: some face. Uh, what was it again? Was it supplied?  Yes, it was. Keep the identical to the inspiration    
04:46:32: image. Replace the face. to face the reference  image. Use dramatic cinematic lighting on the    
04:46:35: face. Cool. I'm just going to save this. Says  that it saves successfully. Oh, hold on a second.    
04:46:40: That's not my face. That's my face. Good god,  Nick. You know, you've been developing an app for    
04:46:47: a long time when you start making trivial errors  like that, huh? Okay, now I'm going to generate    
04:46:53: three variants. Um, we're going to see how  long this takes. So, counting down. 1 2 3 4 22.    
04:47:01: Okay, so right at 22, we had an unexpected error  occurred. So I imagine this probably actually went    
04:47:06: all the way through. There was just some problem  with updating the DB. Uh this occurs as mentioned    
04:47:11: when you go from local to some sort of like  cloud setup or or you know actually like hosting    
04:47:16: it live. So I'm going to go through and just give  this an unexpected error occurred. Do a little bit    
04:47:21: more final debugging and see what we need to do  to make this puppy. I would imagine the issue is    
04:47:26: probably related to the fact that um when we were  running this locally, we didn't have a timeout,    
04:47:31: but services that like manage the calls  for you, like uh Netlefi, for instance,    
04:47:38: typically have timeouts of like 15 seconds or so,  maybe 20 seconds. So, I think we probably just    
04:47:43: ran into that. Okay, just ran out of usage again  after developing this for a good hour or so. So,    
04:47:47: I've moved over to Claude Code. Uh I'm still going  to try pushing and generating the variants here.    
04:47:52: We're going to see how that goes. 22 Mississippi,  23 Mississippi, 24 Mississippi, 25 Mississippi, 26    
04:47:59: Mississippi. Okay, so right at 26 seconds is when  we got the result. Um, I imagine that's probably    
04:48:04: why this one's kind of weird. I think that's the  first one that's like actually objectively failed.    
04:48:09: Uh, but yeah, no, I like this one. So, why don't  we just keep selected thumbnail? Awesome. Looks    
04:48:13: clean as per usual. And uh, yeah, I mean like  we'll just click generate another and we can just    
04:48:17: keep on going as many times as need be. But that's  it. We just launched our app and it works. And    
04:48:25: there's one final thing we need to do, which is  that god darn security audit. Almost forgot. So,    
04:48:29: let's do that. Okay, pasting this directly into  cloud code. As we can see here, now reading all    
04:48:34: the client pages and doing the config. And let's  see how we do. And it's just building to verify    
04:48:39: that everything compiles now. And then I'm going  to do a final check just make sure that, you know,    
04:48:44: the app functionality works the way I want it to.  You'll quickly realize that the vast majority of    
04:48:48: time that you spend on this is not actually the  building. It is just the giving of vibes plus the    
04:48:56: verifying it works to the way your vibes require  it working. So I made a bunch of these changes. Um    
04:49:03: okay, there's some rate limiting off middleware.  Okay, so I'm just going to say implement the    
04:49:10: middleware with check stripe web hook secret etc.  So I'll probably have to go and grab some stripe    
04:49:20: stuff, but I'm just going to go and verify that  this actually works now. Awesome. We still have    
04:49:23: the ability to do everything that we had before,  which is nice. Okay, I'm taking a look at this    
04:49:29: is so interesting. Like if you really zoom into  one of these things, you see every little pixel    
04:49:33: that this constructed. It's wild. Um anyway, I  mean like that dead inside completely. But yeah,    
04:49:40: uh we're now going to run a with check migration  on the database. So that's going to be cool. And    
04:49:45: then we'll also add some web hook secrets. So I'm  going to head over there and then just verify that    
04:49:49: um I got all this. Okay. Well, that one took a  little bit longer than I wanted it to because    
04:49:53: we did have a bunch of back and forth with  the payments on Stripe, but suffice to say,    
04:49:57: still good to go. Uh this is a good example now of  everything. It's not only, you know, kind of CRUD    
04:50:02: create, read, update, delete, like a traditional  app. Doesn't just do stuff that you ask it to. We    
04:50:07: also, um, are wrapping around a pretty popular  and powerful API, the Nano Banana API. And then    
04:50:13: we're applying some prompts and then some sort of  creative applications here to generate really cool    
04:50:18: outputs. Uh, and then we're wrapping it all in a  really nice UX and connecting it to payments. So,    
04:50:22: at this point, like you guys basically have  everything that you need in order to just build    
04:50:25: whatever full stack app you want. Uh, I think  what I'm going to do next is just do one final app    
04:50:29: combining everything that we talked about. Maybe  make the UX a little bit more complicated. So,    
04:50:33: instead of just having three or four, you know,  two or three things on the left hand side, we have    
04:50:36: like what might uh be considered more of like, you  know, like a really successful enterprise app. And    
04:50:42: then I'm just going to run through the motions  that I've already showed you guys multiple times    
04:50:45: at this point before talking a little bit about  the economics of vibe coding and then wrapping up.    
04:50:50: Man, I am so excited for this app because as  somebody that produces a tremendous amount of    
04:50:54: content nowadays, having an app that can basically  allow you to focus on one uh place, let's say    
04:50:59: YouTube or maybe your blog or something and then  have that same content, the same concepts and    
04:51:05: ideas immediately distributed to a bunch of other  platforms is fantastic. My issue with the way that    
04:51:10: most people do this is they just do it in a really  poor way. And so, you know, the end uh output    
04:51:15: quality of, let's say, a blog post converted to  like Xthread snippets or whatever ends up being    
04:51:20: so bad that, you know, the AI slop um overruns it  and then the quality is really poor. So, my idea    
04:51:25: today is I want to make an app that's so dang good  that, you know, you don't get that. And it's still    
04:51:30: written in your tone of voice. It's written really  succinctly. It's written really intelligently.    
04:51:34: And I was trying to come up with like a good  name for this app just before, you know, like    
04:51:38: clearly if you guys have paid attention so far,  the names so far have been afterthoughts, right?    
04:51:42: But um this time I think I already got one. It's  going to be called splinter. And the idea is okay,    
04:51:48: you're going to put in one piece of content which  why don't we just call this like pillar content.    
04:51:55: This is going to be like the pillar upon which  everything else rests. And maybe it'll just be I    
04:51:59: don't know like a blog post or something or maybe  like a video URL, right? And then what I want is    
04:52:04: I want this to be able to create content for a  platform like X. I wanted to be able to create    
04:52:09: content for a platform like LinkedIn. I wanted to  create content for Instagram. I wanted to create,    
04:52:16: I don't know, scripts, maybe like long form  scripts. And then I also want short form scripts,    
04:52:23: right? So we could do stuff. And then like  eventually, and I'm not going to get to this now,    
04:52:27: I don't think, cuz it's kind of a big ask, but um  we should also be able to create like video like    
04:52:32: full stack end video. Um that would be my that  would be my end goal. So, this is basically what    
04:52:38: I want the app to do. I want you to be able to  provide one piece of content and then immediately    
04:52:42: just like, you know, creates high-quality content  that's specific to each platform. And obviously,    
04:52:47: we're going to need to do this through some  sort of dashboard. In addition, okay, I don't    
04:52:51: just want this to be basic where we had like our  little dashboard on the left hand side with like,    
04:52:55: you know, three things and then we have some other  like central section um over here. I want this to    
04:53:00: be more interactive and I want this to have some  sort of like really detailed onboarding as well.    
04:53:05: Um, this is naturally going to involve like a  fair amount if you think about it. Not only are we    
04:53:10: going to have to do everything we did in the last  app, which was to uh summarize a landing page,    
04:53:15: Stripe payment integrations, um, OD DB, some sort  of API wrapping, and then like a good way to,    
04:53:21: you know, present that to the user. We're going  to have to go further because it's now not just    
04:53:24: one like API that we're wrapping around, but  it's realistically going to be multiple. And    
04:53:28: then we're also going to use our own custom logic  sort of um on-site logic to well not on-site sorry    
04:53:34: but like our own proprietary stuff to do things  like manage the tone of voice the prompts and so    
04:53:39: on and so forth. And perhaps one of the coolest  parts of this is I think the last app used AI as    
04:53:43: just like an like an afterthought to help generate  you know a list of filters in this AI is going to    
04:53:48: be like the main deal and uh hopefully we all  know like AI is the big thing right now. So,    
04:53:53: it allows us to sell both uh AI and our value  props, but also AI through the apps. And my my    
04:53:58: goal when building apps is I just want to  build stuff that like I actually would use    
04:54:01: uh if I wouldn't actually use it as somebody in  a space. Odds are I probably don't understand the    
04:54:06: problem enough to even be building this app in  the first place. But yeah, you know, if I could    
04:54:09: save myself a bunch of time with this, that's  going to be a solid win. And then if I could    
04:54:12: save other people time of that and stuff like  this as well, then that'd be even better. Okay,    
04:54:16: so the very first thing I'm going to do is I keep  turning back to this 16 or 17-year-old kid. No,    
04:54:21: he's 16 years old. His name's Leon. And what he's  been doing recently is he's been building like    
04:54:24: really cracked high-quality landing page designs  for Gemini. And so he comes up with these very    
04:54:29: very in-depth prompts. And then he ends up with  like a literal interactive app that you can like    
04:54:33: move your your fingers around. Unfortunately, you  didn't take a video of this, but this is like,    
04:54:37: you know, an app that there's like little strings  that are basically here being um processed every    
04:54:42: second through I don't know if it's like web web  GUI or something like that, but it's some sort of    
04:54:46: 3D library. And um he shares his prompts online.  He's really cool. I used him in my last video.    
04:54:50: I wish I had half that uh brain at 16 years old.  And so what I'm doing just to start us off is I'm    
04:54:55: going to copy this prompt that he's put together.  Okay? And then I'm just going to ask Gemini to    
04:54:59: make me a landing page. And I just want it to  make me a landing page first before I do the rest    
04:55:03: of the app because I just don't trust that it'll  be able to do both the very in-depth programming    
04:55:07: required to build some sort of cool 3D generative  thing and then also do the app. So basically what    
04:55:12: I'm going to do is I'm going to have it like  generate the the landing page and then we'll    
04:55:14: build the rest of the app out afterwards. Um, so  you know, kind of non-traditional, but basically    
04:55:19: what I've done here is I've just pasted all this  stuff in. Okay, I'm going to press enter. And I'm    
04:55:23: not going to read this whole prompt to you, but  this is basically, you know, act as an elite,    
04:55:27: award-winning creative developer and digital  generative artist. Your task to write a single    
04:55:30: self-contained executable file that renders an  ultradetailed pixel perfect and breathtaking hero    
04:55:34: section for a next generation tech company.  Critical constraints, do all this fun stuff.    
04:55:38: Here's the theme and the content. You know,  provide some information about what I want and    
04:55:42: stuff. And stylistically once we have this set up  um you know I'll make some minor modifications to    
04:55:46: it so it's not a one to one clone or rip of this  uh and then we can actually move on with the app.    
04:55:52: Now while I'm doing that just to save on time I'm  going to voice dump everything that I think this    
04:55:57: app is going to include. Um and then I'm going to  send it over to claude code so that I can have two    
04:56:01: of these instances operating simultaneously.  One that's probably a little bit better at    
04:56:05: architecture design than the other that you know  is better at the front-end design that I'm asking    
04:56:08: for. So, uh, I'm not going to repeat it all over  to you guys, but a I want to design an application    
04:56:15: that takes a single piece of pillar content and  then immediately rewrites it, regenerates it,    
04:56:20: and recreates it, and then syndicates it across a  variety of platforms. Okay? And I just gave that    
04:56:24: over to Claude Code, and I asked it for a spec,  which is basically a highlevel description or    
04:56:29: overview of what this app would look like. And I  just want to run you guys through this here while    
04:56:33: Gemini is designing the actual generative part.  So this includes tech stack um app architecture    
04:56:39: some info on the database schema some info  about the landing page and marketing site.    
04:56:42: So after we're done with this, we'll use this  to modify it. Pricing and Stripe integration,    
04:56:46: authentication and signup flow, onboarding  flow, the actual content syndication engine,    
04:56:51: uh info about the dashboard, the content library,  AI configuration and voice model, scheduling and    
04:56:56: calendar, analytics and reporting, settings and  account management, API and webbook architecture,    
04:56:59: and then also some direct platform publishing  and then AI video generation stuff in the future,    
04:57:04: which basically we're just going to like add stubs  or little nuggets that we could use to build that    
04:57:08: out later if necessary. I've then given it some  information on the text stack and then asked it to    
04:57:13: come up with some other things. So for instance,  we're going to use Next.js15. We'll use Tailwind    
04:57:17: CSS plus the Shad CN/ UI component library. We'll  have Superbase Realtime for live updates. We'll    
04:57:23: we'll do a bunch of other stuff as well. ZOD  validation. This is important for security cuz    
04:57:27: I asked it to make sure that it was as secure as  possible on the first shot. What I'm going to do    
04:57:30: is I'm just going to modify a couple of the pages  here. I'm probably not going to use a calendar.    
04:57:34: Okay. Analytics look good. Um platform connections  for now. I'm just going to leave those out.    
04:57:38: Um, AI voice prompt configuration is good. So,  I like this. This is like your tone of voice.    
04:57:44: Just make sure that gets that in right. And then  settings, account, billing, and team. All that    
04:57:47: stuff looks good. Here's like the data objects.  I don't want to spend too much time on that,    
04:57:51: so I'm not going to worry about it. Um, that  looks solid. On the right hand side, it looks like    
04:57:55: this generative component has now been done. So,  that's pretty sexy. Now, it's going to go design    
04:58:00: the rest of the website. While we're looking  here on the lefth hand side from cloud codes,    
04:58:04: uh we have a bunch of different feature sections.  The landing page pricing and stripe integration    
04:58:08: is going to start at 19 a month or 190 a year. So  it's going to be 10 months basically giving two    
04:58:12: free months to people. Of note, just before we do  this, the input method is really clean. Um I asked    
04:58:16: it to be able to either paste raw content. So just  copy and paste a blog post, article, a transcript,    
04:58:21: or a series of notes, or paste a URL. And the  whole idea is, you know, if we paste a URL,    
04:58:26: um it's going to go through and then scrape the  whole website for us. So we didn't even have to    
04:58:30: touch any of that. Um, additionally, I want to  be able to do things like paste a YouTube video,    
04:58:33: although I think right now I'm probably going  to leave that out just uh as the demo. And then    
04:58:37: once I have those core functions and features  in, then I'm going to do more. But you should    
04:58:41: also be able to upload things like MP3s, waves,  M4As, OGs. Um, all these things should be auto    
04:58:46: transcribed. And the idea is it's just going to  be like your one-stop shop portal for like, hey,    
04:58:50: I just produced a piece of content. I'm going to  plug this in and then I'm going to have copy and    
04:58:53: pasteable ready content to distribute to all these  different platforms with minor adjustments. And    
04:58:57: obviously, I'll also be able to like change the  prompt anytime I want. Um, so very valuable for    
04:59:01: me. Hopefully it'll be as valuable uh for other  people as well. Okay, very satisfied with the    
04:59:06: first iteration of this landing page. As you see  here, there are some issues with this WebGL stuff,    
04:59:10: but these are real particles that are being  rendered um in real time. Um I don't like how this    
04:59:14: neurallex stuff is all over the place. Obviously,  that's that's okay. I've since told it to slow    
04:59:18: things down a little bit, but yeah, I mean like  the text on the left hand side of the page looks    
04:59:22: really really clean. Obviously, we have like nice  little mouseover buttons and and stuff like that.    
04:59:26: Um, I'm going to change all of this signap  stuff to uh Splinter, but for now, I mean,    
04:59:30: Gemini uh 3.1 and you know, prompts from Mr. Leon  Lynn over here are absolutely crushing it. So,    
04:59:36: pretty stoked and looking forward where and  looking forward to where the next uh step    
04:59:40: goes. After the next round of edits, we've also  added some additional sections. Common questions,    
04:59:44: ready to syndicate, and then finally down here,  um, a full- length footer. So, that's looking    
04:59:48: pretty sexy. The lines here are still moving  around a fair amount. So, I'm just going to modify    
04:59:51: them a little bit more. But, we've now implemented  some sort of like mouse um interactivity. Do you    
04:59:56: see how this thing is kind of like moving away  from my mouse as I move around the screen? So,    
05:00:00: I can technically control this. It's just  it's not super uh what's the term? Trivial    
05:00:04: or obvious to me as a user of the app how this  works. I've also had it change these lines. So,    
05:00:09: that's going to slow down pretty significantly.  And then we can see what the final product looks    
05:00:12: like. While I was waiting, I also had it go do  a little bit of research on other platforms. So,    
05:00:17: Repurpose.io lately, Constant Studio, Buffer,  and so on and so forth. And then why Splinter    
05:00:22: will solve it. So most are distribution only or  creation only. Splinter will do both. Basically,    
05:00:27: it'll allow you to both create content and then  distribute it quickly. Um voice and tone being    
05:00:32: an afterthought here. We're going to fix that  via um some pretty strong prompt engineering. I    
05:00:36: think most people that are designing these sorts  of repurposing apps are more software engineers    
05:00:39: than they are prompt engineers. I would consider  myself much more prompt engineer than a software    
05:00:43: engineer. So that should allow us to get like  very high quality tone. Okay, these particles    
05:00:47: are looking a lot better. They now move according  to my mouse, which is cool. And then these little    
05:00:52: um things are no longer facing the opposite  direction. I'd say they're probably a little    
05:00:56: too many of them. So, I think I'm going to remove  the entanglement ratio here just so we have three.    
05:01:00: And then I'll probably also just adjust the color  of the particles a bit. So, you know, it's I don't    
05:01:05: know, like kind of lightish yellow, maybe goldish,  something like that. Also see if maybe I can make    
05:01:10: the particles just a little bit bigger. Right  now, I feel like they're kind of compressed,    
05:01:13: which I'm not a fan of. still is kind of neat just  seeing this little streaming animation. Pretty    
05:01:17: interesting seeing the logic and kind of the math  that uh ended up aggregating all these things    
05:01:23: together. I mean, I'm just moving my mouse around  and there's clearly a deep relationship here,    
05:01:27: but I can't exactly figure it out. I think that's  because they're modeling this in 3D instead of 2D.    
05:01:32: Becomes a lot simpler when you see them in black  like this. There's definitely some 3D going on    
05:01:37: here as we could see. And honestly, I think I like  the black. Um I like the 3D translation. So, I'm    
05:01:42: just going to keep it at that. All right, awesome.  So, now that we're done with this, um, now I'm    
05:01:46: just going to modify the content on this page. And  I'm just going to do it by giving Gemini the rest    
05:01:50: of the instructions and saying go for it. Um, you  know, we're going to want to clean out some of the    
05:01:54: contacts and stuff. Uh, but I'll show you guys  what that looks like. So, I'm going to say to    
05:01:58: adjust the copy on the page to match the purpose  of the app, which you can find in this side of    
05:02:01: this spec. I'm not actually going to like manually  do any of this. And then it'll go through and then    
05:02:06: just adjust the rest of it. And yeah, I didn't  actually realize, but this is this is definitely    
05:02:10: like a portal that we are moving through in 3D  space. So, it's actually more complex than I    
05:02:15: thought it was. Looks clean to me. We now have  everything here set up. All of the syndication    
05:02:21: text is in now. Um, it's still saying synapse,  which is kind of annoying. I don't think it got to    
05:02:25: that. Cool. Good to go. So, let's build the rest  of the app now. Um, for us, it's going to be as    
05:02:29: simple as just sending all of this information  over to Gemini and saying, "Excellent work.    
05:02:35: I'd now like you to build the rest of the app  as detailed in splinter_spec.md. But there's one    
05:02:43: change. I'm going to say along the way document  each update in an updates.md file so that we have    
05:02:50: a history of tracked changes in case something  occurs or I need to feed this into another version    
05:02:59: of the model of Gemini. And the reason I'm doing  this is because this is a pretty crazy long app,    
05:03:06: right? There's a fair amount that's going on here.  Um, I anticipate I'm probably going to run out of    
05:03:09: tokens at some point because I ran out of tokens  about an hour and a half into the development of    
05:03:13: most apps so far. What I want is I basically just  want like a list of everything that it has done    
05:03:18: up until the time that it did not do the thing.  Um, and I'm just going to store it in a file that    
05:03:22: I can then give to either another version of  Gemini later on or clawed Opus 4.6 or whatever    
05:03:27: the freaking model I want. And in this way, this  is almost like a GitHub um repo before I get all    
05:03:32: the pushing logic and stuff in. But it gets to  take advantage of AI summarization features. So    
05:03:36: I'm not going to have to load the codebase every  single time. I want to like analyze and you know    
05:03:39: see what the problem is. This section cracked me  up a ton because I don't know if you guys have    
05:03:44: uh seen the draw the rest of the owl meme, but  basically it's like how to draw an owl. Draw some    
05:03:51: circles. Draw the rest of the freaking owl. Um  I feel like we've just done this so far and it's    
05:03:57: doing that. So, thank goodness for AI, huh? This  initial implementation plan is going to be heavily    
05:04:02: modified since we're no longer just building  a one kind of uh file uh website. Instead,    
05:04:08: we're going to be distributing some of the stuff  across big file structure. Here you can see that    
05:04:12: it's also set at the updates.m MD, which is quite  nice. So, we're going to see technical decisions,    
05:04:16: feature implementations, and significant changes  applied to the Splinter project. And my hope is by    
05:04:20: doing it this way and then later on feeding this  to um you know claude I can have both of these    
05:04:25: models both claude code uh sorry claude opus 4.6  and then gemini 3.1 pro high basically like debate    
05:04:31: about which features are better which things  to keep and then which things to remove. Agent    
05:04:35: teams in cloud code does a variation of this right  now where basically they have like a shared chat    
05:04:40: file and then they chat back and forth. Um, this  updates to me is just a slightly more streamlined    
05:04:44: version of doing that without me having to  waste $400 in tokens cuz boy does that agent    
05:04:48: teams feature consume a lot of them. All right,  so it's built the MVP implementation plan. Just    
05:04:53: taking a quick peek through this. This is going  to need everything here, which is fine. Hopefully,    
05:04:58: we are very used to getting all those API keys  now. And yeah, we're going to initialize Nex.js    
05:05:03: directly inside of this root directory. So,  it's going to do all of these steps here. Oh,    
05:05:07: hold on. I see that it's not actually taking that  into account. I'll say initialize in the same um    
05:05:15: folder as root hero.html will be our landing page.  Just want to make sure that's super clear. And in    
05:05:22: this way I get to pause the outputs. I'm not going  to waste a bunch of usage on you know building it    
05:05:27: out and so on and so forth. That's where taking  a peek especially initially at what um Gemini is    
05:05:33: doing can be pretty valuable. I always liken this  to sort of like a trajectory sort of thing. Let's    
05:05:39: say over here is um I don't know South America,  okay, on the left hand side and then over here    
05:05:45: is the westmost coast of Africa and hypothetically  you are a boat trying to make it from one side to    
05:05:51: the other. And so this is you, right? And then  your goal is you want to go over here. Well,    
05:05:55: logically speaking as you are leaving the port on  the eastmost side of South America. Okay. Um there    
05:06:01: are a lot of different directions you could go.  You go this way, you go that way, you go this way.    
05:06:06: only a very small subset of these directions will  actually get you to your goal. Obviously, you're    
05:06:10: going to need to go like here, right? And even  then, I'm a little bit off. And so, initially,    
05:06:15: I guess what I'm trying to say is the direction  that you pick even in like the first kilometer    
05:06:20: as a boat heading to to to sail is really really  important for determining the final placement of    
05:06:25: the app. Um, even if I was like one tiny little  degree off, that could be the difference between    
05:06:30: me making it directly on target and then I don't  know like a one degree difference or something    
05:06:34: could be the difference between me making it to  city that's like 100 km away. And so I usually    
05:06:41: like to be around here to steer the model and  then once it's sort of like in this territory    
05:06:46: or whatever, you know, if it's like on track well  enough that I think it's like going to be okay,    
05:06:50: then I don't really worry too much about that. Now  on the right hand side here you see that the error    
05:06:54: um the agent actually ran into an error. This is  another reason why I like being around. This can    
05:06:58: occur for a number of reasons. This could occur  for token issues. It could occur because I don't    
05:07:03: know like the API is just out. It could occur for  rate limiting reasons or just because sometimes    
05:07:08: um some of these packages don't actually interact  nicely with Gemini and then it kind of struggles    
05:07:11: with the terminal. But yeah, I'm just going  to be around for the first couple minutes for    
05:07:14: a build that this is this comprehensive because  I don't want it to like make a wrong assumption    
05:07:18: and then build something completely different to  what I want and then later on I'm just going to    
05:07:22: have to go back and and redo it all anyway. Okay,  you got the app right over here. So, it's looking    
05:07:26: pretty sexy. If I click get started, we now can  sign in or sign up. So, I'm just going to pretend    
05:07:32: that I've done all of that. Now, we have the  onboarding. So, initialize workspace. Cool. So,    
05:07:40: this is like all the platforms that I'd want to  connect to. It's good. This is really interesting.    
05:07:45: Formality index, humor coefficient. I like that,  but I think we're going to have to add some to it.    
05:07:50: So, I'm just going to go back to the model and  then I'll say change voice profile to a default    
05:07:58: um to an advanced advanced setting advanced let's  say button where I can modify the prompt directly.    
05:08:09: That looks pretty cool. Dry run simulation.  Hey, what's going on? Execute run. This is    
05:08:17: going to be like when it actually does its  thing. Cool. Also add a um an additional    
05:08:26: step right after the dry run that shows the  output. I'll wire you up to Claude Opus 4.6.  
05:08:41: So we can test this next. Okay, we're now going  to enter the dashboard. Okay, so this looks like    
05:08:46: a pretty simple dashboard still. I do like  the style we have. We're going to build out,    
05:08:51: you know, a generative interface. It says  over here. I'm probably going to want to    
05:08:54: move this stuff a little bit over to the left.  I'm not seeing anything under generative engine,    
05:08:58: voice profiles, platforms, or settings. So I  guess right now we have the onboarding all the    
05:09:02: way up to the dashboard. So that's pretty cool.  Still, if I click log out, I go back here. Then    
05:09:06: if I go back here then uh Okay, cool. So yeah, I  think I'm understanding where we're at with this.    
05:09:11: Uh it's looking pretty clean and I'm glad that I  managed to do all that stuff with just a little    
05:09:15: bit of prompting. We still have that cool little  3D thing, too, which is really nice. Okay, so next    
05:09:20: up, I'm going to feed in these instructions and  then I think what I'm going to do is I'm going    
05:09:24: to have it continue the initialization.  Um this is going to be tough. I mean,    
05:09:30: I really like this. I really, really like this,  right? But this is going to be pretty tough. Uh,    
05:09:36: I guess we could probably autogenerate a  prompt that includes some settings with this  
05:09:42: for the sliders. We'll use this in a prompt  to fill variables like formality and humor.  
05:09:56: And then this dry run simulation. We'll  execute the input. We should get a new    
05:10:01: one here. Systems nominals.  Cool. Awesome. Okay, cool.    
05:10:05: Let's also start building out the dashboard.  I'd like you to replicate the attached image    
05:10:15: in terms of content. Now, I'm going to go to  dribble over here. I'm going to go dashboard  
05:10:24: and let's see what we can do here. I want  something that's just like much higherend,    
05:10:28: cleaner. I do like the squareer look. Um, to me  that just implies like a high-end brand. So, I'm    
05:10:33: going to look for something that does have that  square look. Let's try filtering by new instead of    
05:10:38: um popular. That way, maybe we can get things  that other people haven't built before. Okay,    
05:10:44: this looks pretty clean. I like this.  Let's see if we could feed this in. Oh,    
05:10:48: sorry. We need to copy this.  We can't just do that. Okay.    
05:10:52: uh in terms of content and style except I  want you to stick to our pre-established  
05:11:02: um square no border radius. That's the little  um smooth corners. I don't really like that.    
05:11:11: I also want you to add significantly more  functionality as per the initial doc initial    
05:11:19: splinter spec.md. And this is looking pretty  clean. There's an advanced settings feature    
05:11:26: here now where we can actually change things which  is quite nice. I'll pretend I'm executing a run    
05:11:32: running style transfer. Okay, great. Awesome. So,  this looks kind of silly. Not a fan of the design    
05:11:39: for sure, but um you know, it's cool that it has  a lot of the stuff laid out. Interesting. Yeah,    
05:11:45: this is like highly opinionated stuff clearly. Um  all right, so I think what we're probably going to    
05:11:49: want to do is on the left hand side, we're still  going to want to have like a like a database,    
05:11:57: sorry, database dashboard panel. Um we're not  going to want to mention the model. I do like    
05:12:02: the system log. That part's cool. All right, cool.  Let me just give this some stream of consciousness    
05:12:06: feedback. Hey, this looks cool, but it's quite  opinionated. I don't like the dark borders. I'd    
05:12:11: like a higherend sort of Lux design internally  that still sticks to um very similar to the design    
05:12:18: on the landing page. I'd like you to remove all  mentions of the specific models that we're using.    
05:12:23: I want some sort of lefth hand side pane that I  could use to select different views. I really,    
05:12:28: really like the system log. I like the  credit usage, the generation, source items,    
05:12:34: active platforms. These are fine. replace recent  archives with a graph. That graph should go really    
05:12:39: in-depth on the number of generations and which  platforms we've connected and stuff like that.    
05:12:43: We also need the rest of the app. So, I need a way  to see specific and individual generations. I also    
05:12:50: need a way to create a new syndication. Right now,  when I create when I click create new syndication,    
05:12:54: it takes me back to the wizard. But I want this  to take me to a page where I can insert content    
05:13:00: either using URL or MP3 file upload or video  upload or paste in a bunch of text and then it'll    
05:13:09: do the syndication for me. Remember, we're just  dry running all this stuff for now. Uh I'm going    
05:13:13: to include some API credentials for anthropic in  a second. So you could hook up the cloud opus 4.6    
05:13:19: six integration and change the rest of the  language on the actual app side to reflect    
05:13:24: like normal app usage. For instance, I don't like  the term disconnect. I don't like the matrix. Um    
05:13:30: I don't like, you know, some of the other  language that you're using here. It seems a    
05:13:34: little too tryhardy. Okay, after about 40 minutes  of development, we did run out of tokens. But    
05:13:38: never fear, that's one of the reasons why we're  using two models and not just one. So what I've    
05:13:43: done is I've exported our conversation history  and then that updates file. And now I'm just    
05:13:47: uh doing next steps which in my case involves  feeding in the enthropic API key. So I'm going to    
05:13:51: go and find the anthropic API key here. I'm going  to call this uh for splinter. Then I'm going to    
05:13:59: copy it over right there. Okay. And then what I'm  going to do is I'll say let's wire up Claude Opus    
05:14:08: 4.6. Test a bunch of prompts. Give me a few uh a  few dry run examples. And then I'll pick the ones    
05:14:17: I like the most. Let's say test 10 prompts.  Give me a few dryr run examples of befores,    
05:14:24: afters, and I'll pick the ones I like most  and we can integrate them. In general,    
05:14:28: the design quality of Opus 4.6 will be a little  bit lower. So, just keep that in mind. However,    
05:14:33: um there are some other trade-offs. You know,  it's a little bit faster and then addition to    
05:14:36: being faster, I think architecturally, it tends  to make like a better functioning application. So,    
05:14:40: that's why I frontloaded the design with Gemini.  And then after the design and stuff like that was    
05:14:45: all wired up, I did all like the little scripting  or I'm doing all of the little scripting and    
05:14:48: backend passes with um you know cloud opus 4.6.  This database is now set up. So I can head over    
05:14:56: to let's do two things. Under authentication I  just want to go to sign in signin providers and    
05:15:02: then I'll remove that little confirm email step  and then under project settings I'm going to go    
05:15:06: to API keys just so that this has all of the keys  that it needs in order to you know do whatever it    
05:15:11: wants. So I already gave it the publishable key.  We'll go um superbase secret API key and then I'll    
05:15:18: paste that in as well. And the idea is now it has  everything that it needs in order to manage the    
05:15:22: Superbase instance for me. I don't really need to  be involved in this process at all. And I'm doing    
05:15:26: this while Claude is basically just running  a quick little test on the prompts. I'm just    
05:15:30: going to pick the best prompt for now and then  I'll worry about like optimizing the hell out of    
05:15:33: it later. Okay. And whereas anti-gravity was using  its own built-in browser, uh Claude Code typically    
05:15:38: uses Chrome DevTools. So that's what it's doing  right now. jumping on taking a screenshot and then    
05:15:42: it's seeing an internal server error. So whatever  it did either didn't compile or there was just    
05:15:46: some problem on the back end. Um so that's what  it's fixing up now. As you can see the syndication    
05:15:51: page here for create is much lower quality. Um  and as mentioned you know cloud is just nowhere    
05:15:56: near as good as Gemini at least as of the time of  this recording and designing those really high-end    
05:16:00: uh looks unless it's like per perfectly basically  trying to duplicate functionality which is    
05:16:05: unfortunate. Um, it is going to make some minor  changes here because it it can't actually click    
05:16:09: this generate button. So, it's cool that it  can kind of run that testing loop on its own,    
05:16:13: but all of this is just in contrast with Gemini's  high quality design. And it looks like it created    
05:16:18: a LinkedIn post and then also an X and Twitter  post. Just taking a peek here. It took us 3 years    
05:16:22: to hit 1 mill AR with our SAS product. Here's what  actually moved the needle and what didn't. So,    
05:16:26: this is a um phrase that I explicitly said that  I didn't want in the prompt. So, obviously,    
05:16:31: I'm going to have to do some adjustment there. We  sell to dental practices only dental practices.    
05:16:35: The temptation to go horizontal was constant,  but saying narrow am meant we could out build and    
05:16:38: outmarket anyone in the space. We charge more than  felt comfortable from day one. Honestly, the price    
05:16:41: anxiety never fully goes away, but underpricing  would have killed us. Okay, just while we have    
05:16:45: this, I'm going to go back to the actual page.  Make sure that nothing else was changed here.    
05:16:50: Cool. So, the design here is quite nice, right?  Hopefully, we can we can see that. The question    
05:16:54: is where do we go from here? Get started. Sign up.  What's the wizard looking like? Okay. Okay. And    
05:17:04: then we're going to have our prompt here. Try run  simulation. Sure. Oh, is this now actually using    
05:17:11: real cloud code? No, it's not. Okay, cool. Uh,  sorry. Um, Opus 4.6. We'll sign off. Enter the    
05:17:17: dashboard. So, the dashboard here is looking a lot  simpler. Um, you know, we we're missing a fair few    
05:17:24: of those cool design features that we had before.  And then we also have little rounded corners which    
05:17:30: I don't like. So, I'm just going to dump a bunch  of instruction into Claude and see if it can solve    
05:17:34: this. Hey, I want the design of the dashboard to  reflect the design of the landing page. Right now,    
05:17:42: there's a very big discord between the two.  Notably, the corners are rounded in the dashboard    
05:17:47: and not rounded everywhere else. There's also  color discords. We're using this soft purple,    
05:17:52: which uh is correlated with which is typically  associated rather with LLMs. I don't want pill    
05:17:57: style things anywhere here. And in general, I want  you to use the same fonts in the landing page for    
05:18:03: the new syndication or create page. I like how  we've laid this out so far with the URL, file,    
05:18:08: or paste text, but rather than have three buttons  that the user has to click, I just want them to be    
05:18:13: able to do it um do all of these simultaneously.  So, just have one field inside of that field    
05:18:18: allow users to either paste text, import a URL, or  upload the file. It'll eliminate some complexity,    
05:18:24: keep things really streamlined and simple. also  allow them to select which platforms they'd like    
05:18:28: to syndicate content to at the bottom. Right now,  the generating for button, generating for section    
05:18:33: rather, doesn't allow us to um make any of those  changes. Finally, make sure that the app looks    
05:18:38: similar to the landing page. As mentioned, it's  very important that we get this one right. Oh,    
05:18:41: this is much better. Okay, as we see here, we  now have that perfect design unification. I    
05:18:45: like the new syndication button up top. Um content  library, votes, profiles, analytics, config, and    
05:18:50: API access don't fully work yet, but this looks a  lot cleaner. So, we paste a URL. or drop a file or    
05:18:56: type our content here. If I go into my finder, if  I go into my finder and drop it, does that work?    
05:19:02: Oh my goodness, it does. That's really clean.  Likewise, if I paste a URL, so I don't know.    
05:19:08: Let's do this one here. Okay, for my big claw code  course earlier and paste that in. Does that work?    
05:19:14: URL detected. Really clean. Okay, we also have  blog x, Twitter. Okay. Okay, this is much much    
05:19:19: nicer. Thank goodness. Um, obviously this is  going to be difficult to see the differences    
05:19:24: between these lines. So, looks fantastic. Let's  add mild differences between the lines on the    
05:19:31: generation throughput graph. I also want to build  out pages for content library, voice profiles,    
05:19:37: analytics, setup, and API access. So, work all of  those out. Add uh whatever relevant features make    
05:19:43: sense. And if there are any additional features  that you think would make sense on the lefth hand    
05:19:47: side panel, please add them. I'm uh attempting to  increase the at least perceived sophistication of    
05:19:53: the app right now. Okay, I actually just stepped  away to grab myself some breakfast and came back    
05:19:57: and it looks like Claude is still monkeying away  at this. It's been probably 30 or so minutes.    
05:20:03: I've had very little actual hands-on involvement  and uh yeah, you know, like the agentic workflow    
05:20:09: time horizon of this specific model tends to be  quite large. Um, I'll say Gemini actually has    
05:20:14: a slightly longer one, but when you prompt  it right, where essentially you say, "Hey,    
05:20:17: here's a big road map of things. Here are a bunch  of changes that we've already made. Here's the    
05:20:22: uh whole spec of the thing that we ultimately want  to build." And then you just let it run loose. It    
05:20:27: can operate quite independently for quite a  long time. Um, and so this has gone through I    
05:20:31: think three or four context windows at this point  considering it's about 200,000 or so tokens. You    
05:20:35: know, I've spent a few million tokens um using the  cloud or anthropic API. That's multiplied by fast    
05:20:41: mode here. This sort of approach isn't the best  for everybody because of costs, but in my case,    
05:20:45: I'm happy to trade off that cost for um time  as previously and will continue to do. Checking    
05:20:50: back in on the app, it's looking significantly  more fleshed out. We have a content library up    
05:20:55: in here with the actual posts themselves. We can  go grab these posts and do something we wanted    
05:20:59: to. There are voice profiles now. Um there is a  brand voice, casual, blog. You can adjust that    
05:21:06: using this little section down below. You can also  add writing samples for best results which will    
05:21:11: improve the probability that an AI model actually  outputs what it is that you want. Generation    
05:21:15: volume right over here along with tokens used,  average numbers per session, platform breakdown,    
05:21:19: everything that I basically like talked about  in the spec. Finally, automation rules. So,    
05:21:24: um this is like a workflow thing where you can  automatically syndicate new content. Basically,    
05:21:27: every time you add new content, it'll  automatically go through a big flow. We have    
05:21:31: like enabled and and disabled and stuff like that.  Right now, these are all just stored on the local    
05:21:35: database. um it's left to be seen essentially  whether or not I could scale that up. We have    
05:21:40: profile platforms. This is where I can connect  and disconnect and so on and so forth. And ideally    
05:21:45: this would open up a little like connection  panel. And then uh you know we have notifications    
05:21:49: supposedly throughout email with the ability to  export all data. And this is really the section    
05:21:54: that I'm I'm the most excited about because uh you  know if you make your apps like agent compatible    
05:22:00: via API um I think that's going to be a massive  market later on. So, what I've done is I've added    
05:22:04: an API access section with like supposed  production keys and stuff. This isn't fully    
05:22:08: fleshed out, uh, as I'm sure you can imagine, but  still pretty reasonable. Um, what I'd like to do    
05:22:12: next is basically want to verify that all this  functionality works and and actually like does    
05:22:17: what it is that they imply that it does. And so  for this, I'm probably going to use a distributed    
05:22:23: um cloud code either agent team or I'm just going  to ask it to run through one by one by one. The    
05:22:27: idea would be, you know, spin up a se separate  instance to test the API key while you're spinning    
05:22:31: up a separate instance to test the notifications  while you're spinning up a separate instance to    
05:22:35: test the automation rules. We'll see how all  that stuff goes. Hey, this looks fantastic.    
05:22:38: I don't think there's anything else here that I  really want on the app. Um, maybe on the dashboard    
05:22:43: there is a little bit of white space at the bottom  because the system log is just just a little too    
05:22:48: long compared to the connected destinations.  I think we could probably fix that by adding    
05:22:52: one additional row of connected destinations.  That'll um match everything up quite nicely.    
05:22:56: Everything else looks really great. My next desire  is to test this end to end every specific feature.    
05:23:02: Just going through a really simple setup here  for LinkedIn O because I want to verify that    
05:23:06: this actually works. So, uh, we're going to add a  couple products to the app. So, share on LinkedIn,    
05:23:12: we have to do this. So, request access. We also  need, um, sign in with LinkedIn using open ID    
05:23:18: connect. So, I'm going to request access to that  as well. And the good news is, you know, you don't    
05:23:21: actually have to know how to do this yourself.  This is just stuff that uh in this case Claude,    
05:23:25: but Gemini as well can just walk you through.  Then under OOTH 2.0 settings, we need to add this    
05:23:30: redirect URL. So I'm going to go up to O. Just  going to grab the authorized redirect URLs. And    
05:23:36: then I'm going to paste this in. And then I'm also  going to copy both the secret um into this ENV    
05:23:43: file. And then I'm going to uh okay, added restart  dev server etc. And then when this is done,    
05:23:51: I need to go to setup platforms. Connect LinkedIn.  Okay, cool. So, I'm now going to check out what's    
05:23:58: going on over here. We'll mock. We go to setup  platforms and then connect LinkedIn. This is going    
05:24:06: to open up a little LinkedIn dialogue. I'm then  going to sign in using my own credentials. Okay,    
05:24:11: now I have a phone number that I have to verify.  So, I did just get this. I'll type that in.  
05:24:22: Now I'm going to sign in as myself. Cool. And it  looks like LinkedIn status is now connected. I'm    
05:24:28: going to head back over here and say connected  just fine. So we should be fine with this. Um    
05:24:35: find some way to store all of that info so we  don't need to reconnect next time. All right.    
05:24:43: So, we just did this um you know with with  LinkedIn. So, I should be able to go to new    
05:24:49: syndication now and then I don't know. Let me just  like find an actual post that I made before. Maybe    
05:24:53: my my blog. It's a good source for this stuff.  What's a fast one right over here? Actually, let's    
05:25:00: test this functionality. We'll click generate. I  don't know if it's actually feeding in this. So,    
05:25:07: that'll be the tough thing, the thing to double  check. We are on a generating tab. It's a fair    
05:25:12: amount of content. So, you know, I'm not expecting  it to finish basically immediately. Oh, also we're    
05:25:16: syndicating to LinkedIn supposedly. We should have  like a final check before we actually publish it.    
05:25:22: Okay. Okay, cool. So, it's double checked to  basically see whether or not we're connected.    
05:25:26: And so, X doesn't have publish, but LinkedIn does.  Most business small business owners are terrible    
05:25:30: at hiring. Honestly, it's not because they're bad  at business because nobody teaches you how to do    
05:25:33: it properly. Biggest mistake, hiring based on gut  feeling instead of actual data. You meet someone,    
05:25:36: they seem sharp. Cool, cool, cool. All right. Uh,  we still have some issues here. So like I don't    
05:25:41: know hashtags. Nobody uses hashtags anymore,  buddy. Remove that. Explicitly add it to the    
05:25:48: prompt. Uh we should never generate any sort of  hashtags. Also, I'd recommend against emojis in    
05:25:53: general. And then let me see what are we doing  that is sort of unfortunate. Most small business    
05:25:58: owners are terrible at hiring. And honestly, it's  not because they're bad, but it's the biggest    
05:26:01: mistake. Okay, so we have to avoid um LLM isms.  Like essentially the main LLM writing pattern    
05:26:10: that pushes it into uncanny valley territory is  when you jump between extremely short sentence    
05:26:16: lengths and then long sentence lengths and then  do that over and over and over again. That's not    
05:26:20: how most human beings will write unless they're  trying to be direct response copyriters. And for    
05:26:25: the most part we are we are not. So find a way to  adjust the prompt. Cool. And then everything else    
05:26:29: looks pretty good. So I should be able to actually  like push this. Um, thing is I don't really want    
05:26:34: to because then I'm going to have to publish this  on my own LinkedIn, right? Ah, I guess we're going    
05:26:38: to have to test it. All right, why don't we go to  another page here and then just verify whether or    
05:26:45: not this is being published to LinkedIn around  personal profile. If it is my personal profile,    
05:26:49: I'm just going to delete it basically immediately  because I don't want all my all my fans to see    
05:26:54: that. How do I do this again? Good god, man. Okay,  here we go. And we should be able to right click,    
05:27:00: press delete post, right? Okay, cool. Okay, just  ran into one issue right before I did this. So,    
05:27:06: I'm just going to Oops, that's not what I wanted  to paste. Um, I wanted to paste this. There    
05:27:11: you go. So, we ran into a problem just as I was  about to do this. I I don't know if it like out    
05:27:17: um just ran out and sort of timed out or  something, but okay. There we go. There we    
05:27:20: go. That's better. Okay. And now we should be able  to go to dashboard. I would hope anyway. Okay. It    
05:27:27: is going to force me to do this signin flow. We  do have some more platforms here as you could    
05:27:32: see. Fix the onboarding wizard as well. It should  now um function off of live data. Right now it's    
05:27:36: just doing the basic pass with templated stuff.  Okay. Setup. All right. All right. Here we go.    
05:27:43: Content library. Go back to new syndication here.  Go drive blog. Why don't we get something maybe a    
05:27:48: little bit shorter like this. Paste that in. Click  generate. We'll exit out of X Twitter so that we    
05:27:54: only have the syndication option for my LinkedIn.  Then we will go to my LinkedIn and then see if we    
05:27:59: could actually publish this. This is a blog post  I wrote basically all about interacting with my    
05:28:04: YouTube comments. I said uh you know the statues  that we are building aka our YouTube comments last    
05:28:11: way longer than the statues that people throughout  history have built because we don't know if people    
05:28:16: are going to be looking at these comments in  the year 2148 and the year 20,048 or what.    
05:28:20: So there's a lot of potential life there. Okay.  Clicked publish. Refreshing. Not seeing a post,    
05:28:27: which is good. I just clicked publish.  I'm not seeing a post on the LinkedIn. Uh,    
05:28:34: let me just on the generated content. Really helps  to be hyper specific. Did this copy work? Yeah,    
05:28:45: the copy worked. Okay. So, just want to double  check. Going to refresh this. And then I'm also    
05:28:51: going to head over to left click and see maybe if  we published it to there instead. I should be able    
05:28:56: to pull this up just by going back to the LinkedIn  page. Four left clicks. So, I can click on that.    
05:29:01: Go back to the company page and then we'll go  page posts. Okay. I'm not seeing a page post here,    
05:29:06: which is nice. Oh, wow. 675 followers. Did not  have any idea 675 followers in that company page.    
05:29:12: That's funny. Looks like there was a specific  issue with how we pushed this, which is okay. So,    
05:29:16: we're going to use actual API generate calls now.  And then I have the post right over here. Just    
05:29:20: going to head right over here. Click publish. Not  seeing any sort of notification. That's an issue.    
05:29:25: So, I'll head back to Cloud Code. I'm not seeing  any sort of notification after I click publish.    
05:29:29: Honestly, the experience doesn't feel very  snappy to me. I think the cursor might also be    
05:29:34: uh reason why. Find a way to just improve the  perceived customer experience when they click    
05:29:39: that button. Whatever it is, toast, menus, and  whatnot. We'll go back here. I'm just going to    
05:29:45: quadruple check. Make sure I didn't. Did I post?  No, I haven't posted. And then I'll do the same    
05:29:50: thing for leftclick. Let's go leftclick LinkedIn.  Just double check that that didn't post to either.    
05:29:57: It might have. Just unsure if I'm posting to  company pages right now or my own. Okay, doesn't    
05:30:02: look like I'm posting to either. One thing I'm  seeing here is we actually have been storing these    
05:30:06: in the database now, which is cool. Um, our local  database to be clear, but still a database. And    
05:30:10: so, you know, we can copy this. We could post this  to LinkedIn and whatnot if we wanted to manually.    
05:30:15: Um, but I do want to check to see whether or not  we could post u specifically like uh, you know,    
05:30:20: using that flow that we we showed you earlier.  So, I'll go back to new syndication. We're just    
05:30:24: going to do one more. Okay. Yep, we got it. I  got to delete the hell out of this thing ASAP,    
05:30:29: please. Thank you. And uh yeah, we've just  verified that this actually does post. So,    
05:30:33: fantastic work. That's incredible. Um, super  cool. Super cool. I'm going to go back here. Hey,    
05:30:38: I tried publishing and the first time I clicked  it, nothing happened. I waited five more seconds    
05:30:43: and then I clicked it again and that time it  went through the whole publishing loop and    
05:30:46: it actually appeared on my LinkedIn. Diagnose why  this might be the case. Go ahead and fix. Another    
05:30:51: cool feature is in the top rightand corner we  have a new. So I can actually just click new,    
05:30:54: go back here and then do another one. Um and  then I can also store all of that as you guys    
05:30:59: saw before inside of the content library along  with the specific generation for that um rung. So    
05:31:05: that to me is really really neat. Also the fact  that we have sort of the ability to go listical    
05:31:09: view is cool. You can tell that this really ran  with the spec that I gave it and it's um it's done    
05:31:14: a good job. I don't know. Okay, cool. Yeah, even  the search works. So very high quality stuff here.    
05:31:19: I'm going to head over to voice profile and see if  I could maybe set this as the default casual blog,    
05:31:24: do some editing and just double check what's  going on. So, as you can see, we can select    
05:31:28: these here. Um, I don't know. Is there any way  to like go deeper into what the actual prompt is,    
05:31:32: though? I'm not seeing that. I'm just seeing  like the ability to calibrate formality, humor,    
05:31:36: and emoji usage. So, I think I'm going to have  to add that feature. Hey, under voice profiles,    
05:31:40: I'm noticing that we can calibrate formality,  humor, and emoji usage, but I don't see any way to    
05:31:45: adjust the actual prompt itself. What I want you  to do is to add just like we have in the wizard    
05:31:50: some sort of advanced drop down that I can click  on that allow people to actually modify the uh the    
05:31:54: underlying text as well. Under analytics, I want  you to make sure that we are actually reflecting    
05:31:59: real analytics. Uh right now I'm not sure if we're  pulling from our database or what's going on. I do    
05:32:05: see that the recent activity here is updated with  the LinkedIn post, which is pretty solid, but I    
05:32:09: want to make sure that everything else is good,  too. Finally, under scheduling, um verify and    
05:32:13: test that this works for LinkedIn. It looks like  we have a scheduled post coming up. That said, I    
05:32:17: don't want you to actually publish it on LinkedIn.  Um, I just want you to verify that everything    
05:32:21: works up until that point. I've now been given  this initial schema. What I'm going to do is I'll    
05:32:25: head back to Superbase, go to the SQL editor, and  paste this in. Just verifying that these comments    
05:32:29: work. Okay, it looks like they do. I'm now going  to hold command and press enter. We're going to    
05:32:33: run this. And we see success. No rows return. I'm  going to go back to Cloud Code. And it looks like    
05:32:38: my Gemini subscription is finally coming back. The  rate limiting said it would be 1228. So, we have    
05:32:45: just another 10 minutes here before I can get  back to that. Um, which I think I'm going to do    
05:32:48: for like a final design. But that should allow us  to push through probably most of like the database    
05:32:53: migrations and stuff. Superbase SQL added. You  know, just to be clear, I don't like combining    
05:32:59: multiple um different models like while I'm in  the middle of a development session because I    
05:33:03: like all of the context that Cloud Code has to be  used in the cloud code thread and all the context    
05:33:07: of Gemini has to be used in the Gemini thread.  generally speaking, you get much higher quality    
05:33:11: results because uh this thing has processed so  many tokens at this point. You know, has so many    
05:33:15: so much history of like past design decisions and  stuff like that that it just inherently gets what    
05:33:19: it is that I'm trying to say. If I were to try and  just have Gemini, hey, pick up where whatever left    
05:33:23: off, you would basically have to do the entire  job of retraversing all of those failed paths. So,    
05:33:28: we're going to push this through with cloud code  and then at the end I'll probably do like a little    
05:33:31: design or redesign. Um maybe do some finishing  touches, some some final polishing with Gemini.    
05:33:36: Okay, so I'm going to say let's go 100% superbase  and we should be good. And it just got back to    
05:33:40: me saying that the superbase migration is now  complete. So it's also given me a summary with a    
05:33:44: bunch of API route os. It's verified the build and  whatnot. Verifying the build to me is not enough.    
05:33:50: I need to actually go through the whole testing  um end to end. So I'm going to have it log in,    
05:33:54: put in some credentials, and actually like do said  testing on its own because it has the ability to    
05:33:58: screenshot things and whatnot. Then once all this  stuff is done, it's just a matter of pushing that    
05:34:03: to um you know actually like a like a like  a Netlefi host and then also adding payments    
05:34:07: and stuff like that. The reason why I'm not adding  payments right now is uh I sort of had a change of    
05:34:11: heart. I thought a little bit about um what would  Stripe require in order to set all this up and I    
05:34:16: think Stripe would work better with like a live  published app since uh it has like a fair amount    
05:34:20: of callback functionality and I want to be able to  give it a URL. So I I'll do all that stuff after.    
05:34:24: Anyway, I'm not touching anything here. Model is  now proceeding autonomously and it's doing set    
05:34:28: testing without me. spotted a couple of issues  so far with the voice profiles table. So, it's    
05:34:32: going to go through and then actually apply the  migration. I can see this doing a bunch of silly    
05:34:37: BS here trying to solve some Superbase issue. So,  I told it just to give me whatever uh it needs    
05:34:42: and I'm going to go through and actually I can see  this doing some silly BS issue. Um what I'm going    
05:34:46: to do is I'm just going to run this directly  in the Superbase editor instead. It's saying    
05:34:50: alternative install this via Homebrew to run it  from here. I mean, like it can, but I don't know.    
05:34:54: I don't really want it to waste my damn time or my  tokens. So, I just created it. Um, should be good.    
05:35:03: Cool. Yeah. And you can see I've already done the  creation. So, we've saved ourselves some tokens    
05:35:07: there. I would hope. And uh yeah, I mean like  that's why I keep an eye on it. Good mental model    
05:35:11: here is pretend you're at like uh some security  desk job and part of your job is just like    
05:35:16: reviewing CCTV footage and there's like 10 CCTV  things in front of you. You're just like kind of    
05:35:19: glancing around at each. It's basically what we're  doing here. Although um you know with a little    
05:35:23: bit less context switching since I'm using fast  mode. But everything that I've done here, you can    
05:35:26: absolutely replicate with like two or three cloud  windows open. The reason why I'm starting with    
05:35:30: GitHub first is because I want this to be version  controlled. And to be honest, like you could have    
05:35:35: done this from step one. I just uh I'm not working  with anybody else in this project. It's just me,    
05:35:40: myself, and I. So this local folder is enough  for me until I get to, you know, the part where    
05:35:44: I'm ready to go. You can see it's um looking to  ask a question. Uh h I should probably do this    
05:35:49: privately because I don't want anybody to take  my tokens. Cool. We'll do that after it's done.  
05:35:56: um push to Netlefi. Use my credentials  since we're just demoing. I'll remove    
05:36:02: them later. And that way I'm going to  have like my env keys and stuff like    
05:36:05: that so I can actually go through the  uh the generation process and stuff.  
05:36:11: Cool. So now it's setting up Netlefi  deployment and then now we just need to    
05:36:15: connect to Stripe. So I'm going to head back  to Stripe and then I'm going to open up that    
05:36:19: uh publishable key thing. So signing in should  now open up a sandbox. So what I can do is I can    
05:36:25: actually copy the publishable key. Oh, that's not  it. I'll head over to ENV and then I'll also say    
05:36:32: Stripe publishable key. Add that. Also go Stripe  secret key. I'll add that. And I realize it's    
05:36:40: probably going to have to redo the update. Hey,  just a heads up. I've added Stripe publishable    
05:36:44: and secret keys tov as well. Our next step is  going to be to connect it to Stripe to get our    
05:36:49: payment integration set up. I'd like you to handle  this end to end autonomously. Once it's done,    
05:36:55: um, I'll do an endto-end test of the app myself  and let you know if there's any final changes.    
05:36:59: Cool. So, we've since pushed this app live and we  can actually see it at splinter-app.netlifi.app. I    
05:37:05: don't really think I needed that dash app there,  but the model made that choice and that's okay.    
05:37:09: Um, I'm liking this. It also looks like we have  that nice little I didn't really notice, but we    
05:37:13: have that nice little 3D geometric background.  Um, we're going to have to find ways to insert    
05:37:19: these pipeline visualizations. I've realized now  that we haven't done that on the landing page,    
05:37:22: but it shouldn't be too hard. I think we'll be  able to sort that out pretty quick. I'm also    
05:37:26: going to want to widen the landing page a little  bit because notice how the hero header is really    
05:37:29: wide and then everything else is really kind of  compressed. So, I'm just going to voice dump this    
05:37:32: and then um have it run through some final  designs. Hey, the landing page looks solid.    
05:37:38: Just checking the live Netifi link. Now, I'd like  you to add more platforms and social proof. Um,    
05:37:43: so just add more company logos and stuff. Aside  from the hero header, I find that everything    
05:37:48: underneath is pretty squished. Like it's not  very wide. It's very narrow. So I'd like you    
05:37:51: to significantly widen the design. Also, we have  processing pipeline visualization, tone analysis,    
05:37:56: matrix, multi format, compiler. These three are  placeholders that were meant to be filled in.    
05:38:01: What I'd like you to do is actually go through our  app and then fill this in with relevant sections.    
05:38:06: um not screenshots, but actually just mini builds  that uh elucidate various parts of the app,    
05:38:12: whatever the the specific feature is. Make sure  to widen the pricing and then the call to action    
05:38:16: as well. And just in general make this a little  bit longer and a little bit sexier. All right,    
05:38:21: let's take a peek at that actual landing page now.  We should have everything essentially ready. Oh,    
05:38:27: that is so cool. I don't think I'm going to get  over just how interesting it is to move my mouse    
05:38:32: around. Um, looks like we added significantly more  context here. So, we could see these little steps.    
05:38:37: And wow, that some of this is actually dynamic,  which is wild. So, future content creation isn't    
05:38:42: about producing more. It's about distributing  smarter. Here's how we scale our reach 10x without    
05:38:46: hiring a single additional writer. LinkedIn X,  blog, whatever. That's cool. We can then actually    
05:38:51: move these things around. That's really, really  interesting. Oh, wow. Nice. So, we can move the    
05:38:58: emoji usage and stuff like that around and then  add various features and and buttons. And this    
05:39:04: over here has a bunch of different sections for  different types of formats. Hot take. If you're    
05:39:10: still copy pasting the same content across every  platform, leaving 70% of your engagement on the    
05:39:13: table. Hell yeah. Threads. We added some more  steps down here. So, clean. We then added some    
05:39:19: data. We added an additional pricing tier,  which is nice. Creators love Splinter. So,    
05:39:23: we have some supposed big creators. And then  we can start our free trial or book a demo. I    
05:39:27: don't know if there is a demo feature though.  Is there? Yeah. Okay. So this is where we add    
05:39:30: our calendar. It's pretty neat. I'm probably  not going to do the demo stuff. Um anyway,    
05:39:34: that's fine. We'll start free trial. So now I'm  going to add some context. So we'll go Nikki    
05:39:40: Sarif. Go Nick@niki.com. Actually, why don't we  use a real email? We'll go a very simple password.  
05:39:51: So the creating is now taking us to the  onboarding. This is super clean. So maybe we just    
05:39:57: want LinkedIn for now. We're going to set up our  voice. So move this around. Looks like we don't    
05:40:03: have access to that advanced section just yet.  Let me see if I could pull something from my blog.    
05:40:11: Maybe we'll say this. Paste this in. Then I'll  click generate. We should go through a generation    
05:40:19: script here and it should be real. Okay. So  the output is what you get in production. Nice.  
05:40:31: Cool. This is now taking my post and then  it's um iterating on it slightly. Wow. This    
05:40:39: is great. Nice. Oh, nice. Yeah. So I think  the the difference here and the reason why    
05:40:49: this reads so well is because I specifically told  it do not have those crazy short sentences with    
05:40:56: like super long sentences immediately after  and then alternating cuz it's like blah blah    
05:41:01: blah blah blah blah blah that's not pattern  that's signal right it's like you know that    
05:41:05: that's AI just the way that it writes it this  has solved that for me which is clean okay    
05:41:10: nice anyway finish setup apparently we're  all set so we'll go to the dashboard here    
05:41:15: okay And we ran into our first issue, which is an  application error. So I'm going to paste this in.  
05:41:22: This occurred right after the onboarding wizard.  And now I'm just going to continuously push until    
05:41:28: I get all the way through the app. Now,  logically, what we should do after we are    
05:41:31: done our little onboarding wizard is we should  go directly to a pricing page. I'm okay with    
05:41:37: people making like their initial request that  little LinkedIn rewrite thing without having    
05:41:41: to sign in because while I know some people abuse  that um the abuseness I think will be outweighed    
05:41:46: by the convenience and then the wow factor of  actually just being able to pump content in and    
05:41:50: then getting it like nicely formatted and tuned  for LinkedIn. So I'm going to keep that in. But    
05:41:55: immediately after like we do want to force them to  pay and at that point they'll be in a little bit    
05:41:59: of like reciprocity like they will just have used  our app for free which allows us to say use for    
05:42:03: free and then in return um you know it's sort of  like a like a teeter totter or a scale in return    
05:42:09: they're going to want to balance that by paying  us and then I think I'm going to like make the    
05:42:13: intro offer like pretty affordable so people can  you know sign up get the ball rolling and stuff    
05:42:18: like that without necessarily having to spend  a lot and then um from there you know as they    
05:42:22: go grow addicted to Splinter her then uh you know  eventually the monetization will improve. Okay,    
05:42:29: this looks pretty good. Nice. All right, so why  don't we give this a little refresh here and    
05:42:33: see if our data is still in. Beautiful. So we have  this. The thing is we don't have any tokens. So we    
05:42:40: do have to ask ourselves how many credits. So free  plan. Okay, so we can do five I guess in total,    
05:42:44: right? So maybe we'll go new syndication up top  here. We can create content. But notice how we    
05:42:50: don't have LinkedIn or Twitter. So, one more  change I'm going to make is under Oh, actually,    
05:42:55: I guess that's to be expected because I selected  LinkedIn and then that one X or Twitter does not    
05:42:59: have an API and then blog is manual. When I click  new syndication, there's currently only LinkedIn    
05:43:05: X/ Twitter and blog available. I'd like you to  add all. We also need to force the user to connect    
05:43:10: at minimum LinkedIn and we need to do this post  onboarding. To be clear, are we giving them five    
05:43:15: free credits as in five free generations? Another  thing on LinkedIn is now that my app is live,    
05:43:20: we actually need to change the URL. So rather than  being localhost 3000, which is what it was before,    
05:43:26: we actually have to go back to Splinter and then  type in this, not that, this. So that should now    
05:43:34: give us the right redirect URI, which now if  I click on this, this will take us back here,    
05:43:39: which is good. So, I'm going to paste in this  password, click sign in, see if I have to    
05:43:47: connect via this. Okay, no, and I don't. That's  great. I'll head over to dashboard here. Now, we    
05:43:52: have one active platform configured. And um what  else we should do is we should offer some sort of    
05:43:57: like notification saying, hey, connect an active  platform. If a user has zero apps configured, then    
05:44:03: encourage them to connect to platform. Um, drip  this out in various places throughout the app.    
05:44:10: Okay, I'm going to add that here. And then I'm  just going to paste this in, then click generate.    
05:44:16: So now I'm actually going to run through and  I want to see how this interacts with credits,    
05:44:20: right? We're not doing payments here. We're  just doing um credits. It's your consumption.  
05:44:32: Cool. This looks pretty solid. Okay, nice. So I  can do that. Let's check and see whether or not    
05:44:37: this is actually going to work by heading back  to my page. And then I'll also check my posts.    
05:44:44: Then if I can make the post, uh I'm just not  going to test it again. I'm just going to assume    
05:44:48: that this is going to work. Okay, it's saying  published. Refresh. Okay, cool. So, I'm going to    
05:44:56: now delete this. That's pretty great. Uh posting  functionality, which is the core functionality,    
05:45:01: clearly works well. Okay, going back to  the dashboard, we now have one generation,    
05:45:06: but no tokens have been consumed. So, we're going  to have to fix that as well. I'm not seeing any    
05:45:11: credit consumption. I just submitted a request as  a Okay, cool. So, credit consumption here hasn't    
05:45:17: been fixed, but I do have this, which is nice.  So, I have the whole post. That's lovely. Let's    
05:45:22: um see if we can create a voice profile now. Okay.  And then we can also adjust the system prompt,    
05:45:27: which is nice. Cool. Looks like there's a uh  default system prompt here. And then there's    
05:45:31: also the ability to add writing examples. Nice. I  really, really like this design. It's super clean.    
05:45:36: Very brutalist, which is nice. As you can see,  we have one data point. Um, it's picking up our    
05:45:40: time. So, 12:57 p.m. we submitted one, which is  really cool. And then it looks like we've outputed    
05:45:46: one LinkedIn post, but it's also writing one  Xthread. Also, I only published this to LinkedIn,    
05:45:52: but it's telling me that I've also published  an X thread. Perhaps we should just add more    
05:45:56: context surrounding output types in analytics  so that they know that you have the option to    
05:46:01: copy from Xthread whereas the LinkedIn post  was actually published. Okay, heading down to    
05:46:06: scheduling here we could see a content Q. So  this is the generation I can actually select    
05:46:11: uh something I have generated which is neat.  So maybe instead of like publishing what you do    
05:46:16: is you just generate a bunch of things. You then  select the specific platform you want. So in our    
05:46:20: case LinkedIn then you can set the date using this  cute little calendar. So, why don't I pretend it's    
05:46:26: 2025 0228? Okay. And then I don't know, we'll  do 255 in the morning. That looks good. Let's    
05:46:34: add to Q. Cool. And so, now we do have something  coming up on Saturday at 255, which is nice. Now,    
05:46:42: moving over here to setup. It looks like I can  change my account details here. Let's just pretend    
05:46:49: I'm only saving my name. If I refresh this, you  see that that does not persistent. The setup page    
05:46:55: doesn't save my account details when I change it.  For instance, I changed my name from Nikki Sariah    
05:47:00: to Nikki Wiki. I press save changes and then  refresh the page and there was no um context    
05:47:05: there. I do like how under billing we do have uh  both the free plan and then we have starter, pro,    
05:47:10: and business. So, that's nice. Then we have  these little notifications and it looks like    
05:47:13: they're toggling fine, which is good. I do wonder  I don't think that this is 100% hooked up. So,    
05:47:18: we'll have to double check that. We have the  ability to delete an account. Oh, wow. Okay.    
05:47:22: Okay. And that autodeletes. So, we need to set  some sort of like feature that basically checks.    
05:47:28: I just clicked delete account and it immediately  signed me out. Make sure that there's some sort    
05:47:32: of are you sure message. Okay, that looks pretty  nice. Okay, now I guess this is good for me. If    
05:47:40: this actually did delete my account. Okay, no,  it didn't actually delete my account. I see. So,    
05:47:45: it just said that it deleted my account, which  is unnecessary. Never mind. It just said that    
05:47:49: it deleted my account. It didn't actually do the  deletion. Okay, now I'll generate new key example    
05:47:56: key. Okay, and then we need the curl details.  I'm just going to see if we could key here.  
05:48:10: Let's reveal this. And I'll say API key  send a request to this URL using the format.    
05:48:21: Let me see if it makes any sense whatsoever.  API splinter.io. Okay, for the API request, it    
05:48:28: doesn't look like the domain is a live host. Um,  update everything so that it reflects the new URL,    
05:48:35: not api.splinter.io. And then finally, we have  this web hook feature, which uh I don't know,    
05:48:41: let's just go web hook test. And over  here, we can copy a web hook URL. We    
05:48:47: could basically paste that into our app and say,  "Hey, when this is complete, scheduled or posted,    
05:48:52: I want you to deliver to this." So then I'm going  to go back to content library. And then I'm just    
05:48:56: going to do one more. So I guess we'll go to  dashboard, new syndication here. Then I'll just    
05:49:02: copy all of this over again. Paste it in. Okay.  And we have all the rest of these buttons now,    
05:49:07: which is wonderful. Click generate. And then I'm  going to go here and then check to see whether or    
05:49:13: not a web hook was actually sent. If the web hook  wasn't sent, I don't believe it will be. I'm just    
05:49:17: going to notify the agent. Hey, the generation  occurred, but the web hook was not sent to the    
05:49:21: address that I added. Um, double check that all  of that is okay. I imagine there's probably some    
05:49:25: issue related to the fact that we're not on the  URL that we initially thought we'd be on. Yeah,    
05:49:32: cool. So, we have that the generation has  occurred. We didn't end up getting that.    
05:49:36: I can copy this, though. Go back to dashboard.  Now, I see we have two created. And there's the    
05:49:41: content library here with the the the second  post, which is nice. Okay, what else is it    
05:49:45: telling me? It's telling me that um all the code  examples have been updated. So, I should be able    
05:49:51: to go back to API access here and then give this a  little refresh. I'm giving this a refresh because    
05:49:58: I wanted to hardcode the change. Okay, just  taking a look at this code. Example still says  
05:51:02: Okay, I'm going to go to upgrade and let's see  if that works. So, we can now select one of these    
05:51:06: three options. So, I'm going to go pro. Seeing  that it's opening up a Stripe checkout page,    
05:51:11: which is good. I'll go to USD and then I'm  just going to pretend enter some details    
05:51:14: here and then click subscribe. Looks like the  processing is occurring, but is it going through?    
05:51:20: Okay, cool. So, it looks like it went through.  Did we go back to checkout? Okay, cool. Yeah,    
05:51:24: we have and we've upgraded. When a user pays, um,  add some confetti or something upon the redirect    
05:51:30: only when they make it back after paying. Okay,  after a little bit more back and forth, you can    
05:51:34: see we actually have the right profile set up. So,  I'm going to head back to Stripe, generate a new    
05:51:38: key, and then actually reveal and then copy this  whole key. And I'm just going to see if this ends    
05:51:44: up working because that's the API functionality.  Okay, we're still getting unauthorized. Um, this    
05:51:53: using this superb basease session. I don't know  exactly what that is. I imagine this is probably    
05:52:00: going to solve it. Yeah. Okay. So, we we're going  to have to rewrite that a little bit. The good    
05:52:04: news is the name now saves along with various  password problems. Uh, we've now solved all of    
05:52:09: that. Wonder what managed subscription is going  to look like. I've never been there before. Oh,    
05:52:13: nice. Okay, cool. So we can actually like we we  literally have like our own managed subscription    
05:52:16: page which is Sweet. Um why don't I go to  dashboard just so I could take a look at that as    
05:52:20: well. Cool. So here are the generations and stuff  like that. Nothing upcoming because I don't think    
05:52:24: we have anything scheduled. Yep. Cool. Yeah. All  right. This looks pretty good. Generated formats.    
05:52:28: LinkedIn post two generated exert one generated  formats generated. Cool. Cool. This tells me what    
05:52:34: they are now. And then we have access to all of  our old posts. Awesome. So now I'm just going to    
05:52:39: mobile optimize this and then run security audit.  And then honestly that's it. We're live, baby. We    
05:52:44: can see we're actually sending over a live API  request to the Splinter-app API as well. So,    
05:52:49: this isn't just a front-end app for us anymore.  This is entirely um yeah, this is super clean.    
05:52:54: Super clean. So, yeah, pretty stoked about that.  We also have the API functionality. Obviously,    
05:52:58: we could paste in links as you guys have seen.  Not going to lie, this is pretty solid as far    
05:53:02: as apps go. We uh now basically have something  that's capable of doing everything that I want.    
05:53:06: Last thing is I'm just going to paste in this  security prompt. And just because we've done    
05:53:09: this what three times now, I'm not going to bore  you all with the details, but suffice to say,    
05:53:13: using Gemini 3.1 Pro in conjunction with Claude  Code for both a mixture of front-end design and    
05:53:19: then backend configuration, route creation,  and then payments, and so on and so forth,    
05:53:23: is pretty dang efficient. Now, I should note  that we used a ton of tokens this time, and I    
05:53:27: don't actually recommend using that many tokens,  like committing that many tokens to an app. Um,    
05:53:32: I just did this because I traded off speed uh  basically for money. I wanted to get this done    
05:53:37: as quickly as humanly possible because of an  upcoming engagement, not necessarily, you know,    
05:53:41: have three or four instances of cloud running  or uh, you know, take three or four hours when    
05:53:45: realistically I could have done it in 45 minutes.  So, I'm not going to push the fast mode on you.    
05:53:49: It's just an option. Uh, just keep in mind it does  cost a fair amount. This session was probably at    
05:53:53: least $70. And I'm sure you can imagine if  you develop an app every couple of days or    
05:53:57: work on your codebase every few days, that sort  of thing is going to add up pretty quick. For me,    
05:54:01: I'm happy to do it because of the arbitrage and  then the value that I got to produce. Hopefully    
05:54:05: you guys now see how to build an app just like  this. Not just a simple CRUD app, but a CRUD app    
05:54:09: that also has API wrapping functionality that does  OOTH integration with social media platforms even,    
05:54:14: which are some of the most secure and difficult  to authenticate and organize. And then finally,    
05:54:20: um, payment integrations as well, like with  Stripe. All right, so you now know how to    
05:54:25: vibe code an app. Congratulations. However, most  people that have gotten to this point are probably    
05:54:31: not just interested in building internal apps and  tools for themselves. Like, if you've gotten to    
05:54:35: this point, you're probably really interested in  building for other people, whether it's consumers,    
05:54:40: whether it's other businesses, maybe it's some  organizations that you're working with or whatever    
05:54:43: you want to help economize their workflow and so  on and so forth. And so, what I wanted to do next    
05:54:48: is round out the course with a module all about  pricing, packaging, and selling what you build.    
05:54:54: Now, most people that are here in your shoes,  okay, that are probably interested in um pricing,    
05:55:02: packaging, and selling what they just put  together, don't really have any experience doing    
05:55:06: so. And so, it's not that they don't have any like  vibe coding um business experience. It's that they    
05:55:11: don't have any business experience in general. And  so, what I wanted to do is just give you a very    
05:55:14: highle look at some tactics and playbooks that  you could follow to significantly streamline your    
05:55:20: ability to actually successfully go out there and  then sell this sort of stuff. whether you know at    
05:55:24: a small scale or whether at a large scale, whether  your goal is to replace your income or whether    
05:55:28: your goal is to, I don't know, start a business  that does $100 million. Now, I think there are    
05:55:32: a lot of people on YouTube that make courses on  vibe coding and stuff and um they're like, "Oh,    
05:55:37: you know, here's how you make all these super cool  crazy apps and here's how I spun up 500 clones and    
05:55:42: publish them to the app store." But not a lot of  these people have actually made money. So, I know    
05:55:45: that this is a vibe coding course, but hopefully  it'll allow me to dive a little bit into the    
05:55:49: business side of things because personally, that's  what I find the most interesting. Collectively,    
05:55:52: my businesses make over $300,000 a month in  profit. Um, and that's a pretty easy number to    
05:55:56: hit revenue-wise, I think, if you know what you're  doing. But profit-wise is a different story. So,    
05:56:00: all this to say, you know, I I do this sort of  thing professionally. I generate revenue outcomes    
05:56:04: and profit outcomes professionally for businesses  at this point. Let me run you guys through at    
05:56:08: least at a high level what I know and what you  guys can use to make some money with vibe coding.    
05:56:12: So, the big thing I want you guys to know is over  the course of the next, you know, 5, 10, 20 years,    
05:56:17: um, software will no longer be the moat. So back  in the day, right, 30, 40 years ago, if you were    
05:56:22: a cool startup and you were working on some new  computer system, okay, and you were smarter than,    
05:56:28: you know, your competitors and you spent more time  on it than competitors, you might have had like    
05:56:32: a small edge and maybe with that small edge, you  would have carved out like an operating system or    
05:56:37: something like that. And maybe potentially you  would have called that Windows OS and then you    
05:56:42: would have sold that at scale to people and that's  how you would have made your money. So if you    
05:56:45: think about it like Microsoft and Windows, Windows  uh uh was like software mode, software as a mode.    
05:56:51: Same thing with like the Apple brand of computers.  Same thing with like I don't know applications    
05:56:55: afterwards like Photoshop and like various  databases and stuff like that. Businesses that    
05:57:00: were built entirely off of software made sense  like 30 or 40 years ago because software back then    
05:57:05: was very difficult to make. Okay. Well, nowadays  software is very easy to make as hopefully I've    
05:57:10: just demonstrated here over the course of the  last six or seven hours or however long this    
05:57:13: damn course ended up being. So, we've transitioned  pretty heavily. Unfortunately, a lot of people are    
05:57:18: still stuck in that old school world where they  think, okay, that they're going to put together    
05:57:22: this incredible software solution that nobody else  in the market can do because they're smart and    
05:57:27: they're intelligent and they're they're visionary,  they're a forward thinker. The probability that    
05:57:31: you do that is extremely low. It's extremely low.  Not just because, you know, nobody's as special as    
05:57:36: we think we are, but uh because there are soon to  be 100 million times as many software engineers in    
05:57:44: the form of AI agents than there ever would have  been human beings. And so moes are no longer made    
05:57:51: through software. Your edge in the market is no  longer in the cool algorithm that you come up with    
05:57:56: or whatever the heck. Okay. where the moat is is  in distribution, which is fundamentally different.    
05:58:05: And rather than play by the software mode playbook  like everybody in their mom is doing right now,    
05:58:10: um I encourage you to play by the distribution  mode playbook. Hypothetically, why do you    
05:58:15: think Netflix is still Netflix in a world where  literally anybody could just tell their agent,    
05:58:21: hey, here's Netflix.com. can you go and recreate  everything about it and then I don't know you    
05:58:26: know host the the servers and set up databases  and set up all the infrastructure and then like    
05:58:31: have a little login page everything like that the  reason why Netflix is not broke you know today is    
05:58:37: because Netflix contains within it distribution  it contains a collection of clients vendors    
05:58:45: relationships their staff their team their culture  and so on and so on and so forth and these are    
05:58:51: things that an AI agent and until they, you know,  hook it up to the cloning vats and start pumping    
05:58:56: out clients, vendors and and staff members, um,  cannot currently do or reproduce. And so software,    
05:59:05: which used to be like the golden goose, right,  has basically been replaced almost completely    
05:59:12: with distribution. Okay? And in a world where  anybody could build any software, the only thing    
05:59:18: that makes your software different from somebody  else's software are the customers essentially the    
05:59:23: vendors, the relationships, and the staff on  your team um that manage it. Anybody in 2026,    
05:59:29: 2027 and beyond with a couple of ideas, a high  degree of agency, which just means your ability to    
05:59:35: like enact your will on the world, go out and do  things, and a very small budget, just a few bucks,    
05:59:39: literally 15, 20 bucks, can now build whatever  the heck they want. the whole moat, the whole    
05:59:44: edge is just your ability to actually reach and  then retain people within an ecosystem. And if you    
05:59:48: can do that, right, and if you can focus your time  and energy accordingly, then you can make a lot    
05:59:53: of money. But if you're stuck in the software  days, then you're just spinning your tires,    
05:59:56: man. The whole world's up and moved on and you  don't even know it yet. Hypothetically speaking,    
06:00:00: I want to pretend right now that um you know,  we we we got a little clock here, and this is a    
06:00:05: terrible drawing of a clock, but you know, bear  with me. Just pretend that this whole thing is,    
06:00:10: you know, a 60-second um um hand. Imagine that the  entire life cycle of this vibe coded business that    
06:00:17: you are about to start is this hand. Okay? And it  traverses a whole 60-second length. Here is how    
06:00:23: much I'd recommend that you actually spend on the  vibe coding part. Okay? Over the full 60-second    
06:00:30: life of your business, I would recommend you spend  maybe 3 or 4 seconds on the actual building. Let    
06:00:39: me make this a little smaller so we can see it  better. Everything else, okay, literally the    
06:00:46: rest of all of your time, my recommendation would  be to spend it not on building, not on tweaking,    
06:00:53: not on making your server infrastructure better,  not on doing whatever the hell. My recommendation    
06:00:58: would be to spend it on marketing. And this isn't  a joke. If you spend 3 seconds or 12th or 5% on    
06:01:08: building, you should spend the other 1920ths or  95% on the marketing. I don't know if you guys    
06:01:18: have been in like the the build and public space  on X. I used to be uh uh you know following that    
06:01:23: fairly frequently because it was just interesting  to me how people would share their revenues and    
06:01:26: talk about the apps they were building. And back  then they said you should spend at least as much    
06:01:29: time building as you spend marketing. You should  spend at least as much time marketing as you do    
06:01:33: building. And I was like okay so 50/50. Um that  was like four or five years ago. That no longer    
06:01:38: applies. You need to spend like 19 to 20 times  as much time marketing than building cuz anybody    
06:01:43: could do the building. The building is literally  just like your entry ticket to get onto the ride.    
06:01:48: The whole ride itself is your poorly spelled  marketing. So without marketing and sales,    
06:01:54: to be clear, you have no product. You may think  you have a product, but it's not a product. It's    
06:01:59: just a hobby because without customers, you  don't have any sort of business. You need    
06:02:04: revenue and so on and so forth. There are also  some additional benefits to having um customers    
06:02:09: that go far beyond the money that they pay you.  If you have customers, what you get is you get    
06:02:14: faster iteration because you're listening now to  real market feedback. You're not listening to like    
06:02:19: your own opinions and your assumptions, which is  what most builders will do. Most builders are like    
06:02:24: heavily biased. I mean, who the hell builds  software products anyway? For the most part,    
06:02:27: giant nerds, okay? Myself included. I don't know  what the average human being that uses my product    
06:02:32: actually wants or thinks. So, everything that I'm  doing is just assuming. I'm using my own opinions    
06:02:38: essentially and I'm hoping that my opinions  are correct because I possess a strong level    
06:02:41: of empathy or whatever the hell. But the reality  is most of the time I'm wrong. You know, it's like    
06:02:46: a ven diagram. You know, maybe like if this is  my opinions, maybe only like 50% of my oh my god,    
06:02:53: I really need to I'm writing like a doctor.  Um only like 50% of my opinions are actual    
06:03:00: reality. And so the only part of like this ven  diagram that I'm actually moving the needle for    
06:03:05: and like building features into my app that  actually make sense, okay, are over here. But    
06:03:09: like the other 90% is all [ __ ] you know? It's  all like uh I'm just wrong. So why would you even    
06:03:14: like worry about your opinions? Instead, focus off  reality and ground truth. The only way you can get    
06:03:21: reality and ground truth is getting customers.  The ideal is sufficient number of customers.    
06:03:26: so many so that you could start averaging  out their opinions and beliefs and desires    
06:03:29: and needs and so on and so forth and then you  just start designing for them. So rather than    
06:03:33: letting your own assumptions build the product,  use customer requirements, use customer needs and    
06:03:37: actually do like customer surveys. Launch your  vibecoded app today. You know, hypothetically,    
06:03:43: you've seen how easy it is to do. You know,  I can build one of these in just an hour or    
06:03:46: two. Okay? And then contact 20 people and have all  of them use your app for free and then tell you,    
06:03:51: hey, I liked this. I didn't like that. Hey, I  thought this could have been better. Hey, this    
06:03:54: didn't really solve my need. Hey, I wish it did  this. I wish it did that. Take all that feedback    
06:03:58: and then use it to design the next version of  your app because it's not the first version of    
06:04:01: your app that's going to make you any money. It's  like the 20th version of your app that's going to    
06:04:04: make you money. In addition, because customers and  distribution is really the moat, your whole focus    
06:04:09: should be on maximizing the customer experience at  every step. It should not be on making the nicest,    
06:04:14: sexiest, most polished app. And I know this is  kind of annoying cuz I did just spend the last    
06:04:18: part of, you know, five or six hours hopefully  teaching you guys how to do this and how to like    
06:04:22: make a really good product. But in reality, the  product, as we've seen, is really only like 5% of    
06:04:27: the whole pie now. So, focus instead on acquiring  as much distribution as quickly as possible. I'm    
06:04:32: going to run through some specific ways on how to  do that. And then once you have that distribution,    
06:04:36: um try and satisfy the needs of your customer.  And then generally and consistently iterate on    
06:04:40: the product. Okay. So, highle advice aside,  how do you actually do the big thing that I    
06:04:46: think a lot of people are wondering? How do you  price your product? Well, what I want to do next    
06:04:52: is talk about essentially my core principle for  pricing. And this is a core principle that I've    
06:04:56: used to generate tens of millions of dollars in  revenue across a variety of businesses, small    
06:05:00: to mid-size businesses, my own agencies, digital  marketing businesses, uh a couple multi-billion    
06:05:05: dollar portfolio companies. And um this is  something that I just I I continuously return    
06:05:09: to you because it's the easiest and simplest  way to price. So, it's called VBP or valuebased  
06:05:18: pricing. And so in value based pricing, what  you do is you price based off the value that    
06:05:23: your app delivers, not on your costs or your  competitor's pricing. You know, and I think a    
06:05:28: lot of people are like, well, I have to anchor to  my competitor's price, don't I? And to me, I say    
06:05:32: I mean like obviously your competitor's price is a  factor and people are going to be doing some price    
06:05:36: shopping. But if you focus on the value instead of  at what your competitors price rather than running    
06:05:41: uh down to the very bottom and it being like a  race down below like a lot of these freelance    
06:05:45: platforms and stuff where somebody bids nine,  another bids eight, another bid seven till you're    
06:05:49: at freaking zero. What we do is we just establish  how tremendously valuable a product is and then    
06:05:54: charge such a vanishingly small percentage of said  value that the customers are bought in regardless.    
06:06:00: I mean to them it's like a it's it's a pittance.  And I know this because I also purchase software.    
06:06:04: um what ultimately a lot of B2B software users  are looking for is something that maximizes their    
06:06:09: return on investment and minimizes the friction  involved in making the purchase decision. So let    
06:06:13: me explain what I mean by all this. There are two  types of value that you can produce at least in a    
06:06:17: B2B environment. In a B2C environment you have  additional types of value. Those types of value    
06:06:21: are nonmaterial and so it will not be discussed.  You have the ability to directly reduce their    
06:06:27: expenses which is the money that your product  will save a customer if they use you. And then    
06:06:32: you also have the ability to significantly  increase their revenue in opportunity cost,    
06:06:38: which is also termed the additional money  customers can now earn because they use your    
06:06:42: product. I think direct expense savings are pretty  simple, right? If I have product X and product X    
06:06:48: currently costs the user $100 a month and I say,  hey, I just built product Y. Product Y only costs    
06:06:55: $5 a month. What do we have there? What I've done  is, if you think about it, I've saved the customer    
06:07:01: $95 every month. And so the direct expense savings  are 95 bucks. Easy. Now, an opportunity cost. Now,    
06:07:12: opportunity cost is a little bit different.  Instead of focusing specifically on what the    
06:07:15: delta between, you know, their old thing and then  their new thing is, what we focus on instead is    
06:07:21: how much time do they save and what is the  cost of that time. So I'll give you a brief    
06:07:30: little example. Let's say hypothetically you  are currently a salesperson. You work at big    
06:07:36: company. Big company pays you on average about  $100 per hour. Right now, as part of your day,    
06:07:44: you do some [ __ ] admin task. That admin task  involves filling out some CRM or whatever. And    
06:07:50: on average, every single day, you have to spend  2 hours doing this. Okay? So, they're paying you    
06:07:57: $100 an hour. You're doing an admin task that is  worth 2 hours. If you hypothetically could build a    
06:08:03: software solution that enable this salesperson  to spend zero minutes doing this admin task,    
06:08:08: how much money are you saving this salesperson  right off the bat? You're saving this company    
06:08:13: right off the bat. You're saving $2* $100 an hour  or $200 an hour. That is your direct expense. But    
06:08:23: if you think about it, what do sales people do?  Salespeople are tasked with increasing the revenue    
06:08:29: of the business that they work in. Hypothetically,  let's say if instead of focusing on admin time,    
06:08:36: they then focus on sales, aka calling people or  whatever. in those two hours they could contact    
06:08:42: 50 people and if in one in 50 people end up  purchasing a small product or something like    
06:08:48: that okay which is their conversion rate and if  the average cost of that product is let's say    
06:08:53: uh I don't know $500 then by saving 2 hours a day  not only are you adding $200 sorry $200 an hour    
06:09:03: I meant $200 not only you adding $200 back to the  core business that you built the software platform    
06:09:08: for you're also adding If you think about it,  an additional $500 in revenue. So this is minus    
06:09:15: $200 of expense. Okay? And this is plus $500  in revenue. And if you think about the total    
06:09:25: amount now that this software product is saving  or generating the business, we have come to    
06:09:32: $700 in value and that's per day. Okay. So the  expense portion is about saving money whereas    
06:09:40: the revenue portion is about reallocating the time  that your software solution is now saved to allow    
06:09:45: a person at a business to focus on higher revenue  things that actually produce for a company. And in    
06:09:51: practice usually these expenses are much smaller  than the total amount of opportunity cost aka    
06:09:56: the revenue that you are unlocking. So you know  how earlier we built a thumbnail generator? Well    
06:10:00: here's a quick example of what that might look  like. You have direct cost savings. Let's say    
06:10:05: right now whatever system that they are using  cost them $50 a thumbnail and they generate 20    
06:10:10: thumbnails a month. That means that by switching  over to nyx thumbnail company.co, also known as    
06:10:16: thumbly, uh you'll save $1,000 a month. But when  you take into account the time savings revenue,    
06:10:22: okay, you move this 2 hours per thumbnail design  period to 5 minutes. What you're doing is you're    
06:10:28: saving 115 minutes. And hypothetically, let's  say these 115 minutes times 20 are 2,300 minutes    
06:10:36: a month. Let's say with this additional time,  which works out to be approximately 40 hours,    
06:10:42: this designer or something can actually make  an additional $1,000 a month as well. Well,    
06:10:46: now the total value created is $2,000 a month.  What we're doing as somebody that is developing    
06:10:51: a thumbnail product is we're pricing at a very  small percentage of the total value we produce,    
06:10:55: so maybe 10%. So, we charge 200 bucks a month. And  then the customer ends up making 10 times as much    
06:11:00: money as they spend with us for using our service.  Now, obviously, this is going to be an average,    
06:11:04: right? Every customer is going to be different.  Some people are going to produce way more value    
06:11:08: than your $2,000 a month estimate. Others are  going to produce less value. But because you    
06:11:12: can't price individually per every new customer  that you onboard, you have to pick a specific    
06:11:16: package price. What we've done now is we've  basically used facts and logic to work out what    
06:11:21: a strong value would be for a core product and  then how much to charge for it instead of relying    
06:11:27: on things like competitor analysis or worrying  about what the dude in the next cubicle over is    
06:11:32: doing. And so this is a much more sustainable and  higher ROI way of pricing. You're pricing based    
06:11:36: off value. You're not pricing based off of what  everybody else is doing. This young viewers is    
06:11:41: how you zigg when everybody else zags. Once you've  established some sort of price for your product,    
06:11:46: my recommendation is I actually establish  this as my top price. So, for instance,    
06:11:51: um let's say I kind of screwed up the uh writing  here, but let's say this is like your top tier,    
06:11:56: this is your mid tier, and this is your entry  tier. You know how there's typically multiple    
06:12:00: subscription tiers for a product, right? Assuming  you're doing a monthly thing. What you do is you    
06:12:03: take the top and then you set that one at uh you  know, let's say 200 bucks a month. And what you    
06:12:08: do is you set your middle at approximately half of  that and you set that at about 100 bucks a month.    
06:12:13: but you uh reduce the ROI to compensate. So in  this case, you know, previously I'm offering a    
06:12:17: 10x ROI on my top. Well, now I'm offering an 8x  ROI on my mid and then a 6x ROI on my entry. And    
06:12:23: so in this way, you have like a reasonable product  differentiation. You have a reasonable spread of    
06:12:26: values. And this is enough to get you started  before, you know, you can get enough customers,    
06:12:30: you can actually run like strong analytics to  determine whether or not people would actually    
06:12:34: prefer a $37 a month product or a $58 a month  product or whatever. And that's honestly all there    
06:12:39: is to it. To make a long story short, what I do  anytime I'm pricing an app, uh, Pel, an automation    
06:12:44: service, a back-end tool, even like a big business  deal, back when I was um, operating a content    
06:12:48: writing agency and we were trying to work out how  much to price our product, uh, we do it all based    
06:12:52: off of value pricing, which is determining how  much value our product has to the user to begin    
06:12:57: with, an expense, an opportunity cost, and then  just charging a small percentage of that. And    
06:13:01: that usually ends up being somewhere between 10 to  20% of the total ROI. And as a business owner, I'm    
06:13:06: thinking like, hey, I could put my money in the  S&P 500, I could make 8% a year, or I could give    
06:13:10: my money to NYX Co. and then I'd make a,000% on my  initial investment. What am I going to do with my    
06:13:16: money when presented that choice? Obviously, I'm  going to give it to Nyx Co. right now. Uh, whether    
06:13:20: or not somebody chooses to invest in you isn't  just a product of this math. It's also how much    
06:13:24: they believe the math, and that's another part of  marketing. But I'll leave that for another day.    
06:13:28: Hopefully, at least now you guys understand how to  price set products. But that takes us to the next    
06:13:33: big thing, okay? which is well there's pricing the  product but how do I actually get my product out    
06:13:38: there okay how do I actually market this amazing  thing that I have developed well there are three    
06:13:45: major ways the first is outbound a lot of people  shy away from outbound but outbound was the very    
06:13:50: first thing that I did when I started my first  business my first real business about 10 years ago    
06:13:54: I went door to door literally knocking on business  doors coming in trying to shake their hands and    
06:13:59: then sell them on my little marketing package it's  very difficult but this is ultimately what works    
06:14:04: So in this case, you go directly to people who  need your product. You can consider this like a    
06:14:08: sniper rifle approach. The two most popular  methods right now are cold email, which is    
06:14:12: where you actually craft an email, usually using a  template that appears to be personalized onetoone    
06:14:18: communication between you and the person that's  reading. And then you say, "Hey Pete, I love what    
06:14:22: you're doing over at XYZ Business. I think right  now you guys are currently spending all this money    
06:14:26: on the software, and I can save that for you with  XYZ product. I would be happy to give this to you    
06:14:31: for like a major discount because you're going to  be one of my first five uh you know signups. I've    
06:14:35: also attached a video here that runs through how  to do X Y and Z. Um let me know if you have any    
06:14:39: questions. If I can help you out at all would be  happy to. Okay. And so in this way you're reaching    
06:14:43: out directly to them. This is you. This is them  and this is you bridging that gap. That's why it's    
06:14:50: called outbound. The other main way to do this  is through cold DMs. And typically you do this    
06:14:54: on B2B platforms like LinkedIn. Cold DMs stands  for direct messages. It's just the same thing    
06:14:59: as cold email. It's just instead of using like an  email inbox, which tends to be the the highway to    
06:15:04: the soul, um we're instead using like a LinkedIn  message box or like an Instagram message box,    
06:15:08: but it's the exact same idea. Some caveats here.  This works really well for B2B products, but it is    
06:15:14: pretty difficult for consumer products, aka B2C  products, since most of the lead sources where    
06:15:19: you're going to scrape this information do tend to  be B2B. Like for instance, if you think about it,    
06:15:23: LinkedIn is entirely a commercial platform. If  you sign up to LinkedIn, odds are you're signing    
06:15:27: up for employment or business purposes. So, you  can feel pretty safe that most of the people that    
06:15:31: you're scraping on LinkedIn, you're doing so  because it is a B2B sort of transaction. Hey,    
06:15:35: I can help you at XC Corp. Hey, I saw you're  employed at whatever position. I think I can    
06:15:38: assist you with that and so on and so forth. If  they're not on LinkedIn, crap gets a lot harder,    
06:15:43: right? So, for the most part, anytime I sell B2B,  I start with Outbound. The other big benefit to    
06:15:47: outbound is it's just really fast. It is way  faster than any of the other methods on the    
06:15:50: list. It's also way harder, right? you sort of  have to put your freaking ego on the line. And    
06:15:55: um I can't tell you how many times I got thrown  out of businesses when I was knocking on doors.    
06:15:59: Security racing after me being like, "Get  the hell out of this plaza." Uh but you know,    
06:16:03: it it worked and it was what enabled me to make  my first uh probably $15 $200,000. That said,    
06:16:07: this is not the only thing that you can do. It is  not the only way. There are a variety of others.    
06:16:12: The second is inbound, which I think a lot more  people here are probably familiar with. Inbound,    
06:16:17: if you kind of think about it logically, is  kind of like what I'm doing right now. What    
06:16:21: I'm doing is I'm creating very valuable content.  I'm building a very strong and large audience of    
06:16:26: people that enjoy consuming my content. And then  what I'll do is I'll direct a small percentage of    
06:16:30: you guys to some paid products so that you guys  sign up to my service or whatever. The issue with    
06:16:34: inbound, despite the fact that, you know, if I'm  here and then they're here, despite the fact that    
06:16:40: they're now coming to you, is it's a lot slower.  It takes a lot longer to build. Okay. And what a    
06:16:46: lot of people don't realize is they'll watch some  vibecoded course or whatever and then be like,    
06:16:50: I'm going to make my own app business. It's going  to be awesome. And then they start making content    
06:16:53: on it. What they don't realize is like when you  make content um on the on the wider internet like    
06:16:58: on YouTube or LinkedIn or Instagram or whatever,  what you're basically doing is you're like in a    
06:17:02: sea of a billion people and then you're  given a megaphone. And then you're like,    
06:17:06: "Okay, I have a megaphone. This is awesome." And  then what you don't realize is every other person    
06:17:10: also has a megaphone. And then the big people that  are pretty established have megaphones that are    
06:17:14: way bigger than you. And then the small people  like yourself have these tiny little things that    
06:17:17: barely produce any noise uh whatsoever. And so  growth on inbound is extraordinarily difficult    
06:17:23: as a beginner unless you have some pre-established  success or pre-established wins. And most people    
06:17:28: that are starting these sorts of things that  immediately turn to I'm going to post one thread    
06:17:31: on Instagram every day for the next year. Uh  they they don't understand this. And so what    
06:17:35: ends up happening with a lot of inbound is because  it takes so much longer to build and people are so    
06:17:41: unprepared for this, they end up just screeching  into the void, never achieving anything. and then    
06:17:45: quitting before they actually build up the amount  of momentum required to succeed. If I could graph    
06:17:50: sort of like the differences between inbound  and outbound. And I love graphing stuff. So,    
06:17:54: in case you've watched any of my other videos,  get ready for a freaking Nyxive graph. Basically,    
06:17:59: this is the amount of time that it takes to see  any sort of win. And then this is the amount    
06:18:03: of money that it takes. Okay? And I'm going to  I'm going to pretend that blue here is inbound.    
06:18:08: And I'm going to pretend that orange here is  outbound. And you guys are going to see why    
06:18:11: I prefer outbound in terms of the total amount  of money you could make. Um, if you use inbound,    
06:18:16: okay, what happens is you start at this time step  one and then you make no money for a long time    
06:18:21: and then all of a sudden your brand picks up and  then you make a ton of money. With outbound, it's    
06:18:26: basically the exact opposite because every single  time you send a piece of outreach, it consumes a    
06:18:32: little bit of your time. What ends up happening is  you usually have some success initially and then    
06:18:37: you start tapering out or plateauing and hitting  a ceiling. And so if you think about it logically,    
06:18:42: both of these have major trade-offs, right? But  with outbound, what happens is you make money much    
06:18:46: much faster. You know, this might be 1 month. This  over here might be one year. And so with inbound,    
06:18:52: what we've done is we've sacrificed all our  money in the first year for money after year    
06:18:55: number one. And with outbound, what we've done  is we've sacrificed money after year 1 for money    
06:18:59: before year 1. Um in reality things are never  fully black or white and so the recommendation    
06:19:04: is usually to do some sort of blended take of both  where you know at the beginning you start mostly    
06:19:10: with outbound. Okay. And then as time goes on you  shift more to inbound which allows you to generate    
06:19:16: revenue quickly without also tapering out. Um that  said there are a variety of different ways you    
06:19:20: could do this sort of thing. That's where business  programs like u mine maker school and so on and    
06:19:23: so forth come into play. So I'll I'll leave that  with you and you guys could do whatever you want    
06:19:27: strategically there. The third major way that you  could market as somebody that develops and builds    
06:19:30: products is instead of trying to build your own  distribution via you know outbound like we talked    
06:19:36: about earlier or inbound where people come to you.  What you do is you just take somebody else okay    
06:19:43: somebody like Nick Sarif and you say yo Nick can  you market my product for me and then I'll just    
06:19:48: pay you 30%. And then what happens is Nick, you  know, can use a combination of both inbound and    
06:19:54: outbound methods to do that marketing for you. But  the idea is because he's already developed sort of    
06:19:59: pre-existing distribution, it's way faster. And uh  you know, all you're really doing is you're paying    
06:20:04: a percentage. So it's more predictable for you.  Maybe it won't necessarily be cheaper, but it's    
06:20:08: probably cheaper than you initially buying a bunch  of software platforms, getting a bunch of cold    
06:20:12: emails, uh getting a a beautiful studio and all  that stuff. So, the whole idea is you just partner    
06:20:17: with someone who has pre-established distribution  and then you make it a win-win for them. You're    
06:20:20: like, "Hey, man. This software does exactly what  the heck you really like to do. Uh, I think I can    
06:20:25: really help your viewers and stuff like that as  well." And rather than you having to build a whole    
06:20:28: new product from scratch, why don't you just use  my product and I'll just pay you a percentage. You    
06:20:32: like my product, right? Yeah. Okay. Awesome. So,  it's a win-winwin. As mentioned, it can be inbound    
06:20:36: or outbound affiliate, though. Inbound tends to be  the most popular one because it's more scalable.    
06:20:40: And then yeah, you're just monetizing somebody  else's audience or work, which allows you to    
06:20:43: like quickly jump cut in uh basically return for  some predictable outflow of your money. Okay, so    
06:20:50: hopefully I've now showed you guys how to not only  price but also package together multiple tiers and    
06:20:55: then also get started with the marketing of your  product. My recommendation to be clear is to start    
06:20:59: with some form of outbound laser or sniper rifle  target specific people whose needs you are solving    
06:21:07: and handling with your product. And once you have  a solid base set up, maybe 10, 20, $30,000 a month    
06:21:12: in recurring revenue, then you can transition  over to maybe building a brand um um you know,    
06:21:17: doing the whole megaphone analogy that in reality  tends to be the best of both worlds. Um affiliate    
06:21:22: is also open to you at any level of the stack.  So whether you guys are early on, whether you    
06:21:26: guys are a little later on, I do highly recommend  looking for those sorts of partnerships and then    
06:21:30: finding opportunities to, you know, plant your  seed and have other people water them from here    
06:21:34: on out. Obviously, I can't cover every possible  business permutation. Some people are going to do    
06:21:38: like high ticket SAS style stuff where you have  to sit down and do demos. It's going to be more    
06:21:42: sales. Other people are going to do low ticket  SAS stuff where basically people guide themselves    
06:21:46: through their onboarding checklist and stuff. Um,  you know, that tends to be more marketing. But    
06:21:50: hopefully this at least tells you guys a little  bit about where the market is going and then    
06:21:54: how to practically take what I'm talking about  here to improve the quality of your guys' lives,    
06:21:58: businesses, and so on and so forth. Okay, that  was a hell of a course. I had a lot of fun putting    
06:22:02: all that together. If you guys have made it to the  end, y'all are real ones. I have uh one quick ask,    
06:22:07: two, I suppose. The first is if you guys like this  sort of thing and you guys are curious about how    
06:22:11: to monetize your own vibe coding business,  definitely check out Maker School. It's my    
06:22:15: day-to-day accountability program where I actually  guarantee you your first paying customer for an    
06:22:19: AI or automation business in 90 days. If you don't  get customer number one in 90 days, I I refund you    
06:22:25: in full. So, it's a full 100% guarantee. Inside  of Maker School, you'll learn how to put together    
06:22:29: really classy and clever offers, sort of like  the offer I'm using to get you into Maker School,    
06:22:34: as well as do things like set up outbound  campaigns, uh, productize your business, and    
06:22:38: then eventually scale to inbound, like I talked  about here. Additionally, I'd love it if you    
06:22:41: could check out my podcast with Mr. Jack Roberts.  We both talk on AI automation. It's a blend of    
06:22:46: news and then us just goofing around, showing  off our boulder shoulders. So, no pressure.    
06:22:51: Do whatever the heck you want. Lastly, you'll  find everything that you need down below in the    
06:22:54: project description. And then yeah, if you really  like this sort of thing, then please subscribe.    
06:22:57: Helps out my channel. Comment and engage with the  video. And I'll catch all y'all on the next one.  
