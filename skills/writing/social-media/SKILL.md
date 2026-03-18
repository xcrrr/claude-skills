---
name: social-media
description: "Use this skill when writing platform-specific social media content—Twitter/X threads, LinkedIn posts, Instagram captions, or short-form content designed to drive engagement, shares, or follows. Trigger phrases: 'write a tweet about', 'create a LinkedIn post', 'write an Instagram caption', 'write a thread'. Do NOT use for long-form articles or blog posts, or email newsletters."
version: 1.0.0
author: community
tags: [writing, social-media, twitter, linkedin, instagram]
license: MIT
---

# Social Media

## Overview
This skill writes platform-native social media content calibrated to the character limits, audience behaviors, and content formats of Twitter/X, LinkedIn, and Instagram. It applies engagement hooks that stop the scroll, formats threads for maximum readability, and uses hashtag strategy that extends reach without looking spammy. The output matches the voice and goals of the brand or individual—whether that's thought leadership on LinkedIn, a viral Twitter/X thread, or an Instagram caption that drives saves and shares.

## When to Use
- Writing individual posts or captions for any social platform
- Creating Twitter/X threads on a topic, insight, or story
- Drafting LinkedIn posts for professional thought leadership
- Writing Instagram captions for personal or brand accounts
- Repurposing longer content (blog posts, talks, reports) into social snippets
- Writing a series of posts for a campaign or content calendar
- Crafting engagement bait: polls, questions, conversation starters

## When NOT to Use
- Blog posts or articles (use `blog-post` skill)
- Email newsletters or marketing sequences (use `email-drafter` or `copywriter` skills)
- Paid social ad copy (use `copywriter` skill for CTA-optimized ad formats)
- Content requiring extensive detail, nuance, or citation (use `blog-post` skill)

## Quick Reference
| Platform | Character Limit | Best Format | Hashtags | Tone |
|----------|----------------|-------------|----------|------|
| Twitter/X | 280 chars/tweet | Short punchy takes, threads | 0–2 | Casual, bold, conversational |
| LinkedIn | 3,000 chars | Short-form post or mini-essay | 3–5 | Professional, warm, personal |
| Instagram | 2,200 chars | Caption + hashtags | 5–15 in caption or comments | Aspirational, authentic |
| Threads | 500 chars | Casual, conversational | 0–1 | Very casual, reactive |

## Instructions

1. **Identify the platform, goal, and audience.** The same idea written for LinkedIn and written for Twitter/X should look completely different. Confirm: What platform? What is the goal (engagement, followers, website traffic, brand awareness)? Who is the target reader?

2. **Write the hook first.** The first line is everything. On every platform, users see only the first line before deciding to click "more." Hooks that work:
   - Bold claim: "Most productivity advice is wrong."
   - Counterintuitive fact: "The best writers write less, not more."
   - Specific number: "I analyzed 500 viral LinkedIn posts. Here's what they all had in common:"
   - Personal story start: "3 years ago I got fired. Best thing that ever happened to me."
   - Direct question: "What does your morning routine actually accomplish?"
   - Provocative question: "Are you optimizing for the wrong metric?"

