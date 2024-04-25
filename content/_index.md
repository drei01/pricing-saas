---
title: No-Code Stripe Subscription Billing
date: 2020-12-01T14:54:28+01:00
draft: false
type: page
# see header.html for description
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
                Stripe Subscriptions Without Hiring a Developer
            </h1>
            <p class="text-lg xl:text-xl font-normal text-gray-600 mb-2">
                <span class="font-bold">Before PriceWell:</span> Stressing over Stripe for weeks. No time to focus on your product.
            </p>
            <p class="text-lg xl:text-xl font-normal text-gray-600 mb-2">
                <span class="font-bold">After PriceWell:</span> Stripe integrated in 10 minutes. Calm and focused on bringing in new customers.
            </p>
            <div class="flex flex-col md:flex-row space-y-4 md:space-y-0 space-x-0 md:space-x-4 text-center md:text-left mt-6">
                <a href="https://app.pricewell.io/register"
                    class="button"
                    data-analytics="Signup"
                >
                    Try PriceWell for Free
                </a>
                <a href="/book-free-demo" class="button-white-bg bg-none md:bg-[url('/images/matt.png')]  bg-no-repeat bg-left bg-contain">
                    Book a Demo
                </a>
            </div>

            <p class="text-gray-500 text-sm mb-6 mt-2">No credit card required.</p>

            <div class="flex space-x-2 justify-start items-center mt-6">
             {{< partial "testimonial-avatars" >}}
             <div>
            Trusted by 500+ businesses
            </div>
            </div>
        </div>
        <div class="order-2 col-span-2 xl:col-span-3 flex-col">
            {{< partial "promo-video">}}
        </div>
    </div>

</div>

