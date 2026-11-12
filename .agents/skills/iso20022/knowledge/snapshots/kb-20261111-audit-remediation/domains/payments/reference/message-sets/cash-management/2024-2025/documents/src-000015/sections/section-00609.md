---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.1 Account", "37.1.1.3 CashAccountType2Choice"]
file_pages: [786]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.1.3 CashAccountType2Choice

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 786 to 786.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 786

```text
Definition: Identification used to indicate the account identification under another specified name.
Datatype: "Max2048Text" on page 888
37.1.1.3  CashAccountType2Choice
Definition: Nature or use of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 786
Or}   Proprietary <Prtry> [1..1] Text 786
37.1.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Account type, in a coded form.
Datatype: "ExternalCashAccountType1Code" on page 853
37.1.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Nature or use of the account in a proprietary form.
Datatype: "Max35Text" on page 889
37.1.1.4  GenericAccountIdentification1
Definition: Information related to a generic account identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 786
   SchemeName <SchmeNm> [0..1]  786
{Or     Code <Cd> [1..1] CodeSet 787
Or}     Proprietary <Prtry> [1..1] Text 787
   Issuer <Issr> [0..1] Text 787
37.1.1.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max34Text" on page 889
37.1.1.4.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 786 February 2025
```

