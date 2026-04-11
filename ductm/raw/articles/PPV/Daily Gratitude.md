## Giới thiệu Use Case

Let me first explain to everyone what you have described as the use case example is, and if I have missed anything or there's anything you wanna clarify, feel free to jump in.

Okay, so David mentioned this use case in a previous Q&A and then he will like to see the demo here. So what he will like to do is in our daily template there is a section called gratitude. What am I grateful for? So this is the default setup in the PP system in the daily template is that you enter your gratitude notes here inside each page in this section in the template.

What Davey will like to do is he wants to instead not do it in this section but be able to review it without going into each daily page to see what he's grateful for. So essentially he wants a gratitude capturing that is made for reviewing and that reviewing doesn't involve going into each daily page.

Is that a good description of what you wanna do, David? Yeah, definitely. Okay.

---

## Hai phương án được đề xuất

And previously we have talked about two options that we recommend the most.

### Phương án 1: Gratitude như một Property trong Daily Fields

One is you'll essentially add the gratitude note as a property right in the daily fields here, as with other like improvements or other things that you wanna track. So you just add this property here in the daily fields and then in your dual cycles that's where you wanna do.

So we recommend reviewing these things in weekly because there are only seven days of gratitude that you need to review versus in dual cycles you need to review 61 days of gratitude notes. But David mentioned in the comment that he prefers to review them in dual cycles, so a large quantity.

So we will essentially need to create an embedded view of the dailies so that you can see 61 days. So the gratitude notes the gratitude property from the past two months. So that's option one is to enter your gratitude in a property.

### Phương án 2: Gratitude trong Perpetual Neuro Bit

The other option which we have talked about is enter gratitude in a perpetual neuro bit. What you do there is create an ongoing gratitude neuro bit. Then you'll enter your gratitude always in this nobit page.

And then you just simply need to link this page in your daily, like every day when you're entering a gratitude note. Instead of entering here, you'll see a page link and you'll just go to that page. And in your dual cycle it's the same thing. You will link to this gratitude page so you can review your gratitude notes in that page.

---

## Demo: Phương án 1 — Gratitude Property

So let me show you the two approaches first.

So this is our dual cycle template. This is what it looks like if you're reviewing your daily gratitude as a property. Remember that the gratitude is a property in the daily field. You'll have a toggle in your dual cycle template where it's listing all of your gratitude. Note. It's similar to improvement 'cause it's just text.

Then you'll look through two months of gratitude note. And then if there are anything you wanna highlight or your own reflection or things you wanna summarize, you can enter it here.

### Cách thiết lập Embedded View

So this is one setup and let me show you how to set up this. You're going to embed the daily view and what you do is in the cycles database, you're gonna go to a daily view and copy link to view, make sure that you can just copy a daily view instead of having to create one from scratch.

And then you're going to embed this view here in a toggle that you created. 'Cause you don't want it to expand 'cause it's way too long if you wanna expand it. So we better hide this in a toggle called daily Gratitude.

### Cài đặt Filter

And let me show you the filter. That's the most important thing is the type is daily, which should be copied just from that view. And then create a date. Start date is relative to today, past two months 'cause this is a dual cycle. So you're seeing your notes from the past two months.

And visibility is another thing. You need to make sure you're seeing your gratitude and anything else that you might wanna review like improvement. But the most important one, since you wanna review gratitude, make sure that gratitude property is visible so we can read through what you wrote.

So that's the first approach and after I talk about the other one, I show you the other one. I'll tell you the comparison between the two and what I think is probably best for you.

---

## Demo: Phương án 2 — Perpetual Neural Bit Page

So the next approach is enter gratitude in a perpetual neural bit page. So you see already linked it here. So in your dual cycle template and in your daily template, very simple, you just uh link to this page and you just go there.

### Tạo Neural Bit

Very simple. So create a neural bit and you can tag it to a topic if you want. But right now we don't have a gratitude topic. So you could do mindset, identity, sculpting, anything that you think fit or you have other topics that's better. But if you don't have a topic for it, you could leave it blank.

But ideally you might want to have a property for your daily gratitude. Perpetual gratitude note. And this is a note category is personal and value is excellent 'cause you'll be reviewing this one a lot. So you wanna make sure this one has an excellent value. So it's always listed, sorted at the top. The status is in progress because it's a perpetually updated page. So it's in progress for the status.

### Cách nhập Gratitude hàng ngày

So what am I grateful for? This is copied over from the daily template, this description. So what you do is you enter each day here you add one entry per day as a dated line. So you will say add today and then what am I grateful for? Enter it here.

And when you're done you can either leave it here or if you don't wanna review it by the end of the day you will move the previous entry before the next day. So if you want a blank section here, the next time you come here, what you simply need to do is move the previous entry under appropriate monthly toggle.

### Tổ chức theo tháng

