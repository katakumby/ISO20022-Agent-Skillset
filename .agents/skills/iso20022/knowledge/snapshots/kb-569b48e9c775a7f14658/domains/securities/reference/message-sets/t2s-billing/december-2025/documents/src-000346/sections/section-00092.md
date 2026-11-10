---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.5 Identification Information", "4.1.5.2 GenericIdentification36", "4.1.5.2.2 Issuer <Issr>"]
file_pages: [118]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.5.2.2 Issuer <Issr>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 118 to 118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 118

```text
4.1.5.2.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 153
4.1.5.2.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 153
4.1.5.3  GenericIdentification1
Definition: Information related to an identification, for example party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 118
   SchemeName <SchmeNm> [0..1] Text 118
   Issuer <Issr> [0..1] Text 118
4.1.5.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 153
4.1.5.3.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Datatype: "Max35Text" on page 153
4.1.5.3.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 153
4.1.6 Miscellaneous
4.1.6.1  MessageHeader9
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 118 December 2025
```

