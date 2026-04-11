## Bối cảnh và điều kiện

Let's start with synced actions. So about synced actions. First of all, what the context is and what the conditions are that this workflow might work for you.

So first of all, this is the most advanced one of all three use cases we'll be talking about today. So definitely we're doing the hard one first and the other two are relatively, I would say, a lot easier. So just be prepared. This is definitely the most advanced one.

So synced actions, the condition is that you are collaborating with someone who does not have access to your private PPV actions database that is built in your PPV system. And this person could be a virtual assistant of Yay or a contractor like an editor. And this outside person will maintain a separate actions database that is shared with you. So both of you can view and edit that shared database.

So essentially you'll be working with two actions databases. One is your private actions database built in PPV that only you can access. And the other one is the shared actions database that both you and the outside person can access this, but they cannot access your private actions database in PPV. So those are the conditions for this setup.

The objective for synced actions is to sync the Shared Actions database into your private PPV actions database. So you can manage both sets of actions from your private system without having to switch back and forth between the two.

---

## Yêu cầu kỹ thuật

And the technical requirements for this setup are the first one is you need to be on Notion Plus plan or above for customizing advanced database automations. And two is more notion skill from you that you need to be comfortable with the basics of database properties, views, and automations.

So we'll go through the key steps, I'll break them into stages. And after I walk you through the key steps of how to set this up, I'll share some important final thoughts and notes that you need to be aware of for using this setup.

---

## Thiết lập Shared Actions Database

### Tạo database

Okay, right now we're in the PVE Pro Demo template. And so if you already set up this shared database with that outside person, like your VA or your contractor, then you need to just go directly to that shared action database for what I'm about to share with you the things that you need to do.

But if you haven't created that Shared Action database yet, if this is for work purpose, I recommend that the best place to create this shared action database is inside Workspace. So inside the navigation you can create the data source. This is a Shared Actions database and you'll create the database in the workspace here. And if it's for personal use, you can create it in the personal space. That's just the data source.

But again, if you have already set up this Shared Actions database with that individual, like a VA or contractor, then you would just go directly to that database. And now let's go to this shared action database. If you haven't done this, you can create it here.

### Thiết lập properties

So this shared database, again, this is a shared database for someone else like a VA contractor. And this person doesn't have access to your private actions database built in your PV Pro system. So all they have access to is this database.

So to set up this database, you can set up a lot of other properties that you wanna do and say your editor is going to use. And the most important ones that matter for our action syncing are one, you need to have an action name and two, you need to have the due date property and that is properly set up due date.

And three is you need to have the priority property. This one, keep in mind that you need to match the options in your primary action date. So let me pull up another window. Let's go to our primary actions database. Actually let's go to focus up. So it needs to have the same priority options. So these two sets needs to be the exact same options so that way they can sync perfectly. So priority property is another one you need to have.

And the third one is status. And this one, again, it needs to match the status options in your primary actions database. It needs to have the same status right here, the next property that is a little bit depending on what you're using it for.

### Category property

So if you're working with this outside person primarily or only for work purpose, then all you need to do is create one option for this category, select. And that is just work. However, if you're working with a va, a virtual assistant and this outside person needs to be able to create actions for work, for personal, and for your you know, family, for your connection. And if that's the case, you need to make sure it has all three options.

So know that because our category is using all caps, then you also need to make sure that for this category, it needs to be all caps for the options. So again, if you're using this shared database, if that person is creating actions just for work purpose, then you only need work and you don't need to worry about the other options. But if that person aren't creating actions or managing actions across all categories, then you need to create all three. So for this demo purpose, I created all three.

### Relational property

And then finally is you need to create a relational property that is linking to your primary action database. So you just need to create a relational property and to relate to your primary actions database inside your PPV focus zone. And that is it. And two way relation is on.

So these are the most important properties that you need to make sure set up and set up like this. These two need to match the properties in the primary actions database and the category. Again, depending on your use case, you have different options and you need to set up a relational property. So you're directly linking the Shared Actions database to your primary actions database in your focus zone, in your private focus zone. So these are the properties.

---

## Thiết lập Automations cho Shared Actions Database

Next, you need to set up automations in this Shared Actions database. So to access automations is to look at this lightning bolt icon here you can create and view automations.

So we will need to hold off this step until we're done setting up our primary actions database. So just know that this is another thing you need to do, but we will not do this until we're done setting up our primary actions database.

### Default icon

