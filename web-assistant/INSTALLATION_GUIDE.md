# 🛠️ C2M WEB ASSISTANT INSTALLATION GUIDE
**Credit 2 Money Solutions** | Implementation Manual  

---

## 1. Quick Overview
The `c2m-chat-widget.html` is a self-contained, responsive conversational widget engineered to sit in the bottom corner of `credit2money.org` or run as a standalone landing page widget.

It automates:
- 24/7 lead intake.
- Initial triage (Credit repair vs. 0% Business funding vs. $100 flash sale).
- Phone & email collection routed to Antoine's CRM or notifications.
- CROA & TSR legal disclaimer presentation.

---

## 2. Embedding into Websites

### Option A: WordPress / Wix / Squarespace / Webflow
1. In your page builder, add a **Custom HTML / Embed** element to your site footer.
2. Paste the contents of `c2m-chat-widget.html`.
3. Set the widget positioning to `fixed; bottom: 20px; right: 20px; z-index: 9999;` to float over all pages.

### Option B: GoHighLevel (GHL) / LeadConnector
1. In GHL, navigate to **Sites > Funnels / Websites > Settings**.
2. Paste the embed script into the **Body Tracking Code** box.
3. Replace the `respondToAction` function with a webhook call to your GHL Inbound Webhook trigger (`POST https://services.leadconnectorhq.com/hooks/...`) to automatically create contacts and trigger SMS follow-ups!
