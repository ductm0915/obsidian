

## Introduction

Behind the scene, all of these action related views in focus zone are powered by a single actions database. This is the underlying source. Think of it as the engine room.

Most days you don't need to come here at all. Focus zone is where you work. So you only come here to the source view when you need to customize a new high usage view or to do bulk configuration and deep auditing of the entire database. For instance, checking and removing sample data, get the complete master table or test filters.

I'll show you how to remove sample data after we do a quick property walkthrough here in our source view. So, first of all, source view to get there, we're in focus zone. What you do is open navigation and click actions. That will take you to the source actions database. And to emphasize again, for everyday work, you stay in focus zone. You do not need to come to the source view.

---

## Properties Overview

Now properties organized into four functional groups. There are the basic properties, relations properties, automations and helper properties and long-term value properties.

### Basic Properties

So August have walked us through a lot of the properties category you're very familiar with in life aspirations and GPR.

**Due date** - this is when you intend to do an action. You can be a single date that's most common or it can be a date range for things that span separate days.

**Priority** - August has also walked us through this property selection.

**Status** - We have to-do, in progress, and also August mentioned this. Just want to recap it here. This is particularly useful if the actions multi-day or is a batched action containing multiple steps or a simple checklist. So, you will mark it as in progress to know that you've started working on it, but it's not finished yet.

**Revisit** - we saw it in the tab view, is it marks actions to come back to, waiting on, or snoozed to revisit later. and future one future two park for later. I'll set up near-term window and no due date needed and then done.

**Type** - describes the kind of action and becomes useful for batching similar actions like correspondence or errands or see the weight of your day or week by the type. So is your day meeting heavy or it is full of live actions.

---

## Relations Properties

So relations this will be best if we open the page. The relations property is linked to other parts of the system.

**GPR** - this property connects actions to a project or routine in the GPR database. This property drives the by project view that we just saw earlier as a specialized action view and it makes it possible to see what are all the past and future actions for this project or routine.

**People** - this links an action to a specific person or an organization and this relation powers our by people view which is also a specialized view tab. So you can either search existing ones from here or you can create a new profile in the people or database and it lets you see every action you have involving a particular person or organization.

**Topics** - this is a very important relation. It connects actions to topics in the knowledge zone. We'll talk more about the value of the action topic relation in the resource section. And this relation powers the actions by topic view in resource section. And it lets you organize and reuse your action related insights by theme. So SOP, health, marketing, operations, etc.

**Neurobits** - This relation links an action to a neurobbit entry. So a node, media or document. It's useful when you have supporting docs or ideas that go with this action. It helps you bring reference material into focus zone without navigating to the knowledge zone. You can use new neurobbit button to create a new neurobbit that is automatically linked to this action. So clicking add new and clicking the new neurobbit. These two do the same thing. It's just depending on what context like if you're in a table then this is easier to click than going inside a page. You can click this button when the action produces an insight or resource that you want to save outside of the action context. Then you can create a new orbit for this action.

**Remembrance** - This links in action to your curated remembrance entries. This is directly related to the final few properties I will go through with you. So we'll park it here for now.

---

## Automations and Helper Properties

Now let's quickly look at the automations and helper properties.

**Relative due date** - it translate the due date into a relative label. It helps you see how far something is from now without reading the raw dates. and it's very useful for grouping and for quick glance understanding in your action views.

**Autodata property** - is a property that assembles related information including GPR topics, norbits, people into a compact summary. So you can see these key system connections for an action without opening the action page.

And we talked about the norbit button. So that's another automation button.

---

## Long-Term Value Properties

And then finally we come to the even more useful properties for long-term sake not for near-term but for long-term sake.

### The Notable Button

So we start with the notable button. Clicking this button marks an action as notable and send this action to your remembrance system. Remembrance is a knowledge database will cover in details in N zone where it's located. So use it to capture high signal highlights like your wins, your important events, meaning for work. And you can use it when an action is notable enough to be logged as a highlight. And it connects day-to-day execution, your day-to-day activity with your long-term life story and review.

So remembrance the relational property we just saw inside the page that is showing you whether an action and a remembrance entry they are now related. So we can demo click this button here for reach out to this company. So once we click notable and now you open the page you'll see that in remembrance relation this action is now part of the 2025 collection. So that's how the button and the relation work together.

### The Value Property

So the value property is a property that helps you decide how valuable this actions content turn out to be. You don't need to rate each one. You just need to mark the highly valuable ones for future reference. Value filtering is used primarily in the high-value items view that you see across the entire system or these best views and this is also referenced in your review. So you can see which ones are your excellent actions or your excellent neurobbits.

---

## Notable vs Value: Understanding the Difference

Now I do want to quickly note the difference between assigning a value and clicking notable. An action can be memorable, substantive or both. The value and notable properties capture different aspects of this.

So let's look at calendar for instance. So notable is for memorable and it can be substantive. You click this button if this action is worth remembering in your life story even if the page itself is empty and has little reusable content. So it could be like a birthday or family reunion because you want to remember this event when you're reviewing your year when you review every year and it could also be a key decision graduation or a turning point conversation that you had. You can also use this button to mark anything that's substantive like a very complex piece of work or learning. So notable, you can use it for both. Just mark an event or mark a page that's very substantive.

Value rating is different. Value rating is only for the substance inside the action page itself. So you're directly rating the content of the page. So if the page itself contains high value information you like to revisit and reuse in the future, you would give it a high value. So for instance, we have the update zoom links. This is a list inside an action and you think this is something that you'll reuse and you'll make sure that gave it a very high value. And these are pages that you can reference and reuse in the future. You can use this for long notes, frequently used checklist, correspondence draft you'll use or a detailed SOP.

Assigning a high value to an action elevates that action above the rest. In any view sorted by value, your highest value actions will rise the top. So your best work is always easiest to find.

So in short, notable is this matter and I want to remember it. Valuable is this is reusable content inside the action and I want to use it again and again for future projects or related actions. And we'll talk more about these more value and long-term use properties in the resource section.

---

## How to Remove Sample Data

So the last thing I want to show you before we return to focus zone is how to round up and delete sample data. You can use this in any PB Pro database with sample entries except topics because there might be some sample topic that's worth keeping.

So this is how you do it. First go directly to the source database which is where we are. Remember source database is located within the navigation. Go directly to the source database. Don't remove sample entries from any embeds or those views that we talked about. Don't do that in embedded views. Do this always in the source database.

And next you will create a master table view a new view then filter to the action title contained the parenthesis sample. Once you filter this out you see all of the sample data and then hover over the action column. Click this single check box that selects every sample data you have in here. And then you can click delete to delete all of the sample data in bulk.

So this is much more efficient and helps avoid any potential issues with other view. I'm not going to click this button here because I still need this sample data to help with a walkthrough. But just the idea that's the sample data cleanup that can be useful.