So after you're done setting up automations, which we will talk about in a little bit, the next thing you need to do is set up a default icon for your shared actions. The reason is when we're creating these synced actions, you're creating duplicates in your primary actions database. So to be able to identify which one is the shared one, which is the one that this outside person has access to and which one is in your private actions database, you will need to be able to identify and just kind of distinguish them.

So we will apply a default icon for every action generated from the Shared Actions database. So to do that you will essentially create a new template and open the template. And in here you'll add an icon here and you can choose whatever icon you want. So for this demo purpose, we have a green share icon here.

And once you set up this template, you need to open this and set as default and as default is for all views in Shared Action database so that anytime an action is created in this Shared Actions database is applying this icon, it's applying this template with the shared icon that you just picked.

### Liên kết trong Focus Zone

The next thing you need to do is at this database in Focus Zone. So we're in Focus Zone to be able to access this shared database in your focus zone. You can link to it here in the navigation under the other data sources we have here you just at Shared Actions database and you'll link to it here. It's just for your easy access if you need to jump to that database to manage it or to customize it.

### Phân quyền (Permission)

And finally is permission. So for this Shared Action database, of course if you have already set it up that you already know how this is gonna work, but if you haven't set it up, you're just creating it, you're gonna click the share button and you will enter the person's Notion account email and give them can edit access.

So make sure they can edit, suggest and comment if you fully trust this person and you can give them full access. But what I recommend is do can edit to start with. And if you want to give them more permission and they need to share things with other people, then they'll have full access. But if you don't want 'em to be able to share things here with others, then you just wanna give them can edit.

So that's for permission, you need to set it up so they can access this database, which is going to be the home base, their actions database that they're gonna be working from.

---

## Thiết lập Primary Actions Database

Okay, so that's the initial setup, shared in Shared Actions database. Now we need to go back to focus on, we need to go to our primary actions database to look at what we need to set up there.

### Responsible property

So first of all, let's go to our focus zone. This is our focus on our process section and that this is our actions database, different views, and we have an existing view called Table.

So what you do is in this view, first of all, you need to create a property in this demo. 'cause in order to make things quick, already set it up. So to add a property, what you do is click on the setting, edit property and then click new property. And you click a new property where you need to create a property, it's called Responsible. This is a select property and right now you only need option and that is the outside person.

So if you want to put that person's name here, you can or their role like a VA or contractor. But essentially you just need to have a property that's able to identify that this is something for someone else to do and not you. So if it's for you to do, you don't ever need to select this property 'cause it's just default, it's yours. But if it's for someone else to do, you need to make sure that you have a property to identify that this is a task for someone else. So that's what you need to select property for the new selected property called Responsible. You can rename it however you want, but this is a single select property with an option identifying someone else.

### Relational property (xác nhận)

So that's the first property you need to set up. And the second property that should already have set up is the relational property. So remember that we set up this relational property linking the Shared Actions database and your primary actions database. So this will be like that mirror the counterpart property and it's here, it should be identified as Shared actions database. And to relation to the shared actions database is a two-way relation. So just making sure this one is already set up and you just check that in your property list.

---

## Automations cho Shared Actions Database (chi tiết)

Okay, so once we have these two properties set up, we should be good to go. So because now we have these two properties set up, now we can jump back and do some customizations. Finish the customizations in the shared actions database.

### Automation 1: New Actions Sync

So these are the two automations that you need to set up. First is new actions sync. So when a page is added, and this is for all pages in the shared actions database, you need to add a page in the actions database. Remember that this is your primary actions database, it needs to add a page to your primary actions database.

And the action title is a formula, very simple one is trigger page do action name. So what that's doing is it's copying the action name in here and it's going to do the exact name as your shared action. And status again is trigger status. So it's going to copy the status over from the shared actions database. Responsible is someone else and due date is trigger due date.

And category is work because this is for work purpose. And if you're actually working with a va and this VA is creating actions across all categories, then instead of doing work, you'll do trigger category, just like trigger status, trigger due date, you would do category as trigger category instead of work priority is trigger priority and shared actions database, you will just select trigger page in the list. They'll give you this option here and you can just select it and then add page, add it to primary actions database. So these are the automations for new action sync.

### Automation 2: Update Sync

The second automation we need to set up in shared actions database is update syncs. What that means is anytime you make changes in the actions here, like changing their names, changing their due date and changing the priorities status, these things not category. If this person is changing these things, it needs to be reflected in your primary actions database so you can see what's you know, changed like a status or priority.

So the update stink is doing exactly that. So when any property is edited, that's the trigger, it will do defined variable. This is a hard one. So let me show you how to set it back. So when you click new action, when it's a new automation, at the bottom is define variable. That's how you set up this one.

