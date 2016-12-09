Title: UI5 Model Inspector
Date: 2016-12-08 00:00
Modified: 2016-12-08 00:00
Tags: openui5, sapui5, bower
Slug: ui5-model-inspector
Summary: SAPUI5/OpenUI5 custom control to inspect runtime models.
About_author: builds custom controls

![UI5 Model Inspector](http://i.imgur.com/hLtE5hk.png)

Over the past two years, I've spent a fair amount of time getting familiar with the 
open source JavaScript UI library [OpenUI5](http://openui5.org), maintained by SAP.

While working on more than a handful of OpenUI5 applications, I've always had a desire 
to see _more_ of what's going on behind the scenes while my application is running. 

For those unfamiliar with this framework, most of the data (and content) of your application 
is driven by models defined from your JavaScript controller, and populated by your back-end 
API, or from business logic you have written. 

Of course, the OpenUI5 team has since made their debugging tools stronger with the release of 
UI5 Inspector - available as a Google Chrome extension. 

![UI5 Inspector](http://i.imgur.com/OPSIfAY.png)

The tool works great - and it was embedded into the Chrome Developer Console which is 
open nearly all the time anyway. To be honest, the only times I needed to use the 
inspector is when I had controls on the screen which I had tried to bind to a data 
model, but for some reason were not showing the data I expected. So I'd open the 
inspector to check the control's bindings. If the value I expected wasn't there, I 
knew I had entered my binding information incorrectly.

Sometimes, however, my binding information was correct, but the model was still empty. 
Without putting a breakpoint in my JavaScript, I had no reliable way to check the 
content of my models. 

Thus, `ui5-model-inspector` was born. 

<img src="http://i.imgur.com/MOG29hu.png" alt="Inspecting an OData Model" style="height: 400px;display: block;margin: 0 auto;"/>

The secret sauce of the UI5 Model Inspector control is that it lives in the view. I had 
originally hoped to replicate the functionality of the [validator](https://github.com/SAP/openSAP-ui5-course/blob/gh-pages/Validator.js) built for the openSAP course 
[Developing Web Apps with SAPUI5](https://open.sap.com/courses/ui51). However, I was having 
a _very_ difficult time attaching to the same `sap.ui.core` instance as the running 
application. The reason this became an issue is that I wasn't able to identify any models 
that were running! The easiest way around this was to change course and build a custom 
control that could be injected into any view.

Once running from the view, it was easy to pull all "propogated properties" available 
to the view object. 

    :::javascript
    /**
     * Get model names from context object
     * 
     * Use UI5 internal properties to identify models available
     * to inspect. Since there is no public API to retrieve these 
     * model names (to my knowledge), we access internal properties
     * directly.
     * 
     * @param {sap.ui.base} oContext - Context object to inspect for available models
     * @returns {string[]} aModelNames - models available within provided context 
     */
    _getModelNamesFromContext: function (oContext) {
      var aModelNames = [];
      // 1. Get Models directly assigned to context object
      if (oContext.oModels) {
        for (var sModelName in oContext.oModels) {
          aModelNames.push(sModelName);
        }
      }
      // 2. Get Models propogated down to this context object
      if (oContext.oPropagatedProperties && oContext.oPropagatedProperties.oModels) {
        for (var sModelName in oContext.oPropagatedProperties.oModels) {
          aModelNames.push(sModelName);
        }
      }
      return $.unique(aModelNames).sort();
    }

From there, it was easy enough to iterate through the properties of each model that 
I found. I was able to identify the type of most properties found in each model, so 
I could use proper controls to modify those properties - `sap.m.Switch` for boolean, 
`sap.m.Input` for strings and numbers, etc. 

It was a very fun project to do, and I am looking forward to making more custom controls 
in the future - provided I have a good reason to do so. 

* [ui5-model-inspector Source](https://github.com/mitch-b/ui5-model-inspector)


