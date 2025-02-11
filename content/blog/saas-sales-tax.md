---
title: "Saas Sales Tax"
date: 2021-04-27T20:25:18+02:00
draft: false
tags: ["tax", "sales tax", "saas", "stripe"]
---

## Is my SaaS revenue taxable?

**Hint: Yes it is and there are some nasty fines if you get it wrong, read on...**

That's the question every SaaS founder has to grapple with.
It's likely you will have to pay tax in the countries of your customers (not the country your business is based in). Oh, and there's some pretty nasty fines if you get it wrong. Sales tax is different around the world but in short you need to consider where your customer is. Here's our guide to sales tax for your SaaS.

## Always collect the billing address of your customer

It's important to collect your customer's billing address so you know how much tax to charge (it's different by country and even by state/region within some countries). PriceWell will collect the billing address for you as long as you have this feature enabled (the default) in your Pricing Table, so you don't need to worry about this. In some countries you will need to collect *at least two* forms of evidence for the customer's location. They could be:

- Billing address
- Bank location
- Credit card issuing country
- IP address
- SIM card issuing country

## Wait a minute, you might not have to start paying tax right away

Luckily some places have generous revenue thresholds before you need to worry about paying tax in their jurisdiction. In countries that have no threshold (shown as `0` in our table), you will need to charge sales tax.

## Sales Tax thresholds around the world

Here's a table of countries' tax thresholds <sup>[Source](https://web.archive.org/web/20210227121632/https://www.quaderno.io/resources/sales-tax-for-saas)</sup>

<iframe class="airtable-embed" src="https://airtable.com/embed/shrsVinL4kvx4MCF5?backgroundColor=gray&viewControls=on" frameborder="0" onmousewheel="" width="100%" height="533" style="background: transparent; border: 1px solid #ccc;"></iframe>

## Is your business based in the EU?

If your SaaS is based in the EU, it depends whether you are Business to Business (B2B) or Business to Customer (B2C).

### EU VAT - B2B

You **don't** need to charge VAT because of [reverse-taxation](https://www.avalara.com/vatlive/en/eu-vat-rules/eu-vat-returns/reverse-charge-on-eu-vat.html). However your business **must** be registered for tax and have a VAT number and you must **collect your customer's VAT number**. PriceWell lets you collect your customer's VAT number during payment, you just have to enable this feature in your Pricing Table.

### EU VAT - B2C

If you have under €10,000 in sales per year, you **do** need to charge VAT but only at your country of business rate. Once you go over the €10k threshold, you must use the VAT MOSS scheme and charge the tax rate of your buyer's country (not your business country).

*Example:*
*My business is based in Germany and sells (B2C) to the rest of the EU. As long as my sales are under €10,000 per year I must charge 19% VAT (the rate in Germany) on all sales. As soon as I go over that threshold, I must charge the relevant VAT rate in the customer's country and register for [VAT MOSS](https://europa.eu/youreurope/business/taxation/vat/vat-digital-services-moss-scheme/index_en.htm)*

## Which countries do I need to register for VAT in?

If you aren't EU based or you are planning to sell outside the EU, then you'll likely need to register to pay VAT in one or more countries.

Avalara has a [risk calculator](https://vat-risk-assessment.avalara.com/risk-assessment) to help you determine which countries you need to register in.
