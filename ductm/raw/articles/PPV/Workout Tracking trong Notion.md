## Giới thiệu

Welcome everyone. Good to see you guys. Excited for this session. I think this is going to be a particularly fun one and good one. So fired up. Jane, you ready? Yes. I've always been interested in this one because I feel like this is a motivation for me to get more workouts in my daily schedule. So I'm actually excited to see how this is implemented.

Yeah. So today we're diving into workout tracking. And just to give a little bit of background, we had one in the old system for those of you who were previously in the program. And it was really meant to be just a suggestion of some ideas on how you might implement it because everybody has different workouts and there are wide range of things you can do for exercise. And ultimately, you kind of need to customize to your specific type of working out and the range is just expansive.

So with that, we had a sample one in there. You could just try and get some ideas. But we've had a lot of interest in this and it is of course very important and foundational to the way we live and how we can be successful in life. So I went back to the drawing board and bounced some ideas around with Jane and we came up with the idea of a more fullfeatured, more functional, broadly functional workout tracker. And that's what we're going to share with you today.

---

## Cân nhắc giữa Apps chuyên dụng và Notion

### Ưu và nhược điểm của các phương pháp

Before we dive into that, I just wanted to talk a little bit about the balance of using external apps, doing it in notion in an all-in-one environment. There are pros and cons and there's no one right way, but I do think this new approach in notion that we're going to go through today. I think it makes the notion option much more viable and I didn't expect that when I started working on it and started trying to bring this into my workouts initially because I had been using an app called Strong. It's a really good app. I think it's Apple iOS only, but I'm not sure. It works really well. It's very easy to capture the weight training information in particular. And if you're using an Apple Watch, it makes it even easier to quickly capture the information.

And then for cardio, I use Strava, which is extremely popular and I'm sure a lot of you have used as well. And that captures things with a lot of automation and gives a lot of good visualizations and data aggregation on what you've done in the past across running across cycling and I think it's expanding into new sports now. So it's more comprehensive for that kind of thing. And when I was doing swimming, I think the Apple Watch was capturing that really nicely.

### Vấn đề với Apple Health và Data Export

So capturing a lot of data in different places and it was thinking into Apple Health. Although I do think that the Apple Health functionality, the central app that aggregates everything is in my view very disappointing in how it presents the information after it brings it all in. It's a great hub and it sort of consolidates it very nicely, but it's disappointing in what you can do with it.

And it would be nice to have this data in notion where especially now that we have charts and graphs, we have a lot more flexibility to analyze and evaluate the information that's coming in. A lot more control and flexibility. Now, some of these apps will let you export and then import, but that's a manual process and that's we're trying to not spend a lot of time just doing busy work like that.

### Tại sao Automation khó thực hiện

So, you know, the next step is to look at how we can automate it. And almost across the board, it's very hard, in fact, usually impossible to find ways to automate this information coming into Notion because most of these apps don't want you taking the information out and using it somewhere else like Notion. They want you to be attached to the app because aside from the Apple app, the Strong and Strava and all these things, they're subscription-based and they want you to be going to their app to do it. Not just to capture the data, but to actually interact with the data. They want to make it hard for you and in some cases impossible in the case of automations to extract that and use it somewhere else because they want you to be glued to their app and their subscription.

So that's just the way it is. You can't find these apps on Zapier or Make or if they're just not building APIs and integrations like that. Some of them have manual exports and some don't even have that. So, you know, it is what it is. But they do have good interfaces and if you're committed to using those tools, they're functional and they're very good for capture and they're okay to varying degrees for analysis and review.

### Giá trị của việc đưa Data vào Notion

So, that's there. But there is a lot of value for us working in the PPV system where so much of our life is already there and our review cycles and our daily entries and our focus zone is all in one place already. There's a lot of value in having that information in notion and it does give you more control as I said now especially with charts and graphs. But even just analyzing tables by filters and sorted views can be really valuable and give us more control in many cases than what we have in these apps.

So, I thought it was worthwhile and Jane agreed to dive deeper into how we could really bring this more functionally into PPV, but also expanding beyond just what we had before, which was cardio workouts or topline aggregates and bring in the possibility of multi-exercise workouts in a single workout entry for a given day. So, that's what we're going to look at.

---

## Chia sẻ từ cộng đồng

### Thu thập Feedback

I do want to start out by asking you guys if anyone has any thoughts or frustrations. love to hear what you're wrestling with with your fitness tracking, either on the capture side or on the review side. Go ahead and raise your hand or type in the Q&A if you have frustrations or things that have been less than ideal in your fitness workout tracking process. Would love to hear what you guys are struggling with or dreaming of in a future scenario. That'd be super helpful to sort of set the stage here.

### Phản hồi từ người tham gia

I see some comments coming in. definitely exporting data toward my notion tracker. Yeah, it's I mean we've talked about this for a long time since the very beginning of PPV and the reality in the beginning we sort of banged our head and tried to figure out ways. The truth is they don't want you to, right? You can't because they don't want you to. On Notion's end, it's fully there. You can do it on notion's end. You can't do it on the source app's end. Notion is integrated with make and zap year and you can write and update entries. You just can't get the information out of the source application because they don't want you to because they want you to stay stuck in their subscription platform, which you know can be quite good.

