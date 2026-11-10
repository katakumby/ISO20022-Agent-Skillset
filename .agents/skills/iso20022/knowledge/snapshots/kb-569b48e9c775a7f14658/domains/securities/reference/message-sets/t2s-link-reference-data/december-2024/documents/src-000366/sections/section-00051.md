---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types"]
file_pages: [55]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8 Message Items Types

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 55 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 55

```text
8 Message Items Types
8.1 MessageComponents
8.1.1 Account
8.1.1.1  CashAccount38
Definition: Provides the details to identify an account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 55
   Type <Tp> [0..1] ± 55
   Currency <Ccy> [0..1] CodeSet C1 55
   Name <Nm> [0..1] Text 56
   Proxy <Prxy> [0..1] ± 56
8.1.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following elements (see "AccountIdentification4Choice" on
page 59 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 60
Or}   Other <Othr> [1..1] ± 60
8.1.1.1.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the nature, or use of the account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 57 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 57
Or}   Proprietary <Prtry> [1..1] Text 58
8.1.1.1.3  Currency <Ccy>
Presence: [0..1]
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 55 December 2024
```

