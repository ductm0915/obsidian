00:00:00: Hey, welcome to the definitive guide on  
00:00:01: agentic workflows for business. Now,  
00:00:03: agentic workflows have the potential to  
00:00:05: bring about what I think is one of the  
00:00:06: largest wealth transfers in human  
00:00:08: history. But very few people are  
00:00:09: currently talking about how to  
00:00:10: practically use them to improve their  
00:00:12: financial means. That's what this video  
00:00:14: is going to show you how to do. Here's  
00:00:15: what you're going to learn. What an  
00:00:16: agentic workflow really is. How agentic  
00:00:19: workflows function via loops. A few  
00:00:21: common problems with agentic workflows  
00:00:22: and how to fix them. How to actually  
00:00:24: build these things. So, idees, setting  
00:00:26: up your workspace, creating your first  
00:00:28: flow, the DO framework, directive  
00:00:30: orchestration and execution, claude  
00:00:32: skills, MCP and other frameworks, what  
00:00:35: each one does, when to use which and how  
00:00:36: they all fit together, how to test and  
00:00:38: validate agentic workflows, the best  
00:00:40: system prompts for agentic workflows,  
00:00:42: which I will give you, how to make your  
00:00:44: workflows self annealing, aka heal  
00:00:46: themselves when they air out, how to  
00:00:47: move out of the IDE and into the cloud.  
00:00:49: I'll teach you how to create web hooks,  
00:00:50: schedule triggers, and more. How to run  
00:00:52: multiple agents simultaneously. I'll  
00:00:54: show you a sub aents and advanced  
00:00:56: workflow parallelization. And finally,  
00:00:58: how to troubleshoot agentic workflows  
00:01:00: when things break. If you don't know who  
00:01:01: I am, I build two AI based service  
00:01:03: agencies to $160,000 a month in combined  
00:01:06: revenue. I've also consulted for a  
00:01:07: couple of billion-dollar businesses with  
00:01:09: AI. And I tell you this cuz I want to  
00:01:10: make it clear. Well, you guys are of  
00:01:12: course going to learn everything from  
00:01:13: the fundamentals all the way up to the  
00:01:14: advanced concepts today. This course has  
00:01:16: a business focus. My goal is to help  
00:01:18: prepare as many people as possible for  
00:01:19: what I consider to be the next stage of  
00:01:21: the economy. So what you will learn  
00:01:22: today is working right now. It is  
00:01:24: generating revenue right now and you can  
00:01:26: use it to improve your own and other  
00:01:28: people's businesses right now. Please  
00:01:29: bookmark this and use the chapter  
00:01:31: feature to come back to it or whenever  
00:01:32: you need anytime. And I hope you guys  
00:01:34: are excited as I am to get into Agentic  
00:01:36: Workflows. Let's get started. This is a  
00:01:38: practical course. The whole point of it  
00:01:40: is to build and then use Agentic  
00:01:43: Workflows in real business environments.  
00:01:46: And that's because building is the most  
00:01:47: effective way to learn anything. When  
00:01:49: you build with your hands and get them  
00:01:51: dirty, you're forced to deal with  
00:01:53: concepts in a way that you guys never  
00:01:54: would have if you just sat back and  
00:01:56: passively listened. That said, before we  
00:01:59: get into the building, and there will be  
00:02:01: a lot of building and a lot of demos in  
00:02:02: this course, there are some foundational  
00:02:04: things about agents and workflows that  
00:02:06: I'd highly recommend that you understand  
00:02:09: because if you don't understand them,  
00:02:10: you're going to commit many hours to  
00:02:11: this course and you'll only really be  
00:02:13: able to digest or extract a few  
00:02:15: percentage points of it. So what I want  
00:02:17: to do is I want to maximize the ability  
00:02:19: and efficiency of your time by helping  
00:02:21: you cover those concepts now. And by  
00:02:23: doing that, you'll be able to absorb the  
00:02:25: rest of the course a lot faster and a  
00:02:27: lot better. So what do I mean by  
00:02:29: concepts? AI is currently in an overhang  
00:02:32: state. Current AI capabilities are very  
00:02:35: far beyond what most people believe,  
00:02:37: expect, or know how to use. If you guys  
00:02:40: graft this, what we have down here is  
00:02:43: sort of like the general public's  
00:02:45: perception of AI, okay? And their  
00:02:47: ability to use it. And what we have  
00:02:50: above it is sort of like the reality,  
00:02:54: okay? You guys are going to see a lot of  
00:02:56: very crappily drawn lines in this  
00:02:58: course, so you might as well get used to  
00:02:59: them now. So this gap between the  
00:03:02: reality of the situation and then what  
00:03:04: people believe AI is capable of is  
00:03:07: called the overhang.  
00:03:10: The reason why this overhang exists and  
00:03:12: the reason why people are only squeezing  
00:03:13: out a very small percentage of the  
00:03:15: actual value of AI, large language  
00:03:17: models, agentic workflows and so on and  
00:03:19: so forth [snorts] is because right now  
00:03:21: most people are using them as glorified  
00:03:23: copy and paste tools. They are basically  
00:03:25: trying to drink through the Pacific or  
00:03:27: Atlantic Ocean with a tiny straw. You  
00:03:30: know, they ask these galaxy brain  
00:03:32: intelligences. Pretty dumb questions to  
00:03:34: begin with to be honest. They answer and  
00:03:36: then all they do is they copy it from  
00:03:38: one tab into another, which is obviously  
00:03:40: a very low bandwidth, really  
00:03:42: bottlenecked way of working. They are  
00:03:44: not integrating AI into their business  
00:03:46: like I'm about to show you how to do in  
00:03:48: this course. Instead, they're just  
00:03:50: dealing with it like a like an external  
00:03:52: sort of third party thing.  
00:03:54: Now, obviously, people are figuring out  
00:03:56: that AI is a lot more powerful than most  
00:03:58: people give it credit to, and courses  
00:04:00: like mine are helping them do so. But as  
00:04:02: they figure it out, the arbitrage window  
00:04:04: will close. And in case you guys didn't  
00:04:06: know, arbitrage is your ability to  
00:04:08: essentially produce some sort of  
00:04:10: beneficial outcome, revenue or profit,  
00:04:12: based off of a disparity in knowledge.  
00:04:15: And so, if you know, you know, this and  
00:04:18: the rest of the market knows this,  
00:04:21: obviously there's kind of a gap there,  
00:04:22: right? and the market is willing to pay  
00:04:24: you to be somebody that solves that  
00:04:26: little tiny gap. Well, that window is  
00:04:28: closing because people are learning  
00:04:30: about how this technology works. But  
00:04:32: right now, it's wide open and you can  
00:04:34: make a ton of money with it. So, just as  
00:04:35: a demonstration to show you how powerful  
00:04:37: these models are, I'm going to have one  
00:04:39: in particular called Claude Opus 4.5 do  
00:04:42: a pretty straightforward task for me.  
00:04:44: This task is to compile a list of five  
00:04:46: local meal preparation companies that  
00:04:47: deliver to around my area and then find  
00:04:49: their email addresses. I'm then going to  
00:04:51: send each of them emails with  
00:04:52: specifications from this email. I want  
00:04:54: uh you know 3500 calories a day, 200  
00:04:56: grams of protein a day. I'm doing some  
00:04:58: big bulk. Do this entirely autonomously  
00:05:00: requiring no input from me. If you  
00:05:01: cannot find the emails of at least five,  
00:05:03: then keep on searching until you do.  
00:05:05: Most people don't realize that models  
00:05:06: are entirely capable of doing this sort  
00:05:08: of thing for you and essentially acting  
00:05:09: as you know an extension of yourself. So  
00:05:11: it's starting off by searching for meal  
00:05:13: prep delivery companies downtown  
00:05:14: Vancouver BC 2025. If I were doing this  
00:05:16: on my own, this is probably something  
00:05:18: that I would do as well, right? like  
00:05:19: very straightforward and logical. You  
00:05:21: don't need to know how the IDE that I'm  
00:05:23: using uh works. You don't need to  
00:05:25: understand the interface or everything.  
00:05:26: I'm going to cover all this later on in  
00:05:28: the course. And as you can see, it's  
00:05:30: found me a bunch of meal preparation  
00:05:32: services. There's Fresh Prep, Two Guys  
00:05:34: with Knives, Crave Healthy, Fed, Fresh  
00:05:37: in Your Fridge, K-Bop, and then WellFed.  
00:05:39: Now, it's finding email addresses of  
00:05:41: each of these. So, as you can see, it's  
00:05:42: actually simultaneously running a bunch  
00:05:44: of searches on their websites to look  
00:05:46: for email addresses or contact methods.  
00:05:48: A few seconds later, it looks like it  
00:05:50: could only find one email out of the  
00:05:52: four or five searches that it ran. So,  
00:05:53: what is it doing instead? It's now  
00:05:55: broadening its search. It's going on  
00:05:56: contact pages. It's looking for  
00:05:58: alternative solutions. Okay, it's now  
00:06:00: accumulated the email addresses and like  
00:06:01: a temporary database. And it's just  
00:06:03: going through and sending emails. It  
00:06:05: does so through uh what's called an MCP,  
00:06:07: model contact protocol server that I've  
00:06:08: set up. I'll show that to you later. And  
00:06:10: boom. Now, it is done. So, we've sent  
00:06:12: five emails. Down here, you can see it  
00:06:14: said, "I asked each company about custom  
00:06:16: meal plans, pricing for higher volume  
00:06:18: orders, and their delivery schedule to  
00:06:19: downtown Vancouver." We also included  
00:06:21: the requirements. I went through and I  
00:06:23: actually found the email that it sent.  
00:06:24: It was something like this. Hey, company  
00:06:27: team, I'm looking for a meal prep  
00:06:29: service that delivers to downtown  
00:06:30: Vancouver and that contains the  
00:06:32: following requirements. Daily calories  
00:06:34: approximately 3500. Daily protein  
00:06:36: approximately this much. Focus on whole  
00:06:38: foods and healthy ingredients.  
00:06:39: Interested in learning more? Do you mind  
00:06:41: letting me know? you know, if you guys  
00:06:42: offer custom meal plans, um, what your  
00:06:45: pricing looks like and how your delivery  
00:06:47: schedule works. Looking forward to  
00:06:48: hearing from you. Thank you very much.  
00:06:50: So, I mean, like, this is something I  
00:06:51: realistically probably would have sent  
00:06:53: myself. Um, is it in my exact tone of  
00:06:55: voice, honestly? Like, it's really  
00:06:56: close. This is more or less everything  
00:06:58: that I would send. There's no AI isms.  
00:07:00: People on the other end of the line  
00:07:01: aren't going to know that I'm using AI  
00:07:02: to do this sort of thing. And it turned  
00:07:03: a process that realistically would have  
00:07:05: previously taken me maybe like 20  
00:07:06: minutes into something that took me  
00:07:08: literally less than 15 seconds. I mean,  
00:07:10: I wrote the thing, I pressed enter, and  
00:07:12: then I went. And what you'll see is with  
00:07:14: the use of other bandwidth improving  
00:07:16: tools like voice transcription and stuff  
00:07:17: like this, you can actually have agentic  
00:07:20: workflows become more or less your  
00:07:22: interface for the internet. And I should  
00:07:24: note that I didn't even use a defined  
00:07:25: agentic workflow for this. I literally  
00:07:26: just asked an agent to do something and  
00:07:28: it was super unstructured and it still  
00:07:29: did a great job. Imagine when we wrap  
00:07:31: this in the framework. I also want to  
00:07:33: cover this idea of a river of value. The  
00:07:35: way I see the global economy is as a  
00:07:38: giant river. Okay. Now, capital flows to  
00:07:42: whoever provides value. And essentially  
00:07:44: what occurs is for many centuries that  
00:07:46: value has come from human labor,  
00:07:48: primarily physical to start, although  
00:07:50: eventually cognitive. And then the more  
00:07:53: value that people could produce, the  
00:07:55: more downstream little tributaries of  
00:07:57: this river we found. And so this might  
00:07:59: be some person that's producing  
00:08:01: tremendous value, these might be other  
00:08:03: people and so on and so forth. The whole  
00:08:05: idea of capital is that as solutions  
00:08:08: arrive in the economy that are more and  
00:08:10: more effective, [gasps] they produce  
00:08:12: larger diversions of this stream. Okay?  
00:08:16: And so let's say this person Z is using  
00:08:19: agentic workflows. The idea is over the  
00:08:21: course of the next few years, he or she  
00:08:23: is going to consume more and more and  
00:08:25: more and more and more of that river  
00:08:27: until essentially he's getting all of  
00:08:30: it. Those who position themselves as  
00:08:32: people like Z in this case will capture  
00:08:35: massive flows from the future economy  
00:08:37: because agentic workflows aren't  
00:08:39: optional. There's something that are  
00:08:40: coming and being deployed right now. The  
00:08:43: last thing I want to talk about is  
00:08:44: automation in the terms of a Gentic  
00:08:47: workflow. Now, a lot of people that  
00:08:49: watch my channel and are probably here  
00:08:51: are familiar with the idea of  
00:08:52: automation. They're also familiar with  
00:08:54: the idea of roles and they've heard a  
00:08:57: lot of things about how AI agents are  
00:08:59: coming and their whole fleets of teams  
00:09:01: that are being replaced and so on and so  
00:09:03: forth. And this is kind of inaccurate.  
00:09:06: Rather than thinking about agentic  
00:09:07: workflows, which is what we're going to  
00:09:08: cover in this course, as being able to  
00:09:10: automate 100% of one role, I want you to  
00:09:14: think about it a little differently. I  
00:09:15: want you to think about agentic  
00:09:16: workflows as being capable of automating  
00:09:18: 90% of 10,000 roles. So as opposed to  
00:09:22: automating 100% okay of one, we're  
00:09:27: automating say 90% of 10,000 people in  
00:09:31: the organization. Now if you automate  
00:09:33: 100% of one role, that's actually pretty  
00:09:35: valuable. Don't get me wrong. If I could  
00:09:36: automate a software developer completely  
00:09:38: end to end, if I could automate a  
00:09:40: marketer end to end, obviously that  
00:09:41: produces some value in my organization.  
00:09:43: But agentic workflows, like a lot of  
00:09:45: technology, have gaps. And so, um, the  
00:09:48: main issue is human beings tend to  
00:09:49: always have a little bit more context  
00:09:51: than these things do, at least right  
00:09:53: now. And so, even the ability to  
00:09:55: automate 90% of 10,000, despite the fact  
00:09:57: that it's not 100, is still tremendously  
00:09:59: valuable. If you just do the math,  
00:10:01: automating 100% of one person's role is  
00:10:03: equivalent to basically providing one  
00:10:05: unit of economic value. Whereas, if you  
00:10:07: automate 90% of 10,000 people's, you're  
00:10:09: providing 9,000 units of economic value.  
00:10:12: As long as you structure your companies  
00:10:13: in a way to accommodate these things,  
00:10:15: these things are very powerful. Now, I  
00:10:17: call this horizontal leverage and it's  
00:10:19: very, very strong. Another way I want  
00:10:21: you to think about this is like the  
00:10:23: industrial revolution. Back in the good  
00:10:25: old days, well, I don't know if they  
00:10:27: were really good, but certainly back in  
00:10:28: the day, you had people like  
00:10:30: seamstresses who would, you know, knit  
00:10:32: various garments and stitch various  
00:10:34: things together. And maybe one of these  
00:10:36: seamstresses could produce, you know, 10  
00:10:38: pairs of a specific type of clothing per  
00:10:41: day. Well, after the industrial  
00:10:43: revolution, obviously we didn't do a lot  
00:10:44: of this stuff by hand anymore. We had  
00:10:46: machines that did this stuff instead. So  
00:10:48: maybe a loom. Before a single seamstress  
00:10:51: could produce maybe 10 garments a day.  
00:10:53: After one of these machines could maybe  
00:10:55: prepare 10,000 garments in a day. That  
00:10:58: said, it the machine didn't fully  
00:11:00: replace that seamstress because that  
00:11:02: seamstress just transitioned. Instead of  
00:11:04: being somebody that worked with their  
00:11:05: hands on building the garment directly,  
00:11:08: they instead became somebody that was  
00:11:10: supervising whole fleets of machines  
00:11:11: that did it. Now imagine if in this  
00:11:14: analogy, not only can we build and use a  
00:11:16: loom, we are capable of rebuilding that  
00:11:18: loom in any configuration in seconds. We  
00:11:21: don't have to, you know, smelt the metal  
00:11:23: and then hammer it and then construct it  
00:11:26: in a way and screw gears and all that  
00:11:28: stuff in order to build a machine. We  
00:11:30: could literally just use natural  
00:11:32: language. Obviously, that would be a lot  
00:11:34: more powerful, right? Well, that really  
00:11:35: is the idea of an agentic workflow. It  
00:11:38: is something that provides incredible  
00:11:39: horizontal leverage and we can  
00:11:41: reconfigure it in seconds to do more or  
00:11:43: less whatever we want. And it's not an  
00:11:45: exaggeration to tell you that this is a  
00:11:47: phase change essentially in a company's  
00:11:50: ability to automate things. So if you  
00:11:53: guys are familiar with automation  
00:11:54: platforms, in this case this is N8N,  
00:11:57: you'll know that most of the time the  
00:11:59: way that we are currently building  
00:12:00: automated systems is through drag and  
00:12:03: drop nodes or modules. And so on the  
00:12:05: left hand side here, I have a simple  
00:12:07: system set up. I'm not going to go  
00:12:08: through everything because it's  
00:12:09: pointless. The point is not to learn a  
00:12:11: specific automation platform. The point  
00:12:12: is to learn how to automate platforms in  
00:12:14: general, but I have a specific  
00:12:15: automation here that just responds to  
00:12:17: some emails coming in for a cold email  
00:12:19: campaign. And as you see here, we have  
00:12:21: these nodes and they do various things.  
00:12:23: Some of them do HTTP requests. Some of  
00:12:24: them do some data processing and and  
00:12:26: formatting. Some of them call a Google  
00:12:28: sheet. We have some AI functionality and  
00:12:30: so on and so forth. They're all  
00:12:31: connected with these lines, which is  
00:12:33: basically the the flow of logic through  
00:12:35: a system. And this is hunky dory. It  
00:12:37: works really well. Well, the new version  
00:12:40: of that workflow on the left, which  
00:12:42: obviously requires a lot of time,  
00:12:45: energy, and understanding in order to be  
00:12:46: able to to parse and then change is what  
00:12:49: we have on the right. Instead of dealing  
00:12:51: with nodes and specific software  
00:12:53: platforms, we use the universal  
00:12:56: translation, which is natural language,  
00:12:58: and then just write it out in bullet  
00:13:00: points. So on the right hand side I have  
00:13:02: the exact same workflow except I have it  
00:13:04: set for agentic uh systems and all it is  
00:13:08: is a list of bullet points. Hey when  
00:13:10: somebody replies to one of your cold  
00:13:11: outreach campaigns instantly should send  
00:13:12: a web hook. The system should look up  
00:13:14: the campaign in a Google sheet to find  
00:13:16: talking points and example replies. It  
00:13:18: should then research the person who  
00:13:19: replied. It should then generate a short  
00:13:21: friendly reply. If they said something  
00:13:23: negative like unsubscribe or remove me,  
00:13:24: we should skip them. If there's no  
00:13:26: knowledge base, we should skip them.  
00:13:27: Otherwise, we should send the reply  
00:13:29: automatically. I want you guys to see  
00:13:31: that on the left hand side, we had to  
00:13:33: spend months, maybe years, becoming  
00:13:34: skilled enough to use a platform to be  
00:13:36: able to build systems that did this. And  
00:13:38: on the right, a toddler who has a a  
00:13:41: rough idea in mind of what he or she  
00:13:43: wants to do can write it out in natural  
00:13:44: language. And not only can everybody  
00:13:46: else on a team interpret that, we can  
00:13:48: also change that at any point. If I  
00:13:50: wanted to add an additional step to my  
00:13:51: workflow, all I do is I click click on  
00:13:54: this, press enter, and then just write  
00:13:55: it out. and the agentic workflow builder  
00:13:57: and then eventually doer using a  
00:13:59: framework I'm going to run you guys  
00:14:00: through later on in this course will do  
00:14:02: it and it'll do it extraordinarily  
00:14:03: remarkably well. So that's a very  
00:14:05: fundamental change in how these things  
00:14:07: work and hopefully it's clear to  
00:14:08: everybody here that workflows are no  
00:14:10: longer drag and drop sort of builds in  
00:14:13: the concept that we see on the left hand  
00:14:15: side. They're very much so just like  
00:14:17: basic logic. So why is all of this stuff  
00:14:20: possible right now? It certainly wasn't  
00:14:22: just a little while ago. Well, there are  
00:14:24: three main reasons. intelligence, tools,  
00:14:27: and cost. On the intelligence side,  
00:14:30: model intelligence just crossed a  
00:14:32: threshold and became very, very good,  
00:14:34: seemingly overnight, but really we've  
00:14:36: been working up to it for quite a while.  
00:14:38: Frontier models like Anthropics Claude,  
00:14:40: OpenAs, Chat, GBT, Google's Gemini, and  
00:14:42: then a bunch of other ones have gotten  
00:14:44: really smart. They score around 80% on a  
00:14:48: benchmark called software engineering  
00:14:49: bench verified. And this measures real  
00:14:51: software engineering ability. This is  
00:14:53: not a crappy cherrypicked demo. It  
00:14:56: wasn't included in like the training  
00:14:58: data or anything like that. These are  
00:15:00: novel problems that are being solved in  
00:15:01: novel ways through models. And  
00:15:03: essentially, they are genuine  
00:15:04: professional grade work that are better  
00:15:07: than most software engineers. Now, I  
00:15:09: would have considered myself a software  
00:15:11: engineer a couple of years ago. I'd say  
00:15:12: my skills have definitely uh  
00:15:14: deteriorated a fair amount since because  
00:15:16: I've been focusing more on no code tools  
00:15:17: and and making money and stuff like  
00:15:18: that. But this stuff is so far beyond my  
00:15:21: own abilities as sort of like a  
00:15:23: mid-level dev u that it's not even  
00:15:25: funny. Most people that learn about this  
00:15:27: and they're going to be learning about  
00:15:28: it pretty soon will think that AI went  
00:15:30: from, you know, intern level to some  
00:15:32: sort of senior employee overnight. But  
00:15:34: this is just how knowledge works.  
00:15:37: Basically, anytime that you have a  
00:15:39: process and that process slowly gets  
00:15:41: better and better and better over time,  
00:15:42: most people don't see until we hit a  
00:15:45: certain threshold and then it almost  
00:15:47: looks like it went vertical. In reality,  
00:15:49: uh it's almost like the way that boiling  
00:15:51: water works, right? The temperature of  
00:15:53: water goes up and up and up and up and  
00:15:54: up and then eventually it boils and then  
00:15:56: it fundamentally changes state. You  
00:15:58: know, it goes from over here where it's  
00:16:00: like a liquid to over here where it's a  
00:16:02: a gas. And although we're supplying more  
00:16:05: and more energy to this thing, we're not  
00:16:07: really seeing it change until all of a  
00:16:08: sudden, boom, it's producing bubbles and  
00:16:10: getting all over the place. So, I see  
00:16:12: model intelligence a very, very similar  
00:16:14: way. So, a lot of people talk about  
00:16:16: benchmarks. Very few people actually  
00:16:18: show what the questions inside of a  
00:16:20: benchmark realistically ask. I think  
00:16:22: benchmarks are for the most part pretty  
00:16:23: artificial. A much better test of how  
00:16:26: good a model is is just how good you  
00:16:27: feel while using it. But it is important  
00:16:29: that at least we understand how  
00:16:31: benchmarks work in order for us to  
00:16:32: really put in context the capabilities  
00:16:34: of agents. So here's uh one from  
00:16:36: Astropi. It's a misleading exception  
00:16:39: message. And basically, these models are  
00:16:41: so good at coding. Like, like, I mean, I  
00:16:43: tried to look through and understand  
00:16:44: what any of these actual questions meant  
00:16:46: and how to fix them. I'd probably be  
00:16:48: staring at each of these for like a day  
00:16:50: before anything makes sense. Um, let  
00:16:52: alone before I get to the point where I  
00:16:53: could realistically solve it. These  
00:16:55: models can do this sort of thing in in  
00:16:56: seconds. So, issue problem statement.  
00:16:58: Hey, removing a required column from a  
00:17:00: time series raises a misleading error  
00:17:01: message. The error claims the time  
00:17:03: column is missing even when it's  
00:17:04: present. Instead, the error should list  
00:17:06: all missing required columns. Then it  
00:17:08: gives you a snippet of code with the  
00:17:09: actual class time series. Right? So  
00:17:11: looking at that, no idea what the hell  
00:17:13: that does. The bug, if flux is missing,  
00:17:15: error still complains about time. Error  
00:17:17: message is factually incorrect. You're  
00:17:18: fix detect which required columns are  
00:17:20: missing. Report them explicitly. So you  
00:17:22: actually have to go through and you have  
00:17:23: to do this with the code. Okay, here's  
00:17:25: one from sort of like a Panda style  
00:17:27: question. Load CSV silently coerces  
00:17:30: mixtype columns instead of failing  
00:17:31: quickly which leads to incorrect  
00:17:32: downstream computations and then it like  
00:17:34: provides a list. So, we now have models  
00:17:36: that are basically capable of looking at  
00:17:38: a thousand of these and solving more  
00:17:42: than 800 of them perfectly. I mean, if  
00:17:45: you gave me a thousand of these, not  
00:17:46: only would I take like a year, I would  
00:17:49: probably get at least, you know, 50% of  
00:17:51: these things wrong. And I'm somebody  
00:17:53: that has some exposure to this sort of  
00:17:54: stuff. Imagine the average person. And  
00:17:57: so what I mean to say is that we are  
00:17:58: essentially empowering every human being  
00:18:01: on earth or at least we have the  
00:18:03: potential to empower if we were to  
00:18:04: actually distribute this technology and  
00:18:06: if everybody were to know it to the  
00:18:08: level that you will know it by the end  
00:18:09: of this course with the powers of like a  
00:18:11: mid-level to even senior developer in  
00:18:14: many cases. Another important point is  
00:18:16: how fast these models can operate. I  
00:18:19: mean this is me asking chat GPT 5.2  
00:18:21: thinking to just reason a little bit  
00:18:22: about the meaning of life. Check out the  
00:18:24: stream of output that it's providing.  
00:18:26: But you can go way faster than that.  
00:18:28: This is an example of a diffusion LLM  
00:18:30: that it basically immediately processes  
00:18:32: and writes I don't know how many hundred  
00:18:34: words, but extraordinarily quickly. You  
00:18:36: see that we just click generate and then  
00:18:37: immediately after, you know, probably at  
00:18:40: least 300 words for instantiated. These  
00:18:42: models can run these reasoning loops  
00:18:44: extremely quickly behind closed doors.  
00:18:46: In addition, providers like uh Anthropic  
00:18:48: and OpenAI and Gemini and stuff have all  
00:18:50: the compute necessary to run these  
00:18:51: things like 10, 50, 100 times faster  
00:18:54: than you are yourself. So just imagine  
00:18:56: what's going to happen when that level  
00:18:58: of technology drips down to the rest of  
00:19:00: the economy. Like to be clear, these  
00:19:02: models, the ones that I'm using to build  
00:19:03: agentic workflows, are already extremely  
00:19:05: powerful and have automated the vast  
00:19:07: majority of my day-to-day work. They can  
00:19:09: automate the vast majority of your  
00:19:10: day-to-day work as well or any of the  
00:19:12: companies that you work with. But  
00:19:13: imagine the models in 3 months. Imagine  
00:19:15: the models in a year from now. That's  
00:19:17: why learning how to build these sorts of  
00:19:19: workflows today is probably one of the  
00:19:20: highest ROI skills that you can engage  
00:19:22: in. The second thing is tool integration  
00:19:25: is now standardized. So there's some  
00:19:26: protocols out there like model context  
00:19:28: protocol which standardizes how AI  
00:19:31: connects to external tools, databases,  
00:19:33: resources, and stuff like that. I'm  
00:19:34: going to be showing you guys how to use  
00:19:36: model context protocol in pretty  
00:19:37: advanced ways that I don't think a lot  
00:19:38: of other people have covered in this  
00:19:40: course. I'm also going to be talking  
00:19:41: about some of the downsides of model  
00:19:43: context protocol like how initially it  
00:19:45: totally blew but now it's uh actually  
00:19:47: pretty good and well supported so it's  
00:19:48: it's worth us diving in. In addition to  
00:19:51: you know those tools through MCP there  
00:19:53: also some frameworks that have recently  
00:19:55: come out. One is directive orchestration  
00:19:57: execution. This is the framework I'm  
00:19:59: going to be using to build and then use  
00:20:00: our agentic workflows throughout the  
00:20:02: course. There are also platform specific  
00:20:04: frameworks like cloud skills for the  
00:20:05: cloud family of models. these formalize  
00:20:08: tool calling and you know in case you  
00:20:10: have no idea what I'm talking about here  
00:20:11: LLM are really flexible okay which is a  
00:20:13: great thing conceptually it's great if  
00:20:15: you want to write poems and write do  
00:20:16: creative writing and help you respond to  
00:20:18: emails and stuff like that but a lot of  
00:20:20: business functions don't depend on  
00:20:22: flexibility what they depend on is the  
00:20:24: opposite they depend on reliability so  
00:20:27: in business we need to standardize and  
00:20:29: tools are basically just standardized  
00:20:31: little things that we can use in order  
00:20:32: to accomplish business tasks I like  
00:20:35: thinking of it like a caveman that you  
00:20:36: know, is hunting saber-tooth tigers or  
00:20:38: something. If you're a caveman and  
00:20:40: you're hunting saber-tooth tigers, and  
00:20:42: every time you go to a saber-tooth  
00:20:43: tiger, you're completely empty-handed,  
00:20:45: what are you going to do? The first  
00:20:46: thing you're going to do is you're going  
00:20:47: to be like, "Holy crap, is that a  
00:20:48: saber-tooth tiger?" You're going to  
00:20:49: scrge around on the ground to look for  
00:20:51: rocks and pointy stabby things and, you  
00:20:53: know, sticks and anything that can buy  
00:20:55: you some distance and then maybe some  
00:20:56: effectiveness. Contrast that with if  
00:20:59: before you had a little bit of foresight  
00:21:01: and you said, "Hm, I should probably  
00:21:02: build something that's kind of pointy  
00:21:04: and sharp." Huh? So, you you work all  
00:21:06: day and night and you put together a  
00:21:07: spear. Well, every time you encounter  
00:21:09: that problem of the saber-tooth tiger,  
00:21:11: okay, what are you going to do? You're  
00:21:12: just going to pick up your spear and  
00:21:13: deal with it. Just my really crappy  
00:21:16: drawn spear. That's sort of the same  
00:21:17: thing that LLMs use tools for. They  
00:21:20: encounter problems. When they encounter  
00:21:22: them a few times, they then develop  
00:21:24: tools that solve them or use  
00:21:25: pre-existing ones through MCP. And then  
00:21:27: in doing so, we can standardize the  
00:21:29: solving of business problems pretty  
00:21:30: easily.  
00:21:32: Okay. The last thing is just cost  
00:21:33: economics and they finally make sense.  
00:21:36: When Claude Opus 4.5 dropped, it went  
00:21:38: from a cost of about $15 or $75  
00:21:41: depending on input or output per 1  
00:21:43: million tokens to five or $25 depending  
00:21:46: on input or output for 1 million tokens.  
00:21:48: That's a 3x reduction. And newer models  
00:21:50: are even cheaper than that. The cost of  
00:21:52: intelligence per like effectiveness has  
00:21:54: plunged something like 40% in the last  
00:21:56: year. If I were to graph this, it would  
00:21:58: actually look like this. Now, I've been  
00:22:00: using models since GPT3, way back in  
00:22:02: 2020 when it was um initially released  
00:22:05: with a very small, you know, select  
00:22:07: group of people that could access it and  
00:22:08: so on and so forth. GPT3, which is, I  
00:22:12: mean, orders upon orders upon orders of  
00:22:14: magnitude dumber than this, costs more  
00:22:17: than this technology that we are dealing  
00:22:18: with right now. It is insane how quickly  
00:22:21: the price of knowledge work has  
00:22:22: plummeted. It's already gone down 40  
00:22:25: times in just the last year. I imagine  
00:22:26: it'll probably go down another 40 times  
00:22:28: over the course of the next year, maybe  
00:22:29: even more. What that means is we can  
00:22:32: actually send large volumes of tokens to  
00:22:33: these things to replace the work of like  
00:22:36: deterministic um old school automations  
00:22:38: like the NAN flow that I showed you  
00:22:40: without it running a business ragged  
00:22:41: into the ground. There are also tons of  
00:22:43: price wars that are occurring between  
00:22:45: major providers and there's a lot of  
00:22:46: like geopolitical incentives between,  
00:22:48: you know, places in the east and then  
00:22:49: places in the west um to basically make  
00:22:51: these things as accessible and easily to  
00:22:53: use as possible. So to make a long story  
00:22:55: short, this is new. Very few people  
00:22:58: understand the capabilities right now.  
00:23:00: So there are many billions of dollars  
00:23:02: that will shift as the market learns and  
00:23:03: adapts. It is much better to be an early  
00:23:06: mover than somebody that is affected by  
00:23:08: this technology uh without their consent  
00:23:10: or knowingness. What I mean is would you  
00:23:13: rather learn about this stuff now or  
00:23:14: would you rather learn about it in 2  
00:23:16: years when your boss or I don't know  
00:23:18: some some client base of yours turns to  
00:23:20: you and says hey we no longer need you  
00:23:21: because we have aic workflows to do it.  
00:23:23: I would much rather be the person that  
00:23:25: helps them build those agentic workflows  
00:23:27: than I'd be the person that's now  
00:23:28: sitting on my ass because I don't know  
00:23:30: anything about them. Hopefully, you are  
00:23:31: too. Okay, so now that that big  
00:23:33: preamble's out of the way, let's learn  
00:23:34: about chat bots, agents, agentic  
00:23:36: workflows, uh, knowledge tools, and then  
00:23:38: actually get our hands dirty with some  
00:23:40: demos. I like thinking about knowledge  
00:23:41: tools as evolving over the course of the  
00:23:44: last 30, 40 or 50 years. I always think  
00:23:47: about it sort of like the step ladder on  
00:23:49: the right where you have three rungs. At  
00:23:52: the bottom you have documents. In the  
00:23:54: middle you have chats and at the top you  
00:23:58: have agents. Over the course of the last  
00:24:00: 30 40 50 years we basically transition  
00:24:02: from knowledge in the form of docs to  
00:24:05: knowledge in the form of chats over the  
00:24:06: last 5 years to knowledge and action in  
00:24:08: the form of agents. And I'm going to run  
00:24:10: you through what each of these look like  
00:24:11: now before actually using them in a real  
00:24:13: workflow. So documents are static  
00:24:15: knowledge. Hopefully they're pretty  
00:24:16: straightforward. It's oneway information  
00:24:18: flow. All you do is you read the  
00:24:20: document, but it's not like the document  
00:24:22: can respond to you. We currently use  
00:24:24: documents everywhere in school and in  
00:24:25: business. We use them in legal  
00:24:26: agreements. We use them in training  
00:24:28: materials. Once you write a document, it  
00:24:29: obviously stays fixed. That's a feature,  
00:24:31: not a bug, because it's great for  
00:24:33: permanence. Like if you're writing  
00:24:34: contracts or standard operating  
00:24:36: procedures that are immutable, aka it  
00:24:38: should not change. You don't want your  
00:24:39: contract or your standard operating  
00:24:41: procedure rewriting itself unless you  
00:24:42: want it to, right? In most cases, you  
00:24:44: don't. So, u that's great. That's  
00:24:45: actually a feature, not a bug. Chat  
00:24:47: bots, on the other hand, are not static.  
00:24:48: They are dynamic. Chat bots were  
00:24:50: developed realistically way back in the  
00:24:52: 1970s, but we were only starting to use  
00:24:54: them for real knowledge purposes and  
00:24:56: maybe like the early 2020s. And they  
00:24:58: perform two-way interaction. You read  
00:25:00: the output, but you can also ask  
00:25:02: questions back. So, here's a crappy pass  
00:25:04: to GPT40 where I just said, "Hey, what's  
00:25:07: up? Hey, Nick. All good on my end. Quick  
00:25:08: check-in. Zero fluff. I'm ready to help  
00:25:10: if you want to chat. If you got a  
00:25:11: decision to make, whatever. What's on  
00:25:12: your mind?" This is now two-way  
00:25:14: knowledge interaction. the dreaded  
00:25:16: mdash. Um, this allows you to do things  
00:25:18: like clarify confusing points. You can  
00:25:20: ask for research. You can dig deeper  
00:25:22: into topics. You can also modify the  
00:25:24: knowledge. So, you could upload, you  
00:25:25: know, a PDF or you could make some  
00:25:26: statement and then the chatbot now has  
00:25:28: some additional context. Uh, I just  
00:25:30: think of it like really smart colleagues  
00:25:32: who read everything you give them, but  
00:25:33: then they're also confined to a chair.  
00:25:35: You know, they can't move and they can't  
00:25:36: do anything with it. So, essentially all  
00:25:37: you can do is is talk. This is how most  
00:25:40: people treat models today as chat bots.  
00:25:42: They're dynamic knowledge, but they're  
00:25:43: still subject to this little window.  
00:25:45: They can only be communicated with and  
00:25:47: copied and pasted through your chatgbt  
00:25:49: or through your cloud output. Now,  
00:25:50: contrast that with agents, which I  
00:25:52: consider to be dynamic action. To make a  
00:25:54: long story short, this is two-way  
00:25:56: interaction, just like chat bots, except  
00:25:57: this time it acts. On the right hand  
00:25:59: side here, you can see I have a flow  
00:26:01: that says run the thumbnail generator on  
00:26:02: a link. So, it's not just asking it a  
00:26:05: question about the thumbnail generator,  
00:26:06: and I'm actually having it do something.  
00:26:07: And this is a real agentic workflow that  
00:26:09: I developed to basically build YouTube  
00:26:10: thumbnails like what you guys saw on my  
00:26:12: channel. What we see here is a  
00:26:14: fundamentally different interface. On  
00:26:15: the left hand side, we have some of  
00:26:17: these nodes. Green ones here are actions  
00:26:19: that are being taken. These gray little  
00:26:21: sections over here are thinking nodes,  
00:26:23: which are where the model reasons um  
00:26:25: extemporaneously, basically temporarily,  
00:26:27: and then discards these reasoning  
00:26:28: tokens. You can see that it's actually  
00:26:30: calling a script. You don't need to know  
00:26:31: Python in order to like have the model  
00:26:33: do really cool things for you, but  
00:26:34: that's what's happening right here. And  
00:26:35: then down over here we have a bash  
00:26:36: output where it's actually ran. We have  
00:26:38: an output that we can then use and so on  
00:26:40: and so forth. So you're given visibility  
00:26:42: into the reasoning. You're also given  
00:26:43: visibility into the um planning tool  
00:26:46: memory reasoning and then observation  
00:26:48: loop. And I'm going to cover exactly  
00:26:50: what that looks like in a moment. You  
00:26:52: also have autonomy, long execution  
00:26:53: times. Agents can routinely run for 5 or  
00:26:55: 10 minutes. Now yesterday night I  
00:26:57: actually had an agent run for over 5  
00:26:58: hours uninterrupted to build me a really  
00:27:00: cool system. As of today I think of  
00:27:02: models like a mid-tier developer.  
00:27:04: They're 100K a year or so in terms of  
00:27:06: their like capability. But if you think  
00:27:07: about it, I'm spending 20 bucks a month  
00:27:10: for this, which is 240 bucks a year,  
00:27:12: which is over 400 times cheaper. And not  
00:27:14: only is it cheaper, this thing works 24  
00:27:16: hours a day, as I mentioned, or it can  
00:27:17: work 24 hours a day. You can do a lot of  
00:27:19: really cool things with models like  
00:27:20: this. So now is the time to jump on it.  
00:27:22: A point to understand is that an agent  
00:27:24: is not a chatbot, despite the fact that  
00:27:25: they look really similar, right? Now,  
00:27:27: the way I see chat bots is like a chat  
00:27:29: is just an interface, right? It's just  
00:27:31: some specific thing with messages that  
00:27:33: go back and forth and then a little  
00:27:34: window down here where you can enter in  
00:27:36: your own information. The chat is just  
00:27:38: like the app. The agent is what lives  
00:27:40: inside of the app. If you guys are  
00:27:42: familiar with crustaceians or crabs or  
00:27:44: um I don't know, like cute little things  
00:27:46: that crawl around on the ocean subfloor.  
00:27:48: They often will have fine shells and  
00:27:51: then um discard them when they no longer  
00:27:53: fit their purpose. Right? So, like a  
00:27:55: crustation that uses the shell of an  
00:27:57: older animal, an agent is just currently  
00:27:59: using the interface of an older type of  
00:28:01: knowledge tool, the chatbot. And I'm  
00:28:03: sure over the course of the next few  
00:28:04: years, it's going to discard this and  
00:28:05: we're going to have new interfaces that  
00:28:06: are even better. Okay, so let me show  
00:28:07: you guys just the difference between  
00:28:09: chat bots and then a really low-level  
00:28:10: agentic workflow that I put together  
00:28:12: that functions through an agent. Um,  
00:28:13: down over here is a chat GPT desktop  
00:28:15: app. This is really simple and easy. You  
00:28:17: can download it on chatbt's website.  
00:28:18: Super straightforward. I'm just going to  
00:28:20: say um hey, how can I scrape, you know,  
00:28:23: leads from LinkedIn Sales Navigator. So,  
00:28:27: when you're working with models like  
00:28:28: this, the input and output is pretty  
00:28:30: bounded, right? All you can really do is  
00:28:32: you could just see what this model tells  
00:28:34: us. Hey, you know, here's the direct  
00:28:36: high IQ zero fluff rundown. Use this,  
00:28:39: scrape this,  
00:28:42: use this. This is cool, right? I mean,  
00:28:44: it's nice that we're getting information  
00:28:45: on how to do this. And you know a few  
00:28:46: years ago this would have been  
00:28:47: revolutionary. Rather than just have a  
00:28:49: conversation with the model and ask it  
00:28:50: how to do things which is knowledge. I  
00:28:52: can actually force a model to action  
00:28:54: using agentic workflows. So in this case  
00:28:56: I'm saying scrape me 200 HVAC owners in  
00:28:58: the US. I want decision makers. It then  
00:29:01: checks to see if there are lead scraping  
00:29:02: directives and execution scripts. This  
00:29:04: is just part of the framework that helps  
00:29:06: constrain the model's output which I've  
00:29:08: run you guys through a little bit more  
00:29:09: later. It's then going through and  
00:29:11: actually pulling a script together to do  
00:29:13: this thing for me. It then comes up with  
00:29:15: this idea of a test scrape, 25 leads.  
00:29:17: It's then going to verify some industry  
00:29:19: match, run the full scrape, upload to  
00:29:21: Google sheet, and then even go through  
00:29:22: and enrich it for me. In this case, the  
00:29:24: model is performing a search. It's then  
00:29:26: comparing the results of the search with  
00:29:27: what it is that it thinks that I want.  
00:29:29: It's determining that there's a very low  
00:29:31: match rate. And so, it's now adjusting  
00:29:32: its filters on the fly completely on its  
00:29:35: own to find leads with zero input. All  
00:29:38: I'm doing here is texting a friend of  
00:29:39: mine on my phone.  
00:29:42: It's then verified, past threshold. Now  
00:29:44: it's running a full scrape. It then went  
00:29:46: and it actually got us a Google sheet  
00:29:47: with all that information. I mean, it's  
00:29:49: pretty cool in so far that it's totally  
00:29:50: autonomous. It probably would have taken  
00:29:52: me a fair amount of time to come up with  
00:29:53: the filters and so on and so forth  
00:29:54: myself. This thing just did it entirely  
00:29:55: on its own. If you guys check the bottom  
00:29:57: right, we actually ended up getting  
00:29:58: almost 200 emails directly from this. We  
00:30:00: also got a bunch of phone numbers and a  
00:30:01: bunch of other really personal  
00:30:02: information. So, what exactly is going  
00:30:04: on? There are five steps that an agent  
00:30:05: will follow every single time you send  
00:30:07: or receive a message. The first is  
00:30:09: planning. The next is tools. The third  
00:30:10: is memory. The fourth is reflection. And  
00:30:12: the fifth is orchestration. I think I  
00:30:14: called it observation before. My bad on  
00:30:16: that. But orchestration. I use a simple  
00:30:18: fiveletter acronym for this. Just pt  
00:30:20: mro. Helps me remember it. Hopefully  
00:30:21: it'll help you remember it as well. Now  
00:30:23: these five components are as follows.  
00:30:25: Planning is where you break down  
00:30:26: objectives into executable steps. Tools  
00:30:28: are the actions that an agent actually  
00:30:30: takes in the world. If you guys  
00:30:31: remember, it was calling various things  
00:30:33: to do what it needed to do. They then  
00:30:35: stored things into memory. So this is  
00:30:37: how agents retain and recall information  
00:30:39: across tasks. There different forms of  
00:30:41: memory. There's short-term, midterm,  
00:30:42: long-term, and there's different ways  
00:30:44: that that works within an agent these  
00:30:46: days. I'm I'm going to cover each of  
00:30:47: them. Uh reflection is where the agent  
00:30:49: evaluates and corrects its own work. So,  
00:30:51: as you saw there, we had an issue with  
00:30:52: one of the calls and it went through and  
00:30:54: it fixed the filter. And then finally,  
00:30:56: orchestration, which is where you  
00:30:57: coordinate multiple agents or complex  
00:30:59: workflows. We're going to talk about how  
00:31:00: to do that um later on in the program,  
00:31:02: too. Obviously, there's planning, and  
00:31:04: that's mostly goal decomposition. So,  
00:31:05: it's where a highle objective gets  
00:31:07: broken into subtasks. Um, for instance,  
00:31:09: if your highle task is to eat at White  
00:31:11: Castle, you know, it's not just eat at  
00:31:13: White Castle, right? That's not enough  
00:31:15: to go and actually do the thing. What  
00:31:17: you want to do is you want to break that  
00:31:18: down into various tasks. Like maybe step  
00:31:21: one is we have to um, I don't know, get  
00:31:23: in the car, right? Step two is, and  
00:31:26: maybe you do this while you're in the  
00:31:27: car, you do this before, you got to  
00:31:29: research the um, GPS location. You know,  
00:31:32: the third is you have to drive all the  
00:31:34: way over there.  
00:31:36: And then the fourth is you actually have  
00:31:37: to order. And the fifth is you have to  
00:31:40: make a movie about it. Just kidding. But  
00:31:42: um the point that I'm making is you know  
00:31:43: you take this high level task and you  
00:31:44: actually break it down. And that is  
00:31:46: occurring every single time within an  
00:31:47: agent. You don't always see it because  
00:31:49: it's typically buried within reasoning  
00:31:51: and most people don't expose reasoning.  
00:31:52: But this form of highle goal  
00:31:54: decomposition occurs all the time. And  
00:31:56: it's important that it does it right  
00:31:57: because if it screws up at the planning  
00:31:59: stages, probability of it being able to  
00:32:01: move and do the rest of the task is very  
00:32:03: low because it's making a foundational  
00:32:04: misassion. Now, an agent will identify  
00:32:06: dependencies within steps. It'll then  
00:32:08: sequence them logically, like I just  
00:32:09: gave you, five steps. Well, the agent  
00:32:11: will actually reverse those steps as  
00:32:12: necessary. And then good planning also  
00:32:14: means revising the plan when things  
00:32:15: change because there's obviously only so  
00:32:17: much information that we have ahead of  
00:32:18: time. There are limitations to this and  
00:32:20: Claude, GPT, Gemini, these have pretty  
00:32:23: imperfect planning capabilities. So, as  
00:32:25: part of the building of the workflows  
00:32:26: that I'm going to show you later, I  
00:32:28: actually recommend doing a fair amount  
00:32:29: of the planning yourself. The reason why  
00:32:31: is because it's sort of um like an  
00:32:33: analogy where if I'm on I don't know  
00:32:36: let's say the east coast of the United  
00:32:37: States and I want to go somewhere on the  
00:32:39: west coast of Africa or something like  
00:32:41: that. Okay, and I'm this ship over here  
00:32:43: and my goal is I want to make it to this  
00:32:45: port right over here. If I screw up at  
00:32:48: the very beginning, okay, even by a few  
00:32:51: percentage points, let's say, okay, and  
00:32:53: I give myself a range of possible  
00:32:55: outcomes here, this range, even if it's  
00:32:57: like a 1% problem with the planning or  
00:32:59: 1% error or something like that, these  
00:33:01: ranges have massive downstream impacts  
00:33:04: over the course of the entirety of the  
00:33:05: task. Like, if I'm really really bad, I  
00:33:08: could end up in the middle of freaking  
00:33:09: nowhere. Or if I'm really, really,  
00:33:10: really bad on this end, I could end up,  
00:33:12: you know, hundreds of kilometers, maybe  
00:33:13: thousands of kilometers away from where  
00:33:15: I wanted to go. So what planning really  
00:33:17: is if you think about it is effective  
00:33:19: planning just reduces those error bars.  
00:33:21: It just allows us to go a lot tighter  
00:33:23: and a lot narrower. So the probability  
00:33:25: of us actually achieving uh the thing we  
00:33:27: want aka going to where we want to go is  
00:33:29: a lot higher. If there was one place for  
00:33:31: you to exert your human intellect, it's  
00:33:33: at the planning stage. And I'll cover  
00:33:34: some practical ways to do that later. Um  
00:33:36: obviously there's DO which helps by  
00:33:38: providing structured directives. I'm  
00:33:40: going to show you guys how you can just  
00:33:41: dump your company SOPs into a model to  
00:33:42: guide its planning. If you guys don't  
00:33:44: have company SOPs, I'm going to show you  
00:33:45: how to reproduce them really simply and  
00:33:46: easily. Next are tools. Now, these turn  
00:33:48: LLMs into systems that are capable of  
00:33:50: real world action. Um, I think I covered  
00:33:52: the caveman analogy, ancient people  
00:33:54: building a spear or something like that,  
00:33:56: but you can also think of it as like an  
00:33:57: ancient person building a house. It's  
00:33:59: like they will build the house the first  
00:34:00: time and the house will be pretty cool,  
00:34:02: you know, might um have most the things  
00:34:03: that they want. I don't know, some sort  
00:34:05: of um straw roof or whatever. And then  
00:34:07: what's really cool is agents can then go  
00:34:09: back to the tools and then make them  
00:34:10: better. So maybe, you know, you want to  
00:34:11: build a window or something like that.  
00:34:13: So the first iteration of the house  
00:34:14: doesn't have a window. Second one has a  
00:34:15: window. The third one has like a door.  
00:34:17: The fourth one has like a cool barbed  
00:34:19: wire security system and so on and so  
00:34:21: forth. But just to break it down, tool  
00:34:22: use is where agents interact with  
00:34:24: systems and services. In our case,  
00:34:27: because we are dealing mostly with  
00:34:28: digital services, that means things like  
00:34:30: calling APIs. Okay, that's a big chunk  
00:34:32: of tool use to be honest. Then executing  
00:34:34: code. You don't need to know any of the  
00:34:35: code. It does the coding for you, but it  
00:34:37: is still executing the code. It also  
00:34:39: nowadays includes a lot of database  
00:34:40: stuff because you don't want to store  
00:34:42: all the information directly in the uh  
00:34:44: context of the model. Then it also means  
00:34:45: things like browsing the web. So if your  
00:34:48: computer was the entire world, right, in  
00:34:50: your case, the tool that you personally  
00:34:52: use to interact with your computer, if  
00:34:54: you think about it, is use your mouse  
00:34:55: and use the keyboard. And some people  
00:34:57: are now using voice transcription tools  
00:34:59: like myself. So that is our input method  
00:35:01: to our world of the computer, right?  
00:35:04: Well, it's the same thing with agents.  
00:35:05: Tools are their input methods to real  
00:35:08: life. They need tools in order to break  
00:35:10: out of that little chatbot, okay, and  
00:35:12: actually influence things that matter.  
00:35:14: So the entirety of the intelligence of  
00:35:16: models in the do directive orchestration  
00:35:19: execution framework in cloud skills in a  
00:35:22: bunch of these different ways of  
00:35:23: thinking about agentic workflows, the  
00:35:25: entire point of the intelligence is just  
00:35:26: to help it use and then build tools. And  
00:35:29: a good analogy is tools are like the  
00:35:31: agents hands. The LLM is the brain. If  
00:35:33: you're a brain and you're in a vat or in  
00:35:34: a jar somewhere, obviously your ability  
00:35:36: to influence the real world is pretty  
00:35:37: limited, right? But you give a brain  
00:35:39: some wires and neurons and some hands or  
00:35:41: whatever and now it can actually start  
00:35:42: doing things. Unfortunately, right now  
00:35:44: tool quality varies a ton. There is a  
00:35:46: lot of variance in like really good and  
00:35:48: really crappy tools. And just a few  
00:35:50: months ago is actually way larger.  
00:35:51: There's way more variance, but we're  
00:35:52: getting better. And I imagine future  
00:35:54: tool systems are going to be mostly  
00:35:56: pretty solid. There's going to be a lot  
00:35:57: less uh uh range between like a really  
00:35:59: good tool and a really bad tool.  
00:36:01: Essentially, um, this is for a variety  
00:36:04: of reasons. MCP came out pretty  
00:36:05: recently, and there are also a lot of  
00:36:07: people trying to capitalize short-term  
00:36:09: on MCP, so they're building a lot of  
00:36:11: really crappy tools. I'll show you guys  
00:36:12: how to avoid that, and also how to  
00:36:13: select like really high quality tools  
00:36:14: that matter, as well as how to build  
00:36:16: your own that are way better. The way I  
00:36:18: see bad tools is it's like if you give  
00:36:19: somebody a really crappy hammer and then  
00:36:21: you expect them to build you like a  
00:36:22: really nice uh cupboard or cabinet or  
00:36:24: something, probability is low, right? If  
00:36:26: you want to build something really cool,  
00:36:27: you need to have cool tools. If you want  
00:36:29: to do something really cool, you  
00:36:30: obviously need to make sure those tools  
00:36:31: are as high quality as humanly possible.  
00:36:34: So, here's one of the key insights of  
00:36:35: Agentic Workflows and one of the reasons  
00:36:36: why I think a lot of people don't  
00:36:37: understand how the stuff works. When you  
00:36:39: standardize tools, okay, and you turn  
00:36:41: them from vague ideas into actual  
00:36:44: concrete functions. You let anybody use  
00:36:48: them, regardless of the type of model  
00:36:50: that you're using, whether it's Claude  
00:36:51: or whether it's chat GBT or whether it's  
00:36:53: Gemini. All of these models are smart  
00:36:55: enough to know how to use the tool. You  
00:36:57: also ensure consistent inputs and  
00:36:58: outputs, which is really, really  
00:37:00: important for business. And the cool  
00:37:01: thing is you don't actually need to wait  
00:37:02: for other people to build them anymore.  
00:37:04: All of these models are hyper optimized  
00:37:06: for programming. So, we're just going to  
00:37:08: let the model build its own tools. LLMs  
00:37:11: are very probabilistic, right? Their  
00:37:13: decision-m process is pretty opaque to  
00:37:15: us. I heard a great quote the other day,  
00:37:17: uh, might have been from Dario Amod,  
00:37:18: might have been from somebody else, but  
00:37:19: it was that AI models are grown. They're  
00:37:22: not built. And I think about that pretty  
00:37:24: often. AI models are just intelligences  
00:37:26: that we are slowly figuring out how uh  
00:37:28: they work under the hood. We don't  
00:37:30: actually know. We don't have an an  
00:37:31: established consistent decision-making  
00:37:33: process that takes us from one to  
00:37:35: wherever we want to go. Business  
00:37:37: requires that you need interpretability.  
00:37:39: You need the ability to audit things and  
00:37:40: so on and so forth. Okay? So rather than  
00:37:42: have this big probabilistic galaxy brain  
00:37:44: which makes decisions in routes in ways  
00:37:46: that we have no idea how, okay, we just  
00:37:48: give it very very simple tools. And in  
00:37:53: that way, even if there's some  
00:37:54: deviation, maybe it gets all kind of uh  
00:37:57: loopy over here, we know that it called  
00:37:59: a tool. And because it called a tool, we  
00:38:01: can obviously interpret that um a lot a  
00:38:03: lot easier, right? We have a sequence of  
00:38:05: steps like 1 2 3 4 5 6. We go through  
00:38:09: the process. It's just way more  
00:38:10: straightforward. So, we just let an  
00:38:12: agent, which is optimized for coding,  
00:38:13: make its own tools. Then the agent will  
00:38:16: call the tools and then interact with  
00:38:17: life for us. I want to show you guys how  
00:38:19: easy it is to build your own tools. So  
00:38:21: here I have a simple query. Hey, how  
00:38:22: would you build a workflow that takes a  
00:38:24: video, cuts out the silences in said  
00:38:26: video, and stitches it all back together  
00:38:28: to deliver me the results. The cut  
00:38:29: should look natural like most YouTube  
00:38:31: junk cuts. Basically just try and stitch  
00:38:32: the empty space together. You know, this  
00:38:34: is a pretty complicated flow if you  
00:38:36: think about it. There are a lot of  
00:38:37: different ways you could build something  
00:38:38: like this and none of them are basically  
00:38:40: easy. So, what this is going to do is  
00:38:41: it's going to look for a couple of  
00:38:43: simple and easy ways to do this and then  
00:38:45: present them to me because I went down  
00:38:47: here and I selected plan mode, which is  
00:38:48: one of the different modes that you can  
00:38:49: use in um at least the Claude series of  
00:38:51: models. Keep in mind depending on the  
00:38:53: models that you're using may be a little  
00:38:54: bit different. So now once I have this  
00:38:56: plan in front of me, I'm then going to  
00:38:58: be able to decide on how to do the  
00:38:59: workflow and then I could act as more or  
00:39:01: less a highle director letting this  
00:39:03: thing know whether or not I want to do  
00:39:04: something. Okay, next up it's asking me  
00:39:06: are we doing this on short clips, long  
00:39:08: clips, any preference on the defaults  
00:39:10: and so on and so forth. I say short  
00:39:12: clips defaults sound fine. MP4 is great.  
00:39:17: Okay, I then have the plan in front of  
00:39:18: me and if I wanted to build this, all I  
00:39:20: would need to do is click yes and auto  
00:39:22: accept. And I think I will. That seems  
00:39:24: pretty straightforward. So, let's give  
00:39:25: it a try. While this is working, I'm  
00:39:28: just going to see if I could find an  
00:39:29: example of a video that I could feed  
00:39:31: into this. Um, I've done this a couple  
00:39:33: of times previously as you guys could  
00:39:35: see. So, let me just find some really  
00:39:37: simple video that's only a few seconds  
00:39:38: that we can test this on. Okay. And I  
00:39:41: found an example here. It's just a short  
00:39:43: one minute video clip of me doing a  
00:39:45: typical intro.  
00:39:47: Now that this thing is building, I'm  
00:39:48: just going to move this to bypass  
00:39:50: permissions mode. That'll just allow it  
00:39:51: to operate autonomously without me. And  
00:39:53: once it's there, it's actually created  
00:39:54: it. That's great. As you guys can see,  
00:39:56: that only took us maybe like 30 seconds  
00:39:58: or so. From here, I actually want to  
00:39:59: test this. Let's test using  
00:40:02: test_clipip.mpp4.  
00:40:07: Now, I'm not actually expecting this to  
00:40:09: work the first time around because most  
00:40:10: workflows don't actually work the first  
00:40:12: time around. It's all a process of  
00:40:13: progressive iteration. Essentially, if  
00:40:15: the workflow doesn't work, the error  
00:40:17: message is fed back into the agent and  
00:40:19: then the agent will progressively build  
00:40:21: the agentic workflow using the u the  
00:40:23: error messages to sort of guide it in  
00:40:24: the right direction.  
00:40:26: In situations like this, I honestly just  
00:40:28: alt tab and then do something else.  
00:40:30: Okay. And it actually looks like it did  
00:40:32: run through the entire test manually and  
00:40:34: was perfectly fine. That's crazy. What  
00:40:37: I'm going to do now is I'm just going to  
00:40:38: watch the test, see how it is, and then  
00:40:40: we'll just continue to go back and forth  
00:40:41: a few times until I have what I want.  
00:40:43: Oh, by the way, I don't even need to  
00:40:44: find this file. I could actually just  
00:40:45: say open it. Okay, so I'm noticing that  
00:40:48: the cuts are kind of abrupt. They're a  
00:40:49: little bit too fast for me. Um, what I  
00:40:51: mean by that is like instead of cutting  
00:40:53: at the point that I wanted it to cut,  
00:40:55: it's just cutting like a few seconds  
00:40:56: before. Multiple different ways around  
00:40:57: this. I could use a different approach  
00:40:59: to detect the cut points. I could have  
00:41:01: it manually move things over. I mean, if  
00:41:03: you think about it, like I could do  
00:41:04: whatever the heck I want here. Uh, this  
00:41:06: thing's operating at the speed of  
00:41:07: thought. So, I'm just going to give it  
00:41:08: some very high level instructions here,  
00:41:09: and we'll see what it thinks. It's  
00:41:11: giving me a bunch of different options  
00:41:12: here. One of them is voice activity  
00:41:14: detection. I like this. Let's do this  
00:41:17: one. Okay, it's now testing with this  
00:41:18: new approach.  
00:41:20: All right, let's take a look at round  
00:41:21: two.  
00:41:24: Okay, so it worked perfectly on the um  
00:41:27: one minute clip. So now I'm just going  
00:41:28: to run it on test three minutes.  
00:41:32: Okay, and it's just finished and then  
00:41:34: opened the next clip. Let's just see how  
00:41:36: that does. There is a cut point right  
00:41:39: here, I think. Let's see if that's good.  
00:41:44: Cool. Nice. Looks like it did that cut.  
00:41:45: That's cool. How about another one? H  
00:41:49: I think it was right here.  
00:41:54: Nice. It's solid.  
00:41:59: Last one right here.  
00:42:04: Cool. So, yeah, this one worked  
00:42:05: basically perfectly. Um the agentic  
00:42:07: workflow is for the most part now  
00:42:09: complete. So, you guys could see it took  
00:42:11: one back and forth. I just in a very  
00:42:12: high level um realistic way gave it a  
00:42:15: list of what I wanted. I didn't really  
00:42:16: know what I wanted to be honest, just  
00:42:18: like I think most people that have  
00:42:19: probably done any sort of like software  
00:42:20: engineering work know clients usually  
00:42:22: have no clue how to scope a project. So  
00:42:24: you can sort of only take them at face  
00:42:25: value there. I went back and forth a  
00:42:27: little bit. Um you know I was like okay  
00:42:28: this didn't work too well. Is there any  
00:42:30: other thing that we could do? It gave me  
00:42:31: some other thing. So I tried the other  
00:42:33: thing. Hopefully you guys could see that  
00:42:34: this sort of loop is very  
00:42:35: straightforward and realistically only  
00:42:37: takes a few moments of your time. The  
00:42:39: most important part I think of my entire  
00:42:41: day is now just providing some sort of  
00:42:43: highlevel nudge in one direction or  
00:42:44: another to a agents like this when  
00:42:46: designing my agenda workflows. Um, you  
00:42:49: know, like if you just remove me from  
00:42:50: the loop completely, the resulting agent  
00:42:52: workflow is probably going to suck, at  
00:42:53: least for now. But, uh, I'm just here to  
00:42:55: steer the ship, right? It's almost like  
00:42:57: as if I don't know, it's like an old  
00:42:59: school Viking boat where people have to  
00:43:00: like manually row, right? So, I'm just  
00:43:02: the person at the very front of the ship  
00:43:03: doing a little bit of steering. The  
00:43:04: agents are the minions doing my rowing.  
00:43:07: At this point, I'm briefly going to  
00:43:09: cover memory here. It's how agents  
00:43:10: maintain context. This isn't super  
00:43:12: important to know for building, but it's  
00:43:14: important to know if you want to  
00:43:15: understand how these things work under  
00:43:16: the hood. So, short-term working memory  
00:43:18: are basically reasoning tokens that are  
00:43:20: relevant to the current task. They're  
00:43:21: stored temporarily. If you guys have  
00:43:23: ever seen like a little thinking window  
00:43:25: or a thinking tab with like a little  
00:43:26: thing that you could click to open  
00:43:28: inside, it'll be like the user wants to  
00:43:30: do this. The user is thinking about  
00:43:31: doing this. This is your uh short-term  
00:43:33: memory sort of uh analog and like the  
00:43:35: way that our human brains work. Sort of  
00:43:37: your intermediate memory is your back  
00:43:38: and forth messages with the agent. So  
00:43:40: it's like the actual like message chain  
00:43:42: that you are having. Those aren't  
00:43:44: removed like reasoning tokens are. And  
00:43:45: so this is just always stored and sent  
00:43:47: with every API call. Long-term memory  
00:43:49: are things that persist across sessions.  
00:43:51: So they're variables that are stored in  
00:43:52: claude chat GBT etc. On the right hand  
00:43:54: side here, I have that same message that  
00:43:56: I sent earlier as part of our demo where  
00:43:58: I scrape 200 HVAC owners. If I show you  
00:44:00: guys how all of this memory works in  
00:44:01: context, basically this over here, okay,  
00:44:04: and then its replies are what are called  
00:44:06: intermediate messages. Anything inside  
00:44:08: of this thinking tab is like your  
00:44:10: short-term, okay? And then long-term are  
00:44:13: like things that are stored within my  
00:44:15: file space. So they're things like, you  
00:44:18: know, my agents MD. They're things like  
00:44:20: my Gmail accounts.json. They're things  
00:44:22: like my token leftclick. If this all  
00:44:25: seems like magic to you right now, don't  
00:44:26: worry. You're going to get to the point  
00:44:27: you can actually understand and  
00:44:28: interpret everything within an  
00:44:30: integrated development environment by  
00:44:31: the end of the program. But I just  
00:44:32: wanted you guys to be on the same page  
00:44:34: here that this over here is like an  
00:44:36: intermediate piece of memory. It's going  
00:44:38: to include all messages that are sent  
00:44:40: and received from you and the agent and  
00:44:41: then everything in between the reasoning  
00:44:43: loops and stuff for short-term whereas  
00:44:44: long-term tend to be files and then  
00:44:46: system prompts. Right now, one of the  
00:44:47: primary failure modes in Agentic systems  
00:44:50: right now is because of um context. And  
00:44:52: context, for those people that don't  
00:44:53: know, is just all of like the the  
00:44:55: letters and words and tokens that are  
00:44:57: being stored in a model at any given one  
00:44:58: point in time. Uh the way that agents  
00:45:00: manage context limitations right now is  
00:45:02: they are summarizing previous steps to  
00:45:04: save on tokens by compressing the full  
00:45:06: history into key takeaways. If you think  
00:45:08: about it, like the way that I write and  
00:45:10: the way that the model writes isn't  
00:45:11: actually like super token efficient.  
00:45:12: What it does is it makes a bunch of  
00:45:14: summaries of these constantly. So if you  
00:45:16: know this is my actual chat window if  
00:45:18: you think about it that's the message  
00:45:19: that the agent sent me and this is the  
00:45:21: message that I sent the agent this is  
00:45:22: the message that it sent me back and  
00:45:24: blah blah blah what it'll do  
00:45:25: periodically just to save on the token  
00:45:27: cost is it'll actually just summarize it  
00:45:29: in as high density a form as humanly  
00:45:31: possible so we take maybe like a 500word  
00:45:34: uh uh context and then chunk that down  
00:45:36: into like a a 100 or maybe a 50word  
00:45:39: context. It'll do so periodically  
00:45:41: without losing you the core details just  
00:45:43: by rewriting it in various ways that are  
00:45:44: just a lot simpler. For instance, I  
00:45:46: could say hello, how are you doing? My  
00:45:48: name is Nick Sarif. Or I could say, hi  
00:45:52: dash, how you do question mark, I'm Nick  
00:45:58: Sarif. And if you just like count up the  
00:46:00: total number of characters there, the  
00:46:01: latter one is obviously going to be a  
00:46:02: lot more efficient. They also don't  
00:46:04: store reasoning in the main loop. It  
00:46:06: generated temporary and then it  
00:46:07: disappears. It does store intermediate  
00:46:08: results externally by offloading the  
00:46:10: databases, files, and other vector  
00:46:11: stores. And then it'll now load the  
00:46:13: relevant context on demand to only pull  
00:46:15: in what is needed for the current step.  
00:46:17: Um, you know, you can build this in  
00:46:19: explicitly using something called a rag  
00:46:20: or retrieve augmented generation system,  
00:46:22: which I'll talk about later, or you can,  
00:46:24: uh, you know, just let the model do its  
00:46:25: own thing and it does a pretty good job  
00:46:26: of it. When we make it to reflection,  
00:46:28: this is where the agent self-evaluates.  
00:46:30: So that's where it examines its outputs  
00:46:31: to detect errors and then assess whether  
00:46:33: or not what it wanted to do actually  
00:46:35: worked. It identifies the approaches are  
00:46:36: failing. it knows when to pivot and it  
00:46:38: just selforrects. This is really like  
00:46:40: the intelligence of the model to be  
00:46:41: honest. Um, if you don't have this  
00:46:43: reflection loop, you will just have a  
00:46:44: script like a typical Python script or  
00:46:47: like an nadn or make.com or zapier or  
00:46:49: gum loop or lindy automation that just  
00:46:51: breaks at the first hiccup. And this is  
00:46:52: also really important in what's called  
00:46:54: self-annealing which I'm going to cover  
00:46:55: a little bit more of later. But it's  
00:46:56: essentially the way that an agentic  
00:46:58: workflow can run and then also just heal  
00:47:00: itself as it encounters errors and so  
00:47:02: on. Finally, we have what is called the  
00:47:03: orchestration or coordination layer. The  
00:47:05: way that I think of it as if you just  
00:47:07: get all of these steps, right? So  
00:47:08: planning, tool use, memory, then  
00:47:12: reflection. Okay, orchestration doesn't  
00:47:15: exist within the loop. It sort of exists  
00:47:16: outside of it or maybe inside of it. And  
00:47:18: then it's just responsible for shuttling  
00:47:20: the information around from step to  
00:47:22: step. And that's really cool, right? It  
00:47:24: looks at the results of the plan. It  
00:47:27: then feeds that into the right tools. It  
00:47:29: then enters what it needs to enter in  
00:47:31: memory. and then it looks at the results  
00:47:33: of the reflection and then changes the  
00:47:35: next loop of the planning and so on and  
00:47:37: so on and so forth infinitely. I think  
00:47:38: of it as like the brain that combines  
00:47:40: all the components that we just talked  
00:47:41: about similar to how your brain combines  
00:47:43: inputs from like your ears and your eyes  
00:47:45: and your nose and your skin and your  
00:47:47: mouth and your memory and it just like  
00:47:49: factors everything in and then this is  
00:47:51: what thinks and then ultimately comes up  
00:47:53: with decisions. Now there are a couple  
00:47:54: of different approaches uh right now for  
00:47:56: orchestration. uh there's an approach  
00:47:58: with crew AI right now that uses  
00:48:00: role-based team structures and so you  
00:48:02: know up at the top you have some sort of  
00:48:04: manager and then underneath you maybe  
00:48:06: have like a a marketer and then you have  
00:48:08: like a software engineer and you know  
00:48:10: the manager exists above the marketer  
00:48:12: and the software engineer and the  
00:48:13: marketer has like you know some interns  
00:48:15: and so on and so forth the software  
00:48:17: engineer has some juniors this is one  
00:48:19: way of doing it um and it's a way that  
00:48:21: you know crew AAI has done reasonably  
00:48:23: well with like the sort of framework  
00:48:25: role-based team structure I think It's  
00:48:27: kind of like an organization and I think  
00:48:28: that's just looking at things like a  
00:48:30: human being would. I think they're  
00:48:31: actually just much more efficient ways  
00:48:32: to organize. So I don't personally do  
00:48:34: this with the directive orchestration um  
00:48:36: execution framework and then cloud  
00:48:38: skills. Instead, what we do is we  
00:48:40: basically give AI access to um both  
00:48:43: highle instructions and then tools to  
00:48:47: have it execute. And then this AI over  
00:48:49: here, this is sort of like that  
00:48:50: orchestrator that we were talking about  
00:48:52: before. It just looks the high level  
00:48:53: instructions, looks at the tools,  
00:48:55: matches up the two, does stuff, stores  
00:48:57: things into a memory, and then it just  
00:48:58: loops over and over and over in that  
00:49:00: PTML loop. Claude skills is kind of  
00:49:02: similar. It just um organizes the  
00:49:04: instructions. If we visualize this for  
00:49:08: you guys, it basically just stores  
00:49:09: things into a folder. This folder  
00:49:13: contains both the highle instructions  
00:49:15: and the specific tool use and any  
00:49:18: additional resources. And then the model  
00:49:21: now just accesses a folder instead of  
00:49:23: accessing you know two different  
00:49:24: folders. And really the point I'm trying  
00:49:26: to make is no framework is perfect yet.  
00:49:28: I imagine the real best framework in the  
00:49:30: future is just going to be a combination  
00:49:31: of all these. You know taking the best  
00:49:33: parts and leaving the crappiest parts.  
00:49:34: Um but they are all improving rapidly as  
00:49:36: the space gets m more and more mature.  
00:49:38: So my recommendation is we're not going  
00:49:40: for perfection here. We just want what  
00:49:41: works. And in my case um I use dough  
00:49:43: because you know I came up with it and  
00:49:45: then it's a big part of all the content  
00:49:46: that I'm producing now. So I mean this  
00:49:48: works reasonably well right now. Sure,  
00:49:50: maybe there's another framework out  
00:49:51: there that'll get us from 97% accuracy  
00:49:53: to 98.5. I'll worry about that framework  
00:49:56: when it's here. For now, I'm going to do  
00:49:58: what I can with the 97. Okay, we're now  
00:50:00: talking text. This is the universal  
00:50:02: interface. When I want to talk to my  
00:50:05: model, I do so through text, right? When  
00:50:08: I want to talk to my model and I don't  
00:50:10: know, I try and give it a call or  
00:50:12: something like you can do on claw on  
00:50:13: chatbt and stuff like that. What's  
00:50:15: really occurring is I'm transcribing  
00:50:16: most of that into text. Now agents if  
00:50:19: you think about it are actually a step  
00:50:20: back in terms of our interfaces for now.  
00:50:23: Back in the day and when I say back in  
00:50:25: the day I mean like you know very very  
00:50:27: recently um most people use these drag  
00:50:29: and drop no code tools right and these  
00:50:31: are actually really pretty and they're  
00:50:32: very easily interpretable and you can  
00:50:34: see how the data flows and so now we  
00:50:36: basically said no screw that we just  
00:50:38: want a bunch of words on a screen right  
00:50:40: which obviously has a bunch of issues in  
00:50:41: terms of presentation our ability to  
00:50:43: visualize them and understand them.  
00:50:44: Right now we are taking a step back in  
00:50:46: terms of the interface. It's sort of  
00:50:49: like back in like the 70s, 80s and 90s  
00:50:51: when most people coded and then built  
00:50:53: things on computers through DOSs or  
00:50:55: Linux terminals, right? It was like text  
00:50:57: in you get results out. That's it.  
00:51:00: Everything is just like some sort of  
00:51:01: terminal or prompt. And in this way, I  
00:51:03: think it can be really intimidating for  
00:51:04: people because they just see a bunch of  
00:51:05: text and they're like, "Oh, I'm not a  
00:51:06: programmer. Oh, I'm not like a, you  
00:51:08: know, I don't learn through reading and  
00:51:09: writing. I learn through seeing." And I  
00:51:11: think that's fair and it's a totally  
00:51:13: okay criticism to make with these things  
00:51:14: right now. I imagine future systems are  
00:51:17: going to go back to a visual interface.  
00:51:19: It's just we don't have them yet. And as  
00:51:20: I mentioned earlier, my whole goal is  
00:51:22: just make do with what we can at the  
00:51:24: moment. I imagine over the course of the  
00:51:25: next couple years, somebody's going to  
00:51:26: build the most amazing visual interface  
00:51:28: probably in conjunction with one of  
00:51:30: these agents or agent agentic workflow  
00:51:32: builders and then we'll have something  
00:51:33: that combines the best of both worlds,  
00:51:35: natural language and visualization. But  
00:51:37: right now we use some tools. And those  
00:51:39: tools as of the time of this recording  
00:51:40: are cursor, VS code, and anti-gravity.  
00:51:43: And that's where most agent interaction  
00:51:45: happens today. That is the textheavy  
00:51:47: interface that you guys saw earlier as  
00:51:48: part of the demo where I just talk to  
00:51:50: the model through a chat box and see it  
00:51:51: update files and stuff like that. On the  
00:51:53: lefth hand side, I have some  
00:51:54: recommendations to make things feel a  
00:51:56: little bit more natural. I personally  
00:51:57: use speech to text tools like um Whisper  
00:51:59: Flow and Aqua. These are really simple,  
00:52:01: straightforward transcription tools.  
00:52:03: They allow you to feel like you're  
00:52:04: talking to an employee more than you are  
00:52:06: necessarily writing text or typing at  
00:52:09: your computer. I'm going to show you  
00:52:10: guys a bunch of practical examples of me  
00:52:12: using this. But for now, let me give you  
00:52:14: guys a demo. On the left hand side here,  
00:52:16: I'm just talking to my model. I  
00:52:17: basically converted a workspace from the  
00:52:19: directive orchestration execution  
00:52:21: framework to the cloud skill framework.  
00:52:22: And you guys are going to see both of  
00:52:23: those later. But for now, I just want to  
00:52:25: ask it how things are going and you  
00:52:26: know, if you can tell me something about  
00:52:27: it. So, I'm just going to hold down a  
00:52:28: key on my computer. Fn. Hey, can you  
00:52:31: tell me a little bit about the changes  
00:52:32: that we just made? I let go and then I  
00:52:34: press enter and now I'm basically  
00:52:36: talking to my model. Of course, I still  
00:52:37: have to press the enter key. Future  
00:52:39: iterations of this will probably change  
00:52:41: that, but in this way, I'm maximizing  
00:52:43: the bandwidth. Human beings can speak a  
00:52:45: lot faster than they can type, but they  
00:52:47: can also read a lot faster than they can  
00:52:48: listen. So, this is typically how you  
00:52:50: optimize both of those. All right, so  
00:52:51: what I have here are five cloud code  
00:52:53: instances. I'm running the latest model  
00:52:55: of Opus, Opus 4.5, at least as of the  
00:52:58: time of this recording. You guys may  
00:52:59: have some later versions, but just to  
00:53:01: show you as the variability of model  
00:53:02: outputs, I've set all these to plan  
00:53:03: mode. And what plan mode essentially  
00:53:05: means to make a long story short is they  
00:53:07: just don't they can't take actions  
00:53:09: without my express or explicit approval.  
00:53:11: They write a plan for me first, then I  
00:53:12: verify the plan. And so, just to show  
00:53:14: you guys how different um various forms  
00:53:16: of these plans are, I'm going to open up  
00:53:19: five tabs. I'm then going to um open up  
00:53:22: the reasoning and kind of thinking  
00:53:23: panels here. Then we're just going to  
00:53:25: evaluate how different all of these  
00:53:27: answers are to the same simple question.  
00:53:30: What are some ways to send automated  
00:53:31: proposals? So I sent that to all five.  
00:53:33: And you'll see that as we proceed  
00:53:35: through here, there are a variety of  
00:53:38: different routes that these models  
00:53:39: follow. After this does its research and  
00:53:41: and plans, you end up with five answers.  
00:53:44: And you'll notice that um all five of  
00:53:46: these answers are different, meaning  
00:53:47: that there is no like procedural  
00:53:50: simple step-by-step result here. the  
00:53:53: models are doing different things every  
00:53:54: single time. This first one here says,  
00:53:56: "What type of proposal?" So, it's asking  
00:53:58: me some questions. The second one here  
00:53:59: actually just went through and then  
00:54:00: wrote me a big list of different options  
00:54:02: I could take. This third one here wrote  
00:54:04: me sort of a combination, ask me some  
00:54:06: questions. And then it's giving me some  
00:54:08: common automation triggers alongside  
00:54:10: some more questions. This one here gives  
00:54:12: me these four options. And then this one  
00:54:14: here gives me like a little table. And  
00:54:16: this is okay. I mean, obviously I'm  
00:54:18: arriving at like the same sort of answer  
00:54:20: regardless, but I want you guys to know  
00:54:22: that like the way that businesses work  
00:54:24: is, you know, when somebody does  
00:54:25: something like they fill out a form or  
00:54:27: they require an invoice sent or  
00:54:30: something of that nature. This level of  
00:54:32: variability in and of itself is way too  
00:54:33: much. There's no way that we could  
00:54:35: really like meaningfully add value to a  
00:54:37: business, whether it's our own business  
00:54:38: or some other business with variability  
00:54:40: like this, with like 30 40 50% variance  
00:54:43: in answers. What we need is when we  
00:54:45: generate an invoice, the invoice needs  
00:54:47: to be basically the same every time.  
00:54:48: When we generate a receipt, the receipt  
00:54:50: needs to be the same every time. When we  
00:54:52: send an email, maybe an onboarding thing  
00:54:54: or whatever, these should be the same  
00:54:56: every time. When a new form comes into  
00:54:58: our system and we need to qualify them,  
00:55:00: we should use the exact same  
00:55:01: qualification framework every time. Any  
00:55:03: serious company at scale that has this  
00:55:05: level of variability in their processes  
00:55:07: won't be a serious company for long.  
00:55:09: which is why raw large language models  
00:55:11: are very difficult to use in u both  
00:55:14: mid-market and enterprise style  
00:55:15: applications. Now the reason for this is  
00:55:17: because LLMs are probabilistic not  
00:55:20: deterministic. I touched on this earlier  
00:55:22: on in the course but let me run you  
00:55:23: through how a large language model  
00:55:25: actually works under the hood. So a  
00:55:26: while back I actually built a large  
00:55:28: language model. Well I guess kind of a  
00:55:29: small language model. this guy Andre  
00:55:31: Cararpathy, he um built this big uh like  
00:55:34: GitHub repo showing people how to like  
00:55:36: train their own textbased mini GPT. I  
00:55:40: went through this whole thing and then I  
00:55:41: built my own mini GPT and it was really  
00:55:42: instructive and I've since learned a lot  
00:55:44: more about large language models and  
00:55:45: sort of what's going on under the hood.  
00:55:47: So let me just give you guys a very  
00:55:48: brief demonstration. If you guys  
00:55:50: understand this, you guys will go a lot  
00:55:51: further towards getting how these agents  
00:55:53: are working under the hood. What large  
00:55:55: language models are are they are  
00:55:57: basically machines and they are machines  
00:55:59: that operate off of a distribution of  
00:56:02: outcomes. What I mean by this is they  
00:56:05: are statistics sort of pattern matchers.  
00:56:07: What a lot of people think is that large  
00:56:09: language models will predict the single  
00:56:11: best next word but they don't do that.  
00:56:14: Instead they predict a statistical  
00:56:16: distribution of options that they could  
00:56:17: pick from. What I mean is if I say hi,  
00:56:21: how are and then I have a little space  
00:56:26: and if you feed this into a model, what  
00:56:28: you may think you're going to get is  
00:56:30: you're going to get the most likely next  
00:56:31: token, right? Which is sort of like  
00:56:32: universe A. You think you'll just get  
00:56:33: the word you and then maybe a question  
00:56:35: mark. But what you actually get is you  
00:56:37: get a whole graph  
00:56:39: of different outcomes and possible words  
00:56:42: that you could choose from. This one  
00:56:44: might be you. This one might be  
00:56:49: the word things, right? How are things?  
00:56:52: This one here might be your, for  
00:56:54: instance. And what happens is we use  
00:56:57: this concept of temperature and top P to  
00:57:02: basically randomize the process of  
00:57:04: choosing the next token. And so while U  
00:57:08: may statistically be the most likely  
00:57:10: next token, maybe U has like a 98%  
00:57:13: confidence score or something, despite  
00:57:15: the fact that U is the most likely next  
00:57:17: token, we're not always going to pick  
00:57:19: you. What we're going to do is we're  
00:57:20: going to have some cutoff, which is sort  
00:57:22: of like this um top P. And then we're  
00:57:25: going to pick from one of these three or  
00:57:26: four options. And we're going to do so  
00:57:28: with a level of what's called  
00:57:29: stochasticity or randomness. That means  
00:57:32: that you can't actually predict what the  
00:57:33: large language model is going to do  
00:57:35: every time. Now, this isn't a bad thing.  
00:57:37: This is actually a good thing because  
00:57:39: think about it. If we could predict what  
00:57:40: every large language model was going to  
00:57:42: do, there would be no reason to have a  
00:57:43: large language model. If you just  
00:57:44: trained things and always outputed the  
00:57:46: exact same thing every time, there would  
00:57:47: be no way for the model to reason  
00:57:49: flexibly about things. It would  
00:57:50: essentially just be a giant series of  
00:57:52: dominoes that just, you know, knock over  
00:57:54: one to the other. Those are some really  
00:57:55: crappy looking dominoes to the other to  
00:57:57: the other. And then, you know, we'd be  
00:57:58: able to predict everything that's going  
00:57:59: on. Anyway, models um randomness and  
00:58:02: stochasticity is actually a big chunk of  
00:58:04: how they are capable of solving problems  
00:58:05: and reasoning for us. But what I'm  
00:58:07: trying to say is there's a level of  
00:58:09: randomness added to every step of the  
00:58:10: process. Right? So the first thing is  
00:58:12: they predict a distribution of options.  
00:58:14: What that means is there is some  
00:58:15: randomness. There is some statistical uh  
00:58:18: error here or or inaccuracy. Next, we  
00:58:21: can set the temperature and top P. These  
00:58:22: are settings that you'll find in  
00:58:23: parameters for most large language  
00:58:25: models nowadays. Those settings also  
00:58:27: introduce some randomness to the  
00:58:28: process. You now have um architectures  
00:58:31: like the mixture of experts architecture  
00:58:33: which is basically where they don't just  
00:58:35: have one large language model do this.  
00:58:36: They test this simultaneously across  
00:58:38: four or five large language models and  
00:58:40: then they pick the most commonly voted  
00:58:42: task. Believe it or not this introduces  
00:58:44: some additional variance. Then even at  
00:58:46: temperature zero tiny input variations  
00:58:48: can produce wildly different outputs  
00:58:49: because of randomness. Obviously there  
00:58:51: is um sort of like probabilities here at  
00:58:53: every step. Now in math these are  
00:58:56: basically called compound probabilities.  
00:58:59: And I don't mean to make this a math  
00:59:00: thing, but if you're working with AI,  
00:59:02: you might as well um learn at least a  
00:59:04: little bit of the math underneath it  
00:59:05: because it'll help you understand how  
00:59:07: all these things work. Essentially,  
00:59:08: these compound probabilities make it  
00:59:10: very unlikely that you'll be able to  
00:59:12: achieve the exact same outcome every  
00:59:13: time on the large language models own.  
00:59:15: And so what happens is you have these  
00:59:16: error rates that compound  
00:59:18: catastrophically. I'll give you a quick  
00:59:20: example. Let's say you have five steps  
00:59:22: in a process. You want the large  
00:59:24: language model to, I don't know, go out  
00:59:26: into your email inbox, pick the best  
00:59:28: email, then you want it to summarize  
00:59:30: that email, then you want to feed that  
00:59:32: summary into some other model, then you  
00:59:34: want that other model to take that  
00:59:35: summary and then combine it with a bunch  
00:59:37: of other summaries to give you a big  
00:59:38: digest of the day. So if you have five  
00:59:41: steps and each of them are 90%  
00:59:44: successful, the way that math works  
00:59:46: really is although every individual step  
00:59:49: may be 90% successful, if you math it  
00:59:52: out and actually multiply out 90%  
00:59:54: success for step one time 90% success  
00:59:56: for step two times 90% success for step  
00:59:58: three times 90% success for step four  
01:00:01: times 90% success for step five, you end  
01:00:04: up not with a 90% success rate across  
01:00:07: the entire process. you end up with a  
01:00:08: 59% success rate across the entire  
01:00:10: process. Essentially what occurs is  
01:00:12: although the first step might be 90%.  
01:00:15: The second step when multiply makes it  
01:00:17: 081 and then you have 64 or 74 or 63 and  
01:00:21: so on and so forth until eventually your  
01:00:23: actual total error rate is significantly  
01:00:25: higher. Your success rate on the other  
01:00:27: hand is significantly lower. And so when  
01:00:29: you add more and more steps to this  
01:00:31: process, you know, if you get to 10,  
01:00:32: it's 35% success rate. If you're at 20,  
01:00:34: it's 12% success rate. This applies even  
01:00:37: if models are 95% successful at specific  
01:00:39: tasks. What ends up happening is  
01:00:41: basically at every step of the task. A  
01:00:44: good way to consider it is the total  
01:00:47: range and outcomes gets bigger and  
01:00:49: bigger and bigger and bigger. There are  
01:00:51: super successful outcomes, sort of quasy  
01:00:53: successful outcomes. They're not  
01:00:55: successful outcomes and they're like  
01:00:56: catastrophic outcomes, right? And this  
01:00:58: range in business is nowhere near tight  
01:01:02: enough for most companies to trust  
01:01:03: systems like this. Now, because most  
01:01:05: business workflows are multi-step and  
01:01:07: because people have typically tried  
01:01:09: doing things like this with dumber,  
01:01:10: simpler models with no frameworks, you  
01:01:12: know, most raw LLMs are actually just  
01:01:14: not usable in business, aside from copy  
01:01:16: paste outputs, which is why people tend  
01:01:17: to do that. Just as an aside, imagine if  
01:01:20: you were a business that made $100,000 a  
01:01:22: month and you sent a wrong invoice 5% of  
01:01:24: the time. What sort of impact do you  
01:01:26: think you that would have to your  
01:01:27: business? Do you think that would have a  
01:01:28: 5% impact to your business? No, that  
01:01:30: would have like a 95% impact on your  
01:01:32: business. If I'm one of your clients and  
01:01:33: you send me the wrong invoice even one  
01:01:35: out of 20 times, I don't think I'm going  
01:01:37: to work with you the 21st time. So, the  
01:01:39: root cause here is we're asking  
01:01:40: probabilistic systems to do  
01:01:42: deterministic work. Probabilistic is  
01:01:44: that big sort of uninterpretable  
01:01:47: thought process that cloud that I showed  
01:01:49: you guys earlier. Whereas deterministic  
01:01:51: is what businesses use where you have  
01:01:53: one step going into the second step  
01:01:55: going into the third step going into the  
01:01:56: fourth step and so on and so on and so  
01:01:58: on and so forth. This over here is what  
01:02:01: business is and the best businesses, you  
01:02:04: know, productize and standardize  
01:02:05: everything. And then this over here um  
01:02:08: operates in the realm of probabilities  
01:02:10: which ultimately we can't use. What is  
01:02:12: the solution here? Well, it's not  
01:02:13: necessarily just making LLM smarter.  
01:02:15: Although keep in mind, the smarter the  
01:02:17: models get typically the less error and  
01:02:18: variance they do have. That's great. But  
01:02:21: the actual solution is we don't have to  
01:02:22: wait for model intelligence to get smart  
01:02:24: in an unspecified amount of time. We  
01:02:26: just build a framework around those  
01:02:29: models that turns these really rickety  
01:02:31: outputs into something that we could  
01:02:33: still use anyway despite the fact that  
01:02:35: there's variability in the process. We  
01:02:38: give them defined nodes and steps  
01:02:40: between each important thing that we  
01:02:43: want. And in that way, because we're  
01:02:45: shortening the total gap, models are  
01:02:47: capable of performing economically  
01:02:48: valuable work. So what we're going to do  
01:02:50: is wrap this super galaxy brain  
01:02:52: intelligence in a framework. And this  
01:02:55: framework is going to allow us to  
01:02:57: control it for beneficial purposes for  
01:02:59: ultimately business ends. Okay. So how  
01:03:01: do you actually do that? Well, this is  
01:03:02: now where you get into DO or the  
01:03:04: directive orchestration and execution  
01:03:06: framework. What we do is we separate  
01:03:09: concerns. Directives up at the very top  
01:03:11: provide very clear unambiguous  
01:03:14: instructions to the system. These are  
01:03:16: documents which if you guys remember  
01:03:18: were sort of the first rung on that  
01:03:20: knowledge ladder. Orchestration, if you  
01:03:22: think about the PTMRO loop, is where the  
01:03:24: large language model does its thing. It  
01:03:27: chooses what to do and in what order.  
01:03:30: And then execution scripts are the  
01:03:32: actual heavy lifting. And we don't do  
01:03:34: that with the model itself. What we do  
01:03:37: that are with little snippets of code  
01:03:39: that the model has built, then test, and  
01:03:41: then retested over and over and over  
01:03:43: again. Okay? I typically do this in  
01:03:46: Python right now, but I want you guys to  
01:03:48: know you can do this with whatever  
01:03:50: programming language you want. The  
01:03:51: models tend to be pretty good at I want  
01:03:53: to say most of them equally. The reason  
01:03:55: why this works so well is because of  
01:03:56: this concept of separation of concerns.  
01:03:59: Essentially, anything that is  
01:04:00: deterministic aka something that like a  
01:04:02: business would use. So maybe an API  
01:04:04: call, some sort of data transformation,  
01:04:06: some sort of file ops actually go into  
01:04:09: code. Code is always the same every  
01:04:11: single time. If you give it input A,  
01:04:13: it'll always give you output B. There's  
01:04:15: never any variability unless you  
01:04:17: specifically program that in. So, it's  
01:04:19: really, really interpretable. It's very,  
01:04:20: very clear how it works. And you never  
01:04:22: really need to wonder, hm, is that doing  
01:04:24: what I wanted it to do? Because it's  
01:04:26: only going to do what you told it to do.  
01:04:28: And then what we do is we leverage the  
01:04:30: really flexible, cool parts of AI to  
01:04:32: make judgments, to make routing  
01:04:34: decisions, and so on and so forth. Code  
01:04:37: is really reliable. It's also super fast  
01:04:39: and precise. LLMs are flexible,  
01:04:41: adaptive, and then also handle ambiguity  
01:04:43: really well. So, what we're doing is  
01:04:45: we're combining the best of both parts.  
01:04:47: We combine AI's incredible ability to  
01:04:49: route and be flexible and so on and so  
01:04:52: forth with deterministic code's  
01:04:54: extraordinarily ability to run really  
01:04:57: quickly, really precisely, and really,  
01:04:59: really repeatably. When you do this, you  
01:05:01: get the best of both worlds, and you can  
01:05:02: make a ton of money with it. That's how  
01:05:04: Agentic workflows work in a nutshell.  
01:05:05: What's interesting is you probably would  
01:05:07: not have understood any of this had you  
01:05:08: not watched the last hour to hour and a  
01:05:10: half of content all about the basis and  
01:05:12: the foundations. Some other reasons LLMs  
01:05:15: are really really bad at basic  
01:05:16: operations. When I say basic operations,  
01:05:18: I mean math. Up until quite recently, um  
01:05:21: LLM couldn't even count the number of  
01:05:22: letters in a word. That's something that  
01:05:24: you could build a Python script to do in  
01:05:25: like 0.1 seconds. You know, if you have  
01:05:27: a big list of numbers or something, you  
01:05:29: use LLM to sort those numbers. It's kind  
01:05:31: of like hiring a PhD intelligence to  
01:05:33: count some inventory. It's just not the  
01:05:35: best cost basis on your end. You're  
01:05:36: going to spend way too much money and  
01:05:38: get way too little of a result. Hence  
01:05:39: why we pushed the deterministic tasks to  
01:05:42: scripts and then reserve the LLM  
01:05:43: processing with the tokens for actual  
01:05:45: thinking. Also makes everything cheaper.  
01:05:47: Just for the purposes of demonstration,  
01:05:49: if I gave an LLM a really simple task  
01:05:51: and I said, "Hey, I have all of these um  
01:05:54: letters, okay, and they're all arranged,  
01:05:57: you know, in this list." And let's say  
01:05:59: this list hypothetically isn't just, you  
01:06:01: know, six letters long. It's like a 100  
01:06:04: thousand or 10,000 items long or  
01:06:06: something. It's just like really really  
01:06:07: long. Okay, so just pretend that I put  
01:06:08: this thing together and I give it to an  
01:06:10: LM. If I had the large language model  
01:06:12: sort this thing, it would have to run  
01:06:14: billions upon billions upon billions of  
01:06:17: mathematical operations to sort this  
01:06:18: list. If I gave this to a Python script,  
01:06:22: it could literally do this entire thing  
01:06:24: in one function call. I could probably  
01:06:26: do it in like 5 seconds on my own, not  
01:06:28: even with a large language model. And it  
01:06:30: would take milliseconds. If you look at  
01:06:32: the actual mathematical time and then  
01:06:34: the resource usage when you use uh  
01:06:35: deterministic scripts to do things like  
01:06:37: this, these mathematical simple  
01:06:38: operations like sort a big list, you  
01:06:40: could do it 10,000 to 100,000 times  
01:06:42: faster with deterministic code. And then  
01:06:45: it's also for the most part free because  
01:06:47: it's operating on your CPU or  
01:06:49: extraordinarily low cost cuz it's  
01:06:50: operating on some cloud CPU or GPU um  
01:06:52: that's very very uh affordable. This  
01:06:55: gets more and more and more difficult  
01:06:56: the more you do. Instead of having the  
01:06:58: large language model do math for us,  
01:07:00: what we do is we build a calculator tool  
01:07:02: and then we say, "Hey, can you call the  
01:07:03: calculator tool to do the math for us?"  
01:07:05: In this way, obviously, we're maximizing  
01:07:07: the best of all possible worlds. So now  
01:07:09: I want to show you the difference  
01:07:10: between using a large language model's  
01:07:12: native intelligence to do something that  
01:07:14: I think most would consider very simple,  
01:07:16: which is just sorting a list, and then  
01:07:18: using a Python script to do it instead.  
01:07:20: And I'm showing you this because there  
01:07:22: are so many advantages to using  
01:07:23: procedural deterministic tools like  
01:07:25: Python scripts. It's hard for me to know  
01:07:27: where to begin, but I just wanted to  
01:07:28: give this to you guys sort of as a  
01:07:29: representative example. So, what I've  
01:07:31: done up here is I've just had AI or an  
01:07:33: agent assist me with the creation of a  
01:07:35: brief demo list that I'm going to sort.  
01:07:37: The first thing I'm going to do is I'm  
01:07:38: going to tell it to sort the list on its  
01:07:40: own. Sort the list using only your  
01:07:42: native LLM intelligence. Do not make use  
01:07:44: of any tools. Time yourself and at the  
01:07:47: end, let me know how long it took.  
01:07:50: What I'm going to do now is let it run.  
01:07:53: And you'll see that when its native LLM  
01:07:55: intelligence does the sorting, it takes  
01:07:57: significantly longer in order to do so.  
01:07:59: We can see the time that it's taking by  
01:08:01: expanding this reasoning tab.  
01:08:04: Scroll all the way down here. You can  
01:08:06: see it's actually manually outputting  
01:08:07: every token. Here we go. And now it's  
01:08:10: actually gone through and sorted the  
01:08:11: list alphabetically by name. Okay.  
01:08:13: Anyway, it told us it didn't have its  
01:08:14: own internal clock or whatever, but  
01:08:16: realistically, as you guys could see and  
01:08:18: probably timestamped the video, this  
01:08:19: took what, 30 seconds or something like  
01:08:20: that from start to finish. Now, I want  
01:08:22: you to see how quickly it is when we  
01:08:24: just run a script to do it instead. Now,  
01:08:26: run the script.  
01:08:30: So, what it's going to do is instead  
01:08:32: it's just going to call said script,  
01:08:34: then it'll immediately sort this with  
01:08:36: significantly higher levels of accuracy  
01:08:37: on the right hand side. Now, I should  
01:08:39: note that the amount of time it took me  
01:08:41: to call the large language model and  
01:08:42: actually have it do the thing, that's a  
01:08:44: bunch of latency here that we're not  
01:08:45: actually taking into account.  
01:08:47: Realistically, this took 53  
01:08:48: milliseconds. The LLM, I mean, it's  
01:08:50: saying 3 to 5 seconds, but as you can  
01:08:51: tell, it doesn't really understand its  
01:08:52: own internal processing. So, it's closer  
01:08:54: to, you know, 15 to 30. That is um  
01:08:56: several hundred times faster. And not  
01:08:58: only is it several hundred times faster,  
01:09:00: a point that I'm going to make  
01:09:01: repeatedly throughout this course is  
01:09:02: also several hundred times freer because  
01:09:04: running a Python script to sort of list  
01:09:06: on your own CPU or even on cloud CPU  
01:09:09: when we get into uh posting web hooks  
01:09:11: and actually hosting these things on  
01:09:12: servers that aren't ours is like is  
01:09:15: essentially free. I mean it's it's  
01:09:16: occurring in the space of I don't know a  
01:09:18: neuron in your brain firing. This  
01:09:19: thing's doing a whole whole buttload of  
01:09:21: work. And you can see even down here it  
01:09:23: said this is the core argument for  
01:09:24: pushing deterministic work into tools.  
01:09:26: The LLM handles decision-making whereas  
01:09:27: the script handles execution. That's a  
01:09:29: major part of how we are going to be  
01:09:31: talking about how to use these and build  
01:09:32: these agentic workflows later on. So in  
01:09:34: a nutshell, my whole point is reserve  
01:09:36: your large language model calls for  
01:09:37: judgment. Let code handle the rest. By  
01:09:40: doing so, things will be significantly  
01:09:42: faster, things will be significantly  
01:09:43: more reliable and things will also be  
01:09:45: significantly cheaper. This is where the  
01:09:47: DO directive orchestration execution  
01:09:49: framework comes into play and it's how  
01:09:51: we're going to be building out the rest  
01:09:52: of the workflows in this course. Let's  
01:09:54: talk a little bit more about how to  
01:09:56: actually do this. Now, okay, so  
01:09:57: unsurprisingly, right now everything to  
01:10:00: do with the Gentic Workflows happens in  
01:10:01: what's called an IDE. If you guys are  
01:10:04: unfamiliar with IDE, that stands for  
01:10:06: integrated development environment. Now,  
01:10:09: idees look like this, and you've seen  
01:10:12: them already multiple times throughout  
01:10:14: this course. What they are is they are  
01:10:16: basically programming environments. Now,  
01:10:20: agentic workflows are not idees. To be  
01:10:24: clear here, this is just a way that  
01:10:25: we're communicating with them. If you  
01:10:27: guys remember way back in the beginning  
01:10:28: of this course, I talked about how chats  
01:10:31: were sort of like an interface and then  
01:10:33: agents were like things that lived  
01:10:35: inside of the interface almost the way  
01:10:36: that a crustation has shells and it can  
01:10:38: change shells at will. Well, right now,  
01:10:41: because programmers usually build stuff  
01:10:43: and because agentic workflows are  
01:10:45: composed of the same thing that  
01:10:46: programmers used to build, we just  
01:10:48: happen to do them in an IDE. But I want  
01:10:50: you to know that this is most likely to  
01:10:52: change. Now, I don't like IDEIDes  
01:10:54: because they just are really overly  
01:10:55: technical for a lot of newbies, people  
01:10:57: that don't understand this stuff, and  
01:10:58: they look at it and they look at all the  
01:11:00: lines on the page and all the different  
01:11:01: partitions and sections and then they  
01:11:02: go, "Holy crap, Nick. This is way too  
01:11:04: complicated. I'm not a technical person.  
01:11:05: I don't want to deal with it." But what  
01:11:07: I want to do in this course is I want to  
01:11:09: avail you of the notion that you have to  
01:11:10: be technical in order to understand  
01:11:11: what's going on. What this is is this is  
01:11:13: just the same thing as like a bunch of  
01:11:15: instrumentation panels on a car or  
01:11:17: something. You know, the very first time  
01:11:18: you step into a car, you don't know how  
01:11:19: the odometer works. You don't have any  
01:11:21: idea what the gear shift is, how the  
01:11:23: radio works, and all that stuff. This is  
01:11:24: the exact same thing. I'm currently  
01:11:26: taking my pilot's license right now, and  
01:11:27: let me tell you, the damn  
01:11:29: instrumentation panels on even the  
01:11:30: oldest and and cheapest of aircraft are  
01:11:33: sort of the way that I imagine IDs are  
01:11:35: to people that have never touched these  
01:11:36: things. So I entirely empathize with you  
01:11:38: and I'm going to walk you through it all  
01:11:39: in a moment. So as mentioned IDE stands  
01:11:42: for integrated development environment.  
01:11:45: I think of it as basically Microsoft  
01:11:47: Word just for code instead of you know  
01:11:49: natural text documents. They're composed  
01:11:52: of workspaces and this is the same  
01:11:54: language that basically any IDE will use  
01:11:56: where you basically just write organize  
01:11:58: run and then manage everything in one  
01:11:59: place. And it's important for me to note  
01:12:01: like how this works in a historical  
01:12:02: basis cuz otherwise you'll be like why  
01:12:04: the hell did we choose this? Well, the  
01:12:06: reason why is because back in the day,  
01:12:07: we actually used to have like five or  
01:12:08: six different tools. Uh, programmers  
01:12:10: would use tool number one to like write  
01:12:12: their code. Then they'd use tool number  
01:12:15: two to test their code. Then they jump  
01:12:17: over into tool number three to, I don't  
01:12:19: know, run their code, tool number four  
01:12:21: to host their code, tool number five to  
01:12:24: commit their code into a a repository so  
01:12:27: they could save it, and tool number six  
01:12:29: to do something else. And so there was  
01:12:31: just so much switching going on, right?  
01:12:32: We had to jump from tool number one to  
01:12:33: tool number two, whatever. And then  
01:12:35: somebody was just like, "Wait a second.  
01:12:36: Why don't we just combine all of these  
01:12:37: into one unified tool? Sure, the  
01:12:39: interface will probably be an absolute  
01:12:41: cluster, but you know, this is more than  
01:12:43: enough and it'll probably simplify and  
01:12:44: and alleviate some of the context  
01:12:46: switching." And that's basically what  
01:12:47: happened here. We basically just stuck  
01:12:49: them all into this one tool. And this  
01:12:50: tool is really like 20 or 30 tools  
01:12:52: simultaneously, which is why it looks so  
01:12:54: complicated. Now, over the course of  
01:12:55: just the last year or so, ids have  
01:12:57: gotten way smarter. And I mean smarter  
01:12:59: here as in like AI. So, in the last  
01:13:02: year, basically every IDE has added some  
01:13:05: form of AI chat capability. Old school  
01:13:08: ones like VS Code, and I'm going to  
01:13:09: cover what all these are in a minute,  
01:13:11: added built-in AI assistance quite  
01:13:13: recently. And then newer tools like  
01:13:14: anti-gravity, big one that Google just  
01:13:16: released, are now less like coding  
01:13:18: workspace, and they've just eliminated  
01:13:20: and streamlined most of the UX. So, it's  
01:13:22: almost all just like AI based agent  
01:13:23: stuff. Basically, the line between  
01:13:25: writing code and then just directing AI  
01:13:27: to do it all for you through natural  
01:13:29: language is blurring really quickly. And  
01:13:30: that's um one of the motivations behind  
01:13:32: our course actually. So this over here  
01:13:34: is VS Codes logo. This over here is um  
01:13:37: anti-gravities. And this over here is  
01:13:39: cursor. These are three relatively  
01:13:41: popular tools that I'm going to touch on  
01:13:42: in a little bit more detail. And then  
01:13:44: I'm actually going to walk through VS  
01:13:45: Code and anti-gravity just so you guys  
01:13:47: could see how all this stuff really  
01:13:48: plays out. In a nutshell, if you guys  
01:13:49: are going to be comfortable with agents,  
01:13:51: you need to be comfortable in an IDE.  
01:13:53: That's just the whole goal of today's  
01:13:54: module. So three areas of your IDE.  
01:13:58: There's a file explorer on the left.  
01:13:59: There's an editor panel in the center  
01:14:01: and then there's an agent chat panel on  
01:14:03: the right. Let's cover all of them in  
01:14:04: detail. On the lefth hand side, we have  
01:14:07: the file explorer. The file explorer  
01:14:09: almost always looks something like this.  
01:14:11: All this is is it's just another way  
01:14:13: that you guys can explore files. Just  
01:14:15: like on a Mac or a PC, you have the  
01:14:17: native file explorer. Here, your files  
01:14:19: are just arranged vertically as follows.  
01:14:22: This little tab just means that this is  
01:14:24: a folder. And if you click on one of  
01:14:25: these, obviously, this will open and  
01:14:27: expand. and then you'll be able to see  
01:14:28: all the files within. So just as like a  
01:14:30: sanity test, this um first kind of line  
01:14:34: here, this first folder is period cla  
01:14:37: and there are a bunch of other files  
01:14:38: inside of period claude. Same thing  
01:14:40: here. Period dev container period  
01:14:43: prompts period tmp period venv. You  
01:14:47: might be wondering, Nick, what the hell  
01:14:48: do any of these things mean? I'll be  
01:14:49: honest, I have AI do most of that. I  
01:14:51: don't even know, nor do I really care.  
01:14:52: The whole job of coding is not the point  
01:14:54: of gentic workflow building. All I'm  
01:14:57: doing is I'm just giving highle  
01:14:58: instructions and I have the AI deal with  
01:14:59: the how. Next up, we have a directives  
01:15:02: folder as you guys see here, an  
01:15:03: execution folder as we guys see here. Uh  
01:15:06: I also have a folder called for_youtube  
01:15:08: in my workspace. This is where I store  
01:15:10: things like this course node modules  
01:15:13: prompts trigger, right? What you'll  
01:15:14: notice is eventually we run out of  
01:15:16: folders, these little things with the  
01:15:17: tabs, and then everything else is just a  
01:15:18: file. So I have this file here, this  
01:15:20: file here, this file here. We we got a  
01:15:22: ton of files in the workspace. But  
01:15:24: hopefully now you guys have like looked  
01:15:25: at it and squinted hard enough at it  
01:15:27: that you guys at least understand that  
01:15:28: there's nothing magical going on here.  
01:15:29: This is just a file explorer. So just  
01:15:32: like with any other file explorer, you  
01:15:33: can create files, you can rename files,  
01:15:35: you can delete files, and you can  
01:15:36: organize everything you want from here.  
01:15:38: For Aentic work, at least in our case,  
01:15:40: the DO framework. This is also where the  
01:15:43: directives and executions folders live.  
01:15:45: As we saw earlier, I had the directives  
01:15:47: folder here and then the execution  
01:15:48: folder. I'm going to dive into those and  
01:15:49: actually show you what these look like  
01:15:50: in a moment. And really just the way to  
01:15:52: think about this whole thing is as a  
01:15:56: filing cabinet. Okay, that does not look  
01:15:59: like an F, but we're going to roll with  
01:16:00: it regardless. This is just your filing  
01:16:02: cabinet for your agent. And so that is  
01:16:03: how I want you to think about this  
01:16:05: moving forward. In the middle of the  
01:16:06: page, you have the editor panel. Now,  
01:16:08: this is typically in the center,  
01:16:10: although some idees will vary. That's  
01:16:12: okay. I'll cover two instances today.  
01:16:14: When you click on a file, this is where  
01:16:16: they open. And so for instance, as we  
01:16:18: see here in this middle panel, I have a  
01:16:19: file open called capitalized agents.mmd.  
01:16:23: Now we get into system prompts and how  
01:16:25: to actually control these u models  
01:16:27: through long-term context later on. But  
01:16:29: this is basically just like a file that  
01:16:31: you will add to any workspace and it'll  
01:16:33: just be injected at the very top of your  
01:16:35: agent. So the agent will just always see  
01:16:37: this in its context 24/7. And in my  
01:16:40: case, what I do is I just give it some  
01:16:41: highle instructions describing my  
01:16:43: framework. Hey, you operate within a  
01:16:45: three-layer architecture that separates  
01:16:46: concerns to maximize reliability because  
01:16:49: of the same things that I just taught to  
01:16:50: you. LLMs are probabilistic. Most  
01:16:52: business logic deterministic so on and  
01:16:54: so on and so forth. Okay? So, we'll  
01:16:56: cover this file later, but for now, I  
01:16:57: just want you to know that you can  
01:16:58: actually open multiple files and tabs  
01:16:59: just like a browser. You guys see here  
01:17:01: how this is sort of like a tab. Well,  
01:17:03: you can actually have multiple other  
01:17:04: ones open, too. I could have, you know,  
01:17:05: another file here, and then another file  
01:17:07: here, and another file here. You'll  
01:17:09: notice that some of these letters are  
01:17:10: different colors. You see how this one's  
01:17:11: blue and then this uh little um you know  
01:17:14: right arrow is green and then this text  
01:17:16: is white and then this is uh sort of  
01:17:18: orangey. Well, the reason why is just  
01:17:20: because um this this is a natural  
01:17:22: language file. This is markdown it's  
01:17:24: called which is a specific format. But  
01:17:26: like when you're dealing with code like  
01:17:27: Python and JavaScript and Node and so on  
01:17:30: and so forth, there's just so many  
01:17:31: different types of text that coloring it  
01:17:33: just makes it a little bit easier on the  
01:17:34: eyes and you can just tell what's going  
01:17:36: on faster. So in the case of markdown,  
01:17:38: which is the format that my natural  
01:17:40: language or almost plain text files are  
01:17:41: in, um if something is in blue, it's a  
01:17:44: header. So you know that this is like a  
01:17:45: header of some kind, right? Same thing  
01:17:47: over here, right? This is a header or  
01:17:48: it's like bolded, right? So that's what  
01:17:50: that is. If something is in orange, you  
01:17:52: know it's written in like code format.  
01:17:53: So anytime you write something in code  
01:17:55: format, it's done with these little back  
01:17:57: texts. Something is in white, odds are  
01:17:58: it's just like normal text. Something's  
01:18:00: in green, it's like a comment or  
01:18:01: something like that, right? This depends  
01:18:03: on the format. Typically, we only use  
01:18:05: two or three formats in Aentic Workflow.  
01:18:07: So, you're just going to figure this out  
01:18:08: really quick. Nor does it really matter  
01:18:09: to be honest because you you never  
01:18:11: actually read files. And that actually  
01:18:12: takes me to a great point. Um, you can  
01:18:14: look at files in the editor panel, but  
01:18:16: you'd almost never actually manually  
01:18:17: edit them. My rule of thumb is if I'm  
01:18:20: manually editing a file, I am doing  
01:18:22: something horrifically wrong because  
01:18:24: there's no real reason why I should be  
01:18:25: manually editing a file. I just  
01:18:27: communicate with my agent and then it  
01:18:28: does it for me. Even if I want to change  
01:18:30: a specific file, I won't go into that  
01:18:32: file. I'll just say hey change specific  
01:18:34: file to do this and then typically I'll  
01:18:36: just give it a oneline description of  
01:18:38: what I want it to do and it'll go  
01:18:39: through and it'll do it in the most  
01:18:40: efficient way. In this way I'm almost  
01:18:42: like the CEO of my own company. I mean I  
01:18:44: am the CEO of my own company but I am  
01:18:47: like the CEO of my own agent company. I  
01:18:49: just give very highle instructions and  
01:18:51: then it's the agent that interprets  
01:18:52: those highle instructions and does  
01:18:53: things. So that's two out of the three  
01:18:55: sections. The third is the agent chat  
01:18:57: panel that exists all the way on the  
01:18:59: right. So the agent chat panel is  
01:19:00: hopefully very familiar to you guys.  
01:19:02: Same sort of thing as just any chat over  
01:19:04: the last four or five years. In this  
01:19:06: case, I just said, "Hey, what's up?" It  
01:19:07: then read through agents.mmd. As I told  
01:19:09: you, it always reads through this at the  
01:19:11: very beginning of every run. And then it  
01:19:12: says, "Hey, not much. Just ready to  
01:19:14: help. What are you working on?" So, this  
01:19:15: is your primary interface. This is  
01:19:17: really where you're going to live. And  
01:19:19: uh it's such a primary interface that  
01:19:20: the modern idees like anti-gravity and  
01:19:22: stuff have basically done away with  
01:19:24: everything else except for this. And you  
01:19:25: just talk to this all day. So, you'll  
01:19:27: type your instructions here. Agent will  
01:19:29: respond. You can even see the thinking  
01:19:31: tab over here with the reasoning  
01:19:32: processes is deciding what actions to  
01:19:34: take. That's really cool for  
01:19:35: interpretability reasons. And it's also  
01:19:37: just one of my favorite things to watch  
01:19:38: because you're seeing the AI's internal  
01:19:40: monologue. It's also good and and useful  
01:19:42: when you're building aic workflows,  
01:19:44: which obviously we're going to cover uh  
01:19:45: quite shortly so that you could stop it  
01:19:47: if it makes some mistake. Um you could  
01:19:50: see where maybe an error is, do your  
01:19:51: debugging and so on and so forth.  
01:19:53: Finally, just an obligatory section on  
01:19:55: code. I know code is really intimidating  
01:19:57: for a lot of people. I want you to know  
01:19:59: that all scripts are is they're just  
01:20:01: text written in a hyperspecific way.  
01:20:04: This over here is what's called Python.  
01:20:07: Do I know what's going on over here? I  
01:20:09: mean, yeah. I've done some coding in  
01:20:10: Python, so I can look at this. I can  
01:20:12: kind of interpret it, but I I I can't do  
01:20:14: so very quickly, and I don't know what's  
01:20:16: going on for the most part. You don't  
01:20:18: actually need to have any clue what's  
01:20:20: going on in the code these days in order  
01:20:21: to do really powerful, effective things  
01:20:23: with them because, as I mentioned  
01:20:24: earlier, AI is just a way better coder  
01:20:26: than you. So, if you find yourself  
01:20:28: opening coding scripts and stuff, you're  
01:20:30: probably doing something wrong. I never  
01:20:31: actually have a page open like this  
01:20:33: because it just means no difference to  
01:20:34: me. Now, if you do find yourself opening  
01:20:37: this for whatever reason, I want you to  
01:20:38: know that a Python script or whatever  
01:20:40: language you're using, Python's just one  
01:20:41: of the many. It's just a set of  
01:20:43: instructions for the computer to follow.  
01:20:44: It's the same sort of thing as like the  
01:20:46: the the bullet points that I was showing  
01:20:48: you guys at the beginning of the course  
01:20:49: where I was describing an instantly auto  
01:20:51: reply bot. This is just a set of  
01:20:53: instructions written in a way that this  
01:20:54: computer understands, but it's literally  
01:20:56: just text sitting in a file. It doesn't  
01:20:57: do anything on its own. What you have to  
01:20:59: do in order to turn this into some sort  
01:21:01: of function, turn this into some sort of  
01:21:03: execution script, is you have to run it.  
01:21:04: And that just means telling the computer  
01:21:06: to run the instructions. And typically  
01:21:08: the way you do this is you do this  
01:21:09: through the terminal yourself. You'd  
01:21:11: find the file, you'd see it's called  
01:21:12: Python script. py. Then you'd actually  
01:21:15: go into the terminal and very  
01:21:16: intimidatingly, you know, if you even  
01:21:18: script one character, it's not going to  
01:21:19: work. You actually have to type all that  
01:21:20: yourself. Well, guess what? you no  
01:21:22: longer have to do that. The agent just  
01:21:24: does all the coding for you and then it  
01:21:25: also runs the code for you. That's what  
01:21:27: makes it such a powerful um orchestrator  
01:21:30: and that's why I live entirely in the  
01:21:32: editor. Agents just run all the code. I  
01:21:35: just say, "Hey, run my Upwork scraper."  
01:21:37: Do I have to know the format to to  
01:21:38: execute it? No, I don't. What I do is I  
01:21:41: just say, "Do the thing I want." It'll  
01:21:43: then do some thinking. It'll find the  
01:21:45: specific file that I'm referencing and  
01:21:46: then it'll go and it'll run it. And so  
01:21:48: now this is actually running. It handles  
01:21:50: the entire execution loop autonomously.  
01:21:52: That's the whole point of agentic  
01:21:53: workflows. So don't worry about being  
01:21:55: hyper precise. If you spend too much  
01:21:57: time being hyper precise, you're kind of  
01:21:58: wasting it because models, as I  
01:22:00: mentioned, are just millions of times  
01:22:01: faster than us. They think just  
01:22:02: extraordinarily quickly. This is really  
01:22:04: just the domain of the model.  
01:22:06: Communicate with it almost like you'd be  
01:22:07: communicating with an employee or staff  
01:22:09: member. Obviously, you wouldn't say,  
01:22:10: "Hey, Pete, run the Upwork scraper. Give  
01:22:12: me the results. Uh, post it to Slack and  
01:22:14: then give me the Google sheet URL. Hey,  
01:22:16: could you send Sandy an email about X,  
01:22:18: Y, and Z? Use the email template. Just  
01:22:20: speak to it like you'd speak with an  
01:22:22: employee. Don't speak with it like you'd  
01:22:23: speak with a programmer, and you're  
01:22:24: going to do a lot better. When you do  
01:22:26: this, your IDE becomes essentially a  
01:22:28: visual chatbot where you can just watch  
01:22:30: the agent work 24/7. And that's where  
01:22:32: things get really cool and really  
01:22:33: powerful. So, back in the day when we  
01:22:36: didn't have agents, we had to create a  
01:22:37: lot of this stuff manually. What I have  
01:22:39: open here on the right is the terminal.  
01:22:42: And the terminal is essentially the  
01:22:44: command line interface way that you  
01:22:47: would communicate with your computer in  
01:22:48: order to get valuable knowledge work  
01:22:50: done. Usually programming work. And so  
01:22:53: before you know I couldn't just say hey  
01:22:55: write me a script that does XYZ. Why? It  
01:22:59: would say command not found. This only  
01:23:02: works in the context of specific  
01:23:04: commands. You know instead I would have  
01:23:06: to use Python 3 for instance. I'd  
01:23:08: actually have to open it up and then I'd  
01:23:10: have to, I don't know, create a  
01:23:11: function. So, let's just do x= 5, y =  
01:23:15: 10, um, x + y equals what? 15. As I'm  
01:23:20: sure you guys could tell, this is pretty  
01:23:21: laborious. And obviously, this is like a  
01:23:23: highly specialized domain of knowledge  
01:23:25: that you have to learn in order to be  
01:23:26: able to communicate with things in this  
01:23:28: way. Well, if I clear all that out of  
01:23:30: the way, with our previous example, we  
01:23:32: had um a list, right? That list looked  
01:23:35: kind of like this. It was a big list and  
01:23:38: items with water filter, compass watch,  
01:23:40: matches, so on and so forth. So back in  
01:23:43: the day, if I wanted to build a script  
01:23:45: to do this, I needed a tremendous amount  
01:23:47: of domain specific knowledge to be able  
01:23:49: to put together scripts like this. What  
01:23:51: this does here is this. This actually  
01:23:53: sorts the list. It's Python 3 C import  
01:23:57: JSON, D equals JSON.load, open  
01:24:00: item.json, D items equals sort key  
01:24:03: equals lambda. I mean, this is like this  
01:24:04: is a whole another language you have to  
01:24:06: learn. You know, it's like me trying to  
01:24:07: write an essay in Portuguese or  
01:24:09: something. You know, the amount of time  
01:24:10: and energy it would take for me to be  
01:24:12: able to know just how to do this one  
01:24:14: thing would be immense. And you know, I  
01:24:16: can do it and then my list gets nice and  
01:24:17: sorted. But the amount of work that I  
01:24:19: had to do in order to get that done is  
01:24:20: tremendous. Contrast that with our  
01:24:22: agent. All I'm going to say is write me  
01:24:24: a simple function to sort this file  
01:24:26: alphabetically, then execute it. It's  
01:24:28: going to do some thinking to begin. So  
01:24:30: first it's going to read the file then  
01:24:32: it's going to see the structure and it's  
01:24:34: going to write the script and then  
01:24:35: execute it basically immediately. The  
01:24:37: amount of time that it previously would  
01:24:38: have taken me somebody with no knowledge  
01:24:40: how to do this probably is on the orders  
01:24:42: of like a day at least just to be able  
01:24:45: to write that script let alone all other  
01:24:46: ones and this thing can now do it in you  
01:24:48: know just a few moments. You offload the  
01:24:50: coding to the model have it actually put  
01:24:52: together these deterministic scripts  
01:24:54: which are a lot more reliable and then  
01:24:55: what you do is you just sort of sit back  
01:24:57: and orchestrate. Okay, so IDEs, as I  
01:24:59: mentioned, were kind of like code  
01:25:00: editors, right? And they've been around  
01:25:02: for quite a while, at least 15 years.  
01:25:04: They weren't designed with AI agents in  
01:25:05: mind, but the new breed of IDs just give  
01:25:08: agents access to everything. They have  
01:25:09: your editor access, they have terminal  
01:25:11: access, they even have browser access.  
01:25:13: Now, so there are three main options I  
01:25:15: want to talk about today. Each of them  
01:25:16: have different trade-offs, and your  
01:25:17: choice depends on how much flexibility  
01:25:19: versus simplicity you want.  
01:25:22: The first is anti-gravity. I'm actually  
01:25:24: going to be opening this in a moment and  
01:25:25: then running through this in a lot more  
01:25:26: detail. But basically, this is Google's  
01:25:28: brand new agentic development platform  
01:25:31: launched super recently and it's very,  
01:25:32: very good. It's designed primarily for  
01:25:34: their Gemini class of models, but it  
01:25:36: supports other providers as well. It's  
01:25:38: the cleanest and simplest interface in  
01:25:40: the bunch, has by far the lowest  
01:25:41: learning curve, and it looks something  
01:25:43: like this. On the lefth hand side, it  
01:25:45: has the file explorer. On the right hand  
01:25:47: side, you have your agent. And you'll  
01:25:48: notice in the middle, it's actually  
01:25:50: empty. And there's the ability to open  
01:25:51: up agent managers, code with the agent  
01:25:53: or edit the code inline. For the most  
01:25:55: part, this thing is really simplified  
01:25:57: and it knows that you don't really give  
01:25:58: a crap about what the files look like.  
01:26:00: Obviously, if you open a file, it'll  
01:26:01: open up in the middle, but for the most  
01:26:03: part, it abstracts away all that for you  
01:26:04: and you just communicate with the model  
01:26:06: and it does what you want it to do. Next  
01:26:07: is VS Code. That stands for Visual  
01:26:09: Studio Code. This is a lot older of a  
01:26:11: platform. It's actually the platform  
01:26:12: that all other platforms are kind of  
01:26:13: based on nowadays. It was built by  
01:26:15: Microsoft. It's their free co-et code  
01:26:17: editor and it's very, very popular. The  
01:26:19: big draw to Visual Studio Code is its  
01:26:23: extensibility. You can't really see this  
01:26:25: that well, but over on the right there's  
01:26:26: this little extensions tab. And VS Code  
01:26:28: just has like a massive supported  
01:26:29: library of all the different extensions  
01:26:30: you could want. These extensions are  
01:26:32: pretty cool. Now, for the most part  
01:26:34: nowadays, we just use like the Cloud  
01:26:35: Code extension, GitHub Copilot, right?  
01:26:38: These like AI model extensions that add  
01:26:40: AI functionality into your code. But  
01:26:42: there are some cool things that you can  
01:26:43: build in with extensions that just allow  
01:26:45: you to use whatever the heck you want  
01:26:46: with it. So, I see this as less of like  
01:26:48: a specific AI editor and more as just  
01:26:50: like a really general editor that a lot  
01:26:52: of people are used to. They just import  
01:26:53: extensions to turn their editor into,  
01:26:56: you know, a hyperoptimized AI one. I'm  
01:26:58: going to be showing you this one as  
01:27:00: well, just because it's very popular.  
01:27:01: Finally, I want to chat a little bit  
01:27:03: about Kurser. Kurser is actually one of  
01:27:04: the first like AI editors on the market,  
01:27:07: like an an editor that was built  
01:27:08: specifically for AI in mind. I don't  
01:27:10: really like using Kurser these days  
01:27:12: myself. Um, obviously it's baked in  
01:27:14: directly to every part of the platform.  
01:27:17: But for the most part, I just find  
01:27:18: anti-gravity is better in every way,  
01:27:20: shape, and form. Um, very similar  
01:27:22: interface to what you guys are used to.  
01:27:23: So, there's a file explorer, there's an  
01:27:25: editor, and so on and so forth. The file  
01:27:26: explorer, which you can't actually see  
01:27:28: in this screenshot, is usually just on  
01:27:29: the left hand side. Then in the middle  
01:27:31: here, you have like the big code editor,  
01:27:32: and then on the right hand side, you  
01:27:34: have both a chat and a composer. Same  
01:27:36: sort of vibe to anti-gravity. Aside from  
01:27:37: that, it just has access to everything.  
01:27:40: I'm not going to cover this one just  
01:27:41: because while it's somewhat popular,  
01:27:42: it's not as popular as the other two  
01:27:43: options and I want to be mindful of  
01:27:45: everybody's time. Okay, so let's start  
01:27:46: with anti-gravity. Pretty  
01:27:48: straightforward stuff. On the lefth hand  
01:27:49: side, we have that file explorer, which  
01:27:50: I talked about to you guys earlier. In  
01:27:52: the middle, we have obviously the  
01:27:54: editor, which is where you can open  
01:27:55: specific files and then change things.  
01:27:57: And on the right hand side, you have the  
01:27:58: agent window, which is where you can  
01:28:00: talk with agents. So, just to be clear,  
01:28:02: I sent this agent a message saying,  
01:28:03: "Hey, what's up?" And then it tells me,  
01:28:04: "Hey, I'm ready to help. I see you've  
01:28:06: been working on a variety of workflows  
01:28:07: recently from YouTube transcript  
01:28:08: analysis and panda dooc proposals to  
01:28:10: lead scraping. What would you like to  
01:28:11: tackle today? To cover the middle  
01:28:13: section here as I talked about earlier  
01:28:15: uh markdown.md is the file format that  
01:28:17: we put a lot of instructions in. And  
01:28:19: you'll notice that we have a blue sort  
01:28:21: of headers over here you know orange  
01:28:23: text over here and then the rest of it  
01:28:24: is uh is white. And so what I've opened  
01:28:26: up is I've opened up a simple directive  
01:28:28: called the Upwork scrape apply system  
01:28:31: which just scrapes Upwork jobs matching  
01:28:32: AI automation keywords, generates  
01:28:34: personalized cover letters and proposals  
01:28:36: and outputs to a Google sheet with a  
01:28:37: one-click apply link. The whole idea  
01:28:39: behind the system, and I'm going to show  
01:28:40: you how to build ones just like this in  
01:28:41: a moment, is you can automate the  
01:28:44: process for the most part of applying to  
01:28:45: an Upwork job. Upwork being a freelance  
01:28:47: platform. This sort of stuff is going to  
01:28:49: very quickly become an integral part of  
01:28:51: most people's workflows. So as you can  
01:28:53: see here, we define some inputs. So, we  
01:28:55: give it some tools. We give it a filter.  
01:28:57: You may be thinking like, good lord,  
01:28:58: Nick, did you write all this? No, of  
01:29:00: course not. I had AI, write all of this  
01:29:01: for me based off some simple bullet  
01:29:03: points. It's very meta. You use AI to  
01:29:04: come up with the instructions for  
01:29:05: another AI model. Um, in a way, in that  
01:29:08: way, you are literally just some person  
01:29:09: that is giving some minor instructions.  
01:29:11: You're acting more as like the motivator  
01:29:13: than anything else. Okay, I remember I  
01:29:16: talked about on the left hand side how  
01:29:17: there'd be a couple of different folders  
01:29:19: here, directives and then executions.  
01:29:21: I'm just going to open up directives and  
01:29:22: show you guys around a little bit. So,  
01:29:24: as you can see here, I have a bunch of  
01:29:25: these different flows set up. One of  
01:29:27: them was Upwork, scrape, apply, but  
01:29:28: there's, I don't know, another 15 or so.  
01:29:30: Create proposal MD, cross niche  
01:29:32: outliers, deep research, pitch, and so  
01:29:34: on and so forth. Let's say I'm in the  
01:29:36: building process of an agentic workflow.  
01:29:38: What I'm going to do is I'm going to ask  
01:29:39: this to help me out. Hey, is there  
01:29:41: anything that I could do to the create  
01:29:43: proposal directive to improve it?  
01:29:46: Suggest some alternative approaches.  
01:29:49: Going to enter that in. And now the  
01:29:51: model is going to come up with some ways  
01:29:52: that we can make things better. It's  
01:29:54: going to do so with the directive  
01:29:55: structure. Um we injected a prompt into  
01:29:58: its uh agents MD, claude MD, Gemini MD,  
01:30:01: multiple different ways to initialize  
01:30:02: system prompts, but it has all the  
01:30:03: context about what I mean. And this is  
01:30:04: how Gemini's UX works. You know, analyze  
01:30:07: and improve, create proposal directive.  
01:30:09: Gives me the reasoning loop over here,  
01:30:11: progress updates, it gives me a big  
01:30:13: plan, and then I get some  
01:30:14: interpretability, some access to its  
01:30:16: thoughts. At the end of it, we end up  
01:30:18: with, "Hey, you should add a human in  
01:30:20: the loop review step. Hey, you should  
01:30:21: try a web enrichment option. Hey, you  
01:30:23: should handle variable token counts.  
01:30:25: Hey, you should do robust JSON handling.  
01:30:26: Hey, you should do a dynamic follow-up  
01:30:28: email." That's pretty cool. I like the  
01:30:30: idea of number two. Number two sounds  
01:30:32: great. Why don't we give that a try? All  
01:30:35: I'm doing is asking it for its opinion.  
01:30:37: I went through. I didn't like four out  
01:30:38: of the five, but I did like the second.  
01:30:40: So, now I'm just going to have this  
01:30:41: model go to the directive and then  
01:30:43: update it to include a web enrichment  
01:30:45: step. It's then built me a plan that  
01:30:46: looks pretty straightforward and easy.  
01:30:48: I'm then going to okay this. What I  
01:30:50: really like about Gemini is it just  
01:30:51: shows you sort of like the tracked  
01:30:53: changes really easy. And you can see  
01:30:55: here that it's now provided an  
01:30:56: additional step called research client.  
01:30:58: Understand the client's brand voice and  
01:30:59: current context. So on and so forth. If  
01:31:01: a website URL is provided or can be  
01:31:03: inferred from the email domain, then use  
01:31:05: this thing to fetch the client's landing  
01:31:07: page. Analyze all this information and  
01:31:09: output a brief summary. So I like this.  
01:31:11: I'm going to accept it. And then I'm  
01:31:12: going to say, "Yeah, sounds great. Let's  
01:31:14: give this a try.  
01:31:16: As part of this specific workflow, um, I  
01:31:18: have the model ask me a bunch of  
01:31:20: questions about the client. To be  
01:31:21: really, really straightforward here, I'm  
01:31:23: actually just going to open up chat GBT  
01:31:25: and then going to take a screenshot of  
01:31:27: this. I'll feed this in and I say, I'd  
01:31:30: like you to give me a bunch of example  
01:31:32: data here. I'm feeding this into a model  
01:31:34: for a demo, for a YouTube video.  
01:31:38: I'm then going to have Chat GPT  
01:31:39: construct a big list of demo  
01:31:41: information, and then I'm going to feed  
01:31:43: that in in a second.  
01:31:45: Okay, as you guys can see here, I have a  
01:31:46: bunch of data sets here. Um, they fed me  
01:31:49: in 10. I'm just going to use one, use  
01:31:52: this information for the demo.  
01:31:55: Cool. And now I'm sort of orchestrating  
01:31:56: multiple AI models. I am certainly using  
01:31:59: chatbt as a copy paste sort of thing,  
01:32:01: but I just wanted to show you guys that  
01:32:02: like this is data that is in a way real.  
01:32:06: It's data that is supplied outside of  
01:32:07: the system that I'm feeding into this  
01:32:09: workflow. I'm not having um Gemini  
01:32:10: itself within its own context come up  
01:32:12: with it. I'm giving it a bunch of  
01:32:14: information outside of things. Okay. And  
01:32:16: at the end of it, I actually have a  
01:32:17: fully functional proposal over here for  
01:32:19: bright path learning with an AI powered  
01:32:21: student success predictor. How cool is  
01:32:23: that? We have all of the problem  
01:32:24: statements, the solution statements.  
01:32:26: It's really clean. It's pretty nicely uh  
01:32:28: well done. Uh even includes some  
01:32:30: information here about pricing and so on  
01:32:32: and so forth. So, these are actual  
01:32:33: proposals that I sent to actual clients.  
01:32:34: As you guys see, we just generated a  
01:32:36: bunch of demo information for a  
01:32:38: hypothetical demo client that actually  
01:32:39: meaningfully altered a workflow in  
01:32:41: something like 30 seconds of actual  
01:32:43: work. Everything else is me just waiting  
01:32:44: for the model. Okay, so that was  
01:32:46: anti-gravity. Now, I just want to show  
01:32:47: you guys VS Code. And one of the reasons  
01:32:49: I want to show you guys this is because  
01:32:51: I want to show you that you can open up  
01:32:52: the same workspace on multiple different  
01:32:55: IDEs. You could actually create a  
01:32:57: workspace and then you could run it in  
01:32:58: anti-gravity, you could run it in VS  
01:33:00: Code, you could send it to your buddy  
01:33:02: who operates in cursor. There's so much  
01:33:04: that you could do here. It's fully  
01:33:05: interoperable. The only thing that  
01:33:07: really matters is the agent itself and  
01:33:10: then the workspace. You could swap out  
01:33:11: Gemini for GPT 5.2. You could swap that  
01:33:14: out for Claude Opus. I mean there  
01:33:15: there's just so many different options  
01:33:17: here obviously, but just want to give  
01:33:18: you guys um sort of a view into the fact  
01:33:20: that all the stuff is interoperable. It  
01:33:21: doesn't actually really matter what you  
01:33:22: use. So just pick whatever makes sense  
01:33:24: to you, what you enjoy. Okay. So VS Code  
01:33:26: works very similarly because the two are  
01:33:28: very heavily inspired by each other. Um  
01:33:30: on the lefth hand side we have the file  
01:33:31: editor. So right now I have the  
01:33:32: agents.mmd file open. Okay. So if I go  
01:33:35: over here you can see it's actually in  
01:33:36: the root directory. So I'm going to give  
01:33:37: that a click. That opens up the  
01:33:39: instruction file. Obviously I'm then  
01:33:42: feeding in um you know some very simple  
01:33:44: information here just saying run my  
01:33:45: Upwork scraper. It's actually gone  
01:33:46: through generated proposals pushed to a  
01:33:48: Google sheet. Same sort of idea. If I  
01:33:50: open up this Google sheet I have  
01:33:51: information about specific Upwork jobs.  
01:33:53: This took a few moments which is why I  
01:33:55: didn't do this in real time. Um in my  
01:33:57: case I was running a really simple  
01:33:58: workflow. I didn't want to edit a  
01:33:59: workflow here. or I actually just wanted  
01:34:00: to use one. And you'll see that there is  
01:34:02: a distinction between the building of  
01:34:03: the workflows and then the using of the  
01:34:04: workflows. In my case, I'm now using a  
01:34:06: workflow, not building it. Um, which is  
01:34:08: why I just had it say, "Hey, let's run  
01:34:10: this thing." The color scheme is  
01:34:12: slightly different. It looks slightly  
01:34:13: different. I'd say VS Code looks a  
01:34:15: little bit older, of course. But the  
01:34:16: most important thing that I'll show you  
01:34:17: that sort of distinguishes VS Code from  
01:34:19: a lot of things is just how big their  
01:34:21: extension library is. They really do  
01:34:22: support a tremendous number of  
01:34:24: extensions. If I just type the letter A,  
01:34:26: you'll see here that there are like  
01:34:27: hundreds of extensions that it opened.  
01:34:29: This is the search bar for all of the  
01:34:30: extensions. I could scroll down this  
01:34:32: thing for hours and probably never run  
01:34:34: out of things. Hell, I could probably do  
01:34:36: this for like the next two months or  
01:34:37: whatever and then I'd never run out of  
01:34:38: extensions. So, that's pretty cool.  
01:34:40: There's just a ton of different things  
01:34:41: you could do depending on what you're  
01:34:42: doing. There's code formatterers to  
01:34:43: change like the colors and stuff like  
01:34:45: that. Uh, you can kind of think of this  
01:34:46: as like I don't know who here plays  
01:34:48: video games, but it's kind of like  
01:34:49: Skyrim mods, Oblivion mods, you know,  
01:34:51: like you can just modify it to do  
01:34:53: whatever the heck you want, which is  
01:34:54: really awesome. Okay, you guys have now  
01:34:55: seen anti-gravity and VS Code in action.  
01:34:57: Let's talk a little bit more about the  
01:34:59: workspace itself. I've shown you guys  
01:35:00: how to operate within a workspace, but  
01:35:02: how do you actually set it up? Well,  
01:35:03: first thing is you have to obviously  
01:35:04: create a workspace. That's really easy.  
01:35:06: Anytime you open one of these IDs for  
01:35:07: the first time, the first thing it'll  
01:35:08: say is, "Hey, you should create a  
01:35:10: workspace." So, assuming you've done  
01:35:11: that, now you're inside of the  
01:35:12: workspace. What we have to do now is we  
01:35:14: have to set up the folder structure that  
01:35:16: our agent can understand and then  
01:35:17: navigate. We also need to give it some  
01:35:19: instructions that it knows how we  
01:35:21: structure the folder and why. And if you  
01:35:23: think about what I'm doing with you guys  
01:35:24: and then what I did with the agent with  
01:35:26: the agents.mmd file, I'm basically  
01:35:28: giving it a whole education as to why we  
01:35:31: are in the do framework, why we're using  
01:35:32: this to begin with. And I find that sort  
01:35:34: of context is really important. It's  
01:35:36: like a training uh session for your  
01:35:38: agent. Get them up to speed. Have them  
01:35:39: understand the methodology and the  
01:35:41: philosophy behind why you're using them  
01:35:43: in that way. And they'll typically work  
01:35:44: a lot better than if you just tried to  
01:35:46: raw dog it. So I think about this the  
01:35:47: same as like setting up a desk for an  
01:35:49: employee at your organization. They need  
01:35:51: to know where everything goes. They need  
01:35:52: to have like the base sort of things set  
01:35:54: up. They need to have the base folders  
01:35:56: and so on and so forth. Then once you've  
01:35:58: given them that structure, they can  
01:35:59: obviously excel within it. So I'm going  
01:36:00: to cover a lot more about this in the do  
01:36:02: section, but uh for now just know that a  
01:36:04: well organized workspace I would  
01:36:05: consider essential. So what is the  
01:36:07: actual project structure? Well, let me  
01:36:09: show it to you. We start off with the  
01:36:11: workspace itself. And you can name the  
01:36:14: workspace whatever you want. Now  
01:36:15: underneath the workspace, you then have  
01:36:17: two major folders. You have directives  
01:36:20: over here. Then right over here, you  
01:36:22: also have execution.  
01:36:25: Now, inside of directives, let me show  
01:36:27: you guys what that would look like. You  
01:36:29: have a bunch of files. So, you would  
01:36:31: have, for instance, scrape_leads.md.  
01:36:37: You might have another one, upwork  
01:36:41: applybot.md.  
01:36:44: These are your highlevel instructions  
01:36:45: where all of the top information goes.  
01:36:48: you know like hey start the scraping  
01:36:49: leads thing by asking the user what  
01:36:51: leads they want to scrape right once  
01:36:53: they've supplied those leads uh the  
01:36:54: directions to you then ask them what  
01:36:56: platform they want to use just some very  
01:36:58: highle stuff now underneath that as I  
01:37:00: mentioned we have the executions and  
01:37:02: then we have the actual like um Python  
01:37:04: scripts that correspond to the  
01:37:05: directives so over here for instance  
01:37:07: we'd have and let me just make this  
01:37:08: really really simple to see we'd have  
01:37:11: things like uh appify which is a  
01:37:14: platform scraper  
01:37:16: py I underneath that we'd have I don't  
01:37:19: know Upwork  
01:37:22: scraper  
01:37:24: py maybe underneath that we have upwork  
01:37:28: applier or something like that  
01:37:31: py and what essentially occurs in your  
01:37:33: directives is you just say somewhere  
01:37:35: within it hey step three I want you to  
01:37:37: call ampify scraper py it reads that in  
01:37:40: the directive and then it just knows  
01:37:42: which execution to call I have some  
01:37:44: recommendations here of course um use  
01:37:45: subfolders for inputs outputs, prompts,  
01:37:47: and reference materials. So that is sort  
01:37:49: of what the directives and the  
01:37:50: executions are. But if you, let's say,  
01:37:51: have a bunch of files that you feed in  
01:37:53: routinely as resources, you can  
01:37:55: absolutely add a resources folder. The  
01:37:58: only two folders that I would consider  
01:37:59: required in the DO framework anyway are  
01:38:01: just directives and executions. And  
01:38:03: depending on the framework, you know,  
01:38:04: people have different ideas about this,  
01:38:05: but you can add in whatever other  
01:38:07: folders you want. You could add a  
01:38:08: resources folder. A common folder to add  
01:38:09: is a TMP folder. That just stands for  
01:38:11: temporary. So sometimes agents um need  
01:38:14: to create files temporarily to do  
01:38:16: things. They use files like as like  
01:38:17: scratch pads. Uh my friend Gio yesterday  
01:38:20: was telling me about an experiment that  
01:38:21: somebody did where he had like a chat  
01:38:23: room for agents.mmd  
01:38:26: where basically he had multiple agents  
01:38:28: run simultaneously and then add things  
01:38:30: to a chat room. I mean obviously the  
01:38:31: world is your oyster here and I'm not  
01:38:32: going to try and force you in a specific  
01:38:34: way of being, but there are a variety of  
01:38:35: other folders that I would probably  
01:38:36: include as well. I'd include some clear  
01:38:39: naming conventions so the agent knows  
01:38:40: what lives where. For instance, if uh my  
01:38:42: thing scrapes leads, I would call it  
01:38:43: scrape underscore leads. I wouldn't call  
01:38:45: it like s_l with some naming convention.  
01:38:47: I mean, these character tokens are  
01:38:49: cheap, right? Be very descriptive with  
01:38:50: the titles of your files. And then if  
01:38:52: you have any documentation like the  
01:38:53: highle context and then you know like  
01:38:55: your agents  
01:38:57: MD and so on and so forth, make sure to  
01:38:58: include that as well. Talked about the  
01:39:00: directives and execution folders. So I'm  
01:39:02: going to leave that. Um directives  
01:39:04: generally holds things in markdown.  
01:39:06: That's important to understand, which is  
01:39:07: just a way to, you know, um mark up text  
01:39:09: a little bit. An execution is typically  
01:39:10: in Python, although that depends. And  
01:39:12: this is just that simple separation  
01:39:14: between what you do and then how you do  
01:39:16: it. So the directives are what you do  
01:39:18: and then the execution scripts are how  
01:39:19: the thing actually happens. I don't want  
01:39:21: to beat a dead horse here. Um the number  
01:39:23: one other thing that you guys really  
01:39:25: need to understand is this idea of an  
01:39:26: env file. So when you're working in any  
01:39:29: sort of programming environment,  
01:39:31: typically you don't want to store like  
01:39:33: passwords and secrets and API keys in  
01:39:35: the code itself. you want to store it in  
01:39:37: a separate area which um programmers  
01:39:39: have created a convention around called  
01:39:41: your env. That's just sort of like where  
01:39:43: you store all of your API keys, all of  
01:39:45: your credentials and so on and so forth.  
01:39:46: And the idea is instead of saying, "Hey,  
01:39:49: use this API key in your directive," you  
01:39:52: just say, "Hey, grab all your API keys  
01:39:54: from your env." That way, logically, if  
01:39:57: you ever wanted to share your directives  
01:39:58: later on, you could do so really easy.  
01:39:59: You would just copy and paste them. And  
01:40:01: I'm going to cover how to share and set  
01:40:02: up cloud-based instances later on. A lot  
01:40:04: of people ask me why these naming  
01:40:06: conventions exist, why an env.  
01:40:09: Some things in technology just are. You  
01:40:11: ever ask yourself why um JPEG files are  
01:40:14: called JPEG files? Well, it's because  
01:40:16: this is actually like an organization. I  
01:40:18: forget what the name of the organization  
01:40:20: is. It was like the journal for blah  
01:40:21: blah blah blah blah blah executive  
01:40:23: group, right? This is just a thing that  
01:40:26: has occurred 50 years ago that we all  
01:40:28: just must follow now. And if we change  
01:40:30: the name, then other people won't  
01:40:31: understand what they are. So it's just  
01:40:32: easier to stick with the name is widely  
01:40:35: recognized by basically everybody. So we  
01:40:37: just call these things and that's okay.  
01:40:39: Likewise there are some conventions  
01:40:41: right now between the models themselves.  
01:40:43: So for instance um I talked about system  
01:40:45: prompts things that you inject at the  
01:40:46: very top of any model conversation and  
01:40:49: there's a b a bunch of different ones  
01:40:51: right now. Claude.md corresponds to  
01:40:53: claude. Gemini.mmd is for gemini.  
01:40:56: Curser.md is for curser. agents.m MD is  
01:41:00: sort of like a general one that is  
01:41:02: supposed to be a fallback in case you  
01:41:03: don't have this specific one. And you  
01:41:05: know what I do? I just throw all of  
01:41:07: these in my main project route so that  
01:41:09: whatever model I use, I have the exact  
01:41:11: same sort of thing. So I will copy the  
01:41:13: same thing from agents MD to cloud MD to  
01:41:15: Gemini. MD to cursor MD. This  
01:41:17: interoperability is really really easy.  
01:41:19: And obviously these names matter. Just  
01:41:21: because somebody said, well, we should  
01:41:22: probably have some configuration file.  
01:41:24: Why don't we just call it claude MD? We  
01:41:26: use capitals because that'll stand out  
01:41:27: and make it like hypersp specific and  
01:41:29: differentiable and then other people  
01:41:31: sort of went on that bandwagon and  
01:41:32: that's how it is. If you upload a  
01:41:33: gemini.mmd to claude then claude isn't  
01:41:36: going to understand what that is.  
01:41:37: They're not going to automatically  
01:41:38: insert it. But if you upload a claude.md  
01:41:40: to claude it will. If you upload uh you  
01:41:42: know agents.mmd or codecs or cursor or  
01:41:44: whatever to your various models of  
01:41:45: choice it'll understand what's going on.  
01:41:47: The really cool thing is you just create  
01:41:49: the structure one time and then the  
01:41:51: agent just works with it for every  
01:41:52: project going forward. Which is one of  
01:41:54: the reasons why I love this. The  
01:41:56: initialization is so easy that I now  
01:41:58: don't even tell people to initialize it  
01:41:59: themselves. I just give the agents item  
01:42:02: D file to anybody I want to set up and  
01:42:04: then I just say hey have your model do  
01:42:06: it. Then they just go to their agent and  
01:42:07: they say hey can you set up my workspace  
01:42:09: according to this file and then it does  
01:42:11: so automatically. How cool. I want you  
01:42:12: guys to know that as you get better and  
01:42:14: better with IDE, this feeling of  
01:42:16: overwhelm will decrease. But at the  
01:42:18: beginning, it is totally normal to feel  
01:42:20: overwhelmed with the menus and the  
01:42:21: panels and the buttons and all the  
01:42:23: keyboard shortcuts. Um, it's just like a  
01:42:25: beginner pilot looking at cockpit  
01:42:27: instrumentation right now. I think I  
01:42:28: told you guys that I was taking my  
01:42:29: pilot's license and it is it is really  
01:42:31: intimidating. This is the exact same way  
01:42:33: that I tried to put myself in your guys'  
01:42:35: shoes when explaining this. I wish  
01:42:36: somebody explained pilot instrumentation  
01:42:38: to me the same way I'm explaining ID  
01:42:40: instrumentation to you. But you don't  
01:42:41: need to learn everything at once. And  
01:42:43: hopefully it's clear, as long as you  
01:42:44: understand those three things, the file  
01:42:46: explorer on the lefth hand side, the  
01:42:47: editor in the middle, and then the agent  
01:42:49: chat on the right hand side, you're  
01:42:51: already 80% of the way there, and you  
01:42:52: can build and use Agentic Workflows for  
01:42:54: your own business. The goal isn't to  
01:42:56: master every feature here. It's just to  
01:42:57: be comfortable enough that the ID  
01:42:59: doesn't like slow you down. Okay, so let  
01:43:01: me show you how you can easily build  
01:43:02: proposals and high-quality PDFs and  
01:43:04: visual assets with Agentic Workflows.  
01:43:07: This is an example of a workflow that I  
01:43:08: use all the time in my day-to-day  
01:43:09: business. So immediately underneath this  
01:43:11: I have a sales call transcript.  
01:43:13: Essentially what we do is we feed in  
01:43:14: these sales call transcripts and we just  
01:43:16: tell the model hey I want you to  
01:43:17: generate a proposal with it. So what am  
01:43:19: I going to do? I will literally just say  
01:43:21: generate a proposal using the below  
01:43:22: transcript. Then I'm going to press  
01:43:25: enter. What's going to happen is this  
01:43:27: model is going to immediately start  
01:43:29: looking through the existing directives  
01:43:32: which I'll talk a little bit about more  
01:43:33: later in the course. It'll find contact  
01:43:36: details and everything that we need in  
01:43:37: order to actually send the proposal  
01:43:39: because I removed the email from this  
01:43:41: specific one. I am going to supply just  
01:43:43: a demo email. What its reasoning is  
01:43:45: doing is it's extracting the main  
01:43:46: problem areas, the main solution areas,  
01:43:48: the things that we talked about and also  
01:43:50: the pricing. Immediately afterwards,  
01:43:51: it's going to ask me for the email  
01:43:53: address. This is a demo, so just use  
01:43:57: and I'm going to provide my own.  
01:44:01: And once it has this information, it can  
01:44:03: proceed and actually go through with the  
01:44:04: generation of the asset. So it's not  
01:44:06: formatting this in the way that I want  
01:44:07: the proposals to look like. Keep in mind  
01:44:09: that I had no real work here aside from  
01:44:11: copying my transcript over. And even  
01:44:13: that is unnecessary. I could have just  
01:44:14: used it directly from the transcript  
01:44:16: provider Fireflies, but I wanted to show  
01:44:17: you guys how malleable this sort of  
01:44:19: thing is. Whether you copy and paste it  
01:44:21: in, whether you put an API call to like  
01:44:23: some transcript endpoint in, uh, you  
01:44:24: know, it works the same regardless.  
01:44:26: Great. And it's finished. Now it's going  
01:44:28: to do is send a quick follow-up email.  
01:44:30: And the email was sent successfully just  
01:44:32: using an MCP server that I set up. And  
01:44:34: now we get a summary as well as a link  
01:44:37: so we can view it directly.  
01:44:40: When I open this up, you can see the  
01:44:41: proposal document right here. It  
01:44:43: includes um you know your problem areas.  
01:44:46: Number one, your revenue is  
01:44:47: unpredictable because you're relying on  
01:44:48: referrals and sporadic outreach. One  
01:44:50: month may bring three clients, the next  
01:44:51: month brings zero. The feast or famine  
01:44:53: cycle makes it impossible to plan  
01:44:54: hiring, delivery capacity, or growth  
01:44:55: investments with any confidence. This is  
01:44:57: all stuff that the AI came up with. You  
01:44:59: know, I chatted about this briefly on  
01:45:00: the transcript, of course, but um  
01:45:02: everything else here, the tone of voice  
01:45:04: and everything like that was just a very  
01:45:06: simple highle prompt instruction as well  
01:45:08: as a brief example. The actual workflow  
01:45:10: here took me maybe 15 minutes to set up  
01:45:12: and to end. And as you can see now with  
01:45:14: just a prompt, uh I can generate  
01:45:15: high-quality sales proposals within  
01:45:17: seconds. So, this is what you are going  
01:45:19: to learn how to do. You're going to  
01:45:20: learn how to set up workflows, not only  
01:45:22: to do things like generate proposals,  
01:45:24: although I absolutely recommend you do  
01:45:25: if you're in any sort of service  
01:45:27: business where you have sales calls, but  
01:45:28: we can do more or less anything. I've  
01:45:30: set up dozens of workflows to automate  
01:45:32: many of the mundane routine business  
01:45:34: tasks that I have. Things that just a  
01:45:36: few years ago, people probably would  
01:45:37: have raised an eyebrow at you and  
01:45:38: thought you were crazy for suggesting  
01:45:40: you can automate something like this.  
01:45:42: All right, it's now time to talk about  
01:45:43: DO directive orchestration and  
01:45:45: execution. So up at the very top of  
01:45:47: this, you can see that I've written  
01:45:48: three layer software architecture.  
01:45:51: That's because that's what DO is. It is  
01:45:52: a three layer system that we're wrapping  
01:45:55: around an AI agent in order to help  
01:45:58: constrain its outputs and take it from  
01:46:01: like a probabilistic thing which is all  
01:46:02: over the place to something very  
01:46:04: standard, consistent, and deterministic.  
01:46:07: So at the very top of this system is  
01:46:09: your directive layer. Of course, this is  
01:46:11: going to include workflows and SOPs. And  
01:46:14: by the way, if you don't know what SOP  
01:46:15: means, that stands for standard  
01:46:18: operating procedure. And standard  
01:46:21: operating procedures are very common in  
01:46:23: any sort of business, which is one of  
01:46:24: the reasons why I like Do so much  
01:46:27: because all you really do is just import  
01:46:28: your standard operating procedures in  
01:46:30: whatever business you are working with,  
01:46:31: whether it's your own or business you're  
01:46:32: helping. Then you just say, "Hey, turn  
01:46:34: this into a directive as per do." And  
01:46:36: boom, you're done. You now have like an  
01:46:37: AI agent that just does tasks that your  
01:46:39: company needs to do. So up at the very  
01:46:42: top kind of the first layer is this  
01:46:43: directive. Now underneath you have the  
01:46:46: orchestration layer. Your orchestration  
01:46:48: layer is your AI agent or AI employee in  
01:46:51: a way. And you'll also see that like not  
01:46:54: only did I put a little robot face here,  
01:46:55: but I also put a person. And the reason  
01:46:57: why is because it's actually pretty  
01:46:58: similar to how most organizations work.  
01:47:00: You have some highle directives. Those  
01:47:01: directives are read by employees or you  
01:47:04: know other people in the business. And  
01:47:06: then what they do is they just make  
01:47:07: decisions surrounding how to accomplish  
01:47:09: the highle uh directives. This is where  
01:47:12: they perform coordination, task  
01:47:13: management, and stuff like that. And  
01:47:15: what they do with those decisions is  
01:47:17: they call or use tools. Now, if you're  
01:47:20: an AI agent, you're going to be using  
01:47:22: mostly software tools as expected. Hell,  
01:47:24: if you're an employee, for the most  
01:47:25: part, you're going to be using software  
01:47:26: tools. Now, think of the tools that an  
01:47:28: average employee uses in any  
01:47:29: organization. We're using Google Sheets,  
01:47:31: Excel. We're using Microsoft Word, Docs,  
01:47:33: right? All of those things are actually  
01:47:35: analogous to tools that we use within an  
01:47:38: organization to accomplish things. It's  
01:47:40: the same thing that our AI does with  
01:47:42: tools that it creates. Okay. So down at  
01:47:44: the very bottom here, you have the  
01:47:45: execution layer and this contains tools.  
01:47:48: It contains Python scripts and so on and  
01:47:49: so forth. It's primarily responsible for  
01:47:51: action and output. I don't want people  
01:47:54: here to be really scared or worried  
01:47:56: about DO. It's a lot simpler than you  
01:47:58: may think. The thing is we just need to  
01:47:59: frame it as like a three- layer software  
01:48:01: architecture in order for the rest of  
01:48:02: the course to make sense. So to be  
01:48:04: clear, do is literally just a folder  
01:48:06: structure plus a system prompt. And  
01:48:09: pretty much all frameworks out there  
01:48:10: right now for aentic workflows are all  
01:48:13: we do is we just set up a folder called  
01:48:15: directives and a folder called  
01:48:17: execution. Then we add some files like  
01:48:19: an agents MD, cloud MD or Gemini MD as  
01:48:22: our prompt and then you know we might  
01:48:23: add avi keys etc. Again, the API uh env  
01:48:28: is literally just a convention that, you  
01:48:30: know, some programmers made forever ago.  
01:48:32: So, it's great for beginners primarily  
01:48:34: because it's intuitive and it's really  
01:48:35: easy to understand. And it's also really  
01:48:37: cool for businesses because we can just  
01:48:38: copy and paste SOPs directly in like um  
01:48:41: a company that I'm currently working  
01:48:42: with right now does marketing  
01:48:43: specifically for dental practices and  
01:48:45: they do about $2 million a year. And  
01:48:47: when I introduced agentic workflows to  
01:48:49: them, you know, I'm kind of like in a  
01:48:51: meeting I met with the director and I  
01:48:52: started discussing how, hey, you know, I  
01:48:53: think we could probably automate a  
01:48:54: couple of the previously non-automatable  
01:48:55: tasks with aentic workflows, he's like,  
01:48:58: okay, so how do we start? And I was just  
01:48:59: like, well, you guys got a knowledge  
01:49:00: base. Why don't I just feed the entire  
01:49:01: knowledge base in and see what happens?  
01:49:03: And within 15 minutes or so, we had  
01:49:05: actually like procedurally turned most  
01:49:07: of those things into agentic workflows.  
01:49:10: We had all of the the API keys. We had  
01:49:12: everything that we needed preset which  
01:49:13: was lucky cuz a lot of the time you have  
01:49:15: to jump around and you know finagle  
01:49:17: various services. Um but yeah within 15  
01:49:19: minutes we had turned this into dough  
01:49:21: and we now have a workspace that you  
01:49:22: know the director managers and myself  
01:49:24: can use to do like 90% of the  
01:49:26: economically valuable work. Is that  
01:49:28: going to lead to some headcount  
01:49:28: reduction? Probably. I mean when you  
01:49:31: automate 90% of 10,000 people's roles  
01:49:33: obviously you need to take a step back  
01:49:34: and start doing more management style  
01:49:36: stuff than actually getting your hands  
01:49:37: dirty. Uh but yeah, that's just a very  
01:49:39: simple and straightforward example of  
01:49:40: something that I have actually just just  
01:49:41: now done. The reason why dough works  
01:49:44: really is because of the whole  
01:49:45: stochasticity idea. And stochasticity  
01:49:47: just for anybody that's like why the  
01:49:48: heck is Nick using all of these crazy  
01:49:50: words. It's just the way to formalize  
01:49:52: randomness I would say. I mean it's a  
01:49:54: little bit different but for for our  
01:49:55: purposes you could use that. So it just  
01:49:56: takes this big like if this is like the  
01:49:59: total range of possible outcomes. Okay?  
01:50:01: You know you could do uh this outcome  
01:50:03: you could do outcome somewhere here. You  
01:50:04: could do this outcome you could do  
01:50:06: outcome somewhere here. All DO does is  
01:50:08: it just reduces this so that the range  
01:50:09: of possible outcomes is a lot more  
01:50:11: narrow. And so, you know, for the most  
01:50:13: part, we're operating within a very  
01:50:15: tightly bounded range of possible  
01:50:16: outcomes for our system. It can do this  
01:50:18: or it could do that. And it's very, very  
01:50:20: similar uh because we do this through  
01:50:22: the separation of concerns. It's just a  
01:50:24: lot more reliable. This lets me get to 2  
01:50:26: to 3% error rates on a lot of business  
01:50:28: functions. That dental uh marketing  
01:50:30: business that I was talking about  
01:50:31: earlier is a great example of that. It's  
01:50:33: really not more complicated than that. I  
01:50:35: also like to think of it as I don't know  
01:50:36: if you guys have ever gone bowling or  
01:50:37: something, but uh this is going to be my  
01:50:39: crappy  
01:50:41: bowling pin thing. Um you know,  
01:50:44: typically the way that bowling works is  
01:50:45: you have gutters on the side and you  
01:50:47: know if your bowling ball is not very  
01:50:48: good or if you are not very good at  
01:50:50: bowling I should say. Um you know like a  
01:50:53: lot of the time it's going to veer off  
01:50:54: into the gutter and then you're screwed,  
01:50:55: right? So as a total newbie, one thing  
01:50:58: that I really like doing is I like  
01:50:59: asking them to set up the guardrails. So  
01:51:01: I say, "Hey, do you mind setting up the  
01:51:02: guardrails for me?" Then they set up  
01:51:04: these little guardrails that basically  
01:51:06: prevent the ball from um landing. And so  
01:51:09: what ends up happening is I basically  
01:51:11: will bump off of a wall and then I still  
01:51:13: get to hit some pins. That's all dough  
01:51:15: is for agents. It just constrains it. We  
01:51:17: just give it some guardrails and then we  
01:51:18: significantly improve the probability  
01:51:19: that it does something that we want. So  
01:51:21: I'm going to go very into detail here  
01:51:23: and be very comprehensive because this  
01:51:24: is the framework we're using for the  
01:51:25: rest of the program. You've already seen  
01:51:27: me use this a bunch through the various  
01:51:28: demos that I've I've created. Now I just  
01:51:30: want to provide context for everything.  
01:51:31: If some of this stuff is repetitive or  
01:51:33: if you think you already know this  
01:51:34: stuff, that's okay. I would recommend  
01:51:35: just watching it regardless. Try and  
01:51:37: internalize as much of this as possible  
01:51:39: because this is the same idea that any  
01:51:40: framework uh is going to use. So the  
01:51:43: directives obviously are SOPs written in  
01:51:45: natural language as markdown files.  
01:51:47: Markdown is very important. File ending  
01:51:50: all will end in MD. That's obviously  
01:51:53: stands for markdown. Uh and generally  
01:51:55: speaking, this is just a sort of like  
01:51:57: markup language.  
01:51:59: A markup language just formats text. So  
01:52:03: this is plain text for instance, right?  
01:52:04: First SOPs are written in natural  
01:52:05: languages as markdown files. Uh uh uh  
01:52:08: you know marked up version of this might  
01:52:09: be first. Let me make sure I got this  
01:52:12: right. You had some stars. SOPs and now  
01:52:14: this is bolded text are written in you  
01:52:17: know natural language. And so now it's  
01:52:19: like quoted text as markdown files. What  
01:52:21: we're doing is we're taking text and  
01:52:22: then we're just marking it up. We're  
01:52:23: adding some structure to it basically.  
01:52:25: Um markdown is just one way to do so.  
01:52:27: So, for instance, this on a page is  
01:52:28: actually markdown underneath it. Um, I  
01:52:30: used markdown to help uh I used AI  
01:52:32: actually to help me convert a big  
01:52:33: 17,000word document into um a slideshow.  
01:52:36: And so, this was actually a heading. And  
01:52:38: the way you demonstrate or the way you  
01:52:40: use headings in markdown is you use  
01:52:41: little number signs. So, for instance,  
01:52:43: if I wanted to write this big heading, I  
01:52:44: actually would have written this layer  
01:52:47: one, you know, directives.  
01:52:50: Underneath that, you have bullet points.  
01:52:51: Bullet points in markdown are little  
01:52:53: stars. So star first, you know, s os are  
01:52:58: written, right? So all of these little  
01:53:00: characters are just a ways that you add  
01:53:02: formatting to text. And the reason why  
01:53:03: we do this for our AI agent for  
01:53:05: directives is because formatting allows  
01:53:07: us to add a lot moreformational content  
01:53:09: to the text. It also allows us to  
01:53:11: structure things. So it's not just one  
01:53:12: giant massive text dump. We add we get  
01:53:14: to add new lines. We get to add various  
01:53:15: tabs for indentation. Basically, we just  
01:53:17: add a bunch of structure to things as  
01:53:20: opposed to it just being this, right? we  
01:53:22: basically convert it into something that  
01:53:24: is a lot more interesting. We have  
01:53:26: spaces and we have little bullet points  
01:53:28: and you know the structure of the text  
01:53:30: kind of looks like a face funnily enough  
01:53:31: you know allows us to impart a lot more  
01:53:33: information per token and then it's also  
01:53:35: token efficient. There are other  
01:53:36: markdown languages as well. One that  
01:53:38: you've probably heard of before is or  
01:53:40: markup languages as well. One that  
01:53:42: you've probably heard before is called  
01:53:43: HTML. With HTML the way you mark things  
01:53:45: up is you use a variety of tags. And so  
01:53:48: tags are these little number sign  
01:53:49: things. If I were to try and write the  
01:53:51: same thing in tags, it would be  
01:53:53: significantly less token efficient and  
01:53:55: so I'd actually have written way more um  
01:53:58: total tokens, which obviously would have  
01:54:00: consumed a lot of my context. So instead  
01:54:02: of that, okay, instead of the HTML body,  
01:54:06: H1 layer 1 directives, H1, whatever, all  
01:54:08: we're doing to to accomplish the same  
01:54:10: thing is I literally just do a number  
01:54:11: sign. Obviously, this is one character.  
01:54:12: That's like, I don't know, however many  
01:54:13: characters, way more, obviously, to just  
01:54:15: um demonstrate some some structure  
01:54:17: there. Okay, so that's markdown. Now,  
01:54:20: these define your goals. They define  
01:54:22: your inputs. They define your tools,  
01:54:23: your expected outputs, edge cases, and  
01:54:26: ultimately a lot of other things that  
01:54:27: you can define. I don't proclaim to have  
01:54:29: the perfect directive creation  
01:54:30: structure. I'm going to show you my own  
01:54:31: directive creation structures, and that  
01:54:33: tends to include all these things, but  
01:54:34: um in general, you just want to provide  
01:54:36: highle overviews. Now, the way I write  
01:54:38: these or the way I have AI write these  
01:54:40: is I write them like I'd instruct a  
01:54:42: competent employee. I would make them  
01:54:43: clear, but I would not micromanage. And  
01:54:45: really, AI does this for you. All I do  
01:54:47: is I describe the what and the highle  
01:54:49: hows of my task in markdown and then I  
01:54:51: just trust the agent to figure out the  
01:54:52: rest. I'm going to remember to drink  
01:54:53: this tea cuz it is going to get cooled.  
01:54:59: Damn, that stuff's good. Holy.  
01:55:02: So directives obviously live in the  
01:55:04: directives folder in our workspace. The  
01:55:06: way I separate each directive is as a  
01:55:08: separate markdown file that covers one  
01:55:10: workflow or one capability. For  
01:55:13: instance, I would have a scrape_leads.  
01:55:18: MD file, but I wouldn't have a run  
01:55:23: business MD file just because, and maybe  
01:55:26: we'll get to this point later, I don't  
01:55:27: know, but um just because this is a lot  
01:55:29: that we're asking from the model. And so  
01:55:30: the model typically starts looping over  
01:55:31: and and doesn't really understand  
01:55:33: various edge cases and stuff like that.  
01:55:35: I constrain these into sort of like  
01:55:38: modular directives. And then later on I  
01:55:40: can actually group them with umbrella  
01:55:42: directives. Not umbrella to the point  
01:55:44: where it's literally like hey run my own  
01:55:45: business but umbrella to the point where  
01:55:47: it's like hey you know run onboarding  
01:55:49: flow or something like that. So some  
01:55:51: examples lead scraping MD proposal  
01:55:53: generation MD email_enrichment MD and so  
01:55:56: on and so forth. I highly recommend  
01:55:58: making the names descriptive. Logically  
01:56:00: speaking these are the only things that  
01:56:03: uh descriptives descriptive um this is  
01:56:05: the only way that like the model can  
01:56:06: tell kind of what's going on here. You  
01:56:08: can of course add um some other forms of  
01:56:11: structure to the text. You could add  
01:56:12: what's called YAML front matter, which  
01:56:13: I'll talk about a little bit more later  
01:56:15: on. But for the most part, like the  
01:56:16: model just consumes the name and then  
01:56:18: uses that name to determine which  
01:56:19: workflows it's going to use. If I say,  
01:56:20: "Hey, I want you to scrape some leads,"  
01:56:22: obviously it's going to do the lead  
01:56:22: scraping one, right? But if I just  
01:56:24: called that L_S with some  
01:56:26: naming convention, it would have no idea  
01:56:27: what it's doing. So very important here  
01:56:29: to just like be descriptive. Don't use  
01:56:30: acronyms. Don't use anything that like  
01:56:32: complexifies the names of the directives  
01:56:35: if you want the agent to be able to use  
01:56:36: it as best it can.  
01:56:40: Very important point is that directives  
01:56:42: contain no code at all. There is zero  
01:56:44: code within a directive. All directives  
01:56:46: are are natural language instructions.  
01:56:49: We don't have any code, no executables.  
01:56:51: And really there's there's very little  
01:56:52: technical here. You know, I may [snorts]  
01:56:53: include some URLs. I say, "Hey, go to  
01:56:55: this URL in order to get information  
01:56:57: about this." But I'll never actually  
01:56:58: include any sort of code or executable.  
01:57:02: The reason why is because we want these  
01:57:03: directives to remain readable by all  
01:57:05: humans within the organization. And they  
01:57:07: should just make sense to all people  
01:57:08: within the company. If your directives  
01:57:10: are to the point where they're so  
01:57:12: technical and confusing that like any,  
01:57:14: you know, average low-level staff member  
01:57:16: within the business could not read it  
01:57:17: and understand what's going on, you've  
01:57:18: screwed up. The whole idea is that you  
01:57:21: want to lower the barriers to entry so  
01:57:22: that anybody in your company that is  
01:57:24: system-minded, they don't have to be  
01:57:25: technical, but they have to know systems  
01:57:27: can actually just improve things. You be  
01:57:29: like, "Oh, um, yeah, take a look at that  
01:57:30: directive and let me know if there's  
01:57:31: anything that you think I'm missing."  
01:57:32: And then they just read it natural  
01:57:33: language and they go, "Oh, you know, uh,  
01:57:35: sometimes customers ask for X, Y, and Z.  
01:57:37: We should probably add some logic  
01:57:38: there." Right? You want that person to  
01:57:40: actually be able to substantially  
01:57:41: improve the organization. You don't just  
01:57:42: want it to be like a black box. Because  
01:57:44: that's one of the main benefits of this,  
01:57:46: right? We're making this really, really  
01:57:47: interpretable. removing bottlenecks  
01:57:48: across the organization to have people  
01:57:50: see and understand how uh the systems in  
01:57:52: the business work. Okay, so next up  
01:57:54: we're going to talk about layer two  
01:57:55: which is orchestration. This is kind of  
01:57:57: like the who. Um orchestration is  
01:57:59: basically a competent project manager.  
01:58:01: So a good project manager in business  
01:58:02: rarely actually does the hands-on work  
01:58:04: themselves. They're basically just like  
01:58:06: a nexus and that nexus takes information  
01:58:08: in and then it kind of puts information  
01:58:10: out. And you know this might be person  
01:58:13: one, person two, person three. They're  
01:58:15: going to take inputs from these three  
01:58:16: sources. They're going to do some  
01:58:18: thinking and then they're ultimately  
01:58:19: going to go and delegate some additional  
01:58:20: work to person 1 2 and 3. So they make  
01:58:22: routing decisions at the end of the day  
01:58:24: and they take advantage of available  
01:58:25: tools. If you think about old school no  
01:58:27: code flows like NAD and stuff like that,  
01:58:29: this job was basically done by you and  
01:58:31: you would orchestrate it once when you  
01:58:33: built the flow. You'd say this node goes  
01:58:35: to this node, this node goes to that  
01:58:37: node, that node goes to that node, that  
01:58:40: node goes to that node. Maybe this thing  
01:58:42: loops around a little bit and then  
01:58:44: eventually we, you know, do this node or  
01:58:46: something like that. This is a decision  
01:58:48: that you would make once when you built  
01:58:50: the flow. What's really cool is the  
01:58:52: orchestrator basically just does all of  
01:58:54: that on its own. So if I just show you  
01:58:56: guys as like a practical example here,  
01:58:58: the orchestrator  
01:59:02: instead just compiles all the tools and  
01:59:05: then at runtime it decides, hey, you  
01:59:08: know, I actually want to do this and  
01:59:09: then this is actually going to go over  
01:59:10: here. After that's done, it's going to  
01:59:12: go over here. That's going to go over  
01:59:13: here. We're going to loop back three  
01:59:15: times over there, start over here, and  
01:59:16: then we'll finish over here. And because  
01:59:19: it's flexible, it can adapt to any  
01:59:21: situation at the time that you are  
01:59:23: asking it to do things. You just give it  
01:59:24: tools and then it just does all the  
01:59:26: routing and stuff like that for you.  
01:59:27: Obviously, we want to provide at least  
01:59:28: some structure, right? We don't want to  
01:59:30: just give it a bunch of tools and say,  
01:59:31: "Hey, figure it out." That's what our  
01:59:32: directives are for. So, it does ensure  
01:59:34: work gets completed according to those.  
01:59:36: But the flexibility here allows it to  
01:59:38: deal with situations like when something  
01:59:40: breaks, how to diagnose the problem  
01:59:41: rather than just crash and and you know,  
01:59:43: 404. And then later on if you use sub  
01:59:45: aents like I recommend throughout the  
01:59:47: program um we're going to have like a  
01:59:48: document flow that not only will go  
01:59:51: through see uh workflow end to end if  
01:59:54: there's any problems it'll diagnose it  
01:59:55: and so on and so forth it'll actually go  
01:59:57: back and it'll document for the purposes  
01:59:59: or rather the benefits of future  
02:00:00: instances of the agent um you know  
02:00:02: changes that it made things that you  
02:00:04: know the agent needs to keep in mind  
02:00:06: logical errors that you know maybe  
02:00:08: agents typically make to avoid API  
02:00:11: exceptions that don't really make sense  
02:00:12: or work and so on and so forth.  
02:00:14: All right, layer three is execution,  
02:00:16: which is the how. So, logically  
02:00:18: speaking, execution is deterministic.  
02:00:20: It's very modular. It's very  
02:00:21: straightforward. Doesn't mean it's  
02:00:23: simple. The execution scripts are stored  
02:00:25: in the execution folder. I typically  
02:00:27: just use Python for this. Why? Cuz the  
02:00:29: programming language doesn't really  
02:00:30: matter to be honest. And when you have  
02:00:32: Python, like at any point in time, if  
02:00:34: you needed to, you could convert this  
02:00:36: into whatever the heck you want. You can  
02:00:37: convert Python into Rust, you can  
02:00:39: convert uh into Node, you could convert  
02:00:40: it into Java. I mean, like whatever  
02:00:42: language you want really. These things  
02:00:43: are all [snorts] essentially just  
02:00:45: conversions of natural language at this  
02:00:46: point. Anyway, each script handles just  
02:00:49: one thing. So, one job or one task. I'll  
02:00:51: give you an example just using what we  
02:00:53: talked about earlier. So, if I have like  
02:00:54: a scrape leads directive, this is like  
02:00:57: the highle kind of workflow. Right? Now,  
02:01:00: this workflow isn't just going to have  
02:01:01: one, you know, scrape_leads.py  
02:01:06: script. This might actually have  
02:01:08: multiple different scripts. This might  
02:01:09: have uh you know depending on whatever  
02:01:11: you're using might be like  
02:01:13: scrape_appify.py  
02:01:17: might have like a upload to gsh sheet.py  
02:01:23: hell might even have if you have to make  
02:01:25: some interface or something present  
02:01:28: to user.py.  
02:01:31: But the point is these things all just  
02:01:33: do one thing really well. So this one  
02:01:34: scrapes appy really well. This one  
02:01:36: uploads to a Google sheet really well.  
02:01:37: This one presents to a user really well.  
02:01:39: These are just like things that you know  
02:01:40: you like like tools that an agent can  
02:01:42: use in order to do some task. So what  
02:01:45: happens is because they're  
02:01:46: deterministic, they do the exact same  
02:01:48: thing every time when given the same  
02:01:50: inputs. So like if I were just to I  
02:01:52: don't know do this raw dog it and just  
02:01:54: feed in some prompt to my agent and say,  
02:01:56: "Hey, I want you to scrape aify for X,  
02:01:57: Y, and Z." And I had no tools and no  
02:01:59: directives, you know, it would  
02:02:01: eventually figure out what I wanted to  
02:02:02: do. But if I did it 10 times, you know,  
02:02:04: on route one, it would go from here  
02:02:07: to here and then on route two would feed  
02:02:09: back and route three, you know, we just  
02:02:12: have fundamentally different um  
02:02:13: executions every single time, right?  
02:02:15: When you have the exact same inputs  
02:02:17: provided to the exact same execution  
02:02:19: scripts and then you get the exact same  
02:02:20: outputs, it becomes very obvious like  
02:02:22: what the model needs to do and you  
02:02:23: heavily constrain the inputs and outputs  
02:02:25: uh and you essentially just provide a  
02:02:27: simple rule. Hey, you know, if I say,  
02:02:29: hey, scrape appy or whatever, uh, for  
02:02:32: Texas, uh, for 200 people, it'll  
02:02:34: actually feed that in as a parameter to  
02:02:35: the scrape appy. It'll actually like  
02:02:37: have dash dash, you know, location  
02:02:40: equals Texas, for instance, and then d-  
02:02:45: um, you know, amount equals 200 or  
02:02:47: something like that. And because we are  
02:02:49: being extraordinarily explicit here,  
02:02:50: there's never any misunderstanding. So,  
02:02:52: the agent just always knows what to  
02:02:53: expect. So, do you. Another example here  
02:02:55: would be a scrape_apollo. That would  
02:02:57: scrape leads from Apollo, but maybe you  
02:02:59: also enrich the leads. Well, now you  
02:03:01: have enrich_clearb. Maybe that enriches  
02:03:03: company data via that tool. Maybe you  
02:03:05: then have a send email that sends emails  
02:03:07: via specified service and then a create  
02:03:09: pandock which generates proposals. What  
02:03:11: you'll quickly realize is when you build  
02:03:12: a sufficient enough library of tools,  
02:03:14: you can have multiple directives  
02:03:16: reference the same tools. Like for  
02:03:17: instance the send email pi maybe as part  
02:03:20: of my scrape_leads.mmd  
02:03:24: directive I always send an email with a  
02:03:27: summary of the leads right so maybe you  
02:03:29: know somewhere here I say hey you know  
02:03:30: generate the the leads scrape it with  
02:03:31: apolla and then send an email well what  
02:03:33: about the create panadoc maybe in the  
02:03:35: create panadoc uh maybe I have like a  
02:03:37: generate proposal MD well the generate  
02:03:39: proposal MD um also needs to send an  
02:03:43: email what's really cool is when you  
02:03:45: define these atomic functions Both of  
02:03:47: these can call the same execution  
02:03:49: script. And because we've optimized the  
02:03:52: hell out of these execution scripts by  
02:03:54: rerunning and self- annealing and all  
02:03:55: this stuff, which we'll talk about  
02:03:56: later, um, this is really robust and it  
02:03:58: basically like works every time.  
02:03:59: Execution scripts are not AI for the  
02:04:01: most part. They don't hallucinate. They  
02:04:03: don't make things up. They basically  
02:04:04: either work correctly or they throw a  
02:04:05: clear error. So there's no ambiguity.  
02:04:06: There's a programming term here called  
02:04:08: unit testing, which basically means like  
02:04:10: you can like isolate this down to its  
02:04:12: barebones function, just its input and  
02:04:14: its output, and you can just test that.  
02:04:15: You can version control them. So you can  
02:04:17: have like a log of updates and you can  
02:04:19: optimize them independently. You could  
02:04:20: start with like um some sort of serial  
02:04:22: flow where it goes one and then it does  
02:04:24: two and then it does three and then  
02:04:26: after a few runs maybe it'll come up  
02:04:28: with a more efficient way to do things.  
02:04:29: For instance, maybe it'll split it and  
02:04:31: it'll parallelize one, two, and three  
02:04:33: and then recombine the inputs or  
02:04:35: something for some API call. Uh the  
02:04:37: options here are virtually limitless. Um  
02:04:38: but because they don't guess or  
02:04:40: hallucinate, you can just incrementally  
02:04:41: improve these things over time. I had  
02:04:42: this question come up the other day, so  
02:04:44: I figured I'd answer it in this course.  
02:04:45: Um, nothing says you can't actually use  
02:04:47: AI inside of your scripts. For instance,  
02:04:49: you might have a thing called process  
02:04:53: leads with,  
02:04:56: you know, claude. py that, uh, I don't  
02:04:59: know, it feeds in a bunch of leads or  
02:05:01: grabs the leads from like a Google doc  
02:05:02: or something or Google sheet and then it  
02:05:05: just like passes them all through Claude  
02:05:06: and has you tell something about each  
02:05:07: lead. I don't know, whatever the heck  
02:05:09: you want this to say. Well, you can  
02:05:10: still use AI to do that for you, right?  
02:05:12: It's still passing it into Claude. It's  
02:05:14: just doing so in a much more predictable  
02:05:16: way because you are defining it within a  
02:05:18: single workflow as opposed to just like  
02:05:19: giving it full orchestrator access. Like  
02:05:21: for instance, your process leaves with  
02:05:22: Claude would probably start by like  
02:05:24: reading the sheet, right? That's  
02:05:25: probably what's going to happen under  
02:05:27: the hood. After you read the sheet,  
02:05:28: it'll then um send each row to Claude.  
02:05:33: Uh when you do that, you'll have like a  
02:05:35: specific prompt that is like deter, it's  
02:05:37: not deterministic, but it's as  
02:05:38: deterministic as possible. You know, you  
02:05:40: set the temperature really low. It like  
02:05:41: expects the same outputs for the same  
02:05:42: inputs and so on and so forth. After  
02:05:44: you're done with that, maybe you like  
02:05:46: add update  
02:05:49: to sheet or something. Um so you can  
02:05:52: call, you know, open AI anthropic Google  
02:05:54: at your whims. I do it all the time  
02:05:56: within my flows and actually is a pretty  
02:05:57: big chunk of how I do things. I also  
02:05:59: call like neural networks and stuff like  
02:06:00: that. I use various libraries. Uh you  
02:06:02: don't have to just you know do it all  
02:06:04: with old school Python automation. I  
02:06:05: guess the point that I'm trying to make  
02:06:06: is just make these execution scripts  
02:06:07: very atomic. Make them do one thing and  
02:06:09: just make them as deterministic as  
02:06:11: possible. Um this will significantly  
02:06:12: improve the quality of your end result.  
02:06:14: So why does this do model work? It works  
02:06:15: because it plays to everybody's  
02:06:16: strengths. When you do not constrain the  
02:06:18: outputs of LLMs, they're really  
02:06:19: unpredictable, right? They'll try  
02:06:21: anything and when they fail, they fail  
02:06:23: spectacularly. And it might be like they  
02:06:24: work 80% of the time, but the 20% of the  
02:06:26: time they don't. They will like blow up  
02:06:27: a building or something. Uh, pre-built  
02:06:30: tools replace the construction of tools  
02:06:33: on the fly. Because the LLM is running  
02:06:35: pre-built tools, it doesn't have to make  
02:06:37: them from scratch every time, which  
02:06:38: reduces the total number of steps that  
02:06:39: you have to take to get there. A really  
02:06:41: simple analogy for this is imagine if  
02:06:43: you just gave somebody a recipe versus  
02:06:45: asking them to invent a new dish every  
02:06:46: time. Like if I just said, hey, can you  
02:06:48: make that paella recipe that you've been  
02:06:50: making me recently? The likelihood that  
02:06:51: I'm going to get the PA recipe I want is  
02:06:54: probably a lot higher than if I just  
02:06:56: have it, you know, go off the cuff every  
02:06:57: single time. it will know the flavoring,  
02:07:00: the ratio of ingredients I like, the  
02:07:02: various steps that it takes, how to put  
02:07:04: the muscles in, I don't know, just tons  
02:07:05: of stuff. Whereas, you know, every time  
02:07:07: it invents this new dish, this new pa of  
02:07:10: 3.0, obviously, it's just like going off  
02:07:11: of its own biases and randomness at that  
02:07:14: particular moment. So, in addition to  
02:07:16: directives and executions, we also have  
02:07:17: two essential configuration files. And  
02:07:19: it's actually in practice a little more  
02:07:20: than two, but I just call it two because  
02:07:22: it's a system prompt and then it's an  
02:07:23: env. um agents.mmd contain the  
02:07:26: instructions injected at the start of  
02:07:27: every conversation with the  
02:07:28: orchestrator. Now these are named  
02:07:30: according to your um ID environment. So  
02:07:32: this could be cloudMD, gemini.mmd or it  
02:07:34: could be whatever the heck it it asks  
02:07:36: for cursor.mmd whatnot. Um I would just  
02:07:38: always have like all of these  
02:07:39: simultaneously. The reason why is  
02:07:41: because if you just have all of them  
02:07:42: simultaneously you can just like move  
02:07:43: into any new IDE or any new agent or any  
02:07:46: new model and it'll just like  
02:07:47: immediately uh understand what you're  
02:07:49: saying. So in this way you could  
02:07:50: theoretically have like you know rate  
02:07:52: limits for your Gemini model um and then  
02:07:54: rate limits for your claude model and  
02:07:56: then rate limits for your open AI model  
02:07:58: and you just open all three of them in  
02:07:59: tabs and just have them all work on  
02:08:00: things to minimize the probability of  
02:08:02: you running over anything. Most models  
02:08:03: at this point are pretty similar. We've  
02:08:05: kind of converged to really really  
02:08:06: similar accuracy ratings and scores on  
02:08:08: stuff. So aside from preference and  
02:08:09: stuff, this is how you keep those costs  
02:08:11: low. In addition, your env file is where  
02:08:13: you store all your API keys and then  
02:08:14: your credentials. Um, what this ends up  
02:08:16: looking like for instance is just using  
02:08:18: that claude example earlier, uh, if we  
02:08:20: want AI to do something, we would  
02:08:21: actually have claude or rather anthropic  
02:08:24: API_key  
02:08:26: and then you just have like the the key  
02:08:28: itself right over here. Then over here  
02:08:30: you'd have like open AI  
02:08:33: API_key.  
02:08:36: Then you'd actually store that key over  
02:08:38: here as well. And you just like dump  
02:08:40: this. It would be a massive list of just  
02:08:41: all of like the credentials and keys  
02:08:42: that you'd ever want. your execution  
02:08:44: scripts instead of having to hardcode  
02:08:46: the key would just say, "Hey, go into  
02:08:47: ENV and then find it instead." And  
02:08:49: there's just like very simple programs  
02:08:51: that do that sort of thing for you. Just  
02:08:53: so we're all on the same page, what  
02:08:54: agents MD actually does is it acts as  
02:08:56: your persistent context. You inject this  
02:08:58: automatically every single time at the  
02:09:00: beginning of a session, so you just  
02:09:01: don't ever have to repeat yourself. It  
02:09:03: also explains the do framework structure  
02:09:05: to the orchestrator. So everything that  
02:09:06: I've done here, we are basically going  
02:09:08: to turn into an agents.mmd file and then  
02:09:10: just give to the orchestrator so it  
02:09:11: understands what is going on. we're  
02:09:13: going to give it to our agent and be  
02:09:14: like, "Hey, make sure to do it this way  
02:09:16: because it's reliable and because  
02:09:17: execution scripts are pretty  
02:09:18: deterministic and so on and so forth."  
02:09:20: So, it's really meta, right? Like  
02:09:21: everything I'm telling you right now,  
02:09:22: we're just going to tell to the agent.  
02:09:23: We're just going to do it in a very like  
02:09:24: context compressed way. This will also  
02:09:26: define the error handling behavior. The  
02:09:28: agent does not spiral when something  
02:09:29: breaks. And then obviously, what's  
02:09:30: really cool is you can actually just  
02:09:31: make your agents.mmd better and better  
02:09:32: and better. Like I find uh routine edge  
02:09:34: cases that I didn't handle for with my  
02:09:36: agents MD probably like once a week and  
02:09:38: then I just like add a line to it and  
02:09:39: then the next time like my model just  
02:09:40: doesn't make that mistake. I did not  
02:09:42: always self anneal for instance I just  
02:09:43: realized that huh there's some  
02:09:45: situations where my model solves the  
02:09:46: problem itself and then other situations  
02:09:48: where it comes to me for help why don't  
02:09:49: I just make it explicit hey man I want  
02:09:51: you to solve the problem for yourself  
02:09:52: that is what resulted in the self  
02:09:54: annealing concept all right so let's  
02:09:55: actually go and have AI set up directive  
02:09:57: orchestration execution for us I'll show  
02:09:59: you guys the system prompts  
02:10:00: agents.mmdenv  
02:10:02: and everything okay so let's actually  
02:10:04: build our very first real agentic  
02:10:06: workflow together the first thing you  
02:10:08: need to do is open up your IDE  
02:10:11: In my case, I'll be using Visual Studio  
02:10:13: Code for this demo. Not because I think  
02:10:15: it's better than anti-gravity or  
02:10:16: anything like that, but just because I  
02:10:17: want to show you guys you could use  
02:10:18: whatever the heck you want. You know,  
02:10:19: it's all interoperable these days.  
02:10:21: Anyway, the very first thing we need to  
02:10:23: do is we need to create a new workspace.  
02:10:25: So, I'm going to head over here to the  
02:10:26: top lefthand corner and then I'm going  
02:10:28: to say  
02:10:30: open folder. From here, I'm going to at  
02:10:33: least on a Mac, click the new folder  
02:10:35: button. Then I'm going to say YouTube  
02:10:38: workspace. do then going to create. Once  
02:10:42: I'm in it, I'll click open.  
02:10:44: Next up, what we have to do is we have  
02:10:46: to create our system prompt file. I get  
02:10:50: a lot more into detail about these  
02:10:51: later, but for now, what I'll do is I'll  
02:10:54: open up this file. I'm going to type  
02:10:56: claude.md.  
02:10:58: I'm going to paste in one of the  
02:11:00: examples that you can get in the top  
02:11:02: link in the description. So, that is  
02:11:04: this my system prompt. Then going to  
02:11:07: save. The next thing I'm going to do,  
02:11:10: I'm assuming you've already downloaded  
02:11:11: Claude Code. If not, you head over here  
02:11:13: to extensions, type, you know, in this  
02:11:15: case, Claude Code, but realistically,  
02:11:17: whatever model you want. Give that  
02:11:18: button a click, click install over here.  
02:11:21: You're going to need to sign in and all  
02:11:22: that stuff. But assuming you have your  
02:11:24: own key, and assuming you have your own  
02:11:26: um account set up on at least, you know,  
02:11:28: a $10 or $20 a month plan, you're good.  
02:11:30: I'm then going to go to the top right  
02:11:32: hand corner here, click this little  
02:11:33: claude code button, and now I'm just  
02:11:36: going to move back a bit and start  
02:11:38: asking it to help me. Now, what I want  
02:11:40: to do is I want to build a simple email  
02:11:42: onboarding flow. Essentially, when  
02:11:45: somebody joins my organization as a  
02:11:47: client, I want to send them a brief  
02:11:49: email saying, "Hey, thanks so much for  
02:11:51: joining. Really looking forward to  
02:11:53: having you." And you know, here's a link  
02:11:55: to a kickoff call that you can schedule.  
02:11:57: This is a super easy and straightforward  
02:11:59: thing to do. And you can of course set  
02:12:00: up systems to do this outside of Agentic  
02:12:03: workflows. I'm just showing you this  
02:12:04: because I think it's probably the most  
02:12:06: straightforward example to show you how  
02:12:08: to chain together three or four things  
02:12:09: that I can think of. We'll progressively  
02:12:12: design more and more complex workflows.  
02:12:14: But for now, what I need to do is I need  
02:12:16: to talk to this model. I need to have it  
02:12:17: do things. But if you notice on the  
02:12:20: lefth hand side, I don't actually have  
02:12:21: like the workspace itself set up. I just  
02:12:22: have this claw.md. So the very first  
02:12:24: thing I'm going to do is down here, I'm  
02:12:26: just going to go bypass permissions.  
02:12:28: Whatever model you're using probably has  
02:12:30: a bypass permissions mode nowadays. And  
02:12:32: I'm I'm just going to say set up my  
02:12:34: workspace in accordance with claw.md.  
02:12:38: I mean, I could have said whatever. I  
02:12:39: could have said just set my workspace up  
02:12:41: or something like that. What it's going  
02:12:43: to do is it's going to read through  
02:12:44: cloud.mmd. It's going to understand how  
02:12:46: this works and it's going to create a  
02:12:48: full directory structure based off that.  
02:12:50: now. Okay, it's adding a bunch of  
02:12:52: information web hook.m MDs talking about  
02:12:55: the deterministic and execution layers  
02:12:58: and so on and so forth. Now it's going  
02:13:00: to go through and verify the final  
02:13:01: setup. And now it's giving me a brief  
02:13:04: summary. Okay, great. Now that I have  
02:13:06: this set up, I want to show you guys how  
02:13:07: easy it is to actually build this  
02:13:08: workflow. All I'm going to do is I'm  
02:13:10: going to give it a very highle natural  
02:13:12: language instruction of what I want.  
02:13:14: Hey, I'd like to build a brief  
02:13:16: onboarding workflow. Basically, I want  
02:13:18: to be able to tell you onboard client  
02:13:21: email@acample.com  
02:13:23: and then have you send an email to that  
02:13:26: new client that introduces them to our  
02:13:28: company, gives them some background, and  
02:13:30: then invites them to a kickoff call  
02:13:32: using a calendar link.  
02:13:35: Then going to press enter. You'll notice  
02:13:37: that because I'm using my voice,  
02:13:38: sometimes this text is a little bit  
02:13:40: misformatted. That's okay. Doesn't need  
02:13:42: to be perfect. This model is smart  
02:13:44: enough to understand what's going on.  
02:13:46: >> [snorts]  
02:13:46: >> It's going to ask me some questions.  
02:13:47: What should I use to send emails? SMTP,  
02:13:50: resend, send grid, whatever. What's the  
02:13:52: company info? What's the URL? Now, I  
02:13:55: need to obviously go and I need to get  
02:13:56: this information, come back to it. But I  
02:13:58: should know that I don't even need to  
02:13:59: like know for sure. Hopefully, it's  
02:14:01: clear. I just want to like send through  
02:14:02: my own Gmail account. So, I'm just going  
02:14:04: to say, sorry, I don't know what any of  
02:14:06: that means. I just want to send a  
02:14:08: welcome email from my Gmail account.  
02:14:11: And I'm going to provide it my own.com.  
02:14:17: For company info, I'll just give you a  
02:14:19: brief list of bullet points whenever you  
02:14:22: send the email.  
02:14:26: And underneath for the calendar link,  
02:14:28: just use an example calendar link for  
02:14:30: now.  
02:14:32: Cool. I'm giving it some highle  
02:14:34: instructions here, and it's going to  
02:14:36: help and walk both of us through the  
02:14:38: finishing of this workflow.  
02:14:40: The first thing it will do is if we open  
02:14:42: up our directives folder, it'll build  
02:14:45: this onboard_client.mmd.  
02:14:50: If I go up here, you can see there's now  
02:14:51: an onboardclient.md  
02:14:53: with a bunch of highle directives with  
02:14:55: this information.  
02:14:57: Now, you'll see that it's installing  
02:14:59: dependencies and so on and so forth. It  
02:15:01: doesn't fully understand what to do  
02:15:03: here, but that's okay. Okay, what it's  
02:15:04: doing next is it's walking us through a  
02:15:07: one-time setup with our Google  
02:15:09: information. So, what I'm going to do is  
02:15:11: I'm just going to create a new app  
02:15:12: specific password. Let's just call it  
02:15:14: YouTube example. And then going to go  
02:15:17: over here. I'm going to paste this in.  
02:15:19: This is now going to take the app  
02:15:21: password and actually use it to update  
02:15:22: the env file.  
02:15:26: Says the app password saved. We're all  
02:15:27: set. First, I'm going to ask it what  
02:15:29: does the onboarding email look like.  
02:15:32: This looks pretty reasonable. I'm now  
02:15:34: going to go through and then edit this  
02:15:35: template so that we could send what I  
02:15:37: think is a higher quality template every  
02:15:38: time. Okay, just spend a few moments  
02:15:41: here putting together this onboarding  
02:15:43: email. It says, "Hi, name. Thanks for  
02:15:45: choosing to work with us. We're excited  
02:15:46: to have you on board." Here's what  
02:15:48: happens next. We hop on a quick kickoff  
02:15:49: call to align on goals. You meet the  
02:15:51: team and get synced with your project  
02:15:52: manager. From there, we'll map out a  
02:15:54: plan tailored to you and finally receive  
02:15:56: daily updates when the project is  
02:15:57: complete. Book your kickoff call here.  
02:16:00: Very straightforward template. I  
02:16:01: basically just want this to send every  
02:16:03: single time. So, it's just going to go  
02:16:04: and update the directive and presumably  
02:16:06: the execution to always reflect this  
02:16:08: information. And then finally, I'm just  
02:16:10: going to say onboard nick at  
02:16:13: nickleclick.ai.  
02:16:15: And at the end of it, you could see we  
02:16:17: now have a really well formatted and  
02:16:19: simple onboarding email. This whole  
02:16:22: workflow only took me a few seconds to  
02:16:24: put together. Hopefully you guys see the  
02:16:26: power for nontechnical people, even  
02:16:28: people that don't understand what app  
02:16:29: keys are or env tokens or anything like  
02:16:33: that to actually meaningfully integrate  
02:16:35: with software that we're using. All  
02:16:36: right, so now that we've seen a little  
02:16:37: bit about how to set things up, how do  
02:16:38: you actually go and create like really  
02:16:39: good directives? Well, you need four  
02:16:41: things. You need a clear objective  
02:16:42: statement, aka what this directive does.  
02:16:45: You need some form of input  
02:16:46: specification, so what data does the  
02:16:48: agent need to actually get started? You  
02:16:50: need a step-by-step process, which is a  
02:16:52: sequence of operations, scripts, and  
02:16:53: expected outputs in natural language.  
02:16:55: And then you also need a definition of  
02:16:57: done. So that's quality criteria. How do  
02:16:59: you know that the agent has actually  
02:17:00: succeeded? It needs to be able to grade  
02:17:02: itself based on its output. For  
02:17:03: instance, like you'll know you're  
02:17:05: successful when you have a Google Sheet  
02:17:06: link URL with at least 100 rows filled  
02:17:09: in, something like that. You should  
02:17:10: also, of course, include edge cases. So  
02:17:12: any known exceptions, if there are  
02:17:13: quirks with an API, if there are things  
02:17:15: that come out as error codes that should  
02:17:17: not come out as error codes, if they  
02:17:18: have common failure modes, you should  
02:17:20: actually include all of that in the  
02:17:21: directive. Uh you should also describe  
02:17:23: fallback behavior like, hey, if the  
02:17:25: Apollo scraper we're using fails, try  
02:17:27: the instantly lead uh enrichment tool  
02:17:29: instead. And unlike old automations, you  
02:17:32: don't have to like build this massive  
02:17:33: complicated error handling function.  
02:17:35: Unlike naden or make.com or any of these  
02:17:38: visual coding tools, you don't actually  
02:17:39: have to go through and like create these  
02:17:41: error handling flows. You you just add  
02:17:42: one line and you're like, "Hey, if this  
02:17:44: happens, then do this." And it's so much  
02:17:45: simpler. It also includes some sort of  
02:17:47: instructions saying what to return if  
02:17:49: everything fails gracefully. Like a lot  
02:17:51: of um systems do fail really gracefully.  
02:17:53: They don't even really tell you that  
02:17:54: they fail. If you expect a 100 leads to  
02:17:56: pop up or 100 YouTube videos to come  
02:17:57: from your YouTube video scraper or  
02:17:59: whatever, you know, like one will uh  
02:18:01: it'll technically have done so  
02:18:02: correctly, but you know, nothing will  
02:18:04: have errored out. So there's no real  
02:18:06: built-in way for the model to know  
02:18:07: unless you make it hyper explicit what  
02:18:09: happens if things go to plan. That's why  
02:18:12: you need a definition of done. And then  
02:18:13: you also need something to say like,  
02:18:15: hey, if this does fail gracefully, if  
02:18:16: we're under 100 records, let's say if  
02:18:18: that's our minimum, um, rerun it over  
02:18:20: and over and over again with wider  
02:18:22: filters until we get to 100. don't  
02:18:23: return this to the user until we have at  
02:18:25: least whatever he put in. All right, for  
02:18:27: my next system, I basically want to  
02:18:28: build a CRM manager for ClickUp. ClickUp  
02:18:32: is one of many CRM tools that you could  
02:18:34: use. I really like it because I think  
02:18:36: it's simple, it's fast, and then it  
02:18:37: includes a bunch of functionality that  
02:18:40: weaves together different tools like it  
02:18:42: has built-in messaging. Um, it obviously  
02:18:45: has documents. I could store my  
02:18:46: knowledge bases in here and so on and so  
02:18:48: forth. But I want you to know the  
02:18:50: specific tool doesn't really matter at  
02:18:51: all. You can build this sort of thing  
02:18:53: out in basically any CRM so long as it  
02:18:55: has the ability to connect via API and  
02:18:57: MCP and that sort of stuff. So basically  
02:19:00: what I have here is I have a really  
02:19:01: simple CRM setup called template  
02:19:03: creative agency. I'm going to pretend  
02:19:04: I'm a creative agency here. You can see  
02:19:06: there's a sales pipeline. Inside of the  
02:19:09: sales pipeline, I have people like Nick  
02:19:11: Sarif and Peter Jackson and Peter Smith,  
02:19:14: Peter Jackson, Sally Lozen, her last  
02:19:16: name's Lozen, Koth Arllan, and so on and  
02:19:18: so forth. Basically stored um on this  
02:19:20: cool little table. And what happens like  
02:19:22: any CRM is people come in through this  
02:19:24: intake stage like  
02:19:29: Bast Sarif and then um essentially they  
02:19:32: are assigned a status. Then as they are  
02:19:34: updated, I move them to things like  
02:19:36: meeting booked and then proposal sent  
02:19:38: and close lost or closed one. Uh  
02:19:40: depending on whether or not they accept  
02:19:41: the contract. However, I don't really  
02:19:43: want to interact with it manually  
02:19:45: anymore. I think it'd be really cool if  
02:19:46: I could weave this into other workflows  
02:19:49: like our onboarding workflow that we  
02:19:50: made earlier. So, how do I do this? I'm  
02:19:52: just going to ask it to build this for  
02:19:53: me. I'd like you to be a wrapper around  
02:19:56: my ClickUp CRM. I want to be able to ask  
02:19:58: you to do anything inside of ClickUp,  
02:20:00: then have you automate the process for  
02:20:02: me. This will also allow us to connect  
02:20:04: to other workflows that we build around  
02:20:06: my agency. All of the CRM information is  
02:20:10: stored inside of the  
02:20:13: and let me head back over here and let's  
02:20:16: see what it's called. Template creative  
02:20:17: agency space.  
02:20:22: Give me three ways we could do this.  
02:20:24: Okay, it's now going to create me  
02:20:26: everything that I need. The first option  
02:20:28: is a direct script library. It'll create  
02:20:31: a set of execution scripts for common  
02:20:33: ClickUp operations with a master  
02:20:34: directive that routes requests. That's  
02:20:36: pretty cool. I would have to invoke it  
02:20:38: every time. Then there's some sort of  
02:20:40: conversational idea. Then there's also a  
02:20:43: web hook bridge. I like the idea of  
02:20:46: number one. I want to see if there's a  
02:20:47: simpler way to do this. Is there any  
02:20:49: simpler way to do this? Like is there an  
02:20:51: MCP or just anything that wouldn't  
02:20:53: require us building a specific step for  
02:20:55: every request?  
02:20:57: It's going to go through and reason  
02:20:59: first. So, it's going to check to see  
02:21:00: whether or not there is anything out  
02:21:02: there that would allow us to do this  
02:21:03: more easily. What it's doing here is  
02:21:05: it's using a web search sub agent.  
02:21:07: Believe it or not, we're going to talk a  
02:21:08: lot more about sub agents later, but sub  
02:21:10: aents have pros and cons. When you use  
02:21:12: sub agents, things typically take a lot  
02:21:14: longer to finish, but the pro is you  
02:21:16: isolate the context. And um what that  
02:21:19: means is you just don't need to worry  
02:21:20: about inserting all this stuff into the  
02:21:22: main flow. Cool. So, this is sort of  
02:21:25: what I wanted to do initially. kind of  
02:21:27: cheating here, but I know MCP is just a  
02:21:29: simple and easy way that I could build  
02:21:31: something like this. And I'll show you  
02:21:32: guys more about this later. But as we  
02:21:34: see here, there's an official and then  
02:21:36: there's also a nonofficial one. What I'm  
02:21:38: going to do is I'll say, "Hey, let's do  
02:21:41: the official. How do I get my API  
02:21:43: token?"  
02:21:47: Okay, it's giving me some instructions  
02:21:49: here. So, I'm going to head over here. I  
02:21:51: just need to regenerate this API token.  
02:21:54: So, first I have to put my password in.  
02:21:55: Just bear with me.  
02:21:58: Next, I'm going to copy this token over.  
02:22:00: And then I'm just going to head over  
02:22:01: here and paste it. One thing that you'll  
02:22:03: find that models do pretty often is, and  
02:22:06: I don't know if this is because they  
02:22:07: want to conserve on their own token  
02:22:08: usage or something, instead of just  
02:22:10: doing the thing for you, often times  
02:22:12: they will say, "Hey, I'm going to find  
02:22:13: information on how you can do the  
02:22:14: thing." What is super super powerful is  
02:22:17: just to say, "Okay, great. Do it. Looks  
02:22:19: like we need some more information  
02:22:21: here." So, we need to go to ClickUp in  
02:22:23: our browser, look at the URL, and then  
02:22:24: get the team ID.  
02:22:28: I see it right over there. Let me just  
02:22:30: paste it in. Okay. And now all I need to  
02:22:33: do is just restart Claude Code. So, let  
02:22:34: me click this little X, head over here  
02:22:37: again. I double tap on the page in order  
02:22:39: to create that new file.  
02:22:42: Okay. And now I have an MCP. So, let me  
02:22:44: just give that a click. When you type  
02:22:46: back SLMCP, you can now see the MCP  
02:22:48: servers you have. and I'll say,  
02:22:51: "Awesome. Can you create a new record  
02:22:53: for me?"  
02:22:58: So, because this is an MCP, it's like a  
02:23:00: general solution. It's not a specific  
02:23:01: solution. We need to insert some  
02:23:03: information about this. So, what type of  
02:23:05: record? Where should it go? I'd like you  
02:23:07: to act essentially as my ClickUp  
02:23:10: wrapper.  
02:23:12: Keep in mind that this is a new  
02:23:13: instance. So, I need to provide it some  
02:23:14: highle instructions. again.  
02:23:22: So all conversations are going to be  
02:23:25: related to that space.  
02:23:28: I'd like you to store this information  
02:23:30: somewhere. That way the next time I ask  
02:23:31: you to do this, you'll do it the first  
02:23:33: time.  
02:23:35: Go and learn about the space first.  
02:23:39: New lead, Peter Rockwell.  
02:23:45: Okay. And now what it's doing when I say  
02:23:48: new lead Peter Rockwell, it is creating  
02:23:50: a lead in that space. Pretty  
02:23:52: straightforward. Let's go check and make  
02:23:53: sure that it's good. And as you can see  
02:23:55: here, we now have a meeting URL link as  
02:23:57: well as a status of meeting booked.  
02:23:59: Hopefully, it's clear. I could talk all  
02:24:01: day about this and give this all of the  
02:24:03: information that I want in order to have  
02:24:05: it, you know, manage my uh ClickUp CRM  
02:24:08: for me. So, that's one way to do so with  
02:24:09: an MCP, which is really straightforward  
02:24:11: and it's super simple. Let me show you  
02:24:13: another way we can do this just using  
02:24:14: like the ClickUp API instead. So I'm  
02:24:17: just going to exit out of this and then  
02:24:18: create a new cloud code instance. I'm  
02:24:21: going to say, hey, can you uninstall the  
02:24:23: ClickUp MCP and remove anything in our  
02:24:25: environment that has to do with ClickUp?  
02:24:27: I'm doing a demo.  
02:24:29: Then going to bypass permissions. So I  
02:24:31: just don't have to worry about it. It's  
02:24:32: just going to do it all for me. Hey, I'd  
02:24:34: like you to build a series of ClickUp  
02:24:36: directives so that I could automate the  
02:24:38: process of adding records, updating  
02:24:41: them, and so on and so forth. I  
02:24:43: basically want you to act as my ClickUp  
02:24:45: wrapper. I want to do this via API  
02:24:47: calls. We previously tried MCP, but I'm  
02:24:50: doing a demo and I just want to do this  
02:24:51: via API instead. Okay, it's now building  
02:24:54: this out systematically. So, it's going  
02:24:56: to start by building a base ClickUp API  
02:24:58: client. It's then going to create CRUD  
02:25:00: scripts to create, get, update, delete.  
02:25:03: So, I'm going to create directives for  
02:25:04: each operation. Then, finally, it's  
02:25:06: going to update my env template. It says  
02:25:08: with a ClickUp API key placeholder. Um,  
02:25:10: I did just remove it, so I'm going to  
02:25:11: have to add that in again most likely.  
02:25:13: What's really cool is I know nothing  
02:25:14: about any of this stuff, and it's just  
02:25:16: doing it all completely automatically  
02:25:17: right now. It's writing all the  
02:25:19: directives, all the executions,  
02:25:20: literally everything that I need. And  
02:25:21: so, the reason why I'm showing you  
02:25:23: multiple different ways to do things is  
02:25:24: because there almost always are multiple  
02:25:26: different ways to do things. And with AI  
02:25:28: and agentic workflow builders like this,  
02:25:31: it's not necessarily that one approach  
02:25:33: is better than the other. Sometimes I'll  
02:25:35: try an approach and for whatever reason,  
02:25:36: whether the API isn't cooperating or  
02:25:39: it's just not very logistically  
02:25:40: reasonable, I will abandon it halfway  
02:25:43: and then just do another one. There's no  
02:25:44: reason why I have to commit to something  
02:25:46: that isn't working. And I can always  
02:25:48: change things. Nowadays, the barrier  
02:25:50: isn't really whether or not it's  
02:25:51: possible. The barrier is basically just,  
02:25:53: hey, how much time do I want to spend  
02:25:55: guiding or steering the ship in order to  
02:25:57: get this thing done for me. Okay, it's  
02:25:59: now going through adding all the  
02:26:00: information that we need. I gave it the  
02:26:02: API key as you guys could see above.  
02:26:04: It's going to essentially loop over as  
02:26:06: many times as it takes because of what  
02:26:08: is in the cloud MD. Eventually, it will  
02:26:11: um, you know, solve its own problems  
02:26:13: through a process called self annealing.  
02:26:14: And then we'll be able to do things like  
02:26:16: create tasks, delete them, update them,  
02:26:18: and so on and so forth. So, it's just  
02:26:20: running through and testing all of the  
02:26:21: various scripts that it put together.  
02:26:23: The creating of a task, the deleting,  
02:26:26: the cleaning up, so on and so forth. So,  
02:26:28: let me give it some more highle  
02:26:30: instructions just to tell it I really  
02:26:31: wanted to work within that template  
02:26:33: creative agency uh uh space. I'd like  
02:26:36: you to do all of your tasks solely in  
02:26:39: the template creative agency space.  
02:26:44: Update everything to reflect this. Then  
02:26:50: whatever you need to in order to reflect  
02:26:53: this. Then create a new lead called Nick  
02:26:56: Sar.  
02:26:58: Cool. Looks like it already knows what  
02:27:00: it needs to do. So now it's going to  
02:27:02: create the lead. And you can see it's  
02:27:03: even given me a link to the lead so that  
02:27:05: I can pull it up and see it for myself,  
02:27:06: which is pretty cool. Awesome. Why don't  
02:27:09: we see if this has access to some other  
02:27:10: fields? Do you have access to custom  
02:27:12: fields? Okay. First, it's going to see  
02:27:15: the custom fields in this list. It's  
02:27:17: then going to see if we could set the  
02:27:18: appropriate one. Nice. That's pretty  
02:27:20: cool. So, whereas the other one could  
02:27:22: not set custom fields, um, this one can  
02:27:24: set custom fields, which is pretty  
02:27:25: sweet. As you guys could see, sometimes  
02:27:27: there's pros or cons to different  
02:27:28: approaches. This one was really awesome.  
02:27:30: So, to be honest, I now basically have  
02:27:32: like a whole CRM manager. Great. Delete  
02:27:35: the record. That was just for demo.  
02:27:39: I'd personally say having some sort of  
02:27:41: CRM wrapper like this now with the power  
02:27:43: of current technology is like a  
02:27:45: non-negotiable. This thing just makes  
02:27:46: our lives so much easier. And what's  
02:27:48: really cool is we could weave flows in  
02:27:50: together. So when somebody becomes a new  
02:27:52: client, for instance, we could then  
02:27:53: automatically send that onboarding flow,  
02:27:55: then maybe even reflect that by adding a  
02:27:57: comment or something like this. These  
02:27:59: things will supercharge any CRM very  
02:28:01: very quickly. Okay, I want to talk a  
02:28:03: little bit about cloud skills. Um, this  
02:28:04: is really similar to DO like we just ted  
02:28:06: chatted about, but it is specific to the  
02:28:08: cloud family of models. So you can't use  
02:28:10: the same cloud skills structure that I'm  
02:28:12: about to show you in like Gemini or  
02:28:14: OpenAI or or GPT 5.2 or whatever. It's  
02:28:17: very very specific to Claude. That said,  
02:28:19: you know, all of these model families  
02:28:21: now have their own versions of this. So  
02:28:22: I wanted to cover probably like the most  
02:28:24: popular one just so we're all on the  
02:28:25: same page. I care a lot about  
02:28:26: interpretability and modularity. So I  
02:28:29: want to be able to use the same workflow  
02:28:30: setup in, you know, model A versus model  
02:28:33: B versus model C. Um cloud skills are  
02:28:35: obviously hyperspecific to anthropics  
02:28:37: model. Now, this was their attempt to  
02:28:39: standardize Agentic workflows into  
02:28:41: reusable portable packages. And just  
02:28:43: like DO, it's a folder structure. It  
02:28:45: contains instructions, scripts, prompts,  
02:28:47: and resources that Claude will load  
02:28:48: every time you call something. So, it's  
02:28:51: just a slightly different folder  
02:28:52: structure that includes a file called a  
02:28:54: skill.md. And I'm going to run you  
02:28:55: through that in a moment. The way that  
02:28:56: skills work in a nutshell is just ignore  
02:28:58: the lefth hand side of this graph cuz I  
02:29:00: think this is a little more complicated  
02:29:01: than we probably need right now. But  
02:29:02: basically, you have your agent and your  
02:29:04: agent organizes things into these skills  
02:29:07: folders. And so, it's a skills folders  
02:29:09: slash whatever the the skill um that you  
02:29:11: want it to to know is. So, in this case,  
02:29:14: there's a skill called big query. Then,  
02:29:16: you'll see there's a capital skill.md  
02:29:18: with a data sources.md, a rules.md. Over  
02:29:21: here, there's an NDA review, which  
02:29:23: includes a skill.md. The skill.md is  
02:29:25: just your directive, right? And you'll  
02:29:26: notice that because it's in markdown.  
02:29:28: Everything else here is entirely up to  
02:29:30: you. And so it's sort of like a loose  
02:29:31: framework right now where people are  
02:29:32: just dumping in whatever the heck they  
02:29:34: want the agent to have access to. It's  
02:29:35: also just a form to uh a way that you  
02:29:37: can modularize things. And basically  
02:29:38: what you'll do is you'll just have like  
02:29:40: a big list a big directory called  
02:29:42: skills. Then underneath that you will  
02:29:44: have things like you know hey uh let's  
02:29:47: do big query. Let's do one called docx.  
02:29:50: Let's do one called pdf. Let's do one  
02:29:52: called I don't know scrape leads. And  
02:29:55: each of these are going to be folders um  
02:29:57: themselves. So very similar to do. just  
02:30:00: takes a slightly different approach.  
02:30:01: Instead of having like the executables  
02:30:03: and like the scripts and stuff like that  
02:30:05: stored in other folders like an  
02:30:07: execution scripts folder, um it just  
02:30:09: stores it all in the exact same one. The  
02:30:10: way I treat things is as an instruction  
02:30:12: manual that Claude reads first. There's  
02:30:15: one slight difference between the way  
02:30:16: that the markdown file is written in so  
02:30:18: far that um it uses what's called YAML  
02:30:20: front matter. YAML just stands for yet  
02:30:22: another markup language by the way,  
02:30:23: which is really funny. There's like a  
02:30:24: million different ways to do this.  
02:30:25: Basically what this is is this is like a  
02:30:27: short I don't know 100 character 200  
02:30:30: character description of what the skill  
02:30:32: does. Um so as opposed to with you know  
02:30:34: the directive orchestration execution  
02:30:36: framework you know I don't usually use  
02:30:37: YAML I just like have it whip it up  
02:30:39: although YAML I think would be an  
02:30:40: improvement. Um you know instead of just  
02:30:43: naming something really descriptively  
02:30:44: what this does is actually just provides  
02:30:45: some context. Hey this script does X Y  
02:30:48: and Z. Hey this uh skill asks for this  
02:30:51: thing. And then you know what'll happen  
02:30:53: is upon runtime claude will load the  
02:30:56: skill based on whatever task you're  
02:30:57: asking to perform just based off of the  
02:31:00: YAML front matter which just means it  
02:31:01: saves a lot of tokens. It doesn't have  
02:31:02: to read the whole thing. So this is just  
02:31:04: a small block of metadata at the top of  
02:31:06: the file. There's like a name field,  
02:31:08: there's a description field, and then  
02:31:11: there's a purpose field and I'll show  
02:31:12: you an actual concrete example in a  
02:31:14: second. And then it's like kind of  
02:31:16: separated like this. And then when the  
02:31:17: agent loads the file um to actually like  
02:31:19: search through your skills, you say,  
02:31:20: "Hey, you know, I want you to scrape  
02:31:21: some leads." It'll actually just load  
02:31:23: this. So, it's way way shorter. Small  
02:31:26: metadata allows it to, you know, only  
02:31:28: load a few hundred characters at a time  
02:31:29: as opposed to big chunks. It allows it  
02:31:31: to understand what the skill does  
02:31:32: without reading the whole thing. Now,  
02:31:33: there's also a big library of pre-built  
02:31:35: skills right now for common tasks,  
02:31:37: mostly relating to documents. Um, and  
02:31:38: these are just skills that have been  
02:31:40: like hyper optimized over the course of  
02:31:41: tens of thousands of runs. You can think  
02:31:43: of them as execution scripts and  
02:31:45: directives that are just really, really,  
02:31:46: really self- annealed and they're just  
02:31:47: really, really powerful. So, we can do  
02:31:49: PDF creation, do word documents easily,  
02:31:51: Excel spreadsheets, PowerPoint  
02:31:53: presentations. The quality is  
02:31:54: surprisingly good. And because so many  
02:31:56: people have run these things because  
02:31:57: they've optimized the hell out of it,  
02:31:59: they tend to execute super quickly and  
02:32:00: then they also tend to be like pretty  
02:32:02: reliable. All right, let me show you  
02:32:03: some cloud skills in action. Let's talk  
02:32:04: about how to build things in cloud  
02:32:06: skills format instead of do format. I  
02:32:09: want you guys to see it's more or less  
02:32:10: the same thing. This is just highly  
02:32:11: cloudspecific. So I have a simple task  
02:32:14: in front of me here. I want to create a  
02:32:15: new cloud skill called generate- report.  
02:32:18: And I want this to build a weekly  
02:32:19: weather report with publicly available  
02:32:21: information from some API. I just  
02:32:24: Googled weather API. Pasted this in  
02:32:26: there. I don't even know if it's going  
02:32:26: to work, but we'll figure it out  
02:32:27: alongside each other. I also said I want  
02:32:29: a Canada specific just because I'm  
02:32:31: Canadian. I.e. this report should be all  
02:32:32: about the weather across Canada. Now the  
02:32:34: last thing I need is I need some sort of  
02:32:36: template. So I'm just going to go and  
02:32:37: I'm going to see if I could download a  
02:32:39: free report template.  
02:32:41: Let's see. It's going to open up a bunch  
02:32:43: of tabs. What do we got here? 2035  
02:32:45: annual report. That looks ridiculous.  
02:32:47: [gasps] Um, okay. This one looks pretty  
02:32:49: cool. Can I just download this whole  
02:32:50: thing? Okay. Anyway, I'm just going to  
02:32:52: go over to Canva here. And then I'm just  
02:32:55: going to download this as uh what are we  
02:32:58: going to do? PDF. Let's just do PDF.  
02:33:01: We'll do all pages. I'll click download.  
02:33:04: Once I have this, I'm then going to  
02:33:06: provide this file to Cloud Code.  
02:33:09: I have a template file in I'll just drag  
02:33:13: this over tot  
02:33:18: and I'll just call it uh  
02:33:22: orange and black modern annual report  
02:33:24: that I want you to use. Go. Awesome.  
02:33:29: So it's then going to pull that file and  
02:33:31: then it's going to because it knows how  
02:33:33: to generate cloud skills sort of  
02:33:34: natively go through the whole process.  
02:33:36: Okay. It's going through and then  
02:33:37: creating the skill directory structure.  
02:33:40: Uh it's then writing the skill MD with  
02:33:42: instructions. It's doing a fair amount  
02:33:43: of stuff. So I'm just head over to here  
02:33:44: to skills and then I'll see where this  
02:33:46: would be. Okay. Generate report right  
02:33:48: over here.  
02:33:51: Okay. And inside there's a skill.md.  
02:33:53: Then there's also a scripts folder. This  
02:33:55: is where we're going to insert the  
02:33:57: scripts. It's now going to go fetch a  
02:33:59: bunch of weather data. The cool thing  
02:34:01: about Claude skills is there's this  
02:34:04: little YAML front matter. It's called Y  
02:34:07: A ML and then front matter is just  
02:34:10: everything that's between these three  
02:34:11: dashes. And here we have the name, a  
02:34:13: brief description, and then also some  
02:34:15: allowed tools, which is really cool. So  
02:34:17: you can get very granular with how you  
02:34:18: give your agent access to these  
02:34:21: workflows. And then what's cool is they  
02:34:23: only actually um load this into context  
02:34:26: before deciding on which skill to use.  
02:34:28: So that way you save a fair amount of  
02:34:30: tokens because it doesn't have to like  
02:34:31: read every single file, right? Okay, I'm  
02:34:34: then going to get an API key payment.  
02:34:37: Okay, it looks like open weather map is  
02:34:39: not free despite it saying that it is  
02:34:41: free. I need to sign up and then enter  
02:34:42: some payment information. So don't use  
02:34:44: that. U what I've done here is I've just  
02:34:46: said, hey, it's not free. So find a  
02:34:48: source that is free. So now it's going  
02:34:49: to go and it's going to find me  
02:34:50: something that is realistically. Looks  
02:34:52: like it found an alternative source  
02:34:53: called open- so it's just going to  
02:34:55: rewrite it with that information in  
02:34:57: mind. Now that it's done a little bit of  
02:34:59: work, what it's doing is just testing  
02:35:00: this skill. Okay, looks like it has now  
02:35:02: generated me a file. Let's just say open  
02:35:06: PDF.  
02:35:09: Cool. And now we have it. So, Canada  
02:35:11: weekly weather 2025, table of contents,  
02:35:14: national overview, weather highlights,  
02:35:16: west coast prairie, central Canada. So,  
02:35:19: you guys can see it is very, very easy  
02:35:21: to create a template using a PDF. Just  
02:35:24: drag and drop that puppy in. And then  
02:35:25: boom, you now have native intelligence  
02:35:27: that is capable of interacting with  
02:35:28: tools like this to generate honestly a  
02:35:31: very clean and very sexy proposal  
02:35:35: document. Pretty straightforward, huh?  
02:35:38: So, I mean like this is just one of many  
02:35:39: asset generation workflows that you  
02:35:41: could do. Um, hopefully you guys see you  
02:35:42: could now like generate proposals in a  
02:35:44: flash. You could generate any PDF in a  
02:35:46: flash, customized assets or slide decks  
02:35:48: or whatever the heck you want. um it  
02:35:49: really only takes a data source, the  
02:35:52: template itself and then you waiting  
02:35:54: around 5 minutes or so as it self  
02:35:55: anneals and then generates. Let's talk a  
02:35:57: little bit about model context protocol.  
02:35:59: So this is essentially a USB for AI. The  
02:36:03: idea is that it is a universal adapter  
02:36:05: that lets any assistant whatever model  
02:36:08: family connect to any data source  
02:36:11: interoperably. Now when I say USB um a  
02:36:14: while back you had so many different  
02:36:15: types of USBs. You had like a USB 1, you  
02:36:18: had a USB 2, you had a USBA,  
02:36:21: a USB. I don't actually know if this  
02:36:24: one's real, but you had like hundreds of  
02:36:25: different types of USB configurations,  
02:36:27: basically hundreds of different cables.  
02:36:29: And then um eventually somebody made a  
02:36:31: USBC and they realized that this is just  
02:36:33: like the superior format and then they  
02:36:35: made either regulations depending on  
02:36:37: where you live or just heavily  
02:36:38: incentivized the market to just produce  
02:36:40: USBC's because USBC's if we all just  
02:36:43: standardize to one adapter means that  
02:36:44: like I could just buy any device and  
02:36:46: then I could just slot that into any  
02:36:48: other device and it would just work. I  
02:36:49: don't have to carry around 20 different  
02:36:50: types of cables. I just know that this  
02:36:52: sort of adapter function is just going  
02:36:53: to make everything work and uh it's  
02:36:55: going to be super easy and more  
02:36:56: convenient. That's essentially just what  
02:36:58: MCP is. We're just doing that for our AI  
02:37:00: agents. This was introduced by Enthropic  
02:37:02: back in November 2024. It's a  
02:37:03: standardized way for AI assistants to  
02:37:05: connect to any external data and tools.  
02:37:07: And this isn't just Claude to be clear.  
02:37:08: Um they just made this for everybody. So  
02:37:10: this works with, you know, like the  
02:37:11: OpenAI family of models. This works with  
02:37:13: the Gemini family models. The whole idea  
02:37:15: is it just eliminates the need for those  
02:37:17: custom USBs for every connection. Just a  
02:37:19: universal translator. It's like imagine  
02:37:21: there was some language that you know  
02:37:23: anybody on planet earth could speak and  
02:37:25: you know when you meet a person who  
02:37:26: doesn't speak the other language that  
02:37:28: you speak you just all use the same  
02:37:29: language it's espironto or whatever but  
02:37:31: it's for um you know AI agents that's  
02:37:33: basically it there are two main pieces  
02:37:34: to understand there are MCP clients on  
02:37:36: one hand and then there are MCP servers  
02:37:38: on the other hand so you know these  
02:37:40: clients are basically our AI apps so  
02:37:43: these are our things like anti-gravity  
02:37:46: these are our VS codes and these are  
02:37:50: also are things like uh I don't know  
02:37:52: clawed desktop  
02:37:54: these are things like you know chat GPT  
02:37:58: and basically what these are is you  
02:38:00: remember how earlier in the course I  
02:38:01: said that chats are just like the  
02:38:02: interfaces that agents are using right  
02:38:04: now they're sort of borrowing them  
02:38:05: because we don't have a better interface  
02:38:07: well that's essentially all a client is  
02:38:09: it's just an interface so the client is  
02:38:10: the tool that houses the agent right  
02:38:12: it's the shell around it and what this  
02:38:15: does is it connects to servers and these  
02:38:18: servers are based on specific tools. So  
02:38:21: for instance, there is an Appify MCP  
02:38:23: server. In addition to an Appify MCP,  
02:38:26: there's like an Apollo MCP.  
02:38:29: There is a I don't know Google Drive  
02:38:31: MCP. There's a Sheets MCP.  
02:38:35: And the point is whatever client you're  
02:38:37: using at the time, so maybe anti-gravity  
02:38:39: in this case, just calls the specific  
02:38:42: MCP whose configuration files you  
02:38:44: include in your workspace. So in  
02:38:47: anti-gravity I might have you know an  
02:38:49: appy mcp drive mcp and sheets mcp and  
02:38:52: then what I do is I just say hey can you  
02:38:54: you know look at my drive for whatever  
02:38:56: file and then turn that into a big CSV  
02:38:58: and then can you feed that CSV into appy  
02:39:00: and you know assuming that these three  
02:39:02: MCPS are good because there's a lot of  
02:39:04: quality variance in MCPS right now um it  
02:39:06: can actually do what you want it to do  
02:39:08: you can also store highle directives  
02:39:10: that explain how to chain these together  
02:39:11: even more in-depthly and more reliably  
02:39:14: and then the MCPS are essentially ally  
02:39:16: just your execution scripts. Right now  
02:39:18: there are three main ways that MCP  
02:39:20: servers communicate with MCP clients.  
02:39:22: There are resources which are structured  
02:39:23: data like documents, code, database  
02:39:25: records and so on and so forth. Then  
02:39:27: there are tools which are functions that  
02:39:28: your agent can call. These are analogous  
02:39:30: to execution scripts on our end. And  
02:39:32: then there are prompts which are  
02:39:33: basically just like system prompts for  
02:39:35: specific things. They guide how the  
02:39:37: model should interact with specific  
02:39:38: server. Hey, you should use this uh  
02:39:40: execution script when you want to do  
02:39:42: this function. Hey, you should call this  
02:39:44: resource. You shouldn't pagionate all of  
02:39:46: them. You should only call the first 50  
02:39:48: lines. This just is like highle  
02:39:49: instructions that help the model do  
02:39:50: things more reliably. The whole idea of  
02:39:52: MCP is really just to make the entire  
02:39:55: internet web accessible to our agents.  
02:39:59: Every tool gets its own MCP server. What  
02:40:02: your agent does is it only loads the  
02:40:05: ones that you absolutely need. This  
02:40:08: means you never have to build custom  
02:40:10: tools from scratch. though I think it is  
02:40:13: pretty easy and pretty great to get  
02:40:14: yourself that functionality and you get  
02:40:17: to give your agent breadth out of the  
02:40:18: box with very little effort on your  
02:40:20: part. In addition, you can also build  
02:40:22: your own custom MCP servers. The value  
02:40:26: here is not only are you going to have  
02:40:28: your own agent use it, of course, you  
02:40:30: could share it with other people. And by  
02:40:32: sharing it with other people, you can  
02:40:34: either ask them to either pay you or  
02:40:35: something to build the MCP server or,  
02:40:38: you know, let's say you're an API that  
02:40:39: builds an MCP server around your  
02:40:41: function, you can make things more  
02:40:43: accessible and then increase your  
02:40:45: company revenues. So, it's very very  
02:40:47: easy to build these things with AI  
02:40:48: assistance. When MCP came out, it was  
02:40:50: very difficult, but now it's super easy.  
02:40:52: I actually built one in 10 minutes the  
02:40:54: other day. I never read any MCP  
02:40:56: documentation and it did something  
02:40:58: really cool for me, which I may talk  
02:41:00: about in a future video. This means you  
02:41:01: can create specialized tools for  
02:41:03: specific workflow needs anytime that you  
02:41:05: want. And then if other people within,  
02:41:07: let's say, your organization want to use  
02:41:08: this or whatever, you just share the MCP  
02:41:10: server. Uh it's always going to work the  
02:41:12: same out of the box because it's the  
02:41:14: same server now. There are multiple  
02:41:15: people that can iterate and improve it,  
02:41:17: not just you. So the main question I get  
02:41:18: at this point is why don't we just use  
02:41:20: MCP for everything? Sounds great, right?  
02:41:23: Maybe we should. Well, the reason why is  
02:41:26: because MCP takes a lot of tokens. And  
02:41:28: the more context a model deals with, the  
02:41:31: dumber it gets. If you fed in the exact  
02:41:35: same prompt to two models, except prompt  
02:41:38: one said what you wanted it to say in, I  
02:41:41: don't know, 10 words, and prompt two  
02:41:43: said the exact same thing, but it wrote  
02:41:45: it really inefficiently and made it  
02:41:46: really, really, really, really long. The  
02:41:49: model would almost always perform better  
02:41:50: here. Maybe this would have a 99%  
02:41:54: success rate, whereas this would have an  
02:41:56: 85% success rate or something. What I  
02:41:58: mean to say is there's a very strong  
02:42:00: relationship between token count in  
02:42:04: context and then performance  
02:42:08: and this is improving as models get more  
02:42:09: intelligent but essentially performance  
02:42:12: as tokens go longer and longer and  
02:42:13: longer in the context almost always  
02:42:15: necessarily will decline. It's not  
02:42:18: exactly like this because usually when  
02:42:20: you provide more context, it's actually  
02:42:21: a little like bump until you get to a  
02:42:24: certain point and then it starts  
02:42:25: declining because it's like here we  
02:42:26: didn't really provide enough information  
02:42:27: for the model to know what's going on.  
02:42:29: Whereas here, maybe we provided a bunch  
02:42:30: of examples or whatever, which is why it  
02:42:32: does better. But inevitably, the longer  
02:42:34: that you um add a bunch of information  
02:42:35: that isn't relevant to your task, the  
02:42:37: more tokens that you have in that  
02:42:38: prompt, the crappier your outputs are  
02:42:40: going to be. And the issue with MCP is  
02:42:42: it actually loads pretty much all of its  
02:42:45: available functions into your agents  
02:42:46: context window. Now there are some  
02:42:49: developments that are fixing this. These  
02:42:50: are like at runtime MCP servers where um  
02:42:54: your AI just makes an intelligent  
02:42:56: determination about which MCP servers to  
02:42:58: load and stuff like this. But MCP as a  
02:43:01: framework is still pretty new and a lot  
02:43:02: of the MCP servers out there are pretty  
02:43:04: crappy. So regardless, we're loading a  
02:43:06: ton of tokens into a context window.  
02:43:09: Every function will have a name. They'll  
02:43:11: have a description. There'll also be a  
02:43:12: schema. This will be a few hundred  
02:43:14: tokens usually. And what that means is  
02:43:16: if you connect five servers and every  
02:43:18: server has 10 tools. So like if you  
02:43:20: connected to the drive server and then  
02:43:22: the drive server had I don't know get  
02:43:24: file. Okay, this is one of the functions  
02:43:27: or execution scripts. I don't know it  
02:43:29: has read file. It has share file and so  
02:43:34: on and so forth. Right? Every single one  
02:43:36: of these would have a name, description,  
02:43:38: schema, name, description, schema, name,  
02:43:40: description, schema. We're getting  
02:43:42: really high up in the tokens already,  
02:43:44: right? If you have 300 tokens per  
02:43:45: definition, even five servers with 10  
02:43:47: tools each means 15,000 tokens. And  
02:43:50: that's before you've done anything. So,  
02:43:52: it's like you're already on that graph  
02:43:53: that I showed you guys earlier, you  
02:43:54: know, if this is your performance when  
02:43:56: your token count is really low, you're  
02:43:57: probably already like down over here.  
02:43:59: You have some loss in percentage, which  
02:44:02: is just ultimately not efficient for  
02:44:04: business purposes. And you're probably  
02:44:05: wondering like, well, Nick, how bad is  
02:44:06: it really? What I want to do here is I  
02:44:08: just want to show you a quick example on  
02:44:10: some older models. And obviously, keep  
02:44:12: in mind that in order for us to do  
02:44:13: research on things, they necessarily  
02:44:14: have had to been out for a while. Um,  
02:44:16: but older models and how their accuracy  
02:44:18: on tasks scales with the number of  
02:44:21: documents in the input context. So  
02:44:23: number of documents in the input context  
02:44:24: is basically equivalent to tokens in  
02:44:26: this way. So I don't know just call the  
02:44:29: the number you know one document in this  
02:44:31: case is probably equal to like 1,000  
02:44:33: tokens or something like that. So as we  
02:44:36: see here at the very beginning when the  
02:44:37: context is quite small and we only have  
02:44:39: five documents in the input context. You  
02:44:41: know this um model here GBT3.5 turbo 16k  
02:44:44: performs very well. It performs maybe  
02:44:46: somewhere around 75% or so. The second  
02:44:48: we double that accuracy is now to  
02:44:51: slightly over 65%. We double that again  
02:44:53: and now it's almost down to 60%. And  
02:44:55: then if we 1.5x that, now it's like  
02:44:57: somewhere between 50 and 60%. So  
02:44:59: performance here really drops off  
02:45:01: extraordinarily quickly. And so to make  
02:45:02: a long story short, the reason why this  
02:45:04: happens is really similar to what I  
02:45:05: showed you guys earlier on in a demo  
02:45:07: where like if you just have one token  
02:45:09: and then you have three potential tokens  
02:45:11: here, you know, basically every single  
02:45:14: time you are forced to compute like the  
02:45:16: next token in a sequence, the total  
02:45:19: variance of the things that you could be  
02:45:21: generating just kind of go through the  
02:45:22: roof. And so that's that's what's  
02:45:24: occurring here. In order for you know  
02:45:26: this model to somehow know that the  
02:45:28: right answer is over here obviously it  
02:45:30: needs to somehow maintain some degree of  
02:45:32: accuracy and coherence. And that just  
02:45:33: becomes less and less and less and less  
02:45:35: likely uh the more tokens that you  
02:45:37: generate. Now obviously it doesn't  
02:45:38: happen this quickly. It happens over the  
02:45:40: course of many thousands of tokens  
02:45:41: nowadays. But back in the day when I was  
02:45:43: working with um just the base vanilla  
02:45:44: GPT2 the output quality was super  
02:45:47: sensitive to the number of tokens the  
02:45:48: input prompt. Like if you added an  
02:45:49: additional five tokens and those tokens  
02:45:51: were not very high quality tokens, they  
02:45:53: didn't really add a lot of value. Like  
02:45:55: accuracy would plunge off a cliff. Screw  
02:45:57: documents here. Pretend like we're just  
02:45:58: talking number of tokens. At five it  
02:46:01: might be 70, but at 10 it would  
02:46:02: literally jump down and so on and so  
02:46:04: forth. So anytime you try and get to any  
02:46:05: reasonable answer, you're already  
02:46:07: working super super below um you know  
02:46:09: total accuracy limits. Here's another  
02:46:10: example of memory retrieval accuracy. So  
02:46:13: basically if there is some token buried  
02:46:15: super deep in the context of you know a  
02:46:18: model that's doing 2 million48,000  
02:46:21: context window um it forgets it you know  
02:46:24: when there are only 30,000 tokens in the  
02:46:26: prompt or whatever it sees and finds it  
02:46:28: like 100% of the time but if there are I  
02:46:30: don't know 2 million it'll actually  
02:46:32: forget about that a massive chunk of the  
02:46:34: time and it won't even realize like that  
02:46:35: there is a token within its context.  
02:46:37: basically its ability to retrieve things  
02:46:38: from its memory, intermediate memory in  
02:46:41: this case, which is just the chat and  
02:46:42: the prompt, um, plummets. Finally, you  
02:46:44: could see here a needle in the haystack  
02:46:46: sort of example. Um, very similar to  
02:46:48: what we were talking about earlier, but  
02:46:50: basically as the number of tokens goes  
02:46:52: up, you see a massive decrease in just  
02:46:54: the model's ability to meaningfully keep  
02:46:56: track of things. And this is just sort  
02:46:58: of the way that intelligence works,  
02:47:00: right? The more things we're trying to  
02:47:01: juggle and keep in our head  
02:47:02: simultaneously, the higher the  
02:47:04: likelihood that we're going to forget  
02:47:05: any one of them. So, as a demonstrative  
02:47:07: example, let's say I wanted my agent to  
02:47:09: write me an absolutely beautiful poem  
02:47:10: all about the meaning of life and our  
02:47:12: place in the universe. I say, "I'm a big  
02:47:14: fan of MayaangAngelou and Pablo Nuto is  
02:47:16: wonderful as well. Please make this um  
02:47:18: short but also punchy and very  
02:47:21: beautiful." If you think about it  
02:47:23: logically, like this prompt right here  
02:47:24: is a certain number of tokens and I can  
02:47:26: count that here. I'm using a service  
02:47:28: called wordcounter.net. It doesn't count  
02:47:30: tokens, it counts words. But if you want  
02:47:31: the number of tokens, you basically just  
02:47:33: grab the number of words, then you  
02:47:34: multiply it by, you know, uh, 1 divid  
02:47:37: 0.7 approximately. If I do that math,  
02:47:40: this is somewhere on the order of like  
02:47:42: 67 tokens. But I want you to look  
02:47:44: really, really closely at what I just  
02:47:46: wrote here. Are all of these words  
02:47:48: required in order to get the model to do  
02:47:50: something for us? Like what is the  
02:47:52: information density of this sentence?  
02:47:55: Hello. Is that required? Probably not,  
02:47:58: right? I could probably realistically  
02:48:00: remove that. could. It's kind of a long  
02:48:02: way to say can. Can can you is kind of a  
02:48:05: long way to just tell it to write  
02:48:06: something. So, write me an absolutely  
02:48:09: beautiful do I need that? No. Write me a  
02:48:12: beautiful poem all about no about the  
02:48:15: meaning of life and our place in the  
02:48:18: universe. I say  
02:48:23: emulate Maya Angelou  
02:48:27: Pablo Naruda.  
02:48:33: Short, punchy,  
02:48:38: and I don't actually need to say very  
02:48:40: beautiful because I just said so earlier  
02:48:43: up here. Now, if you compare what I just  
02:48:44: wrote um initially at 47 words to what I  
02:48:47: wrote here at 22 words, notice how I  
02:48:49: basically said the exact same thing I  
02:48:51: did in the first prompt just in terms of  
02:48:53: the actual like pure information  
02:48:54: density. I just did it in less than half  
02:48:57: of the words. So now instead of 67  
02:48:59: tokens, this is probably somewhere right  
02:49:00: around like, you know, 28 tokens or  
02:49:02: something like that. What that means,  
02:49:03: walking back to our example, is you can  
02:49:04: realistically significantly improve the  
02:49:07: ultimate quality of an output just by  
02:49:10: refactoring the sentences that you feed  
02:49:12: into a prompt. Instead of hello, could  
02:49:14: you write me an absolutely beautiful  
02:49:15: poem all about the meaning of life or  
02:49:16: whatever, I could create a new prompt  
02:49:19: instance and then I could just say the  
02:49:20: exact same thing. And instead of me  
02:49:22: doing this on, you know, two lines or  
02:49:23: something like that, I could do this on  
02:49:24: one line. And although it is very  
02:49:27: difficult to determine the quality of a  
02:49:29: poem quantitatively what is occurring  
02:49:31: statistically is the quality of this  
02:49:33: poem over here will be better than the  
02:49:35: quality of this poem over here. The  
02:49:37: reason why is I just wrote it in a  
02:49:39: shorter sort of punchier way. So as  
02:49:40: opposed to if you think about this graph  
02:49:42: um you know quality and then the prompt  
02:49:45: length  
02:49:48: as opposed to me being somewhere over  
02:49:50: here like in this example realistically  
02:49:52: this example I'm probably somewhere over  
02:49:54: here right so the reason I'm showing you  
02:49:56: this is because this is exactly what  
02:49:58: models are actually doing under the hood  
02:50:00: instead of writing in in like laborious  
02:50:02: long sort of ways what they are doing is  
02:50:04: they're actually compacting the words  
02:50:05: that you are saying into as high an  
02:50:08: information density summary of your  
02:50:10: prompt as humanly possible. And they  
02:50:11: have a couple of strategies to do this.  
02:50:13: I don't know if you guys have seen like  
02:50:14: reasoning tokens, but the way that  
02:50:16: reasoning occurs here is it's actually  
02:50:17: done like a very high information  
02:50:19: density way. They actually specifically  
02:50:22: have trained the model to write in a way  
02:50:24: that is shorter on tokens as opposed to  
02:50:26: longer. If you look at other models out  
02:50:28: there like GPTOSS 20 bill for instance  
02:50:31: or maybe 120 bill, um these are open  
02:50:33: source models that OpenAI released a  
02:50:34: little while ago. You'll notice when you  
02:50:36: expand the reasoning tokens a very  
02:50:38: peculiar thing. It writes super short.  
02:50:40: It says need to define X but also Y but  
02:50:44: maybe Z. And you're like what the heck's  
02:50:47: going on? This is like an alien really  
02:50:48: short form way of writing. Well, the  
02:50:50: reason why it's writing that way is  
02:50:51: because it's just much higher  
02:50:52: information density. And the higher  
02:50:53: theformational content in your prompt  
02:50:55: per token, the ultimate better response  
02:50:58: you are going to get. Another strategy  
02:51:00: that models will use is they will  
02:51:01: compact. Okay? And what I mean by this  
02:51:03: is basically every time you feed in any  
02:51:05: prompt to a model, what it's also doing  
02:51:07: is it's going back and feeding in every  
02:51:09: message that you and it have ever sent  
02:51:10: to each other in the same chain. So what  
02:51:12: compaction is is it basically is just  
02:51:14: you take the entire history of your  
02:51:17: prompt and then you just summarize it.  
02:51:18: Summarize everything we've talked about  
02:51:21: so far. So now I'm just going to have it  
02:51:23: summarize it all into a very succinct  
02:51:25: message. And then the way the compaction  
02:51:27: works is once we hit a certain token  
02:51:29: amount which uh could be you know 50% of  
02:51:31: the total number of tokens allotted or  
02:51:33: whatever this summary is then fed into  
02:51:35: the next instance of the model and so  
02:51:37: now you know a future instance of in  
02:51:39: this case claude code would have access  
02:51:40: to more or less the full summary. Sure  
02:51:42: we'll miss some details but a lot of  
02:51:44: those details aren't really that  
02:51:46: consequential or important anyway. Think  
02:51:47: of how many fewer tokens this is than  
02:51:49: literally my entire conversation history  
02:51:51: from start to finish. Another big issue  
02:51:53: is when your agent calls an MCP tool  
02:51:55: directly, the entire response goes into  
02:51:57: the context. So if I were wanted to pull  
02:52:00: a document from Google Drive, for  
02:52:01: instance, I would actually then have to  
02:52:03: store the entire thing in my context, at  
02:52:04: least the way models are right now. If I  
02:52:06: wanted to query a Google sheet for like  
02:52:08: 10 rows or something, let's say all 10  
02:52:10: rows had like 20 columns each. Well, now  
02:52:12: I have 200 additional cells within my  
02:52:14: context. Meaning that your agent can hit  
02:52:16: the context ceiling really fast. they  
02:52:18: can burn a ton of money and so on and so  
02:52:19: forth when you use generalized MCP  
02:52:21: tools, not tools that you build  
02:52:22: yourself, but ones that other people  
02:52:23: build for you without really optimizing  
02:52:25: the process.  
02:52:27: Last thing I'm going to note on this is  
02:52:29: not all MCP servers are created equal. A  
02:52:31: lot of servers are rushed to market to  
02:52:32: capitalize on the hype. I know a couple  
02:52:34: just off the top of my head that are  
02:52:35: just super poor. They don't return like  
02:52:37: any good error codes. They don't even  
02:52:39: interact with the APIs correctly and  
02:52:40: tons of people are unfortunately  
02:52:41: struggling because of that. Um, some  
02:52:43: good examples are perplexities and NAND  
02:52:45: servers. Uh, but some really bad  
02:52:47: examples of this, too. I'm not going to  
02:52:48: name the names, but some are a complete  
02:52:49: joke. In general, you will know when you  
02:52:51: start interacting with an MCP server.  
02:52:53: Just going to flag a bunch of errors.  
02:52:54: Your model's just going to be dumb as  
02:52:55: hell. You could tell pretty quick. All  
02:52:57: right, so let me show you how easy it is  
02:52:59: to connect the Google Drive MCP server.  
02:53:00: We've already done a little bit of MCP.  
02:53:02: I've obviously wanted to tease that  
02:53:04: throughout the course to keep you guys  
02:53:05: um interested and engaged, but this time  
02:53:07: I'm actually going to do a full  
02:53:08: comprehensive walkthrough on how to do  
02:53:09: it. We're going to connect this to our  
02:53:10: agent, and then we're going to use it to  
02:53:11: perform a really simple operation. I  
02:53:13: just want you to notice how how seamless  
02:53:14: the integration is. Once it's set up, I  
02:53:16: don't actually have to even like set up  
02:53:18: the directive or the script or anything.  
02:53:19: I can just like uh communicate with it  
02:53:21: in plain language and it can go in and  
02:53:22: call the appropriate tools for me. Let's  
02:53:24: talk MCPs. Now, as I've talked about,  
02:53:26: model context protocol servers differ in  
02:53:28: their quality. Some were made pretty  
02:53:30: hastily, others were made very um  
02:53:33: carefully and are very high quality. But  
02:53:35: because of this, you do have to be a  
02:53:36: little bit careful and be open to doing  
02:53:38: some trial and error when it comes to  
02:53:39: adding your own MCPs. Regardless, I'm  
02:53:41: going to show you guys how simple and  
02:53:42: easy it is to do. First of all, there  
02:53:44: are tools and websites out there like  
02:53:46: mcpmarket.com  
02:53:48: and mcpservers.org  
02:53:50: whose sole job it is to basically  
02:53:52: categorize and then list all of the good  
02:53:55: MCP features out there. So, as you can  
02:53:57: see, there's an MCP for Trigger Dev, MCP  
02:54:00: for OpenSpec, Fast API, Pipe Dream, PAL,  
02:54:04: and these on these tools anyway are  
02:54:06: basically rated uh based off of their  
02:54:08: quality. So, the higher up the better,  
02:54:10: right? So, if you want the ability to  
02:54:11: automate browser interactions for large  
02:54:13: language models using Playright, this is  
02:54:15: the MCP for you. You know, if you want  
02:54:16: Chrome DevTools, this is the MCP model  
02:54:19: for you. If you want to automate, I  
02:54:21: don't know, Sereno specifically, then  
02:54:23: this is the one for you, and so on and  
02:54:24: so on and so forth. What I want to do in  
02:54:26: this video is show you just how easy it  
02:54:27: is to set one up. Um, you guys have  
02:54:29: already seen me do this for ClickUp,  
02:54:31: although that wasn't the point of the  
02:54:32: tutorial. What I'm going to do in this  
02:54:33: demo is just be a lot more specific  
02:54:35: about it. So, simplest and easiest way  
02:54:37: to get up and running with an MCP is  
02:54:38: just to ask your agent. So, I'm just  
02:54:40: going to say, hey, I want to set up a  
02:54:41: Gmail MCP so that I can send emails on  
02:54:44: demand from my email address. And then  
02:54:47: I'm going to give it some details just  
02:54:49: that it knows that, you know, this is  
02:54:51: like a Google Workspace sort of address.  
02:54:53: And let's see what it does. First, it's  
02:54:56: going to look and see whether or not  
02:54:58: there's some email MCP already. It's  
02:55:00: probably not going to find it. It really  
02:55:02: does help to open up these thinking  
02:55:04: modules. So now it's going to say, "Hey,  
02:55:06: you know, I see you've already set up an  
02:55:07: SMTP email for this email address, but  
02:55:10: instead here are two approaches. First,  
02:55:12: you can do quick SMTP. Second, you can  
02:55:15: do the Gmail MCP." So obviously, I want  
02:55:17: to do Gmail MCP. Let's do the Gmail MCP.  
02:55:22: I want you to do everything you can for  
02:55:24: me. Typically, models will give you  
02:55:26: instructions and stuff like this, but  
02:55:28: it's much better just to have them do it  
02:55:29: all for you. So, anytime you don't  
02:55:31: really know what to do or it's laborious  
02:55:33: or involved, just see how much the model  
02:55:34: can do for you. And that's what it is  
02:55:36: currently doing. Okay, cool. And this  
02:55:38: actually ended up finding a previous  
02:55:39: OOTH instance somewhere on my computer.  
02:55:41: I should note it was not in this folder.  
02:55:43: I just asked it to get up and going.  
02:55:44: It's running into some issues here  
02:55:46: because I haven't actually done this for  
02:55:48: this MCP before, which is  
02:55:49: understandable. Now, it's going to add  
02:55:51: some to my cloud config. Okay, now it's  
02:55:53: asking me to sign in. So, I'm going to  
02:55:54: sign in right over here. Cool. Says the  
02:55:56: authentication successful. We can now  
02:55:58: close this window. Okay, so now I just  
02:55:59: need to restart cloud code. Okay,  
02:56:05: just going to go MCP or manage MCPS.  
02:56:09: See that I had have my Gmail MCP  
02:56:11: connected.  
02:56:12: And now I can just say, "Hey, send an  
02:56:15: email to Nicholas orgmail.com  
02:56:19: saying what's up." Boom. Just sent me  
02:56:20: the email. Fantastic. That was easy.  
02:56:23: Okay, that's cool. Um, now that we've  
02:56:25: sent the email, obviously we have to  
02:56:26: talk about how to set up your own MCP  
02:56:29: servers, which is way cooler. So, how do  
02:56:31: you actually go about this process?  
02:56:32: Well, I didn't actually know until quite  
02:56:34: recently. I just asked how would I  
02:56:35: create my own MCP server, and now it's  
02:56:37: giving me a bunch of knowledge. Here's  
02:56:39: how to create your own server using  
02:56:40: Python. So, hypothetically, just for the  
02:56:43: purpose of this demonstration, I want to  
02:56:44: set up a really simple MCP, one that um  
02:56:46: just does something really  
02:56:47: straightforward. Just reads my website.  
02:56:49: Maybe it has some information about my  
02:56:50: website, and then it just like returns  
02:56:51: information about it. So, I said,  
02:56:53: "Create a simple custom MCP server whose  
02:56:55: sole job it is is to interact with this  
02:56:57: website, www.leftclick.ai."  
02:57:00: Now, in case you guys didn't know,  
02:57:01: leftclick.ai is my business. Um, we are  
02:57:04: the definitive AI growth partner for  
02:57:05: fastmoving B2B companies. Uh,  
02:57:07: essentially what we do is we build  
02:57:09: outbound growth engines that supplement  
02:57:11: AI to do things like personalize the  
02:57:13: emails, find leads, and so on and so  
02:57:15: forth. I talk about it a lot on my  
02:57:16: channel. And so, literally all I want  
02:57:18: this MCP to do is basically just to be  
02:57:20: be a resource for this website. I want  
02:57:22: people to be able to download it and  
02:57:23: then just be like, "Hey, tell me about  
02:57:24: leftclick and I want it to call the  
02:57:26: MCP." Is that something you need? No,  
02:57:28: obviously not. But you don't need MCPs  
02:57:30: in general. MCPS are just convenient,  
02:57:32: nice little wrappers around functions.  
02:57:33: Moving back to Cloud Code here, you can  
02:57:35: see that it now created an MCP-servers  
02:57:38: folder. And what it's doing next is  
02:57:39: it'll write the server Python code. I  
02:57:42: have no idea what that Python code looks  
02:57:43: like. After that, it'll create some TOML  
02:57:46: for dependencies before providing some  
02:57:48: registration instructions for me. Okay,  
02:57:50: so it looks like it just finished.  
02:57:52: Creates a server that exposes five  
02:57:54: tools. Get company overview, get  
02:57:56: services, get booking link, get case  
02:57:58: studies, and search site. So that's  
02:58:00: pretty easy. It's saying, "Hey, do you  
02:58:01: want to register with cloud code?" I'll  
02:58:03: just say, "Great. Sounds good.  
02:58:04: Register."  
02:58:06: It'll go through the rest of that  
02:58:07: process for me. Okay. So now I'm going  
02:58:10: to do a new instance of Cloud Code.  
02:58:12: Again, going to go /mcp status. It's now  
02:58:15: loading my servers. And you can see now  
02:58:16: we have the leftclick st server  
02:58:18: available. So go to bypass permissions  
02:58:20: and then I'll say tell me about  
02:58:22: leftclick. Now what occurs when this  
02:58:24: happens is because we have access to the  
02:58:26: MCP data, it'll actually find that and  
02:58:28: then get me information about it. So  
02:58:30: that's what's happening right here. We  
02:58:32: called the MCP server as opposed to  
02:58:34: doing something else. Maybe I'll say  
02:58:36: what's the booking link. The reason I'm  
02:58:39: asking this is because I saw there was a  
02:58:40: booking link feature. So it's going to  
02:58:42: call the get booking link function. Here  
02:58:44: it is. Leftclick.ai I book a call to  
02:58:46: schedule a complimentary 30-inut  
02:58:48: discovery call. Now, in my case, I don't  
02:58:50: think I actually have a calendar, which  
02:58:51: is why it just gave me the thing and  
02:58:52: then it told me where to find it. But  
02:58:54: hopefully, it's clear. You can build  
02:58:55: your own MCP servers super easily. So,  
02:58:57: why build your own MCP servers to begin  
02:58:59: with? Well, generally speaking, like I  
02:59:01: probably wouldn't put together MCP  
02:59:03: servers for most things these days  
02:59:04: unless I wanted to share them with  
02:59:05: others. So, like a creator building an  
02:59:08: MCP server for all of his followers to  
02:59:10: use, that's a pretty good um option. And  
02:59:12: so maybe if there's something cool that  
02:59:14: you know I want to share with you guys,  
02:59:15: I might do that and then make it  
02:59:16: publicly available. But aside from that,  
02:59:18: like why would you build an MCB server  
02:59:20: instead of maybe using cloud skills or  
02:59:22: do I've had a lot of people ask me this,  
02:59:24: Nick, why don't you uh recommend MCP  
02:59:26: more often and so on and so forth. And  
02:59:28: the reason why is it's just not really  
02:59:29: required. MCP is positive in so far that  
02:59:32: it standardizes the ability to call  
02:59:34: tools and whatnot, but it's also  
02:59:35: negative in so far that it loads a ton  
02:59:37: into context. Like what you're not  
02:59:40: seeing here is how many tokens that I am  
02:59:41: essentially consuming by having this MCP  
02:59:44: server. If I go back slash and then  
02:59:45: write the word context, you'll see that  
02:59:47: it actually includes a bunch of  
02:59:48: information about my context usage. And  
02:59:50: so of the basically the entire  
02:59:52: conversation we've had so far, um I've  
02:59:55: used 1.4% in the system prompt, which is  
02:59:57: just the um you know, claude.mmd, 7.4%  
03:00:00: in my system tools, which is just  
03:00:02: something I don't have control over. And  
03:00:03: you'll see that there's 8.2% 2% of my  
03:00:06: entire context window dedicated just to  
03:00:07: MCP tools. The rest of the stuff, 0.6%  
03:00:10: 0.6% of my messages. And so what's  
03:00:12: really really kind of annoying is that  
03:00:14: this thing has basically filled up about  
03:00:16: half of my entire contact window. And  
03:00:18: really I just have like a bunch of  
03:00:19: really simple tools. Leftclick at  
03:00:20: company overview, uh, Gmail send email.  
03:00:23: You know, this is eating up a ton of my  
03:00:25: total token space if you think about it.  
03:00:27: The left click server itself is uh  
03:00:29: almost what I guess that's like 3,000 or  
03:00:31: so over 3,000 3,300 or something like  
03:00:34: that um of my tokens. And you know these  
03:00:36: tokens aren't free. I spend money to use  
03:00:38: these tokens. I also obviously every  
03:00:40: time I make a message and you know have  
03:00:43: some output um the number of tokens in  
03:00:45: my prompt it does affect the output  
03:00:47: quality which we're going to talk about  
03:00:48: later. So, for the most part, I don't  
03:00:50: actually recommend using MCPS unless  
03:00:52: it's something hyper standardized or  
03:00:53: unless it's like a one-click thing and  
03:00:55: uh unless, you know, you're building one  
03:00:57: that you want to, you know, share maybe  
03:00:58: with your team or maybe with like a  
03:01:00: group of people. All right, so now let's  
03:01:01: talk about building the workflows. I've  
03:01:03: built a bunch of workflows for you  
03:01:04: throughout various demos, but I now I  
03:01:06: want to provide you guys a systematic  
03:01:07: approach to be able to do so yourself  
03:01:09: really easily and really  
03:01:10: straightforwardly. First major  
03:01:12: principle, everything begins and ends  
03:01:15: with your system prompt. That system  
03:01:17: prompt, as we know, is typically called  
03:01:18: agents MD, claude MD, Gemini MD, or  
03:01:22: cursor MD. And there are many more  
03:01:24: naming conventions. I'm not going to  
03:01:25: cover them all. The [snorts] name  
03:01:26: basically just needs to match whatever  
03:01:27: your IDE or agent looks for. And the  
03:01:30: content should be identical regardless  
03:01:31: of how you call it. Now, for D  
03:01:33: specifically, I'll show you guys exactly  
03:01:34: what mine looks like in a sec. This  
03:01:36: system prompt or agents MD or cloud MD  
03:01:38: or whatever, it's basically just a  
03:01:40: supercharged prompt. When you  
03:01:41: communicate with chatbt in your window  
03:01:43: or in your browser and you say, "Hey, I  
03:01:44: want you to do whatever for me. That's a  
03:01:46: pretty short prompt. This one is  
03:01:47: basically a prompt that's inserted every  
03:01:49: time and it's just super super long,  
03:01:51: super intense, super comprehensive, and  
03:01:53: it covers more or less all of the edge  
03:01:55: cases and ideas that you want the model  
03:01:56: to have. It should explain your  
03:01:58: framework. It should also explain your  
03:02:00: thinking, what you want it to do at  
03:02:01: every step, and then more. This is how  
03:02:03: you customize your agent essentially, so  
03:02:05: it's not just a cookie cutter vanilla  
03:02:06: agent that functions the same for  
03:02:07: everybody else. The prompt right now is  
03:02:09: kind of the moat. Now, I do recommend  
03:02:10: you to copy and paste mine because it's  
03:02:12: just like out of the box pretty good.  
03:02:13: But there's some important things I'd  
03:02:14: like you guys to make sure to include  
03:02:16: regardless of whether you're using mine  
03:02:17: or whether you guys are using somebody  
03:02:19: else's. The first is you should explain  
03:02:21: the framework. So whatever framework  
03:02:24: you're using, whether you are using do  
03:02:25: or claude skills, you should actually  
03:02:26: explain that to the model. You should  
03:02:28: tell them where the resources are. You  
03:02:30: know, hey, directives are in the  
03:02:31: /directives folder. Hey, you should use  
03:02:33: TMP if you want to store temporary  
03:02:35: files. Make sure to delete temporary  
03:02:36: files after you're done. I also find a  
03:02:38: lot of success in explaining the  
03:02:39: rationale behind the framework. It  
03:02:41: reduces error rate significantly. So I  
03:02:42: don't just say hey you're using the do  
03:02:44: framework I say hey right now as a large  
03:02:46: language model the probability that you  
03:02:48: can do things completely on your own  
03:02:49: without any framework is pretty low  
03:02:51: because of that I'm using a framework  
03:02:52: called directive orchestration execution  
03:02:54: here's how it works directives store  
03:02:56: whatever orchestration is you execution  
03:02:59: does whatever by using this framework  
03:03:01: you significantly reduce your error  
03:03:02: rates and blah blah blah blah here's why  
03:03:04: you should do this right we actually  
03:03:05: convince the model you almost have to  
03:03:07: get like buyin from the model when you  
03:03:09: get buyin from the model the resulting  
03:03:10: outputs are a lot higher quality the  
03:03:12: second thing you should include is an  
03:03:13: explanation of self- annealing. Now, I'm  
03:03:15: kind of cheating here because I haven't  
03:03:16: actually got to this point, but bear  
03:03:17: with me. Self- annealing is the process  
03:03:19: of the model fixing its own mistakes  
03:03:20: without coming to you first. So, rather  
03:03:22: than just break like an old school  
03:03:24: automation, self- annealing means if  
03:03:26: there's an error, you then feed that  
03:03:28: error into the model, the model then  
03:03:30: reasons and then it solves and then  
03:03:32: finally updates so that it doesn't run  
03:03:33: into that problem the next time. In a  
03:03:35: nutshell, self annealing allows the  
03:03:37: models to become more resilient. Doesn't  
03:03:39: just get back to working. And every time  
03:03:41: something breaks, it's a feature, not a  
03:03:42: bug, because it reveals weak points in  
03:03:44: your flow that you didn't even know  
03:03:45: existed. I'm going to tell you all about  
03:03:47: self-nealing and go really in depth with  
03:03:49: like system prompts and stuff like that  
03:03:50: later on, but for now, it's sufficient  
03:03:51: that you just know what it is.  
03:03:54: The third thing you need to include is  
03:03:55: you need to include a sense of autonomy.  
03:03:59: What do I mean by this? Well, I let the  
03:04:01: model know that, hey, my goal is for you  
03:04:02: to run autonomously without me. You are  
03:04:04: an agentic workflow. I say you should  
03:04:07: test each system on its own. you should  
03:04:08: identify mistakes on your own and you  
03:04:10: should loop repeatedly until you make it  
03:04:12: work. I also say, "Hey, be careful when  
03:04:14: you're sending API calls or consuming my  
03:04:16: tokens for testing reasons." And then I  
03:04:19: say, "Hey man, this is really just a  
03:04:21: rule that says come to me only if you  
03:04:23: absolutely need to. I don't want you to  
03:04:24: come to me unless you are 100% confident  
03:04:27: that you cannot solve this thing without  
03:04:28: my human input." And that's very, very  
03:04:30: rare. When you do this, your model gets  
03:04:32: significantly more autonomous and you  
03:04:34: really change it from like this uh a  
03:04:36: co-builder programming thing into like a  
03:04:39: co-orker and a co-mp employee. At the  
03:04:41: end of the day, directives and execution  
03:04:43: scripts are basically living documents.  
03:04:44: So, if there's an error or a constraint  
03:04:46: that you guys find, you should instruct  
03:04:47: your agent to update them. Cool. So,  
03:04:49: talking a little bit more about  
03:04:50: building, if you have SOPs, you're  
03:04:51: actually already halfway to having  
03:04:53: strong agentic workflows. All you really  
03:04:54: do is you just open your IDE. You drag  
03:04:57: your existing SOP document from, you  
03:04:59: know, your knowledge base or your  
03:05:01: company PDF or your company uh one drive  
03:05:03: or Google Drive into your workspace. You  
03:05:06: just say, "Hey, I just uploaded a file  
03:05:08: into the workspace. Could you turn it  
03:05:10: into a directive and build the execution  
03:05:11: scripts to make it happen?" Now, if it's  
03:05:13: a really simple SOP, let's say something  
03:05:15: that doesn't even need an execution  
03:05:16: script necessarily. It's just like a an  
03:05:18: AI prompt thing, it it'll just do it and  
03:05:20: it'll do it like really quickly. If it's  
03:05:22: a complex one, it may ask you to verify  
03:05:23: its approach. Hey, you know, here's some  
03:05:25: ideas that I have. What do you think I  
03:05:26: should do? Okay. Yeah, let's pick the  
03:05:28: first one. Let's proceed. When the agent  
03:05:29: does this, it'll create the directive in  
03:05:31: /directives. It'll build whatever  
03:05:33: scripts are needed, then store them in  
03:05:34: executions, and then if it doesn't have  
03:05:36: API tokens or whatever, it'll just ask  
03:05:37: you to add them to an ENV. This works  
03:05:39: really well because SOPs are literally  
03:05:41: already directives. They contain  
03:05:42: everything the agent needs, the goals,  
03:05:44: the steps, the inputs, outputs, and edge  
03:05:46: cases. If yours are written correctly,  
03:05:48: all you're doing is you're just  
03:05:49: translating your human readable  
03:05:51: documents into another human readable  
03:05:53: document in the form of directives.  
03:05:54: You're not really getting the agent to  
03:05:56: like come up with anything new. It's  
03:05:57: just reformatting and translating into a  
03:05:59: more token efficient format. All you're  
03:06:00: really doing is converting a recipe into  
03:06:02: a format that some sort of robot chef  
03:06:03: can follow. You're basically like  
03:06:05: programming this thing. If your SOPs  
03:06:07: aren't very good, believe it or not,  
03:06:08: this is actually an opportunity to make  
03:06:10: them better because your agent, knowing  
03:06:12: that it does not have everything that it  
03:06:14: needs in order to do the task, will ask  
03:06:15: clarifying questions. This will force  
03:06:18: you as a systems engineer to resolve  
03:06:21: ambiguities that a human being might  
03:06:23: just figure it out without explicitly  
03:06:24: having to write. The resulting directive  
03:06:27: ends up being a lot better than the  
03:06:28: original SOP a lot of the time. And it  
03:06:31: means that your messy docs become an  
03:06:33: opportunity to actually clean up your  
03:06:34: processes and become a clearer company.  
03:06:37: I think that's really underrated, but  
03:06:39: companies in general tend to bury the  
03:06:42: lead. A lot of the time they don't  
03:06:43: actually make explicit or verbalize all  
03:06:46: of the knowledge within the business.  
03:06:47: It's like, oh, just ask Pete for  
03:06:49: whatever. Send an email to this person.  
03:06:51: I mean, your agent will say, well, like,  
03:06:52: who the heck is that and why does that  
03:06:53: matter? Right? Can we just include the  
03:06:55: information that we need in order to do  
03:06:56: it? Now, if you have a big weight step  
03:06:58: or something, it'll be like, "Okay, to  
03:07:00: be clear, why do you want me to wait?  
03:07:01: What is the purpose of this?" And so,  
03:07:03: the very building process itself can  
03:07:05: actually help significantly upgrade your  
03:07:07: business. Now, let's say you have no  
03:07:09: documentation. Well, if you don't have  
03:07:11: any pre-existing documentation or SOPs,  
03:07:13: no problem. We can still make this work.  
03:07:15: What you do is you begin with some very  
03:07:17: basic bullet points that describe your  
03:07:19: ideas surrounding the agent. I use  
03:07:21: really plain conversational language. I  
03:07:23: will literally write down what I want to  
03:07:25: do as if I'm explaining it to a  
03:07:27: colleague. I have a bunch of people in  
03:07:28: my team. A lot of the time this is  
03:07:29: messages that I would have sent to them.  
03:07:31: So sometimes I literally just go into  
03:07:32: Slack and I say, "Hey, I want you to do  
03:07:34: X, Y, and Z. It should be this. It  
03:07:36: should be that. It should be that."  
03:07:37: After I'm done explaining it like I'd  
03:07:38: explain it to a colleague. I then just  
03:07:40: copy and paste it in my agent. Do not  
03:07:42: overthink the structure. Don't overthink  
03:07:44: the format. Just get your ideas down.  
03:07:45: Agents are really good at formatting  
03:07:47: this. You can also use voice prompts  
03:07:48: like you've seen me do a bunch. And then  
03:07:49: you can refine and add detail later as  
03:07:51: you test and learn and try different  
03:07:52: approaches. The really cool thing is you  
03:07:54: don't actually need to know how to code  
03:07:55: at all. You just need to know how to  
03:07:57: explain what it is that you want, which  
03:07:58: I think is a far more achievable skill.  
03:08:00: This is a real prompt from a lead  
03:08:01: generation system that I just built. I  
03:08:03: said, "Hey, scrape leads from Appify  
03:08:04: based on the industry and location I  
03:08:06: specify. Then verify 80% match my target  
03:08:08: market before doing the full scrape.  
03:08:10: When you're done, enrich missing emails  
03:08:11: using a secondary service like any  
03:08:12: mailinder. Then add everything to a  
03:08:14: sharable Google sheet and send me the  
03:08:15: link." Pretty straightforward and pretty  
03:08:17: simple, huh? All right, let me show you  
03:08:18: a practical demo. All right, let's build  
03:08:20: another agentic workflow together. This  
03:08:22: one I want to be a lead generation or  
03:08:25: lead scraping workflow. You guys might  
03:08:27: have seen me build these sorts of things  
03:08:28: before on my channel. I love building  
03:08:30: them because they are so high leverage  
03:08:32: relative to what I used to have to do  
03:08:34: back in the day. So, I figured I'd just  
03:08:36: bring you guys alongside me for uh one  
03:08:38: of the new lead scraping workflows that  
03:08:40: I'm going to put together. So, the first  
03:08:41: thing I'm going to do, just like I  
03:08:42: always do, is I'm going to give it in  
03:08:44: natural language a set of instructions  
03:08:46: to club. I'm using a voice transcription  
03:08:48: tool. So, I'll say, "Hey, I'd like to  
03:08:50: build a lead generation workflow that  
03:08:53: scrapes publicly available information  
03:08:56: to get me a list of B2B leads. What are  
03:09:00: the three best approaches for this?"  
03:09:03: Now, I kind of know what I want to do  
03:09:05: here, but I want to show you guys how  
03:09:06: you can use an agent, not only as some  
03:09:09: builder, but also as something to assist  
03:09:11: you with the ideation. So what this is  
03:09:13: saying is we could start by using a  
03:09:14: LinkedIn sales navigator or similar  
03:09:16: tools to identify decision makers by  
03:09:19: title, industry, company size, then  
03:09:21: enrich with contact data via APIs. That  
03:09:24: sounds pretty good to me. So I'm going  
03:09:25: to need some additional tool. That's  
03:09:27: okay.  
03:09:29: Let's go with the first. I think I've  
03:09:31: heard of a few different tools we could  
03:09:33: use to do this. Phantom Buster is one.  
03:09:35: There's another one called Vain. Which  
03:09:37: do you think is best for our approach?  
03:09:39: How should we go about this exactly? So,  
03:09:41: it's now going through and it's  
03:09:42: performing a bunch of research on these  
03:09:44: tools. Okay, now it's gone through  
03:09:46: performed a bunch of research on all of  
03:09:48: the tools that we could use and it since  
03:09:50: recommended me a uh a pipeline. So, that  
03:09:52: sounds awesome. I really like this. Why  
03:09:54: don't I say let's do it. Yes, I already  
03:09:56: have a sales navigator subscription.  
03:09:59: Let's do it. Build out a pipeline. I  
03:10:02: also already have a pre-existing  
03:10:04: subscription to any MailFinder, which is  
03:10:06: an enrichment tool. So, why don't we use  
03:10:07: that as part of our flow? I want you to  
03:10:09: build this using the DO framework. Let  
03:10:12: me know if you need anything.  
03:10:15: So now what we've done is we've  
03:10:17: basically taken  
03:10:19: our demand or our request I should say  
03:10:22: and then we've paired it down into a  
03:10:24: much higher probability build path um  
03:10:27: just based off a couple of back and  
03:10:28: forth questions. If you think about it,  
03:10:30: the total amount of time that it takes  
03:10:32: an agent to build something is pretty  
03:10:34: short, all things considered, but it's  
03:10:36: still like five or 10 or 15 minutes. If  
03:10:39: you screw up and you go down the wrong  
03:10:41: path, in order for you to walk back and  
03:10:43: start fresh, you're probably going to  
03:10:44: have to spend another 10 or 15 minutes  
03:10:45: in order to have the agent rebuild the  
03:10:47: next thing. And so, at a very high  
03:10:49: level, giving it a tiny bit of input  
03:10:51: initially is super powerful, and it's  
03:10:53: also a big time saver. So, I usually  
03:10:55: recommend going back and forth at least  
03:10:56: a little bit while it does its searches.  
03:10:58: and you know use your own human  
03:11:00: knowledge really to pair down the total  
03:11:02: um possible number of paths. So it's  
03:11:05: going through building a Google Sheets  
03:11:07: LinkedIn lead genen lead enrichment  
03:11:09: pipeline and any mailfinder client  
03:11:11: pipeline. All right, once it's almost  
03:11:13: done all of the scripts, it's going to  
03:11:15: create a directive just to tie  
03:11:16: everything together. Do all this for me.  
03:11:20: Okay, I'm now having it wrap things up.  
03:11:23: We can now start giving it a test.  
03:11:25: Obviously, it is one thing if a model  
03:11:27: tells you that it is good to go. It's a  
03:11:29: complete other thing um whether or not  
03:11:31: the flow actually works. So, we always  
03:11:33: have to verify that the flow works with  
03:11:34: with a real test. Okay, it's now testing  
03:11:37: out any mailinder, testing out the  
03:11:39: Google Sheets connection.  
03:11:41: Looks like it found an issue with the  
03:11:43: way that it was going to do the  
03:11:44: connection. I added a credentials.json  
03:11:46: file here just from another workspace,  
03:11:48: which is basically like an ooth thing.  
03:11:50: Um I didn't generate this thing. I had  
03:11:52: the model generate it for me. It's now  
03:11:54: going to ask to authenticate for the  
03:11:57: first time. Anytime you connect to a new  
03:11:59: Google credential with OOTH, you're  
03:12:01: going to have to do this. Now I have the  
03:12:02: browser authentication. I'm just going  
03:12:04: to pump over here and connect this. This  
03:12:06: is a great opportunity for me to point  
03:12:08: out a common issue that people have with  
03:12:10: the Gentic workflows. It's where they um  
03:12:13: essentially have the model generate a  
03:12:14: test case for them. So in this case,  
03:12:16: that's what's occurring here.  
03:12:17: Test_leads.csv.  
03:12:19: It then uses the test data essentially  
03:12:21: to test end to end to see whether or not  
03:12:23: the flow works. That's not good enough  
03:12:26: because if you think about it, the model  
03:12:27: just created a bunch of scripts. So the  
03:12:29: test case that it will come up with is  
03:12:31: most likely going to be in the same  
03:12:33: format that all of the rest of the  
03:12:35: scripts and so on and so forth expect.  
03:12:37: What's way more informative is for us  
03:12:38: just to do this entirely based off new  
03:12:40: data. So that's what I'm going to do  
03:12:42: next. I don't really want to export the  
03:12:44: leads from Vain. I instead want you to  
03:12:46: do all that for me.  
03:12:50: Okay. And it looks like it now is ready  
03:12:51: for a test. So I just need to give it a  
03:12:53: sales marketing or a sales navigator URL  
03:12:55: anyway and it'll do everything or I  
03:12:57: could run it myself with one command.  
03:12:59: That's cool. Um what I'm going to do is  
03:13:01: I'll just go back to LinkedIn sales nav  
03:13:03: here and I have a link. Basically what  
03:13:04: what happens on LinkedIn when you want  
03:13:06: to find something like a list of people  
03:13:08: is you need to generate a search on the  
03:13:09: lefth hand side. Now you just need to  
03:13:11: copy over the URL and then just paste it  
03:13:12: in. So I'm just going to paste this in  
03:13:13: and I'm just going to see what happens.  
03:13:14: We'll just test it in 10. All right. And  
03:13:16: now it has found 231 prospects. So it's  
03:13:19: going to go through and scrape the 231  
03:13:21: profiles via vein. Then enrich with any  
03:13:23: mailinder before exporting to Google  
03:13:25: Sheets. Okay, it had some issues with a  
03:13:28: particular API call uh to Vain. It since  
03:13:31: self-annealed and automatically fixed it  
03:13:33: all. So it's just continuing down the  
03:13:35: building process on that first run. Once  
03:13:37: I have it finished this first run, I'm  
03:13:38: just going to ask it to do a second run.  
03:13:40: And I'm going to do it completely from  
03:13:41: scratch. So it's going to be like a cold  
03:13:43: start. I'm going to instantiate a fresh  
03:13:44: cloud instance, one that has no idea  
03:13:46: what the heck's going on. Then we'll see  
03:13:48: how it goes. Okay, one of the outputs  
03:13:50: was buffered. That just means that uh  
03:13:52: basically it was in a loop repeating. So  
03:13:54: I just paused it and said how are we  
03:13:56: doing? Looks like it's still running. So  
03:13:58: Python is buffering the output. We're  
03:14:00: just going to wait for the completion.  
03:14:01: Sometimes some of these tool calls can  
03:14:02: take a fair bit and that's what's  
03:14:03: happening with any mailfinder. The  
03:14:05: reason why this is actually good for us  
03:14:07: is because I get to show you guys later  
03:14:08: on what it looks like to optimize a  
03:14:10: workflow realistically. And I know this  
03:14:12: because I've done a fair amount of  
03:14:14: enrichment at this point. You do not  
03:14:16: need to take this long to enrich 200  
03:14:18: records. You could probably enrich 200  
03:14:20: records in maybe like 15 seconds or so  
03:14:23: through bulk requests. Um the first time  
03:14:26: that a agent ever builds a workflow,  
03:14:29: it's going to do so in as simple a way  
03:14:31: as humanly possible. Typically through  
03:14:33: serial requests, which just means that  
03:14:34: it's sending one request at a time,  
03:14:36: waiting until the request is done, then  
03:14:38: sending another request after that. But  
03:14:40: what you can do with a lot of workflows  
03:14:42: is you can parallelize them, which means  
03:14:43: you could actually send 200 requests  
03:14:45: simultaneously and then wait for the  
03:14:47: outputs of all 200 in the same time  
03:14:49: block as opposed to, you know,  
03:14:50: independently. So I'm still going to  
03:14:52: wait for this thing to finish because I  
03:14:53: want this test to be done end to end at  
03:14:56: least once. Um, after that, we're going  
03:14:57: to look into ways to make this faster  
03:14:59: through parallelization and so on and so  
03:15:01: forth. Okay, so I got a little bit bored  
03:15:02: and I just said, hey, could we make this  
03:15:04: way faster? It's since um offered to  
03:15:06: batch all of these requests. So that's  
03:15:08: what it's going to do next. and let's  
03:15:10: see how quickly it performs. While I'm  
03:15:12: doing that, let me just create a new  
03:15:14: search. Maybe instead of United States  
03:15:16: residents, um I want to search Canadian  
03:15:18: residents. [gasps] That way, we'll be  
03:15:21: able to split test this very quickly and  
03:15:22: easily. As you can see here, we have 31  
03:15:25: results. Uh maybe we'll also do posted  
03:15:27: on LinkedIn, so maybe 45 or something  
03:15:28: like that. Okay, no, it's just 20. If I  
03:15:32: deselect this, how many do we get? 683.  
03:15:35: Uh too many. Why don't we just do  
03:15:37: Vancouver instead? I I want like between  
03:15:39: 50 to 100.  
03:15:42: Okay, 66. That's perfect. So, this is  
03:15:44: going to be the URL I use to test the um  
03:15:46: totally fresh app. It's now just going  
03:15:48: to go through the process of self  
03:15:50: annealing, running, testing, and so on  
03:15:51: and so forth. Looks like it found 139  
03:15:54: valid emails of my 231 sent. Now, it's  
03:15:57: just going through and updating the  
03:15:59: script a couple more times. Cool. It's  
03:16:00: gone through and since found me a bunch  
03:16:02: of leads, I can open up the spreadsheet  
03:16:04: to get 159 rows. So, um, these are all  
03:16:08: of the the records with email addresses.  
03:16:11: Um, there were more records that didn't  
03:16:12: have email addresses, but we just left  
03:16:13: those out. Obviously, this is pretty  
03:16:15: solid, but, um, I want to number one,  
03:16:18: make sure that we're documenting this.  
03:16:19: So, I'm going to head back over here,  
03:16:21: and I'll say make sure to document all  
03:16:23: changes, both directives and executions.  
03:16:27: Once it's done with the documentation,  
03:16:29: I'm then going to open up a totally new  
03:16:30: fresh instance and then go through and  
03:16:33: then um, update and then test. Cool. And  
03:16:36: it looks like it did some updating.  
03:16:38: That's pretty solid. What I'm going to  
03:16:39: do next is I'm just going to open up a  
03:16:40: new instance of Cloud Code. Going to set  
03:16:43: it to bypass permissions and I'll say,  
03:16:45: "Hey, here's a search URL. Scrape these  
03:16:50: using our pipeline."  
03:16:52: All right. So now this is a totally new  
03:16:55: fresh cloud code instance. Let's see how  
03:16:57: it performs. It's going to start by  
03:16:59: thinking it's checking the directive for  
03:17:01: LinkedIn scraping, which is great.  
03:17:02: That's what we wanted. It's then going  
03:17:04: through here. URL is a sales navigator  
03:17:06: search has a bunch of information here.  
03:17:08: It's going to check how many leads are  
03:17:09: available. Cool. Found 66 prospects. It  
03:17:12: is now going to perform the full scrape.  
03:17:15: Okay. And it looks like we got uh 45 out  
03:17:18: of those 66. So, this did work on a  
03:17:21: totally fresh list. Um took me about 4  
03:17:24: minutes. I got a little bit overeager  
03:17:26: and I was like, "Hey, are you done yet?"  
03:17:27: But realistically, this uh this works  
03:17:30: pretty well. So, I mean, a couple of  
03:17:31: different approaches that I could take  
03:17:32: here. Obviously, I could make this  
03:17:34: better, could make this faster. I could  
03:17:36: set up approaches to dump all this into  
03:17:38: Google sheet instantly using bulk. I  
03:17:40: could do I could do a lot of stuff and  
03:17:42: uh that's what I want to talk about  
03:17:43: next. But for the purposes of this  
03:17:44: demonstration, this is good to go. We  
03:17:46: have essentially created a workflow to  
03:17:49: completely or almost completely automate  
03:17:51: the entire process of scraping LinkedIn.  
03:17:52: Obviously, there is still one manual  
03:17:54: step, which is we need to provide the  
03:17:55: LinkedIn sales navigator URL, but that's  
03:17:57: something that we could reasonably  
03:17:58: automate if we'd like to as well. So,  
03:18:00: here's what you don't need to specify.  
03:18:02: You don't need to know which APIs to use  
03:18:04: or how they authenticate. You also don't  
03:18:05: need to know how to structure the code  
03:18:07: or handle an error case yourself. And  
03:18:08: you don't even need to know any Python,  
03:18:10: any JavaScript, or any programming  
03:18:11: language. The agent's whole job is to  
03:18:13: abstract that complexity away from you  
03:18:14: and turn it into a natural language. A  
03:18:16: really cool hack that I'm using a lot  
03:18:17: more of now is I don't just have the  
03:18:19: agent solve it one approach. I actually  
03:18:21: have the agent produce three approaches  
03:18:22: simultaneously. Then I either pick one  
03:18:24: of the three, whichever one makes the  
03:18:26: most sense, or this is kind of neat,  
03:18:28: [clears throat] I have parallel  
03:18:29: instances of my agent generate all three  
03:18:32: directive and execution scripts based  
03:18:35: off of each approach. I then just test  
03:18:37: their outputs and I rate. I test them on  
03:18:39: things like how fast it is, test them on  
03:18:41: things like how reliable it is and how  
03:18:43: cheap it is, and then I just pick the  
03:18:45: best performing one, and then that's it.  
03:18:46: Why three approaches? Well, if you think  
03:18:48: about it, the cost of exploring multiple  
03:18:50: approaches is basically free. They're  
03:18:52: not it's not free free tokens are not  
03:18:54: free yet but they are very cheap  
03:18:55: compared to the cost of intelligence and  
03:18:57: it's also a big chunk of the search  
03:18:59: space. Uh basically if this is like the  
03:19:01: amount of space you have to search  
03:19:03: through in order to come up with your  
03:19:04: really really cool problem rather than  
03:19:06: have your agent just go like manually  
03:19:08: one by one by one by one and just kind  
03:19:10: of do this whole thing on its own. Um  
03:19:12: you can actually just like quarter this  
03:19:14: you know and in my case I said three but  
03:19:16: you could totally have it four and then  
03:19:17: just have like four agents independently  
03:19:19: simultaneously. I can't draw  
03:19:21: simultaneous executions here, but just  
03:19:23: assume that it is. Explore that search  
03:19:25: base in like a tenth of the time. When  
03:19:26: you do this, I recommend you have it run  
03:19:28: in a temporary folder. So, you say,  
03:19:30: "Hey, do this in a temporary folder.  
03:19:31: Don't do this in the main directive  
03:19:33: execution um framework." Cuz I'm  
03:19:34: actually giving this to a few of your  
03:19:35: brother and sister agents to run  
03:19:37: simultaneously to figure out the best  
03:19:38: approach. There are a couple of  
03:19:39: trade-offs with every single way that  
03:19:41: you build. The first is speed versus  
03:19:43: cost. So, do you need it fast or do you  
03:19:44: need it cheap? Obviously, we're looking  
03:19:45: for situations where we have both, but a  
03:19:47: lot of the time you have to make  
03:19:48: trade-offs. Next is reliability and  
03:19:50: complex complexity. The simple solutions  
03:19:52: do break less often. If you can store  
03:19:54: things in one execution script, it's way  
03:19:55: faster and better than if you store  
03:19:57: things in 10. The next is breadth versus  
03:19:59: depth. So if you cover more ground or go  
03:20:01: really, really, really deep on a few  
03:20:02: items, it's going to depend or it's  
03:20:04: going to change how your agent  
03:20:06: constructs things. And then finally,  
03:20:08: sometimes you just need human judgment  
03:20:09: to weigh these things. So I would  
03:20:10: recommend at least asking your agent,  
03:20:12: how would you do this stuff before you  
03:20:13: actually have it go and build uh every  
03:20:15: approach. If you think about it  
03:20:16: logically, this steering is the highest  
03:20:19: return on investment time that you will  
03:20:21: ever spend across your entire agentic  
03:20:23: workflow career. And the reason why is  
03:20:25: really some of what I talked about  
03:20:26: earlier. If you just look at any process  
03:20:28: that has variability in its outputs,  
03:20:29: okay, this variability grows over time  
03:20:33: as you proceed through the process just  
03:20:35: because there are more and more and more  
03:20:36: and more steps possible, right? And so  
03:20:38: right now, this is kind of like the  
03:20:40: range of all of the possible um  
03:20:42: decisions that the model could make.  
03:20:43: Well, if you think about it, the one  
03:20:45: thing that you have the power to do at  
03:20:46: the very very beginning is you have the  
03:20:48: power to steer what direction this thing  
03:20:50: goes. And so let's say hypothetically my  
03:20:53: goal is over here, right? Or maybe we  
03:20:55: should say my goal is over here. If at  
03:20:58: the very beginning, literally from the  
03:21:00: first step, the model is already in the  
03:21:02: wrong direction. It doesn't really  
03:21:03: matter how much time and energy it takes  
03:21:05: to build things, right? But if you could  
03:21:07: just reorient this approach down over  
03:21:09: here, then your solution is actually in  
03:21:11: the range of all possible outcomes. I  
03:21:13: call this steering just like steering a  
03:21:14: car. If you steer, let's say you're  
03:21:16: going like a real straight line track  
03:21:18: and your car at the very beginning of  
03:21:20: the track is already starting to veer  
03:21:22: off a little bit. Obviously, the most  
03:21:24: important thing you can do as a, you  
03:21:25: know, driver is you could just steer it  
03:21:27: so that it goes basically as as straight  
03:21:29: down the middle of this thing as humanly  
03:21:31: possible, right? And that's just  
03:21:32: ultimately something that really takes  
03:21:34: like a minute or two. I wouldn't  
03:21:35: recommend trying to outsource everything  
03:21:37: to the model, like the thinking itself.  
03:21:38: The first version of anything you build  
03:21:40: probably will not be perfect. And the  
03:21:42: first versions of a lot of the things  
03:21:43: that I build do suck, but that's okay.  
03:21:44: That's actually one of the points. Dough  
03:21:46: really depends on iteration. So just run  
03:21:48: the workflow a few times, watch what  
03:21:50: happens, open up the reasoning loop, and  
03:21:52: then just take some notes on what's  
03:21:53: slow. Hey, I don't really like this.  
03:21:55: Hey, this takes forever. Is that  
03:21:56: necessary? Hey, um, I don't like how  
03:21:58: this had to call this API. Hey, this is  
03:21:59: a little too expensive. How can we do it  
03:22:01: cheaper? Right? Actually, just tell the  
03:22:03: model what it is. Like, it's you're not  
03:22:04: going to hurt its feelings. It's a the  
03:22:06: form of intelligence that none of us can  
03:22:08: really quantify. Don't anthropomorphize  
03:22:10: the damn thing. What'll happen is the  
03:22:12: agent will diagnose the problem and then  
03:22:14: implement a fix. And ideally, assuming  
03:22:15: that you have it in your system prompt,  
03:22:17: it'll also update both the execution  
03:22:18: script and your directive, which means  
03:22:20: next time you run from a fresh instance,  
03:22:22: it will already know the solution. And  
03:22:23: that's typically what I recommend. I  
03:22:24: recommend running it, fixing it, getting  
03:22:26: in that testing loop over and over and  
03:22:28: over again. And when you really want to  
03:22:29: verify that this thing works, you just  
03:22:30: open it up in a new instance and then  
03:22:31: have it run. Every problem that you  
03:22:33: encounter will make your system stronger  
03:22:34: if you're smart. Edge cases will get  
03:22:36: handled that you never anticipated. uh  
03:22:38: and after a few iterations you will have  
03:22:40: a robust workflow uh that I've heard a  
03:22:42: lot of people say this term battle  
03:22:43: tested I think battle tested about is  
03:22:45: about as real and as accurate a way to  
03:22:47: describe it but you'll have something  
03:22:48: that is actually just kind of like been  
03:22:50: there done that it has seen all possible  
03:22:51: instances of the problem because it's  
03:22:53: run 10 or 20 times it sort of knows what  
03:22:55: to expect um you know you basically go  
03:22:57: from a workflow that the very first time  
03:22:59: it runs maybe is 80% reliable to one  
03:23:01: that's 90% reliable to one that's 95%  
03:23:03: reliable one that's 97% reliable one  
03:23:06: that's 98% reliable and so on and so on  
03:23:08: and so on and so forth until it's like  
03:23:09: 99.25% or something. And maybe this is  
03:23:12: the theoretical limit that you reach.  
03:23:13: All right, let's build a lead genen flow  
03:23:14: start to finish using everything that  
03:23:15: I've talked about so far. You remember  
03:23:17: how earlier we created a lead generation  
03:23:19: workflow? Well, what if instead of just  
03:23:22: using one cloud instance to generate it,  
03:23:24: we used multiple cloud instances to  
03:23:25: generate the lead generation workflow in  
03:23:27: parallel. not only would be able to  
03:23:29: generate higher quality lead generation  
03:23:30: workflows, we'd be able to create things  
03:23:32: that are most likely better because we  
03:23:34: are able to search more opportunities  
03:23:36: and options. If that doesn't make sense  
03:23:38: to you, I'm just going to copy and paste  
03:23:39: the same thing that I pasted in here.  
03:23:41: Instead of three best approaches, I'll  
03:23:44: say five best approaches, I'll say be  
03:23:47: comprehensive and give me all possible  
03:23:50: options. And then instead of publicly  
03:23:51: available information, I'll say HVAC  
03:23:54: companies in Texas  
03:23:57: to get me a list of B2B leads and their  
03:23:59: emails.  
03:24:00: Okay, great. Once I give this parent  
03:24:03: agent some room to think, what I'm going  
03:24:05: to do is I'm then going to open up a  
03:24:07: bunch of additional clawed code  
03:24:09: instances. So, new,  
03:24:11: new,  
03:24:13: new,  
03:24:15: new. So, we're going to have five in  
03:24:16: total. What I'm going to do is I'm just  
03:24:18: going to  
03:24:20: set things up so we could see them all.  
03:24:22: Next, I'm going to provide some  
03:24:23: scaffolding. So, I'm just going to say,  
03:24:25: "Hey, your task is to build a lead  
03:24:27: generation workflow according to the  
03:24:29: below details." I'm giving similar tasks  
03:24:31: to five other agents. Since you're  
03:24:33: operating the same workspace, uh to  
03:24:35: minimize the probability of a conflict,  
03:24:37: do all your work in a new tmp/ test3  
03:24:40: folder. And then what I'm going to do is  
03:24:41: I'm just going to feed in all of this.  
03:24:43: So, I'm going to say boom  
03:24:49: boom  
03:24:53: boom  
03:24:57: boom.  
03:25:03: And then boom. And now I'm actually just  
03:25:05: going to run all of these  
03:25:06: simultaneously.  
03:25:08: What's cool is this is going to create  
03:25:10: new folders inside of this TMP which are  
03:25:12: not going to interfere with our other  
03:25:14: directives, our execution scripts. I can  
03:25:15: now remove this top level script here  
03:25:17: for simplicity. And now it's going to go  
03:25:19: through and just create all of these.  
03:25:21: Not all of these are at the exact same  
03:25:22: level obviously, but um you know this  
03:25:24: test two directory structure and the  
03:25:26: test 4 uh when they get created they're  
03:25:28: going to just do their work in there. So  
03:25:30: in this way I'm capable of exploring a  
03:25:32: large number of options in a very short  
03:25:33: period of time. I mean obviously I can  
03:25:35: take a brief highle look at like one of  
03:25:36: these things and say okay this one is  
03:25:38: most likely uh the highest probability  
03:25:40: of working but it's much easier if I  
03:25:42: just explore them and then what I do is  
03:25:44: anytime I run into a hiccup with one of  
03:25:46: these flows I just take a look at what  
03:25:47: the hiccup is and if the hiccup is like  
03:25:49: so big that it would be a pain in my ass  
03:25:51: to deal with then I just drop that and  
03:25:52: then I don't continue. Then for the  
03:25:54: survivors, um, once I have like a pretty  
03:25:56: good-look workflow, I'll test them all  
03:25:58: side by side, ask them to go do a  
03:26:00: scrape, and then once I've done the  
03:26:01: scrape, I can just compare and contrast  
03:26:03: results. What's really sweet is when all  
03:26:05: these things are done, I can sometimes  
03:26:06: combine the best of each, and then I can  
03:26:09: say, "Hey, build a unified lead  
03:26:10: generation workflow that combines the  
03:26:12: best of X, Y, and Z." And then it'll,  
03:26:14: you know, find 30% of leads with one  
03:26:16: approach, 30% of leads with the other  
03:26:18: approach, 30% of the leads with a third  
03:26:20: approach, and so on and so forth.  
03:26:21: Anecdotally, it feels really cool to be  
03:26:23: able to manage and orchestrate this many  
03:26:25: simultaneous builders. I don't usually  
03:26:27: do five at a time, but I just wanted to  
03:26:29: demonstrate that you can explore a very  
03:26:31: large search space in a very short  
03:26:32: period of time. So, after a few minutes,  
03:26:34: these are now beginning to finish. The  
03:26:36: one on the left hand side has tested the  
03:26:38: pipeline with a full batch. Just going  
03:26:39: to take a peek. See, we've now generated  
03:26:41: four of these files. We then have our  
03:26:43: pipeline summary, and now we just need  
03:26:45: to enter some API keys essentially. Now,  
03:26:47: the issue is I've yet to give it a  
03:26:48: Google Places API key or a Hunter API  
03:26:50: key. So, I'll just say, "Could you set  
03:26:53: up the Google API key for me?" I don't  
03:26:56: have Hunter, but I do have an email  
03:26:59: finder. Please do this instead. Over  
03:27:02: here, Apollo.  
03:27:09: Okay. And then one of these wanted a  
03:27:10: sales navigator URL for HVAC companies.  
03:27:13: So, I'm just going to go HVAC. And then  
03:27:15: geography. Why don't we just go Texas  
03:27:17: because I think that's what that was.  
03:27:20: Rest of this looks pretty reasonable.  
03:27:21: It's 4,000 results. I just want a really  
03:27:23: really like simple one. So, I'm just  
03:27:24: going to go change jobs 54. That way, we  
03:27:27: should only get 54. Go back here and  
03:27:29: then I'll feed in the URL.  
03:27:32: I then see an Apollo API key. Yes,  
03:27:35: Apollo API key. It's then going to go  
03:27:38: through  
03:27:40: and give me instructions on one of my  
03:27:42: API keys. So, I'm going to head over  
03:27:43: here to Google Places API. What I want  
03:27:46: is the Places API new apparently. So,  
03:27:48: I'm going to enable this. And now it's  
03:27:50: just a process of getting API keys for  
03:27:52: everything really.  
03:27:54: Copying the API key. Just going to paste  
03:27:57: that in there. This is now testing. This  
03:27:59: is going to test. This is now testing.  
03:28:03: And then we just have these two over  
03:28:04: here which are in the process of  
03:28:06: building. This here ran into an issue  
03:28:08: with one of the scrapers. So, it's  
03:28:10: decided to pivot and then use an Appify  
03:28:11: API token. That's cool. I don't mind  
03:28:13: that. This here on the left is now doing  
03:28:15: some debugging and so on and so forth.  
03:28:17: That's okay. I don't need to be a part  
03:28:18: of this. All I'm doing is I'm just  
03:28:19: overseeing. And if any one of these  
03:28:21: workers needs me for anything, I'll  
03:28:23: provide it. All right. And we are just  
03:28:24: testing across the board. We got 50  
03:28:26: leads running for most of these tests.  
03:28:29: Some of them are 10. That's okay. I'm  
03:28:31: seeing this task over here is running  
03:28:34: into some issues. Namely, the Apollo API  
03:28:36: key that I provided earlier was for a  
03:28:37: totally free account. So, it doesn't  
03:28:38: look like I can it can actually go and  
03:28:40: enrich them. This one here on the left  
03:28:42: looks like it's pretty solid. So, it's  
03:28:44: since found a verified email address.  
03:28:46: That's pretty cool. I did uh no work  
03:28:48: here. I just let it run. This over here  
03:28:51: is doing a batch email scrape. And this  
03:28:53: right over here is now running a  
03:28:55: pipeline test with a fixed client. I've  
03:28:57: actually forgotten what's going on over  
03:28:58: here on the left. So I'll say describe  
03:29:00: what is occurring top to bottom. So this  
03:29:03: is scraping the Google Places API for  
03:29:05: terms like HVAC contractors, heating  
03:29:07: contractors. It's going across 50 Tex  
03:29:10: and cities. Then it gives me a big list  
03:29:12: of leads. It's then enriching with  
03:29:14: emails before exporting to Google  
03:29:15: Sheets. So, that's pretty cool. Let's  
03:29:17: run this on a test of 50. Meanwhile,  
03:29:20: over here on the right, we did run it on  
03:29:22: a test of 50, and it looks like we ended  
03:29:24: up with 26 email addresses. That's  
03:29:26: pretty badass. I should note that not  
03:29:28: all of these are valid. I'm seeing here  
03:29:30: one of them is for somebody that works  
03:29:31: at Neurolink. So, probability of that  
03:29:33: being a valid lead is kind of off. Um,  
03:29:35: I'm going to want to double check that.  
03:29:37: So, I'm going to go back here and I'll  
03:29:38: say, I noticed one of the leads was for  
03:29:40: Neurolink. How are these filters? Are  
03:29:42: they super accurate? Make sure to double  
03:29:44: check. Meanwhile, this one over here on  
03:29:46: the lefth hand side is doing some  
03:29:47: enrichment. This is now actually testing  
03:29:50: to see how many of these leads are HVAC  
03:29:53: related. So, we're seeing a bunch of  
03:29:54: these are HVAC related. A bunch of these  
03:29:56: are not HVAC related. So, uh the search  
03:29:58: that we're going to be providing here is  
03:30:00: presumably going to have to be a little  
03:30:01: bit more specific. I can't just like,  
03:30:03: you know, head over to LinkedIn Sales  
03:30:05: Nav, copy and paste something with a  
03:30:06: term HVAC, and then have it work 100% of  
03:30:08: the time. Okay. on the right hand side.  
03:30:10: This is now giving me some highlevel  
03:30:11: instructions on how I can uh you know do  
03:30:14: the search better. So that's nice. HVAC  
03:30:16: and refrigeration equipment  
03:30:17: manufacturing. Why don't I actually go  
03:30:18: ahead and just do this? So I'm going to  
03:30:19: remove this keyword HVAC. And what I  
03:30:21: want to do is click industry.  
03:30:24: Go down here.  
03:30:27: I see HVAC right over there. I'm going  
03:30:28: to include that. This is 341 results. So  
03:30:32: then I'm just going to copy this and  
03:30:33: paste this back in. Let's run a test on  
03:30:36: 50. Cool. Cool. Cool. Looks like this  
03:30:39: lead flow here worked really well. 18  
03:30:41: out of 20 businesses had websites. 13  
03:30:43: out of 20 had emails. Meanwhile, we  
03:30:45: happen to get Satia Nadella, the CEO of  
03:30:47: Microsoft's email over here. That's  
03:30:49: always fun. Okay, cool. And now we have  
03:30:51: a whole list of steps right over here in  
03:30:53: the middle. So, that's awesome. Gives me  
03:30:56: a brief description of what's going on.  
03:30:57: And yeah, I mean, I like this. So, why  
03:30:59: don't I actually see a result? Where are  
03:31:02: the leads? Looks like it's going to find  
03:31:04: me the leads. Text businesses with  
03:31:06: emails. Then it has them all over here.  
03:31:07: This is cool. So hopefully it's clear at  
03:31:09: this point. I mean I could do pretty  
03:31:10: much whatever I wanted, right? And like  
03:31:11: we've actually gone through and explored  
03:31:12: a tremendous amount of search space in a  
03:31:14: very short period of time. I could for  
03:31:15: instance just um send the same message  
03:31:17: to all five. Hey, show me the results in  
03:31:19: a Google sheet. You know, I could then  
03:31:21: standardize the test and just ask all of  
03:31:23: them to do 20 leads simultaneously and  
03:31:26: then I could just have them really  
03:31:27: quickly test to see which one delivers  
03:31:29: me the highest degree of accuracy on the  
03:31:31: leads. Um I could also disqualify a  
03:31:33: couple. Don't really like this one. I  
03:31:35: mean like it it's working. It just found  
03:31:36: me three. uh with verified emails, but  
03:31:38: I'm seeing that it's using an Apollo  
03:31:40: endpoint, which isn't 100% right. Um  
03:31:42: it's kind of crazy because we're not  
03:31:44: supposed to be able to use Apollo in  
03:31:45: this way. We should be having to pay a  
03:31:47: fair amount of money. And you know, I  
03:31:48: think there are a lot of things that  
03:31:49: realistically anybody could do. You  
03:31:50: could also just use all five of these,  
03:31:51: but yeah, I just wanted to show you guys  
03:31:53: what that looks like. So, what I'm going  
03:31:54: to do is I'm just going to pretend that  
03:31:56: I've now selected three and I'm going to  
03:31:57: say excellent. turn this into directives  
03:32:02: or merge these directives executions  
03:32:05: with the main branch your approach one  
03:32:09: then update everything to ensure that  
03:32:13: the file paths etc are correct that's  
03:32:16: actually really cool I wasn't expecting  
03:32:18: this to do anything with Apollo um I  
03:32:20: mean I fed it in my API key which is  
03:32:22: free but uh yeah normally they don't  
03:32:24: allow you to see any of that and finally  
03:32:26: it ended up finishing and it since  
03:32:28: merged my directives with the main  
03:32:30: directives folder. So I actually have  
03:32:32: the Texas SOS Legen directly here. What  
03:32:34: I could do now is I could test it. I  
03:32:36: could rerun it. I could optimize it by  
03:32:37: just asking it to do things faster and  
03:32:39: faster and faster. And yeah, I was able  
03:32:41: to accurately assess that this is the  
03:32:43: flow that I wanted in light of five  
03:32:45: other ones. Total cost to this was no  
03:32:48: more time than it would have taken me to  
03:32:49: do the first. Sure, I did spend some of  
03:32:52: my um in this case Claude Max plan  
03:32:54: usage, although keep in mind that we're  
03:32:56: talking cents on the dollar here. I also  
03:32:58: spent a few dollars on Google Places  
03:32:59: API. You know, I would have spent a few  
03:33:01: dollars over here. I spent a few HTTP  
03:33:04: calls over here and then, you know, some  
03:33:05: Ampify tokens over here. Realistically  
03:33:07: though, this allows you to do 5x the  
03:33:10: tests for like just a couple of dollars  
03:33:12: per workflow build. Way cheaper than  
03:33:14: anything um that N8, make.com or Zapier  
03:33:17: would have charged you just for like  
03:33:19: development and testing costs alone. And  
03:33:21: we get to do it through self annealing  
03:33:23: and have a very robust reliable workflow  
03:33:25: to boot. So, how do you actually improve  
03:33:27: these workflows over time? And when I  
03:33:28: say this, I mean practically. Like, how  
03:33:30: do you actually cut through the noise  
03:33:31: and then do this thing in a way that is  
03:33:32: consistent and reliable? Well, you just  
03:33:34: ask. I actually literally just say, can  
03:33:37: you make this faster? Can you make this  
03:33:39: cheaper? Over and over and over and over  
03:33:40: again, like 30 times. I say, list 10  
03:33:42: approaches to make this thing cheaper.  
03:33:44: List 20 approaches to make this thing  
03:33:45: faster. Most of the approaches will not  
03:33:47: work, but I will use my human judgment.  
03:33:49: And then after it opens up and gives me  
03:33:51: 20 possible opportunities, I then just  
03:33:53: pick one that I think makes the most  
03:33:55: sense. And then we proceed with that.  
03:33:56: Then I just repeat the process over and  
03:33:58: over and over again until my workflow is  
03:34:00: now significantly faster and  
03:34:02: significantly more optimized. That said,  
03:34:03: cuz I think a lot of people have  
03:34:04: probably stumbled on this, um, I do have  
03:34:06: a rule and my rule is the order of  
03:34:08: magnitude rule. I don't actually do this  
03:34:11: anymore unless I can get at least a 10  
03:34:14: times improvement in a key metric. For  
03:34:16: instance, time, cost, or accuracy  
03:34:18: because a workflow running in 3 minutes  
03:34:20: versus 2 minutes, well, technically it's  
03:34:22: a 33% improvement or whatever, it's not  
03:34:24: actually meaningfully better for me. and  
03:34:26: the amount of time that I take to  
03:34:28: implement it multiplied by the  
03:34:29: introduced error risk by doing what is  
03:34:32: typically an approach that trades off  
03:34:34: time, money or accuracy for speed  
03:34:38: against each other means that I'm  
03:34:41: usually losing. If you think about it,  
03:34:43: it's basically what's the metric we  
03:34:44: want? We want like time, right? And so  
03:34:46: the degree to which the time gets better  
03:34:48: is sort of related to the degree to  
03:34:51: which maybe the cost and the accuracy go  
03:34:54: down. And so the amount of time that I  
03:34:57: spend on this I in addition to like the  
03:34:59: introduced error rate and stuff like  
03:35:01: this means that this only really makes  
03:35:02: sense to do if there's a very clear path  
03:35:04: to making your flow 10 times better.  
03:35:06: What's an example of this? Um I used to  
03:35:08: scrape tons of leads using a serial  
03:35:11: approach and I found that it took  
03:35:12: forever. My serial approach was  
03:35:14: something like you know 20 minutes for  
03:35:16: 2k leads. If you do the math on that  
03:35:19: that's like I don't know 100 leads a  
03:35:21: minute or so. Um, I came through and I  
03:35:23: tried optimizing the hell out of the  
03:35:24: serial approach with like every way way,  
03:35:26: shape, and form that I could. I tried  
03:35:28: like changing the compute that I was  
03:35:29: using. I tried changing like the Ampify  
03:35:30: actors I was using. I tried changing  
03:35:32: like the API requests that I was making  
03:35:33: to Google Sheets and stuff like that.  
03:35:35: And I was only really able to get this  
03:35:36: down to maybe 15 minutes. That is like a  
03:35:39: 25% improvement in time of course, but a  
03:35:41: lot of the time this is even my  
03:35:42: bottleneck. Like it doesn't actually  
03:35:42: matter if it takes 15 minutes or 20  
03:35:44: minutes because I'm not utilizing the  
03:35:45: leads 100%. Anyway, what I ended up  
03:35:47: finding was I ended up finding an  
03:35:48: approach that batch parallelized them.  
03:35:50: So sent instead of um 2k leads for 20  
03:35:53: minutes, it basically sent 100 leads at  
03:35:55: a time 20 times and then it finished in  
03:35:58: approximately 1 minute. Um this for  
03:36:01: example is a 20 times improvement. This  
03:36:04: is something that I'd actually do. Um  
03:36:05: that actually worked. But this whole  
03:36:07: like I don't know this whole like uh  
03:36:09: detour or rabbit hole thing was just a  
03:36:11: total waste of my time because this  
03:36:12: turned the flow into an unreliable mess.  
03:36:14: So my rule is I basically just like I  
03:36:16: don't make small optimizations anymore  
03:36:18: because they reduce accuracy and  
03:36:19: reliability for marginal gains. I would  
03:36:21: only do this on something that I  
03:36:22: actually see there being an order of  
03:36:24: magnitude possible improvement. What are  
03:36:25: some examples? It's like moving from  
03:36:27: software encoding to hardware encoding.  
03:36:29: You don't need to know what that means.  
03:36:30: Just make sure that when you ask the  
03:36:31: model and you see words like that, it's  
03:36:33: like okay, I should probably use the  
03:36:34: hardware encoding. Parallelizing or  
03:36:36: using what's called like multiple  
03:36:37: threads or using multiple service  
03:36:38: workers simultaneously. These are things  
03:36:40: that usually do provide like an order of  
03:36:42: magnitude jump. Um, sometimes you can  
03:36:44: like fundamentally change the order of  
03:36:46: operations in a workflow. Uh, but in  
03:36:48: general, unless the model expects that  
03:36:49: this is going to provide at least a 10x  
03:36:51: boost, I don't really recommend doing  
03:36:53: it. What is really cool is that every  
03:36:54: workflow that you build does become a  
03:36:56: permanent asset in your library. And I  
03:36:58: mean this both in the way of directives  
03:37:00: and execution scripts as well. Your  
03:37:02: library ends up infinitely reusable. If  
03:37:04: you think about it, you could open up  
03:37:06: any workspace in any IDE or agent model.  
03:37:09: You could also copy directives and  
03:37:10: execution scripts over to anybody else's  
03:37:12: workspace like your friends or your  
03:37:13: colleagues. You could put it on GitHub  
03:37:15: with like GitHub code spaces, something  
03:37:17: I'm going to talk about soon. You could  
03:37:18: reuse automations the exact same way  
03:37:20: that you do them in, you know, drag and  
03:37:22: drop no code tools like naden, make.com,  
03:37:24: or gum loop, but you just do that with  
03:37:26: natural language instead. Your  
03:37:28: blueprints, if it makes sense now, is  
03:37:30: just like a bunch of words on a page,  
03:37:31: which are much, much more portable. And  
03:37:33: over time, your ID will become basically  
03:37:35: a giant treasure chest that you can  
03:37:37: deploy anytime you want, anywhere you  
03:37:39: want. So, for instance, what my library  
03:37:41: can do right now is it can do automated  
03:37:43: lead scraping, automated email  
03:37:44: enrichment, automated personal replies  
03:37:46: on campaigns that I run because we're  
03:37:47: predominantly like a cold email agency.  
03:37:49: I can initiate high quality voice agent  
03:37:51: calls. I literally just say, "Hey, call  
03:37:52: this person. Hey, I want you to call  
03:37:53: people on this list. Hey, I want you to  
03:37:55: split to like 20 20 uh threads and then  
03:37:57: call 20 people." I could do automated  
03:37:59: proposal generation. I could do slide  
03:38:01: deck creation that actually matches my  
03:38:02: tone of voice and it looks pretty good.  
03:38:04: Um, and all of it is customized to how I  
03:38:06: communicate. It is not generic AI slop.  
03:38:08: Um, so it's pretty cool. Obviously, I  
03:38:10: didn't build all this stuff overnight.  
03:38:11: It took me a fair amount of time, few  
03:38:12: days, well, a few weeks now to really uh  
03:38:15: put the finishing touches on all these.  
03:38:16: But yeah, I mean, at the end of the day,  
03:38:18: this thing can basically be your  
03:38:19: terminal for life. A real example from  
03:38:21: my actual day-to-day was automating my  
03:38:23: school posts. So, I kept forgetting to  
03:38:24: post a weekly community call thread. I  
03:38:26: did it three weeks in a row, which is  
03:38:27: really embarrassing, especially because  
03:38:28: I uh like to make it clear that if I  
03:38:30: don't do like the foundational  
03:38:32: fundamental things that I promise people  
03:38:34: I will do, then why why the hell am I  
03:38:36: entitled to their money? So, I gave a  
03:38:37: bunch of people refunds. Um, I asked my  
03:38:39: agent, Claude Opus 4.5, at the time if  
03:38:42: automating this was straightforward. I  
03:38:43: had never even really thought of this  
03:38:44: before, but I was basically just like,  
03:38:45: "Hey, I keep forgetting about this  
03:38:47: thing. Man, I really suck. Any ideas?"  
03:38:48: And then it's just like, "Oh, yeah, we  
03:38:50: could totally automate that." So, it  
03:38:51: went and found a reex uh pre-existing  
03:38:53: school system that I had built um which  
03:38:55: just handled like the authentication and  
03:38:56: the logging in. Then it built a simple  
03:38:58: scraping spec and it figured it out in  
03:38:59: like 3 minutes flat and I automated my  
03:39:02: school post in 3 minutes flat using a  
03:39:04: simple schedule timer which I'll talk  
03:39:05: about later. So now it just happens for  
03:39:07: me which is incredible and it's super  
03:39:08: easy and it's super straightforward. Um  
03:39:10: you can solve so many tiny little  
03:39:12: problems in your life using tools like  
03:39:14: this. So once you've built like  
03:39:16: individual workflows that work really  
03:39:17: well, then you eventually transition to  
03:39:19: what I call metadirectives. So at the  
03:39:21: end of this, what you will essentially  
03:39:23: have is you will essentially have okay  
03:39:26: giant families of workflows  
03:39:29: that do various things. For instance, I  
03:39:32: will have like a marketing workflow  
03:39:34: umbrella. And this is a family of  
03:39:36: workflows that does things like, you  
03:39:38: know, scrape leads, create ad copy, you  
03:39:42: know, do uh voicemail drops, I don't  
03:39:44: know, whatever the heck, right? And so  
03:39:46: what this umbrella workflow, this  
03:39:48: metadirective does is it just ties them  
03:39:50: together. So, for instance, if you have  
03:39:51: a bunch of separate workflows for, I  
03:39:53: don't know, a welcome email, the setup  
03:39:54: of a workspace, and the copyrighting of  
03:39:55: an email, this is sort of like an  
03:39:57: onboarding thing, right? So, you could  
03:39:58: just tile all these together with a new  
03:40:00: client workflow that just does all them  
03:40:01: in sequence. I recommend storing the  
03:40:03: directives separately in order to make  
03:40:04: this happen. I don't recommend just like  
03:40:06: having a giant new client workflow  
03:40:08: that's like four quadrillion lines  
03:40:10: because it's much easier and more  
03:40:11: maintainable for the model to load only  
03:40:12: what it needs in context at any one  
03:40:14: particular time. But this becomes really  
03:40:15: powerful because they just chain all of  
03:40:17: the existing capabilities together.  
03:40:18: Instead of you having to go like 1 2 3,  
03:40:21: you know, you have like four or five  
03:40:22: workflows. What you do is you just turn  
03:40:24: that into one workflow and then every  
03:40:25: time you want all of these done in  
03:40:26: sequence, you just call the big  
03:40:28: workflow, not individual workflows. It  
03:40:30: also means that when you prompt the  
03:40:32: model and use it as like an assistant or  
03:40:33: whatever, you could just say, "Hey, I  
03:40:34: want you to do X, Y, and Z onboarding  
03:40:36: workflow." And then you can just step  
03:40:37: away, have a freaking nice cup of tea or  
03:40:39: something like that and come back and  
03:40:40: everything's okay. You don't actually  
03:40:41: have to get like interrupted all the  
03:40:42: time. And yeah, when you combine that  
03:40:44: with the infinite reusability of these  
03:40:46: workflows, this becomes really, really  
03:40:47: powerful because then you can just send  
03:40:49: your new client workflow to the other  
03:40:51: three account managers on your team and  
03:40:52: then they can just run it every time  
03:40:53: they get a new client. or as I'm going  
03:40:55: to show you later, maybe you could  
03:40:56: attach that to a schedule trigger or  
03:40:57: some sort of web hook so that it just  
03:40:59: runs autonomously without you. Hopefully  
03:41:01: that makes sense. Now, we're starting  
03:41:02: one of my favorite topics in directive  
03:41:04: orchestration execution and just agentic  
03:41:05: workflows in general, and that's this  
03:41:07: idea of self annealing. First, let's  
03:41:09: talk about annealing in a general sense.  
03:41:11: Annealing is the process of heating a  
03:41:13: piece of metal and then slowly cooling  
03:41:15: it down. Basically what happens is  
03:41:17: previously the molecules in the metal  
03:41:19: are kind of all over the place. But what  
03:41:21: happens when you heat up a metal is they  
03:41:23: end up actually moving to like their  
03:41:25: highest or rather lowest energy state  
03:41:27: and they end up looking kind of like a  
03:41:29: crystal lattice which is really badass.  
03:41:31: And then what we do is we cool it down  
03:41:33: very quickly which then hardens this and  
03:41:35: sets it into you know some really strong  
03:41:38: robust piece of metal. Blacksmiths and  
03:41:40: so on have been doing this for many many  
03:41:41: generations. It removes a bunch of these  
03:41:43: internal weird misconfigurations of the  
03:41:45: atoms and it creates a really strong  
03:41:47: more stable structure. So people do this  
03:41:49: with swords and you know uh uh devices  
03:41:52: and and pieces of metals all the time in  
03:41:53: real life. It's cool as hell. And today  
03:41:55: I wanted to talk about a similar concept  
03:41:57: in agentic workflows. So what if we had  
03:41:59: the ability to stress test our workflows  
03:42:02: as well to make them significantly more  
03:42:04: resilient? Turns out we do. When we  
03:42:07: build instruction sets, prompts or  
03:42:09: directives for our agents. I want you to  
03:42:11: think of them as looking something like  
03:42:13: what we see on the left hand side here.  
03:42:15: In short, these are pretty rough. We  
03:42:17: have some idea of how we want the  
03:42:19: workflow to develop. Maybe we want it to  
03:42:22: start here and then go over here and go  
03:42:25: over here, here, and then here. But we  
03:42:28: don't really have uh uh you know a  
03:42:29: strong mechanism to do it. All we really  
03:42:31: have so far is just an outline. You  
03:42:33: know, when we when you say step one, do  
03:42:35: X, step two, do Y, and step three, do Z,  
03:42:38: all this really is is just a couple of  
03:42:40: bullet points on a piece of paper. And  
03:42:41: even if you have an agent like produce a  
03:42:42: workflow for you uh in a directive form,  
03:42:45: it's not super tight. What self-  
03:42:47: annealing does is basically every single  
03:42:49: time we run into some error or issue or  
03:42:52: opportunity for improvement, the system  
03:42:56: reinforces that flow. And so if this on  
03:42:59: the left hand side is what we kind of do  
03:43:00: on the first day, this on the right hand  
03:43:02: side is after maybe 60 days of you using  
03:43:04: an agentic workflow. Instead of it just  
03:43:07: being this small little piss ant line on  
03:43:09: the left, we have a super strong battle  
03:43:12: hardened protocol. You know, every one  
03:43:14: of these little shields is some form of  
03:43:16: retry logic. You know, uh it's so much  
03:43:18: beefier. There's like validation steps  
03:43:20: that that go into place. Maybe you have  
03:43:22: human in the loop at specific steps you  
03:43:24: didn't realize that you needed before  
03:43:25: and so on and so forth. And so you know  
03:43:27: if I'm somebody designing a workflow  
03:43:29: despite the fact that I start over here  
03:43:31: on the left hand side at the end of the  
03:43:32: self- annealing process my workflow  
03:43:34: actually becomes super super robust and  
03:43:35: very resilient as well. So that concept  
03:43:37: is self- annealing instead of brittle  
03:43:40: systems that break every time that you  
03:43:42: error out like with you know nadn or  
03:43:46: make or whatever. When you build these  
03:43:48: systems they just strengthen over time.  
03:43:51: The secret ingredient is adding a level  
03:43:54: of thoughtful error handling to your  
03:43:56: system prompt. And the whole idea is  
03:43:59: when you do this, it will learn and it  
03:44:00: will adapt. Problems essentially stop  
03:44:03: being like problems in the error sense  
03:44:05: and they start being opportunities for  
03:44:06: you and the model to build edge cases um  
03:44:09: error handling and sort of unexpected uh  
03:44:12: uh steps in that you just didn't really  
03:44:13: understand the first time because a lot  
03:44:15: of the time the only way to know is just  
03:44:17: by doing a bunch. So when you enter the  
03:44:19: self annealing loop essentially what  
03:44:21: happens is there will be some sort of  
03:44:23: error. Immediately after you will  
03:44:25: diagnose where the error is coming from  
03:44:28: then you will attempt some sort of fix.  
03:44:31: After the fix you will then update. So  
03:44:33: you'll actually update the workflow the  
03:44:36: execution script itself and then you'll  
03:44:37: just rotate over and over and over and  
03:44:39: over and over again. And then finally  
03:44:40: eventually this stops erroring out right  
03:44:42: and then it becomes successful. And when  
03:44:45: it becomes successful, all we do is we  
03:44:47: just do some sort of documentation  
03:44:49: upgrade. And so we let the directive  
03:44:51: know, hey, you know, this is a common  
03:44:53: issue that previously used to happen a  
03:44:54: lot. We've since reinforced against it,  
03:44:56: and it's a lot better. And then the next  
03:44:57: time the loop uh fixes, and let's say  
03:44:59: this eventually goes into some sort of  
03:45:01: error. Well, guess what happens? We just  
03:45:04: run the same thing. We go through an  
03:45:06: error, then we diagnose, then we fix, or  
03:45:08: attempt to fix, I should say, and then  
03:45:10: we update. And then we just loop over  
03:45:12: and over and over again until we can no  
03:45:14: longer loop. Okay, so this is really  
03:45:16: like that four-step process. The agent  
03:45:18: will continue until the operation  
03:45:19: succeeds or it hits like some super  
03:45:21: unfixable wall, just something that like  
03:45:22: actually requires a human being even  
03:45:23: when something is unfixable. You'll find  
03:45:25: that an agent often will find a creative  
03:45:27: workound. So like for instance, if one  
03:45:29: of the things that you asked for is like  
03:45:30: you asked for 50 leads or something or  
03:45:32: maybe I always use leads cuz you know  
03:45:34: I'm just super in that business. But  
03:45:36: let's just take a step back here and say  
03:45:38: you are looking for like 50 blog posts  
03:45:40: on a subject, right? And your whole job  
03:45:42: is you want to like take these blog  
03:45:44: posts and then use them to create  
03:45:45: something. Your definition of done is  
03:45:47: you get 50 blog posts from your scraper.  
03:45:49: Well, let's say the scraper only returns  
03:45:51: 40. This loop will start and continue.  
03:45:54: And maybe the reality is there just  
03:45:55: aren't any more blog posts on the  
03:45:57: internet about this. Well, your model  
03:45:58: finds a creative workaround by maybe  
03:46:00: changing one of the filters in how it  
03:46:02: pitched the first thing. and it lets you  
03:46:03: go from 40 to 50 technically  
03:46:06: accomplishing what you were looking for  
03:46:07: despite the fact that it is a  
03:46:08: fundamentally different process. Now  
03:46:10: you're using maybe a different set of  
03:46:11: filters and then although it didn't work  
03:46:13: 100% it worked 80% the model will then  
03:46:15: give you a notification or ping you or  
03:46:17: something to be like hey this mostly  
03:46:18: worked know if this filter is okay too.  
03:46:20: So then you provide some feedback or  
03:46:22: whatever and then it actually cements  
03:46:23: the fact that this filter is okay too  
03:46:24: preventing it from ever happening again.  
03:46:26: And in that way every cycle will leave  
03:46:28: the system a lot more robust and  
03:46:29: reliable than it was before. So, as a  
03:46:31: business owner, somebody that's been  
03:46:32: doing stuff like this for the better  
03:46:33: part of the last decade, I like thinking  
03:46:35: about agents and agentic workflows as  
03:46:37: basically many employees. And in  
03:46:40: business, when you hire a bunch of  
03:46:41: people, you quickly realize that you can  
03:46:43: bin human beings into two camps. You  
03:46:45: could have employee A, who I'm going to  
03:46:47: consider the blocker, and you can have  
03:46:48: employee B, who I'm going to consider  
03:46:50: pretty self-capable. So, in the  
03:46:51: situation of employee A, anytime that  
03:46:53: they have a problem, and I've hired a  
03:46:55: lot of people like this, that problem is  
03:46:57: now your problem. So, hey boss, I tried  
03:47:00: doing XYZ, couldn't make it happen.  
03:47:02: Could you help me with this? Meaning,  
03:47:05: this is the sort of person that cannot  
03:47:06: proceed without your intervention. Every  
03:47:08: time they run into an issue, well, now  
03:47:10: it's your issue as well. All work grinds  
03:47:12: to a halt, not just theirs. This is the  
03:47:14: sort of person that makes the same  
03:47:15: mistakes over and over and over again,  
03:47:16: doesn't seem to learn, and ultimately  
03:47:18: you become the bottleneck for their  
03:47:19: productivity. They almost require you to  
03:47:21: micromanage them in order to succeed.  
03:47:23: I'm sure there's some business owners  
03:47:24: here that are watching this video. This  
03:47:26: happens very often and this is one of  
03:47:27: like the easiest and simple tells that  
03:47:29: you probably shouldn't hire a person  
03:47:30: that you know runs into issues and can't  
03:47:32: actually self-mmitigate them. Employee B  
03:47:34: on the other hand is a star performer.  
03:47:36: They encounter the same problems but  
03:47:37: they have a simple SOP. The SOP is well  
03:47:40: even if I don't know how to solve the  
03:47:42: problem. I'm going to try on my own  
03:47:44: first and so they'll only escalate when  
03:47:46: it's absolutely necessary. They respect  
03:47:48: your time. They document solutions when  
03:47:50: they run into them that your team so  
03:47:52: that your team never ever hits the same  
03:47:53: issue twice. They make a a statement in  
03:47:55: your Slack. Hey guys, ran into XYZ  
03:47:57: problem. Just wanted you all to know  
03:47:58: that you could fix this by doing XYZ  
03:48:00: solution. Sometimes they even run a  
03:48:02: quick session to teach others what they  
03:48:03: learned. Now, if I gave you a choice  
03:48:04: between these two, which one would you  
03:48:06: choose? Obviously, you'd choose employee  
03:48:09: B. And I think most business owners  
03:48:11: would too. Well, self annealing agentic  
03:48:13: workflows behave like employee B. They  
03:48:16: don't behave like employee A. And so,  
03:48:18: we're giving them a level of autonomy  
03:48:20: that I think a lot of people previously  
03:48:21: would have considered insane.  
03:48:24: But I think the definition of insane is  
03:48:25: going to change pretty quickly as these  
03:48:27: models get more and more intelligent.  
03:48:28: How do you actually enable this cool  
03:48:30: process? It really just boils down to a  
03:48:32: small set of instructions and a prompt.  
03:48:34: You just add to your cloud MD, Gemini  
03:48:36: MD, agents MD, whatever a key thing that  
03:48:38: just changes its opinion uh essentially  
03:48:41: like the default mode of problem  
03:48:43: solving. And the default mode of problem  
03:48:44: solving with these programming agents is  
03:48:46: usually, hey, if I can't do something,  
03:48:47: return it to the user and ask them what  
03:48:49: they'd like me to do. which makes sense  
03:48:50: because for the most part this these  
03:48:52: sorts of models are used predominantly  
03:48:53: in like enterprise coding applications  
03:48:55: now where like a small change can  
03:48:56: actually result in a big downstream  
03:48:58: problem but like if we're building  
03:48:59: simple agentic workflows that are  
03:49:00: modular and like unit testable uh and  
03:49:02: then we're just using them in our IDE  
03:49:04: like that doesn't apply to us.  
03:49:08: So all we say is something along the  
03:49:09: lines of hey when you encounter an error  
03:49:11: first diagnose it then fix it then  
03:49:14: update your scripts and directives to  
03:49:15: handle similar errors in the future. Now  
03:49:17: I always add is something like try super  
03:49:19: duper hard before escalating to the  
03:49:21: user. What happens over time is the  
03:49:23: initial workflow will look very  
03:49:25: different on the initial implementation  
03:49:26: than it does you know several weeks  
03:49:28: later. Retry logic in instances where  
03:49:30: one-off failures occur will be added  
03:49:32: automatically. It'll do things like um  
03:49:35: self retry loops. It'll do things like  
03:49:38: um if you guys are in the programming  
03:49:40: space, you'll know there's stuff like  
03:49:41: exponential backoff.  
03:49:44: There's various forms of error handling  
03:49:45: like logging and so on and so forth. And  
03:49:48: because it is hyper optimized to program  
03:49:51: really well and understands these things  
03:49:52: outside of the box, it'll just do them  
03:49:53: for you. Which means edge cases that you  
03:49:55: never anticipated get handled as your  
03:49:56: agent encounters them. Efficiency  
03:49:58: improvements occur organically. You  
03:50:00: know, bulk endpoints, parallelization,  
03:50:02: multiple workers. If there's like a a  
03:50:04: request that you made initially in your  
03:50:05: directive, I want this to occur under 5  
03:50:06: minutes after you run this every single  
03:50:08: time. Just make sure to like see how  
03:50:09: long it took. If it takes more than 5  
03:50:10: minutes, IDate solutions. If you have  
03:50:12: simple little blockers in there or  
03:50:14: decision or router points uh in there,  
03:50:16: agents will naturally do a lot of this  
03:50:17: stuff for you, which is really cool. And  
03:50:18: then obviously you can also just ask,  
03:50:19: "Hey, make this thing better. Make this  
03:50:21: thing better. Make this thing better.  
03:50:22: Make this thing better." In this way,  
03:50:23: your system continuously optimizes  
03:50:25: itself without any form of ongoing  
03:50:27: intervention. Uh which is the coolest  
03:50:29: thing ever in practice. That said, when  
03:50:31: you guys start getting really deep into  
03:50:33: self- analing and you have workflows  
03:50:34: that do a lot of their work themselves,  
03:50:37: safety becomes a much bigger portion of  
03:50:39: the conversation than it ever was  
03:50:40: before. Like with N8N and Make.com  
03:50:42: workflows, the biggest potential issue  
03:50:44: was basically that you just like turned  
03:50:46: it on and you forgot to turn it off and  
03:50:47: then it just continued consuming your  
03:50:49: credits or operations or whatever longer  
03:50:51: than you realistically wanted it to,  
03:50:52: which charges costs and so on and so  
03:50:54: forth. But most APIs, most systems, and  
03:50:57: most automation platforms now have some  
03:50:59: sort of built-in detection for this, or  
03:51:00: at least thresholds that you could set.  
03:51:02: So, it's not that big of a deal. But  
03:51:03: with fully autonomous AI, especially AI  
03:51:05: that were proposing giving total  
03:51:07: bypassed permission access to a system,  
03:51:10: safety becomes much more important. I  
03:51:12: was just reading this thread the other  
03:51:13: day where somebody let Gemini basically  
03:51:15: run autonomously for I think it was like  
03:51:17: 2 days or something like that and you  
03:51:19: know it checked in and it had some cool  
03:51:20: little workflow loop where it did this  
03:51:21: but then when they went back to it they  
03:51:23: realized that they didn't put it in a  
03:51:24: container. They basically gave it full  
03:51:26: system access and then it like deleted  
03:51:27: their whole like C or D drive. Anybody  
03:51:30: that's in the know, you delete your  
03:51:31: whole CR D drive, your computer's  
03:51:32: basically screwed. You know, you have to  
03:51:34: do like a fresh install. So that's on  
03:51:36: your server, right? The thing is you're  
03:51:38: also giving this thing access to the  
03:51:40: internet. And so if you have cookies or  
03:51:41: API keys or whatever, I'm sure you can  
03:51:44: imagine even if there's like a 0.1%  
03:51:46: risk. If you just stack up that 0.1%  
03:51:49: over the course of a very long period of  
03:51:51: time, okay, this is just uh let's say  
03:51:54: you know 99.9 raised to the 1,000  
03:51:57: operations. At the end of this process,  
03:51:59: there is only a 36% chance that the  
03:52:02: model will actually do what you  
03:52:03: initially intended it to do. Despite the  
03:52:05: fact that on an individual basis, every  
03:52:07: step was 99.9% um secure and logical.  
03:52:10: The more steps you have, the basically  
03:52:12: the larger those error bars become like  
03:52:14: I've drawn a few times now. So, what  
03:52:15: this means is we really do have to add  
03:52:17: at least some sort of uh uh guard rail  
03:52:20: towards the model so that it doesn't  
03:52:21: screw things around completely. Now,  
03:52:23: there are a few simple ones that I do.  
03:52:24: My processes are never a thousand steps,  
03:52:26: right? I mean, I might be dealing with a  
03:52:27: five or 10step process. So, I typically  
03:52:29: don't have to go much further than this,  
03:52:30: but if you want really autonomous  
03:52:32: longunning agents, um you need to  
03:52:33: develop what are called harnesses for  
03:52:34: them, which I cover later. But  
03:52:36: basically, here are four things that I  
03:52:37: would always do. I would always ask the  
03:52:39: model to confirm beyond making API calls  
03:52:41: above a cost threshold. So, a lot of  
03:52:43: APIs have the ability to check usage.  
03:52:45: So, I'd actually add like a little step  
03:52:46: in there that says, "Hey, make sure to  
03:52:47: check the usage. If you've spent more  
03:52:49: than, you know, $5 in the last like few  
03:52:51: minutes, then you should not continue  
03:52:53: doing this. You should let me know, send  
03:52:54: me a notification, whatever. Hey, never  
03:52:57: modify credentials or API keys unless I  
03:52:59: explicitly tell you to." That's valuable  
03:53:01: because a lot of the time it'll do  
03:53:02: things like reformat your API key.  
03:53:04: Sometimes it'll delete API keys that it  
03:53:06: thinks it doesn't need anymore.  
03:53:07: Sometimes, you know, that'll be a big  
03:53:08: pain in your ass because you have to go  
03:53:10: back to the platform then reinstitute an  
03:53:11: API key. Never remove secrets out of ENV  
03:53:15: files or hardcode them into the  
03:53:16: codebase. Models are really good at this  
03:53:17: already, but I always just like having  
03:53:18: this explicit because if I try and share  
03:53:20: something with somebody at any point in  
03:53:21: time and it has like my enthropic API  
03:53:23: key or whatever, then these guys now own  
03:53:25: my ass. And finally, although this does  
03:53:27: eventually run into a limit, I have the  
03:53:28: model log all self modifications as a  
03:53:31: change log at the bottom of the  
03:53:32: directive. What this does is it  
03:53:33: basically allows me to take a look at  
03:53:34: any point in time be like, "Okay, so  
03:53:36: like what was the sequence of of events?  
03:53:37: What was the order of operations?"  
03:53:39: essentially. Um, I do this in like  
03:53:40: GitHub format. So, it's sort of like a  
03:53:42: commit if you guys know what that means.  
03:53:43: And it's a really simple just like one  
03:53:45: paragraph. Uh, well, a lot of the time  
03:53:47: it's just like a one sentence  
03:53:48: explanation of the changes that we made,  
03:53:50: how the changes worked and whatever. And  
03:53:52: the reason why this is valuable is  
03:53:53: because like if you're not using version  
03:53:54: control like a lot of people will not be  
03:53:56: using uh and I know that for a fact at  
03:53:58: least you have like a change log that  
03:53:59: the model can use to go through and see  
03:54:01: hm before this I was doing X and that  
03:54:03: was working okay. Then I tried doing Y  
03:54:04: and Y is working not so good. So let's  
03:54:06: move back to X. You should also just  
03:54:08: accept that some rules will occasionally  
03:54:10: be broken. That's just how these things  
03:54:11: are. We know that agents are  
03:54:13: probabilistic at this point. 100%  
03:54:15: compliance and everything is just not  
03:54:16: realistic and it's not achievable. So  
03:54:18: despite our best efforts, there will  
03:54:19: always be some sort of edge case  
03:54:22: failure. Although it is getting a lot  
03:54:24: better with time, obviously this is just  
03:54:26: a trade-off that we have to accept  
03:54:27: anytime we're using AI. I mean, AI  
03:54:29: multiplies our leverage by thousands  
03:54:31: upon thousands upon thousands of times,  
03:54:32: right? But in doing so, it also  
03:54:35: multiplies um accuracy or or reliability  
03:54:37: issues as well. Again, it's one of those  
03:54:40: like even if our human workflows are  
03:54:42: 99.9% accurate, obviously if you run  
03:54:44: them enough times, let's say a thousand  
03:54:46: times, these errors compound and then  
03:54:48: you end up with a total process that's  
03:54:49: only maybe 36% successful.  
03:54:51: [gasps and sighs] Well, a human being  
03:54:53: can typically spot that earlier. But  
03:54:54: also, a human being typically just  
03:54:56: doesn't do a thousand operations in a  
03:54:57: row, right? There'll usually be some  
03:54:59: sort of check mark or guardrail. With  
03:55:01: agents, you could do a thousand  
03:55:02: operations like this. So obviously  
03:55:03: despite the fact that like our accuracy  
03:55:05: levels are still really high because  
03:55:07: we're giving them so much autonomy and  
03:55:08: because at the end of the day they do  
03:55:10: lack some context that human beings have  
03:55:11: and you know a lot of people would argue  
03:55:13: they're not as intelligent as like the  
03:55:14: most intelligent human being. This thing  
03:55:15: is just going to occur and there's just  
03:55:17: nothing you can do about it. So I plan  
03:55:19: for graceful recovery not perfect  
03:55:21: prevention and I'd recommend you do too.  
03:55:23: Cool. Let's chat about using these  
03:55:24: workflows. And I just want to make this  
03:55:26: clear that this program is both about  
03:55:29: building workflows. Then it's also using  
03:55:31: said workflows. And the two are not the  
03:55:34: same. Building a workflow versus using a  
03:55:36: workflow are two very different things.  
03:55:38: When I build a workflow, I am having my  
03:55:40: agent essentially be a programmer for  
03:55:42: me. When I use my workflows, that's sort  
03:55:44: of DO, right? The directive  
03:55:46: orchestration execution idea. My agent  
03:55:48: is just executing a sequence of steps  
03:55:49: that a previous iteration of an agent  
03:55:51: built. So these agentic workflows are  
03:55:53: mostly about the using side of things,  
03:55:54: right? like building them while is  
03:55:56: important and stuff like that, it's just  
03:55:57: a very small part of actually living in  
03:55:59: your ID and getting things done. And to  
03:56:01: that point, I have an important thing to  
03:56:02: say. The interface to everything is now  
03:56:06: just a text box. So my actual day-to-day  
03:56:09: work occurs almost entirely now through  
03:56:11: a single text box. It occurs through,  
03:56:14: you know, anti-gravity or Visual Studio  
03:56:15: Code. And I just have the agent do  
03:56:17: everything that I have created  
03:56:19: painstakingly over the course of the  
03:56:20: last few weeks using the tools that I've  
03:56:22: I've set up. So, I'll have it do things  
03:56:24: like generate, you know, my YouTube  
03:56:25: thumbnails. I'll have it do things like  
03:56:27: uh generate scripts and stuff like that  
03:56:28: that I could send to people. I have it  
03:56:30: do things like generate pitch decks so  
03:56:31: that I could send to people that are  
03:56:32: interested in working with me, generate  
03:56:34: proposals. I do things like analyze my  
03:56:36: transcripts and stuff like that. But I  
03:56:37: don't do it in individual software  
03:56:39: applications, okay? I don't do it in  
03:56:41: Fireflies and Google Drive and Panda Doe  
03:56:45: and, you know, Quiller and all these  
03:56:47: other platforms. I literally just do it  
03:56:49: all through a single text interface. And  
03:56:51: this is just the way that high leverage  
03:56:53: work is now going to be done, at least  
03:56:55: until we come up with a better  
03:56:56: alternative, which may come in some  
03:56:58: time. But I wouldn't hold out on it. For  
03:57:00: a lot of people, a single text box feels  
03:57:02: like a downgrade. Cuz if you think about  
03:57:04: it, we've spent decades learning  
03:57:06: software through visual interfaces and  
03:57:08: menus. And GUIs, graphical user  
03:57:12: interfaces, are basically the current  
03:57:14: standard. If you contrast that to typing  
03:57:16: and stuff like that, a lot of people  
03:57:18: also consider it really slow and tough  
03:57:20: compared to, you know, clicking buttons  
03:57:21: and whatnot that they're used to, right?  
03:57:23: Sometimes people type at 50, 60, 70  
03:57:25: words per minute. I have some family  
03:57:26: members that can't type it more than 20  
03:57:28: words per minute. Obviously, that is  
03:57:29: very slow relative to dragging stuff  
03:57:31: around and clicking buttons and stuff  
03:57:32: like that. So, there is no obvious right  
03:57:34: way to do this. It's very open-ended and  
03:57:36: unfamiliar, and I'm sure eventually  
03:57:38: we'll converge on like a really cool  
03:57:40: visual thing that combines the best of  
03:57:41: both worlds. But there are ways to make  
03:57:44: doing a lot more natural and efficient,  
03:57:45: which I want to talk about. The first is  
03:57:47: just to switch to using voice  
03:57:48: transcription tools. In case you guys  
03:57:50: didn't know, you can now just say  
03:57:51: whatever you want to your computer, and  
03:57:52: there's like a 99.9% chance that it will  
03:57:54: understand that and be able to turn that  
03:57:56: into text. The reason why this is  
03:57:58: valuable is because the average typing  
03:57:59: speed is 50 to 70 words per minute,  
03:58:00: which is really slow bandwidth. The  
03:58:02: average speaking speed is 150 to 200  
03:58:04: words a minute, which is three to four  
03:58:06: times faster. You guys have been  
03:58:07: listening to me talk at between 150 to  
03:58:09: 200 words a minute on average. Sometimes  
03:58:11: I'm a little bit slower, maybe around  
03:58:13: like 130. Other times I'm a little bit  
03:58:15: faster, maybe around 220 or so. But in  
03:58:17: general, I'm speaking maybe three times  
03:58:20: faster than most human beings type,  
03:58:21: which is very, very important. Nowadays,  
03:58:23: models are pretty smart. So, you don't  
03:58:25: even need to really organize your  
03:58:26: thoughts in a hyperspecific way. Like  
03:58:27: back when I was using GPT3, okay, back  
03:58:29: in the uh the good old days, you had to  
03:58:31: be extraordinarily precise and concise  
03:58:33: with your prompts because even 10  
03:58:34: additional tokens could really really  
03:58:36: screw up the intelligence and the  
03:58:37: steerability of the model. Nowadays  
03:58:39: though, I could have prompts that are  
03:58:41: thousandword text dumps where I just I'm  
03:58:43: in my car driving somewhere. I click the  
03:58:44: voice transcribe tool and then I just  
03:58:46: talk. And it does a really good job at  
03:58:47: turning that into something useful. The  
03:58:48: highest bandwidth way of communicating  
03:58:50: with computers, at least right now, is  
03:58:51: the following. Nobody really talks about  
03:58:53: this, but you transcribe your text as  
03:58:55: input, which gets you to route 200 words  
03:58:57: a minute. So my input bandwidth is now  
03:58:59: 200 WPM. And then you don't like have it  
03:59:02: say stuff to you like you do with like I  
03:59:04: don't know the chatbt voice call or  
03:59:06: whatever. Instead, you just read as the  
03:59:08: output because most people can actually  
03:59:09: read between 300 to 500 words per minute  
03:59:11: if you skim. And most people will skim  
03:59:13: in some way, shape, or form. Some people  
03:59:14: can go much faster to like a thousand.  
03:59:16: And in that way, you have like 200 word  
03:59:18: per minute input, 1,000 word per minute  
03:59:21: output, you know, in terms of skimming  
03:59:22: to relevant materials. Um, the old way  
03:59:25: of doing this is like 50 to 70. And then  
03:59:27: if you're doing voice, it'll be, you  
03:59:29: know, like 200. So, what we're doing  
03:59:30: here is we're basically quadrupling our  
03:59:32: input um at at at both sides of this. So  
03:59:34: this is like a 3 to 5x and this is like  
03:59:36: a 5x at least. So maybe like a quadruple  
03:59:38: I would say. Um I would recommend just  
03:59:40: doing that moving forward. It's way  
03:59:41: simpler. The only situation which I  
03:59:43: actually type stuff now is if I like  
03:59:44: absolutely have to because there is some  
03:59:46: hypersp specific file that I need to  
03:59:48: reference on my computer somewhere. And  
03:59:49: even then I'll usually just like copy  
03:59:50: the name and paste it manually. From  
03:59:52: here on out when I say the word prompt  
03:59:53: assume I'm just generating all this with  
03:59:55: my voice. And then you guys have also  
03:59:56: seen me do this on multiple demos. But  
03:59:58: um I will proceed to assume that you  
03:59:59: guys know that. How do you actually use  
04:00:01: workflows? Well, it's really simple.  
04:00:02: Hopefully you guys have already seen. We  
04:00:04: just ask for it. There's no need to  
04:00:05: memorize the exact name of the  
04:00:07: directive. Agent typically knows the  
04:00:09: directives exist because we've included  
04:00:10: that in our system prompt and it'll scan  
04:00:12: for matches automatically. You do of  
04:00:14: course need to provide some data um  
04:00:16: specifically that your directives input  
04:00:17: schema requires. So if your directive  
04:00:20: says, hey, you know, I want you to  
04:00:21: include uh I don't know the name of a  
04:00:23: person or something like this and we  
04:00:25: need the name of the person in order to  
04:00:27: generate some form of proposal or  
04:00:28: something. And if you say, "Hey, just do  
04:00:30: the thing." It'll look at it and be  
04:00:31: like, "Hey, you're currently lacking  
04:00:32: this input." So, like, "What's the name  
04:00:33: of the person you wanted? Let me know  
04:00:34: and I'll I'll create that for you."  
04:00:37: Really, this is just like ordering food,  
04:00:38: right? Kitchen needs to know what dish  
04:00:39: any modifications or whatever. You can't  
04:00:41: just say, "Hey, get me food." You need  
04:00:42: to be like, "Hey, you know, can you can  
04:00:44: I have like the hamburger with a side of  
04:00:45: fries, please?" Like, there's a level of  
04:00:47: specificity here. You don't have to go  
04:00:48: super deep, but you also don't need to  
04:00:50: overthink it. I'm pretty specific with  
04:00:52: my requests that I know have specific  
04:00:54: input methods. So, like in the case of  
04:00:57: getting me some leads, I can absolutely  
04:00:58: just say, "Hey, get me some leads today,  
04:01:00: obviously, it's going to ask me a bunch  
04:01:01: of questions and then I'm going to have  
04:01:02: to like feed those questions in and then  
04:01:04: I can kind of mess about with my  
04:01:05: directive, right?" So, I much rather  
04:01:06: say, "Hey, scrape 200 HVAC companies in  
04:01:08: Texas, then verify the emails,  
04:01:10: personalize them, and then give me the  
04:01:11: Google sheet." This takes, you know, 2  
04:01:12: seconds longer than the first version,  
04:01:14: but because I'm at the helm of the ship,  
04:01:16: I'm able to steer it into a much uh more  
04:01:18: straight line direction to what it is  
04:01:20: that I want. The more steps you put in  
04:01:22: an AI's hands, the more chances for  
04:01:24: errors that it has. Remember that error  
04:01:25: rates multiply. If I had, you know, a  
04:01:27: 90% chance doing the first thing  
04:01:29: correctly and then a 90% chance doing  
04:01:30: the second thing correctly, um, you  
04:01:32: know, I would have a, I don't know, I  
04:01:34: guess a 081% total chance. Ideally,  
04:01:36: we're dealing with higher rates, but let  
04:01:37: me just show you how that transforms,  
04:01:39: right? If I give it everything I need  
04:01:40: immediately, I now have this is a 90%.  
04:01:44: Let's say, you know, in the first one, I  
04:01:46: say get me leads. Well, what happens? It  
04:01:50: interprets my request as saying, okay,  
04:01:51: we need to get some leads, so let's go  
04:01:52: to the directive or whatever. and then  
04:01:54: it says we don't have any leads. Hey  
04:01:55: Nick, can you send me some leads? And  
04:01:57: then I need to provide it leads and then  
04:01:58: it goes through another process and then  
04:02:00: gives me a total uh success rate of  
04:02:01: let's say 81%. Here if I just say you  
04:02:04: know hey scrape me 200 HVAC companies in  
04:02:06: Texas, verify their emails and so on and  
04:02:08: so forth. [gasps] It's only been one  
04:02:10: step. So I've significantly reduced  
04:02:12: what's called the compound probability  
04:02:13: of the error. When you're specific, you  
04:02:15: also reduce the back and forth. It  
04:02:17: lowers your overall failure risk and  
04:02:18: then it's just faster. So I just do it  
04:02:19: faster that way. If you're not sure  
04:02:21: what's available, you could just ask  
04:02:22: like, "Hey, what workflows do I have?"  
04:02:24: Um, you know, eventually after you  
04:02:25: design so many directives, it does start  
04:02:26: being a little bit overwhelming for both  
04:02:28: you and the model. And obviously, there  
04:02:29: are some strategies that you could use  
04:02:31: to help accommodate that, like sub  
04:02:32: agents, which we talk about later. But  
04:02:34: for now, just know that, you know, if  
04:02:35: you don't know what's available,  
04:02:36: absolutely just ask your model. You  
04:02:37: could ask the model to do things like  
04:02:39: refactor your directive base. Hey, are  
04:02:40: any directives that look really similar?  
04:02:41: Are there any executions that look  
04:02:42: really similar? I want you to run a  
04:02:43: comprehensive refactor and everything to  
04:02:45: like group them in ways that make sense.  
04:02:47: You obviously have a lot of freedom to  
04:02:48: do this in your own. Now, for really  
04:02:49: complex workflows, I'll usually just  
04:02:50: paste in the context rather than typing  
04:02:52: it all manually. Like um you know,  
04:02:54: rather than asking the model to do some  
04:02:56: sort of like Fireflies API request for  
04:02:57: me, I'll just like paste my call  
04:02:59: transcript directly in. Takes  
04:03:00: approximately the same amount of time.  
04:03:02: It's just this one is like exact and  
04:03:03: there's no room for error. Another  
04:03:05: really common request that I typically  
04:03:06: will do is I will like go to a website  
04:03:09: and I'll just like command all copy  
04:03:11: everything and then paste it in the  
04:03:12: model and be like, hey, you know, build  
04:03:13: me a proposal with this website or  
04:03:15: something. Obviously, I could have it,  
04:03:16: hey, HTTP request this link and then it  
04:03:18: goes through that. But, I mean, it's the  
04:03:19: same thing, right? It takes me the same  
04:03:20: amount of time to do that versus this.  
04:03:22: So, from the model's perspective,  
04:03:23: doesn't matter. Everything gets inserted  
04:03:24: in context the same way. Can be a big  
04:03:26: time saver since HTTP calls and then API  
04:03:28: requests and then accessing databases  
04:03:30: and stuff like that can take some time  
04:03:31: to set up. So, if you're using this as a  
04:03:34: user, right, you are executing your  
04:03:36: workflows using this orchestrator, you  
04:03:38: can absolutely just like co-create with  
04:03:40: it. You can go on websites yourself,  
04:03:41: copy paste stuff in, it's no big deal.  
04:03:43: The next thing I wanted to do is talk a  
04:03:45: little bit about how to peruse API  
04:03:47: documentation with Agentic workflows.  
04:03:49: So, as you guys remember in a previous  
04:03:51: demo, I built a workflow that took  
04:03:53: LinkedIn Sales Navigator URLs, fed them  
04:03:56: into the service vein, uh, you know, did  
04:03:58: a couple of other things, and then ended  
04:03:59: up giving me a big list of leads in a  
04:04:01: Google sheet. So, how exactly do we do  
04:04:03: this sort of thing in like a reasonable  
04:04:04: way? Well, obviously we could just, you  
04:04:06: know, tell the model, hey, I want you to  
04:04:08: build XYZ with Fain. But what you'll  
04:04:10: quickly realize is models will spend  
04:04:11: maybe 50% of their time just looking up  
04:04:13: API documentation and another 50% of the  
04:04:16: time like running into some sort of  
04:04:17: error. Like for instance, if I were to  
04:04:19: use this API documentation so let me  
04:04:21: just go over here then feed this into AI  
04:04:24: and say something like tell me about  
04:04:25: this API documentation.  
04:04:28: The first thing it'll do is it'll take  
04:04:30: the link and then it'll try accessing it  
04:04:31: using some sort of web search tool.  
04:04:33: That's what it'll do here. The thing is,  
04:04:35: not all API docs are created equal, and  
04:04:37: so some API documentation pages don't  
04:04:40: actually include um all of the  
04:04:42: information that we need in order to do  
04:04:43: what we need to do. Some of them don't  
04:04:45: return things the way that we need them  
04:04:47: to. So here it's saying the page is  
04:04:49: fairly lightweight on specifics. No  
04:04:50: detailed endpoint schemas, rate limits,  
04:04:52: or code examples. You need to log into  
04:04:53: their dashboard to add the full open API  
04:04:56: spec with the request and response  
04:04:57: schemas. But that's kind of weird  
04:04:59: because we have all the information  
04:05:00: right here, right? Well, that's the  
04:05:02: thing. Some of these API pages only load  
04:05:04: through JavaScript. So realistically,  
04:05:06: this isn't actually capable of accessing  
04:05:07: the API docs. If I said, hey, you know,  
04:05:10: could you find the endpoints or  
04:05:11: something? It could eventually do so,  
04:05:12: but it probably wouldn't do so very  
04:05:13: well.  
04:05:15: So I say, what are the API endpoints  
04:05:17: here? It's going to look for more  
04:05:19: information. So it's going to look for  
04:05:20: some spec to get more detailed  
04:05:21: information about the page. It's going  
04:05:23: to run through the same thing that it  
04:05:24: just did a moment ago, probably to no  
04:05:27: success. And here you see it uses  
04:05:29: JavaScript to render the UI, which means  
04:05:31: the endpoints aren't actual HTML. So now  
04:05:33: it's just starting to look and sort of  
04:05:35: guess at what the um JSON information is  
04:05:38: for the API. Sort of annoying, right?  
04:05:41: Doesn't actually provide that  
04:05:42: information. So what else is it going to  
04:05:43: do? Well, it's going to do more. It's  
04:05:44: going to start looking for other  
04:05:46: people's um API docs. It'll start  
04:05:47: looking for blog posts and stuff like  
04:05:49: that. And I mean like this information  
04:05:51: here, it's not terrible or anything, but  
04:05:52: if we're clear about how long this takes  
04:05:55: and then um what sort of resources it's  
04:05:57: requiring on our end, if I just type  
04:05:59: back slashcontext over here, you can see  
04:06:01: now that we've already started filling  
04:06:03: up our message um context, right? I  
04:06:06: mean, you know, MCP is still the  
04:06:07: prevailing one because this is using the  
04:06:09: same um series that we were using  
04:06:10: before. But yeah, I mean, like messages  
04:06:12: are already 1.4%. We haven't even done  
04:06:13: anything yet. Imagine if this continued  
04:06:15: operating on its own sort of like loop  
04:06:17: for another 30 seconds or so. Hell, we  
04:06:19: probably get up to like 3% 4% 5% or  
04:06:21: more. And so in order to prevent all of  
04:06:23: that from occurring, um, a lot of the  
04:06:25: time for APIs, I will actually just open  
04:06:27: the things that I want. So we wanted  
04:06:30: open, we wanted get, and then  
04:06:32: [gasps and sighs] what else did I do?  
04:06:33: There was like a URL check right over  
04:06:34: here. And I'll just copy all of it in  
04:06:36: directly.  
04:06:38: These are vehins API docs list endpoints  
04:06:42: for me. So now instead of having the  
04:06:45: model do all of that searching itself,  
04:06:47: which if you think about it is like  
04:06:48: that's an additional step which  
04:06:49: compounds error probabilities, I just  
04:06:51: copy and pasted everything in which  
04:06:53: means it's going to get everything right  
04:06:54: on the first try. It's not going to go  
04:06:56: back and forth or try and guess at  
04:06:57: various API endpoints or whatever. I  
04:06:59: basically have everything that I need.  
04:07:01: If I wanted to make a simple API call to  
04:07:04: the post endpoint, what would that look  
04:07:05: like in Python? Now it's actually going  
04:07:08: through and then giving me all the  
04:07:09: information that I need. That's pretty  
04:07:11: straightforward. Okay, great. Let's do  
04:07:12: it. Now, I should contrast that with a  
04:07:15: few other APIs out there that are  
04:07:17: actually optimized directly for AI and  
04:07:19: large language models and agentic  
04:07:20: workflows. So, one in particular is the  
04:07:23: Ampify API and these guys I want to say  
04:07:25: are like a leader, but um there are  
04:07:27: other services that are catching up and  
04:07:28: they're doing stuff like this as well.  
04:07:30: Like obviously I could feed all of this  
04:07:31: in to AI via plain text and you know it  
04:07:33: would do a good job, don't get me wrong,  
04:07:35: but what you'll see is that now there  
04:07:37: actually are copy for LLM buttons up at  
04:07:40: the top of the page. If I were to copy  
04:07:42: this for LLM, view it as markdown, open  
04:07:43: in chat, GBT, open in cloud, open in  
04:07:45: perplexity, it actually like includes  
04:07:47: information for  
04:07:50: AI models and I mean like this is just a  
04:07:52: markdown version of everything we saw on  
04:07:53: the page. Because it's marked down, it's  
04:07:55: actually already significantly more  
04:07:56: efficient and AI natively understands  
04:07:59: how to traverse this. So this is a brief  
04:08:01: example of like APIs accommodating to AI  
04:08:06: models and agentic workflows. APIs are  
04:08:09: sort of like anticipating that agentic  
04:08:10: workflows are going to quickly come and  
04:08:12: swallow up everything. So they're making  
04:08:14: all of their documentation totally  
04:08:16: available through like very token  
04:08:18: performant, token efficient markdown  
04:08:19: like this. So you know if I wanted to  
04:08:22: have it check the um documentation, I  
04:08:23: would actually just copy this  
04:08:27: and then I would just say  
04:08:30: tell me about this API. It would  
04:08:32: actually go when it would um first  
04:08:34: access the page itself to grab all the  
04:08:36: markdown data. And what's cool is  
04:08:37: despite the fact that it's a fair amount  
04:08:39: of text, this does so very quickly. Once  
04:08:41: it's done, it gives me a big overview.  
04:08:44: Then I can also ask follow-up questions.  
04:08:46: What kind of endpoints  
04:08:48: are most common?  
04:08:51: Okay. And as you can see, it's already  
04:08:52: providing me a bunch of information. So  
04:08:54: that's pretty sweet, right? You would  
04:08:56: not believe how much money on the  
04:08:57: internet is available for the taking if  
04:08:59: you just know how to connect APIs. And  
04:09:01: nowadays, to be honest, you don't even  
04:09:02: really have to know how to connect APIs.  
04:09:04: You just need to be able to communicate  
04:09:05: the fact that you want to connect to an  
04:09:07: API to a model. So if you could just  
04:09:08: say, "Hey, here's an API. Could you like  
04:09:10: really quickly connect to it and then  
04:09:11: send a quick test query like XYZ and  
04:09:14: then it does?" So, you know, you can  
04:09:15: actually swoop up a large chunk of like  
04:09:17: the economically valuable work on  
04:09:19: freelancing platforms, simple one-off  
04:09:21: queries that, you know, like businesses  
04:09:23: commonly require. Hey, I'm using  
04:09:25: Xplatform, but Xplatform doesn't have a  
04:09:27: a one-click Zapier integration. How do  
04:09:29: we connect to their API? It's so scary  
04:09:31: and intimidating. I mean like you can  
04:09:33: actually solve that really easily not  
04:09:34: just for yourself but for other people  
04:09:35: with a tool like this. In terms of how  
04:09:38: to actually do the stuff once a workflow  
04:09:40: starts for the first few times maybe  
04:09:42: first 10 or 15 times I actually  
04:09:43: recommend watching it work end to end.  
04:09:45: It seems like this is a big time  
04:09:46: investment keeping in mind that  
04:09:48: workflows can take you know 30 seconds  
04:09:49: to a minute to execute. Um, I don't  
04:09:51: think this is anywhere near that big of  
04:09:53: a deal because if you just watch the  
04:09:55: reasoning for a little bit for even like  
04:09:56: one or two executions, you typically  
04:09:58: learn more about what's the model is  
04:09:59: currently and actually doing under the  
04:10:00: hood than you would if you had like 3  
04:10:03: days of autonomous flows. Uh, and so in  
04:10:05: doing so, you're very very quickly able  
04:10:06: to iterate and make it very very good.  
04:10:08: You don't have to like stretch that  
04:10:09: iteration process out for like weeks or  
04:10:11: months. What's cool too is when you  
04:10:13: watch workflows, you get to develop a  
04:10:14: sense of intuition about the reasoning  
04:10:16: the model goes through. And I honestly  
04:10:17: think there's probably nothing more  
04:10:19: important, no better skill to develop  
04:10:20: than intuition surrounding how models  
04:10:22: think as of the current date. I mean,  
04:10:24: these models are going to run our  
04:10:25: economy very soon and they're already  
04:10:27: running our economy in many ways. So  
04:10:28: like if I am going to spend some time  
04:10:30: working, my whole time working should be  
04:10:32: spent developing an intuition for how  
04:10:34: these models actually function. I mean,  
04:10:35: it's also really satisfying. It's super  
04:10:37: cool just to see the model solve  
04:10:38: problems and, you know, make logical  
04:10:40: conclusions based off information that I  
04:10:42: provided it. And it's usually pretty  
04:10:43: easy to pinpoint when the reasoning goes  
04:10:45: sideways. the model will be like wait  
04:10:47: maybe I should use this approach and  
04:10:48: then you're looking at it you're like  
04:10:49: well that's not the approach to use  
04:10:50: which means you can actually  
04:10:51: significantly cut the amount of time it  
04:10:53: would take by just like pressing X and  
04:10:55: then pausing the run and then just  
04:10:56: saying hey sorry it's actually Y right  
04:10:58: way easier to do it that way and then  
04:11:00: co-creating with that model also again  
04:11:01: lets you build that good intuition for  
04:11:03: how your workflow is supposed to work  
04:11:04: now if I'm handling a really long  
04:11:06: workflow like I have a video editing  
04:11:07: workflow whose full execution due to you  
04:11:09: know the ffmpeg library can take like 45  
04:11:12: minutes or something I'm not going to  
04:11:14: just sit there and watch it obvious  
04:11:15: obviously because most of it is the  
04:11:16: script executing and then my hardware  
04:11:18: running and stuff, right? So, I'll just  
04:11:19: open an extra agent window and then I'll  
04:11:21: use what are called background tasks.  
04:11:22: Background tasks depend on the different  
04:11:24: model provider and interface that you're  
04:11:26: using. Claude introduced background  
04:11:27: tasks a while back and I've been using  
04:11:28: the Claude family of models um quite a  
04:11:30: bit recently. So, that's easy. What I'll  
04:11:32: then do is I'll set up some sort of hook  
04:11:34: in my IDE to play some sort of sound  
04:11:36: when the thing is done. Hooks connect to  
04:11:38: specific points in the workflow. Uh what  
04:11:40: that means is like if you know my  
04:11:42: workflow takes 30 minutes and it's a  
04:11:43: background task when it's done I can  
04:11:44: actually have my computer go duh ding  
04:11:46: and then you know tell me when the thing  
04:11:47: is completed. I'll show you guys an  
04:11:49: example of that later. Um there's also  
04:11:50: native system notifications. Obviously I  
04:11:52: just find the sounds more reliable for  
04:11:54: getting my attention. I get a lot of  
04:11:55: notes nowadays. To set up hooks  
04:11:57: depending on the platform you just  
04:11:58: create a mini workflow that triggers the  
04:12:00: sounds or the animation. So you can just  
04:12:01: like give it a cool sound that you want  
04:12:03: and then say, "Hey, set up this up so  
04:12:05: that when you finish operating um  
04:12:07: there's some hook and then it it  
04:12:08: triggers this sound and it just plays  
04:12:09: natively on my computer because that'll  
04:12:11: help me direct my attention back to you  
04:12:13: and then like help you with the next  
04:12:14: step." Claude has really good  
04:12:15: documentation on hooks. Most people that  
04:12:17: have built hooks have done so with  
04:12:18: Claude. You can check their hook docs  
04:12:20: for specifics. Um the common use case,  
04:12:22: as I mentioned, is to play sound when  
04:12:23: the workflow finishes just so you can  
04:12:25: check the output, verify things which  
04:12:26: you wanted. But you can also do things  
04:12:27: like play different sounds for human in  
04:12:29: the loop steps where it's like, hey,  
04:12:30: action required type stuff. Okay, brief  
04:12:32: example of me setting up a hook. Here's  
04:12:34: a practical guide on setting up hooks.  
04:12:36: So, first of all, what I'm going to do  
04:12:37: is I'll say, hey, how's it going? I'd  
04:12:39: like you to set me up a hook that plays  
04:12:41: a nice chime sound every time that one  
04:12:45: of my agents is done with a task. That  
04:12:48: way, I'll know to go back to the task  
04:12:50: because I normally have you alt tabbed  
04:12:51: while I'm doing other things.  
04:12:55: This already knows that it's a clawed  
04:12:57: code hook feature. There are shell  
04:12:58: commands that execute in response to  
04:12:59: events like tool calls. So now it's  
04:13:01: giving me all this information. First,  
04:13:03: it's going to do some research. Then  
04:13:06: it's going to actually write a script to  
04:13:07: run the claude code hook. All right. And  
04:13:10: it's now adding the hooks configuration  
04:13:12: with a little glass sound. I don't know  
04:13:13: if you guys heard that, but that's that.  
04:13:15: It just finished. So yeah, I did just  
04:13:17: finish. I'm going to pretend I'm alt  
04:13:18: tabbed somewhere, not paying attention,  
04:13:20: but I'm not hearing the chime.  
04:13:26: So, it looks like every time it plays it  
04:13:28: directly, I could hear it.  
04:13:33: Okay. So, I'm going to back slash check  
04:13:36: hooks.  
04:13:38: I'm just going to start a new Cloud Code  
04:13:40: instance like it's telling me to do.  
04:13:42: Hey, how's it going?  
04:13:47: Perfect. And now I hear the chime. So,  
04:13:49: it's that easy. You can now set let's  
04:13:51: say five of these simultaneously.  
04:13:54: One,  
04:13:57: two, three, four. Then I'll just open  
04:14:01: all these in separate tabs. Then I'm  
04:14:04: just going to send to all of them. Write  
04:14:07: me a funny poem.  
04:14:11: Now I will send to all. One, two, three,  
04:14:16: four, five.  
04:14:29: Nice. Now, this thing has gone through  
04:14:31: and written me funny poems, and I got a  
04:14:33: bunch of chimes, too. Hopefully, you  
04:14:35: guys could see how this thing could be  
04:14:37: helpful if you guys were working on a  
04:14:38: cloud code instance without  
04:14:40: notifications enabled or something like  
04:14:41: that, uh, and then you were on another  
04:14:43: tab. In practice, I find when you are  
04:14:45: juggling a bunch of things and trying to  
04:14:47: stay in context, but obviously also  
04:14:49: monitoring or orchestrating some sort of  
04:14:51: AI flow, um, a big chunk of the time you  
04:14:53: will spend is literally just completely  
04:14:55: wasted time where you haven't given AI  
04:14:56: the next instruction. So to really  
04:14:58: economize that time, simplest way to do  
04:15:00: it is just to like have some sort of  
04:15:01: notifying flow. Play a nice chime noise  
04:15:04: or I don't know, you could set it up so  
04:15:06: the claud window actually pops up every  
04:15:07: time it's done. That way, you'll very  
04:15:09: quickly go back to this, give it some  
04:15:11: additional instructions, and then be  
04:15:12: able to double up on the return on your  
04:15:14: time. Now, when any workflow completes,  
04:15:16: you're almost always going to get a  
04:15:17: deliverable. This is a link or a  
04:15:20: document or a summary or something.  
04:15:22: You'll also usually get some sort of  
04:15:24: report of what happened during the  
04:15:26: execution. My recommendation for you is  
04:15:29: to review the output, confirm that it  
04:15:31: meets your needs, and if it does, tell  
04:15:33: the model. Let them know. Say, "This  
04:15:36: worked great." If you've had to do some  
04:15:39: trials and some some iterations in order  
04:15:41: to get this, let the model know that  
04:15:43: like this is what you want and to update  
04:15:45: the directive in execution unless it's  
04:15:47: already done. So most of the time this  
04:15:49: will happen automatically, but it's  
04:15:51: cheap and almost free to say that every  
04:15:53: time you get like a really really good  
04:15:54: output. As I mentioned previously,  
04:15:56: individual workflows are really useful,  
04:15:58: but I actually think chaining them  
04:16:00: together is where the real magic  
04:16:01: happens. I always provide that umbrella  
04:16:04: analogy and I like how my umbrellas are  
04:16:06: getting better and more and more um  
04:16:08: sophisticated as this course goes on. I  
04:16:10: don't think I used to see that little  
04:16:11: thing up there. That's really badass. Um  
04:16:13: this is like your, you know, marketing  
04:16:16: umbrella, you know, your new new client  
04:16:18: onboarding umbrella or whatever. What  
04:16:20: you do is you get all the individual  
04:16:21: workflows that you've created, group  
04:16:23: them under this thing, and then next  
04:16:25: time you can just run all of them  
04:16:27: simultaneously by just saying, "Hey,  
04:16:29: trigger the new onboarded client  
04:16:31: automation." This solves the manual  
04:16:33: handoff process with the deliverable.  
04:16:35: Like you could build a lead scraper. You  
04:16:37: could build an enrichment workflow, but  
04:16:39: what that means is this workflow will  
04:16:41: start and then it'll finish and say,  
04:16:43: "Hey, we're done." And then you actually  
04:16:44: have to take that link and say, "Okay,  
04:16:46: now do the enrichment workflow. Oh,  
04:16:47: okay, now we're done." You have to take  
04:16:48: that and be like, "Okay, let's actually  
04:16:50: send the emails. Okay, now we're done."  
04:16:51: Like much better for me just to  
04:16:53: eliminate that process completely and  
04:16:55: then, you know, only check in once we've  
04:16:57: actually completed the entire thing,  
04:16:58: right? Assuming that I've verified that  
04:17:00: every individual step does what it is  
04:17:03: that I want it to do because otherwise,  
04:17:05: yeah, you're basically the bottleneck.  
04:17:07: And I can't tell you how many times I've  
04:17:09: just had 10 claw instances open or 10  
04:17:12: Gemini instances open and I just forget  
04:17:14: to proceed with one of the steps. It's  
04:17:16: like, "Would you like me to send the  
04:17:18: email?" And then I'm like, "Where the  
04:17:19: heck's this damn email?" And then I look  
04:17:21: back and I realize, "Oh, I didn't  
04:17:22: actually tell it to continue. I wasted  
04:17:23: like an hour." So, I've covered similar  
04:17:25: examples, but here's another one. Uh,  
04:17:27: lead scraping is really popular. So, you  
04:17:29: find potential customers, then you  
04:17:30: enrich their emails, then you  
04:17:32: personalize their first line generation.  
04:17:34: I do this using a casualization workflow  
04:17:36: I've shown you guys multiple times, but  
04:17:38: essentially this is all just batched  
04:17:39: under um you know like end toend  
04:17:44: new client workflow. So that when I get  
04:17:48: a new client, it actually goes through,  
04:17:50: analyzes the client niche, scrapes  
04:17:52: leads, enriches the emails, and then  
04:17:54: does personalized first lines before  
04:17:55: giving me a Google sheet. It's kind of  
04:17:57: cool because this is all stuff that I  
04:17:58: was doing manually step by step. As you  
04:18:00: get to higher levels of abstraction,  
04:18:01: eventually we'll have things that are  
04:18:03: basically like do all of the marketing  
04:18:05: for this campaign and it'll do a really  
04:18:06: good job. When does the agent actually  
04:18:08: require our help? Well, sometimes the  
04:18:11: agent genuinely cannot fix something  
04:18:12: automatically. And it's rare, but when  
04:18:15: this happens, it'll typically just ask  
04:18:16: you directly. Usually, it'll provide a  
04:18:18: fair amount of context, which is good.  
04:18:20: Now, the question is what it was trying  
04:18:22: to do, what went wrong, and then what  
04:18:24: options exist to fix it. Your job is  
04:18:26: literally just to look at that and say,  
04:18:28: "Okay, let's do this then or okay,  
04:18:31: update the directive to do this or are  
04:18:33: you sure you fully tried?" Or, "Have you  
04:18:35: research all of the solutions?" or  
04:18:36: something along those lines. And so, in  
04:18:38: this way, you're not only like uh, you  
04:18:41: know, like a decision maker at a high  
04:18:42: level. A lot of the time, you're also  
04:18:43: just a motivator. To be honest, I can't  
04:18:45: tell you how many times I've had one of  
04:18:46: these agents go on some loop for 10  
04:18:48: minutes and try and build something and,  
04:18:50: you know, they get really close, but  
04:18:52: then they just can't seem to get the API  
04:18:54: spec. And then I say, "Could you  
04:18:55: research the API spec?" And they go,  
04:18:57: "All right, yeah, I'll go research the  
04:18:59: API." And then they actually go do the  
04:19:01: thing and they get it right on the first  
04:19:02: try. It sounds weird, but a lot of the  
04:19:04: time agents don't just need the  
04:19:06: decisions made, they also need some  
04:19:08: level of motivation. I've also found  
04:19:11: that sometimes a gets stuck in a really  
04:19:13: silly loop. Sometimes it'll literally  
04:19:16: just like do the same thing over and  
04:19:17: over and over again and then it'll try  
04:19:19: the same next solution over and over and  
04:19:20: over again and then it'll just chain  
04:19:21: those two together and go back and forth  
04:19:23: and back and forth and back and forth.  
04:19:25: Who knows why this happens? I'm sure the  
04:19:26: smarter the models get, the less this  
04:19:28: will occur. But when this happens, you  
04:19:30: you just pause it. You look at the  
04:19:31: reasoning. You see what's going on. You  
04:19:32: say, "Hey, you've just been doing these  
04:19:34: two things for the last like 20 minutes.  
04:19:35: Could you please not do that anymore?  
04:19:36: Instead, do research on this best  
04:19:38: solution before proceeding." The reason  
04:19:40: why you do this is because iteration is  
04:19:41: actually just really cheap. So it's much  
04:19:43: better to do something than nothing.  
04:19:45: Like I mean the cost of you sending this  
04:19:47: one message or whatever is like cents on  
04:19:49: the dollar, right? And then the  
04:19:50: potential upside is is very very big.  
04:19:53: And typically when you have like a  
04:19:54: massive disparity between the cost and  
04:19:57: then the upside, it would take many many  
04:19:59: many runs of this thing completely  
04:20:02: failing without returning some sort of  
04:20:05: like ROI. And in my case, you know, I'm  
04:20:07: usually capable of doing on the first or  
04:20:08: the second try. So when should you jump  
04:20:11: in? When should you do let it run aka  
04:20:12: when is there human in the loop? The way  
04:20:14: that I determine when I should build a  
04:20:17: human in the loop flow or rather I  
04:20:19: should use human in the loop in a in a  
04:20:20: flow is what is the magnitude of the  
04:20:23: outcome and then what is the sensitivity  
04:20:25: to quality. So if the magnitude of the  
04:20:27: outcome is really big aka this single  
04:20:30: task matters a ton for my business then  
04:20:32: I'm going to step in. If it's very  
04:20:35: sensitive to quality, as in if there are  
04:20:36: very small errors that create  
04:20:38: disproportionately large problems, I  
04:20:40: also step in. And if they're high on  
04:20:41: both, you absolutely want a human in the  
04:20:44: loop. A really simple example of this is  
04:20:46: cold email templates and then outreach  
04:20:48: sequences. So I do a lot of these,  
04:20:50: right? It's part of my day-to-day as  
04:20:51: part of leftclick. I find that when you  
04:20:53: have an AI do 100% of this, performance  
04:20:55: is pretty trash. And the reason why is  
04:20:58: because I could actually graph this.  
04:20:59: There's basically like a really  
04:21:02: uncanny valley essentially where let me  
04:21:07: see  
04:21:09: if this is the let's just say quality  
04:21:14: and then this is the perception.  
04:21:18: If this is zero and then this is one.  
04:21:21: Notice how it doesn't really matter how  
04:21:23: much quality we put in  
04:21:26: until we reach some like phase change  
04:21:28: level and then all of a sudden it goes  
04:21:30: boom and then it becomes really really  
04:21:32: really good. So for my cold email if I  
04:21:35: have AI right AI it's gotten better over  
04:21:37: the years. Maybe it started over here  
04:21:38: and now it's over here and now it's over  
04:21:40: here and now it's over here here here.  
04:21:43: It doesn't really matter how good AI is  
04:21:46: at this process because the sensitivity  
04:21:50: of the perception of my email campaigns  
04:21:53: is very very high. And so there's this  
04:21:56: uncanny valley effect over here where  
04:21:58: like a tiny little improvement in  
04:21:59: quality massively improves the  
04:22:01: perception. And so in situations like  
04:22:03: this where the model just can't seem to  
04:22:04: get up this thing, obviously it makes  
04:22:06: sense for me to like review it really  
04:22:08: quickly, change up two or three words,  
04:22:09: and then boom, all a sudden the quality  
04:22:10: is up here, right? It's like, did I  
04:22:12: objectively change the quality a ton?  
04:22:14: No. But did the perception massively  
04:22:16: change? Yeah. And that might have taken  
04:22:17: me a few moments of work. So, I find  
04:22:19: stuff like that is really, really  
04:22:20: important on um, you know, cold email  
04:22:22: templates, outreach. I would always, you  
04:22:24: know, given the volume of the task, the  
04:22:26: fact that I'm sending this stuff out to  
04:22:27: tens of thousands of people, I would  
04:22:29: almost always at least have a person  
04:22:30: looking it over before it runs because  
04:22:32: it's like, well, what if I'm just like  
04:22:33: off by one degree here? I just wasted  
04:22:35: 10,000 emails. I might have as well like  
04:22:37: spent 2 seconds to fix that up and then  
04:22:39: sent to 10,000 and then gotten much  
04:22:41: better results, right? [gasps] Same  
04:22:43: thing with financial documents like  
04:22:44: invoices and even proposals. I mean, I  
04:22:46: automate the hell out of my proposals,  
04:22:47: don't get me wrong, but I have a human  
04:22:48: in the loop stop. I will take a look at  
04:22:50: the proposal before I send it out cuz  
04:22:52: imagine what if you accidentally added  
04:22:53: an extra zero or something. It's very,  
04:22:55: very unlikely, right? But even if that  
04:22:57: occurs like 01% of the time, you screw  
04:23:00: up on some number because your AI system  
04:23:02: just misinterpreted what you said or  
04:23:03: maybe your voice transcription tool was  
04:23:04: wrong or whatever. The point I'm making  
04:23:06: is like the time savings that you get by  
04:23:08: not looking it over are not at all  
04:23:10: equivalent with the negative impact to  
04:23:12: you, your reputation, and your business  
04:23:14: if you do not look it over. So anywhere  
04:23:17: where there's a few percentage points of  
04:23:18: quality making a massive difference to  
04:23:21: the impact, generally anytime the impact  
04:23:24: over here and then the quality over here  
04:23:28: has this sort of relationship. Pardon  
04:23:29: me, I didn't draw that cuz I think my  
04:23:31: tablet's malfunctioning. Um, you  
04:23:33: generally always want a human in the  
04:23:34: loop. On the other hand, there are a lot  
04:23:36: of tasks out there that are really low  
04:23:37: sensitivity. And when this happens, it's  
04:23:39: like the volume of this thing is a lot  
04:23:42: more important than being perfect. So,  
04:23:43: you might as well just let it run  
04:23:44: completely autonomously. Good example of  
04:23:46: that is web scraping. Like, this is not  
04:23:48: a really high sensitivity task. Models  
04:23:50: are pretty great at this. Creating  
04:23:52: multiple drafts or variations for later  
04:23:54: selection is a design pattern that I use  
04:23:55: all the time. And it's like I don't  
04:23:57: actually need to steer it that much cuz  
04:23:58: the whole idea is I just want it to like  
04:23:59: generate me a bunch, right? So, that's  
04:24:01: really simple. Generally anything that  
04:24:03: sales linearly with quality, right?  
04:24:06: Where it's like the amount of quality  
04:24:08: here and then the amount of impact sort  
04:24:11: of at like a onetoone relationship, I'm  
04:24:13: okay with it going autonomously because  
04:24:15: even if I'm up here, okay, and it's over  
04:24:17: here, the amount of time that I save  
04:24:20: having it automated, you know, at like  
04:24:22: 70% of the full thing versus 100% of the  
04:24:24: full thing is typically way better than  
04:24:26: whatever the the actual impact  
04:24:28: improvement is. Now, some things should  
04:24:30: not be automated at all. I don't  
04:24:32: actually think that you should have  
04:24:33: voice agents doing any sales calls for  
04:24:35: you. And this is something I see so many  
04:24:37: people do. Like if you're offering a  
04:24:39: call, you clearly care a lot about the  
04:24:41: outcome of the call, right? It is a  
04:24:44: hightouch sales conversation. And you  
04:24:47: know, if there's even a.1% chance that  
04:24:50: somebody thinks that there's not a real  
04:24:51: human being talking to them, it's like a  
04:24:52: robot. That's going to have a much  
04:24:54: bigger impact on the quality of that  
04:24:56: deal than 0.1%. Right? So it's not a  
04:24:58: linear relationship between that at all.  
04:25:00: And you know, some things I just don't  
04:25:01: automate. Like would I automate the  
04:25:03: calling of my client or something? No, I  
04:25:05: I wouldn't. At least not right now at  
04:25:06: current levels of tech. Maybe if um  
04:25:08: agentbased calling becomes better and  
04:25:10: like more socially acceptable later. But  
04:25:12: for now, no. What I would do is I would  
04:25:14: like automate the process of coming up  
04:25:16: with a bunch of information and context  
04:25:18: about the client. I would automate the  
04:25:20: process of doing research on the client.  
04:25:22: These are all things that scale pretty  
04:25:23: linearly as I was talking about, right?  
04:25:24: So, I'd have some big dossier of  
04:25:26: information in front of me to save me  
04:25:28: from having to manually go through hours  
04:25:30: and hours of LinkedIn research, but um I  
04:25:32: would actually just make sure that the  
04:25:33: actual calling part is me, right? It  
04:25:34: just doesn't make sense. It's too  
04:25:35: sensitive of a process. Research, on the  
04:25:38: other hand, a lot more linear. There's  
04:25:40: some situations that do require empathy,  
04:25:42: judgment, but you can convert situations  
04:25:44: that require empathy and judgment into  
04:25:46: situations that you just like  
04:25:47: automatically say yes or no to. A good  
04:25:49: example of this is um Amazon. Amazon has  
04:25:51: like basically automatic refund  
04:25:53: dispersement. If uh you have asked for I  
04:25:56: think less than like a 2% refund rate or  
04:25:58: something like that. So if there's an  
04:25:59: issue with your order and like for the  
04:26:01: most part you don't ask for refunds very  
04:26:02: often and you say, "Hey, there's some  
04:26:03: issue with this. Could you give me a  
04:26:04: refund?" Like they will automatically be  
04:26:06: like, "Yes, refund granted." And then  
04:26:08: you're like, "What the hell? I didn't  
04:26:09: even tell anybody about like I didn't  
04:26:10: even give a photo or anything. It's  
04:26:12: fully automatic." It's like, "Yeah, see  
04:26:14: how much time and energy they save by  
04:26:15: doing that." So you can just reconstruct  
04:26:18: um sensitive customer situations and  
04:26:20: like quantify them and then you can like  
04:26:21: totally automate them. But in situations  
04:26:23: where like you genuinely can't. Let's  
04:26:24: say this is somebody with sort of a  
04:26:26: shakier refund rate and stuff like yeah,  
04:26:28: you're going to need to find a way to  
04:26:28: pass that off to somebody that has  
04:26:30: empathy and judgement. So yeah, I mean I  
04:26:33: would not automate things just for the  
04:26:34: sake of automating them. I'd only ever  
04:26:36: automate something if like it actually  
04:26:37: made a bottom line difference to my  
04:26:38: business. And things like lead scraping  
04:26:40: for instance, research, accumulation of  
04:26:42: large data sets and stuff like Like all  
04:26:43: this stuff in videos make a large  
04:26:44: difference to my bottom line. So I'm  
04:26:46: happy to automate it. But the calls and  
04:26:47: whatnot, it's all just me, baby. At the  
04:26:49: end of the day, your goal is supervised  
04:26:51: autonomy. It is not babysitting. So I  
04:26:54: just talk to them like Slack messages. I  
04:26:56: do not use formal syntax or precise  
04:26:58: technical language. I just DM my  
04:27:00: colleagues and then just replace the  
04:27:02: colleagues with my agent. You know, uh I  
04:27:04: was running a YouTube workflow just the  
04:27:06: other day to edit one of my videos and I  
04:27:07: said, "Hey, could you run the YouTube  
04:27:08: editor for the new file? Make the cuts a  
04:27:10: little bit tighter." and it took the  
04:27:11: average cut distance and then it just  
04:27:13: like decreased it a little bit and then  
04:27:14: it just reran the YouTube editor and  
04:27:16: then I said I liked it so then it  
04:27:17: updated the flow so I would just use  
04:27:18: that the next time. Same thing with  
04:27:20: voice transcription in general. Just  
04:27:22: just speak naturally and then send it.  
04:27:23: It'll understand you. Okay. So manually  
04:27:25: triggering these workflows is actually  
04:27:27: just the beginning and that may be  
04:27:28: frustrating for you because there many  
04:27:29: hours through the course but that goes a  
04:27:31: lot deeper than this. Right now what  
04:27:33: we're doing is we're opening our IDE.  
04:27:35: We're talking to our agents and then  
04:27:36: we're starting the flows yourself, which  
04:27:38: is fine if you have like ad hoc tasks,  
04:27:39: one-off requests. It's fine when you  
04:27:41: work 8 hours a day and between, you  
04:27:42: know, 9 to5 or whatever when you're at  
04:27:44: your desk, you can you can get things  
04:27:45: done. But as I'm sure you'd imagine, the  
04:27:48: automatic part in the word automation,  
04:27:50: like the auto is pretty important,  
04:27:52: right? So, how do you actually have  
04:27:53: these things run automatically without  
04:27:54: your involvement? Well, these are called  
04:27:56: event- driven workflows. For instance,  
04:27:58: let's say a new lead fills out your  
04:27:59: website form. You want a workflow that  
04:28:01: automatically replies and books a  
04:28:02: meeting, right? But what if the new lead  
04:28:03: comes in at 5:30 and and you leave for  
04:28:05: home at 5? What if a customer sends a  
04:28:07: support email? Your agent does the  
04:28:09: triage, write the draft, and writes to  
04:28:10: the right person for sending. I mean,  
04:28:12: that's great and all, but like what are  
04:28:13: you going to do? Like wait until the  
04:28:14: next day, um, look at your inbox and  
04:28:16: then do the triage, then that defeats  
04:28:18: the purpose. So, how do we actually  
04:28:19: build these things? There's also  
04:28:21: schedule driven workflows. Maybe it's  
04:28:22: 9:00 a.m. on Monday and you want a  
04:28:24: weekly report to generate itself. So, do  
04:28:25: you really want to come in every Monday  
04:28:27: and then be like, "Hey, generate my  
04:28:29: weekly report." I mean, of course, you  
04:28:30: can, but it's nice if some of these  
04:28:31: things are done automatically for you.  
04:28:32: Maybe the weekly report is summarizes  
04:28:34: your work and then sends it to your boss  
04:28:36: or something or your client with your  
04:28:38: timetable, right? Same thing for these  
04:28:40: other things. These are uh specific  
04:28:42: schedules. Well, that's what we're going  
04:28:43: to learn about next. Web hooks and  
04:28:45: scheduling. Now that you know everything  
04:28:46: that you need to know about agentic  
04:28:48: workflows in order to build them and  
04:28:51: then use them, it's time to take these  
04:28:54: things which up until now have been  
04:28:55: constrained to your own device or your  
04:28:57: integrated development environments,  
04:28:59: then put them in the cloud where they  
04:29:00: can be triggered through means other  
04:29:02: than you actually prompting. So in order  
04:29:05: to do this successfully, which I'm going  
04:29:07: to call cloudifying my workflows, we  
04:29:11: don't actually upload the orchestrator  
04:29:13: itself. Remember in the loop where we  
04:29:16: have the directives, the orchestration  
04:29:17: layer and then the executions. What we  
04:29:19: don't upload is the orchestrator. All we  
04:29:22: really do is upload the execution  
04:29:24: scripts themselves which are the  
04:29:26: deterministic parts. You can also upload  
04:29:28: the directives too if you wanted to  
04:29:30: provide context to a a model later on in  
04:29:33: case it wanted to edit or or whatever.  
04:29:35: So for the most part just upload the  
04:29:38: execution scripts. I'm going to show you  
04:29:39: guys how to do that and some  
04:29:41: alternatives. The way that you can think  
04:29:43: of it is as creating many APIs that do  
04:29:46: one specific thing reliably. And the  
04:29:48: same concepts apply whether you're using  
04:29:49: DO or other frameworks like cloud skills  
04:29:52: or whatever. Now you may be wondering  
04:29:54: Nick what is fundamentally different  
04:29:55: about this versus what we were doing  
04:29:57: before. Well, what's fundamentally  
04:29:58: different about this versus what we're  
04:30:00: doing before is there is no LLM.  
04:30:01: Instead, all we're really doing is we're  
04:30:03: just creating our own API and we're  
04:30:05: using LLMs to do it really really  
04:30:06: quickly and easily with some sort of  
04:30:08: defined input and output. The reason why  
04:30:10: is because you need to remember  
04:30:11: stochasticity or sort of randomness. The  
04:30:14: tendency for models to eventually  
04:30:15: diverge from what it is that you wanted  
04:30:17: them to do over time given enough time  
04:30:19: steps. So because of this, LMS are very  
04:30:21: probabilistic and they sort of have  
04:30:22: randomness in every direction. When  
04:30:24: they're working in your IDE, for the  
04:30:26: most part, you're around, right? Whether  
04:30:27: you're not looking at it right this  
04:30:28: second, you'll probably look at it at  
04:30:30: some point over the course of the next  
04:30:31: hour. And because of that, if it has an  
04:30:33: issue, you're watching. You can course  
04:30:34: correct. But if it's 3:00 a.m., okay,  
04:30:36: and this is running unattended with full  
04:30:38: system permissions, this level of  
04:30:40: variability is a liability. And so we're  
04:30:42: taking the AI just out of the cloud loop  
04:30:45: entirely.  
04:30:47: Additionally, instead of having slightly  
04:30:48: different routing decisions like we see  
04:30:50: here, we're just going to force them  
04:30:52: into one routing decision every time  
04:30:54: using what's called server side logic.  
04:30:56: So because your execution scripts do the  
04:30:58: same thing every time, you never  
04:31:00: actually have to suffer this. Instead,  
04:31:01: it's always just, hey, we start by  
04:31:03: executing node one, then we move to  
04:31:05: executing node two, and then so on and  
04:31:07: so on and so forth to node n. And all  
04:31:11: we're doing is we're taking those  
04:31:12: execution scripts, deploying them as  
04:31:14: standalone cloud functions. No LLM in  
04:31:16: the loop, just an API on a schedule or  
04:31:18: responding to web hooks. The  
04:31:19: intelligence that we use during this  
04:31:21: process is just used to build the  
04:31:23: execution scripts, not to actually run  
04:31:24: them. In this way, you can consider this  
04:31:26: like basically deploying your own mini  
04:31:27: app. A good way to think about this is,  
04:31:29: you know, like your agent is the  
04:31:31: architect and your cloud workflow is the  
04:31:32: building. Architects design buildings  
04:31:34: all the time, but it's very rare that  
04:31:36: they actually live in the buildings they  
04:31:37: design, right? So, what our agent is  
04:31:38: doing in this point is just architecting  
04:31:40: our beautiful building and we're going  
04:31:42: to put execution scripts to live in  
04:31:44: there instead. This obviously loses a  
04:31:46: fair amount. I mean, this takes our  
04:31:47: agentic workflows and changes them back  
04:31:49: into traditional workflows or procedural  
04:31:51: workflows. It means that they can't  
04:31:53: adapt to unexpected situations on the  
04:31:55: fly. They also can't self-anneal or ask  
04:31:58: clarifying questions when things get  
04:31:59: weird. You know, you are going back to  
04:32:01: that old school traditional automation  
04:32:02: behavior and it just does exactly what  
04:32:04: you told it to do. Nothing more, nothing  
04:32:05: less. But if you think about it, by the  
04:32:08: time your workflows deploy, they should  
04:32:10: be pretty battle tested as I was  
04:32:12: mentioning earlier from having run  
04:32:14: dozens of times locally and you've  
04:32:15: probably already worked out all the  
04:32:17: kinks in your IDE locally where the  
04:32:18: debugging is easy. So if something  
04:32:20: breaks, you are still going to get error  
04:32:22: notifications. And the really cool thing  
04:32:23: is you can just fix it with your agent.  
04:32:24: If you're using a modern platform like  
04:32:26: modal, um models can read the errors  
04:32:28: from modal really easily. So you can  
04:32:29: actually just say, "Hey, this workflow I  
04:32:30: think is broken, fix it." And I can  
04:32:32: actually just do the debugging process  
04:32:33: for you. So you get all of like the  
04:32:35: ability to debug and stuff like that.  
04:32:37: It's just you're not doing it on like a  
04:32:39: live loop because if you were doing it  
04:32:40: on a live loop, results, assuming that  
04:32:42: it doesn't do what you wanted to do,  
04:32:44: could be catastrophic, go all over the  
04:32:45: place. And I mean like I could sit here  
04:32:47: and I could give you guys a way to do  
04:32:49: this that includes the orchestrator  
04:32:51: directly in the uh environment. I could  
04:32:54: have the agent actually like listening  
04:32:55: and constantly modifying things. But  
04:32:57: I've tried this now in a in a few actual  
04:32:59: businesses. And despite the fact that  
04:33:00: it's very shiny and it's very sexy and  
04:33:02: people like, "Wow, I can just query my  
04:33:03: LLM um you know on some cloud container  
04:33:06: somewhere and have it do whatever I want  
04:33:07: via web hook." Despite the fact that it  
04:33:09: seems really cool, we're just not there  
04:33:11: yet. I'm pretty sure we'll be there some  
04:33:13: point in the next couple of years, but  
04:33:14: for now we're just going to leave the  
04:33:15: orchestrator out of it completely and  
04:33:17: basically just use our agentic workflow  
04:33:19: building skills to build APIs really  
04:33:21: quickly that we can then call. So the  
04:33:23: platform that I use for all this is  
04:33:24: called modal. Modal is not the only  
04:33:27: platform out there. There are many  
04:33:29: others like trigger.dev etc. I'm not  
04:33:31: associated with any of these. Um but  
04:33:33: modal is just a good product.  
04:33:34: Trigger.dev is a good product. We've set  
04:33:36: up some workflows there and there are a  
04:33:37: couple of other builders too that like  
04:33:39: essentially do this function. But  
04:33:41: essentially the way that u modal works  
04:33:42: is it's really simple. You just take a  
04:33:44: Python script and then you turn it into  
04:33:46: a cloud function. It's also pay-per-use.  
04:33:48: So when your workflow isn't running,  
04:33:49: it'll spin down and it'll cost nothing.  
04:33:51: You'll get a web hook URL just like you  
04:33:52: would from make or nad. And it's also  
04:33:54: very cheap, especially for Python based  
04:33:56: execution scripts. They gave me $5 of  
04:33:58: credits the beginning of this month and  
04:33:59: I think so far I've used like 3 cents.  
04:34:01: So very very very affordable. The best  
04:34:03: part is you don't need to know anything  
04:34:04: about any of these platforms to be  
04:34:05: honest. They're built for agents and so  
04:34:08: agents know how to crawl them and  
04:34:09: traverse them and set things up really  
04:34:10: easily because their documentation is  
04:34:12: fantastic. All I really had to do in  
04:34:14: order to do this, which I'll show you in  
04:34:15: a moment, is say turn this into a cloud  
04:34:17: function. And then it did everything  
04:34:18: else. Now, the web hook URLs that modal  
04:34:20: gives you can be called from anywhere,  
04:34:21: including by other agents. And then it  
04:34:23: also allows people at regardless of  
04:34:25: whatever skill level you are to set up  
04:34:27: this sort of web hook or event- driven  
04:34:28: flow. It's sort of like nadn or make.com  
04:34:31: or you know gumloop or zapier any one of  
04:34:34: these platforms  
04:34:36: these will expose these little web hook  
04:34:38: urls right and you take these web hook  
04:34:41: urls and then you give them to services  
04:34:43: like I don't know um clickup or  
04:34:46: instantly or pandadoc or whatever the  
04:34:47: heck you want right well this is exactly  
04:34:49: what modal does it's just instead of  
04:34:51: giving it to you in sort of this visual  
04:34:52: way um we just do it through natural  
04:34:54: language we're like hey set this thing  
04:34:56: up and then give me a web hook URL so  
04:34:57: that I can call here's what the request  
04:34:59: body is going to look like. Cool. We  
04:35:00: done. Awesome. Thank you very much. That  
04:35:02: said, wanted to take a couple steps back  
04:35:03: here just in case people didn't know  
04:35:04: what web hooks are. If what I just said  
04:35:06: made no sense to you, that's okay. I'm  
04:35:07: going to cover it. First of all, a web  
04:35:08: hook is literally just a URL that  
04:35:10: triggers your workflow when something  
04:35:11: hits it. So, an external system like a  
04:35:13: CRM or website form or make or n can  
04:35:16: actually just call a URL like this  
04:35:17: automatically. It's just like a  
04:35:18: doorbell. When somebody presses it, your  
04:35:20: workflow will wake up and run. Um, you  
04:35:22: don't necessarily have to be there to do  
04:35:23: it. If you guys have ever done any home  
04:35:24: automation stuff, any sort of like, I  
04:35:26: don't know, switches or whatnot, it's  
04:35:28: the same it's the same idea. There's  
04:35:29: like some URL somewhere, some  
04:35:31: destination, it could even be your  
04:35:33: website, and when somebody visits it, it  
04:35:35: triggers something that does something  
04:35:36: else. Obviously, the something else in  
04:35:38: this case is going to be our automated  
04:35:39: workflow. If I had a URL like this,  
04:35:41: let's say it's my  
04:35:42: nick-thbot.webhook.com,  
04:35:45: I could do anything with this URL. Like  
04:35:46: I I could literally just like enter this  
04:35:47: into my browser and press enter, and it  
04:35:49: would trigger a flow. Or I could send an  
04:35:50: HTTP request which is um like a web  
04:35:53: request through make.com nada and any  
04:35:55: other noode builder. I could do it  
04:35:56: through my terminal. I could do it  
04:35:57: through an agent. But basically this is  
04:35:58: just a destination on the internet.  
04:36:00: Okay, that's like a node and when  
04:36:02: somebody accesses the node, this thing  
04:36:04: does some logic and depending on whether  
04:36:06: or not the node input fits its  
04:36:07: specifications, it'll continue and then  
04:36:09: call whatever the heck you want. So web  
04:36:10: hooks really are just like URL with some  
04:36:12: logic attached to them. That's more or  
04:36:13: less it and they're very very common in  
04:36:15: any sort of automated scenario. All  
04:36:17: right. So, what is the agent doing  
04:36:18: behind the scenes in order to set this  
04:36:20: up for you? Well, it'll review our  
04:36:21: agents.mmd and our claude MD and our  
04:36:23: gemini.mmd and so on and so forth. Just  
04:36:26: to understand the setup first, ideally  
04:36:27: somewhere in there, you would say, "Hey,  
04:36:29: you know, as part of your work, one of  
04:36:30: the things you do is you set up cloud  
04:36:32: web hooks or cloud scheduled workflows  
04:36:35: on modal. Here's how to do so." What it  
04:36:37: then does is it looks at your existing  
04:36:38: execution scripts for the workflow that  
04:36:40: you want to deploy. It'll wrap  
04:36:41: everything in a simple format that modal  
04:36:43: really likes proper decorators and  
04:36:45: whatnot and then if there are any  
04:36:47: prompts or API keys or whatever it'll  
04:36:49: actually like ask you for them although  
04:36:50: I find most of the time it's  
04:36:51: plug-and-play it's just like oh you know  
04:36:52: I have the keys let me convert them into  
04:36:54: modals format once deployed you get a  
04:36:56: simple URL this is the you know node  
04:36:58: that it calls um this is the phone  
04:37:00: number that other systems can give a  
04:37:01: ring in order to make something happen  
04:37:03: and then in whatever service you're  
04:37:05: using because this is obviously being  
04:37:06: triggered by some service by some  
04:37:08: notification from Slack or some some  
04:37:10: incoming web hook from instantly or  
04:37:12: whatever, you just give them the web  
04:37:14: hook URL. And a lot of the time there's  
04:37:15: like a field or something and it'll say,  
04:37:16: "Hey, what's the web hook URL you want  
04:37:18: us to send results to?" And then you  
04:37:19: just put it there. The request just  
04:37:21: needs to match the format that the agent  
04:37:23: expects. It's usually in what's called  
04:37:24: JSON or JavaScript object notation. You  
04:37:26: don't actually need to know JSON  
04:37:27: nowadays. Um, all you need to do is be  
04:37:28: able to recognize it. Typically starts  
04:37:30: with some curly braces and then when  
04:37:32: your agent sees this, um, you know, you  
04:37:33: can just copy and paste whatever you see  
04:37:35: in the web hook documentation. It'll go  
04:37:37: from a demo to actually doing stuff  
04:37:38: really, really quickly, which is  
04:37:39: fantastic. If you don't know how to  
04:37:40: connect stuff, you literally just ask,  
04:37:42: "Hey, how do I set up, you know, ClickUp  
04:37:43: to call this web hook when a new lead  
04:37:44: comes in agent or Claude or Gemini or  
04:37:47: whatever you're using, we'll actually  
04:37:48: walk you through all that step by step,  
04:37:50: especially if it's a platform specific  
04:37:51: UI thing. I find a lot of the time  
04:37:52: they'll just pick, oh, um, here's the  
04:37:53: link. Just go to this link and then  
04:37:55: you're done." You don't need to spend  
04:37:56: hours Googling stuff or chatbing stuff.  
04:37:58: This is exactly what the tools are good  
04:37:59: at. So, don't sweat it. And to take that  
04:38:01: one step further, if you wanted to,  
04:38:02: instead of making it web hook driven,  
04:38:04: have it schedule driven, you just use  
04:38:06: something called cron. Um, again, this  
04:38:08: is something that's very native that is  
04:38:09: supported by Modal and our agents out of  
04:38:11: the box. Instead, you just say, "Hey,  
04:38:13: can you run this thing at, you know,  
04:38:14: 5:00 p.m. every single day, and it'll do  
04:38:16: it. No complex configuration. You just  
04:38:18: describe when you want something to run.  
04:38:19: It'll handle all the syntax and  
04:38:20: deployment details." That's just kind of  
04:38:22: annoying for me because I spent a lot of  
04:38:23: time learning cron way back in the day  
04:38:25: when I wanted to schedule simple things.  
04:38:27: But, um, yeah, it's just like setting a  
04:38:28: recurring calendar reminder. You're just  
04:38:30: doing it for your workflows. So, God  
04:38:31: bless the fact that we are at this point  
04:38:32: where technology can do all that for us  
04:38:34: because good lord do I not want to have  
04:38:36: to learn another scheduling syntax  
04:38:37: again. Okay, so some example prompts.  
04:38:39: You just say, "I want my weekly workflow  
04:38:41: report to run automatically every Monday  
04:38:42: at 9:00 a.m. It'll actually set up the  
04:38:44: cron for you. Deploy it to modal and so  
04:38:45: on and so forth." You know, agent will  
04:38:47: figure out the rest. Whatever your  
04:38:49: timing is, whether it's every minute,  
04:38:50: every hour, every year, every 2,000  
04:38:53: years, whatever, like you can set this  
04:38:54: stuff up really, really easily. Don't  
04:38:56: sweat it. Um there is some like  
04:38:59: misunderstanding usually in modal about  
04:39:01: like API keys and tokens and credentials  
04:39:03: and stuff like that. Um inevitably you  
04:39:05: will need obviously to connect one  
04:39:06: platform to another and there is always  
04:39:08: going to be some inherent risk in  
04:39:09: uploading a secret to the server. So  
04:39:11: just keep that in mind. By making things  
04:39:13: cloud accessible you are introducing a  
04:39:14: little bit of risk. You're basically  
04:39:15: setting up a server on the internet  
04:39:16: right like anybody can theoretically  
04:39:18: access it if they know your credentials,  
04:39:19: password, whatever. So your agent will  
04:39:21: prompt you naturally. It'll say hey this  
04:39:23: script needs your Apollo API key. Should  
04:39:24: I use what's in your env? All you do is  
04:39:26: you just say yes. You just say no. You  
04:39:28: say hold on, use this one instead or or  
04:39:30: whatever. The way that modal works  
04:39:31: really is they will store these  
04:39:32: credentials as an encrypted secret which  
04:39:34: is separate from your code and then the  
04:39:36: credentials only actually run when  
04:39:38: somebody calls the the web hook. So it's  
04:39:40: never actually like in the codebase or  
04:39:42: whatever. It's kind of similar to how we  
04:39:43: separate our code from thev file in um  
04:39:46: you know our IDE. Very very common. It's  
04:39:49: not specific to Asian workflows, but  
04:39:50: yeah, it's the same way that  
04:39:51: professional engineering teams do this  
04:39:53: sort of thing. And then what happens to  
04:39:54: your IDE is it basically just becomes  
04:39:55: your command center. I mean I obviously  
04:39:57: do both um cloud workflows and then I  
04:40:00: also do local workflows. And I actually  
04:40:01: just like have all of them operate from  
04:40:03: my IDE. Like I will say hey run this  
04:40:05: workflow and it'll be like okay this is  
04:40:06: a cloud workflow so I'm going to call  
04:40:08: this web hook URL. Then it'll actually  
04:40:09: create its own request and then send it  
04:40:11: to my own server which is kind of cool.  
04:40:14: Um although keep in mind that when you  
04:40:15: do that as I mentioned earlier you will  
04:40:17: remove the agentic kind of part the  
04:40:19: self- annealing and so on and so forth.  
04:40:21: What's really cool though is your IDE  
04:40:22: helps you get this done too. And then  
04:40:24: what you end up with is you actually end  
04:40:25: up with specific agentic workflows made  
04:40:27: to automate the process of uploading  
04:40:28: things to modal which is pretty sweet.  
04:40:31: What are my recommendations around when  
04:40:32: to actually turn something into a cloud  
04:40:34: workflow? Um just scheduled workflows.  
04:40:36: If you guys have stuff that is like a  
04:40:38: daily report or a weekly summary or some  
04:40:39: sort of like recurring scrape or HTTP  
04:40:41: request, like you can do that in modal,  
04:40:43: no problem. If it's event triggered, aka  
04:40:45: um it's very timely, you need to do  
04:40:47: something within a few moments of some  
04:40:48: other requests coming in, then set up  
04:40:50: the web hook functionality like I talked  
04:40:51: about and then boom. But if it doesn't  
04:40:53: fit one of these two categories, believe  
04:40:55: it or not, probably is best to stay  
04:40:56: local. If it does not need to run when  
04:40:59: you're not around, it's probably better  
04:41:00: to like run it while you are around  
04:41:01: because as I mentioned, these agentic  
04:41:03: workflow things, they uh they multiply  
04:41:05: your leverage like crazy right now,  
04:41:06: right? But they also multiply the error  
04:41:08: bounds. So you should probably be around  
04:41:10: to see in case it does something you  
04:41:11: don't want it to do. Now, if you're just  
04:41:13: hanging around by your computer for 3 or  
04:41:15: 4 hours a day or whatever, keep in mind  
04:41:16: you are now doing like 3 or 4 hours a  
04:41:18: day of work, keep in mind that like you  
04:41:21: are now capable of doing 30 to 40 hours  
04:41:23: of work in the 3 or 4 hours with aentic  
04:41:25: workflows. Um, so it's not like you're  
04:41:26: really losing too much here. You're  
04:41:28: multiplying your leverage as all  
04:41:29: technology is done. But there are of  
04:41:31: course some instances and automations  
04:41:32: where you just always want to run the  
04:41:33: thing automatically and and that's  
04:41:34: that's what this is for.  
04:41:39: Last thing I really need to mention  
04:41:40: about this is logging and monitoring.  
04:41:43: Now, if something happens in your IDE,  
04:41:46: it's typically pretty easy to see where  
04:41:47: it went wrong. Why? Because you have  
04:41:49: little reasoning windows that you can  
04:41:50: pop open, right? It's very easy for you  
04:41:52: to like see and poke around and be like,  
04:41:53: "Okay, I could see that there was a  
04:41:55: problem here with this HTTP request and  
04:41:56: so on and so forth." But right out of  
04:41:58: the box, um, in the cloud, you don't  
04:42:00: have access to that and most of this  
04:42:02: logging functionality is not around. So,  
04:42:04: cloud deployments don't have that. What  
04:42:06: that means is your agent action needs to  
04:42:07: explicitly force the logging in the  
04:42:09: code. It won't always be able to do this  
04:42:11: and um when it can't do this, the debug  
04:42:13: process can take quite a while. That  
04:42:15: said, okay, if you learn how to build in  
04:42:17: some form of observability, that's what  
04:42:19: this is called in programming. I'm in  
04:42:21: from the start, it becomes a lot more  
04:42:23: straightforward. My own personal  
04:42:24: monitoring setup is I actually have a  
04:42:26: dedicated Slack channel called  
04:42:27: Agentic-Cloud-LOG  
04:42:29: for all cloud workflow updates. So every  
04:42:31: time a workflow runs, it'll actually  
04:42:33: automatically send an update to my own  
04:42:35: Slack channel letting me know if it was  
04:42:36: successful or not. I have like a pretty  
04:42:38: superficial highle version of  
04:42:40: interpretability now and observability.  
04:42:42: If something happens, I know that it  
04:42:44: worked. If something doesn't happen, I  
04:42:45: know that it didn't work. Uh it's not as  
04:42:46: like super in-depth as it could be, but  
04:42:48: it's simple enough that I could just  
04:42:50: look at that and then go to my agent and  
04:42:51: then say, "Hey, you know, I noticed this  
04:42:52: thing isn't working. Can you double  
04:42:53: check to see what's going on?" And then  
04:42:54: it can do its loop on its own. I don't  
04:42:56: need to be around. And then, you know, I  
04:42:57: can continue working on something else  
04:42:58: while it does that. But if I didn't have  
04:43:00: this, if I didn't know, then obviously  
04:43:02: that would be a problem. I've seen some  
04:43:04: ways that people have built automated  
04:43:06: systems where they will um automatically  
04:43:08: take an error notification and send it  
04:43:10: back to another cloud, a claude or  
04:43:12: Gemini or, you know, GPT 5.2 instance or  
04:43:16: something like that and basically say,  
04:43:17: hey, there was some error with this  
04:43:18: thing. Fix it. And it'll just like do it  
04:43:20: completely autonomously. I think that  
04:43:21: stuff can be kind of cool. Although,  
04:43:23: keep in mind like most people aren't  
04:43:25: building like 3,000 web hooks a day,  
04:43:26: right? So that's usually not the actual  
04:43:28: bottleneck. the bottleneck is more like,  
04:43:29: you know, why are you building this  
04:43:30: webbook in the first place? So, I don't  
04:43:32: really want to like mislead people here  
04:43:33: and have them build these cool automatic  
04:43:35: self-fixing loops when it doesn't really  
04:43:37: matter all that much in the first place.  
04:43:39: Not to mention like the probability of  
04:43:40: it actually entirely fixing itself  
04:43:42: without introducing more errors is  
04:43:43: pretty low. And you know, I hopefully  
04:43:45: you guys understand what I'm trying to  
04:43:46: say. Okay, so pretty easy to do that.  
04:43:47: You just say, "Hey, when you deploy to  
04:43:49: modal, make sure to add logging that  
04:43:50: sends me a Slack message every time it  
04:43:52: runs. Here's my Slack web hook URL." If  
04:43:54: you don't have that, you can ask it,  
04:43:55: hey, get me a Slack web hook URL. If  
04:43:57: you're using Discord or something, you  
04:43:58: do the same thing there. If you, I don't  
04:44:00: know, want a text message or an email  
04:44:01: address, you can obviously set that up  
04:44:02: on your end as well. Pretty  
04:44:03: straightforward. I also say stuff like,  
04:44:05: "Hey, could you give me a status check  
04:44:06: on all my modal deployments? How are  
04:44:07: they going?" It'll go through all of the  
04:44:09: modal deployments, run through their  
04:44:10: logs. Um, it has access to its API. As I  
04:44:13: mentioned, the docs are pretty  
04:44:14: straightforward. And so, you end up just  
04:44:16: getting everything that you need from a  
04:44:17: a check-in like this. So, you can do it  
04:44:19: manually, you can do it based off of  
04:44:20: like some Slack notification, you can do  
04:44:22: it based off the email notice that you  
04:44:24: get. There are a lot of um ways to error  
04:44:26: handle this. The reality is you just  
04:44:27: need to like know to do this. If you  
04:44:29: don't do this, you're going to have a  
04:44:30: bad time. In the future, we will have  
04:44:32: cloudnative agents, right? Instead of  
04:44:34: leaving the orchestrator out of this,  
04:44:36: we're going to actually be inserting the  
04:44:37: orchestrator in. And so, we're going to  
04:44:39: minimize that agent accuracy as models  
04:44:41: get more intelligent and people design  
04:44:43: better frameworks to deal with us. It'd  
04:44:44: be pretty cool, right? If you think  
04:44:45: about it, what you could do is you could  
04:44:47: just send a natural language query to,  
04:44:49: let's say, nyx-agent.com.  
04:44:51: This is my agent, with a question mark,  
04:44:53: which is a query parameter that says,  
04:44:54: "Run the lead scraper." It would then go  
04:44:56: through the agent PTM MRO loop. It would  
04:44:58: do planning. It would do tool use. It  
04:45:00: would check its memory. It would do some  
04:45:02: reasoning and reflection before finally  
04:45:04: doing the orchestration. But as I  
04:45:05: mentioned, now we're just at the point  
04:45:06: where the error bars are a little too  
04:45:08: high. It will be pretty cool though  
04:45:09: because once you're done with that,  
04:45:10: you'll be able to set up a whole  
04:45:12: ecosystem of just cloud agents that talk  
04:45:13: to each other and hang out. So, you  
04:45:15: know, you'll have one agent here, Nick's  
04:45:17: agent, then you'll have Peter's agent,  
04:45:18: and then Sam's agent. Then Peter's agent  
04:45:20: will say something Nick's agent, which  
04:45:22: will query Sam's agent for more  
04:45:24: information. and they'll decide on  
04:45:25: something together and then I don't  
04:45:26: know, you could even introduce payments  
04:45:27: into this sort of structure and more.  
04:45:29: So, early versions of this do exist  
04:45:31: today. I published some videos exploring  
04:45:33: some of them. Just check out my channel.  
04:45:34: They're just a little too high risk  
04:45:36: right now and it just doesn't really  
04:45:37: make too much sense to do that all  
04:45:38: yourself. Okay, so I'm going to walk you  
04:45:39: through actual modal web hook  
04:45:41: deployment. Now, I have a bunch of  
04:45:42: prompt templates and stuff like that.  
04:45:43: You can obviously get all of that stuff  
04:45:44: in the link at the very top of our  
04:45:46: description. Um, let's actually go  
04:45:48: through setting up uh web hooks in  
04:45:49: modal. All right, now let's talk about  
04:45:51: how to take your directives that are  
04:45:53: inside of your IDE and then put them on  
04:45:56: the cloud, specifically on a service  
04:45:58: called modal.com. Now, in case you guys  
04:46:00: were unaware, modal is basically what's  
04:46:02: called serverless infrastructure, which  
04:46:04: is where they have these virtual servers  
04:46:07: that they spin up on demand on the fly  
04:46:09: every time that you want them to do  
04:46:11: something. What's really cool is most  
04:46:13: the time these serverless  
04:46:15: infrastructures sort of bend into one of  
04:46:17: two camps. One is they're like online  
04:46:20: all the time and then they're always  
04:46:21: charging you some usage per minute,  
04:46:24: second, week, month, whatever. The  
04:46:26: second is they're offline, but then they  
04:46:28: have to start. This is termed a cold  
04:46:30: start. And cold starts typically just  
04:46:32: take a lot of time and energy. So that  
04:46:34: if you have a flow that requires like  
04:46:36: instant reaction like a lot of the uh  
04:46:38: you know executions that you  
04:46:40: realistically want to host in the cloud  
04:46:41: um you know it takes a fair amount of  
04:46:43: time and you don't actually get it  
04:46:44: instantly. You get it after like a  
04:46:45: minute or two. So, what's really cool is  
04:46:47: modal solves both both of these  
04:46:48: problems. And what you can do is you can  
04:46:50: just take the execution scripts that you  
04:46:52: developed and then put them on modal so  
04:46:53: long as you have the right system prompt  
04:46:55: uh and have it work essentially  
04:46:56: instantaneously. So, what you do is you  
04:46:59: create an account on this service and I  
04:47:00: should note that I'm not affiliated with  
04:47:01: them. Do whatever you want. There are  
04:47:03: variety of other ways to do this, but  
04:47:04: this is definitely the simplest one.  
04:47:05: They give you a bunch of free credits,  
04:47:07: at least as of the time of this  
04:47:08: recording. And it's worth me noting that  
04:47:09: I've used Modal now for like at least  
04:47:11: two weeks, maybe three, and I've used 4  
04:47:14: cents out of the $5 available. Like  
04:47:16: realistically, you're not going to run  
04:47:17: out of this credit usage. Um, just as a  
04:47:19: test. I can't imagine how much $30 in  
04:47:22: free credits would take you. If you're  
04:47:23: just using like a Gentic Workflow for  
04:47:25: yourself or for like a small to-size  
04:47:27: business, this will take you really far.  
04:47:28: So, it's I mean, not free, but it's  
04:47:30: virtually costless. Once you're done,  
04:47:32: because we added all the information  
04:47:34: into our um cloud MD and our agents MD  
04:47:37: and and so on and so forth. If we want  
04:47:38: to push one of our flows to Modal, it's  
04:47:40: actually really easy. All we need to do  
04:47:42: is just get some authentication going  
04:47:43: and then obviously find the specific  
04:47:44: flow that we want. So I want to do the  
04:47:46: create proposal. I'm going to speak to  
04:47:48: my agent. Hey, I'd like to create a  
04:47:51: modal web hook for create_proposal MD. I  
04:47:54: basically just want to be able to  
04:47:56: replicate the functionality of that and  
04:47:58: just do it on the cloud instead.  
04:48:01: Get me a web hook  
04:48:03: URL for this.  
04:48:05: So now it's going to go through read my  
04:48:08: pre-existing system prompt which will  
04:48:10: include a bunch of information all about  
04:48:11: this. All right, this is almost done  
04:48:13: working through the modal web hook. As  
04:48:15: part of the system prompt, we set up  
04:48:17: what's called a web hooks.json. This is  
04:48:19: just a giant list of all of the  
04:48:20: different web hooks we have. I should  
04:48:22: note that before it was empty, so all we  
04:48:24: did is we just populated it. Now getting  
04:48:26: some information about the web hook that  
04:48:27: we set up and it looks like it was  
04:48:29: deployed successfully. So, we actually  
04:48:31: have a web hook now available at this  
04:48:34: URL here, nick- 90891-cloud-  
04:48:38: orchestrator-  
04:48:40: directive and so on and so forth. It  
04:48:42: looks like this takes all of our  
04:48:44: information in as follows. So, I mean  
04:48:47: like we could hardcode all of these. We  
04:48:49: could also have AI generate them. So,  
04:48:51: what I'm going to do is I'm actually  
04:48:52: just going to have it run. Okay, great.  
04:48:54: Could you run a brief example then  
04:48:56: return the URL when it's done? Okay. And  
04:48:58: it looks like at the end of it, we got  
04:49:00: our proposal which is right over here.  
04:49:02: Let's take a look and see how it did.  
04:49:04: Demo Corp AI automation pilot has some  
04:49:07: brief problem areas, has some brief  
04:49:10: solution areas. You guys remember we um  
04:49:12: built this earlier on in the course. And  
04:49:14: uh yeah, we now have essentially an  
04:49:17: automated proposal generator. Obviously,  
04:49:19: I wouldn't just like send an HTTP  
04:49:21: request to this with this information.  
04:49:22: This is a little bit short. I'm not  
04:49:24: going to call something demo corp, nor  
04:49:25: am I going to call uh manual data entry  
04:49:27: taking 20 hours per week. I'm going to  
04:49:28: go in a lot more detail. So just for the  
04:49:30: purposes of this, I'll say great, please  
04:49:33: update the documentation. Every time I  
04:49:34: call this, I want to make sure that the  
04:49:36: demo that I'm providing is really  
04:49:38: complete. So lengthen the paragraphs for  
04:49:41: the benefits and the solution  
04:49:42: statements. Make things longer in  
04:49:44: general and significantly more  
04:49:46: realistic. Then rerun the test.  
04:49:50: And opening up the new proposal. Let's  
04:49:53: see what this one looks like. Cool. I  
04:49:55: mean, we did write uh I guess it took my  
04:49:58: description of long to mean that we  
04:50:00: should write the title long, too. But  
04:50:03: these look significantly better. Check  
04:50:05: this out. We now have way more  
04:50:06: customized information here. Yeah, this  
04:50:09: is uh much much better. Awesome. So,  
04:50:11: that's great. So, what did we learn  
04:50:12: today? We learned that it is actually  
04:50:14: really easy to set up a web hook. All we  
04:50:15: really need to do is we just take our  
04:50:17: flow which um you know in our case was  
04:50:19: the creation of a proposal and then send  
04:50:21: it to our agent alongside um some system  
04:50:24: prompts that describe how to upload  
04:50:27: agentic workflows to the cloud.  
04:50:29: Obviously we need to add our  
04:50:30: documentation and so on and so forth.  
04:50:32: Really cool thing about modal is it's  
04:50:34: just one click takes like two seconds.  
04:50:36: You just go get your modal API key and  
04:50:38: then post it in here. It'll ask you to  
04:50:39: do so. In terms of how to create the  
04:50:41: token, you just click on that new token.  
04:50:42: The token secret is on the right. So  
04:50:44: that's what you copy and then you just  
04:50:45: paste it directly in here uh when it  
04:50:47: asks you for the modal token and boom,  
04:50:48: you're done. And yeah, that's how to do  
04:50:50: it with web hooks. Okay, now that we've  
04:50:51: set that up, let's actually go through  
04:50:53: setting up scheduled um triggers in  
04:50:55: modal as well. This is different from  
04:50:57: web hooks obviously because now we  
04:50:58: wanted to do so on a schedule, not just  
04:51:00: like based off of some event that comes  
04:51:01: in. So last time we did this with web  
04:51:03: hooks. Let me show you instead how to do  
04:51:04: it with some sort of schedule trigger.  
04:51:05: Maybe instead of running this via web  
04:51:07: hook call, what I want to do is I want  
04:51:08: to run a really simple workflow,  
04:51:10: probably some lead scraper or something  
04:51:12: like that, uh, every 5 minutes. So, what  
04:51:14: I'm going to do is I'm just going to  
04:51:15: tell it which thing I want to run and  
04:51:17: then how often I want to run it. And  
04:51:19: then everything baked into the system  
04:51:20: prompt is super easy and it'll just tell  
04:51:22: Modal to run this using what's called  
04:51:23: cron. Hey, could you send a welcome  
04:51:25: email to nickleclick.ai  
04:51:28: every 5 minutes and I want you to set up  
04:51:30: a modal cloud scheduled trigger to do  
04:51:33: this for me automatically.  
04:51:35: Cool. So now it's setting up the modal  
04:51:36: scheduled function to send the welcome  
04:51:38: email every 5 minutes. First it's going  
04:51:41: to check the existing schedule function  
04:51:42: pattern. Realizes that there is no  
04:51:45: schedule function pattern. So now it's  
04:51:46: just going to add some scheduled welcome  
04:51:47: emails. Cool. And now we have it.  
04:51:49: Scheduled welcome email is live.  
04:51:51: Schedule every 5 minutes. So that's what  
04:51:53: that looks like in cron. What we're  
04:51:55: going to do now is we're going to send.  
04:51:58: What's really cool is when you add them,  
04:52:00: you can actually see the the various  
04:52:02: schedule triggers. So, there's one here  
04:52:03: with a little clock icon that says every  
04:52:05: 5 minutes UTC. If I click on this,  
04:52:07: you'll see that there are no scheduled  
04:52:09: calls um that have gone out yet, but  
04:52:11: there is one in 1 minute and 9 seconds.  
04:52:13: And modal's cool because it actually  
04:52:15: allows you to run in between a schedule.  
04:52:17: So, you can just click on that little  
04:52:18: run now button, and when you click the  
04:52:20: run now button, it'll actually do the  
04:52:22: thing. You can see here that it took 3  
04:52:24: seconds to start up the server and 1.47  
04:52:27: seconds to actually send. Finally, if I  
04:52:30: go to the email address that I  
04:52:31: specified, you can see that it's  
04:52:32: actually sent the email. I mean, in this  
04:52:35: case, I just used a basic kind of  
04:52:36: onboarding email template, or rather, it  
04:52:38: created an basic onboarding email  
04:52:40: template. If I wanted to update this, I  
04:52:42: just tell my agent, hey, you know,  
04:52:44: change this so that it's like a welcome  
04:52:45: email from whatever to whatever. I could  
04:52:47: even give it a template. I could give  
04:52:49: whatever I wanted to.  
04:52:51: And just so that you guys could see it  
04:52:52: actually run, I'm just going to wait  
04:52:54: until this counter goes down to zero so  
04:52:55: you guys see what occurs when you set up  
04:52:57: a schedule. It's pretty straightforward.  
04:52:59: I mean, at the end of the day, since  
04:53:00: we're no longer using directives in our  
04:53:02: cloud um, you know, servers, all we're  
04:53:05: really doing here is we're just running  
04:53:06: a Python script, right? Because it's a  
04:53:08: Python script, these things execute  
04:53:09: nearly instantly. And that's really,  
04:53:10: really helpful rather than, you know,  
04:53:12: have to wonder about whether or not this  
04:53:14: thing is sent, rather than have to wait  
04:53:15: a really long startup time or send and  
04:53:18: receive things to or from Anthropic, we  
04:53:20: execute pretty quick. And as you see,  
04:53:22: because we just finished the previous  
04:53:24: query, I think within like 3 or 4  
04:53:25: minutes or something like that, we  
04:53:26: didn't even have to wind down the  
04:53:27: server. So, this one took 0 milliseconds  
04:53:28: and this execution time um was under 1  
04:53:31: second. So, I mean, we just did this  
04:53:33: whole thing in like less than a second  
04:53:34: flat, which is really cool. Heading back  
04:53:36: over here, you see that we now have the  
04:53:38: same email. This is your scheduled  
04:53:39: welcome email. And then we also have  
04:53:40: that 5-minute block that we talked  
04:53:42: about. Uh it's almost 1000 p.m. UTC,  
04:53:44: which is why that time says that. Cool.  
04:53:46: So, hopefully I've convinced you guys  
04:53:48: that setting up these sorts of web hook  
04:53:50: based triggers and schedule based  
04:53:51: triggers is actually really easy. That  
04:53:53: definitely isn't the bottleneck here.  
04:53:55: Before with uh no code platforms like  
04:53:57: Zapier and NADN and make.com and stuff  
04:53:59: like that, you had to be a lot more  
04:54:00: precise. Now you just get the URL and  
04:54:02: what can we do with the you know web  
04:54:03: hook URL? Well, now I can just connect  
04:54:05: it to whatever service I want. I could  
04:54:06: very easily set it up so that let's say  
04:54:08: when one of my prospects moves to the  
04:54:11: send proposal stage in my ClickUp CRM  
04:54:13: for instance, which by the way I can  
04:54:15: control completely um agentically using  
04:54:17: the agentic workflow that I set up  
04:54:19: previously as an example. uh you know we  
04:54:21: then trigger the web hook and maybe that  
04:54:24: occurs automatically as well. And so in  
04:54:26: this way we build a full endto-end  
04:54:27: completely automatic flow with web hook  
04:54:29: URLs that I could share within my  
04:54:30: organization or give to other people.  
04:54:32: And that's it. You now know how to build  
04:54:33: workflows that essentially run without  
04:54:35: you. The next step is to take this to  
04:54:37: the next level. Right now we've been  
04:54:38: running agents sequentially which just  
04:54:40: means one at a time. But imagine a  
04:54:42: future where you could actually run  
04:54:43: multiple agents simultaneously. That's  
04:54:45: what this next chapter is going to be  
04:54:46: about. It's going to be about  
04:54:47: parallelizing your work to multiply your  
04:54:49: output. Essentially, you're going to go  
04:54:50: from one employee to a whole team.  
04:54:52: Instead of doing things like this where  
04:54:54: you finish task one and then you do task  
04:54:56: two and then you do task three, we're  
04:54:58: actually going to in one fell swoop  
04:55:00: actually do tasks one, two, and three.  
04:55:02: Then we're just going to recombine the  
04:55:04: outputs. And we can um do this  
04:55:06: arbitrarily basically all the way to n  
04:55:08: service workers or threads or or or  
04:55:10: instances of an agent so long as you set  
04:55:12: up the environment right. Okay. Okay, so  
04:55:14: how do you set up multiple agents  
04:55:15: simultaneously? Well, spoiler alert, all  
04:55:18: you're really doing is just opening  
04:55:19: multiple terminal instances. Nothing  
04:55:21: super magical here. In VS Code or  
04:55:23: anti-gravity or any terminal based  
04:55:25: workflow, they all provide you the  
04:55:26: ability to open multiple panes, which  
04:55:28: allows you to run Gemini, GPT, Cloud  
04:55:30: Code, whatever the heck you want in  
04:55:32: different terminal windows. My favorite  
04:55:34: way to do this right now, and sort of my  
04:55:36: optimal, is three. I don't really work  
04:55:38: with more than three simultaneously  
04:55:39: unless we're doing long background tasks  
04:55:41: just because I find that my attention  
04:55:43: starts wavering and I start losing  
04:55:44: effectiveness at like remembering what  
04:55:46: the heck I'm doing. I always just do  
04:55:47: this vertically, left, middle, and  
04:55:48: right. I'll show you guys examples of  
04:55:50: all that stuff in a minute. So instead  
04:55:51: of just doing all of this within a  
04:55:53: single IDE, you can also be kind of  
04:55:54: smart about it. Uh most models are  
04:55:56: basically at approximately the same  
04:55:58: level right now. Like if this is three  
04:55:59: different models, they're basically all  
04:56:01: capping out at similar levels of  
04:56:02: intelligence. There are model  
04:56:03: differences between them, but most of  
04:56:04: them are trained in the same data,  
04:56:06: trained in similar ways, and so they're  
04:56:07: all kind of like reaching same levels  
04:56:09: right now. So if you find yourself with  
04:56:11: an IDE or a model, I should say like um  
04:56:13: Gemini within anti-gravity that is  
04:56:15: stricter rate limits or higher costs,  
04:56:17: instead of running like three instances  
04:56:19: of let's say Claude against each other,  
04:56:20: you could run one instance of Claude,  
04:56:22: then you could run one instance of  
04:56:23: Gemini, and you could run one instance  
04:56:24: of like GPT 5.2 or something. By doing  
04:56:27: all this stuff simultaneously, the  
04:56:29: frontier models will remain at a similar  
04:56:31: intelligence level. You're also going to  
04:56:32: get some slightly different ways to do  
04:56:34: work which can be beneficial for you if  
04:56:36: you're still in the building stage or  
04:56:37: the doing stage not necessarily running  
04:56:39: this sort of stuff um really high scale  
04:56:41: and then because we have the same  
04:56:42: initialization files agents MD cloud MD  
04:56:45: Gemini MD etc there's no functional  
04:56:47: difference for the model as a result  
04:56:49: instead of let's say like this is the  
04:56:51: the the threshold here where you know  
04:56:53: you pay $200 a month for the plan of  
04:56:57: claude I think this is like a the claude  
04:56:58: max plan or something like that and then  
04:56:59: you have to pay another I don't know  
04:57:01: $100 in credits after you hit this  
04:57:02: threshold, right? So, instead of being  
04:57:04: like this, what we basically do is we  
04:57:06: get to use three models instead and keep  
04:57:08: them below that threshold the entire  
04:57:09: time. I'm going to show you guys this  
04:57:10: and a bunch of others um in anti-gravity  
04:57:12: and then uh you know, have you guys run  
04:57:14: through practical ways to do this. Um,  
04:57:16: another thing I wanted to mention was  
04:57:17: practical limits on parallel agents. So,  
04:57:19: I find that in practice, two  
04:57:21: simultaneous agents is probably the  
04:57:23: average baseline that I like sticking  
04:57:25: at. Four agents is what I consider to be  
04:57:27: my soft max before things start getting  
04:57:28: counterproductive. Like it seems really  
04:57:30: cool when you have a million tabs open  
04:57:31: and all these agents are working on  
04:57:33: things. You feel like a superpower,  
04:57:34: right? But you're not actually being  
04:57:36: productive. You're just feeling  
04:57:37: productive. So instead of like being in  
04:57:39: a situation like that where most of the  
04:57:40: agent time will actually be spent  
04:57:42: waiting for you to like see the tab and  
04:57:43: like do something with it. I want you  
04:57:44: guys to know that feeling busy is not  
04:57:46: the same thing as actually being busy.  
04:57:48: Feeling productive is not the same thing  
04:57:49: as being productive. So this is a good  
04:57:51: way to just like help monitor that. I  
04:57:53: stick to three to four. Any more than  
04:57:55: that, you're probably just shooting  
04:57:56: yourself in the foot. Okay. Okay, so  
04:57:57: I've talked a little bit about this  
04:57:58: before, but you know, when you don't  
04:58:00: know how to build a workflow, you have a  
04:58:02: couple of approaches here. You can  
04:58:03: obviously just say, "Hey, can you build  
04:58:04: a workflow for me that does this?" And  
04:58:06: it's like a first pass. That's fine. But  
04:58:08: an advanced way to do it is actually  
04:58:09: say, "Hey, can you give me three  
04:58:10: approaches to build this thing?" What  
04:58:13: you do is you take those three  
04:58:14: approaches and you give them to either  
04:58:17: separate models or separate instances.  
04:58:20: Then what you do is once they're all  
04:58:21: done, you test to see which one scores  
04:58:23: the best. So maybe this one here scores  
04:58:25: 75%, this one here scores 84%, this one  
04:58:28: here scores 99%. What are you going to  
04:58:30: do? Obviously you're going to use this  
04:58:31: one, right? This one's the best  
04:58:33: combination of speed, cost, accuracy,  
04:58:34: and so on and so forth. In doing this,  
04:58:36: rather than having to um, you know, get  
04:58:38: a subpar solution and then slowly like  
04:58:41: make a bunch of changes to get to this  
04:58:42: point. You can actually just run these  
04:58:43: three agents in parallel and get three  
04:58:45: times the total search space instead of  
04:58:48: like manually going through this process  
04:58:50: one by one by one. I want you to imagine  
04:58:52: dividing this into three sections,  
04:58:53: having three of these little snakes go  
04:58:55: at the same time, which is just much,  
04:58:56: much faster, and then ultimately build  
04:58:58: something that is way better and way  
04:58:59: more scalable. How do you do this?  
04:59:01: Really straightforward. Just send that  
04:59:02: brief list of bullet points describing  
04:59:03: what you want to build to one agent.  
04:59:05: Then say, can you generate three  
04:59:06: distinct approaches with in-depth steps  
04:59:08: for each because I'm going to send this  
04:59:09: over to another model. Also, give me  
04:59:11: some pros and cons so I can understand  
04:59:12: the trade-offs up front. And you know,  
04:59:14: this will take you a few minutes up  
04:59:15: front, but it'll also save you a lot of  
04:59:16: time because if you go with a subpar  
04:59:18: solution initially, two or three hours  
04:59:20: down the line, you may still be working  
04:59:21: out some bugs or kinks or ways to make  
04:59:23: things faster. Whereas, if you just  
04:59:24: started with the right architecture  
04:59:25: right off the bat, you would have had  
04:59:26: all that stuff solved. Once you're done  
04:59:28: with that, it's pretty easy. Just open  
04:59:29: three separate instances of your agent,  
04:59:31: one for every approach. Give each agent  
04:59:33: a dedicated working folder. I like doing  
04:59:35: this in TMP. So I do like uh temporary  
04:59:37: folder SL1 temporary folder SL2  
04:59:39: temporary folder SL3 and actually just  
04:59:41: copy a prompt and I'll say hey you're  
04:59:43: currently working in this folder. The  
04:59:44: reason why is because we're creating  
04:59:46: three copies of a similar build with  
04:59:48: three different approaches. I want to do  
04:59:49: it here so that we're not, you know,  
04:59:51: crisscrossing files and so on and so  
04:59:52: forth. I'll show you guys a brief  
04:59:54: example what that looks like in a  
04:59:55: moment. Once you're done, you just  
04:59:56: review all three outputs side by side.  
04:59:58: Pick your favorite approach based off  
04:59:59: the actual results and the theoretical  
05:00:00: assumptions. Then you move the winning  
05:00:02: solution into DO or whatever it is that  
05:00:04: you're using, cloud skills and so on and  
05:00:06: so forth. Once it's moved over, you  
05:00:07: obviously also have to retest  
05:00:09: everything. And the reason why is  
05:00:10: because if you don't retest everything  
05:00:12: when the files are moved over, there may  
05:00:13: just be some issues with file references  
05:00:15: and that sort of thing. So this lets you  
05:00:18: do three builds in the same amount of  
05:00:19: time. Best one wins. You can obviously  
05:00:21: do exactly what I'm talking about, not  
05:00:22: just for the building, but also for the  
05:00:24: doing. You can run dozens of agents. And  
05:00:26: there are also things like background  
05:00:27: tasks which allow you to run agents sort  
05:00:29: of like in the background so that you  
05:00:31: could still do something else in  
05:00:32: parallel on top of it within a single  
05:00:34: thread. So I've talked a lot about  
05:00:36: building agentic workflows until now.  
05:00:38: But what I wanted to do here is just  
05:00:40: give you guys a brief demonstration of  
05:00:41: what using agentic workflows looks like  
05:00:43: in my day-to-day. So to be clear, I  
05:00:46: personally do a few things with my  
05:00:48: day-to-day. Number one is I run  
05:00:51: leftclick which is a growth/outbound  
05:00:53: AI enabled agency. We basically help you  
05:00:56: go to market for a product or service or  
05:00:59: scale up an existing product's outreach  
05:01:02: using AI and lead scraping mechanisms  
05:01:04: like you see here. We let you build  
05:01:06: completely autonomous outbound pipelines  
05:01:09: that don't rely on you or your team. You  
05:01:11: just end up with a bunch of booked  
05:01:13: meetings to sell your service in you or  
05:01:15: your salesperson's calendar. The other  
05:01:17: main thing I do is I create content like  
05:01:19: this. So I make YouTube videos. I write  
05:01:21: big long guides on how to, you know,  
05:01:23: build with agentic workflows and stuff  
05:01:25: like that. And so I'm constantly  
05:01:27: juggling between these two things. The  
05:01:29: third thing is I run a school community,  
05:01:32: actually a series of school communities.  
05:01:33: One called Maker School over here and  
05:01:35: one called Make Money with Make over  
05:01:37: here. And so I have a fair amount that I  
05:01:39: have to do on a daily basis as I'm sure  
05:01:41: you can imagine. You know, I have to do  
05:01:43: things for Leftclick that are kind of  
05:01:44: older school agency things. I need to  
05:01:47: create proposals and, you know, I need  
05:01:48: to scrape leads from my clients and  
05:01:50: onboard them and stuff like that. Then I  
05:01:51: have to do things for school like I have  
05:01:53: to manage replies. I have to, you know,  
05:01:55: send and receive DMs. I have to answer  
05:01:57: people's questions and so on and so  
05:01:59: forth. Plus, I have to do things for  
05:02:00: YouTube, like I have to create scripts  
05:02:02: and monitor YouTube for competitors and  
05:02:04: stuff like that. So, let me just give  
05:02:05: you a brief example of what me doing all  
05:02:07: three of these things simultaneously  
05:02:08: would look like in an Agentic workflow.  
05:02:10: So, the first thing I'm going to do is  
05:02:11: I'm going to have this run through  
05:02:13: basically my end to-end agency flow  
05:02:15: using a demo kickoff call transcript  
05:02:18: that uh I'm pulling up from my TMP  
05:02:20: folder. This is just plain text. Um, you  
05:02:22: know, I could pull this up from like  
05:02:23: Fireflies or any other like  
05:02:25: transcription tool if I wanted. I've  
05:02:27: just stored this plain text inside of  
05:02:28: TMP for simplicity. So, I'll say run the  
05:02:31: post kickoff flow for demo kickoff call  
05:02:34: transcript  
05:02:36: over here. you know, maybe I'm just  
05:02:38: getting started for the day and I want  
05:02:39: to see what sorts of YouTube outliers  
05:02:41: there are. Uh, with those YouTube  
05:02:42: outliers, I'm going to be able to  
05:02:44: ideulate a new video or something like  
05:02:45: that, come up with an outline and so on  
05:02:47: and so forth. So, I'll say run the  
05:02:49: YouTube outlier workflow and find me  
05:02:51: between 10 to 20 outliers for agentic  
05:02:54: workflows.  
05:02:56: This is what I'm going to be doing a  
05:02:59: fair amount today because, as you guys  
05:03:00: could see, I'm recording a video on  
05:03:02: agentic workflows and, you know, it's  
05:03:03: sort of like the hot topic now. And over  
05:03:05: here on the right, I'm obviously  
05:03:06: managing my school community. And so I  
05:03:08: built up some agentic workflows to help  
05:03:10: me pull relevant questions and comments  
05:03:12: and stuff like that from school. Pull  
05:03:15: the top 10 most recent school posts from  
05:03:18: Maker School. And so now I have these  
05:03:20: three clawed code instances basically  
05:03:23: running in the background for me. And  
05:03:24: all I'm going to do as somebody that is,  
05:03:26: you know, attempting to be economically  
05:03:28: productive is I'm just going to sit here  
05:03:29: and then watch over these and then, you  
05:03:32: know, add and chime in where necessary.  
05:03:34: So over here on the left hand side, it's  
05:03:36: asking me some simple questions. I'm  
05:03:38: just because I'm doing a demo here, say  
05:03:40: Nick at left  
05:03:43: uh leftclick.ai AI  
05:03:46: do the lead genen with modified query  
05:03:51: and then everything else too. Cool. Over  
05:03:55: here on the right hand side I see that  
05:03:56: we're done with my school post. So now I  
05:03:58: have a bunch of information about this.  
05:04:01: Looks like Suam recently posted a cold  
05:04:03: email guide. So I'm going to say Suam's  
05:04:05: cold email guide. Run me through his  
05:04:07: step by step. This over here in the  
05:04:10: middle is using the tube labab API which  
05:04:12: is part of one of the agentic workflows  
05:04:13: that I put together to go and then  
05:04:15: scrape me a bunch of um outliers. So one  
05:04:17: of our members was kind enough to share  
05:04:20: with us how he made $500,000 in about 6  
05:04:23: months or so using instantly which is a  
05:04:25: cold email tool and then a lot of the  
05:04:27: same um you know principles that we talk  
05:04:29: about here. So he ran through and  
05:04:30: actually provided a ton of info and I  
05:04:32: mean I'm just curious what that looks  
05:04:33: like. I could of course use the school  
05:04:35: UI. I could log into school and then  
05:04:37: scroll through the post myself and stuff  
05:04:38: like that. But I set up an agentic  
05:04:40: workflow to do this. Why? Because it  
05:04:42: becomes really easy to do really cool  
05:04:44: things with agentic workflows inside of  
05:04:46: school. Like hypothetically, I get a lot  
05:04:48: of questions, right? And what I did was  
05:04:50: I built a rag or retrieval augmented  
05:04:53: generation uh tool that essentially  
05:04:55: looks every time somebody asks a  
05:04:56: question to see if something similar has  
05:04:58: been answered in the community before.  
05:05:00: If so, it actually goes and it gives me  
05:05:01: the link. Then what I can do is as I  
05:05:03: respond to them, I could just copy the  
05:05:05: link over and say, "By the way, if you  
05:05:06: want a much more detailed explanation,  
05:05:08: check out this post or so on and so  
05:05:10: forth." So, what I'm seeing here on the  
05:05:11: cross niche outlier sheet is it's  
05:05:13: looking like we're not including all um  
05:05:16: AI based uh results. And that's probably  
05:05:19: because realistically there just aren't  
05:05:21: any competitors for agentic workflows  
05:05:24: yet because I've kind of coined the  
05:05:25: term. So, that's great for me. What I'm  
05:05:27: going to do now is I'm just going to  
05:05:28: have it run some sort of outlier scraper  
05:05:30: for terms like AI agents instead. That  
05:05:32: should give me a fair amount of stuff to  
05:05:34: work with. Anyway, on the right hand  
05:05:36: side here, now we're done with this.  
05:05:38: This is great.  
05:05:40: Fantastic.  
05:05:42: Comment extremely valuable guide. So,  
05:05:46: what I'm going to do is use my school  
05:05:48: system to go through this, get all of  
05:05:51: the post ID and stuff like that, and  
05:05:53: then actually send a comment on that  
05:05:55: saying, you know, excellent or extremely  
05:05:58: valuable guide. If I open this up and  
05:05:59: then scroll all the way down to the  
05:06:00: bottom, you can see that I just left a  
05:06:02: comment here saying super valuable  
05:06:03: guide. And so, I basically get to  
05:06:05: communicate with school, which is a  
05:06:06: service that previously required a  
05:06:07: graphical user interface, just entirely  
05:06:09: through an agentic workflow instead,  
05:06:11: which is fantastic. I'm sure future  
05:06:14: versions of Aentic Workflows will be  
05:06:15: able to recreate the UX any flavor or  
05:06:18: way that I want, but for now, this is  
05:06:20: pretty cool for me. I don't mind. Over  
05:06:21: on the left hand side, you can see we  
05:06:23: came up with 15 leads. The reason why I  
05:06:25: did 15 and not say 1,500 just because it  
05:06:28: was trying to be mindful of my token  
05:06:29: costs, knew that I was doing this as  
05:06:31: part of a demo. Um, we've actually  
05:06:33: already gone through and and got what I  
05:06:35: think is nine emails, which is cool. And  
05:06:37: then after that, if we scroll a little  
05:06:39: bit further down, this actually went  
05:06:40: through and uploaded leads to the  
05:06:42: campaign, which is pretty sweet. It then  
05:06:44: even added things to a knowledge base  
05:06:45: and then even went as far as to send a  
05:06:47: summary email to my client, which in  
05:06:49: this case I just used my own email for  
05:06:51: um basically telling them, hey, you  
05:06:52: know, we're done with the campaign and  
05:06:53: so on and so forth. What's really cool  
05:06:54: is it also gave me three links. So, I'm  
05:06:56: just going to open up these three links,  
05:06:58: which take me directly to my cold email  
05:07:00: tool um where I can actually see the um  
05:07:02: campaigns that it came up with. So, this  
05:07:05: might sound crazy, but hear me out. I  
05:07:06: want to generate 50,000 in revenue for  
05:07:07: company name in the next 90 days. If I  
05:07:09: don't hit that number, I'll work for  
05:07:10: free until I do. How? LinkedIn thought  
05:07:12: leadership. I run a company. We spent  
05:07:14: six years helping 200 partners at  
05:07:15: professional services firms turn  
05:07:17: LinkedIn into a revenue channel.  
05:07:18: Counting firms, consultancies, financial  
05:07:20: adviserss, executive coaches. Our  
05:07:22: clients regularly close 50K deals  
05:07:23: directly from LinkedIn. Some see 3 to  
05:07:25: 10x follower growth and most start  
05:07:27: getting two to three inbound leads per  
05:07:28: month once the content machine is  
05:07:29: running. I know this is bold, but I'm  
05:07:31: confident we could do something similar  
05:07:32: for you when you open to a quick chat.  
05:07:33: No pressure, just a conversation. I  
05:07:35: mean, this is just one of three  
05:07:36: campaigns with two split tests each.  
05:07:39: Obviously, while this copy is uh I would  
05:07:41: consider very punchy and probably  
05:07:43: [snorts] higher quality than like 80 85%  
05:07:45: of all of the copy that other people are  
05:07:47: running for campaigns like this. I'm  
05:07:48: going to like take a look at the copy,  
05:07:49: maybe make some minor changes before I  
05:07:51: actually go through the process. Um, but  
05:07:52: it's still pretty great, right? I did  
05:07:54: notice that there was an issue here  
05:07:55: where the Gmail MCP was not  
05:07:57: authenticated. So, um, because I was  
05:07:59: showing you guys how to authenticate  
05:08:00: MCPS in another video here, it was a  
05:08:03: demo that I did a few hours ago. um it  
05:08:05: unauthenticated my MCP. Obviously, if  
05:08:07: this occurs, you need to reauthenticate,  
05:08:09: right? So, what I would do in this case  
05:08:11: would be reauthenticate MCP and then it  
05:08:13: would just go through that process  
05:08:14: together. On the right hand side here,  
05:08:15: I'm going to say something like, hey,  
05:08:18: what sorts of questions have been asked  
05:08:20: in the last 24 hours that I can answer.  
05:08:23: So now I'm going to get a list of  
05:08:24: questions the right hand side here.  
05:08:26: That's pretty straightforward. While I'm  
05:08:27: doing this, I'm reauthenticating my  
05:08:29: Gmail MCP. That's going to trigger OOTH,  
05:08:31: which is pretty cool. in the middle  
05:08:32: here. We're still scraping more  
05:08:34: outliers.  
05:08:35: Would you give me the highest priority  
05:08:37: ones  
05:08:40: over here? We now need to restart the  
05:08:42: Gmail MCP server. So, I'm just going to  
05:08:44: restart cloud code. The new O flow  
05:08:46: should capture a refresh token. Let me  
05:08:47: know once you've completed the browser  
05:08:48: authentication and then I will start  
05:08:50: again. Cool. So, I'm going to do is I'll  
05:08:51: go new. Just going to go /mcp.  
05:08:58: We'll say off  
05:09:01: my MCP, off my Gmail MCP.  
05:09:05: Over here on the right hand side, you  
05:09:07: see some people have asked some  
05:09:08: questions. So, Emil's asked some  
05:09:09: questions about client delivery when  
05:09:11: you're offering a lead genen system. For  
05:09:12: how long should you sign up the client  
05:09:13: for and how long can you keep on  
05:09:15: providing new leads for the company? For  
05:09:16: how long are you guys typically running  
05:09:17: campaigns for clients? On average, I run  
05:09:20: campaigns for a minimum of 90 days. I  
05:09:22: didn't used to do this, but I found that  
05:09:24: 90 days was sort of the sweet spot as it  
05:09:26: typically takes some stopping and  
05:09:28: starting before you figure out the right  
05:09:30: offer combination and the right lead  
05:09:32: targeting. When I started, I went  
05:09:34: month-to-month entirely. I'd probably  
05:09:35: recommend that in your case just to keep  
05:09:37: friction low, but hopefully this helps  
05:09:39: give you an understanding of the various  
05:09:41: ways that you could put something like  
05:09:43: this together. And we have another  
05:09:44: question here about 400 bucks. Well,  
05:09:47: first off, nice job on the 400 bucks.  
05:09:49: the JSS score tanking is hard to hear.  
05:09:53: My recommendation would be to send him a  
05:09:55: message  
05:09:57: letting him know that immediately after  
05:10:00: you finished your contract, you had a  
05:10:01: massive JSS dump. This is something  
05:10:03: about Upwork. And softly implying that  
05:10:06: this will unfortunately have serious  
05:10:08: consequences as to your ability to get  
05:10:10: future work. I would also ask him if  
05:10:12: there's something or anything that you  
05:10:13: can do to improve that job success  
05:10:16: score, whether it's going back and  
05:10:17: providing free or additional work etc.  
05:10:20: It looks like on the third he put some  
05:10:22: copy together. So I'm just going to say  
05:10:23: show me the copy.  
05:10:26: Cool. And now this is going to go  
05:10:27: through top to bottom and then send that  
05:10:28: info. What's cool is this also formats  
05:10:30: my text for me. So I can just dump all  
05:10:32: this in. It's now going to authenticate.  
05:10:35: So I'm just going to head over to my  
05:10:36: email. Looks like it's successful. So I  
05:10:39: can go back here. This looks pretty  
05:10:41: solid. I would probably  
05:10:43: remove the  
05:10:54: just because this doesn't offer a lot of  
05:10:55: value. If you work with  
05:11:00: somebody in your niche, I would  
05:11:03: recommend that.  
05:11:11: This is usually considered positive  
05:11:14: social proof. The would you be open to a  
05:11:16: 15-minute call about this as the last  
05:11:19: question is a little weak. I would  
05:11:22: probably be hyper specific with the  
05:11:25: times that I'm asking for. I.e. could  
05:11:28: you do?  
05:11:36: Okay, over here on the left hand side we  
05:11:37: have the Gmail MCP. So I'll just say  
05:11:40: send me  
05:11:42: a hello email to nicholas@gmail.com.  
05:11:47: Over here we have the output of our  
05:11:49: agent. So let's take a look at this.  
05:11:52: Looks like it's saying that a lot of  
05:11:53: these are related to ICE agents, which  
05:11:57: is sort of a political thing that's  
05:11:58: going on right now, which is why we're  
05:12:00: getting these outliers. Obviously,  
05:12:02: that's not, you know, that's not what  
05:12:03: I'm going to be doing. I really care  
05:12:04: about looking for those outliers, but I  
05:12:06: do see some of these are more agent  
05:12:08: related. So, a agents that actually work  
05:12:09: the pattern anthropic just revealed. We  
05:12:11: have the thumbnail right over here.  
05:12:14: That's cool. Google Workspace Studio  
05:12:16: between these two. Sam Alman looking  
05:12:18: quite menacing.  
05:12:20: These are pretty funny, honestly. Uh,  
05:12:22: cool. Yeah. So, I have some reasonable  
05:12:23: outliers here, which is nice. Um, you  
05:12:25: know, I'm probably not going to be able  
05:12:26: to do the political ones, and I'm not  
05:12:27: really making content like that or  
05:12:29: talking head, so I can avoid those. But  
05:12:30: hopefully you guys see that, you know,  
05:12:31: now I have some outliers that I could  
05:12:33: work with that have just been released  
05:12:34: in the last few days. Um, but, you know,  
05:12:36: maybe I could start modeling my content  
05:12:37: around or something like that.  
05:12:38: Meanwhile, the MCP now works. So, we did  
05:12:40: fix that. And then I've also sent three  
05:12:43: um messages within school. So, I'm just  
05:12:44: going to take a little peek at that.  
05:12:47: Cool. also just sent that just sent that  
05:12:51: and then right over here just said that  
05:12:54: and you can see it's also formatted my  
05:12:55: text for me and stuff like that. Okay,  
05:12:57: so I don't do this because I think any  
05:12:59: of these three particular ones that I'm  
05:13:00: running are super powerful or super  
05:13:02: incredible or whatever, but these are  
05:13:03: just things that I had to do today, you  
05:13:04: know, and I just figured I would run  
05:13:06: through them with you guys. Um, this is  
05:13:08: like a practical look at this the  
05:13:09: day-to-day work that I do within my  
05:13:10: Agentic Workflow IDE. Um, and hopefully  
05:13:13: you guys see how this is a very simple  
05:13:15: and easy way to like multiply your  
05:13:16: leverage, right? I mean, I just did like  
05:13:18: a whole endto-end workflow for uh,  
05:13:20: admittedly a demo client, but a demo  
05:13:22: client nonetheless on the lefth hand  
05:13:24: side. In the middle, I ran like outlier  
05:13:26: detector and on the right hand side, I  
05:13:28: even interacted and engaged with school  
05:13:30: posts much faster than I could do  
05:13:32: manually. Um, that auto automatically  
05:13:34: formatted my text, found like good  
05:13:36: questions for me to answer and so on and  
05:13:38: so forth. You guys can use Agentic  
05:13:40: Workflows in your ID in the exact same  
05:13:42: way for whatever the knowledge work is  
05:13:44: that you need to do. Whether you're  
05:13:45: copyrighting campaigns, whether you're  
05:13:47: scraping leads, whether you're just like  
05:13:49: organizing your CRM or adding things to  
05:13:50: a record, like it is now entirely  
05:13:52: possible. And I hope you guys also see  
05:13:54: that there is a split between the  
05:13:56: building of a workflow and then the  
05:13:58: using of the workflow. The building is  
05:14:00: something you do once and then the using  
05:14:01: is an opportunity to make a return on  
05:14:03: investment on the building time over and  
05:14:05: over and over and over again basically  
05:14:06: every day. I don't really think it's a  
05:14:08: far cry to say that most people could  
05:14:10: probably automate 50% or more of their  
05:14:12: day-to-day work using flows like this  
05:14:14: and at minimum at least make it 50% more  
05:14:17: enjoyable or easier to do. So, next I  
05:14:19: want to talk a little bit about sub  
05:14:20: agents. Why sub agents? Because context  
05:14:23: windows fill up really, really quickly.  
05:14:26: Most people don't realize this, but  
05:14:28: current models have a context window of  
05:14:30: around 200,000 to around 1 million  
05:14:32: tokens in certain instances. And that  
05:14:35: sounds like a lot, but when you add  
05:14:36: tools, all of this context disappears  
05:14:39: much faster than you would think.  
05:14:41: Specifically, detail oriented tasks burn  
05:14:44: through context really quickly because  
05:14:45: of that loop that I was telling you  
05:14:47: about. Debugging burns through context  
05:14:49: very quickly because of the loop I was  
05:14:51: talking to you about. Any sort of MCPs  
05:14:53: burn through context really quickly. And  
05:14:55: before you know it, half of your whole  
05:14:57: context window of let's say 500,000  
05:14:59: tokens or something is filled with  
05:15:01: intermediate garbage that significantly  
05:15:02: reduces the probability of a successful  
05:15:05: output. Now, this phenomenon where  
05:15:07: there's a bunch of garbage in your  
05:15:08: context window and that leads to poor  
05:15:10: quality outputs is called context  
05:15:12: pollution. And pollution is essentially  
05:15:15: where that intermediate memory, that  
05:15:16: sort of midterm memory that I talked  
05:15:18: about way back at the beginning of the  
05:15:19: course, gets cluttered with a bunch of  
05:15:21: irrelevant noise. Now, scientists have  
05:15:24: been working with these models for quite  
05:15:26: a while. As I may have mentioned to you  
05:15:28: at some point in the past, AI models  
05:15:29: these days are more grown than they are  
05:15:31: built. And so, it's very much like a  
05:15:33: natural phenomenon that we are testing.  
05:15:35: And what they've found is consecutively  
05:15:37: across thousands and thousands and  
05:15:39: thousands of tests, the more tokens in a  
05:15:41: context window, typically the poorer the  
05:15:45: quality is. And the relationship looks  
05:15:47: something like this.  
05:15:49: And the reason it looks like this is  
05:15:51: because over here on the very left hand  
05:15:53: side, you probably have zero tokens,  
05:15:54: right? And so if it's fresh and you ask  
05:15:57: it to do something with no context or  
05:15:58: whatever, it'll do an okay job. If you  
05:16:00: add a bunch of context and you tell it,  
05:16:03: hey, you know, I'd like you to do this.  
05:16:04: Here are a couple of examples of past  
05:16:06: instances of this run correctly. Uh  
05:16:08: here's a bunch of context. Here's a  
05:16:09: bunch of links and whatever. Performance  
05:16:11: actually goes up in the short term. What  
05:16:13: you'll notice is as you go on and on and  
05:16:15: on and you start filling it with more,  
05:16:17: you know, irrelevant garbage and  
05:16:18: whatnot, performance and quality and  
05:16:20: outputs go down a lot. Now, back in the  
05:16:22: day with GPT2 and GPT3 when I was  
05:16:24: starting 1 second copy in my content  
05:16:26: writing business, you know, this was  
05:16:28: super super important and it was so  
05:16:30: important that I actually trained all of  
05:16:31: my writers not to use more than 256  
05:16:34: tokens at a time. So, imagine that we  
05:16:36: had to stick under 256 tokens with our  
05:16:39: prompt. Essentially, if we went any over  
05:16:41: that, we found um quality went off a  
05:16:43: cliff. In our case, now we can use  
05:16:44: significantly more than 256 tokens.  
05:16:46: Obviously, this point here is probably  
05:16:48: somewhere closer to like 10k or so, not  
05:16:50: 256. So, we're sort of blessed in that  
05:16:52: way. But still, there is that  
05:16:54: relationship between more stuff in the  
05:16:55: context window and then poor quality.  
05:16:57: So, we need to make sure that uh you  
05:17:00: know, if all else is held equal, we try  
05:17:01: and minimize the amount of tokens in our  
05:17:03: context as much as possible. Now that we  
05:17:04: understand that, onto sub aents. The way  
05:17:06: that sub agents solve this is through  
05:17:08: isolation of context. Now the idea is in  
05:17:12: order for something to be a sub aent and  
05:17:14: not a part of the main agent, it gets  
05:17:16: its own fresh clean context window to  
05:17:19: work in. So all you do with a sub agent  
05:17:22: is basically you give it a task. You let  
05:17:25: it do all the messy work in its own  
05:17:27: space and then you return only the  
05:17:29: relevant findings. So just as a quick  
05:17:32: little demonstration here, let's say  
05:17:34: this is a chat back and forth with you  
05:17:37: and you know your agent. So this is you  
05:17:41: over here. This is your agent over here.  
05:17:45: Any every time you ask it something, it  
05:17:47: sends something back and so on and so  
05:17:48: forth. Imagine what happens every time  
05:17:51: you send a call. Essentially what is  
05:17:53: occurring is we stack up all of these.  
05:17:56: And so our total context, if you think  
05:17:57: about it, is that block up there plus  
05:18:00: this block over here plus that block  
05:18:02: over here plus that block over here plus  
05:18:04: that block over here. So how many blocks  
05:18:06: is this? We're just counting. That's  
05:18:08: five blocks. And let's say everyone's a  
05:18:10: thousand words. You're actually sending  
05:18:11: like a,000 words. So what that means is  
05:18:13: on the next query, what we're doing is  
05:18:14: we're sending a total of five blocks of  
05:18:17: context plus the thing that we asked. So  
05:18:19: maybe 6,000 in total. What sub aents  
05:18:21: allow you to do is instead of doing this  
05:18:24: um you know having this 1,000 here,  
05:18:26: let's pretend that this over here is  
05:18:27: actually a sub aent loop. What we do is  
05:18:29: we actually just eliminate this  
05:18:30: completely. Okay, and then we eliminate  
05:18:33: that completely. And so what ends up  
05:18:34: happening is basically the model instead  
05:18:37: of storing the results directly in the  
05:18:39: context, okay, only stores the outputs  
05:18:42: of that response. So all we're really  
05:18:45: doing to make a long story short is we  
05:18:46: ask the sub agent to do something. It  
05:18:48: deals with all of that stuff sort of  
05:18:50: internally in its own head and then just  
05:18:52: spits us out a brief summary plus the  
05:18:54: results that we asked for. If you guys  
05:18:56: are keen, you'll notice that this is  
05:18:57: very similar to how reasoning tokens get  
05:18:59: discarded after use to keep the total  
05:19:01: token countdown. Remember how there's  
05:19:03: that sort of like thinking tab and you  
05:19:06: can open up the thinking tab if you want  
05:19:07: to see what's kind of going on under the  
05:19:09: hood. Well, those tokens aren't actually  
05:19:10: added to what I talked about here. Those  
05:19:12: tokens disappear. So, it's the exact  
05:19:13: same thing. Whether it's reasoning,  
05:19:15: whether it's sub aents, both of these  
05:19:16: strategies are meant to reduce the total  
05:19:18: amount of stuff and garbage polluting  
05:19:20: the context window. And the data backs  
05:19:22: this up. Anthropic, a company that sort  
05:19:24: of not coined sub aents, but is  
05:19:26: definitely the leading force behind them  
05:19:28: with clawed code. Um, it ran a test  
05:19:30: where opus was the lead and then opus  
05:19:32: essentially controlled a bunch of sub  
05:19:34: aents and had those sub aents do a  
05:19:36: variety of smaller tasks before  
05:19:38: reporting back their findings. And it  
05:19:39: found that it outperformed single agent  
05:19:41: opus by over 90% on research. based  
05:19:44: tasks. Now, I should note that's  
05:19:46: research, right? Not all tasks are  
05:19:48: research related. Obviously, research  
05:19:50: involves a ton of tokens. And so, sub  
05:19:52: agents here obviously did way better  
05:19:54: than they probably do on most other  
05:19:55: tasks relative to, you know, the  
05:19:57: standard. But, there are some  
05:19:58: circumstances where sub agents do  
05:20:00: perform significantly better even in  
05:20:02: day-to-day use. And that's why I'm  
05:20:03: talking about it. You'll know that I uh  
05:20:06: I really haven't really given a crap  
05:20:07: about sub agents or anything like that.  
05:20:09: This is a very recent phenomenon for me.  
05:20:10: People have been talking about sub  
05:20:11: agents for the better part of the last  
05:20:12: two years. And every time they are like,  
05:20:14: "Nick, why aren't you using sub aents or  
05:20:15: whatever?" I'm always like, "Because  
05:20:16: it's pointless." Like sub agents as an  
05:20:18: architectural addition just complicate  
05:20:21: things. They don't actually make things  
05:20:22: easier. Models for the most part can  
05:20:24: handle tasks on their own. It's okay.  
05:20:25: You don't need to like, you know, try  
05:20:26: and develop some big fancy framework.  
05:20:29: Well, model intelligence has gotten to  
05:20:30: the point where we can actually make use  
05:20:32: of these things now. So long as you're  
05:20:33: nuanced and kind of smart about how you  
05:20:35: do it. So the catch between this is  
05:20:38: there's implementation complexity  
05:20:39: because you are now inserting your own  
05:20:40: biases and how you think the model  
05:20:42: should operate. Then you're also  
05:20:43: compounding errors. What do I mean by  
05:20:45: compounding errors? I mean, you know, if  
05:20:47: you think about it, there's a step here  
05:20:48: where in order for my parent agent to  
05:20:50: send something off to a child or sub  
05:20:52: agent, it needs to summarize what it is  
05:20:54: that it wants the sub agent to do. And  
05:20:56: so that right there is a step. And that  
05:20:58: step might be like 99% accurate. But as  
05:21:00: we know, if you have a bunch of things  
05:21:01: that are 99% accurate, if you add enough  
05:21:05: steps into the process, eventually that  
05:21:07: turns out into something that is much  
05:21:09: less than 99% accurate, right? It might  
05:21:11: be like uh I think my example was 99.9%  
05:21:14: stretched out over a,000 tasks was 36%  
05:21:16: accuracy at the end of it. So you know  
05:21:18: the more uh steps you have like  
05:21:20: summarization steps sending to this this  
05:21:22: does some summarization sends back the  
05:21:24: more area you're inserting in the  
05:21:25: process and the higher the variability  
05:21:26: is. So basically what you need to do is  
05:21:28: you just need to find a situation where  
05:21:30: the added error as a result of the  
05:21:32: additional steps is outweighed  
05:21:34: essentially by the beneficial effect on  
05:21:36: the context. And there's no real  
05:21:38: non-trivial way to know this right off  
05:21:40: the top of your head. Like you need to  
05:21:41: test this. You need to try this. Now  
05:21:43: since I've tested this and trying this,  
05:21:45: my recommendation is to stick to two sub  
05:21:48: aent types for now. And there's in in  
05:21:49: particular just two that I'm going to  
05:21:51: talk about. Before I tell you what those  
05:21:52: two are, the other two big wins from sub  
05:21:55: agents are there's context management.  
05:21:57: Your main agent will stay super clean  
05:21:58: and it'll only have things that are  
05:22:00: highly relevant to what it is that we  
05:22:01: want. So let's say you delegate to a  
05:22:03: bunch of sub aents that have MCP access.  
05:22:05: Those sub aents are the ones that load  
05:22:07: up all the context and other MCP. Then  
05:22:09: they do the job and then they report  
05:22:10: back. If your sub aents are atomic  
05:22:12: enough, obviously we can do that over  
05:22:13: and over and over again and we can  
05:22:14: actually make some real headway without  
05:22:15: polluting the context window. The second  
05:22:17: is parallelization. So sub aents can  
05:22:19: actually run all simultaneously. What  
05:22:21: you'll find when you delegate to sub  
05:22:22: agents like I'll show you later is a  
05:22:25: single agent can spawn multiple and then  
05:22:28: those multiple basically all run on  
05:22:29: their own and report back whenever  
05:22:31: they're individually finished. So if  
05:22:33: you've ever seen, you know, Gemini or  
05:22:35: Claude sort of do research, typically  
05:22:37: what'll occur is it'll spin up, you  
05:22:39: know, three or four research sub aents  
05:22:42: because that's native to their  
05:22:43: architecture and they're basically just  
05:22:45: going to wait until all three or four of  
05:22:48: these are completed. But these don't  
05:22:50: occur top down. It's not like this  
05:22:51: finishes first, this finishes second,  
05:22:53: this finishes third, this finishes  
05:22:54: fourth. These are all individual  
05:22:56: processes. So this one might finish  
05:22:58: first and report back. This one could  
05:23:00: finish second, this one could finish  
05:23:01: third, and this one could finish fourth.  
05:23:03: It's a very interesting phenomenon that  
05:23:04: you guys have probably seen but not  
05:23:06: fully understood where that comes from  
05:23:07: yet. A good example of that  
05:23:08: parallelization is if you want to scrape  
05:23:10: a bunch of leads. I do tons of lead  
05:23:11: scraping, hence why it's always my  
05:23:12: example. But um you know, you don't need  
05:23:14: to scrape all these one by one. You  
05:23:16: don't need to scrape, let's say, 30,000  
05:23:17: independently through some big serial  
05:23:19: thing. You can actually just have your  
05:23:21: parent agent, okay, spin up three sub  
05:23:23: aents and maybe every sub agent itself  
05:23:26: uses some form of parallelization to do  
05:23:28: a task. And so now what you're doing,  
05:23:30: and I know this sounds really fancy,  
05:23:32: you're probably like, does it actually  
05:23:33: work? Now what you're doing is you're  
05:23:34: basically just cutting the total amount  
05:23:35: of time it takes to do this thing down.  
05:23:37: And then what what occurs is once these  
05:23:39: are all done, okay, if you kind of like  
05:23:40: check mark these, they report their  
05:23:42: results back to the main agent. Then the  
05:23:44: main agent's task is really just  
05:23:45: consolidating these, putting them  
05:23:47: together, which if you think about it  
05:23:48: like the act of I don't know stitching  
05:23:49: together three lists of things is a lot  
05:23:51: easier of a task to ask a parent agent  
05:23:53: than you know actually going through the  
05:23:54: orchestration of scraping that many  
05:23:56: leads. If something previously takes 3  
05:23:57: hours sequentially with the spin up, the  
05:24:00: uh scraping and then the wind down. This  
05:24:02: might only take 30 minutes in parallel  
05:24:03: because you are consolidating those  
05:24:05: fixed costs uh in terms of spin up and  
05:24:07: then wind down and then your parent  
05:24:09: agent just gets the results. In terms of  
05:24:10: like the technical and logistical bits  
05:24:12: where sub aents live, they're defined as  
05:24:14: markdown files. Exact same thing as the  
05:24:16: directives. Nothing really different  
05:24:17: here. Uh in clawed code specifically,  
05:24:20: they're included/  
05:24:22: aents. So this is a tople folder with  
05:24:25: another folder underneath it. And then  
05:24:26: if you want to go global as in have that  
05:24:28: accessible like across your entire  
05:24:30: project directory, then you put it in  
05:24:31: your current directory. Claude/ aents.  
05:24:34: The disambiguation there isn't super  
05:24:36: important. If you want sub agents to  
05:24:38: only have access to a specific workspace  
05:24:40: or project, this is how you do it. But  
05:24:41: if you wanted to have access to  
05:24:42: everything, uh then you'd put it over  
05:24:44: here and that way sub agents can work  
05:24:45: across your workspaces. Now, other  
05:24:47: agenda coding tools do follow similar  
05:24:49: patterns. There is no consensus, at  
05:24:51: least not as of the time of this  
05:24:52: recording, how Gemini is organizing its  
05:24:54: sub aents, how Codeex and so on and so  
05:24:56: forth are organizing their sub aents.  
05:24:57: But rest assured, everybody has their  
05:24:59: own little framework and it's all about  
05:25:00: like the system prompt, right? You can  
05:25:02: absolutely just have these models spin  
05:25:03: up the equivalent of the claw code  
05:25:05: version of sub aents. It's just a matter  
05:25:07: of doing a little bit more heavy lifting  
05:25:08: up front. The anatomy of a sub aent file  
05:25:11: right now is again you have the name  
05:25:14: then you'll have the description and  
05:25:15: then also really important you have the  
05:25:17: permissions. So which tools the sub aent  
05:25:20: can access tools in our do framework for  
05:25:22: instance are going to be directives and  
05:25:23: executions. After that, you have the  
05:25:25: system prompt. And just like we do  
05:25:27: system prompts across the entire  
05:25:29: workspace, we also have a sub aent  
05:25:31: specific system prompts. Um, you guys  
05:25:34: don't actually need to know any of this.  
05:25:35: I just say make me a sub agent that does  
05:25:37: X, Y, and Z. And this sort of stuff is  
05:25:39: just baked into um at least the Claude  
05:25:41: family of models as of the time of this  
05:25:42: recording. It'll most certainly be baked  
05:25:44: into other ones as well. So yeah, you  
05:25:45: don't need to create these yourself. You  
05:25:46: can just ask the agent to do it. Um  
05:25:48: here's an example prompt. literally just  
05:25:50: create a sub agent called document that  
05:25:52: gets called after every workflow to  
05:25:53: update to consolidate changes in the  
05:25:55: directive and execution scripts. It'll  
05:25:57: go through a process of creating the  
05:25:58: thing. I'm going to show you what that  
05:25:59: looks like in practice and yeah, you're  
05:26:01: done. Your agent will generate a file,  
05:26:03: put in the correct folder, and then it's  
05:26:04: immediately available. Talk about  
05:26:06: something recursive, huh? It's agents  
05:26:07: creating agents. I should note that  
05:26:09: agents can create the definition of an  
05:26:11: agent, but an agent can only spawn an a  
05:26:14: sub aent. Sub agents can't spawn more  
05:26:16: sub agents themselves. And this is like  
05:26:17: a memory constraint. They don't want sub  
05:26:19: aents to be able to spawn more sub aents  
05:26:21: to be able to spawn more sub aents  
05:26:22: because essentially what you're going to  
05:26:23: do is you're going to end up with a  
05:26:25: situation where you know your parent  
05:26:26: agent spins up two sub aents your sub  
05:26:29: aents spin up two sub aents your two sub  
05:26:31: aents spin up two more sub aents and so  
05:26:33: on and so on and so on and so forth  
05:26:35: until basically your I don't know CPU is  
05:26:37: as hot as the surface of the sun not to  
05:26:39: mention you know some safety and  
05:26:40: security concerns and stuff like that so  
05:26:43: um really what happens is we sort of  
05:26:45: limit it to if we just cut all this  
05:26:47: stuff out these too. And so your parent  
05:26:49: agent can spin up however many sub aents  
05:26:51: it wants, but they all report back to  
05:26:52: that parent agent. So what are those two  
05:26:54: sub aents that I talked about that I  
05:26:56: personally find genuinely useful?  
05:26:58: They're not required to be clear. You  
05:27:00: can absolutely use DO and whatever other  
05:27:02: framework um it is that you want to  
05:27:03: build with without sub aents. But I  
05:27:05: found that these actually improve the  
05:27:07: accuracy and quality of my execution  
05:27:08: scripts and they are a joy to use as  
05:27:10: opposed to something that is you know  
05:27:11: laborious and time inensive and so on  
05:27:13: and so forth. The first is the reviewer  
05:27:16: sub agent. So a main issue with building  
05:27:19: directive orchestration executions or  
05:27:21: cloud skills is your orchestrator will  
05:27:23: write a bunch of code. And so if you ask  
05:27:25: it, hey, how's this code looking? It's  
05:27:27: going to be biased towards thinking that  
05:27:29: that code is correct because it just,  
05:27:30: you know, probably ran it a bunch of  
05:27:31: times and it sees some correct runs in  
05:27:33: its history. The unfortunate thing is  
05:27:35: that's kind of like asking somebody to  
05:27:36: read their own essay right after writing  
05:27:38: it. Um, any experienced writers will  
05:27:40: know what you want to do is you want to  
05:27:41: take a little bit of a break. You want  
05:27:42: to like take a deep breath, go sit down  
05:27:44: somewhere else, you know, like do not  
05:27:46: look or read that essay. Come back to it  
05:27:47: maybe an hour or two later because when  
05:27:49: you come back to it an hour or two  
05:27:50: later, your mind is no longer polluted  
05:27:52: by all the biases and your own flavoring  
05:27:55: of thought surrounding, you know, how  
05:27:56: good that essay is. When you come back  
05:27:58: to it, you basically come back to it  
05:27:59: with fresh eyes and you can tell by  
05:28:01: definition whether or not it is a good  
05:28:02: essay or a bad essay, whether it's some  
05:28:04: of your good best work or maybe some  
05:28:05: sort of mediocre work. And so reviewer  
05:28:07: sub agents work basically the exact same  
05:28:09: way. Instead of the orchestrator which  
05:28:12: remembers all its decisions, what we do  
05:28:13: is we give it to something that can  
05:28:14: actually see a lot more clearly. What  
05:28:16: occurs is the reviewer gets loaded with  
05:28:18: completely fresh context which is just  
05:28:20: the directives and just the executions  
05:28:22: that we built. We then ask it to  
05:28:24: evaluate the script purely on its  
05:28:26: quality. In short, it acts like a second  
05:28:28: pair of eyes. We give it no context  
05:28:30: about what this thing is for. And the  
05:28:31: idea is it needs to like determine the  
05:28:33: context through the code. Meaning the  
05:28:34: code has to be documented. It has to be  
05:28:36: pretty straightforward to understand and  
05:28:38: read. Has to be written simply. And then  
05:28:39: if you think about it, if it has no  
05:28:40: context whatsoever, it'll be able to  
05:28:41: look at it and be like, hm, that seems  
05:28:43: kind of weird because most other code  
05:28:44: like this will probably have some error  
05:28:46: handling, but this one doesn't. I think  
05:28:48: this should probably build in some error  
05:28:49: handling and then it can provide  
05:28:50: suggestions back to the main agent who  
05:28:52: is sort of biased to actually go and and  
05:28:54: build the thing. How do you do this?  
05:28:55: Well, your main agent just calls sub  
05:28:57: agents automatically when you define  
05:28:58: them in the system prompt. So in  
05:29:00: agents.mmd, after you create any script,  
05:29:02: use the reviewer sub agent to check for  
05:29:04: its quality. That's a totally okay thing  
05:29:06: to write somewhere in your agents.MG um  
05:29:08: G or system prompt. Um while it won't be  
05:29:10: 100% accurate, aka it's not going to do  
05:29:12: this every single time, you know, it  
05:29:14: will do this up until the context window  
05:29:15: gets polluted enough, which is a pretty  
05:29:17: reasonable thing uh to do. And I find  
05:29:19: just having this probably improves my  
05:29:20: accuracy a good 5 10%. In addition, you  
05:29:23: can obviously also ask the model to do  
05:29:24: things manually. So you could say, "Hey,  
05:29:26: uh that's great. Call the reviewer sub  
05:29:28: agent, just make sure everything's  
05:29:29: okay." Or, "Call our reviewer and ensure  
05:29:31: that you know this is fine. Hey, I want  
05:29:33: you to make some edits after you're done  
05:29:34: making those edits. Ping reviewer,  
05:29:36: double check that it's okay. If it's  
05:29:37: okay, then give me the thumbs up. These  
05:29:39: are all just flavors and variants of  
05:29:40: things that you can ask your agent.  
05:29:42: Obviously, your mileage varies and it's  
05:29:44: up to you. The second sub aent that I  
05:29:46: recommend building is a document sub  
05:29:48: agent. So, this one updates directives  
05:29:51: based on what the system has learned  
05:29:52: over time. You know, after your workflow  
05:29:54: self anneal for a while inside of your  
05:29:56: IDE, sometimes the agent will forget to  
05:29:58: update. That's just because, as I  
05:30:00: mentioned, it has a ton of context and  
05:30:02: so it's going to forget some of the  
05:30:03: things that you mentioned initially in  
05:30:04: the system prompt like, "Hey, I want you  
05:30:05: to update your thing." So, what the  
05:30:07: document does is it just reviews scripts  
05:30:09: and then it updates the directives to  
05:30:10: reflect their current behavior. A lot of  
05:30:12: the time in practice, what happens is  
05:30:14: you'll have some um issues with your  
05:30:16: script and so the agent will go and  
05:30:17: update the script over and over and over  
05:30:19: and over again. And then the directive  
05:30:21: will be untouched despite the fact that  
05:30:22: you spent all this time um updating the  
05:30:24: script. And then on a fresh instance of  
05:30:26: a new agent, maybe tomorrow or the next  
05:30:28: day, you try running the workflow and  
05:30:29: then it goes like, "hm, this is weird. I  
05:30:31: tried running the execution script, but  
05:30:32: it looks like it wants different  
05:30:33: parameters. What's going on here? I I  
05:30:35: followed the directive." And then, you  
05:30:37: know, there's a big debugging step and  
05:30:38: then it fixes it. But it takes like, I  
05:30:40: don't know, 5 or 10 minutes. Well, just  
05:30:41: call your document sub agent and have it  
05:30:43: just rectify everything right then and  
05:30:44: there instead. What you do is you give  
05:30:46: it read access to all files and then  
05:30:48: write access just to your directives.  
05:30:50: So, it can read through all of your  
05:30:51: execution scripts, but it can't make any  
05:30:52: updates to that. And then it can update  
05:30:54: the directives to match the execution  
05:30:56: scripts. This is pretty simple, too.  
05:30:58: Create a sub aent whose job is reviewing  
05:31:00: scripts and updating documentation so  
05:31:01: everything aligns and just call it  
05:31:02: whenever you update a script. Anytime  
05:31:04: you make a change, your main flow will  
05:31:06: then call the document sub agent. Just  
05:31:07: do some review. The document will review  
05:31:09: the scripts and summarize the changes  
05:31:11: automatically since it's sort of like  
05:31:12: trained to do so with its prompt. Now,  
05:31:14: as I mentioned before, the really cool  
05:31:16: thing about sub aents is they don't just  
05:31:17: work in sequence. Um, they can work in  
05:31:19: parallel. What I mean by parallel? Well,  
05:31:21: just like opening new tabs, sub aents  
05:31:23: let you run tasks in parallel. Just like  
05:31:25: opening three or four instances of  
05:31:26: Gemini and then asking each to do a  
05:31:28: different thing. You could just run  
05:31:29: three or four sub agents within a single  
05:31:31: window. Now, your parent agent has the  
05:31:34: ability to run multiple agents what's  
05:31:35: called synchronously and then wait for  
05:31:36: the results of all of them. And so, as  
05:31:38: I've talked to you guys many times, you  
05:31:40: know, if you have some parent A, this  
05:31:42: can now whip up C, B, and then D, and  
05:31:45: then it can combine the results into  
05:31:47: some result E, loop that back around,  
05:31:49: and then just use that result to, you  
05:31:50: know, proceed instead of doing  
05:31:52: everything sequentially. Because this  
05:31:54: this can take a fair amount of time,  
05:31:56: right? If every single step here takes,  
05:31:59: I don't know, 20 minutes, that's 20  
05:32:00: minutes here, 20 minutes there, 20  
05:32:02: minutes there. Why not just like  
05:32:03: consolidate them all and then only have  
05:32:04: one 20-minut step? Parallelization is  
05:32:07: probably one of the freest wins in  
05:32:08: computing to be honest because most of  
05:32:09: your CPU cores and GPU cores are  
05:32:11: literally just left idle 99% of the  
05:32:13: time. This is a good way that you can  
05:32:14: make use of them. When you do this, the  
05:32:16: context window will also stay really  
05:32:17: small. It's usually under a couple  
05:32:18: thousand tokens in the main thread to do  
05:32:19: the thing. And then every sub aent works  
05:32:22: independently without cluttering your  
05:32:23: primary workspace, assuming that you  
05:32:24: know you you you give it the right  
05:32:26: system prompt so that it can do that.  
05:32:28: Hey, I want you to store intermediate  
05:32:30: research results in, you know,  
05:32:32: tmp/ressearch instead of polluting my uh  
05:32:35: parent agents context window. Now,  
05:32:37: obviously when you give sub agents  
05:32:38: autonomy, okay, and keep in mind that  
05:32:40: that autonomy is also given by the  
05:32:43: parent agent. So, it's like you're  
05:32:44: multiplying autonomies just like you're  
05:32:45: multiplying probabilities. Obviously,  
05:32:47: safety becomes pretty important, right?  
05:32:49: And so, what I recommend is giving each  
05:32:51: sub agent different tool access. You  
05:32:53: need to specifically say you can only do  
05:32:55: X, Y, or Z. So, your guardrails have to  
05:32:58: be a lot stronger than let's say the  
05:32:59: guardrails on, I don't know, some other  
05:33:01: sort of agent. I'm just going to draw my  
05:33:04: little bowling ball analogy over here,  
05:33:06: but it is very much one of those things.  
05:33:07: You do need to have some sort of  
05:33:08: guardrail. I think of it like giving my  
05:33:10: intern, you know, readonly access to my  
05:33:13: production database. Production database  
05:33:14: being like my live actual database that,  
05:33:17: you know, people are really using. I  
05:33:18: don't know. You know, I've had some  
05:33:20: issues in the past where people that  
05:33:21: aren't very skilled come into my  
05:33:22: organization and then they start  
05:33:23: screwing around with databases they  
05:33:25: probably shouldn't be touching and then  
05:33:26: I don't know, they drop my tables and  
05:33:28: then all of a sudden everything's all  
05:33:29: crappy. So, you know, an SOP that I and  
05:33:31: I think a lot of other people probably  
05:33:33: use is, hey, you know, if you're new to  
05:33:34: my organization, you only get read  
05:33:36: access to things. You can only like look  
05:33:37: at it. If you want to make changes, ask  
05:33:39: me. Well, sub agents are very, very  
05:33:40: similar. And this is obviously an  
05:33:42: architectural pattern that we're  
05:33:43: borrowing from hierarchical  
05:33:44: organizations. This is called lease  
05:33:45: privilege. It's where you give each  
05:33:46: agent only the resources it needs for a  
05:33:49: specific job. If you think about the  
05:33:50: document sub aent that I was telling you  
05:33:52: about, the document sub agent only  
05:33:53: really needs to be able to read the  
05:33:55: executions. It doesn't need to be able  
05:33:57: to write them. The only thing it needs  
05:33:59: to be able to write, which is sort of  
05:34:00: like the really scary thing is the  
05:34:02: directives. And so in that way, we  
05:34:04: ensure that it's only really ever, hey,  
05:34:06: information from executions goes into  
05:34:08: directives, not really the other way  
05:34:09: around. I could of course create like a  
05:34:11: hypers specialized optimized coding  
05:34:13: agent which has a bunch of context about  
05:34:14: the best ways to do code. Then maybe I  
05:34:16: give that read access to my directives  
05:34:18: and write access to my executions or  
05:34:19: something. A couple of other limitations  
05:34:21: about sub agents that I want to talk  
05:34:22: about because I think they're really  
05:34:24: shiny and they're fun and everybody  
05:34:25: likes being the top of some big  
05:34:27: organization. They add some overhead and  
05:34:29: they also add some latency. So spinning  
05:34:31: up a sub agent and getting some results  
05:34:33: back does take extra time is not instant  
05:34:35: unfortunately because you are literally  
05:34:36: spinning up like a separate entity. So  
05:34:39: for simple tasks, your main agent will  
05:34:40: almost always be faster just doing it  
05:34:42: directly. And so like most simple tasks,  
05:34:43: it'll just do the main thread. I'm not  
05:34:45: going to spin up a sub agent to do my  
05:34:46: research for me. Even though some of  
05:34:48: that is just built into the way that  
05:34:49: these agents now work, uh I'm just going  
05:34:51: to be like, hey, you know, look up this  
05:34:52: and get me the results. I'm not going to  
05:34:54: be like, spin up the research sub agent  
05:34:56: and then feed that into the  
05:34:57: decision-making sub aent and so on and  
05:34:59: so forth because I think that's just  
05:35:01: kind of BS. So yeah, I don't really use  
05:35:03: sub aents for most things. The time cost  
05:35:04: often isn't worth it. I'll only really  
05:35:06: use it in the context of like a hypersp  
05:35:08: specific framework like directive  
05:35:09: orchestration execution like cloud  
05:35:11: skills and so on and so forth. So let me  
05:35:13: show you how to actually create one of  
05:35:14: these sub aents. I'm using sub aents in  
05:35:16: cloud code just because cloud code is  
05:35:18: currently like the defined sub aent  
05:35:21: pattern. So I could just say hey make me  
05:35:22: a sub aent it'll do it. I want you guys  
05:35:24: to know that you can build sub aents or  
05:35:25: at least things that are analogous to  
05:35:27: sub aents in whatever model uh structure  
05:35:30: you want. All a sub aent really is  
05:35:32: doesn't have a formal definition yet,  
05:35:33: but I'm going to define it is something  
05:35:35: that does not have context aside from  
05:35:38: the input that it is given by a parent  
05:35:40: agent. So, I want to create a reviewer  
05:35:42: sub agent, right? In order to create a  
05:35:43: reviewer sub aent, I'm just going to  
05:35:44: like voice dump my um my requirements  
05:35:47: directly in. Hi, I'd like to create a  
05:35:49: reviewer sub aent. The whole idea behind  
05:35:51: the reviewer sub agent is it will look  
05:35:53: at the execution scripts that another  
05:35:55: agent develops and it will look at it  
05:35:57: with totally fresh eyes and just  
05:35:58: determine if this is done in as  
05:36:00: effectively or efficiently a manner as  
05:36:02: humanly possible. It will then provide  
05:36:04: instructions to the top level agent  
05:36:06: which can then take that guidance and  
05:36:08: review to improve the quality of the  
05:36:10: build.  
05:36:11: I'm just going to feed all that in  
05:36:13: directly. It's then going to do some  
05:36:15: tinkering and some thinking.  
05:36:17: Then it's going to ask me a bunch of  
05:36:18: questions. My main goal here is I want  
05:36:21: you to be able to call the sub agent as  
05:36:23: required. So set it up in whatever way  
05:36:25: allows you to do the calling.  
05:36:28: I also want you to check everything. All  
05:36:31: of the above. The output format should  
05:36:33: just be whatever is most amendable or  
05:36:36: convenient for you since you are going  
05:36:38: to be the one that is calling it. Okay.  
05:36:39: Funnily enough, I ran into a limit um  
05:36:42: earlier when I tried finishing that. So,  
05:36:44: I went and I added um what's called  
05:36:46: additional credits, which is pretty easy  
05:36:48: to do essentially in Claude. Anyway,  
05:36:50: your current session eventually hits a  
05:36:52: cap. I'm using the Claude Max plan, so I  
05:36:54: have a fair amount of usage, but yeah, I  
05:36:56: eventually do run into some sort of  
05:36:57: issue. Uh and so what I did is I enabled  
05:37:00: the extra usage toggle and then I said,  
05:37:02: "Hey, just use this to pay for any extra  
05:37:03: usage whenever I do." I set a very low  
05:37:06: spending cap because I very rarely run  
05:37:07: into sessions. It's my fault for just  
05:37:09: doing like 20 demos today. Anyway, um  
05:37:12: after that I then had this run on a  
05:37:14: test. So I said, "Hey, run the reviewer  
05:37:16: on scrape_cross_nicheoutliers.  
05:37:19: py." So it's now actually running a  
05:37:21: test. It's saying, "Hey, read the  
05:37:23: directive first. Understand the  
05:37:24: criteria. Read the script completely.  
05:37:25: Produce the structure of view output  
05:37:26: specified in the directive. Be  
05:37:28: ruthlessly honest and specific." And so  
05:37:30: this thing is only going to have read  
05:37:32: functionality. And it since found me a  
05:37:34: bunch of information that I could use to  
05:37:35: improve it. script is functional but a  
05:37:37: significant efficiency issues. Excessive  
05:37:39: API calls, no rate limiting and  
05:37:41: potential quota exhaustion. Here they  
05:37:43: are. Wonderful, wonderful, wonderful.  
05:37:46: This is really cool. An O squared string  
05:37:48: matching for 175 niche terms. Full  
05:37:50: transcript load only 8K characters used.  
05:37:53: So now we can do basically a fix. I'll  
05:37:55: say great, try this on the create  
05:37:59: proposal  
05:38:01: flow. I'm doing this because um the  
05:38:03: create proposal flow is pretty solid,  
05:38:05: but it's also quite simple and I  
05:38:06: actually want to see how this would work  
05:38:08: doing a review on create proposal. It's  
05:38:10: now spinning up base sub agent. Now the  
05:38:12: way that sub aents work at least in  
05:38:13: cloud code is there's a defined  
05:38:15: structure. They live include/comands  
05:38:19: inside of the commands is the sub aent  
05:38:21: tool spec. As you see, we haven't  
05:38:23: actually done that. There is no um you  
05:38:25: know reviewer sub aent here. That's  
05:38:27: because the model typically defaults  
05:38:29: just doing this in the directive  
05:38:30: orchestration execution framework way by  
05:38:32: just like having a directive called hey  
05:38:34: you're the agent but we want to do this  
05:38:36: in claude format specifically just  
05:38:38: because the probability of this working  
05:38:40: is a lot higher on like totally fresh u  
05:38:42: roles so what I'm going to say is  
05:38:45: excellent work before you proceed create  
05:38:48: an actual claude command for this right  
05:38:51: now you are using a directive to spawn  
05:38:52: the sub aent but I instead want you to  
05:38:54: search through theclaw pod folder and  
05:38:58: see how it should be done. After you're  
05:39:00: done, update the execution script with  
05:39:04: the reviewer sub agents thoughts.  
05:39:10: This is fantastic. It found a bunch of  
05:39:12: discordant issues that probably  
05:39:14: significantly increased error rate. Now  
05:39:16: we have correct paths. Everything here  
05:39:18: is much more on board with uh uh the  
05:39:21: directive. And we've even gone as far as  
05:39:23: actually creating the claude command. So  
05:39:26: this is fantastic. What I will now say  
05:39:27: is great test create_proposal.  
05:39:30: py with the demo sales call transcript  
05:39:33: intmp. It found it. Now what it's doing  
05:39:36: is generating all of the information.  
05:39:38: This is the same thing that I ran in an  
05:39:40: earlier demo in case you guys are aware.  
05:39:42: It's going to use a plausible email.  
05:39:44: Create the JSON input and then test.  
05:39:46: Cool. And this actually significantly  
05:39:48: improved the functioning of create  
05:39:50: proposal. Previously we had to do some  
05:39:52: some polling. Now what it does is it  
05:39:54: waits for the document to be ready  
05:39:55: before returning the link. Um so we  
05:39:58: actually have this um ready and we've  
05:40:00: significantly improved the effectiveness  
05:40:02: of the script as well. It's a welcome  
05:40:04: surprise. I wasn't actually expecting to  
05:40:06: improve this. Looks like the one issue  
05:40:08: here is it just titled this with the  
05:40:10: company name which made that spill over  
05:40:12: to a second line. I can obviously change  
05:40:13: that anytime I want. But yeah, the rest  
05:40:16: of this looks pretty solid. I'm not  
05:40:17: seeing any major issues here. So  
05:40:19: fantastic work. Hopefully it's clear.  
05:40:21: You can use a reviewer sub agent and a  
05:40:24: document sub agent to significantly  
05:40:26: increase the effectiveness of not just  
05:40:27: the DO framework but your agentic  
05:40:30: workflows in general. And that's that.  
05:40:32: Thank you very much for making it  
05:40:34: through the agentic workflows course. If  
05:40:35: you guys have made it through the many,  
05:40:37: many hours of content, you are now in a  
05:40:39: position where you can use and leverage  
05:40:40: aic workflows better than probably 99.9%  
05:40:44: of the rest of the population. The skill  
05:40:45: set that you guys have is  
05:40:46: extraordinarily in demand right now.  
05:40:48: Whether you want to use it for your own  
05:40:50: business, maybe a software business,  
05:40:52: maybe an agency or service business, an  
05:40:54: ecom business, or in a consulting  
05:40:56: business to help other people with their  
05:40:57: businesses through Agentic Workflows.  
05:40:59: So, whatever category you're in, take  
05:41:01: the knowledge that you've learned today  
05:41:03: and use it to produce great things and  
05:41:04: accelerate the transition to a more  
05:41:06: efficient economy. If you guys like this  
05:41:08: sort of thing and want to learn how to  
05:41:09: implement agentic workflows in other  
05:41:10: people's businesses, please check out  
05:41:12: Maker School. It's my 90-day  
05:41:14: accountability roadmap that guarantees  
05:41:16: you your first customer for AI  
05:41:18: automation or agentic workflow  
05:41:20: consulting businesses. That means that  
05:41:21: by the end of the 90-day period, you  
05:41:23: will have your first customer or I'll  
05:41:25: give you your money back. More  
05:41:26: generally, it's just a great community.  
05:41:27: We have over 2,000 fantastically  
05:41:29: talented and capable people in there.  
05:41:31: It'd be great to add another. Aside from  
05:41:33: that, want to thank you from the bottom  
05:41:34: of my heart for making it to the end of  
05:41:35: the video. Have a lovely rest of the day  
05:41:37: and best of luck implementing Agentic  
05:41:39: workflows.  
