---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.1 Account", "6.1.1.3 CashAccountType2Choice"]
file_pages: [530]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.1.3 CashAccountType2Choice

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 530 to 530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 530

```text
Definition: Identification used to indicate the account identification under another specified name.
Datatype: "Max2048Text" on page 608
6.1.1.3  CashAccountType2Choice
Definition: Nature or use of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 530
Or}   Proprietary <Prtry> [1..1] Text 530
6.1.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Account type, in a coded form.
Datatype: "ExternalCashAccountType1Code" on page 591
6.1.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Nature or use of the account in a proprietary form.
Datatype: "Max35Text" on page 609
6.1.1.4  GenericAccountIdentification1
Definition: Information related to a generic account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 530
   SchemeName <SchmeNm> [0..1]  530
{Or     Code <Cd> [1..1] CodeSet 531
Or}     Proprietary <Prtry> [1..1] Text 531
   Issuer <Issr> [0..1] Text 531
6.1.1.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max34Text" on page 609
6.1.1.4.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 530 March 2026
```

