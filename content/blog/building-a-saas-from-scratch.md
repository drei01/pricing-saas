---
title: "Building a Saas From Scratch"
date: 2021-04-26T20:17:24+02:00
draft: false
tags: ["SaaS", "Stripe", "Billing"]
---

Comfortable with code and looking for tutorials on building a SaaS? [Check out saasbase.dev](https://saasbase.dev)

## Here's what you need to build a SaaS from the ground up

We've put together a killer list of tips to make building your SaaS a breeze. We undertook all this time consuming research so you don't have to.

Here's what you are going to need:

- A landing page
- The ability to collect payments
- User registration and authentication
- User onboarding

### Landing page

![an open laptop displaying a product landing page. coffee cup and writing tools nearby](/img/laptop-landing-page.jpg)

Before you go ahead and build anything else, you are going to need to validate your idea. One of the cheapest ways to do this is to build a landing page, send people to it (via twitter/facebook/linkedin posts or google ads etc.) and see if there's interest. You want to make your landing page actionable and the best way to determine if your product has real interest is to [charge for it up front using pre-sales](https://saasbase.dev/guides/pre-sales/collect-pre-sales-revenue-from-early-adopters-using-the-stripe-api). It's very low friction to enter an email address into a site but making an actual payment requires real commitment from a potential customer. If people are paying for your product before you've actually built it, then you know you are on to something.

💡 *Tip: you can email buyers as soon as they paid, explaining that they product doesn't exist yet and offer a full refund (most people will wait for the product!)*

Now you've determined that there is real demand for your product, it's time to get building. The core functionality is going to be unique to each SaaS but the basics are the same no matter what you are building

### Payments

![hand holding a credit card near a laptop](/img/entering-credit-card.jpg)

From your pricing page to collecting and managing subscriptions, payments are the bread and butter of your SaaS. Let's face it, without them you don't have a business at all. You can't go anywhere in the SaaS world without hearing about Stripe, they are by far the largest payment provider in the business and with good reason. They have top notch API documentation, all the features you will ever want and reasonable pricing. 

#### The trick to saving weeks integrating subscription payments

The problem is, coding all the subscription payment architecture will take you weeks. That's time you could be spending building your actual application (remember, the one you pre-sales customers already paid for?). We at [PriceWell](https://www.pricewell.io) have got you covered. PriceWell is built on top of Stripe so you can rely on their underlying infrastructure and use our drag and drop interface to get your subscriptions up and running in **minutes**, not weeks (yes, you read that right, minutes).

### User registration and authentication

![person holding an iphone with thumbs poised to enter password](/img/login-to-instagram.jpg)

Every developer has built some kind of user login or registration system. Every system that charges for content needs one but they are a tricky thing to get right. How do you support multiple languages? What happens if a user forgets their password? How you do prevent brute force attacks and other security vulnerabilities? How do you store the passwords? The list goes on...

Luckily, there's a wave of recent innovations that mean you no longer have to build user authentication yourself. Here's a few options:

- [Firebase Authentication](https://firebase.google.com/docs/auth/)
- [Keycloak](https://www.keycloak.org/)
- [Auth0](https://auth0.com)

Keycloak and Auth0 are stand alone systems that focus on one thing, making sure user registration and login is fast, secure and convenient. Keycloak is open source so you can even host your own instance to avoid paying subscription fees. Firebase Authentication is built into the Firebase platform so if you are already using their realtime database or serverless functions, it's a no-brainer. If you have yet to choose a database this could also be a good option to begin with as they have a generous free tier. Be aware that Firebase can get expensive if you start getting serious traffic, although once you get to this level you are hopefully making enough money not to worry about that.

### Onboarding

Once a user has registered with your SaaS, you just leave them to get on with it right? Wrong, a proper onboarding is **vital** to the success of your SaaS business. It might not be immediately obvious to new users how they should get started using your app or what functionality your app offers. A good user onboarding highlights your product's value and shows the user the difference between their expectation and what your product will actually help them do.

> User onboarding is a vital tool for customer retention

#### Types of user onboarding

- Drip emails
- Product tours

#### Drip emails

These are sequences of emails that the user receives (1 per day) after they register for an account. They serve to educate the user on the value of your product and remind them to come back to the app. You can build drip emails in tools like:
- [Drip](https://drip.com?utm_source=pricewell)
- [Engage](https://engage.so?utm_source=pricewell)

#### Product tours

This are in-app tours highlighting how to use the product. You know the ones, where the screen goes dark and an arrow highlights which buttons to click. You can build product tours in tools like [Driftly](https://driftly.app/?utm_source=pricewell).

Good luck building your SaaS and feel free to <a href="javascript:$crisp.push(['do', 'chat:open']);"
                        class="text-blue-600 underline">get in contact</a> if you have any thoughts on this article.