<div class="bg-gray-100 py-12 lg:py-24">
    <div class="text-sm text-center font-light">Integrates with</div>
    <div
        class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid grid-cols-1 sm:grid-cols-2 space-y-5 sm:space-y-3 xl:grid-cols-4 col-gap-6 opacity-60"
    >
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -60 540 245" class="h-28 p-1 self-end justify-self-center"><path fill="#00749a" d="M313.19 48.227h-21.257v2.255c6.649 0 7.718 1.425 7.718 9.856V75.54c0 8.431-1.067 9.976-7.718 9.976-5.104-.713-8.55-3.444-13.3-8.67l-5.462-5.937c7.361-1.308 11.28-5.938 11.28-11.164 0-6.53-5.58-11.518-16.031-11.518h-20.9v2.255c6.649 0 7.718 1.425 7.718 9.856V75.54c0 8.431-1.068 9.976-7.718 9.976v2.256h23.631v-2.256c-6.648 0-7.718-1.545-7.718-9.976v-4.273h2.019l13.182 16.505h34.557c16.981 0 24.345-9.024 24.345-19.832-.002-10.807-7.364-19.713-24.346-19.713zm-49.756 19.355V51.79h4.868c5.343 0 7.719 3.681 7.719 7.956 0 4.157-2.376 7.837-7.719 7.837zm50.113 16.508h-.832c-4.274 0-4.868-1.067-4.868-6.53V51.79h5.7c12.35 0 14.604 9.024 14.604 16.031.001 7.243-2.255 16.269-14.604 16.269zM181.378 71.978l8.193-24.228c2.376-7.006 1.308-9.023-6.293-9.023v-2.376h22.325v2.376c-7.48 0-9.262 1.78-12.23 10.449L179.834 89.79h-1.543l-12.114-37.17-12.349 37.17h-1.545l-13.181-40.613c-2.85-8.669-4.75-10.449-11.638-10.449v-2.376h26.363v2.376c-7.008 0-8.908 1.662-6.413 9.023l7.956 24.228 11.993-35.627h2.258zm40.374 17.336c-13.062 0-23.75-9.618-23.75-21.376 0-11.638 10.688-21.257 23.75-21.257s23.75 9.619 23.75 21.257c0 11.758-10.687 21.376-23.75 21.376zm0-38.949c-10.924 0-14.726 9.854-14.726 17.574 0 7.839 3.802 17.576 14.726 17.576 11.045 0 14.845-9.737 14.845-17.576 0-7.72-3.8-17.574-14.845-17.574z"/><path fill="#464342" d="M366.864 85.396v2.375H339.67v-2.375c7.957 0 9.382-2.019 9.382-13.896V52.502c0-11.877-1.425-13.775-9.382-13.775V36.35h24.581c12.23 0 19.002 6.294 19.002 14.727 0 8.194-6.771 14.606-19.002 14.606h-6.77V71.5c.001 11.878 1.425 13.896 9.383 13.896zm-2.613-44.771h-6.77v20.664h6.77c6.65 0 9.737-4.631 9.737-10.212.001-5.7-3.086-10.452-9.737-10.452zm100.582 35.984-.595 2.137c-1.067 3.919-2.376 5.344-10.807 5.344h-1.663c-6.174 0-7.243-1.425-7.243-9.855v-5.462c9.263 0 9.976.83 9.976 7.006h2.257V58.083h-2.257c0 6.175-.713 7.006-9.976 7.006V51.79h6.53c8.433 0 9.738 1.425 10.807 5.344l.596 2.256h1.898l-.83-11.162h-34.914v2.255c6.649 0 7.719 1.425 7.719 9.856V75.54c0 7.713-.907 9.656-6.15 9.934-4.983-.762-8.404-3.479-13.085-8.628l-5.463-5.937c7.363-1.308 11.282-5.938 11.282-11.164 0-6.53-5.581-11.518-16.031-11.518h-20.9v2.255c6.649 0 7.719 1.425 7.719 9.856V75.54c0 8.431-1.068 9.976-7.719 9.976v2.256h23.632v-2.256c-6.648 0-7.719-1.545-7.719-9.976v-4.273h2.02l13.181 16.505h48.806l.713-11.161zm-62.937-9.027V51.79h4.868c5.344 0 7.72 3.681 7.72 7.956 0 4.157-2.376 7.837-7.72 7.837zm87.043 21.732c-4.75 0-8.907-2.493-10.688-4.038-.595.595-1.662 2.376-1.899 4.038h-2.257V72.927h2.375c.951 7.838 6.412 12.469 13.419 12.469 3.8 0 6.888-2.138 6.888-5.699 0-3.087-2.73-5.463-7.6-7.719l-6.77-3.206c-4.751-2.258-8.312-6.178-8.312-11.401 0-5.7 5.344-10.568 12.707-10.568 3.919 0 7.243 1.426 9.263 3.088.593-.476 1.188-1.782 1.544-3.208h2.256v14.014h-2.494c-.832-5.582-3.919-10.213-10.212-10.213-3.325 0-6.413 1.899-6.413 4.87 0 3.087 2.493 4.749 8.194 7.361l6.53 3.206c5.701 2.731 7.956 7.127 7.956 10.689 0 7.48-6.531 12.704-14.487 12.704zm36.575 0c-4.751 0-8.908-2.493-10.688-4.038-.594.595-1.662 2.376-1.898 4.038h-2.257V72.927h2.375c.95 7.838 6.411 12.469 13.419 12.469 3.8 0 6.888-2.138 6.888-5.699 0-3.087-2.731-5.463-7.601-7.719l-6.77-3.206c-4.75-2.258-8.312-6.178-8.312-11.401 0-5.7 5.344-10.568 12.707-10.568 3.919 0 7.242 1.426 9.263 3.088.593-.476 1.187-1.782 1.542-3.208h2.257v14.014h-2.493c-.832-5.582-3.919-10.213-10.212-10.213-3.325 0-6.414 1.899-6.414 4.87 0 3.087 2.494 4.749 8.195 7.361l6.53 3.206c5.7 2.731 7.955 7.127 7.955 10.689 0 7.48-6.531 12.704-14.486 12.704z"/><g fill="#00749a"><path d="M8.708 61.26c0 20.803 12.089 38.779 29.619 47.299L13.258 39.872a52.354 52.354 0 0 0-4.55 21.388zm88.032-2.652c0-6.495-2.333-10.993-4.334-14.494-2.664-4.329-5.16-7.995-5.16-12.324 0-4.831 3.663-9.328 8.824-9.328.233 0 .454.029.682.042-9.351-8.566-21.808-13.796-35.49-13.796-18.36 0-34.513 9.42-43.91 23.688 1.233.037 2.396.062 3.382.062 5.497 0 14.006-.667 14.006-.667 2.833-.167 3.167 3.994.338 4.329 0 0-2.848.335-6.016.501L48.2 93.546l11.502-34.493-8.189-22.433c-2.83-.166-5.511-.501-5.511-.501-2.832-.166-2.5-4.496.332-4.329 0 0 8.679.667 13.843.667 5.496 0 14.006-.667 14.006-.667 2.835-.167 3.168 3.994.337 4.329 0 0-2.853.335-6.015.501l18.992 56.494 5.241-17.517c2.273-7.269 4.002-12.49 4.002-16.989z"/><path d="m62.184 65.857-15.768 45.818a52.516 52.516 0 0 0 14.846 2.142c6.12 0 11.989-1.059 17.452-2.979a4.451 4.451 0 0 1-.374-.724zm45.192-29.811c.226 1.674.354 3.472.354 5.404 0 5.333-.996 11.328-3.996 18.824l-16.053 46.413c15.624-9.111 26.133-26.038 26.133-45.427a52.268 52.268 0 0 0-6.438-25.214z"/><path d="M61.262 0C27.483 0 0 27.481 0 61.26c0 33.783 27.482 61.264 61.262 61.264 33.778 0 61.265-27.48 61.265-61.264C122.526 27.481 95.04 0 61.262 0zm0 119.715c-32.23 0-58.453-26.223-58.453-58.455 0-32.229 26.222-58.45 58.453-58.45 32.229 0 58.45 26.221 58.45 58.45 0 32.232-26.222 58.455-58.45 58.455z"/></g></svg>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-28 p-1 self-end justify-self-center" viewBox="0 0 120 60"><path d="M44.37 27.572c0-1.6-1.535-3.278-4.203-3.278-2.992 0-6.277 2.203-6.78 6.6-.514 4.44 2.237 6.413 5.01 6.413s4.225-1.085 5.71-2.532c-1.277-1.61-2.926-.866-3.242-.702a3.31 3.31 0 01-1.714.417c-1.07 0-2.162-.482-2.162-2.488 6.856-.68 7.38-2.84 7.38-4.43zm-3.398.263c-.044.493-.24 1.337-3.712 1.81.73-2.61 2.13-2.806 2.773-2.806a.909.909 0 01.946.998zm-11.612.428l-1.594 5.032-1.125-8.737c-2.51 0-3.86 1.798-4.564 3.694l-1.944 5.054-.273-5c-.148-2.324-2.27-3.738-3.985-3.738l2.074 12.64c2.63-.01 4.05-1.798 4.793-3.694l1.644-4.297c.015.175 1.136 7.992 1.136 7.992 2.642 0 4.062-1.677 4.823-3.508l3.7-9.132c-2.605 0-3.978 1.787-4.687 3.694zm24.706-4c-1.627 0-2.87.888-3.92 2.192v-.01l.938-7.597c-2.162 0-3.92 1.886-4.258 4.692L45.2 37.11c1.245 0 2.566-.362 3.276-1.283.634.822 1.583 1.48 2.992 1.48 3.646 0 6.147-4.253 6.147-8.244-.022-3.64-1.78-4.79-3.538-4.79zm-.34 6.523c-.38 2.225-1.616 3.738-2.805 3.738s-1.714-.537-1.714-.537c.23-1.95.372-3.146.808-4.177s1.474-2.675 2.555-2.675c1.06 0 1.54 1.414 1.157 3.65zm12.982-6.227h-2.544l.01-.132c.175-1.666.568-2.543 1.864-2.686.885-.088 1.278-.548 1.376-1.052l.317-1.765c-5.1-.033-6.714 2.18-7.125 5.558l-.01.077h-.055c-.83 0-1.746.943-1.9 2.138l-.055.438h1.704l-1.43 11.86-.438 2.127c.055 0 .12.01.174.01 2.39-.088 3.92-1.984 4.258-4.736l1.116-9.263h.8c.786 0 1.704-.79 1.864-2.105zm13.232-.22c-2.937 0-5.71 2.17-6.56 5.58s.438 7.443 4.76 7.443 6.797-4.2 6.797-7.696c.004-3.475-2.342-5.328-4.996-5.328zm1.19 6.336c-.152 1.546-.83 3.892-2.686 3.892s-1.605-2.74-1.425-4.045c.197-1.392.972-3.376 2.642-3.376 1.502 0 1.643 1.787 1.47 3.53zm18.32-2.423l-1.594 5.032c-.043-.395-1.124-8.737-1.124-8.737-2.51 0-3.854 1.798-4.558 3.694l-1.944 5.054c-.01-.362-.273-5-.273-5-.158-2.324-2.278-3.738-4-3.738l2.063 12.64c2.63-.01 4.05-1.798 4.793-3.694l1.638-4.297c.01.175 1.136 7.992 1.136 7.992 2.642 0 4.056-1.677 4.823-3.508l3.703-9.132c-2.598 0-3.974 1.787-4.673 3.694zm-30.34-9.33l-2.14 17.33-.438 2.138c.054 0 .12.01.174.01 2.302-.033 3.94-2.06 4.247-4.615l1.233-9.943c.374-3.037-1.427-4.922-3.076-4.922z" fill="#4353ff"/></svg>
        <img src="/img/bubble-logo.png" alt="bubble.io logo" class="h-28 p-1 self-end justify-self-center object-contain">
        <img src="/images/stripe-blurple_lg.png" alt="Stripe logo" class="h-28 p-6 self-end justify-self-center object-contain">
    </div>
    <div class="flex pt-8">
    <a href="/integrations" class="block mx-auto focus:outline-none inline-block font-semibold underline py-2 px-8 text-gray-800">Explore 100+ more integrations</a>
    </div>
