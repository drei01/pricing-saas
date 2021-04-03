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
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
        <div class="order-1 col-span-2 self-center mt-12 md:mt-0">
            <h1 class="text-gray-800 text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4 lg:mb-8">
                Build subscriptions into your website in minutes <br/> No coding required.
            </h1>
            <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                Subscription businesses trust PriceWell with their Pricing Infrastructure, <b>saving weeks</b> of development time.
            </p>
            <div class="flex space-x-4 mb-6">
                <a href="https://app.pricewell.io/register"
                    class="focus:outline-none inline-block bg-gradient-to-br from-blue-600 to-blue-700 hover:from-blue-500 hover:to-blue-700 font-semibold rounded-lg py-2 px-8 text-white"
                >
                    Get started for free
                </a>
            </div>

            <p class="text-gray-500 text-sm">No credit card required.</p>
        </div>
        <div class="order-2 col-span-2 xl:col-span-3 flex-col">
            <img src='images/hero.png' alt="woman lifting a pricing table into an empty space in a website" class="m-auto">
                  <!--<svg xmlns="http://www.w3.org/2000/svg"  class="w-40 mr-0 ml-auto" viewBox="0 0 485.61 100"><path d="M479.15 100a6.46 6.46 0 006.46-6.46V6.46A6.46 6.46 0 00479.15 0H173.21L152 100z" fill="#fff"/><path class="fill-current text-blue-400" d="M23.36 0H6.46A6.46 6.46 0 000 6.46v87.08A6.46 6.46 0 006.46 100H152L173.21 0z"/><g style="isolation:isolate"><path class="cls-2" d="M196.42 64.53l-10.21-27.48h5.28l7.57 21.36 7.62-21.36h5l-10.09 27.48zM210.66 54.5c0-5.89 4-10.44 9.57-10.44 5.82 0 8.92 4.4 8.92 9.91v1.53h-14.09c.35 3.44 2.41 5.55 5.36 5.55a4.55 4.55 0 004.67-3.22l3.94 1.5a8.87 8.87 0 01-8.61 5.67c-5.74 0-9.76-4.3-9.76-10.5zm4.63-2.44h9.23a4 4 0 00-4.33-4.14c-2.37 0-4.19 1.42-4.9 4.14zM244.27 49a12.85 12.85 0 00-1.69-.11 4.83 4.83 0 00-5.13 5.11v10.53h-4.59V44.44h4.59v3a5.87 5.87 0 015.51-3.1 11 11 0 011.31.08zM247.63 37.05h4.75v4.71h-4.75zm4.67 27.48h-4.59V44.44h4.59zM266.69 40.69h-1.37c-1.8 0-2.8.54-2.8 2.83v1h4.1v3.9h-4.1v16.11h-4.59V48.34h-2.79v-3.9h2.79v-1.3c0-4.17 2.33-6.51 6.85-6.51h1.91zM269.45 37.05h4.75v4.71h-4.75zm4.67 27.48h-4.59V44.44h4.59zM278 54.5c0-5.89 4-10.44 9.56-10.44 5.82 0 8.92 4.4 8.92 9.91v1.53h-14.13c.34 3.44 2.41 5.55 5.36 5.55a4.55 4.55 0 004.66-3.22l3.95 1.5a8.89 8.89 0 01-8.61 5.67C282 65 278 60.7 278 54.5zm4.63-2.44h9.22a4 4 0 00-4.32-4.14c-2.43 0-4.26 1.42-4.95 4.14zM298.88 54.5c0-5.7 3.22-10.44 8.84-10.44a7.28 7.28 0 015.78 2.52v-9.53h4.59v27.48h-4.59v-2.1a7.28 7.28 0 01-5.78 2.57c-5.62 0-8.84-4.79-8.84-10.5zm9.76-6.42c-3.33 0-5.13 2.6-5.13 6.42s1.8 6.43 5.13 6.43c2.83 0 5-2.1 5-5.81v-1.19c-.02-3.79-2.17-5.85-5-5.85zM336.43 64.53h-4.9V37.05h11c6.13 0 9.95 2.87 9.95 8.42s-3.82 8.42-9.95 8.42h-6.08zm5.81-14.85c3.53 0 5.4-1.53 5.4-4.21s-1.87-4.21-5.4-4.21h-5.81v8.42zM370.8 64.53h-4.48a10.14 10.14 0 01-.12-1.61 8 8 0 01-5.7 2c-3.82 0-6.77-2.34-6.77-5.94 0-3.82 2.87-5.51 6.73-6.31l5.54-1.19v-1c0-1.8-1.26-2.45-3.33-2.45-2.41 0-3.44 1-3.56 2.71h-4.47c.15-4.63 3.67-6.69 8.3-6.69s7.54 2.06 7.54 5.7v10a32.1 32.1 0 00.32 4.78zM366 55l-4.32.92c-1.95.42-3.41 1-3.41 2.83 0 1.57 1.15 2.45 2.91 2.45 2.45 0 4.82-1.3 4.82-3.75zM386.83 49a12.58 12.58 0 00-1.68-.11A4.83 4.83 0 00380 54v10.53h-4.59V44.44H380v3a5.87 5.87 0 015.51-3.1 10.7 10.7 0 011.3.08zM391.08 48.34h-2.79v-3.9h2.79v-5.89h4.52v5.89h4.21v3.9h-4.21v10.41c0 1.8 1 2 2.68 2a15.81 15.81 0 001.87-.11v3.86a17.85 17.85 0 01-3.17.27c-3.83 0-5.9-1.18-5.9-5.28zM403.87 44.44h4.59v2.14a7.08 7.08 0 015.54-2.52c4.21 0 6.73 2.91 6.73 7.23v13.24h-4.59v-11.9c0-2.49-1-4.29-3.52-4.29a4.16 4.16 0 00-4.17 4.4v11.79h-4.59zM424.42 54.5c0-5.89 4-10.44 9.57-10.44 5.81 0 8.91 4.4 8.91 9.91v1.53h-14.08c.34 3.44 2.41 5.55 5.36 5.55a4.56 4.56 0 004.67-3.22l3.94 1.5a8.88 8.88 0 01-8.61 5.67c-5.74 0-9.76-4.3-9.76-10.5zm4.63-2.44h9.22a4 4 0 00-4.27-4.14c-2.42 0-4.26 1.42-4.95 4.14zM458 49a12.58 12.58 0 00-1.68-.11 4.83 4.83 0 00-5.11 5.11v10.53h-4.59V44.44h4.59v3a5.87 5.87 0 015.51-3.1 10.7 10.7 0 011.3.08z"/></g><path d="M85.77 27.59v5.85L78.38 35v-5.88zm38.45 15.53c-1.86 0-3.93 1.43-3.93 4.84H128c0-3.41-1.95-4.84-3.78-4.84zm-24.62.46a4.41 4.41 0 00-3.52 1.49V56.2a4.34 4.34 0 003.47 1.42c2.72 0 4.54-3 4.54-7s-1.8-7.04-4.49-7.04zm-29.25-4.11a4.87 4.87 0 016.06-2.22v6.9c-.92-.31-3.82-.76-5.54 1.57v17.83h-7.26v-26.3h6.28zm15.42-2v26.08h-7.39V37.44zM37.61 37a19 19 0 017.32 1.38v7.13a16.21 16.21 0 00-7.33-2c-1.54 0-2.5.46-2.5 1.64 0 3.41 11.26 1.79 11.26 10.82 0 5.45-4.22 8.56-10.35 8.56a20 20 0 01-8-1.72v-7.23A18.07 18.07 0 0036 58c1.65 0 2.83-.45 2.83-1.85 0-3.61-11.21-2.25-11.21-10.64.02-5.36 4.01-8.51 9.99-8.51zm17.94-6v6.55h5.59V44h-5.59v10.73c0 4.44 4.65 3.05 5.59 2.67v6.13a11.14 11.14 0 01-5.16 1 7.5 7.5 0 01-7.65-7.75V32.6zm68.72 6c7.07 0 10.73 6.07 10.73 13.82 0 .73-.06 2.32-.1 2.73h-14.55c.33 3.55 2.89 4.59 5.8 4.59a15.54 15.54 0 007.31-1.67v6.1a16.45 16.45 0 01-8.25 2c-7.26 0-12.34-4.62-12.34-13.75 0-7.75 4.31-13.82 11.4-13.82zm-22.92 0c5.17 0 10 4.73 10 13.46 0 9.52-4.82 13.83-10.08 13.83a8.19 8.19 0 01-5.21-1.9v8.48l-7.36 1.59v-35h6.48l.38 1.86a8.16 8.16 0 015.79-2.32z" fill-rule="evenodd" fill="#fff"/><path d="M479.15 1.5a5 5 0 015 5v87.04a5 5 0 01-5 5H6.46a5 5 0 01-5-5V6.46a5 5 0 015-5h472.69m0-1.5H6.46A6.46 6.46 0 000 6.46v87.08A6.46 6.46 0 006.46 100h472.69a6.46 6.46 0 006.46-6.46V6.46A6.46 6.46 0 00479.15 0z" fill="#adbdcc"/></svg>-->

        </div>
    </div>

