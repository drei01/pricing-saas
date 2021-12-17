---
title: Homepage
date: 2020-12-01T14:54:28+01:00
draft: false
type: page
description: no code pricing pages
---
{{<rawhtml>}}
    <script>
        function toggle(x) {
            if (document.getElementById(x).style.display == 'none') {
                document.getElementById(x).style.display = '';
            } else {
                document.getElementById(x).style.display = 'none';
            }
        }
    </script>
    <div class="py-12 md:py-24">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
        <div class="order-1 col-span-2 self-center my-12 md:my-0">
            <h1 class="text-gray-800 text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4 lg:mb-8">
                Build Stripe subscriptions into your website in minutes.
            </h1>
            <p class="text-lg xl:text-xl font-normal text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                Subscription businesses trust PriceWell with their Pricing Infrastructure, <b>saving weeks</b> of development time.
            </p>
            <div class="flex space-x-4 mb-6">
                <a href="https://app.pricewell.io/register"
                    class="focus:outline-none inline-block bg-gradient-to-br from-wedgewood-600 to-wedgewood-700 hover:from-wedgewood-700 hover:to-wedgewood-800 font-semibold rounded-lg py-2 px-8 text-white"
                    data-analytics="Signup"
                >
                    Get started for free
                </a>
                <button class="focus:outline-none inline-block font-semibold border rounded-lg py-2 px-8 bg-white text-black hover:bg-gray-200" onclick="Calendly.initPopupWidget({url: 'https://calendly.com/matthew_reid/pricewell?hide_event_type_details=1&hide_gdpr_banner=1'});return false;" data-analytics="Demo">Book a Demo</button>
            </div>

            <p class="text-gray-500 text-sm">No credit card required.</p>
        </div>
        <div class="order-2 col-span-2 xl:col-span-3 flex-col">
            <img src='images/hero.png' alt="woman lifting a pricing table into an empty space in a website" class="m-auto">

        </div>
    </div>

</div>

