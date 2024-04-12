---
title: 'SaaS Million Dollar Customer Calculator'
description: 'Want to make a million dollars? Use this calculator to find out how many customers you need to reach your goal.'
date: 2024-03-07T09:03:46+02:00
draft: false
---

{{<rawhtml>}}
<script src="https://cdnjs.cloudflare.com/ajax/libs/dom-to-image/2.6.0/dom-to-image.min.js" referrerpolicy="no-referrer" async></script>
   
<style>
@import url(https://fonts.googleapis.com/css?family=Work+Sans:300,400);
.calculator {
    font-family: "Work Sans", "Helvetica", sans-serif;
  font-size: 0.9em;
  line-height: 1.45;
  padding-left: 9%;
}

.giant-letters, h1, .form {
  font-size: 50px;
  line-height: 2;
  letter-spacing: -1px;
  font-weight: 300;
}

.form::first-line {
  line-height: 1;
}

.input, .select {
  font: 300 50px "Work Sans", "Helvetica", sans-serif;
  border: 0;
  outline: none;
  color: white;
  background-color: #ee5757;
}

.form-wrapper {
  position: relative;
}

.input {
  -webkit-appearance: none;
  padding: 10px 10px 10px 45px;
  width: 270px;
  margin-left: 5px;
}

.input__label {
  display: inline-block;
  position: absolute;
  top: -5px;
  left: 0;
  padding: 0 0 0 20px;
  font-size: 70%;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
  color: white;
}

.calculated-result {
  border-bottom: solid 10px #ee5757;
  min-width: 80px;
  display: inline-block;
  margin-right: 10px;
}

.data {
  background: #222;
  color: white;
  padding: 100px 40px;
}

@media (min-width: 1285px) {
  .calculator, .data {
    display: inline-block;
  }

  .calculator {
    float: left;
    width: 60%;
    padding-left: 2%;
  }

  .data {
    float: right;
    width: 40%;
    padding: 20px 40px;
  }
}
.data p, .data h1, .data table {
  width: 80%;
}</style>

<div class="bg-gray-100 py-12">
<h1 class="text-gray-800 text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4 lg:mb-8 text-center">
    SaaS Million Dollar Customer Calculator
</h1>
<h3 class="text-2xl leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto mb-4 px-4">How much should you charge for your SaaS? Use our calculator to work how many customers you need to reach that magic✨ million dollars ARR (Annual Run Rate).</h3>
 </div>

<section class="calculator bg-white relative py-16" id="calculator"></section>

<script type="module">
    import { html, Component, render, useState, useEffect } from 'https://unpkg.com/htm/preact/standalone.module.js';


function Calculator() {
	const [targetAmount, setTargetAmount] = useState("1000000");
	const [monthlyCharge, setMonthlyCharge] = useState();
	const [requiredCustomers, setRequiredCustomers] = useState();
	const handleTargetChange = (e) =>
		setTargetAmount(e.currentTarget.value);
	const handleChangeMonthlyCharge = (e) =>
		setMonthlyCharge(e.currentTarget.value);
    const handleShareImage = (e) => {
        e.currentTarget.remove();
        domtoimage.toJpeg(document.getElementById('calculator'))
        .then((dataUrl) => {
            var link = document.createElement('a');
            link.download = 'pricewell.jpeg';
            link.href = dataUrl;
            link.click();
        });
    };

	useEffect(() => {
		if (isNaN(targetAmount) || isNaN(monthlyCharge) || monthlyCharge === "0") {
			return;
		}
		const customers = (
			parseInt(targetAmount) / (parseInt(monthlyCharge) * 12).toFixed(0)
		).toFixed(0);
		setRequiredCustomers(isNaN(customers) ? "" : Math.max(1, customers));
	}, [targetAmount, monthlyCharge]);

	return html`<React.Fragment>
		<div className="form">
			I want to make
			<br />
			<span className="form-wrapper">
				<input
		className="input"
					type="number"
					min="0"
					step="100"
					onChange=${handleTargetChange}
					value=${targetAmount}
				/>
				<label className="input__label">
					<span className="input__label-content">$</span>
				</label>
			</span>
			ARR. <br />I charge
			<span className="form-wrapper">
				<input
					className="input"
					type="number"
					min="0"
					step="100"
					value=${monthlyCharge}
					onChange=${handleChangeMonthlyCharge}
				/>
				<label className="input__label">
					<span className="input__label-content">$</span>
				</label>
			</span>
			/ mo.
			<br />I need <span className="calculated-result mr-2">
				${requiredCustomers}
			</span>
			customer${!requiredCustomers || requiredCustomers > 1 ? "s" : ""}.
		</div>
        <div className="absolute bottom-4 left-4">
        <button onClick=${handleShareImage} className="flex items-center px-4 py-2 space-x-3 text-gray-600 transition-colors duration-300 transform border rounded-lg lg:flex focus:outline-none text-black hover:bg-gray-500"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-6 h-6">
  <path strokeLinecap="round" strokeLinejoin="round" d="M7.217 10.907a2.25 2.25 0 1 0 0 2.186m0-2.186c.18.324.283.696.283 1.093s-.103.77-.283 1.093m0-2.186 9.566-5.314m-9.566 7.5 9.566 5.314m0 0a2.25 2.25 0 1 0 3.935 2.186 2.25 2.25 0 0 0-3.935-2.186Zm0-12.814a2.25 2.25 0 1 0 3.933-2.185 2.25 2.25 0 0 0-3.933 2.185Z" />
</svg>

<span>Share image</span></button>
        </div>
<div className="absolute bottom-4 right-4 mb-1 rounded-md border bg-white px-2 py-1 align-middle text-xs font-medium text-gray-600 backdrop-blur-lg"><a href="https://www.pricewell.com/?utm_source=poweredby" className="text-xs text-gray-800 font-light hover:underline" rel="noopener noreferrer"><svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 59.998 59.998" className="inline w-4 mr-1 align-bottom"><path d="M59.206.293a.999.999 0 0 0-1.414 0L54.085 4H30.802L1.532 33.511c-.666.666-1.033 1.553-1.033 2.495s.367 1.829 1.033 2.495l20.466 20.466a3.51 3.51 0 0 0 2.491 1.031 3.54 3.54 0 0 0 2.509-1.041l28.501-29.271V5.414l3.707-3.707a.999.999 0 0 0 0-1.414zm-5.707 28.581L25.574 57.553a1.53 1.53 0 0 1-2.162 0L2.946 37.087a1.532 1.532 0 0 1 .003-2.165L31.636 6h20.449l-4.833 4.833A4.969 4.969 0 0 0 44.499 10c-2.757 0-5 2.243-5 5s2.243 5 5 5 5-2.243 5-5a4.969 4.969 0 0 0-.833-2.753l4.833-4.833v21.46zm-6-13.874c0 1.654-1.346 3-3 3s-3-1.346-3-3 1.346-3 3-3c.462 0 .894.114 1.285.301l-1.992 1.992a.999.999 0 1 0 1.414 1.414l1.992-1.992c.188.391.301.823.301 1.285z"></path></svg>Powered By PriceWell</a></div>
</React.Fragment>`;
}

render(html`<${Calculator}/>`, document.getElementById("calculator"));

</script>
<div class="bg-gray-100 pt-24 pb-12">
<h3 class="text-gray-800 text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4 lg:mb-8 text-center">
    Now what?
</h3>
<p class="text-2xl leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto mb-4 px-4">Now you know what you have to charge your customers to earn a Million dollars a year. Next, it's time to build your app. There's a bunch of no-code tools like <a href="https://bubble.io/template/saas-stripe-billing-included-1696494539976x572962782574018600" class="underline">Bubble</a>, <a href="https://help.pricewell.com/integrations/webflow/" class="underline">Webflow</a> and even <a href="https://help.pricewell.com/integrations/notion-and-super-so/" class="underline">Notion</a>. Now you need a way to accept payments with Stripe. That's where PriceWell comes in 👇🏻 </p>
 </div>
<div class="flex justify-center bg-gray-100 pt-12">
<div class="w-full md:w-1/2 px-4">
{{< partial "promo-video">}}
</div>
</div>

<div class="pt-24 md:pt-48 pb-24 mb:pb-64 bg-gray-100">
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
            </div>
            <div class="order-1 md:order-2 col-span-2 xl:col-span-3">
                <img src='images/gated-content-screen.png' class="rounded-lg shadow-2xl" alt="" />
            </div>
        </div>
    </div>

<div class="bg-gray-100 py-12">
<h2 class="text-gray-800 text-3xl md:text-4xl lg:text-5xl font-bold mb-2 md:mb-4 lg:mb-8 text-center">
    Save $1,000's vs hiring a developer
</h2>
<div class="max-w-2xl m-auto">
 <div class="senja-frame-embed" data-id="653c0c07-e8a3-403d-8b35-9336433e060b"></div>
 </div>

{{</rawhtml>}}

{{< partial "pricing" >}}
{{< partial "pricing-explainer">}}