</div>

<div class="pb-12 lg:pb-16">
    <h2 class="w-full text-center font-bold">Powered by</h2>
    <div
        class="max-w-screen-xl mx-auto pt-4 px-6 lg:px-8 xl:px-4 grid grid-cols-auto space-y-5 sm:space-y-3 col-gap-6 opacity-75 filter-grayscale"
    >
        
        <img class="h-12 p-1 self-center justify-self-center" src='images/stripe-blurple_lg.png' alt="" />
    </div>
</div>

<div id="features" class="py-12 md:py-24 pb-12 lg:pb-16 bg-gray-100 flex flex-col place-items-center">
    <div><h3 class="text-2xl md:text-3xl">Start charging for subscription fees with PriceWell</h3></div>
    <div class="pt-8 pb-2 px-4">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-16 text-center text-lg">
            <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="w-24 mb-8 m-auto"><path d="M341.495 341.492l48.581-73.615-48.581-12.517c-6.364-19.092-17.185-37.126-32.459-52.4-15.063-15.063-32.882-26.095-52.4-32.459l-.637.637-59.188-2.334-26.307 1.697c-19.517 6.364-37.337 17.396-52.4 32.459l-78.646 78.646c-52.612 52.612-52.612 138.12 0 190.732 54.097 54.097 139.593 51.34 190.932 0l78.646-78.446c15.276-15.276 26.096-33.307 32.459-52.4zM177.354 419.3c-23.761 23.761-61.734 23.125-84.859 0-23.336-23.336-23.336-61.523 0-84.859l78.009-77.809 42.642 42.217L256 340.854 177.354 419.3z" fill="#4a696f"/><path d="M309.037 393.891l-78.646 78.446c-51.34 51.34-136.835 54.097-190.932 0L92.495 419.3c23.125 23.125 61.098 23.761 84.859 0L256 340.855l-42.853-42.006 95.89-95.89c15.274 15.274 26.095 33.307 32.459 52.4l48.581 12.517-48.581 73.615c-6.364 19.094-17.184 37.125-32.459 52.4z" fill="#384949"/><path d="M415.11 436.321l-21.215-21.215c-5.863-5.863-5.863-15.352 0-21.215 5.863-5.862 15.352-5.863 21.215 0l21.215 21.215c5.863 5.863 5.863 15.352 0 21.215-5.864 5.863-15.352 5.863-21.215 0z" fill="#d2c5c2"/><path d="M96.89 118.101L75.674 96.886c-5.863-5.863-5.863-15.352 0-21.214s15.352-5.863 21.214 0l21.214 21.214c5.863 5.863 5.863 15.352 0 21.214s-15.35 5.863-21.212.001z" fill="#dfd7d5"/><path d="M444.363 306.464c2.144-8.008 10.369-12.752 18.376-10.608l28.984 7.769c8.008 2.103 12.731 10.369 10.608 18.376-2.144 8.008-10.369 12.752-18.376 10.608l-28.984-7.769c-7.955-2.129-12.754-10.321-10.608-18.376z" fill="#d2c5c2"/><path d="M9.669 189.99c2.144-8.008 10.369-12.752 18.376-10.608l28.984 7.77c7.977 2.092 12.741 10.359 10.608 18.376-2.144 8.008-10.369 12.752-18.376 10.608l-28.984-7.77c-7.955-2.129-12.755-10.321-10.608-18.376z" fill="#dfd7d5"/><path d="M303.629 491.719l-7.77-28.984c-2.144-8.008 2.6-16.232 10.608-18.376s16.222 2.569 18.376 10.608l7.769 28.984c2.144 8.008-2.6 16.232-10.608 18.376-8.053 2.146-16.246-2.653-18.375-10.608z" fill="#d2c5c2"/><path d="M187.155 57.026l-7.77-28.984c-2.144-8.008 2.6-16.232 10.608-18.376 8.008-2.123 16.242 2.569 18.376 10.608l7.77 28.984c2.144 8.008-2.6 16.232-10.608 18.376-8.054 2.144-16.246-2.655-18.376-10.608z" fill="#dfd7d5"/><path d="M472.54 39.655c-52.612-52.612-138.108-52.825-190.932 0l-78.646 78.446c-15.274 15.274-26.094 33.306-32.459 52.4a135.954 135.954 0 00.001 86.132c6.364 19.092 17.184 37.127 32.458 52.401 14.851 14.851 32.671 25.881 52.401 32.458l.636-.636c23.337-23.337 23.336-61.523 0-84.859s-23.336-61.523 0-84.859l78.646-78.446c11.457-11.457 26.307-17.396 42.431-17.396.423-.423 4.029-.212 4.879.212 11.456-.001 26.517 6.151 37.549 17.184 23.336 23.336 23.337 61.522 0 84.859l-78.008 77.808a135.957 135.957 0 010 86.133c19.304-6.576 37.55-17.608 52.4-32.459l78.646-78.446c52.612-52.613 52.61-138.32-.002-190.932z" fill="#ffd400"/><g fill="#ff9f00"><path d="M256 340.854l-.636.636c-19.729-6.576-37.551-17.607-52.401-32.458L256 255.995c23.336 23.337 23.337 61.523 0 84.859zM472.54 230.588l-78.646 78.446c-14.85 14.851-33.095 25.883-52.4 32.459a135.957 135.957 0 000-86.133l78.008-77.808c23.337-23.337 23.336-61.523 0-84.859l53.037-53.037c52.613 52.611 52.615 138.318.001 190.932z"/></g></svg><div class="font-bold text-lg md:text-xl">Connect with Stripe</div> </div>
            <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="w-24 mb-8 m-auto"><circle cx="256" cy="256" r="245" fill="#ffaf10"/><path fill="#445ea0" d="M174.63 379.83h108V426h-108z"/><path fill="#2e4c89" d="M174.63 379.83h19.842V426H174.63z"/><path d="M333.134 450c0 2.75-2.25 5-5 5H129.131c-2.75 0-5-2.25-5-5v-20c0-2.75 2.25-5 5-5h199.003c2.75 0 5 2.25 5 5v20z" fill="#293d7c"/><path d="M143.973 450v-20c0-2.75 2.25-5 5-5h-19.842c-2.75 0-5 2.25-5 5v20c0 2.75 2.25 5 5 5h19.842c-2.75 0-5-2.25-5-5z" fill="#1a2b63"/><path d="M0 370.834c0 5.5 4.5 10 10 10h300.175v-66.951H0v56.951z" fill="#293d7c"/><path d="M19.842 370.834v-56.951H0v56.951c0 5.5 4.5 10 10 10h19.842c-5.5 0-10-4.5-10-10z" fill="#1a2b63"/><path d="M310.175 286.987c0-2.206 1.794-4 4-4h143.09V66.465c0-6.046-4.946-10.992-10.991-10.992H10.992C4.946 55.473 0 60.419 0 66.465v248.418h310.175v-27.896z" fill="#445ea0"/><path d="M310.175 286.987c0-2.206 1.794-4 4-4h121.107V82.457c0-2.75-2.25-5-5-5H26.984c-2.75 0-5 2.25-5 5v205.441c0 2.75 2.25 5 5 5h283.19l.001-5.911z" fill="#eef6ff"/><circle cx="228.63" cy="348.21" r="13.911" fill="#445ea0"/><path d="M416.361 206.376c0 2.75-2.25 5-5 5H252.904c-2.75 0-5-2.25-5-5v-72.718c0-2.75 2.25-5 5-5h158.457c2.75 0 5 2.25 5 5v72.718z" fill="#ffaf10"/><path d="M267.747 206.376v-72.718c0-2.75 2.25-5 5-5h-19.842c-2.75 0-5 2.25-5 5v72.718c0 2.75 2.25 5 5 5h19.842c-2.75 0-5-2.25-5-5z" fill="#ff9518"/><g fill="#c3ddf4"><path d="M299.266 240.121h-43.112c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h43.112c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5zM299.266 262.916h-43.112c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h43.112c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5zM351.28 240.121h-32.06c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h32.06c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5zM351.28 262.916h-32.06c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h32.06c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5zM411.772 240.121h-40.836c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h40.836c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5zM411.772 262.916h-40.836c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h40.836c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5z"/></g><g fill="#ef8318"><path d="M359.365 111.084c0 2.75-2.25 5-5 5h-10.999c-2.75 0-5-2.25-5-5v-10.999c0-2.75 2.25-5 5-5h10.999c2.75 0 5 2.25 5 5v10.999zM387.363 111.084c0 2.75-2.25 5-5 5h-10.999c-2.75 0-5-2.25-5-5v-10.999c0-2.75 2.25-5 5-5h10.999c2.75 0 5 2.25 5 5v10.999zM415.361 111.084c0 2.75-2.25 5-5 5h-10.999c-2.75 0-5-2.25-5-5v-10.999c0-2.75 2.25-5 5-5h10.999c2.75 0 5 2.25 5 5v10.999z"/></g><g fill="#69cdff"><path d="M190.898 257.005h-9c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h9a7.5 7.5 0 017.5 7.5 7.5 7.5 0 01-7.5 7.5zM156.898 257.005h-9c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h9a7.5 7.5 0 017.5 7.5 7.5 7.5 0 01-7.5 7.5zM122.897 257.005h-9c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h9a7.5 7.5 0 017.5 7.5 7.498 7.498 0 01-7.5 7.5zM88.897 257.005h-9c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h9a7.5 7.5 0 017.5 7.5c0 4.143-3.357 7.5-7.5 7.5zM220.148 226.106a7.5 7.5 0 01-7.5-7.5v-9a7.5 7.5 0 0115 0v9a7.5 7.5 0 01-7.5 7.5zM220.148 192.106a7.5 7.5 0 01-7.5-7.5v-9a7.5 7.5 0 0115 0v9a7.5 7.5 0 01-7.5 7.5zM220.148 158.106a7.5 7.5 0 01-7.5-7.5v-9a7.5 7.5 0 0115 0v9a7.5 7.5 0 01-7.5 7.5zM50.147 226.106a7.5 7.5 0 01-7.5-7.5v-9a7.5 7.5 0 0115 0v9c0 4.143-3.357 7.5-7.5 7.5zM50.147 192.106a7.5 7.5 0 01-7.5-7.5v-9a7.5 7.5 0 0115 0v9c0 4.143-3.357 7.5-7.5 7.5zM50.147 158.106a7.5 7.5 0 01-7.5-7.5v-9a7.5 7.5 0 0115 0v9c0 4.143-3.357 7.5-7.5 7.5zM190.898 121.005h-9c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h9c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5zM156.898 121.005h-9c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h9c4.142 0 7.5 3.357 7.5 7.5s-3.358 7.5-7.5 7.5zM122.897 121.005h-9c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h9c4.142 0 7.5 3.357 7.5 7.5s-3.357 7.5-7.5 7.5zM88.897 121.005h-9c-4.142 0-7.5-3.357-7.5-7.5s3.358-7.5 7.5-7.5h9c4.142 0 7.5 3.357 7.5 7.5s-3.357 7.5-7.5 7.5z"/></g><path d="M200.148 224.505c0 2.75-2.25 5-5 5h-120c-2.75 0-5-2.25-5-5v-86c0-2.75 2.25-5 5-5h120c2.75 0 5 2.25 5 5v86z" fill="#5dc1d8"/><path d="M89.99 224.505v-86c0-2.75 2.25-5 5-5H75.147c-2.75 0-5 2.25-5 5v86c0 2.75 2.25 5 5 5H94.99c-2.75 0-5-2.25-5-5z" fill="#28a5a5"/><g fill="#52bbef"><path d="M234.145 121.009c0 2.75-2.25 5-5 5h-21c-2.75 0-5-2.25-5-5v-21c0-2.75 2.25-5 5-5h21c2.75 0 5 2.25 5 5v21zM68.145 123.009c0 2.75-2.25 5-5 5h-21c-2.75 0-5-2.25-5-5v-21c0-2.75 2.25-5 5-5h21c2.75 0 5 2.25 5 5v21zM234.145 260.883c0 2.75-2.25 5-5 5h-21c-2.75 0-5-2.25-5-5v-21c0-2.75 2.25-5 5-5h21c2.75 0 5 2.25 5 5v21zM68.145 260.883c0 2.75-2.25 5-5 5h-21c-2.75 0-5-2.25-5-5v-21c0-2.75 2.25-5 5-5h21c2.75 0 5 2.25 5 5v21z"/></g><g fill="#1e99d6"><path d="M214.167 121.009v-21c0-2.75 2.25-5 5-5h-11.022c-2.75 0-5 2.25-5 5v21c0 2.75 2.25 5 5 5h11.022c-2.75 0-5-2.25-5-5zM48.167 123.009v-21c0-2.75 2.25-5 5-5H42.145c-2.75 0-5 2.25-5 5v21c0 2.75 2.25 5 5 5h11.022c-2.75 0-5-2.25-5-5zM214.167 260.883v-21c0-2.75 2.25-5 5-5h-11.022c-2.75 0-5 2.25-5 5v21c0 2.75 2.25 5 5 5h11.022c-2.75 0-5-2.25-5-5zM48.167 260.883v-21c0-2.75 2.25-5 5-5H42.145c-2.75 0-5 2.25-5 5v21c0 2.75 2.25 5 5 5h11.022c-2.75 0-5-2.25-5-5z"/></g><path d="M435.458 366.773c-.155-.422-.143-.662-.121-.74.001 0 .062-.006.119-.006.114 0 .313.023.614.134l42.104 15.465v-94.638c0-2.75-2.25-5-5-5h-159c-2.75 0-5 2.25-5 5v114.8c0 2.75 2.25 5 5 5h135.98l-14.696-40.015z" fill="#5dc1d8"/><path d="M329.017 401.787v-114.8c0-2.75 2.25-5 5-5h-19.842c-2.75 0-5 2.25-5 5v114.8c0 2.75 2.25 5 5 5h19.842c-2.75 0-5-2.25-5-5z" fill="#28a5a5"/><path d="M436.415 365.222c-1.647-.605-2.501.248-1.896 1.896l26.365 71.782c.605 1.648 2.116 1.98 3.357.739l13.997-13.997a3.203 3.203 0 014.515 0l16.128 16.13a3.202 3.202 0 004.514 0l7.674-7.674a3.202 3.202 0 000-4.514l-16.129-16.129a3.202 3.202 0 010-4.514l13.996-13.997c1.242-1.24.909-2.751-.739-3.356l-71.782-26.366z" fill="#293d7c"/></svg><div class="font-bold text-lg md:text-xl">Customize your design</div></div>
            <div><svg xmlns="http://www.w3.org/2000/svg" viewbox="0 0 512 512" class="w-24 mb-8 m-auto"><path d="M481.081 438.5H30.919C13.843 438.5 0 424.657 0 407.581V137.102h512v270.479c0 17.076-13.843 30.919-30.919 30.919z" fill="#a9dbf5"/><path d="M481.095 137.102V438.5c17.069 0 30.905-13.849 30.905-30.932V137.102z" fill="#88c3e0"/><g fill="#43809f"><path d="M103.87 233.967a7.501 7.501 0 00-10.606 0l-46.431 46.431a7.5 7.5 0 000 10.607l45.816 45.816c1.464 1.464 3.384 2.196 5.303 2.196s3.839-.732 5.303-2.196a7.5 7.5 0 000-10.607l-40.513-40.513 41.127-41.127a7.5 7.5 0 00.001-10.607zM264.52 280.397l-46.431-46.431a7.501 7.501 0 00-10.606 10.607L248.61 285.7l-40.513 40.513a7.5 7.5 0 0010.606 10.607l45.817-45.816a7.502 7.502 0 000-10.607zM185.813 206.063a7.497 7.497 0 00-9.673 4.351l-54.902 144.638a7.5 7.5 0 1014.023 5.322l54.902-144.638a7.5 7.5 0 00-4.35-9.673z"/></g><path d="M386.318 234.23h-48.419c-8.534 0-15.453-6.918-15.453-15.453 0-8.534 6.918-15.453 15.453-15.453h48.419c8.534 0 15.453 6.918 15.453 15.453 0 8.534-6.919 15.453-15.453 15.453z" fill="#29cef6"/><path d="M465.642 296.041H337.899c-8.534 0-15.453-6.918-15.453-15.453 0-8.534 6.918-15.453 15.453-15.453h127.742c8.534 0 15.453 6.918 15.453 15.453.001 8.534-6.918 15.453-15.452 15.453z" fill="#ffc328"/><path d="M427.695 357.852h-89.796c-8.534 0-15.453-6.918-15.453-15.453 0-8.534 6.918-15.453 15.453-15.453h89.796c8.534 0 15.453 6.918 15.453 15.453 0 8.534-6.919 15.453-15.453 15.453z" fill="#f78e36"/><path d="M512 147.737H0v-43.318C0 87.343 13.843 73.5 30.919 73.5h450.162C498.157 73.5 512 87.343 512 104.419z" fill="#43809f"/><path d="M481.095 73.5v74.237H512v-43.305c0-17.083-13.837-30.932-30.905-30.932z" fill="#3a7190"/><circle cx="49.455" cy="111.126" fill="#29cef6" r="15.453"/><circle cx="109.37" cy="111.126" fill="#f3f3f3" r="15.453"/><circle cx="169.285" cy="111.126" fill="#f78e36" r="15.453"/></svg><div class="font-bold text-lg md:text-xl">Copy the code snippet</div></div>
            <div><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 591.604 591" class="w-24 mb-8 m-auto"><path d="M555.879 168.52L449.105 61.543V490.23H592V255.38a122.5 122.5 0 00-36.121-86.86zm0 0" fill="#ffb782"/><path d="M83.457 412.117L2.738 202.57c-8.101-21.035 2.38-44.664 23.426-52.77L407.156 3.048c21.035-8.102 44.664 2.379 52.766 23.426L540.64 236.02c8.101 21.035-2.38 44.664-23.426 52.77l-380.98 146.753c-21.048 8.102-44.665-2.39-52.778-23.426zm0 0" fill="#de4c3c"/><path d="M489.012 101.96L32.195 279.032l30.418 78.961L519.45 181.004zm0 0" fill="#7a4930"/><path d="M.004 265.68V41.129C.004 18.582 18.285.3 40.832.3h408.273c22.547 0 40.829 18.281 40.829 40.828v224.55c0 22.548-18.282 40.829-40.829 40.829H40.832c-22.547 0-40.828-18.281-40.828-40.828zm0 0" fill="#4398d1"/><path d="M449.105.3h-43.378L99.52 306.509h349.585c22.547 0 40.829-18.281 40.829-40.828V41.129C489.934 18.582 471.652.3 449.105.3zm0 0" fill="#3e8cc7"/><path d="M40.832 163.61H81.66v20.413H40.832zm0 0M40.832 224.852H81.66v20.414H40.832zm0 0M224.555 224.852h40.828v20.414h-40.828zm0 0M102.074 163.61h40.824v20.413h-40.824zm0 0M163.313 163.61h40.828v20.413h-40.828zm0 0M224.555 163.61h40.828v20.413h-40.828zm0 0M418.484 41.129h20.414V71.75h-20.414zm0 0M377.656 41.129h20.414V71.75h-20.414zm0 0M336.828 41.129h20.414V71.75h-20.414zm0 0M296.004 41.129h20.41V71.75h-20.41zm0 0" fill="#5eb3d1"/><path d="M408.277 490.23H592v102.067H408.277zm0 0" fill="#88b337"/><path d="M378.32 184.688c-17.312-17.25-45.328-17.2-62.578.113-16.68 16.738-17.258 43.633-1.316 61.078l83.644 91.25c-25.14 44-24.066 98.258 2.785 141.23l7.422 11.871h132.688V347.336zm0 0" fill="#ffb782"/><path d="M438.898 520.852h20.414v20.414h-20.414zm0 0" fill="#6b962a"/><path d="M40.832 106.453V57.461c0-9.023 7.309-16.332 16.332-16.332h48.992c9.024 0 16.328 7.309 16.328 16.332v48.992c0 9.024-7.304 16.332-16.328 16.332H57.164c-9.023 0-16.332-7.308-16.332-16.332zm0 0" fill="#fdb62f"/><path d="M40.832 71.75h30.621v20.414H40.832zm0 0M91.867 71.75h30.617v20.414H91.867zm0 0" fill="#fd7b2f"/><path d="M530.758 347.336a10.187 10.187 0 01-7.215-2.992l-40.828-40.828c-3.918-4.051-3.805-10.512.258-14.434 3.96-3.816 10.226-3.816 14.175 0l40.829 40.828c3.98 3.992 3.98 10.453 0 14.434a10.21 10.21 0 01-7.22 2.992zm0 0" fill="#f2a46f"/></svg><div class="font-bold text-lg md:text-xl">Collect payments</div></div>
        </div>
    </div>

    <div class="font-light mt-10 px-6">Want to see the end result? Check out our own <a href="/#pricing" class="underline hover:font-bold">pricing</a>, built with PriceWell.</div>