Another one I use is Whoop. And that is sort of an all-in-one all-inclusive, but it's terrible at ascending out and and coordinating outside of that. So, another thought from Kathy is seeing trends longer than a couple days. Yeah, a lot of these apps, they tend to have very short views of the history. That's another reason it's valuable and helpful to bring it into Notion.

### Các thiết bị và Apps khác

Well, I have a sense of your frustrations because I've talked with a lot of you and I've had similar frustrations myself. I use a wing scale as well and that captures the information very well. But once again, it doesn't export in a very friendly automated way. So just that ongoing issue. But individually, they're good.

---

## Phương pháp Checkpoint trong PPV

### Tích hợp với Daily Planning

And one of the approaches, I'll expand on this a little bit more. This is sort of the approach that we talked about in the original core training for the PPV Pro series, is wherever you want to interact with your data, whether it's capture or whether it's review and analyze, we can build that into our system as checkpoints. So if it's in the daily planning in our daily page, we might have a stop in the morning routine to go do your workout. You might have a stop at the end of the day to review and analyze, in which case you could either have a checkbox to confirm you do it, to prompt yourself to do it, and a link to relevant sources to go see the information.

But it wasn't bringing the information in because as I talked about, they make it hard to bring that in certainly in an automated way. even manually it's not as easy as I would think it should be in this day and age of you know fluid data flows similarly in our cycle reviews we can have the checkpoints to review and we can link to the things and that works really well.

### Khi nào nên dùng Apps chuyên dụng

And if you find a lot of value in the apps and the specialized apps will do things that we can't do in notion they're designed and coded for that one specialty function they will do things that are better in some ways so if you find those apps to be valuable run with it in some ways they're going to have a lot of advantages. And you can build the checkpoints into cycle reviews to go and do the review in the app where you have an abundance of data that was captured with automations and with smart and customized specialized presentations of your data.

I do find often it doesn't have the presentations I want even though they're very slick and beautiful. Sometimes it does, sometimes it doesn't. You know, that's the nature of hard-coded software that we can't manipulate ourselves. But the beauty of notion is we can customize our views and filters and charts and graphs and layouts and data rows and so we can have a lot more control over how we see things and often that's more valuable.

So that's the trade-off. Those are the pros and cons and it'll be an endless consideration that everybody needs to make. But if you want to go all in on one application and capture in a very efficient way, that's one of the things that surprised me and sort of won me over to the notion approach after having done the app ones for a long time is I think I've come up with in this presentation of this new template I'm going to share a way to capture, especially on the weightlifting and multi-exercise workout days, very quickly capture the information because that can be quite tedious and you don't want it to be interrupting your workout.

---

## Chia sẻ về Diet Tracking

### Giới hạn của Notion với Calorie Tracking

So with that, let's dive in and take a look at that. Let me check the written chat here before we jump into it, just because I know a couple things here I've missed.

So Kirsten wanted to deep dive physical symptoms with exercise foods. Being able to blend data from different realms into one place, like notion would be great, but I've never been able to do that as I mentioned. Yeah, I'll tell you it's even harder when you get into diet. Those apps have even more data and they're even more designed to quickly enter. Like what's the main one? My Fitness Pro or My Fitness app. My Fitness Pal. My Fitness Pal. That's the one. Thank you. That sounded like Connor.

So, yeah, My Fitness Pal is great for capturing your diet and getting the calories and even the macros all mapped out in there. It's great. I mean, you're not going to be able to do that in Notion. Not even close. But there's no way I'm aware of, and I don't think it's even possible, certainly not to automate extraction of that information and send it into Notion. And really the analysis of that information is a bit more sophisticated and benefits from a specialty app.

So I wouldn't even try on the calorie or macro counting side, but it would be nice. One day potentially maybe AI will open this up. But on the fitness and workout side, I think we can do this and I'm actually really excited about this new approach and I've been migrating toward it myself and I'm thrilled that it's doable. And then we have all the information in our systems and we can resurface it even more fully with customization in our BPV systems.

Yeah, Danielle also chimed in with My Fitness Pal. That's a great app if you want to count your calories and your macros. There are other good ones, too. They're new ones where you can just take a photo and somehow AI extracts the calories. I'm a little suspicious of how capable that is, but people say it's great, so perhaps it is.

---

## Tổng quan Template Workout Tracking

### Hai khía cạnh của hệ thống

All right, with that we have here this new template that I'm going to share with you guys that I've been working on for a while and using a bit myself and I'm excited about it. So that's why I thought this might be a good session here for this use case and we'll talk about how it can integrate into PPV Pro as we go.

So there are two aspects to a system like this. One is going to be the capture of the data and one is going to be the review and analysis of the data. You'll see in this dashboard here, there is a link up here to the visualizations. We'll get into that after we go through how to capture it.

---

## Data Capture - Cardio Workouts

### Cấu trúc cơ bản

But first, let's talk about data capture. And the idea here is we have workouts each day or three days a week or whenever you do them on some interval within the week, multi-day a week, you're doing a variety of exercises. And in the past, if you're coming from the old system, we did the easier part, which is the cardio. So here we have cycling. We have the icon for running. These are the cardio workouts. And you of course could create views to filter just for those, but I think it's valuable to see all the workouts in aggregate.

