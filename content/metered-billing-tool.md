---
title: Stripe invoice PDF generator
date: 2023-10-27T00:54:28+01:00
draft: false
type: page
description: Stripe collect cancellation reasons from customers and provide insights into how they are using their subscriptions.
---
{{<rawhtml>}}
    <div class="py-12 md:py-24">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
        <div class="order-1 col-span-2 self-center my-12 md:my-0">
            <h1 class="text-gray-800 text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4 lg:mb-8">
             Stripe <br/>
                Metered Billing? <br/> Report usage without code.
            </h1>
            <div class="flex space-x-4 mt-6">
                <a href="https://app.pricewell.io/register"
                    class="button"
                    data-analytics="Signup"
                >
                    Stripe Usage Reporting Tool
                </a>
            </div>

            <p class="text-gray-500 text-sm">No credit card required.</p>
        </div>
        <div class="order-2 col-span-2 xl:col-span-3 flex-col">
            <img src='/img/usage-billing-tool.gif' class="rounded-lg shadow-2xl" alt="" />

        </div>
    </div>

</div>


<div class="py-12 md:py-24 pb-12 lg:pb-16 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-1 col-span-2 xl:col-span-3 self-center">
                <img src='img/usage-billing-tweet.png' class="rounded-lg shadow-2xl" alt="" />
                
            </div>
            <div class="order-2 col-span-2 mt-12 md:mt-0">
                <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Charge customers for what they use... <span class="underline">pain free</span>.
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                   Metered billing or usage-based billing is a common pricing model for SaaS companies. It's a great way to charge customers for what they use. But it's not easy to implement. We make it easy to report usage to Stripe without code.
                </p>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                We're the only tool on the market that lets you do this. Check out the <a href="https://help.pricewell.com/features/metered-billing/" class="text-blue-600 underline">documentation</a> to see all the features in action.
                </p>
            </div>
        </div>
    </div>

{{<partial "testimonials">}}


<div class="bg-gray-100">
<div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 py-12 lg:py-16 xl:py-24">
    <div class="text-center mb-6 md:mb-8">
        <h2 id="pricing" class="text-black text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4">We charge a flat fee, that's it</h2>
        <p class="text-lg xl:text-xl text-gray-800 relative w-1/2 m-auto">Oh, and our pricing is made with PriceWell <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 372.136 372.136" class="w-12 ml-10 transform rotate-120 fill-current text-black"><path d="M371.682 143.271c-14.688-44.676-26.316-90.576-50.797-131.58-2.447-4.284-10.403-5.508-12.239 0-17.748 42.228-36.108 83.844-47.736 127.908-1.836 7.344 7.344 12.852 12.852 7.344 10.404-10.404 21.421-20.196 33.049-28.764-1.225 90.576 1.836 195.84-105.876 223.992-47.736 12.24-100.98 5.509-140.76-25.092C18.557 284.644 9.377 231.4 12.437 181.828c0-4.896-7.344-6.12-8.568-1.224-23.868 110.772 66.096 197.064 176.256 181.764 54.468-7.344 100.368-33.048 123.624-85.068 20.809-46.512 19.584-102.204 18.36-153 11.628 10.404 24.479 19.584 37.943 26.928 6.121 3.672 14.077-1.224 11.63-7.957zm-55.08-40.391c-3.672-1.224-6.12.612-7.345 3.672l-.611.612c-9.792 3.06-18.36 7.956-26.316 13.464 9.18-29.988 21.42-59.364 33.048-88.128 15.912 29.988 25.092 62.424 35.496 94.248-11.017-9.18-21.421-18.36-34.272-23.868z"/></svg></p>
    </div>

    {{< partial "pricing" >}}

    <div class="pt-8">
    {{<partial "pricing-explainer">}}
    </div>

</div>
</div>
{{</rawhtml>}}