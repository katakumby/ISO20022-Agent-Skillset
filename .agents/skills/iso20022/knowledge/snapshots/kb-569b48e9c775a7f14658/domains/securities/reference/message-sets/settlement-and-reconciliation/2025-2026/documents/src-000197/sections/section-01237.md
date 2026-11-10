---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.22 PartyIdentificationAndAccount224", "35.1.18.22.4 CashAccount <CshAcct>"]
file_pages: [1694]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.22.4 CashAccount <CshAcct>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1694 to 1694.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1694

```text
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 1691 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1691
   Country <Ctry> [1..1] CodeSet C7 1691
   AlternateIdentification <AltrnId> [1..1] Text 1691
35.1.18.22.4  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
CashAccount <CshAcct> contains one of the following elements (see
"CashAccountIdentification9Choice" on page 1342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C21 1342
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 1343
Or}   Proprietary <Prtry> [1..1] Text 1343
35.1.18.22.5  ChargesAccount <ChrgsAcct>
Presence: [0..1]
Definition: Account to be used for charges/fees if different from the account for payment.
ChargesAccount <ChrgsAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 1343 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C21 1343
Or}   Proprietary <Prtry> [1..1] Text 1344
35.1.18.22.6  CommissionAccount <ComssnAcct>
Presence: [0..1]
Definition: Account to be used for commission if different from the account for payment.
CommissionAccount <ComssnAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 1343 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C21 1343
Or}   Proprietary <Prtry> [1..1] Text 1344
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1694 March 2026
```