And you'll set up the variable's name. This is something you can type, you just call it related actions. And the formula here is trigger page dot primary actions database. Just do exactly this.

And then the next step is edit this variable that we just define. So you can select it from a list, it will show up as this list and you will select the variable. You just define, edit the variable and change their status to trigger page status due date to trigger page, due date, priority category, and action name. So that's the update is sync automation.

---

## Automations cho Primary Actions Database

So now we're done with setting up this shared actions database. We can go back to our primary actions database and finish our setup there. We need to create our own sets of automations in our primary actions database.

### Automation 1: New Action Sync

And the two automations are essentially similar. The first one is new action sync is for all pages in action. When the responsible is set to someone else or whatever you define this option. And it will add a page to shared actions database as a new page. And set the action name to this. A custom formula, very simple one, status, primary ad, primary actions database, select trigger page, category, due date, priority and add page added to shared actions database. So that's the first automation.

### Automation 2: Update Sync

The second automation again is update synced. So if you are creating, generating some actions for your VA or for your editor, for your contractor, when you make changes to the actions that you're creating for them, it's also making sure that it's updating their copy in the shared actions database.

So for this automation we have when any property edited, again define variable related actions, trigger page, do shared ad, and then edit the variables that you just designed and update the action name category, due date, priority and status.

And then when you're done click done edit didn't make any changes. So the done is grayed out. But when you're making changes, make sure that you click done not out. 'cause that's not going to save the changes you've made in the automation itself. So these are the automations part for our primary actions database.

---

## Thiết lập Filtered View

And this next one we need to make sure that we do is create a filter view. So the whole point of setting up synced actions is so that we don't need to go to their page, their actions database in order to manage their actions. And we are syncing our actions so we can manage it from our home base, from our focus zone.

So it will be great that if you can just set up a view in your process section that you can create actions for them or view the actions that they created and see what the status are and what the progress is.

### Tạo view

So to do that, a simple way to do is you can like duplicate this table view that we already hear and rename it to shared, or you can click new and just add a table of your primary actions database. So either way you can duplicate an existing one and just customize it or you can create it from scratch.

### Filter rules

So let's look at this shared view, what we need to set up. So in this shared view, the first thing we need to do is make sure that we set up the filters, right? So in this view, all the actions that we're creating are for someone else. So we need to have this filter set up that the responsibility is someone else, that person's name or what you call this option.

And the due date I recommend maybe this week because you can see what they completed and what you have scheduled or they have scheduled for this week. This is customizable. If you wanna see a month or just today, you can do that. But my recommendation is this week, just so you have a slightly wider range to see what's being done this week or what you have planned or what they have planned for this week. So that's the due date.

And the category is work because for a contractor, like an editor, they're just working with you and they're creating work items and you are creating work items. But again, if this is for your va, then you will delete this filter because you need the VA to be able to create actions for all categories. And you need to be able to see actions in all categories and you can create actions across all categories for them to do.

So. This is a dependent filter that you can remove or you can just set it to work. In this case, in this demo, let's do it for just work purpose. All the actions you're creating for them are for work purpose. And what they're creating for you are for work purpose. So this is the work category, that's the filter rules.

### Property visibility

And next thing we need to make sure we do is change the property visibility. Again, the important ones that we've talked about are the action name, due date, priority, status, category, responsible and shared. That direct link that you can see what actions they have are the counterpart in their database.

And after that, the other ones are up to you. 'cause these properties are built into your PPV actions database and they don't have these. So it's for your management. You can create a type or link, GPR and topics, all of these things and they won't see it because these are all properties in your private action database. So depending on what you want to see here in this view, you can either hide them or leave them here. But the important ones are the ones that I just talked about. These are the most important properties that you need to be able to make sure that you see in this view.

### Grouping

And finally, we have grouping. Now, my recommendation for grouping is that you group actions by the status group, let me show you. So group by status and group. So what that means is you only see actions in three to do in progress or complete.

And if you need to fine tune it, say this is for future one, future two, you can do it and they will have this option if you set up the stats properly to match. But the thing is for you to see, to organize in the most simple way, you wanna see just the group, like what they need to do and what's already in progress and what they complete. And right now nothing's completed and nothing's in progress. Therefore you're only seeing this grouping because it's hiding the grouping that are empty. But once they have finished, you should be able to see and we will demo a little bit.

---

## Thiết lập Page Layout

Okay? So that's the filtered view and that's a shared view in your primary focus zone and in the process section.

