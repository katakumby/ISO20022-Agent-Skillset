---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.16 QuantityAndAccount118", "35.1.21.16.2 AccountOwner <AcctOwnr>"]
file_pages: [1743]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.16.2 AccountOwner <AcctOwnr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1743 to 1743.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1743

```text
Datatype: "Max210Text" on page 2191
35.1.21.16.2  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
35.1.21.16.3  CashAccount <CshAcct>
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
35.1.21.16.4  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C33 "SafekeepingPlaceFormatOrLEIRule"
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace5" on
page 1749 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 1749
   LEI <LEI> [0..1] IdentifierSet 1750
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1743 March 2026
```