And over here we have a template for each because we want to apply the date in the title. We're not titling it by the sport. We're indicating what it is by the icon. And of course, we have the sport designation here. But we have the date here. Now unfortunately notion requires that titles of database entries be a text property. You cannot put an actual date property in the title. Now you can write the date but it's written as text.

So for that reason we also have a date property to have a more rigid sortable date function and we're writing the date in here because that truly is what actually matters. So you could actually hide this and this will be a duplication of that but you need the date property for greater control also comes into play with the charts and graphs.

### Chia sẻ Template

Now I'm going to share this template with all of you guys. So no worries you don't have to create it from scratch and we'll talk about how to integrate it into PPV when I post this video. Under it will be the template and you'll have full access to it then including these samples.

Okay, so it's sorted by date here, you know, sorted by date descending. And the one rule is that it's within the past 30 days. So, we have a 30-day view. Obviously, you can customize that to whatever view or views you want.

### Tạo Cardio Entry

But very simply, when we create a cardio exercise, this is very similar to what we had in the past. You would apply the template down here. So, let's say it's a it's a cycling one. We said cycling. It'll just apply the icon and the dates automatically entered. We'll go through this, but in here these will be closed. You got two toggles here. So for cycling, we would enter whatever data you want. You can add and expand on this or just keep the basic stuff. We'll enter the number. We'll enter that. This will come from your cycling computer.

If you're doing running or again, you add the exercises you do. You can add swimming, you can add whatever. Now keep in mind there are two kinds of exercises as we'll see in a moment. There are ones that are just an entry with aggregate data for the whole workout. This tends to be cardio stuff. Then separately, there are entries where you have multi-exercises within a single workout. That would be weightlifting, Pilates, yoga, things like that.

### Tùy chọn đơn giản hóa

So, right now, we're just looking at ones such as cardio where there's sort of aggregate stats. Now, you could make your weightlifting an aggregate entry where you simply either have a check box or indicate that you did it and it being done is all you want to enter. That's fine if you don't want to track sets and weights and all that stuff and different exercises. Or you could have the time, you could have your heart rate, you know, just like the cardio stuff, you could treat weightlifting or Pilates or yoga like that. That's totally fair game and that's there if you want it. And this is similar to what we had in the past.

And then for running here, just to give you the more common example, again, you'd have running and that's up here with the icon to indicate it's got the running sport and then you would do the toggle for running. You just enter whatever data you want in your template. We'll have by default just pace and distance. And then up here we have heart rate and total time if you want to capture that. Again, you decide what you want to capture for your workouts. So very straightforward, very simple.

### Một Database duy nhất cho Aggregate Data

And if all you're doing is that this aggregate data, not multi-exercise data, then you're going to just use this one database. This is it right here. This is what we had in the past.

Now, you'll see here you can of course customize. It's going to run. And I do want to point out this is covered thoroughly in our learn notion fasttrack notion course, but all of these layouts with these toggles down here in the layouts up here are all customizable in the custom layout capability here. And you can add new groupings for the different toggles over here. Add the different exercises. Build it out as you want. If this is not familiar to you, just check out this lesson in the FastTrack Notion Learn Notion course in the program.

And then you can customize that. And of course, similarly, if you want to add exercises that are not listed here, you can either change one of the ones that you don't do or duplicate and create additional ones based on that. These are for these more cardiocentric ones.

---

## Data Capture - Multi-Exercise Workouts

### Giới thiệu phương pháp mới

All right. So that's simple and that's what we've had if you've been with the program in the past and perhaps if you've created your own because that's the more straightforward. The more sophisticated one that I think is the real innovation here and the real breakthrough here is the multi-exercise approach.

So to do multi-exercise, we have two additional databases here. This one is the exercises. Now the example I'm giving is weightlifting, but this could be Pilates or any multi-exercise workout that you're interested in. and I have entered all the exercises that I am interested in doing at various times. So, it's the full collection of the exercises that I want to be able to choose from when I do a workout. And obviously, this lends itself very well here in this example to weightlifting, but again, Pilates, yoga, whatever.

### Exercises Database

And in here, you will have a template that you can apply. And in that template you will have this in a opportunity to embed a video which will show you proper form. So you can easily call it up and get a demonstration of form to remind you and fine-tune your approach to the exercise. And it will create an aggregate as we'll get to above the history of days and reps and weights and times you've implemented this exercise which in this case is the bench press. and others will be similar.

Now for other than that one, I just put the instructions here of how you can embed the video from YouTube. YouTube has short demo videos on every exercise you can imagine. And then we get our aggregate history here. The one real piece of data entered here is the muscle groups. I just thought that was nice to see what the muscle groups are. Again, you'll customize this for whatever types of exercises you're entering, whatever is relevant for that and whatever you're interested in.

So this is where you'd start. you'd add the exercises that you're interested in doing. And of course, there's an archive here. You just click the check box if you want to archive them. That way, if you ever want to retrieve them later, it's accessible, but you can keep the list manageable. All right. So, that's a very simple database, but that's where you start if you want to do multi-exercise workouts.

