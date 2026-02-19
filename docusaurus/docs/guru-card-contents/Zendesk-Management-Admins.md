---
title: Zendesk Management Admins
sidebar_label: Zendesk Management Admins
---

# Zendesk Management Admins

## Table of Contents

- [MS | Zendesk White Label Email Integration/Setup Process](#ms-zendesk-white-label-email-integrationsetup-process)
- [Client Engagement Process](#client-engagement-process)
- [Receiving the Information](#receiving-the-information)
- [Completing the Email Integration](#completing-the-email-integration)
- [#1: Configuring the Email in Zendesk Admin Center](#1-configuring-the-email-in-zendesk-admin-center)
- [#2: Enabling Email Forwarding](#2-enabling-email-forwarding)
- [Gmail](#gmail)
- [Outlook (Microsoft)](#outlook-microsoft)
- [#3: Domain Registrar Settings](#3-domain-registrar-settings)
- [GoDaddy](#godaddy)
- [WIX](#wix)
- [#4A: Verifying Forwarding Success](#4a-verifying-forwarding-success)
- [GODADDY — ADDITIONAL STEPS TO ENABLE FORWARDING](#godaddy-additional-steps-to-enable-forwarding)
- [TROUBLESHOOTING FAILED FORWARDING](#troubleshooting-failed-forwarding)
- [#4B: Verifying DNS & SPF Setting Success](#4b-verifying-dns-spf-setting-success)
- [TROUBLESHOOTING FAILED SPF RECORDS](#troubleshooting-failed-spf-records)
- [TROUBLESHOOTING FAILED DNS RECORDS](#troubleshooting-failed-dns-records)

---

## MS | Zendesk White_Label Email Integration/Setup Process

Marketing Services is offering the ability for partners to integrate a custom white_label email
address with Marketing Services' Zendesk, for communications between MS and the partners
/clients.

This addition is one of the benefits of using Marketing Services and doesn't require any
activations or additional charges. This is available to all partners, regardless of subscription
tier (even
 partners.)
Free

This free offering is
 to partners as they
 follow our strict instructions for access
optional
must
to ensure this process is efficient and hassle_free.
If they do not want to provide us with their
domain & email login credentials, we will default to using
marketingservices@yourdigitalagents.com for communications.

Required from the partner:

• Name of email provider (Gmail, Outlook, etc.)

• Email address

• Password

• Domain registrar (GoDaddy, Google Domains, etc.)

• Domain username:

• Domain password

• OR they can provide us
 if their registrar is
delegate access
GoDaddy or Google

Domains. Delegate access to websites@yourdigitalagents.com

Here
 is the partner_facing resource to refer Partners to if they want to set up their white_
labeled email with Marketing Services.

## Client Engagement Process

## Receiving the Information

1. When a new response is added to this
 (by Partners or the Vendasta sales
Google form

rep), we will receive a new Zendesk ticket to da_incoming@vendasta.com with the

subject line "
"
The Marketing Services White_label form has a new response!

    a. Client Engagement team members should
 to one of the
assign these tickets

following team members so they can process them:

    i. Jordan Hall, Sayda M or Aesha Zala (Agency)

    ii. Craig M or Jason G (High Velocity)

2. The assigned team member will
 information via the
review the submission

spreadsheet.

    a. Ensure that all fields are filled out for the required login credentials.

    b. Any info that says "will provide later" or "don't want to provide" will require us to

follow_up with the partner to get those credentials and communicate that

without these, we will default to using the unbranded email.

3. Follow the steps below to integrate the email.

    a. Once the email has been integrated, highlight the row green in the Google form

to show that it has been completed.

## Completing the Email Integration
Follow the steps below to:

1. Add the email to the backend of Zendesk

2. Enable email forwarding

3. Configure the DNS records

4. Test integration success by verifying that forwarding & DNS record checks come back

successful.

You will need to follow the steps below based on their email and domain providers. If you
encounter an account different than one of the ones listed below, please document the steps
in this Guru card.

## #1: Configuring the Email in Zendesk Admin Center
1. Open up the Zendesk Admin Center (accessible by Zendesk Admins only.)

![](/img/guru/Zendesk-Management-Admins/01.png)

2. On the left side, type "email" into the search bar, and click the "
" page from
Email

Channels &gt; Talk and email:

![](/img/guru/Zendesk-Management-Admins/02.png)

3. On the Email page, click "
" &gt; "
"
Add address
Connect other

![](/img/guru/Zendesk-Management-Admins/03.png)

    a. Type in the white_label email address into the box, and select "Yes, I have

"
forwarded this address to support@vendasta.zendesk.com

![](/img/guru/Zendesk-Management-Admins/04.png)

    b. Even if it says that forwarding is unsuccessful, just close out of the error window.

The email will still be added to the panel, where you can retry the forwarding

check.

You will only need to do this step once. After you've added the email here, you can find it later
by navigating to this Email page and using
 or
 to look up the address.
ctrl + f
cmd + f

## #2: Enabling Email Forwarding

## Gmail
1. In a new Chrome browser/profile, log into the Gmail account with the provided

username and password.

2. Click on the settings
 in the top right of the Gmail inbox, then "
Gear icon
See all

"
settings

![](/img/guru/Zendesk-Management-Admins/05.png)

3. On the Settings page, click on the "
" tab:
Forwarding and POP/IMAP

![](/img/guru/Zendesk-Management-Admins/06.png)

4. Click "
" and in the pop_up window, add the email:
Add a forwarding address

support@vendasta.zendesk.com

![](/img/guru/Zendesk-Management-Admins/07.png)

5. On the following pop_ups, click "
" then "
"
Proceed
OK

6. A verification link will be sent to Zendesk. This email will show in the Suspended

Tickets view (viewable by Zendesk Admins only.)

![](/img/guru/Zendesk-Management-Admins/08.png)

    a. Open up the Suspended Tickets view and click on the "
" heading twice
Received

to change the sort order to newest_first:

![](/img/guru/Zendesk-Management-Admins/09.png)

7. Locate the email. It should look something like this:

![](/img/guru/Zendesk-Management-Admins/10.png)

    a.  Copy the URL near the top of the email message. Paste this into a new tab.

Follow the prompt(s) on the page to verify forwarding.

![](/img/guru/Zendesk-Management-Admins/11.png)

8. Go back into the Gmail inbox settings to the "
tab.
Forwarding and POP/IMAP"

    a. In the "Forwarding" settings, select the second option "Forward a copy of

" support@vendasta.zendesk.com and "
incoming mail to
keep Gmail's copy in the

."
Inbox

![](/img/guru/Zendesk-Management-Admins/12.png)

9. Click "
" at the bottom of the settings page.
Save Changes

## Outlook (Microsoft)
1. In a new Chrome browser/profile, log into the Outlook email account with the

provided username and password.

2. At the top of the page, select the "
"
.
Settings gear icon

![](/img/guru/Zendesk-Management-Admins/13.png)

3. Within the Settings panel, click on
 &gt;
Mail
Forwarding

![](/img/guru/Zendesk-Management-Admins/14.png)

4. a. Select
, enter the forwarding address
Enable forwarding
support@vendasta.

zendesk.com.

    b. Select "
."
Keep a copy of forwarded messages

    c. Click "Save."

The majority of the time, Outlook emails will require an additional forwarding permission
enabled within the domain registrar before the forwarding will register successfully.

AND/OR

You may need to go to
 (while logged into the Outlook
https://security.microsoft.com/antispam
account) and under the Anti_Spam Outbound Policy, you'll need to
.
Enable Forwarding

The above is because Microsoft—by default— disables all email forwarding for Microsoft
accounts.

## #3: Domain Registrar Settings

## GoDaddy
1. Sign into the associated
 account. If you have delegate access, sign in using

the
 account (password can be located within the
websites@yourdigitalagents.com

Webslingers Lifeline.)

    a. If you are signing in via the Partner's account, skip to STEP 5

2. Once logged in, click on "
" &gt; "
" in the top left.
My Account
Domains

![](/img/guru/Zendesk-Management-Admins/15.png)

3. On the left side panel, click on "Settings" then "Delegate Access" from the drop_down.

![](/img/guru/Zendesk-Management-Admins/16.png)

4. Locate the account from within the "Accounts I can access" column on the left. The

account will appear under the name the partner has put on their GoDaddy account.

(You cannot search by domain name.)

    a. Once you have located the account, click "
"
Access Now

![](/img/guru/Zendesk-Management-Admins/17.png)

5. Once in the delegate account, find the domain associated with the white_label email

address within the domain list.

    a. Click "
" to open up the DNS settings.
DNS

![](/img/guru/Zendesk-Management-Admins/18.png)

6. By clicking the "
" button each time, create the following NEW unique
Add New Record

records:

![](/img/guru/Zendesk-Management-Admins/19.png)

![](/img/guru/Zendesk-Management-Admins/20.png)

    a. i.

zendesk1

1. mail1.zendesk.com

    ii. zendesk2

1. mail2.zendesk.com

    iii. zendesk3

1. mail3.zendesk.com

    iv. zendesk4

1. mail4.zendesk.com

7. One of the records will have a custom value unique to any emails belonging to that

domain. To obtain the custom value, follow steps for Configuring the Email in

Zendesk Admin Center (above) to open up the email in the Admin Dashboard.

    a. Click on "
" for the DNS records
See details

    i. The value in the box next to "Set to" will be your unique value:

![](/img/guru/Zendesk-Management-Admins/21.png)

8. In the GoDaddy DNS settings, add a NEW record with the following:

    a. zendeskverification

![](/img/guru/Zendesk-Management-Admins/22.png)

9. The last record you will need to add is an SPF record. Within the DNS records, there

cannot be more than 1 SPF record. Most domains will already have an SPF record, so

you will need to add our value to the existing one.

Example:

![](/img/guru/Zendesk-Management-Admins/23.png)

You don't need to worry about other TXT records with "@" as the name. ONLY ones

where the "Data" has "v=spf1" in there.

Ie. You can disregard these:

![](/img/guru/Zendesk-Management-Admins/24.png)

    a. If they do not have an existing SPF record, you need to create a new one:

v=spf1 include:mail.zendesk.com ~all

Please note: there is a space on either side of include:mail.zendesk.com

![](/img/guru/Zendesk-Management-Admins/25.png)

    b. If they already have an existing SPF record, you need to merge the values by

inputting
 into the existing record.
include:mail.zendesk.com

    i. Example of original:

![](/img/guru/Zendesk-Management-Admins/26.png)

After merging:

![](/img/guru/Zendesk-Management-Admins/27.png)

When merging, you'll need to put a space before

include:mail.zendesk.com

to separate our value from the others.

## WIX
Locate the Domains options under Billing & Subscriptions on the left.

![](/img/guru/Zendesk-Management-Admins/28.png)

![](/img/guru/Zendesk-Management-Admins/29.png)

1. Update the CNAME Records as per the table below.

![](/img/guru/Zendesk-Management-Admins/30.png)

![](/img/guru/Zendesk-Management-Admins/31.png)

2. Update the TXT records are per the table.

![](/img/guru/Zendesk-Management-Admins/32.png)

For the
record, if they already have an existing record, we
v=spf1 include:mail.zendesk.com ?all
will need to merge both of them. For example, the existing record was

v=spf1 include:sendersrv.com include:_spf.google.com include:sendgrid.net ~all so we will add
ours before ~all.

Merged record: v=spf1 include:sendersrv.com include:_spf.google.com include:sendgrid.net
include:mail.zendesk.com
~all

3. Save the changes, go to the Admin Center in Zendesk, and verify the SPF and DNS

records.

DNS Settings:

Type
Name
Data
TTL

CNAME Record
zendesk1
mail1.zendesk.com
Automatic/default

CNAME Record
zendesk2
mail2.zendesk.com
Automatic/default

CNAME Record
zendesk3
mail3.zendesk.com
Automatic/default

CNAME Record
zendesk4
mail4.zendesk.com
Automatic/default

TXT Record
zendeskverification
[custom value]
Automatic/default

TXT Record
@
v=spf1 include:mail.zendesk.
com ?all

Automatic/default

NAMECHEAP

Type
Host
Value
TTL

CNAME Record
zendesk1
mail1.zendesk.com
Automatic/default

CNAME Record
zendesk2
mail2.zendesk.com
Automatic/default

CNAME Record
zendesk3
mail3.zendesk.com
Automatic/default

CNAME Record
zendesk4
mail4.zendesk.com
Automatic/default

TXT Record
zendeskverification
[custom value]
Automatic/default

TXT Record
@
v=spf1 include:mail.zendesk.
com ?all

Automatic/default

Type
Host
Value
TTL

CNAME Record
zendesk1
mail1.zendesk.com
Automatic/default

CNAME Record
zendesk2
mail2.zendesk.com
Automatic/default

CNAME Record
zendesk3
mail3.zendesk.com
Automatic/default

CNAME Record
zendesk4
mail4.zendesk.com
Automatic/default

TXT Record
zendeskverification
[custom value]
Automatic/default

TXT Record
leave blank
v=spf1 include:mail.zendesk.
com ?all

Automatic/default

GOOGLE DOMAINS

Host name
Type
TTL
Data

zendesk1
CNAME
Automatic
/default

mail1.zendesk.com

zendesk2
CNAME
Automatic
/default

mail2.zendesk.com

zendesk3
CNAME
Automatic
/default

mail3.zendesk.com

zendesk4
CNAME
Automatic
/default

mail4.zendesk.com

zendeskverification
TXT
Automatic
/default

[custom value]

@
TXT
Automatic
/default

v=spf1 include:mail.zendesk.
com ?all

IONOS

Type
Host Name
Value (Points to)
Service
TTL

CNAME Record
zendesk1
mail1.zendesk.com
_
1 hour

CNAME Record
zendesk2
mail2.zendesk.com
_
1 hour

CNAME Record
zendesk3
mail3.zendesk.com
_
1 hour

CNAME Record
zendesk4
mail4.zendesk.com
_
1 hour

TXT Record
zendeskverification
[custom value]
_
1 hour

TXT Record
@
v=spf1 include:mail.
zendesk.com ?all

_
1 hour

Type
Host Name
Value
TTL

CNAME Record
zendesk1
mail1.zendesk.com
1 hour

CNAME Record
zendesk2
mail2.zendesk.com
1 hour

CNAME Record
zendesk3
mail3.zendesk.com
1 hour

CNAME Record
zendesk4
mail4.zendesk.com
1 hour

TXT Record
zendeskverification
[custom value]
1 hour

TXT Record
@
v=spf1 include:mail.zendesk.
com ?all

1 hour

CLOUDFLARE

Type
Name
Content
Proxy Status*
TTL

CNAME
zendesk1
mail1.zendesk.com
Toggle
OFF
Auto

CNAME
zendesk2
mail2.zendesk.com
Toggle
OFF
Auto

CNAME
zendesk3
mail3.zendesk.com
Toggle
OFF
Auto

CNAME
zendesk4
mail4.zendesk.com
Toggle
OFF
Auto

TXT
zendeskverification
[custom value]
Toggle
OFF
Auto

TXT
[domain name]
v=spf1 include:
mail.zendesk.com
_all

Toggle
OFF
Auto

*For the Proxy Status, you do NOT want this to be Proxied because we have issues with SSL
generations (this is more of an issue for DNS settings for sites being hosted with Website Pro,
but a good idea to toggle it off when we're integrating Zendesk just to avoid any other issues.
If the Proxy is on, it also won't show the real IP address.

## #4A: Verifying Forwarding Success
1. If only the forwarding is set up, it should have a green checkmark next to Forwarding:

![](/img/guru/Zendesk-Management-Admins/33.png)

    a. If the Forwarding is failing, recheck the above Gmail settings. To retry, you can

click on "See details" and "Verify forwarding."

![](/img/guru/Zendesk-Management-Admins/34.png)

    b. As Zendesk checks the forwarding, it will turn the status to a yellow exclamation

triangle. You will need to repeatedly refresh the page until you see either it is

successful (green checkmark) or failed (red exclamation.) It usually takes a

couple to a few minutes.

2. Depending on the combination of email provider and domain provider, there
 be
may

additional forwarding permissions you need to enable within the domain registrar. If

enabling forwarding in Gmail isn't sufficient enough, follow the below steps.

## GODADDY — ADDITIONAL STEPS TO ENABLE FORWARDING
If the forwarding is still failing after you've enabled it within the email inbox, you may also
need to follow the below steps within GoDaddy:

1. On the page after you sign in, scroll down. Beneath "All Products and Services" click "

" in the "Email & Office" section:
Manage All

![](/img/guru/Zendesk-Management-Admins/35.png)

![](/img/guru/Zendesk-Management-Admins/36.png)

2. On the Email & Office page, click on "
" &gt; "
"
Admin
Email Forwarding

![](/img/guru/Zendesk-Management-Admins/37.png)

3. Click on the black "Forwarding Status" button in the "Email Forwarding Overview"

section. Ensure it is enabled.

![](/img/guru/Zendesk-Management-Admins/38.png)

![](/img/guru/Zendesk-Management-Admins/39.png)

4. Within the "Email Forwarding for [Domain name]" section, click "
" and
Add Forwarding

add forwarding to our Zendesk.

    a. User = white_label email address

    b. Forwards to = support@vendasta.zendesk.com

![](/img/guru/Zendesk-Management-Admins/40.png)

## TROUBLESHOOTING FAILED FORWARDING
Check for additional forwarding permissions within the domain registrar (like we did above for
GoDaddy.)

## #4B: Verifying DNS & SPF Setting Success
1. Open up the email in the Zendesk Admin Center (refer to Configuring the Email in

Zendesk Admin Center steps above.)

2. Click on "
" next to SPF and DNS records, and click the corresponding blue
See details

verification buttons:

![](/img/guru/Zendesk-Management-Admins/41.png)

3. When successful, there should be green checkmarks next to both:

![](/img/guru/Zendesk-Management-Admins/42.png)

## TROUBLESHOOTING FAILED SPF RECORDS
• Try clicking the blue "Verify SPF Record" button again. Sometimes, it takes a few

moments to update.

These settings can be
 finicky. Check/test out the following:
very

• Is our value
the last one in the merged record, before "~all"?
include:mail.zendesk.com

Usually, it only works if it's the last value. Otherwise, you can try moving it to the

beginning after "v=spf1"

• Instead of "
", it may work if you change it to "
" or "
"
~all
?all
_all

• Rarely, removing the spaces in the SPF record works. You can try it out.

Be sure that if anything doesn't work, you revert the changes back to our recommended
setup. As we are adjusting an existing SPF value with other values in it, it's the one record that

impact other areas for the Partner with their domain, so you need to be careful.
could

## TROUBLESHOOTING FAILED DNS RECORDS
• Double check that all the DNS settings are accurate.

• Double check that the email address you put into the Zendesk Admin Center doesn't

contain a typo. A single letter could affect the custom TXT record it generates.
