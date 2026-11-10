---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.13 Person Identification"]
file_pages: [832]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.13 Person Identification

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 832 to 832.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 832

```text
ContactDetails <CtctDtls> contains the following elements (see "Contact13" on page 832 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 833
   Name <Nm> [0..1] Text 833
   PhoneNumber <PhneNb> [0..1] Text 833
   MobileNumber <MobNb> [0..1] Text 834
   FaxNumber <FaxNb> [0..1] Text 834
   URLAddress <URLAdr> [0..1] Text 834
   EmailAddress <EmailAdr> [0..1] Text 834
   EmailPurpose <EmailPurp> [0..1] Text 834
   JobTitle <JobTitl> [0..1] Text 834
   Responsibility <Rspnsblty> [0..1] Text 834
   Department <Dept> [0..1] Text 834
   Other <Othr> [0..*]  835
     ChannelType <ChanlTp> [1..1] Text 835
     Identification <Id> [0..1] Text 835
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 835
37.1.13 Person Identification
37.1.13.1  Contact13
Definition: Specifies the details of the contact person.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 832 February 2025
```