</div>

    <section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="text-center mb-20">
      <h1 class="sm:text-3xl text-2xl font-medium text-center title-font text-gray-900 mb-4">Save weeks compared with Stripe Checkout</h1>
      <p class="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto">Implementing Stripe Checkout yourself can take weeks of development. PriceWell saves you the hastle, plus you get a copy-paste pricing page.</p>
    </div>
    <div class="flex flex-wrap lg:w-4/5 sm:mx-auto sm:mb-2 -mx-2">
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">GDPR Compliant</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Subscription Management</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">No coding required</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Pricing page included</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Instant Pricing Changes</span>
        </div>
      </div>
      <div class="p-2 sm:w-1/2 w-full">
        <div class="bg-gray-100 rounded flex p-4 h-full items-center">
          <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
            <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
            <path d="M22 4L12 14.01l-3-3"></path>
          </svg>
          <span class="title-font font-medium">Implement in 1 hour</span>
        </div>
      </div>
    </div>
    <button class="flex mx-auto mt-16 text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Button</button>
  </div>
</section>

    <div class="py-12 md:py-24 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-2 md:order-1 col-span-2 self-center mt-12 md:mt-0">
            <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Connect your Stripe account and select Plans to feature.
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Pricing plans are pulled automatically from your Stripe account. Haven't set your pricing up in Stripe yet? No worries, you can do it from PriceWell and everything syncs to Stripe.   
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
                <img src='images/customize-design.png' class="rounded-lg shadow-2xl" alt="" />
                
            </div>
            <div class="order-2 col-span-2 mt-12 md:mt-0">
                <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Designed to match your website
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Design and Customize your Pricing Page, so it matches your website’s theme and attitude. 
You can change it any time you want and the changes happen <b>live</b> on your pricing page. No need to wait for a developer to update your pricing.
                </p>
            </div>
        </div>
    </div>

    <div class="py-12 md:py-24 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-2 md:order-1 col-span-2 self-center mt-12 md:mt-0">
            <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    Copy the generated Snippet
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Upon finishing customizing, the generated snippet can be copied into your website's html. Our algorithm checks for safe installation and whether the pricing plans you have just created are online for your customers to use.
                </p>                
            </div>
            <div class="order-1 md:order-2 col-span-2 xl:col-span-3">
                <img src='images/copy-snippet.png' class="rounded-lg shadow-2xl" alt="" />
            </div>
        </div>
    </div>