</div>

    <section class="text-gray-600 body-font">
  <div class="container px-5 py-24 md:py-64 mx-auto">
    <div class="text-center mb-20">
      <h1 class="sm:text-3xl text-2xl font-medium text-center title-font text-gray-900 mb-4">Save <b>$1,000's</b> on development and maintenance costs</h1>
      <p class="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto mb-4">Implementing Stripe Checkout and Stripe Customer Portal can add weeks to your development process. Not to mention all the changes every time you update pricing. PriceWell integrates in minutes. Saving you $1,000's with no hidden maintenance.</p>

    </div>
    <div class="flex flex-wrap lg:w-4/5 sm:mx-auto sm:mb-2 -mx-2">
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-green-600 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Implement in 1 hour</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-green-600 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Subscription Management (via <a href="/customer-portal" class="text-blue-600 underline hover:text-blue-300">Customer Portal</a>)</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-green-600 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">No Coding Required</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-green-600 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Embeddable Pricing Page</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-green-600 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Instant Pricing Changes</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-green-600 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">GDPR Compliant</span>
        </div>
      </div>
    </div>
  </div>
</section>

    <div class="pt-24 md:pt-48 pb-24 mb:pb-64 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-2 md:order-1 col-span-2 self-center mt-12 md:mt-0">
            <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Pricing Tables
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Pricing Tables can be embedded anywhere on your website. You can change pricing at any time without ever writing any code. Customize the design to match your brand, apply add-ons, accept coupon codes etc. This is the fastest way to implement Stripe Checkout.
                </p>   
                 <a href="https://app.pricewell.io/register"
                    class="button"
                    data-analytics="Signup"
                >
                    Create a Free Pricing Table
                </a>         
            </div>
            <div class="order-1 md:order-2 col-span-2 xl:col-span-3">
                <img src='images/select-pricing-plans.png' class="rounded-lg shadow-2xl" alt="" />
            </div>
        </div>
    </div>