3. **Write platform-native content.**

   **Twitter/X (Individual Tweet):**
   - Max 280 characters; aim for 200–240 to leave room for quote-tweets
   - One idea per tweet—no hedging, no "however"
   - Lists of 3 work well in single tweets
   - End with a question to drive replies (but not every tweet)

   **Twitter/X Thread:**
   - Tweet 1: Hook + preview of what's coming ("Here's what I learned:")
   - Tweets 2–N: One point per tweet, numbered (2/ 3/ 4/)
   - Each tweet must work standalone AND flow to the next
   - Second-to-last tweet: summarize key takeaways
   - Last tweet: CTA (follow, retweet, link to article)

   **LinkedIn Post:**
   - Optimal length: 150–300 words for engagement posts; up to 700 for mini-essays
   - First line ends mid-thought or is provocative—forces "see more" click
   - Use line breaks liberally; no wall of text
   - One idea per paragraph
   - End with a question to drive comments
   - Avoid link-in-post (LinkedIn suppresses reach); put links in comments

   **Instagram Caption:**
   - Lead line: strong hook visible before "more"
   - Body: story, context, or value; can be longer on educational accounts
   - Hashtags: 5–15, mix of high-volume (#marketing) and niche (#b2bmarketing); put them at the end or in first comment
   - CTA: tell them to save, share, comment, or click the link in bio

4. **Apply hashtag strategy.**
   - Twitter/X: 0–2 hashtags; more looks spammy. Only use if it's a trending topic or community tag.
   - LinkedIn: 3–5 hashtags at the end; mix of broad and niche
   - Instagram: 5–15; use a mix of sizes. Avoid banned hashtags. Consider putting in first comment.
   - Choose hashtags based on where your target audience actually hangs out, not just volume

5. **Match the voice to the person/brand.** Ask:
   - Formal or casual? ("We believe" vs. "I think")
   - Personal stories included, or stays topic-focused?
   - Humor and personality, or straight expertise?
   - Uses "you" and addresses reader directly, or broadcasts?

6. **Write the CTA.** Every post that has a business goal needs one action. But not every post—some posts build brand equity without a hard ask.
   - Engagement: "What would you add?" / "Do you agree or disagree?"
   - Traffic: "Full article in bio" / "Thread link in comments"
   - Follow: "Follow for more posts like this"
   - Save: "Save this for later when you need it"

## Examples

### Example 1: Twitter/X Thread

**Input:** "Write a Twitter thread about the 5 biggest mistakes people make when learning to code, from the perspective of a self-taught developer. Conversational tone."

**Output:**

---

**Tweet 1 (Hook):**
I've watched hundreds of people fail to learn to code.

Most quit for the same 5 reasons. Here's what they are—and how to avoid them:🧵

---

**Tweet 2:**
1/ Starting with the wrong language.

"What's the best first language?" is the wrong question.

The right question: "What do I want to build?"

Want web apps? Start with JavaScript.
Data stuff? Python.
iOS apps? Swift.

Language matters less than building something you care about.

---

**Tweet 3:**
2/ Tutorial hell.

You've done 40 hours of tutorials. You feel like you're learning.

But you've never built anything yourself.

Tutorials give you the illusion of progress. Real projects give you the actual thing.

After every tutorial section → build a mini version yourself. No looking back.

---

**Tweet 4:**
3/ Trying to understand everything before moving on.

You don't need to know why `git rebase -i HEAD~3` works to use it.

Use it. It works. Move on.

Understanding comes from exposure over time, not from refusing to proceed until you've memorized the docs.

---

**Tweet 5:**
4/ Learning alone.

The fastest thing I ever did was join a Discord server of other learners.

When you're stuck, you get unstuck in 20 minutes instead of 3 days.

When they're stuck, explaining it to them cements your own understanding.

Community is not a nice-to-have.

---

**Tweet 6:**
5/ Stopping when it gets hard.

There's a moment around week 3–4 where everything feels impossible.

This is not a sign you're bad at coding. It's a sign you're learning to think differently.

Everyone hits this wall. The ones who make it are the ones who treat it as a rite of passage, not a stop sign.

---

**Tweet 7 (Summary):**
To recap:

→ Build things you care about
→ Escape tutorial hell
→ Use before you understand
→ Learn with other people
→ Push through the hard weeks

Self-taught is hard. It's also completely possible.

---

**Tweet 8 (CTA):**
If this was useful, RT the first tweet so other learners see it.

I post about self-teaching, building in public, and dev career stuff. Follow along if that's your thing.

---

### Example 2: LinkedIn Post

**Input:** "Write a LinkedIn post about why hiring managers should stop filtering out candidates who have employment gaps. Written in first person, from the perspective of an HR consultant. Professional but personal tone."

**Output:**

---

I hired someone last year who had a 2-year gap on their resume.

My ATS almost filtered them out automatically. I'm glad I didn't let it.

That candidate had spent those two years:
→ Caring for a parent with Alzheimer's
→ Running household finances under pressure
→ Managing a team of visiting caregivers and medical providers

When I interviewed them, they were the most emotionally intelligent, operationally organized candidate I'd seen in a year of hiring.

The employment gap told me almost nothing useful.

Here's what I wish more hiring managers would internalize:

A resume gap is not a signal of professional failure. It's a signal that life happened.

Candidates take gaps for illness, caregiving, layoffs, mental health, travel, and a hundred other legitimate reasons. None of those things predict job performance.

What predicts job performance? Skills. References. Track record in prior roles. How they think through problems in your interview.

I've seen people with pristine, unbroken work histories who were catastrophically bad employees.

The next time your ATS flags a gap, stop. Read the resume. Ask the question.

"What were you doing during this time?"

Then actually listen to the answer.

---

Hiring practices that haven't been examined in 10 years deserve a second look.

What's one outdated hiring assumption you've seen cause real harm?

#Hiring #HR #TalentAcquisition #Leadership

---

**Why it works:**
- First line hooks with a specific, human story
- Arrow-formatted list is LinkedIn native and easy to scan
- "I" throughout—personal voice builds trust
- Ends with a question to drive comments
- 3 relevant hashtags (not over-stuffed)
- No links in post (added in comments to avoid reach suppression)

---

### Example 3: Instagram Caption

**Input:** "Write an Instagram caption for a coffee brand (@morninglab) posting a photo of a pour-over setup at golden hour. Product: single-origin Ethiopia beans. Goal: drive saves and engagement."

**Output:**

---

The slowest part of your morning is the best part of your day.

This is our Ethiopia Yirgacheffe in a Hario V60, shot just before 7am on a Tuesday.

Notes of blueberry, jasmine, and something we can never quite name but keep reaching for.

Pour-over isn't just a brewing method. It's a pace. A reminder that some things get better when you slow down and pay attention.

If your mornings feel like a sprint, this one's for you. ☕

---

Save this for when you need a reminder to slow down.
Tag someone who needs a better morning ritual.

📦 Ethiopia Yirgacheffe available now — link in bio.

—

#pourovercoffee #coffeeathome #morningritual #singleorigin #coffeephotography #v60 #yirgacheffe #slowmorning #morninglab #coffeelovers

---

## Best Practices
- Write the hook before anything else—if the first line doesn't stop the scroll, nothing else matters
- Repurpose long-form content by extracting the single best insight—don't summarize, extract
- Match vocabulary to platform: LinkedIn allows "leverage" and "stakeholders"; Twitter/X prefers "use" and "teams"
- Post consistently over posting perfectly—a good post published beats a perfect post in perpetual draft
- Use the platform yourself; you can't write great LinkedIn posts if you never read LinkedIn
- Vary your content types: tips → stories → opinions → questions → behind-the-scenes

## Common Mistakes
- **Same post on every platform:** Copy-pasting from LinkedIn to Twitter breaks both; adapt to each platform
- **Hashtag stuffing on Twitter:** More than 2 hashtags on a tweet hurts reach and looks desperate
- **Weak hook → "See more" never clicked:** If the first line doesn't create curiosity or value, the rest doesn't matter
- **Link in LinkedIn post body:** LinkedIn's algorithm significantly suppresses posts with external links; put the link in the comments
- **Closing with a generic CTA:** "Let me know your thoughts" is lazy. "What's the one thing you'd add?" drives more responses
- **Writing to broadcast, not engage:** Social media is conversation. Ask questions. Reply to comments.

## Tips & Tricks
- For LinkedIn, break after every 1–3 sentences—white space is reach
- A Twitter thread's first tweet is the ad; the rest is the product—make the hook irresistible
- "Save this post" is Instagram's highest-value CTA because saves are weighted heavily in the algorithm
- For Instagram captions, put the hashtags after a line break or in the first comment to keep the caption clean
- The best time to post varies by audience—test and check your platform analytics rather than following generic advice
- Engaging with comments in the first hour of posting dramatically improves reach across all platforms

## Related Skills
- [blog-post](../../writing/blog-post/SKILL.md)
- [copywriter](../../writing/copywriter/SKILL.md)
- [storyteller](../../writing/storyteller/SKILL.md)