<div class="py-12 lg:py-16">
    <div class="text-sm text-center font-light">Integrates with</div>
    <div
        class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid grid-cols-2 sm:grid-cols-2 space-y-5 sm:space-y-3 xl:grid-cols-4 col-gap-6 opacity-60"
    >
        
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="h-28 p-1 self-end justify-self-center" viewBox="0 0 120 60"><g fill="#00749a"><path d="M55.5 40.9h-4.62v.48c1.444 0 1.684.3 1.684 2.118v3.273c0 1.83-.24 2.166-1.684 2.166-1.107-.144-1.877-.77-2.888-1.877l-1.203-1.3c1.588-.3 2.455-1.3 2.455-2.406 0-1.396-1.203-2.503-3.465-2.503h-4.524v.48c1.444 0 1.684.3 1.684 2.118v3.273c0 1.83-.24 2.166-1.684 2.166v.48h5.102v-.48c-1.444 0-1.684-.337-1.684-2.166v-.914h.433l2.84 3.56h7.508c3.706 0 5.294-1.973 5.294-4.283.048-2.262-1.54-4.187-5.246-4.187zm-10.78 4.187V41.68h1.06c1.155 0 1.684.818 1.684 1.733s-.53 1.684-1.684 1.684zm10.877 3.56h-.193c-.914 0-1.06-.24-1.06-1.396v-5.58h1.25c2.695 0 3.176 1.973 3.176 3.465 0 1.588-.53 3.513-3.176 3.513zM26.912 46.06l1.78-5.246c.53-1.54.3-1.973-1.348-1.973v-.53h4.86v.53c-1.636 0-2.02.385-2.647 2.262L26.62 49.9h-.385l-2.647-8.037L20.94 49.9h-.337l-2.84-8.807c-.626-1.877-1-2.262-2.503-2.262v-.53h5.68v.53c-1.54 0-1.925.337-1.396 1.973l1.733 5.246 2.6-7.75h.48zm8.758 3.755c-2.84 0-5.15-2.07-5.15-4.62 0-2.503 2.3-4.62 5.15-4.62s5.15 2.07 5.15 4.62-2.3 4.62-5.15 4.62zm0-8.47c-2.358 0-3.176 2.118-3.176 3.802s.818 3.802 3.176 3.802c2.406 0 3.225-2.118 3.225-3.802 0-1.636-.818-3.802-3.225-3.802zm31.477 7.603v.53h-5.92v-.53c1.733 0 2.02-.433 2.02-3.032v-4.14c0-2.6-.3-2.984-2.02-2.984v-.53h5.342c2.647 0 4.14 1.348 4.14 3.176 0 1.78-1.492 3.176-4.14 3.176h-1.444v1.348c0 2.55.3 2.984 2.02 2.984zm-.578-9.722h-1.444v4.476h1.444c1.444 0 2.118-1 2.118-2.214s-.674-2.262-2.118-2.262zm21.803 7.844l-.144.48c-.24.866-.53 1.155-2.358 1.155h-.337c-1.348 0-1.588-.3-1.588-2.118v-1.203c2.02 0 2.166.193 2.166 1.54h.48v-3.85h-.48c0 1.348-.144 1.54-2.166 1.54V41.73h1.396c1.83 0 2.118.3 2.358 1.155l.144.48h.433l-.193-2.406h-7.556v.48c1.444 0 1.684.3 1.684 2.118v3.273c0 1.684-.193 2.118-1.348 2.166-1.06-.144-1.83-.77-2.84-1.877l-1.203-1.3c1.588-.3 2.455-1.3 2.455-2.406 0-1.396-1.203-2.503-3.465-2.503h-4.524v.48c1.444 0 1.684.3 1.684 2.118v3.273c0 1.83-.24 2.166-1.684 2.166v.48h5.102v-.48c-1.444 0-1.684-.337-1.684-2.166v-.914h.433l2.84 3.56h10.588l.144-2.406h-.337zm-13.62-1.973V41.68h1.06c1.155 0 1.684.818 1.684 1.733s-.53 1.684-1.684 1.684z"/><use xlink:href="#B"/><use xlink:href="#B" x="7.942"/><path d="M46.803 19.485c0 5.234 3.007 9.744 7.406 11.86L47.973 14.14c-.724 1.67-1.17 3.452-1.17 5.346zm22.107-.67c0-1.615-.613-2.784-1.114-3.62-.668-1.114-1.28-2.005-1.28-3.118 0-1.225.947-2.34 2.227-2.34h.167c-2.34-2.168-5.458-3.45-8.9-3.45-4.622.056-8.63 2.394-11.025 5.958h.835c1.392 0 3.508-.167 3.508-.167.724-.056.78 1.002.1 1.114 0 0-.724.1-1.503.1l4.8 14.255 2.895-8.63-2.06-5.624-1.392-.1c-.724-.056-.613-1.114.056-1.114 0 0 2.172.167 3.452.167 1.392 0 3.508-.167 3.508-.167.724-.056.78 1.002.1 1.114 0 0-.724.1-1.503.1l4.8 14.2 1.336-4.4c.557-1.838 1.002-3.118 1.002-4.288zm-8.687 1.84l-3.953 11.47c1.17.334 2.45.557 3.73.557 1.56 0 3.007-.278 4.4-.724-.056-.056-.056-.1-.1-.167zm11.36-7.46l.1 1.336c0 1.336-.223 2.84-1.002 4.733l-4 11.637c3.898-2.283 6.57-6.515 6.57-11.415-.056-2.283-.668-4.4-1.67-6.292zM60 4.116c-8.464 0-15.368 6.905-15.368 15.368S51.536 34.853 60 34.853s15.368-6.905 15.368-15.368S68.464 4.116 60 4.116zm0 30.068c-8.074 0-14.644-6.57-14.644-14.7C45.356 11.4 51.926 4.84 60 4.84s14.644 6.57 14.644 14.644c0 8.13-6.57 14.7-14.644 14.7z"/></g><defs><path id="B" d="M93.618 49.815c-1.01 0-1.925-.53-2.3-.866-.144.144-.337.53-.433.866h-.48v-3.56h.53c.193 1.684 1.396 2.695 2.888 2.695.818 0 1.492-.48 1.492-1.25 0-.674-.578-1.203-1.636-1.684l-1.444-.674c-1.01-.48-1.78-1.348-1.78-2.455 0-1.25 1.155-2.3 2.743-2.3.866 0 1.588.29 2.02.674.144-.096.24-.385.337-.674h.48v3.032h-.53c-.193-1.203-.866-2.214-2.214-2.214-.722 0-1.396.433-1.396 1.06 0 .674.53 1.01 1.78 1.588l1.396.674c1.25.578 1.733 1.54 1.733 2.3-.048 1.636-1.444 2.79-3.176 2.79z"/></defs></svg>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-28 p-1 self-end justify-self-center" viewBox="0 0 120 60"><path d="M44.37 27.572c0-1.6-1.535-3.278-4.203-3.278-2.992 0-6.277 2.203-6.78 6.6-.514 4.44 2.237 6.413 5.01 6.413s4.225-1.085 5.71-2.532c-1.277-1.61-2.926-.866-3.242-.702a3.31 3.31 0 01-1.714.417c-1.07 0-2.162-.482-2.162-2.488 6.856-.68 7.38-2.84 7.38-4.43zm-3.398.263c-.044.493-.24 1.337-3.712 1.81.73-2.61 2.13-2.806 2.773-2.806a.909.909 0 01.946.998zm-11.612.428l-1.594 5.032-1.125-8.737c-2.51 0-3.86 1.798-4.564 3.694l-1.944 5.054-.273-5c-.148-2.324-2.27-3.738-3.985-3.738l2.074 12.64c2.63-.01 4.05-1.798 4.793-3.694l1.644-4.297c.015.175 1.136 7.992 1.136 7.992 2.642 0 4.062-1.677 4.823-3.508l3.7-9.132c-2.605 0-3.978 1.787-4.687 3.694zm24.706-4c-1.627 0-2.87.888-3.92 2.192v-.01l.938-7.597c-2.162 0-3.92 1.886-4.258 4.692L45.2 37.11c1.245 0 2.566-.362 3.276-1.283.634.822 1.583 1.48 2.992 1.48 3.646 0 6.147-4.253 6.147-8.244-.022-3.64-1.78-4.79-3.538-4.79zm-.34 6.523c-.38 2.225-1.616 3.738-2.805 3.738s-1.714-.537-1.714-.537c.23-1.95.372-3.146.808-4.177s1.474-2.675 2.555-2.675c1.06 0 1.54 1.414 1.157 3.65zm12.982-6.227h-2.544l.01-.132c.175-1.666.568-2.543 1.864-2.686.885-.088 1.278-.548 1.376-1.052l.317-1.765c-5.1-.033-6.714 2.18-7.125 5.558l-.01.077h-.055c-.83 0-1.746.943-1.9 2.138l-.055.438h1.704l-1.43 11.86-.438 2.127c.055 0 .12.01.174.01 2.39-.088 3.92-1.984 4.258-4.736l1.116-9.263h.8c.786 0 1.704-.79 1.864-2.105zm13.232-.22c-2.937 0-5.71 2.17-6.56 5.58s.438 7.443 4.76 7.443 6.797-4.2 6.797-7.696c.004-3.475-2.342-5.328-4.996-5.328zm1.19 6.336c-.152 1.546-.83 3.892-2.686 3.892s-1.605-2.74-1.425-4.045c.197-1.392.972-3.376 2.642-3.376 1.502 0 1.643 1.787 1.47 3.53zm18.32-2.423l-1.594 5.032c-.043-.395-1.124-8.737-1.124-8.737-2.51 0-3.854 1.798-4.558 3.694l-1.944 5.054c-.01-.362-.273-5-.273-5-.158-2.324-2.278-3.738-4-3.738l2.063 12.64c2.63-.01 4.05-1.798 4.793-3.694l1.638-4.297c.01.175 1.136 7.992 1.136 7.992 2.642 0 4.056-1.677 4.823-3.508l3.703-9.132c-2.598 0-3.974 1.787-4.673 3.694zm-30.34-9.33l-2.14 17.33-.438 2.138c.054 0 .12.01.174.01 2.302-.033 3.94-2.06 4.247-4.615l1.233-9.943c.374-3.037-1.427-4.922-3.076-4.922z" fill="#4353ff"/></svg>
        <img src="/img/bubble-logo.png" alt-"bubble.io logo" class="h-28 p-1 self-end justify-self-center object-contain">
        <img src="/images/stripe-blurple_lg.png" alt-"Stripe logo" class="h-28 p-6 self-end justify-self-center object-contain">
    </div>
