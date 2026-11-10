---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.1 Account", "35.1.1.3 SecuritiesAccount36", "35.1.1.3.2 Type <Tp>"]
file_pages: [1342]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.1.3.2 Type <Tp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1342 to 1342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1342

```text
Datatype: "Max35Text" on page 2192
35.1.1.3.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.1.3.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 2192
35.1.1.3.4  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 2192
35.1.2 Account Identification
35.1.2.1  CashAccountIdentification9Choice
Definition: Unique identifier of an account, as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C21 1342
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1343
Or}   Proprietary <Prtry> [1..1] Text 1343
35.1.2.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1342 March 2026
```

