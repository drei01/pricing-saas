---
title: "Credit card declines: What do those codes mean?"
date: 2022-10-10T10:04:44+02:00
description: "SaaS companies get very worried when the words \"insufficient funds\" appear on their Stripe dashboard. But why?"
draft: false
tags: ["Stripe", "Errors"]
---

![entrepreneur in a hawaiian shirt sitting on a sofa holding a credit card out looking shocked](/img/credit-card-fail.jpeg)

First, some basics. Your customer makes a purchase and provides their payment details. When you try to charge their credit card, the payment information goes through what's called a Payment Gateway. The payment gateway passes the information on to the cardholder’s bank who will approve or decline the transaction. If the transaction is approved, the funds are transferred from the cardholder’s account to your Stripe account (minus any applicable fees). If the transaction is declined, no funds are transferred.

When a transaction is declined, Stripe will provide a decline code that indicates the reason for the decline. Here’s a list of all the decline codes split into those where it’s safe to try again and those that aren't.

## Try again if you get these codes

Some codes are safe to retry. You'll notice that for some the error message looks like you shouldn't retry (call_issuer for example) but retrying can actually work.

`approve_with_id`

The payment can’t be authorized.

`card_velocity_exceeded`

The customer has exceeded the balance or credit limit available on their card.

`authentication_required`

The transaction requires authentication.

`call_issuer`

unknown reason.

`card_not_supported`

The card does not support this type of purchase.

`generic_decline`

unknown reason.

`issuer_not_available`

The card issuer couldn’t be reached, so the payment couldn’t be authorized.

`no_action_taken`

unknown reason.

`stop_payment_order`

unknown reason.

`transaction_not_allowed`

unknown reason.

`try_again_later`

unknown reason.

`withdrawal_count_limit_exceeded`

The customer has exceeded the balance or credit limit available on their card.

`processing_error`

An error occurred while processing the card.

`reenter_transaction`

The payment couldn’t be processed by the issuer for an unknown reason.

`insufficient_funds`

The card has insufficient funds to complete the purchase.


## Some action needs to be taken for these codes

These codes indicate that something was entered incorrectly. Card details or billing details. Either way, you need to contact the customer to get them to enter their card details again. Otherwise, they need to use another card.

`incorrect_number`

The card number is incorrect.

`incorrect_cvc`

The CVC number is incorrect.

`incorrect_pin`

The PIN entered is incorrect.

`incorrect_zip`

The postal code is incorrect. Check the billing address with the customer

`invalid_account`

The card, or account the card is connected to, is invalid

`invalid_amount`

The payment amount is invalid, or exceeds the amount that’s allowed.

`invalid_cvc`

The CVC number is incorrect.

`invalid_expiry_month`

The expiration month is invalid.

`invalid_expiry_year`

The expiration year is invalid.

`invalid_number`

The card number is incorrect.

`invalid_pin`

The PIN entered is incorrect.


Never retry for these decline codes
-----------------------------------

Retrying payments with these codes will never work. They generally mean the card was lost, stolen or blocked for some security issue. You need to contact your customer and ask them to provide another payment method or contact your bank.

`currency_not_supported`

The card does not support the specified currency.

`do_not_honor`

unknown reason.

`do_not_try_again`

unknown reason.

`duplicate_transaction`

A transaction with identical amount and credit card information was submitted very recently.

`expired_card`

The card has expired. An expired card should never be retried

`fraudulent`

The payment was suspected as fraudulent.

`lost_card`

The card is reported lost.

`merchant_blacklist`

The payment matches a value on the Stripe user’s block list.

`new_account_information_available`

The card, or account the card is connected to, is invalid.

`not_permitted`

The payment isn’t permitted.T

`offline_pin_required`

Some cards require a pin to be entered. This only affects offline transactions, i.e. those in a physical store.

`online_or_offline_pin_required`

The card requires a PIN.

`pickup_card`

The customer can’t use this card to make this payment (it’s possible it was reported lost or stolen).

`pin_try_exceeded`

The allowable number of PIN tries was exceeded.

`restricted_card`

The customer can’t use this card to make this payment (it’s possible it was reported lost or stolen).

`revocation_of_all_authorizations`

declined for an unknown reason.

`revocation_of_authorization`

declined for an unknown reason.

`security_violation`

unknown reason.

`service_not_allowed`

unknown reason.

`stolen_card`

The card is reported stolen.

## When is the best time to retry a card payment

If the payment isn’t successful the first time, you can retry it instead of asking the customer if they have another card to make payment with. Stripe has smart retry rules so be sure to activate them. If you are manually retrying payments. Here are the best time to try:

### The first of the month

People often get paid on the first of the month. If you retry a payment that was blocked for insufficient funds, try it on the first of the month when it’s likely they’ll have just been paid.

### In the middle of the night

Some card payments are declined because the bank is busy or the simply have too many transactions at that moment. It can depend where the business is located. Retrying in the dead of night can greatly improve your chances of success.

### On the weekends

Banks are busy processing direct debits, standing orders and direct deposits on weekdays. Retrying on a Saturday or Sunday gives them more time to clear these money movements and there is more capacity to process your transaction. Again is depends where the business is located.

### Avoid manual retries

While useful when done correctly, manual retries have a number of drawbacks and should only be used to retry payments that are in the “try again“ list above.