</div>

<div class="bg-gray-100 px-6 lg:px-8 xl:px-4">
{{<partial "testimonials">}}
</div>

    <section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="text-center mb-20">
      <h1 class="sm:text-3xl text-2xl font-medium text-center title-font text-gray-900 mb-4">Hiring a Developer is <b>expensive</b></h1>
      <p class="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto">Implementing Stripe Checkout and Stripe Customer Portal can take weeks of development time. PriceWell takes minutes! Saving you $10,000's, with no hidden maintenance costs.</p>
    </div>
    <div class="flex flex-wrap lg:w-4/5 sm:mx-auto sm:mb-2 -mx-2">
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-blue-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Implement in 1 hour</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-blue-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Subscription Management (via <a href="/customer-portal" class="text-blue-600 hover:underline">Customer Portal</a>)</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-blue-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">No Coding Required</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-blue-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Embeddable Pricing Page</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-blue-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Instant Pricing Changes</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-blue-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">GDPR Compliant</span>
        </div>
      </div>
    </div>
  </div>
</section>

    <div class="py-12 md:py-24 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-2 md:order-1 col-span-2 self-center mt-12 md:mt-0">
            <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Pricing Pages
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Pricing Pages can be embedded anywhere on your website. You can change pricing at any time without ever writing any code. Customize the design to match your brand and make changes whenever you want. This is the fastest way to implement Stripe Checkout. 
                </p>                
            </div>
            <div class="order-1 md:order-2 col-span-2 xl:col-span-3">
                <img src='images/select-pricing-plans.png' class="rounded-lg shadow-2xl" alt="" />
            </div>
        </div>
    </div>