And lastly I would say is for the page layout, because you added some properties right in your primary action database, let's open a page and you can decide where you want these additional properties to be used. So I think the responsible properties should be in the more info toggle. So you can see that this is the first to someone else, like when you're creating action for them, you can easily select this option here.

And the direct linked relational property I think is better hidden here in the side panel. So that if you need to check it, you can check, but most of the time you can just see it here, you see if you created some.

---

## Kiểm tra (Testing)

So the next thing you need to do once you've set it up in your primary actions database, in your focus zone and in the shared database, is to test, test to make sure that the sync is working.

### Test 1: Tạo action từ phía outside person

So pretend that I am the va, I'm working for you. I need to create an action and let's say edit two videos today. Okay, I'm a va, I just created this action that I need to do. And the due date is, yeah, let's say tomorrow on Friday. And the priority is first priority is to do category is work.

So then you see your own copy, the primary copy in your private action database. This is created. So you open this up, you can see that now this is a copy of what your editor created in the shared database is now available in your primary. And we can check it to see that. Now we have edit two videos today and this is in your primary review and you don't ever need to jump to a shared database and you can see what actions they created.

### Test 2: Cập nhật trạng thái

Okay? And if in this actions, so they're now ready to do it, it's in progress. And you can see that now in your primary action view, your own copies status is updated too. You can say, okay, so this is something that's in progress. And when it's done, when they market it as done and you come back to your primary action view and you should now see a new grouping cut done. And that's what they finished today.

### Test 3: Tạo action từ phía bạn

So that's when they're editing and creating actions. Now when you need to create actions for them, like say you wanna create a new action for them called a review of feedback, okay, you want them to get this done today, that's good. And the priority is, let's say third priority and to do it's work category and it's for someone else. You see these are applied automatically because this poll view is filtered for someone else at work. So these are pre-filled for you and you can actually see that this is already created for the other person, for the contractor.

And you go to their database, you see that this is the action that they now have, review feedback, and you know they can do their own sorting or you can set up sorting for them. So this is highly customizable and they might have other properties that they need to add. But the essential ones, you can see that these have been updated and it's their priority to do. And very convenient. You can create actions for them and without ever leaving your focus zone.

---

## Lưu ý quan trọng

So that's the setup part. Now some important notes that I wanna mention.

### Syncing chỉ dựa trên properties

One is syncing is property based. So only properties included in the sync will update across databases. So this is what I mentioned, that you have a lot more properties in your private actions database, but because you're not syncing them, they will not be shared. They will not be updated. So you could choose what you wanna sync and what you don't wanna sink. So unsynced properties do not carry over. If a property is not part of the sync, changes will not be shared.

### Page content không được sync

So the next note that I'll make is page content is not synced. So this syncing action is only for properties that you can see here and not what's inside a page. What's inside a page is not shared. Anything written in the page body stays in that database. So if you type some notes in your private actions database where you're typing here will not be shared with them. And vice versa. If they add something to the page content, these things will not be shared with you.

But if you do wanna see it, it's very easy. You just look at your action and go to their copy and instantly you can go to their action and see if they have anything in there.

If you want synced page content, what you need to do is use synced blocks. And that is a notion of basic functionality to sync page content or paragraphs or any page sections that you wanna sync as page body. So again, page content is not synced in this setup. You can sync them with synced blocks.

### Giữ private PPV action list gọn nhẹ

And the final note is you wanna keep your private PPV action list lightweight. And the purpose of this setup is to track and manage the other person's execution without pulling all details into a private system. So you're sinking only the essential ones like status and due date. These are the two most important thing and priority. So you wanna be able to see when the status is changed or the due date is changed if they need to postpone something. So sync only the essentials, not everything.

And my recommendations for view settings, best for management purpose is data. This week we talked about and group by status group and categories work.

---

## Kết thúc và Q&A

So that wraps up our action sync, our sync action setup. That is fantastic. Remember for years we dreamed of being able to do something like that and now it's come to life. What a great methodology for doing that. So any questions? Let's see if anyone wants to dive in a little deeper. It looks like we have one question here.

Ross asks, is there a reason why you use a select field for someone else instead of using an assigned to a user field?

You can use the user field. That's the same thing. The reason is because I don't currently have someone to assign, so I'm using a select property, you can use the assigned property, but to make things simple, if you don't want to like tag their icon, because anytime if they're tagged as the assignee in a person property, they will get a notification. But that assigning process is only in your private action database. So in my perspective, I don't want to trigger notifications that I've tagged them in my private action database.

So that's why I prefer to use a select property as opposed to a assignee. But you can do that. It's the same purpose, it does the same thing. Just preference. If you wanna use the person property, you can totally do that. So good question.