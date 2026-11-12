---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.1 Account", "8.1.1.4 GenericAccountIdentification1", "8.1.1.4.3 Issuer <Issr>"]
file_pages: [59]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.1.4.3 Issuer <Issr>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 59 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 59

```text
Datatype: "Max35Text" on page 78
8.1.1.4.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 78
8.1.2 Account Identification
8.1.2.1  SecuritiesAccount19
Definition: Account to or from which a securities entry is made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 59
   Type <Tp> [0..1] ± 59
   Name <Nm> [0..1] Text 59
8.1.2.1.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max35Text" on page 78
8.1.2.1.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 63 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 63
   Issuer <Issr> [1..1] Text 63
   SchemeName <SchmeNm> [0..1] Text 63
8.1.2.1.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 79
8.1.2.2  AccountIdentification4Choice
Definition: Specifies the unique identification of an account as assigned by the account servicer.
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 59 December 2024
```