<div class="py-24 md:py-64 pb-12 lg:pb-16 bg-gray-100">
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
                <a href="https://app.pricewell.io/register"
                    class="button"
                    data-analytics="Signup"
                >
                    Create your free portal page
                </a>
            </div>
        </div>
    </div>

    <div class="py-24 md:py-64 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-2 md:order-1 col-span-2 self-center mt-12 md:mt-0">
            <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Gated Content
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Gated Content allows you to create a paywall for your content. You can restrict access to a single page or an entire website. Great for newsletters, courses and SaaS products.
                </p>                
                <a href="https://app.pricewell.io/register"
                    class="button"
                    data-analytics="Signup"
                >
                    Create a paywall
                </a>
            </div>
            <div class="order-1 md:order-2 col-span-2 xl:col-span-3">
                <img src='images/gated-content-screen.png' class="rounded-lg shadow-2xl" alt="" />
            </div>
        </div>
    </div>

    <div class="px-6 lg:px-8 xl:px-4">
    {{<partial "integrations">}}
    </div>

    <div class="px-6 lg:px-8 xl:px-4 pb-24 md:pb-64">
    {{<partial "testimonials">}}
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
                        Yes, of course. We are more than happy to jump on a call and discuss your particular needs. You can <a href="/book-free-demo" class="text-wedgewood-800 underline">book a time</a> in our calendar that suits you. We are experts on anything Stripe. Can Stripe change price of subscription? Just ask us.
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
                    Yes. You can use PriceWell for as many websites as you like as long as they share one <a href="/blog/stripe-login/">Stripe</a> account.  <a
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
                        class="w-10 h-10 text-green-600"
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
                    <h3 class="font-bold text-xl lg:text-2xl mb-3">Compare Plans</h3>
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
                        class="w-10 h-10 text-green-600"
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
                    <h3 class="font-bold text-xl lg:text-2xl mb-3">Need advice?</h3>
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