So you create a February toggle 'cause we're in February and you just drag it here and you're done. Now you've organized it into the February toggle.

The one thing I wanna notice default is when you just drag something and drop it into a toggle is automatically the latest one is at the bottom. So if you want to reorganize you can just move it at the top and that's it. So that's your February dated gratitude. You can just review your February notes here.

You're gonna organize as you go, move the previous entries under the appropriate monthly toggle. If you wanna do two month toggle, you can January, February. So the prior days stay hidden by default.

### Tổ chức theo năm

And then to organize by year. 'Cause you are gonna have 12 months each year and then have next 12 months. You just need to drag it into this toggle. You can drop it in here and that's why you're done with this month. And the next month you just create a new toggle called March and start organizing the March notes here.

### Review và tóm tắt

And during review you will open only the relevant monthly or two month toggle to scan the entries and highlight keywords. And at the top of each monthly toggle, this is something you mentioned in the comment that you can add a short summary line, a summary box. So you can write in your own summary.

Having reviewed your gratitude notes and some standout highlighted words, you can put them here for later review that. You don't need to go through these list again, you can just look at what you have summarized or highlighted.

And then most importantly, you'll link to this page in your daily and in your dual cycle. So we are actually here in this page coming from dual cycle. So that's how easy it is.

---

## Tóm tắt các bước chính

So these are the two approaches. Let me briefly just walk through the key steps again.

### Các bước cho Phương án 1: Gratitude Property

So for enter gratitude as the daily property, you'll add a new text property in the daily view called gratitude. So you will add it here in the daily field 'cause this is something you're entering daily.

And then you'll enter your gratitude reflection in the gratitude property instead of in the daily page body because you want to review it as part of a database. And in the dual cycle template, you will embed the daily database view for reviewing your gratitude. And you're gonna make sure the gratitude property is visible in this embedded view. And set the embedded views date filter to past two months. 'Cause you wanna review. That's the time range you wanna review. That's the first approach.

### Các bước cho Phương án 2: Perpetual Neural Bit

Second approach, again, quick rundown. Enter gratitude in a perpetual neural bit. You will create one ongoing gratitude neural bit. Then you will group daily gratitude texts using a month or two month toggle.

And then in this neural page you can add one entry per day as a dated line and you can move previous entries under the appropriate monthly toggle. So prior days to stay hidden by default.

And during the review, open only the relevant monthly or two month toggle to skin entries and highlight keywords at the top of each toggle. Add a short summary of patterns or standout highlighted words. And then link this gratitude neural bid in your daily and the dual cycle template for quick access.

---

## So sánh hai phương án

So these are the two approaches. Both of them are very practical.

### Phương án 1: Database Customization

The main differences are the first approach, which is creating it as a property in the database. This is database customization because daily is not a database, it's part of the cycles database. So when you're making changes, when you're adding a property that is applied to the entire database, of course you're using it for daily purpose. But this is database customization, which is entering gratitude as a property.

And this gratitude is data in itself. So it's less expressive because every day you're looking at it, this property and you're entering it. So it's less freeform, it's less expressive and it's review friendly. Beyond scanning, you know you can't format or organize however you want 'cause you're limited to just a property that you're reviewing. So it's good for scanning. But beyond that you're quite limited.

And to add the property and review it in dual cycles, it involves database modifications and database embed. And that's what it just show you. You do need a brain, a data database here, the cycles database, a filter for daily and then create your time range, the date range that I wrote review. So that's the first option. And that's database customization essentially.

### Phương án 2: Page Customization

So the second option, this is not database customization, this is page customization. Page customization is always simpler than database customizations.

So for the capture part is better for freeform reflection and pattern review. And it takes a little bit of a upkeep to manually group things and you know, organize them. But you have a lot more freedom with formatting your notes and formatting this entire page and the layout.

So when it comes to personalization, a page is always better. You can't really personalize a property, but you can personalize a page however you want. You can truly make this page your gratitude dashboard or your gratitude central if you will. So whatever you do in this page does not change or interfere with another database. It doesn't involve another database.

So this is just a page that you created and you can customize, personalize however you want, and to put it in cycles. It's a simple plugin, you just need to tack at this page, like link to this page and that's all.

---

## Khuyến nghị

So I would say for technical simplicity, entering gratitude note in a neuro bit page is what I recommend the most for you. But if you want to set up the database option, I completely understand and both of 'em are very practical. It just, this is a lot more customization and you never need to worry about changing a database. This is just a page that you can customize however you want. This is your gratitude central.

---

## Phản hồi từ David

So having said that, what do you think David?

Those are two good approaches for me. When I'm doing gratitude, I've done it in the past. It's usually just a single word. I don't really like flush it out much. And I try not to repeat the word, but within like a couple of months if it's important, you know, like if it's family related and something very significant happened with my family, I will put them down a second time within like a couple of months. That's the way I've used gratitude list in the past. It's just like a single word or two.