### Sets Database

Then, once you've done that, just so you're aware, this is a database of all the sets you do, and it's grouped by date. So, as we add some new ones, the new ones will be in today. And it's sorted by date and then breaks out, let's look at the sorting here, by date first and then the exercise type and then the set. So it breaks it out very nicely. So we have all the bench presses, the deadlifts and the flies and then bench press set one, two, three. Deadlift 1, two, three, four, flies one, two. Whatever you do is what'll be captured.

It'll have the reps, the weights, the muscle groups are rolling up because you're attaching. This is a relational link to the exercise list database below. and rolling up with that automatically is the muscle groups. So it's there.

So just be aware of that this is here and mainly the purpose of this is sort of backend as we'll see we're going to be entering this in our workout sessions not in this database but we'll be using this to create data analysis later because this gives us the full history of the workout strength training or multi-exercise workout. So this is going to be the database we use for analysis and charts and graphs. But we're not actually going to enter here. This is just aggregating data.

---

## Demo: Nhập Data Workout

### Tạo Weightlifting Entry

We're going to enter them here. So if we want to do a weightlifting workout or again any multi-exercise workout, we will enter that here. Let's look at yesterday's. And it is going to create a nice breakout here grouped by exercise. So this is a grouping of the database view. It's one database view, but it's in using the grouping functionality. And the bench presses sets one, two, three. The deadlifts sets one, two, three, four. in the flies sets one and two with all the relevant weights and muscle groups and everything else.

Now, let's see how we would enter this very fast and efficiently because that's the thing, the risk is that it's just too cumbersome to enter this because you got to enter it while you're doing it and you don't want it interrupting your workout.

### Multiple Workouts trong một ngày

So, let's say we want to do a new workout today. We see that the most recent one was yesterday. I should also point out before we dive in here, you can do a multiple exercises in or sorry, multiple workouts in the same day. So maybe you do a cycling and a weightlifting in the same day. No problem. Just enter them both. They'll both be automatically dated and you'll have both of them here.

### Nhập Cardio nhanh chóng

But if we want to do, let's say, a new cardio, we just pick the run. Say we're doing a running today. Don't enter the date or the name title. It will automatically enter those. It'll automatically enter the sport and the icon. And all you need to do is enter the data from whatever app you used to capture the run distance and pace and time and heart rate or whatever data that you put into your template. So that's there.

So let's just put in five for miles but again kilometers whatever. Use what you want. 10 whatever metric of speed you're using. We'll put in say no hours and 45 minutes or whatever. I'm just throwing random stuff. 135 whatever. So, that's how long it took to enter it. Very quick. Now, we've got today's run in there.

### Nhập Multi-Exercise Workout

Now, we can also, and I think more interesting for the demo is the multi-exercise. So, now we're going to do a weightlifting. We're going to apply a weightlifting template here. And I think this is where it gets a lot cooler.

So, automatically, it's going to enter the date in the title. Don't touch those. And it's going to build out the table here so you get your breakout of the different workouts so you can track them as you go.

### Quy trình nhập Set cực nhanh

Now, here's how fast this is. All you're going to do is come down here and add a new page or new. Just hit new. It's going to open the new page. This is for the first set. And it's going to automatically again enter the date and time. So it can all sync up in the system. Don't enter date or time. All you do is pick your exercise from here. And this is a relational database property to the exercises list that we talked about in the beginning where you entered all your exercises.

So now we're going to pick one of the exercises. And once you click it, it goes to the top. You hit escape. It backs you out of it. You hit set one. Tab. You hit the weight you're doing 150. Tab. And the reps you're doing. You do the reps. And then you see what you can squeeze out. And you enter 12. And you hit back arrow. And it's there. That is how fast and easy it was to enter.

### Tiếp tục nhập các Set

Now we do the next set. Hit new again. Automatically enters the date and time. We can just go ahead and enter. What exercise did we do? Oh, it puts it on the top. Actually, the one you last chose is on the top. So, we have squats. Very easy. Again, escape set number two. Weight, you know, 160, reps, nine, back arrow, and they're already stacking up here. One and two.

So, let's say we do under our next exercise. It'll automatically enter date and time or title and date. And we enter, let's say, let pull downs. Again, you'll put in the exercises relevant to you. Escape. Set one. Tab weight 95. Tab 12 reps. Back arrow. And it breaks it out into a second grouping because we have in this template the grouping. Group is set to the exercise. So, it's grouping the same database by exercise. And we got our first set.

### Demo thêm các Set

All right. Let's do our next set. Click on exercises here. You don't have to wait for the name to come in. It'll come in on its own. and it'll have the most recent one on the top. Click that again. Escape. Set two. Tab. Weight 105. Reps eight. Back arrow. Done.

One more. Lat pull again. Escape. Set three. Weights 110. Got six reps in this time. Back arrow. Done. We've got the full list here. Breaks it out. Organized. Fast. Efficient. This is why I'm loving it.

### Tất cả Data trong Notion

