---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.13 Person Identification", "37.1.13.1 Contact13", "37.1.13.1.1 NamePrefix <NmPrfx>"]
file_pages: [833]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.13.1.1 NamePrefix <NmPrfx>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 833 to 833.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 833

```text
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
37.1.13.1.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 861
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
MISS Miss Title of the person is Miss.
MIST Mister Title of the person is Mister or Mr.
MIKS GenderNeutral Title of the person is gender neutral
(Mx).
37.1.13.1.2  Name <Nm>
Presence: [0..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max140Text" on page 888
37.1.13.1.3  PhoneNumber <PhneNb>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 833 February 2025
```

