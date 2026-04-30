---
title: Website Support Process Guide
sidebar_label: "Website Support Process Guide"
sidebar_position: 1
---

# Website Support Process Guide

## Table of Contents

- [**Website Import Support**](#website-import-support)
- [**Project Steps and Assignees**](#project-steps-and-assignees)
- [**Client Engagement Steps**](#client-engagement-steps)
- [**Website Support Steps – Vet Website**](#website-support-steps--vet-website)
- [**Send Import Approval/Rejection Email**](#send-import-approvalrejection-email)
- [**Add-Ons Activated**](#add-ons-activated)
- [**Complete Website Import**](#complete-website-import)
- [**Adjust DNS Records**](#adjust-dns-records)
- [**Publication Email Sent**](#publication-email-sent)
- [**FindLaw Imports**](#findlaw-imports)
- [**Imports with Website Files**](#imports-with-website-files)
- [**Website Support (Tiers)**](#website-support-tiers)
- [**Process Guide for Client Engagement**](#process-guide-for-client-engagement)
- [**Process Guide for Website Support Specialists**](#process-guide-for-website-support-specialists)
- [**Process Guide for Website Support QA**](#process-guide-for-website-support-qa)
- [**Posting Blogs**](#posting-blogs)
- [**Google Workspace Set Up**](#google-workspace-set-up)
- [**Inbox Pro Enablement**](#inbox-pro-enablement)

---

## Website Import Support

This section covers the end-to-end process for importing and supporting client websites, including vetting, import steps, DNS, and handoff.

---

## Project Steps and Assignees

| Step | Assignee |
|------|----------|
| Send Confirmation Email | Client Engagement Admin |
| Domain Back-End Access Received | Client Engagement Assignee |
| Vet Websites | Website Support Specialist |
| Send Import Approval/Rejection Email | Drafted by Website Support Specialist, Sent by Client Engagement Assignee |
| Add-Ons Activated | Website Support Leadership |
| Complete Website Import | Website Support Specialist |
| Adjust DNS Records | Website Support Specialist |
| Publication Email Sent | Client Engagement Admin / Client Engagement |

---

## Client Engagement Steps

### Send Confirmation Email

The Admin team will send the **Order Confirmation** email to the contacts listed on the order form to confirm we have received the request to vet the website to be imported and/or supported.

### Domain Backend Access Received

- Communications will check that we have received **Domain** and **WordPress backend login credentials** and that they are valid.
- If not, follow up with the client/Partner to ensure the correct credentials are received.
- Once we have the credentials, send the **Websites - Import Vetting Receipt** macro to the client with the due date of **2 business days**.
- The ticket should be assigned to **Website Support as On-Hold** with a due date of **two business (M–F) days** from the time we receive the credentials.

**Note:** If we have the WordPress Admin credentials, we can begin the process without the domain credentials. These can be obtained later in the process.

- The website support team will respond to the email with a confirmation if we can support the website or not. Send the information to the partner/client with the update.
- **If the website is REJECTED** — ensure all tasks in the project are closed.
- **If the website is APPROVED** — assign the ticket back to **MS Website Support** with:
  - **Internal Notes:** PID/SMB/AGID/VTM
  - **Due date:** 3 Business Days
  - **Website Support Tier:** Import
  - **Status:** ON HOLD  
  The ticket will be reassigned to you when the import has been completed.

---

## Website Support Steps – Vet Website

**Note:** The development of the site should be done in the **Production environment** unless there is a branded domain connected.

Within **2 days** of receiving the domain and WordPress credentials from the partner or client, Website Support will log into the site to be imported and/or supported and check (vet) if it is a site we can support or not.

### Vetting a Website for Import and Support

Check the following to verify if a site is eligible for import:

| Check | Guidance |
|-------|----------|
| **Themes** | Ensure the theme is **not** a custom coded theme (they use sections that have to be custom created; adding to those pages becomes problematic due to HTML, CSS, and taxonomy issues). Ensure the theme is up to date — typically within **6 months to 1 year**. |
| **Plugins** | Ensure plugins are up to date — usually within the last **6 months to 1 year**. Older versions can cause issues and functionality may not be intact once updated. |
| **ACF (Advanced Custom Fields)** | We actively try to **avoid** sites with these. Updating plugins, especially on older versions, can cause issues with functionality. |
| **Multiple website builders** | These will cause issues; many leave code in the backend of each page that should have been deleted and can cause functionality issues. |

- **If Yes** — Proceed with the rest of the steps. In Zendesk, Support Specialists reply to the Vetting Process email thread with an internal macro which includes the website URL and license keys.
- **If No** — Send Approval/Rejection Email rejecting the import. Provide the reason to the client/Partner for the rejection. Close out the rest of the tasks.

---

## Send Import Approval/Rejection Email

- Use the macro in Zendesk: **Websites - Website Vetting Reject/Accept**.
- Keep the **red** portion of the macro for rejected imports and the **green** portion for accepted imports.
- Ensure the approval or rejection is updated in **VTM**.

**Template (adjust as needed):**

> Hey [Name],  
> We have reviewed the website URL for import and we **are / are not** able to import and support this site.  
> **Rejected:** Reason for Rejection. Please note that we do offer website rebuilds and that is our recommendation at this time.  
> **Accepted:** We are excited to begin importing your website. Your site will be imported within 3 business days (due date: [date]). We have activated the Website Support add-on product and Website Pro on your behalf to begin the import process. If you have any questions, please do not hesitate to reach out!  
> Please note: in order to keep communications organized, please use this email thread only. It will help prevent the loss of content from you and your team and also ensure we don't miss anything on our end. Thank you!

---

## Add-Ons Activated

The following add-ons/products need to be activated upon approval of website import:

| Product | Description |
|---------|-------------|
| **Website Import (Add-on)** | $200 set-up fee, one-time charge |
| **Website Support+** | $30/month Support SKU. **3-month commitment** |
| **WordPress Hosting \| Pro** | As needed for hosting |

---

## Complete Website Import

1. Log into the website on the **external Hosting Platform**.
2. **DO NOT UPDATE PLUGINS OR THEMES** at this stage.
3. Open **Plugins** and install and activate **WP All-in-One Migration** plugin.  
   You may also need the **WP All-in-One Unlimited Extension** depending on the size of the website: [All-in-One WP Migration Unlimited Extension](https://wiki.marketingservices.dev/wp-content/uploads/2024/07/all-in-one-wp-migration-unlimited-extension.zip).
4. Open **WP All in One Migration** and select **Export**. When you select **Export** → **Advanced Options**: select **Do not replace email domain**; **Export To** → **Select File**.
5. Open the account in **WordPress Hosting Pro** from [Partner Center](https://partners.vendasta.com/dashboard).
6. Keep the domain and title information as default (unless domain is unavailable).

   ![](/img/sop-website-support/image8.png)

7. Select **blank template** — wait for WordPress to install.
8. Open the **WordPress Dashboard**. Under **Plugins**, install **WP All in One Migration** (ignore if already installed). If the plugin asks for the Unlimited version of All-In-One, use [this link](https://wiki.marketingservices.dev/wp-content/uploads/2024/07/all-in-one-wp-migration-unlimited-extension.zip).
9. Select **Import** and choose the file you exported from the old hosting.

10. **Update themes, plugins, and WordPress Core** after import.
11. Review the website and ensure all links and functionality are working.
12. In the **footer**, ensure the name of the **Agency** has been changed to the new Agency that has had the site imported, along with the link to the new Agency.

---

## Adjust DNS Records

Once we have received approval from the Partner, adjust the DNS settings to push the site live:

| Record Type | Host | Value |
|-------------|------|--------|
| **A** | @ | 34.149.86.124 |
| **CNAME** | Www | https://host.websiteprohosting.com |

In the **Website Pro** dashboard:

1. Select **Domains** → **Connect a Domain**.
2. **Add Domain** — check the box to include **www** and add the domain.
3. Once the domains populate, set the **primary domain** to the custom domain **without** the www.

---

## Publication Email Sent

- Select the **Website Import Completed** email (a white-label version is available for Partners with White/Grey Label emails), update, edit, and send.
- Send the ticket to the **QA Specialist** and close out all tasks in the VTM project after the notes have been made.

**Note:** If Website Pro is deactivated for more than **3 months**, the site cannot be retrieved if the instance is activated again. We can restore the website after deactivation of Website Pro within **365 days**, but it will require **1x hour** for re-import on a new instance of Website Pro.

---

## FindLaw Imports

**Must be approved by Management.**

In the case of an import that has been previously hosted on **FindLaw**: the only PID approved to import these sites is **HV68 - Capstone Marketing**; all other PIDs must receive approval from Website Support leaders to proceed. The files for these websites will be provided to us and must be imported uniquely.

### Process

1. Install a local instance of WordPress on your computer.
2. Add **WP Prime Mover** to the WP instance.
3. Import the website into the local instance of WordPress on your device.
4. **Remove WP Prime Mover** (this plugin is not compatible with Website Pro).
5. Install the **All-In-One Migration** and **Unlimited** plugins.
6. Export the website from the local instance using All-in-One.
7. Once exported using All-in-One, we can proceed with **standard import steps** to bring the website into Website Pro.

While the website is being imported, we will receive a list of plugins that are no longer present on the website; please make note of these in the [Capstone Marketing Import Checklist](https://docs.google.com/document/d/1r6beRnGEWIDAKZc4NTz7emljUiSHQRo1oR0oh_FnFik/edit?usp=sharing) under **Audit Plug-Ins after Import**.

Once this initial import is completed, Client Engagement will communicate the turnaround time to the Partner as determined by the website support team and approved by the Website Support Manager. The typical turnaround time on these websites is about **10 business days**. Once turnaround time is communicated to the Partner, the work can begin. Please refer to the [Capstone Marketing Import Checklist](https://docs.google.com/document/d/1r6beRnGEWIDAKZc4NTz7emljUiSHQRo1oR0oh_FnFik/edit?tab=t.0#heading=h.bllyran0q013) for tasks to be completed and checked over.

### Checklist

**Contact Forms**

- Contact forms need to be rebuilt in Gravity Forms.
- Recaptcha needs to be added to the form.
- The form needs to be tested to confirm they are sending to the correct email address.

**Header / Navigation**

- Check that all links in the Navigation are correctly pointing to the appropriate pages.
- Rebuild the side menu bar on the services pages.
- Confirm Logo and Favicon are displaying correctly.
- Ensure the correct phone number is showing at the top of the page.

**Footer**

- Add the provided disclaimer to the footer (see Checklist).
- Change the copyright information.

**Plugins**

- Complete a plugin audit and let the Partner know any plugins that need to be repurchased.
- Install **Divi Blurb Extended Plugin** (For Capstone sites; all other PIDs need to purchase this plugin). The file is linked in the checklist.

**Website Edits**

- Audit each page on the website and ensure that links are working.
- Ensure all Social Media is linking to the correct page.
- Replace missing images.
- Add Privacy Policy page.
- Delete user access from Thomson Reuters emails.
- Update Blog author to admin.
- Update blog pages (check links and images).
- Check the content and replace the Phone and firm name with the correct information.
- Ensure the appropriate Meta Titles and Descriptions are showing. Please pay attention to the phone number listed.

Once this work is completed, assign the website to **Support QA** to check over before sending it back to Client Engagement. When we receive the green light, push the website live.

---

## Imports with Website Files

For websites where we are not able to gain backend admin access to vet the site for import and support, we can vet the site via a file. Depending on the file type we typically charge **1x Hourly Charge** for the work needed to vet a site this way. There are typically two types of files that we can use to vet a site for import and support.

| File Type | Notes |
|-----------|--------|
| **All-in-One files (.wpress)** | Can be imported into Website Pro. If we can support the site, proceed as per normal — no need to charge the additional hour. If we cannot, inform the partner that we cannot support the site; charge **1x hourly** as the site was imported and that work was completed. |
| **Backup files (.zip, .tar.gz)** | More complicated. All websites vetted this way need **1 hour charged** regardless of whether we can import them. |

---

## Website Support Tiers

Website Support requests are divided into **three tiers** (plus Tier 0) based on type and complexity. The tier determines turnaround time. A **Website Support leader** must approve any task/request that is urgent and requires same-day turnaround.

| Tier | VTM Task Name | Turnaround Time | Types of Requests | Examples |
|------|----------------|-----------------|-------------------|----------|
| **Tier 0** | Website Support Request T0 | 1 Business Day | Quick basic website support requests | Photo changes, colour changes, button updates |
| **Tier 1** | Website Support Request T1 | 1 Business Day | Basic website support requests | Basic requests, changes, updates; information updates; website down; uploading blogs; **pushing websites live**** |
| **Tier 2** | Website Support Request T2 | 1 Business Day | Lengthy requests, multiple edits | Large number of edits; requests that take longer than 30 minutes; Adobe XD or markup files; documents with edits |
| **Tier 3** | Website Support Request T3 | 1 Business Day | Technical requests | Integrations; changes to website functionality; plugins; hourly charges; email issues; analytics; indexing concerns |

**\*\*Pushing websites live:** DNS records should **not** be adjusted any later than **2:00 PM CST** Monday–Thursday or **noon on Fridays**. Delays in SSL certificate generation can cause the site to go down until SSL is generated in Website Pro. We strongly recommend against pushing sites live after noon on Fridays; if an issue arises, there may be no one available to troubleshoot until Monday morning.

---

## Process Guide for Client Engagement

1. When a website support request is received, compose a response to the Partner or SMB using the **Website Support Request** macro in Zendesk. This email needs to summarize the support request to the client to confirm the desired website edits to be completed.
2. Keep the ticket in the Client Engagement assignee’s queue as **Pending** with a due date of **1–5 days** depending on the type of request.
3. Open the **Website Build** project in VMKA and add a task labeled: **Website Support Request T1**, **Website Support Request T2**, or **Website Support Request T3**. This wording must be EXACT, including capitalization and spacing for tracking purposes.
   - **Website Support Request T1**
   - **Website Support Request T2**
   - **Website Support Request T3**
4. Create a new task in **VTM (Vendasta Task Manager)**. Fill in the following information:
   - List of edits or work requested
   - Main Zendesk ticket number (this is the Zendesk ticket from step 1)
   - Assign to **Website Support** with:
     - **Service Category:** Website Support
     - **Service Level:** (Verticals / Agency / High Velocity)
     - **Classification:** Support Request
     - **Type:** Task
     - **Due Date:** Tier 1 = next business day; Tier 2/3 = 3 business days from today
     - **Website Support Tier:** Match the VTM task
   - Submit the Internal ticket as: **Tier 1 – On Hold**; **Tier 2 or 3 – Open**
5. These requests need to be reviewed by website support to determine if any additional time or hourly charges are needed.
6. Add an internal note to the main ticket thread referencing the submitted internal Website Support ticket number. The main ticket and internal ticket should both have the same due date as the VTM task.

---

## Process Guide for Website Support Specialists

- Review all tickets assigned to you to ensure you have everything necessary to complete the request.
- **Order of completion:** Imports → Tier 2/3 tickets (up to 3 days old) → Tier 1 tickets.

### Tier 1 Requests (Due 1 business day after request)

- Once completed, send the ticket to the **QA** team member for review.
- Log the request information in the **website support QA tracking sheet**.

### Tier 2 Requests (Due 3 business days after request)

- Once completed, send to QA for review and log in the QA tracking sheet.
- Follow-up questions without edits do not need to be QA’d.

### Tier 3 Requests (Due 3 business days after request)

- Review to ensure we are not missing any assets or information.
- If we cannot deliver by the due date, inform Client Engagement immediately with the updated completion date.
- Once completed, send to QA for review and log in the QA tracking sheet.
- Follow-up questions without edits do not need to be QA’d.

---

## Process Guide for Website Support QA

- Tickets are assigned to QA after completion by Website Support.
- Ensure ticket information was entered into the **Website Support Quality Assurance Error Log**.
- Review the requested edits and check them against the **live site** to ensure they were completed as requested.
- If there are discrepancies, log them in the **QA Error Log**, then reassign the ticket to the Specialist who completed the work.
- If there are no errors, assign the ticket back to the **Client Engagement Assignee** as **Open**.
- If there are issues **unrelated** to the requested edits, update Client Engagement and request reassignment as a T1 or T3 request with the appropriate due date and a new VTM task.

---

## Posting Blogs

| Blog Written By | Website Hosting | Website Support | Do We Post? |
|-----------------|-----------------|-----------------|-------------|
| Vendasta Services | WordPress Hosting Active | Yes | **Yes** |
| Vendasta Services | WordPress Hosting Not active | Yes | **Yes** |
| Vendasta Services | Duda (All Duda sites have Support) | Yes | **Yes** |
| Vendasta Services | External Hosting, Channel Partner – No Support | No* | **Yes** |
| Vendasta Services | External Hosting, Direct/Broadly – External Support Active | Yes | **Yes** |
| Partner / Client | WordPress Hosting Active | Yes | **Yes** |
| Partner / Client | WordPress Hosting Not Active | No | **No** |
| Partner / Client | External Hosting, Channel Partner – No Support | No | **No** |
| Partner / Client | External Hosting, Direct/Broadly – External Support Active | Yes | **Yes** |

- Where we do **not** post but Vendasta Services is the author of the blog, **Custom Request** can be activated as an add-on to the Blog Product for posting (monthly recurring or one-time).
- For blogs written by partners or clients, we will post **up to 3** for sites with active Website Support at no additional cost. After 3 blogs, additional costs may apply.

![](/img/sop-website-support/posting-blogs-broadly.png)

---

## Google Workspace Set Up

### Setting up Google Workspace

1. In products, confirm **Google Workspace** is ordered under that AGID.
2. Click the kebab (⋮) inline with Google Workspace, then **Launch**. A new window opens with the **Users** tab.
3. If no users are added, check the request received for the following emails to set up.

### Setting up Users in Google Workspace

- Select the **Business Center User** if a specified user is selected.
- Enter **first and last name** as per the partner/client.
- Enter **email address** without the domain.
- Enter a **recovery email address** (for password recovery; use an email **not** on the Google Workspace domain).
- Send **reset password email** to the Business Center user.

### Verify domain and DNS

- **Verify domain** using a **TXT** record added to the domain.
- **MX record** for Google Workspace to send/receive email:
  - **Type:** MX | **Host:** @ | **Value:** SMTP.GOOGLE.COM
- **TXT (SPF):**  
  - **Type:** TXT | **Host:** @ | **Value:** `v=spf1 include:_spf.google.com`

To migrate data from one Google Workspace to another, activate **Google Workspace Transfer** and follow the steps per the product.

### Configuring settings

- **Single Sign-On (SSO):** When active, allows Google Workspace users to access the product via Business App.

---

## Inbox Pro Enablement

*This product is fulfilled by the Automations team; Websites may need to provide support with this process from time to time.*

### Setting up the Web Chat (Business App flow)

1. Ensure you have access to the backend of the site (credentials from the SMB or via Website Pro). **Website Pro is NOT required** to add the Web Chat. If you do not have access, reach out to Client Engagement and do not proceed until access is received. Add notes in the VTM project each time you reach out.
2. Navigate to [Partner Center](https://partners.vendasta.com/dashboard) and select the desired account.

   ![](/img/sop-website-support/image7.png)

3. Ensure **Inbox Pro** and **Inbox Pro Enablement** are active under Products.  
   **Products that do not require both:** Agency Website SKU (see full instructions in product), Amazon Sponsored Display Ads.
4. In the top bar, click **Open In** → **Business App**.

   ![](/img/sop-website-support/image9.png)

5. In the Business App, click **Settings** → **Inbox Settings**.

   ![](/img/sop-website-support/image2.png)

6. Scroll to **Web Chat** and click **Setup Web Chat**.
7. Enter the **Widget Name** (internal only; default is “Web Chat”).
8. In **AI Assistant**, ensure **Business Profile** is selected (most information is pulled from here; see Business Profile section below).
9. In **Add Knowledge**, click **Add New Knowledge** → **Website**. Enter the URL and business name; in **Mode** select **Follow Links** so all pages are crawled. Click **Next**.

   ![](/img/sop-website-support/image3.png)

10. After it finds all pages, in **Choose Applications** select the web chat you set up and click **Save**.

    ![](/img/sop-website-support/image4.png)

11. Enter the **Web Chat Greeting** (or leave blank for default). E.g. *“Welcome to Madison’s Electric. How can I help you today?”*
    ![](/img/sop-website-support/image6.png)

12. In **Appearance**, set colours to match the website branding; ensure text is readable (light on dark or dark on light).
13. Click **Next**. **Installation Settings:**
    - **Amazon Ads only:** Click **Google Tag Manager**, copy the JavaScript code provided, click Save. In the VTM project, paste the code into the document linked in the Project Description. Add GTM code to the site (head/body as specified). If GTM is not there, ask Client Engagement to reach out to the Ads team. Log into the site and paste the code; save.

      ![](/img/sop-website-support/image10.png)

    - **Inbox Pro Enablement or Website SKU:** Click **Website**, copy the JavaScript code provided, click Save. Log into the backend and paste the code in the **head of all pages** (instructions vary by platform). Save.

      ![](/img/sop-website-support/image1.png)

### Business Profile information

In the Business App: **My Business** → **Business Profile** (can also be edited in Partner Center). Ensure at least:

- **Primary Info:** Business Name, Primary Category, Phone Number, Address and/or Service Area, Services Offered, Hours of Operation.
- **Descriptions:** Short Description, Long Description (use **Suggest Description** or pull from their website if needed).
- **Social:** Any business pages as necessary.

Save any changes. If anything above is missing, flag this with Client Engagement so the partner can fill it out.

---

### Setting up Inbox Pro in Partner Center

1. Ensure you have access to the backend of the site (from the partner or Website Pro). If not, reach out to Client Engagement and add notes in the VTM project each time.
2. Go to [Partner Center](https://partners.vendasta.com/dashboard) and select the desired account.
3. In the top bar, click the **Inbox** icon.

   ![](/img/sop-website-support/inbox-partner-center-inbox-icon.png)

4. Click the **Settings** icon.
5. Scroll to **Web Chat** → **Setup Web Chat**.
6. Enter **Widget Name** (internal only; default “Web Chat”).
7. In **AI Assistant**, ensure **Business Profile** is selected. In **Add Knowledge** → **Add New Knowledge** → **Website**. Enter URL and business name; **Mode** = **Follow Links**. Click **Next**. After pages are found, in **Choose Applications** select the web chat → **Save**.  
   If the website is already added as a knowledge area, ensure **Mode** is **Follow Links** and refresh the data.

   ![](/img/sop-website-support/image3.png)

   ![](/img/sop-website-support/image4.png)

8. Enter **Web Chat Greeting** (or leave default). Set **Appearance** (colours, readability). Click **Next**.

   ![](/img/sop-website-support/image6.png)

9. **Installation:** For Amazon Ads use **Google Tag Manager** and copy the Javascript code provided; follow the same GTM steps as above; refer to the document on implementing GTM for different platforms. For Inbox Pro Enablement or Website SKU, use **Website**, copy the Javascript code provided, and paste in the **head of all pages** on the site. Save.

   ![](/img/sop-website-support/image10.png)

   ![](/img/sop-website-support/image1.png)

10. Complete **Business Profile** as in the previous section (Primary Info, Descriptions, Social). Save. Flag any missing info to Client Engagement.

### Next steps

- Refer to the [**Ways to upload the GTM/chat widget codes for different platforms**](https://docs.google.com/document/d/1r6beRnGEWIDAKZc4NTz7emljUiSHQRo1oR0oh_FnFik/edit?tab=t.0#heading=h.bllyran0q013) document for implementation details.

---

**Contacts**

- **Listings support (GMB access):** [listings@yourdigitalagents.com](mailto:listings@yourdigitalagents.com) (Michelle for team access)
- **Bing / website analytics:** [websiteanalytics@localmarketpage.com](mailto:websiteanalytics@localmarketpage.com)