Now all the data is in notion, perfectly suited for notion, captured in notion. And you can do this on the phone. You can do this on a little laptop in your gym. Whatever works for you. You don't really look at them when they come in here while you're working out unless you're just perusing. But generally, you're just hitting new ones. You just hit the next one. Boom. Escape. Set for tab. Weight reps. Back arrow. You're really just adding them while you're going through the workouts.

So you get the full collection here. here. If we added another one, it would do another grouping. Let's just do one more so we can see the full grouping. Let's do deadlifts. Escape set one. Tab 100 10 back arrow. And so we got another grouping. So they all build out here. Great.

---

## Đồng bộ Data giữa các Views

### Workouts và Sets coordination

So we enter that. And just so you can see how things are nicely coordinating across all of these. We now have today's workouts. These are the ones I just entered in today's workout grouped by today. And then we have the list of yesterdays that I entered yesterday when I was preparing for this workshop. But in your case, it would be yesterday's workout. And then the last seven days, and even the last seven days are in order by date of workout.

Again, these are just the weightlifting ones. This workouts up here has the weightlifting workouts and the cardio. These are the workouts. What we have down here is the sets. And again, this could be Pilates, yoga, whatever. Yoga probably doesn't work as well because you're fluidly going between them. You're not stopping and entering. But Pilates, you could do that. And I imagine there are exercises that I'm not thinking of where you have multi-exercises and you could document them as you go.

### Sets Database cho Analysis

So all the sets are entered here. Again, you're not entering here, but this is wonderful for analysis. If you want to come back, say you're on the free notion plan, the charts and graphs require being on a paid plan. If you're on a free one, you'd come in here and you can analyze the progress by looking at the numbers, the weights and the sets. And you could analyze it through tables. Of course, if you're on any of the paid plans, you can build all kinds of charts and graphs, which we'll look at in a moment.

### Exercise History trong mỗi Exercise

And then as we come down here, you're seeing for each of these, which ones did we add today? We did lat pulls. So, we have some of these entered for today, and we have the previous ones from before. And we have the history of sets with all their reps and weights and everything. in each exercise history.

So it gives you a nice view of which exercises are getting done and the progress you're making. So you might even come in here and just look at how your strength is improving by exercise because that's where you really want to do comparison. Are our lat pulls are we getting stronger in our lateral muscles and you can see how the weight numbers are increasing or the ability to do more reps and maybe that means you need to increase the weight. You know it gives us a great view to do a lot of assessment.

---

## Lưu ý về Bug Notion

### Vấn đề "No Access"

So that is that that is capture. Let me just say one thing because it's possible. Wait, now it's not happening and that makes me happy. But there is a bug in notion when you duplicate the template. When I did this previously, there were a bunch of these entries that said no access. And it's a complete bug in notion because those no access entries were not in the source database that it duplicated from. It's just this quirk. It's it's happened in a few other instances where we shared templates before.

All of the ones that actually have data in the source template will be here. So if you see any no access links, just click on the square, hit minus for the no accesses. No more will be created. It's an artifact of the duplication. So just remove the no accesses to get rid of them and then everything will work perfectly. That's the only little quirk I've seen. That's just a notion quirk. And if we update this template, just as usual, we'll have a last updated date stamp down here so you can see if any updates have been applied to the template.

---

## Q&A về Data Capture

### Mobile Usage

All right. So, let's see if there are any questions or thoughts on this before we move on to the visualizations and analysis. Anyone have any thoughts, questions, ideas? I see some questions. I think these are new. Let me just see where they start.

Okay, so Kristen is asking, "This is cool. I'm wondering how easy it'll be to use on mobile as that's likely when we'll be using it during workouts." Yeah, I mean, it works like any other Notion database. And as you see here, the databases are pretty simple. we get into trouble is where you get multicolumns and we're not doing multicolumns here.

We go into our workout here all stacked single column and really you're you're just hitting new new new for each new workout. But if you want to access the history of the day it's all here you just you scroll down single column table database works very well on mobile. So that was very much in our minds when Jane and I were developing this. So, good question, but yeah, factored in and works well.

### Pre-built Routines

So, Danielle asks, August, would it be better to group them by specific routine workout that automatically open a workout template with all the sets reps set in a table format? They are already grouping by routine. Oh, I see. You're saying you have pre-built routines. You can build pre-routines if you want. This is capture. That's planning. So, that would be designing workouts.

And yeah, you could totally do that. And that's one thing that Strong does. So for sure that's totally an option and notion gives you all that flexibility even to differentiate by workout type because depending the routine exercise order the weights will change a lot messing up the exercise history.

### Data vẫn hoạt động tốt

Yeah but once you've captured it it doesn't matter what the order was really the data is there and it'll be pulling the data. So if I understand your first question it's a very thoughtful one to actually have combinations. You can build that.

So, you could build templates that have pre-built combinations and have, you know, it'll say exercise bench press one, two, three, and the numbers could be blank. And you could just fill them out in pre-built. So, you just build templates that would apply that. And since the templates, you might have a button above to apply the entries. I mean, play with it. Do whatever you want. You got all the flexibility of notion. But the point is we can capture these exercises in the data as we go and then we have all the data to work with.

---

## Data Analysis và Visualizations

### Dashboard Visualizations

