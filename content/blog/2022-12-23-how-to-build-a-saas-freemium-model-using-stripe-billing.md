---
title: How to  Build a SaaS Freemium Model using Stripe Billing
date: 2022-12-23T13:22:03.125Z
description: An easy, quick handbook on building a freemium billing model for you business
---
This guide explains how to build a fully-functional Freemium SaaS business model with Stripe Billing and PriceWell![](https://lh3.googleusercontent.com/zVZnboR0yFdcIGtCxrx1-EhCr5FPJIxg7X_yQqfI_Y99JDgV8UUgI2Ier6kRylXt82K7g61lbCGMUhoV8DvYmEd_7pBBGNYB4D6aKO0rKN_ojLYklgs2YcNBvcm5ZPwjRReB0DbozUOta5mA-vGUxKleAzi3tnHEM_HmdRNO9fL5L3ocT0oeta1-nYa9)

<!--EndFragment-->

- - -

<!--StartFragment-->

Whether you are creating a brand new SaaS product or updating the pricing model and/or onboarding process, a basic understanding of the billing flow architecture is necessary.

# SaaS Freemium Logic

Trying to understand the SaaS Freemium Flow architecture there are 5 distinct steps the user needs to follow. ![](https://lh6.googleusercontent.com/lbmZa1OkYCWC8YqHTSPfCDMpNF25yZcdDydykjcCpDFMhsPY2ofvqcgXAS3Oah9_OQiYqtxg-6p2kmtuukymCa3dRlu8u3euYo5h0tW4PwZ7iqyIsMHUccORNHJ3zvdhel1VI47ZJS0mrJ10RekZ9sh5HCbkOr7cPqJ3_a-Ed4O9qRWiAI84kN2mjO6I)

\
**Pricing on the Landing Page**: Users see the pricing table -with some slick features and some cool design. That can be a static HTML page or a dynamically Stripe populated table from Products and Prices.

**Users Create a Free Account**: With the Authentication System, users can create a free account and use the services allowed to the free plan. Credit Card credentials are optional on that part of the logic flow - but really important if you are building on Stripe, just because Stripe does not let you create a Customer without collecting their payment details.\
[\-You can do that alternatively with PriceWell-](https://headwayapp.co/pricewell-changelog)

**Users use the freemium features**: Give value through the most basic features that solve the pain point of your users.

**User upgrades their plan to use premium features**: As soon as the user grasps the initial value, will try to upgrade to premium features through the [Customer Portal](https://www.pricewell.io/customer-portal/)

**Users manage their subscription:** Think of the customer portal as your Billing HQ, where Users can view their billing plan details, update credit card, upgrade or downgrade between plans, download and automate invoice sending.

# Integrate Stripe Billing with your SaaS

![The logic flow customers subscribe and manage their payments through a billing portal](/img/arrows.jpg "Billing Logic Flow in Freemium")

In the freemium model, the billing system comes into play the moment when your customer upgrades to one of your premium plans. In the case, you are not using [Stripe Billing](https://stripe.com/en-fr/billing) , connecting your Stripe Account to [PriceWell](https://www.pricewell.io/) will automatically allow you to use Stripe Billing’s full range of capabilities. 

A common practice many SaaS companies use is to refrain from creating a customer, or a so-called “subscription object” into your billing system until the customer has upgraded to a premium account.\
\
The difference is in the structure and logic of your billing flow and the compatibility with the company’s business model and acquisition strategy. 



# **Stripe Webhooks - How to use them**

![The differences between webhooks and APIs with a nice analogy](/img/webhooks.png "Webhooks vs. APIs")

In the freemium model, the billing system comes into play the moment when your customer upgrades to one of your premium plans. In the case, you are not using [Stripe Billing](https://stripe.com/en-fr/billing) , connecting your Stripe Account to [PriceWell](https://www.pricewell.io/) will automatically allow you to use Stripe Billing’s full range of capabilities. 

A common practice many SaaS companies use is to refrain from creating a customer, or a so-called “subscription object” into your billing system until the customer has upgraded to a premium account.The difference is in the structure and logic of your billing flow and the compatibility with the company’s business model and acquisition strategy.

Syncing the Stripe subscription data with your SaaS is the last and final step to create your freemium billing system. The most efficient way to retrieve and safely store this data is to go by Stripe’s webhooks. 

The 3 most important webhooks you should use are:

customer.subscription.created - Whenever a customer subscribes to a new plan

customer.subscription.deleted - Whenever a customer cancels the subscription

customer.subscription.updated - Whenever a subscription changes - upgrades or downgrades between plans.



# Gated Content 🔐

Ever wanted to hide a page on your website from those who aren't subscribers?\
Well, we've come up with the easiest way in the world 🌎 to do it.\
Configure which URLs should be restricted\
Drop the generated snippet into your website\
Now anyone visiting the restricted pages must have a Stripe customer (with an active, non-zero subscription) that matches their email address.

![Manage Subscriptions with an easy efortless way without integrating coding](/img/gifs.gif "Subscription Management Button and Capabilities")

<!--EndFragment-->