<div class="py-12 md:py-24 bg-gray-100">
    <div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 grid md:grid-cols-4 xl:grid-cols-5 gap-x-12 lg:gap-x-20">
            <div class="order-1 col-span-2 xl:col-span-3 self-center">
                <img src='images/pricing-page-2.png' class="rounded-lg shadow-2xl" alt="" />
                
            </div>
            <div class="order-2 col-span-2 mt-12 md:mt-0">
                <h2 class="text-gray-800 text-2xl md:text-3xl lg:text-4xl font-bold mb-2 md:mb-4 lg:mb-8">
                    You are ready to collect payments 🎉
                </h2>
                <p class="text-lg xl:text-xl text-gray-600 mb-6 lg:mb-8 xl:mb-10">
                    Without a single line of code written. Now you can concentrate on providing value for your customers without worrying whether your payment process is working. 
                </p>
            </div>
        </div>
    </div>

<div class="bg-gray-100">
<div class="max-w-screen-xl mx-auto px-6 lg:px-8 xl:px-4 py-12 lg:py-16 xl:py-24 bg-black">
    <div class="text-center mb-6 md:mb-8">
        <h2 id="pricing" class="text-white text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4">Grow your business with our tailored pricing</h2>
        <p class="text-lg xl:text-xl text-gray-200 relative w-1/2 m-auto">Oh, and our pricing is made with PriceWell <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 372.136 372.136" class="w-12 ml-10 transform rotate-120 fill-current text-white"><path d="M371.682 143.271c-14.688-44.676-26.316-90.576-50.797-131.58-2.447-4.284-10.403-5.508-12.239 0-17.748 42.228-36.108 83.844-47.736 127.908-1.836 7.344 7.344 12.852 12.852 7.344 10.404-10.404 21.421-20.196 33.049-28.764-1.225 90.576 1.836 195.84-105.876 223.992-47.736 12.24-100.98 5.509-140.76-25.092C18.557 284.644 9.377 231.4 12.437 181.828c0-4.896-7.344-6.12-8.568-1.224-23.868 110.772 66.096 197.064 176.256 181.764 54.468-7.344 100.368-33.048 123.624-85.068 20.809-46.512 19.584-102.204 18.36-153 11.628 10.404 24.479 19.584 37.943 26.928 6.121 3.672 14.077-1.224 11.63-7.957zm-55.08-40.391c-3.672-1.224-6.12.612-7.345 3.672l-.611.612c-9.792 3.06-18.36 7.956-26.316 13.464 9.18-29.988 21.42-59.364 33.048-88.128 15.912 29.988 25.092 62.424 35.496 94.248-11.017-9.18-21.421-18.36-34.272-23.868z"/></svg></p>
    </div>

    {{< partial "pricing" >}}

    <div class="text-gray-300 pt-8">
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
                            Can I use my Stripe account in Test mode
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