So, any other questions? No, I don't see any hands up and I don't see Let me scroll down. Yeah, I don't see any more. So, okay. So, let's go into the data analysis and we will see what we can do with this. Then we'll talk about how to integrate into PPV.

Okay. So, now we just have this second dashboard here which gives us some visualizations. And all of these are examples. You do what is valuable to you, but I'll show you some ideas of what you can do. And these are some of the obvious things I think you would do.

### Yêu cầu Paid Plan

First of all, this is just a note here, and I do highlight that to use charts and graphs, you need to be on any of the paid plans, even the lowest one. But without a paid plan, you only get one chart, and that's pretty limiting. So, this might be worth upgrading or it might not. Up to you.

### Notes và Motivation Box

Once you have read this and understand, you can use this box here to enter ideas, thoughts, inspirations, motivations, notes you want to give to yourself in how you reflect on your workouts. So, it's kind of a mini mindset and identity sculpting box here or any notes or reminders you want to keep in mind. You might even embed a view of your fitness goals. You know, it's a little box for you to put messages to yourself.

### Pie Chart - Workout Mix

On the right, we have a 30-day look at the mix of strength, cycling, and running workouts. So, it's just a pie chart with the various types of exercises pulling from the top table we saw on the previous page where you enter the type of workout you're doing each day. It just gives you a sense of how the mix is and it's, you know, the filter is just for the past 30 days. And the buildout here is very simple and straightforward, but I think it's a pretty useful topline look.

---

## Cardio Tracking Charts

### Distance và Pace Views

And then we come down here. Actually, we can close that. Then we come down here and we get into the real analysis. So break it out however you want. Build your dashboard how you want. But some ideas are we can take the cardio tracking here.

And to track cardio, we are going to be looking at that database, the top level one, the workouts database. This one here. That's where all the cardio exercises or workouts are. So we're pulling from that database.

And what I've done here is for each of the ones I have a different view here. So run distance, cycling distance, run pace, cycling pace. And what I thought would be useful is to see the run distance and the run pace together in a stacked view. So we can see the distance and the pace and the distance and the pace and you can get a sense of how the two are moving together because obviously the two are related and those two I think give you a pretty good view of how your cardio endurance is improving.

### Cycling Charts

So similarly and stacked you know in parallel as well as we now have cycling distance and cycling pace and we're looking at how those two are evolving over time. Now we only have three entries three days. Each thing across the bottom is a date of data but as you do more and more workouts you're going to have a lot more data in a much longer graph. That's also why I keep it full width here. So I thought that was a nice way to evaluate the cardio. But of course, you have all the data to pull from to do everything you want.

---

## Strength Tracking Charts

### Chọn Exercise làm Proxy Metrics

When we start looking at strength tracking, I think the key is to do all of the weightlifting exercises. Might be overkill, but you'll pick a few as proxy metrics. Maybe one for arms, one for legs, one for core, one for shoulders. You pick.

### Total Weight View

And I thought it'd be valuable to look at the total weight. First of all, we're just filtering by bench press. That's how we're making it a bench press view. And then we're bringing in across the bottom across the x-axis we have date to show time. And then the y-axis here is the sum of weights. So all of the weight lifted by bench press because it's filtering for that date. So all the sets added up. So the total weight added up across all the sets.

So that gives you a sense of how much weight you moved in this exercise, the bench press on each of these days. That's one way to look at it. you know, because the number of sets is part of your workout and the number of weight is part of your workout. So, we're sort of combining them.

### Maximum Weight View

Or alternately, there's a view here of maximum weight. So, whichever set had the highest weight is what's showing here. So, similarly, we're showing max weight. So, it showed weight and here we got max. In the other one, we had sum. So, it was totaling in the first view and now showing the highest you reached in this view. This is the more traditional one. Again, you do what's most interesting to you. the combination might be interested.

And you could do this exact view for any of the weight exercises that you want to use as your primary proxies for your strength gains. So that's that.

### Daily Page Metrics

And then I put a place down here. This isn't things we would pull from the weight tracking. This is things we would pull from our daily page entries in our focus zone. So perhaps if you're entering your weight or you're entering your heart rate variable or you're entering your resting heart rate or your hours of sleep per night or your V2 max or your body fat percentage, whatever you're measuring, you could then put charts and graphs in here and that'll really show the results of all your efforts. So that's a good place to park that in this overall view.

---

## Tích hợp vào PPV System

### Đặt Dashboard vào Focus Zone

And then with each of these, okay, so this is a dashboard that shows the visualization and I think that's super valuable and I'm excited about having this in my own system. But in addition, any one of these, let me first go back to the previous page because it applies to both the visualizations and the data capture stuff here.

Actually, let me step back. I'm about to explain how to bring this into the rest of the PPV system. Let me first talk about this entire dashboard. I would bring this into the PPV pro system. So, you'll have the template there. I'd bring it into the focus zone because this is something you sit down and focus on. You could argue it could go in knowledge zone, your call.

Either way, you'd put it in the navigation. And in the same way we added the content pipeline in our previous workshop and the client management, you would similarly drag this in here and bring it in as a data source. So now you have this dashboard built into your system in the focus zone. Of course on these blocks and other pages you could or on the footer you could add links if you want, but this is where it lives and then it's inside your PPV system.

