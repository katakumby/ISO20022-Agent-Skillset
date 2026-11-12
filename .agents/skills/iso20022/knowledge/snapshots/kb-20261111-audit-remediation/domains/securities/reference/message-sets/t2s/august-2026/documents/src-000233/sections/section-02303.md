---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.21 Person Identification", "82.1.21.1 Contact14", "82.1.21.1.14 ValidFrom <VldFr>"]
file_pages: [3084]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.21.1.14 ValidFrom <VldFr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3084 to 3084.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3084

```text
82.1.21.1.14  ValidFrom <VldFr>
Presence: [0..1]
Definition: Starting validity date for the contact.
Datatype: "ISODate" on page 3319
82.1.21.1.15  ValidTo <VldTo>
Presence: [0..1]
Definition: Ending validity date for the contact.
Datatype: "ISODate" on page 3319
82.1.21.2  Contact13
Definition: Specifies the details of the contact person.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 3084
   Name <Nm> [0..1] Text 3085
   PhoneNumber <PhneNb> [0..1] Text 3085
   MobileNumber <MobNb> [0..1] Text 3085
   FaxNumber <FaxNb> [0..1] Text 3085
   URLAddress <URLAdr> [0..1] Text 3085
   EmailAddress <EmailAdr> [0..1] Text 3085
   EmailPurpose <EmailPurp> [0..1] Text 3085
   JobTitle <JobTitl> [0..1] Text 3086
   Responsibility <Rspnsblty> [0..1] Text 3086
   Department <Dept> [0..1] Text 3086
   Other <Othr> [0..*]  3086
     ChannelType <ChanlTp> [1..1] Text 3086
     Identification <Id> [0..1] Text 3086
   PreferredMethod <PrefrdMtd> [0..1] CodeSet 3086
82.1.21.2.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 3265
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MADM Madam Title of the person is Madam.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3084 August 2026
```

