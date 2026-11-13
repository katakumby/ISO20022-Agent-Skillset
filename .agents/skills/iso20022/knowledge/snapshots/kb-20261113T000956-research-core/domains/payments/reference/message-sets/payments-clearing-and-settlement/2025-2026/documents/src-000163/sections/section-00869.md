---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.1 Account", "10.1.1.3 CashAccountType2Choice"]
file_pages: [1164]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.1.3 CashAccountType2Choice

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1164 to 1164.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1164

```text
Definition: Identification used to indicate the account identification under another specified name.
Datatype: "Max2048Text" on page 1245
10.1.1.3  CashAccountType2Choice
Definition: Nature or use of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1164
Or}   Proprietary <Prtry> [1..1] Text 1164
10.1.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Account type, in a coded form.
Datatype: "ExternalCashAccountType1Code" on page 1227
10.1.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Nature or use of the account in a proprietary form.
Datatype: "Max35Text" on page 1246
10.1.1.4  GenericAccountIdentification1
Definition: Information related to a generic account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1164
   SchemeName <SchmeNm> [0..1]  1164
{Or     Code <Cd> [1..1] CodeSet 1165
Or}     Proprietary <Prtry> [1..1] Text 1165
   Issuer <Issr> [0..1] Text 1165
10.1.1.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max34Text" on page 1245
10.1.1.4.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1164 March 2026
```