### Embed Views vào Daily Pages

So that's great. Now, one of the places we might consider bringing some of this information, this is not prepped for a workshop. So, that's just a long history of aggregation in the template. Disregard that long list. Obviously, you'll have a shorter list because you'll be managing your action items. But, when you come into our daily entry, we have our daily entry template that we can go in and edit our daily entry template.

And in here, we have some opportunities. We could do what I said in the beginning and just have a checkbox. You know, we have the checkbox here for data tracking. Did you do your tracking? Some of that could be entered up here if it's stuff like weight, V2 max, body fat percentage, whatever, sleep. And those are the properties you could bring in a charts and graphs in the workout visualization page as well. You would of course use this database, which is the cycles database filtered for daily entries to make those charts and graphs.

### Link vs Embed

One option is in the morning startup routine is to have a link here to that dashboard we were just looking at. That's personally what I would do because when you're doing a workout, it's not just something you're quickly doing in your list of morning startup items. It's something you're doing for an extended focused period of time. You're going to be working out for an hour, hour and a half, two hours. And it's more than just plowing through a startup list.

So for me, I'd have it here, but I'd have a link to the whole dashboard, and I'd go there and have the full glory and control of the whole workout dashboard.

### Cách Embed Database View

Alternately, you could embed a view of anything from that that you want. So let's say you were up here and you wanted to embed like the logical one if you did want to embed it might be to embed the workout session so that you could create a new workout page and from that location open the page and do your workout there sort of inside the daily entry page.

Well, all you would need to do if you wanted this is you know the entire database view here is a block. So you would find the block for that. You click that, you go to copy link. And once you've copied the link, you can go anywhere in your system, whether it's the daily pages or as we'll think in a moment in cycle reviews and just paste it. I just copied it from there. I'm now hitting V to paste it. And you have the option, you choose linked database view, and it will embed the whole thing there with the exact same formatting and layout. It used to be that it would jumble it. Now it's the exact same format and layout.

### Filter cho Today

So maybe now you want to screen and make the date that the date is sorry the the filter is that the date is not one month ago but the date is today. So now you have a filtered view of just that for today and that would be a great way to embed that into your daily pages. Let me delete.

So that would be in the focus zone here in our daily pages. We would now have I was in the template but you would add it in the template edit and you could embed that perhaps under a toggle here and that whole thing filtered for just today you'd have your create a new entry do your workout all accessed from here either that or link to the whole dashboard.

### Embed Charts cho Cycle Reviews

Similarly at the end of the day you can or the middle of the day whenever you want to do your workout embed or link to the dashboard as you wish. You can have charts and graphs. So just as I showed you how you can move the entire view of the table, you can do the same thing with all of these visualizations.

So say you want to show how your workout went. You can take this, copy the link, copy link. Yeah. And this can similarly be pasted anywhere. Choose link database view and you get the exact same design visualization anywhere you put it.

So you could put that at the end of your day, although that's probably less useful, but you could. I mean, if you want to see the past week as you're going through day by day, but perhaps that would be more valuable if you were to go into the alignment zone, and you went into your cycles, cycle reviews, and perhaps in the template for weekly reviews or dur cycles or whatever you want, edit. And you can now embed the visualization of your workouts to review your progress.

Similarly, you could embed the database table of your data for the past week, month, whatever. You set the view that would be valuable to you. And now you have built into your daily pages and your cycle reviews all the data that you're capturing in our workout dashboard.

### Tổng kết khả năng tích hợp

So, I just go here and leave this up. So really you can pull anything here, anything here, embed it anywhere else in the system and that is why notion is great and of course you can filter and sort and create charts based on what is of most value to you.

---

## Q&A Session

### Danielle's Questions về Routines

So with that let's open it up and see what thoughts or questions we have. Okay go ahead Daniela you are up.

Hello August. Hello. So I have a couple of question for you. So basically I was talking about the routine before not only for the template but even because basically now that you show the data track so the views of the analysis basically depending the routine it can change a lot and even discourage people for example let's talk about leg exercises if we do squat before and deadlift later and another time we swap those exercises for example basically the data for the squat will drop because doing this like a second precise.

Yeah. So, this is my point and the same for running if you could just choose to do them or you could just choose to do them in the same order and solve that. That's true. But then after a while basically the battery get used so it doesn't progress anymore. And this is true especially for the running. So if we start running and at some point basically our body get used and the point is that our data will not progress anymore. And I don't know this is a bit discouraging to be honest.

### Discussion về Training Periodization

That's why I was kind of setting with routines and especially with on that point. My understanding is that's a call for changing exercises, not changing the order of the exercises. Yeah. I mean the routine like periodically you change your training routine, your running routine in order to not get used. Yeah.

And that's why I was asking for the template like assigning a kind of topic. For example, this month focusing on running, the next month focusing on strength and so on. That's why do it. Yeah.

### Nutrition Data Discussion

Plus, I was even thinking about the nutritional data because I know this is like the main focus and lots of people basically track the body weight in order to lose weight for example and in this case this can affect even the energy level. For example, losing weight of course we will decrease the strength that we have in the gym. So this will decrease the data and when talking about this because we had a discussion in these days in the topic session about basically the focus and the energy level.