<div class="py-12 md:py-24 pb-12 lg:pb-16 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-1 col-span-2 xl:col-span-3 self-center">
                <img src='img/customer-portal.png' class="rounded-lg shadow-2xl" alt="" />
                
            </div>
            <div class="order-2 col-span-2 mt-12 md:mt-0">
                <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Customer Portal
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Let customers manage their subscription on your terms. Designed to fit into your existing website, the embeddable Customer Portal takes minutes to set up. Simply drop the widget into your website and you no longer have to worry about subscription management.
                </p>
            </div>
        </div>
    </div>

    <div class="py-12 md:py-24 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-2 md:order-1 col-span-2 self-center mt-12 md:mt-0">
            <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Gated Content
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Control which features your users see based on their subscription plan. All configured through your pricing so you can add new gated features and update your website at the same time.
                </p>                
            </div>
            <div class="order-1 md:order-2 col-span-2 xl:col-span-3">
                <img src='images/feature-flags.png' class="rounded-lg shadow-2xl" alt="" />
            </div>
        </div>
    </div>

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

<div class="bg-gradient-to-b from-gray-100 to-white lg:mb-16 xl:mb-24 py-12 lg:pt-20 relative overflow-hidden">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 relative z-20">
        <div class="text-center mb-6 md:mb-8 lg:mb-12">
            <h2 class="text-gray-800 text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4">FAQ</h2>
            <p class="text-lg xl:text-xl text-gray-600">Answers to your frequently asked questions.</p>
        </div>
        <div class="mb-12 lg:mb-20">
            <ul class="divide-y divide-gray-300text-base md:text-lg">
            <li>
                    <button
                        class="py-3 lg:py-4 font-bold focus:outline-none hover:text-blue-700 w-full flex items-center justify-between"
                        onclick="toggle('integration');"
                    >
                        <span class="flex-1 text-left pr-6">
                            Can you help with the integration?
                        </span>
                        <svg
                            class="w-6 h-6 text-blue-600"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
                            ></path>
                        </svg>
                    </button>
                    <div id="integration" class="py-4" style="display:none;">
                        Yes, of course. We are more than happy to jump on a call and discuss your particular needs. You can <a href="https://calendly.com/matthew_reid/pricewell" class="text-wedgewood-800 underline">book a time</a> in our calendar that suits you.
                    </div>
                </li>
                <li>
                    <button
                        class="py-3 lg:py-4 font-bold focus:outline-none hover:text-blue-700 w-full flex items-center justify-between"
                        onclick="toggle('gdpr');"
                    >
                        <span class="flex-1 text-left pr-6">
                            Is PriceWell compliant with GDPR regulations?
                        </span>
                        <svg
                            class="w-6 h-6 text-blue-600"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
                            ></path>
                        </svg>
                    </button>
                    <div id="gdpr" class="py-4" style="display:none;">
                        Yes. PriceWell does not store any personally identifiable information of your customers. That
                        information is all held in your Stripe account. We only store the identifier to your Stripe account (and
                        use that to trigger payment flows for your customers. This means you do not need to remove any personal
                        user data from PriceWell, but you may need to from your Stripe account (see the 
                        <a
                            href="https://stripe.com/en-de/guides/general-data-protection-regulation"
                            target="_blank"
                            rel="noopener noreferrer"
                            class="text-blue-600 underline"
                        >
                            Stripe GDPR Documentation
                        </a>)
                    </div>
                </li>
                <li>
                    <button
                        class="py-3 lg:py-4 font-bold focus:outline-none hover:text-blue-700 w-full flex items-center justify-between"
                        onclick="toggle('testMode');"
                    >
                        <span class="flex-1 text-left pr-6">
                            Can I use my Stripe account in Test mode?
                        </span>
                        <svg
                            class="w-6 h-6 text-blue-600"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
                            ></path>
                        </svg>
                    </button>
                    <div id="testMode" class="py-4" style="display:none;">
                    Yes. You need to connect your live Stripe account in order to set up your PriceWell account. Once your
                    account is connected you can switch an individual Pricing Page between Test and Live mode. In test mode
                    you can use test credit cards (see the 
                    <a
                        href="https://stripe.com/docs/testing"
                        target="_blank"
                        rel="noopener noreferrer"
                        class="text-blue-600 underline"
                    >
                        Stripe Testing Documentation
                    </a>
                    ) to test the full process. If a page is in test mode, a banner will be displayed when your pricing page
                    is loaded (so you don't forget to switch it to live mode before you launch it to customers).
                    </div>
                </li>
                <li>
                    <button
                        class="py-3 lg:py-4 font-bold focus:outline-none hover:text-blue-700 w-full flex items-center justify-between"
                        onclick="toggle('multiAccount');"
                    >
                        <span class="flex-1 text-left pr-6">
                            Can I use PriceWell for multiple websites / businesses?
                        </span>
                        <svg
                            class="w-6 h-6 text-blue-600"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
                            ></path>
                        </svg>
                    </button>
                    <div id="multiAccount" class="py-4" style="display:none;">
                    Yes. You can even connect multiple Stripe accounts so you don't have to host all your businesses in one. <a
                        href="javascript:$crisp.push(['do', 'chat:open']);"
                        class="text-blue-600 underline"
                    >
                        Get in touch
                    </a> if you have any questions.
                    </div>
                </li>
            </ul>
        </div>
        <div class="grid md:grid-cols-2 gap-8 lg:gap-12">
            <a
                href="javascript:$crisp.push(['do', 'chat:open']);"
                class="bg-white rounded-lg shadow hover:shadow-xl transition-all duration-500 p-6 lg:p-8 border border-blue-100 flex flex-col lg:flex-row space-y-6 lg:space-y-0 lg:space-x-6"
            >
                <div
                    class="h-16 w-16 lg:h-20 lg:w-20 bg-green-100 rounded-full flex items-center justify-center border border-green-200 shadow-inner"
                >
                    <svg
                        class="w-10 h-10 text-green-500"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"
                        ></path>
                    </svg>
                </div>
                <div class="flex-1">
                    <h5 class="font-bold text-xl lg:text-2xl mb-3">Compare Plans</h5>
                    <p class="text-lg text-gray-600 mb-6">Find out which plan is right for you</p>
                    <span class="font-bold text-lg text-blue-600 flex items-baseline">
                        Chat with us
                        <svg
                            class="w-4 h-4 ml-2"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M14 5l7 7m0 0l-7 7m7-7H3"
                            ></path>
                        </svg>
                    </span>
                </div>
            </a>
            <a
                href="javascript:$crisp.push(['do', 'chat:open']);"
                class="bg-white rounded-lg shadow hover:shadow-xl transition-all duration-500 p-6 lg:p-8 border border-blue-100 flex flex-col lg:flex-row space-y-6 lg:space-y-0 lg:space-x-6"
            >
                <div
                    class="h-16 w-16 lg:h-20 lg:w-20 bg-green-100 rounded-full flex items-center justify-center border border-green-200 shadow-inner"
                >
                    <svg
                        class="w-10 h-10 text-green-500"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"
                        ></path>
                    </svg>
                </div>
                <div class="flex-1">
                    <h5 class="font-bold text-xl lg:text-2xl mb-3">Need advice?</h5>
                    <p class="text-lg text-gray-600 mb-6">Chat with one of our team</p>
                    <span class="font-bold text-lg text-blue-600 flex items-baseline">
                        Contact our professionals
                        <svg
                            class="w-4 h-4 ml-2"
                            fill="none"
                            stroke="currentColor"
                            viewBox="0 0 24 24"
                            xmlns="http://www.w3.org/2000/svg"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M14 5l7 7m0 0l-7 7m7-7H3"
                            ></path>
                        </svg>
                    </span>
                </div>
            </a>
        </div>
    </div>
</div>
{{</rawhtml>}}