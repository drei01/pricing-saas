---
title: "Vs Stripe Checkout"
date: 2021-03-24T11:10:31+01:00
description: Stripe Customer Portal without coding. Implement PriceWell in minutes and save money.
draft: false
---

{{<rawhtml>}}
        <h1 class="text-gray-800 text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4 lg:mb-8 text-center">
            Don't get us wrong, Stripe Checkout is great.
        </h1>
        <div class="py-8 md:px-32 w-full">
            <div class="mb-8 md:px-32">
            <p>PriceWell is built on top of Stripe Checkout so we know what we're talking about when we compare the two. But why shouldn't you just integrate Stripe yourself? Well if you've got serious developer chops then go for it. If you'd rather spend time working on your SaaS, then we've got your back. Check out the head-to-head comparison below.</p>

            <div class="bg-white rounded pb-16 mt-8">
            {{< partial "vs-stripe" >}}
            </div>

            <h3 class="mt-16 mb-8 text-xl">Who is PriceWell <b>not</b> for?</h3>
            <ul class="list-disc list-inside">
                <li>If you have a completely custom pricing model it's unlikely we'll be a fit. Do <a href="javascript:$crisp.push(['do', 'chat:open']);" class="text-blue-600 hover:font-bold">get in touch</a> to find out if we can help you.</li>
                <li>If you don't bat an eyelid at integrating webhooks, calling APIs and generally getting your hands dirty with billing code.</li>
            </ul>
            </div>
        </div>

        {{<partial "testimonials">}}

        <div class="bg-gray-100">
        <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 py-12 lg:py-16 xl:py-24">
            <div class="text-center mb-6 md:mb-8">
                <h2 id="pricing" class="text-black text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4">Grow your business with our tailored pricing</h2>
                <p class="text-lg xl:text-xl text-gray-800 relative w-1/2 m-auto">Oh, and our pricing is made with PriceWell <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 372.136 372.136" class="w-12 ml-10 transform rotate-120 fill-current text-black"><path d="M371.682 143.271c-14.688-44.676-26.316-90.576-50.797-131.58-2.447-4.284-10.403-5.508-12.239 0-17.748 42.228-36.108 83.844-47.736 127.908-1.836 7.344 7.344 12.852 12.852 7.344 10.404-10.404 21.421-20.196 33.049-28.764-1.225 90.576 1.836 195.84-105.876 223.992-47.736 12.24-100.98 5.509-140.76-25.092C18.557 284.644 9.377 231.4 12.437 181.828c0-4.896-7.344-6.12-8.568-1.224-23.868 110.772 66.096 197.064 176.256 181.764 54.468-7.344 100.368-33.048 123.624-85.068 20.809-46.512 19.584-102.204 18.36-153 11.628 10.404 24.479 19.584 37.943 26.928 6.121 3.672 14.077-1.224 11.63-7.957zm-55.08-40.391c-3.672-1.224-6.12.612-7.345 3.672l-.611.612c-9.792 3.06-18.36 7.956-26.316 13.464 9.18-29.988 21.42-59.364 33.048-88.128 15.912 29.988 25.092 62.424 35.496 94.248-11.017-9.18-21.421-18.36-34.272-23.868z"/></svg></p>
            </div>

            {{< partial "pricing" >}}

            <div class="pt-8">
            {{<partial "pricing-explainer">}}
            </div>

        </div>
        </div>
{{</rawhtml>}}