So the nutrition of course has a big impact on the focus level because of course if we lose weight our bodies get tired let's say so losing weight consistently is something that really affects everything and that's why I was suggesting even to add the data of the nutrition at least the weekly data from my fitness pal to notion in order to have like a data track and especially when you feel very tired you can kind of see the trend line of the weight and the nutritional data and kind of manage better this stuff. This was my point here.

### Manual Entry từ My Fitness Pal

Yeah, that's great. Does my fitness data export the database tables easily? I don't think so. But you can see the weekly Yeah. Yeah, that's the point. You can see the weekly trend for sure. So, it's easy to manage in few seconds the weekly data to bring in the aggregate. Good. Yeah. Yeah.

Just enter that in the daily pages. You enter that in the daily pages and then you've got it to combine and lay over top. Yeah. I think that's a great point.

### Systems Thinking

Yeah, what you first I'll let you continue, but what what I love here is this is systems thinking and I want to highlight this. So you're saying that there's the exercise that's one thing, but there's it operates within systems within systems within systems and everything's affecting everything. So that's a great point to highlight and we obviously need to always be aware of that.

Yeah, because we had like the discussion about for example the burnout and you know I'm personal trainer and my burnout so the mental burnout is affected even by the nutrition. So when my body fat is too low, I have less energy and of course I'm more prone to the burnouts and that's why is affecting a lot.

### Calories và Macros Entry

The other things is that you were talking about daily data entries about for example the V2 max and this kind of stuff but for example is much more efficient to put the calories data because of course very low amount of calories kilo calories data. Yeah. And the macros split that are literally four data. So, kilo calories, carbs, fat, and protein. And this is a very quick entry, but it changes a lot. Yeah.

So, this would be my suggestion.

### Giới hạn vai trò của August

Let me be clear. I'm not saying what metrics people should track. I'm providing a system for people to track the metrics they want to track or that their coaches and trainers guide them. So, yeah, don't misinterpret anything I'm saying as I'm recommending these exercises. I'm not I'm not recommending what data to track, but I'm explaining how to use Notion to track the data that you and your fitness team choose to track. That's all I'm doing.

Yeah. Yeah. You're giving us an amazing system. So, let's try to manage like improving even more and more. So, we're trying to the best from it. Always.

### Expert Perspective

Good point. Yeah. Good to put it in the context of a real fitness professional and and health professional. So, yeah. I mean you this doesn't replace the need for knowledge and research and coaches and physical therapists and trainers to help determine what you want to track and that's a whole different realm that's really beyond my expertise. So I figure out out the best I can but we have experts like you who can give better insights and of course the part of the the challenge is you read about this you study this and there's a lot of conflicting information. Different people say different things and you can't track everything.

So, you know, do the research you can, find the people you trust and apply the best you can.

So, good points. Yeah, definitely. If I can help you like to add some specific stuff like generic stuff, let's say following the scientific guidelines, I'm very happy to help to be honest. I appreciate that. But yeah, I don't want to get into the business of telling people what to do for the workouts. That's not my thing. But professionals like you are out there to do that. So, systems here, experts are there. Bring them together. I got to stay in my lane.

Thank you. Good points. Good points. And great to hear a true expert perspective on how to put this into context and apply it.

---

## Kết thúc

### Final Thoughts

Well, so any other thoughts or questions on this? I think we've covered what I intended to cover. And Jane, of course, chime in if you have any impulses to elaborate. Always welcome your input as well.

So, any other thoughts? I think I mean I'm seeing if Yeah, looks like the comments I think we're caught up on those. Yeah. So Christian's appreciating Daniellea's thoughts which which were definitely good for context and putting things in a proper relative place. Good. Looks like I don't see any written questions here. So yeah, this is the opportunity to chime in if you want to elaborate or dig in deeper or share experiences.

So we've covered this. So what I'll do is we're going to edit the video, post a video. Under that will be the link to the template and it'll be available.

### Request for Feedback

Any other thoughts or questions? Last call for thoughts and questions. If not, we will wrap it up.

So, is this helpful? Does this take things to a little further than for those of you who use the previous system? Take things further. And does this sound like something that'd be valuable for you guys across the board, new and longtime members? Would love your feedback either here or in the comments next to this when we post the video. I definitely want to hear the thoughts and reactions as we bring out new tools and capabilities in the system.

### Closing

Looks like we covered it. All right, then. In that case, we will wrap it up.

Jane, any final closing thoughts on your end or are we good? I love it. Like I said earlier, this makes me want to work out.

Perfect. And I feel I can learn a lot from you and from Danielle, from experts, but this definitely makes me want to work out.

Yeah, that's how we learn too. We talk and systems like this can highlight things to look at. Not that this is guiding your fitness, but it can raise the questions in discussion with a coach or trainer or whoever you're going to or an AI, you know, if you just want some simple basic advice, sort of generic advice, that's readily available and then of course you go deeper with true experts.

So that is a good point. So hope that's helpful. We'll post this template once the video goes up and we'll go from there. Thanks everybody. Good session. Good exploring ideas with you as always.