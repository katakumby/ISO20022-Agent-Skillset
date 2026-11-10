---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.6 Identification Information", "7.1.6.1 GenericIdentification13", "7.1.6.1.1 Identification <Id>"]
file_pages: [145]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.6.1.1 Identification <Id>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 145 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 145

```text
7.1.6.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max4AlphaNumericText" on page 184
7.1.6.1.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 183
7.1.6.1.3  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 183
7.1.6.2  MessageIdentification1
Definition: Identifies a message by a unique identifier and the date and time when the message was
created by the sender.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 145
   CreationDateTime <CreDtTm> [1..1] DateTime 145
7.1.6.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the message.
Datatype: "Max35Text" on page 183
7.1.6.2.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date of creation of the message.
Datatype: "ISODateTime" on page 180
7.1.6.3  GenericIdentification1
Definition: Information related to an identification, for example party identification or account
identification.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 145 August 2026
```

