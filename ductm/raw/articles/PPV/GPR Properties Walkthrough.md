## Giới thiệu

Now we've done the organization protocols and the differentiation between goals project 13s. Now let's walk through some of the properties. These are the basic components of the GPR database. And I'm going to do it in the master view because we can see the property title. So starting with the basics and then we'll talk about the custom optional ones.

---

## Basic Properties

### Type

First is type. This as you just saw in my restructuring of the entries. This is an automatic property. Anything that you enter in GPR as a default if it's at the top level it's just a new entry it's automatically a goal. It becomes a project when it becomes the sub item of a parent item. So the projects are the sub items with dates and routines are sub items without dates. As you can see here the routines don't have dates. So the type is handled automatically and it's reflecting the structure that you have in the GPR database.

### Title

So title is plenty obvious like as mentioned earlier you want it to be concrete measurable and for routines you want the routine titles to be phrased as an action.

### Status

Status is straightforward. I do want to mention something. If you're putting something on hold like if it's a project that you said you know what I don't have bandwidth for it. I just don't have the capacity. You can put it on hold temporarily. But if it's something that you said I want to shove this project indefinitely then it's better to archive it than to delete it. Because if a project has a lot of links and information in the page, deleting it, you're removing it from your system altogether. So it's better to archive something that you want to shove indefinitely than to delete it. So use on hold and archived wisely.

### Priority

Next is priority. Very straightforward. You can sort your GPR entries from top priority, medium to low priority.

### Category

And category is also very straightforward. What category is this goal, project, routine fitting in? Is it personal, work or connection?

### Lưu ý về Priority và Category

Topic and work. So you can see the note here that it says the priority and category you assign to goal only. Now this doesn't mean that the projects and routines don't need priority and category. The reason why there's a note here is because the system has automations that automatically handles. It's going to transfer the priority and topic of the goal over to its sub items.

So that anytime when you make changes for instance you just want to change you're changing this goals category from work to personal and the system automatically updates that for all of its sub items and if you want to change the priority for instance you have a read five books this year right and this low priority and then you decide that you know what this is pretty important I want it to be a medium priority and let's see the sub items will all be medium priority so this is updated automatically so that you don't need to do it and this update is top down.

So that means when you update the goals priority and category, it transfer that to the projects and routines. But if you want to say change the priority for a sub items like but this routine really is not an important because this is a leisure reads. It's not like a study. I want to still like bump this lower to low. You can do that and this won't affect the top level. So this transfer is top down not bottom up. So I just want to clarify that.

### Dates

Next is dates. Now dates is for projects and goals only and this is a complete by date. So a lot of times when you're entering a new project or new goal, you're thinking, you know what, I don't really know when I want to start working on this goal or project. Then you don't need to enter it as a date range. You can simply enter it as a complete by date. I want to finish this by the end of February. Then you will enter a date here.

It's important to have that date in your system. And it really is, especially on the sub items level. That's what separate projects from routines which you're doing more casually and it's not that strict of a time frame. So make sure for goals and projects at least have an end date if not a date range.

---

## Auto Data Property

Now auto data is a very important property here and it's one of the places where the system does the quiet work for you. This is a summary and this is a formula property that pulls together key signals from each entry so you can see the status of that item at a glance. You don't type into auto data. You don't type in there at all because everything is already set. And instead, this property reads other properties you'll have already set. And the goal is to give you a quick dashboard line for each GPR item.

So we can see that from the goal level you can see that this goal contains three sub items and two of them are active and what are the active projects and you can click into these are clickable and then you see from the goal level this is counting all of the actions and topics and neurobbits and people organizations connected to every layer of this whole GPR structure. So it's rolling everything up at the goal level and it also has some really useful information that you can see.

So when you get to the project level because these are more you know layered say you can see the structure this is under a goal and then how many actions to do and of the four actions that you have in your action list one have no due date. So this is a really helpful signal that you know oh there's one that doesn't have a due date I'm going to go in and see which one I'm going to add that and how many are done and topics.

And then for this one this is a project and this one's a whole but this one has no action. So you can see all kinds of these alerts across the system that they have no dates. Like this goal had no date. Yes, it doesn't have a date. And this goal has no dates, no projects, routines, and no actions.

And another very useful one is it shows you if something is behind schedule. So this one, the original complete by date. You want to get it done by October 17th. Now it's obviously way past that. So you're going to see behind schedule. So when you see this alert, you're going to go in and readjust the day or put something on hold.

So this is a very very very helpful property and this property inform your decisions and it gives you a fast signal so you know where to look and what to adjust without needing to open the page or build your own formulas.

---

## Quick Add Buttons

And now we're going to talk about the quick app buttons before we talk about topics. So the quick app buttons, we have two here, the add action and add neurobits. At neurobbit, I just went singular.

