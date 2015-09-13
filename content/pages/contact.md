Title: Contact
Date: 2015-09-13 00:00
Modified: 2015-09-13 00:00
Slug: contact
Authors: Mitchell Barry
Summary: Contact Me

Thanks for reaching out! I'd be thrilled to meet to discuss your product idea, or help step through an issue you're having.

* [GitHub](https://github.com/mitch-b)
* [BitBucket](https://bitbucket.org/mitch-b)
* Email me below

I am available for:

* [OpenUI5](http://openui5.org)
* C#.NET (ASP.NET MVC, WebAPI)
* OData (ASP.NET WebAPI, design)
* Architecture reviews
* Speaking engagements

<form id="submitForm" class="pure-form-stacked" method="POST" action="http://formspree.io/me@mitchbarry.com">

  <label for="_replyto">Email</label>
  <input type="email" name="_replyto" placeholder="Your email" />
  <label for="body">Message</label>
  <textarea name="body" rows="5" placeholder="What kind of help are you looking for?"></textarea>
  <input type="submit" class="pure-button pure-button-primary" value="Send Message" />
  
  <!-- hidden elements used by formspree.io -->
  <input type="hidden" name="_subject" value="Website Contact" />
  <input type="hidden" name="_next" value="//mitchbarry.com/contact/?sent=true" />
  <input type="text" name="_gotcha" style="display:none" />
</form>

<section id="confirm" style="display:none;">
  <aside><p><strong>Thank you for your interest! I will respond as soon as I can.</strong></p></aside>
</section>

<script>
(function() {
  if (/[?&]sent=true/.test(location.href)) {
    document.getElementById('submitForm').style.display = 'none';
    document.getElementById('confirm').style.display = 'inline';
  }
}());
</script>