These buttons are there so you can create the right kind of linked pages without leaving GPR and they do two important things.

One is reduce friction. So you're in this project for instance and you click this and it creates a new page linking to the GPR applying the category for you and it fills the day ads today but you can change that later and you never left GPR. You're still in the context of GPR. So one these kind of button properties they reduce friction. You can add new actions or the next note or resource in one click from the GPR row without switching context to actions or neurobbits database.

And two it protects the relationship as you just saw that the relation to this project is set automatically your GPR entry so that applies to both actions and neurobbits if you create a new bit it's going to link back to this project as well and you also saw that it also carries over the category of this project or goal or routine.

So when you click add action. It creates a new action that's already linked to the GPR entry and it carries the category over for you and you can then fill in other details in the new action as you normally would and that applies to the add neurobbit button as well.

---

## Topics Auto Property

So next we'll talk about topics auto. It looks like a very simple property but this is one of the most useful properties in the entire GPR database. This is another formula property that does topic aggregation for you.

This property reveals that across all of the actions and neurobbits linked to this goal, what topics are actually in play. You don't need to tag topics directly from GPR. Instead, it looks at the topics that are already attached to the actions and neurobbits and then roll those up to the goal or project or routine. So what it's doing is that it's quietly collecting those topics relations for you and it's showing you the themes that are relevant for this project or for this goal.

At the goal level, the topic auto property acts like an umbrella over all of the related projects and routines.

### Topics Direct vs Topics Auto

So for instance, let's open a page here. So if you want more direct and intentional control over the connection between a goal and a topic, you can directly tag an existing topic in this topic direct property.

So you use auto as the reference, right? Sometimes you may have like for instance this one, you have no direct topics, but they're all being distracted from all of the actions and neurobbits linked to this goal and projects and routines. So you can use the topics auto as a reference to decide if you want to use direct link for more curated tagging.

So you can then select okay so I have communication operations and personal development here and I want to directly tag one from these one. So I have more direct link then you can click link existing and you can find that topic.

Note that if you directly tag a topic that isn't yet appearing in the topics auto, it will pull into that topic automatically. For instance, so we have communication operations, personal development, but you want to link let's say entertainment just as example. You see as you directly tag entertainment, entertainment is being pulled into the topics auto too. So what that means is the topics auto remains the most complete view of all topics relation for that GPR entry.

---

## Relational Properties

So this I just want to demonstrate and the rest of the relational properties are pretty straightforward. The life aspirations is linking directly to goal and people organization and also in the page you see here that we also have you can link actions you can link neurobits you can link people and remembrance.

So remembrance is something that you do when you click notable. It's going to link this entry GPR entry to the annual collection like the 2025 collection or if you do it next year it's going to be linked to the 2026 collection and we'll talk about that more in the following sessions.

So that is the walkthrough of the basic properties of GPR.

---

## Segments Property

Next I'll hand it over to August to talk about the segments property and how it works across GPR.

So a lot of questions come up when we have the spaces or categories which are then rolled up into the spaces dashboard where you have personal, you have work and you have connections. Some people want other customized views or customized dashboards. Beyond those those are meant to be very high level slices. Personal and work is very universal. Connections will be relevant to some people. If you don't need connections, you don't need to use it. If it's adding too much overlap with the others, that's optional. Everybody, unless you're retired, has some kind of personal and work and you just organize between those two. If connections is something like you want a family dashboard or a social circle dashboard, that's there for you.

But sometimes you want narrower slices, not these big broad categories of life. And that's where segments comes in. It lets you create very narrow slices.

For those from the older system, this might relate to some of the pillar dashboards you did. We found very few people did the pillar dashboards, but some people did and they missed that. This is where you would create your own dashboard on whatever slice narrow or wide is of value to you.

### Ví dụ sử dụng Segments

A good example that often comes up is people who are running multiple companies. So work, if you just run one company, you have one career, you know, employment with a larger company, you might run that all in your work dashboard. But what if you have multiple companies and you want separate dashboards for each or it could be anything like that.

And this is where you will select segments. And segments will be across all the GPRs, which means goals, projects, routines. It'll be across topics. And this is a selector property. You'll define the segments. They're by default listed as segment one or segment two. But you'll name it company A, company B, or whatever the slice of life you want to create dashboards for.

The whole purpose of this is so you can filter for that slice of your life. Whether it's a one of multiple companies or any other slice. If you have a hobby that's incredibly important to you, you could create a slice for that. These segments will indicate goals, projects, routines, topics that are pertinent to that slice or that company or that element of your life. And then with that, you can create the dashboard you want focused on just that.

So it's that simple. It's just a selector property that lets you zero in on a slice of life that is important to you that's narrower than people or work or connections.

So that concludes the property walk.