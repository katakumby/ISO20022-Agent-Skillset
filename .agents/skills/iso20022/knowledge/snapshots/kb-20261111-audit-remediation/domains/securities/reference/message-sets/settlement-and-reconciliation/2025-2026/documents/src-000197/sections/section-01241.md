---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.24 CashParties41"]
file_pages: [1698]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.24 CashParties41

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1698 to 1698.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1698

```text
Constraints
• AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if DeclarationlDetails and/or
PartyContactDetails are present, then they must not contain information that can be provided in a
structured field.
35.1.18.24  CashParties41
Definition: Payment processes required to transfer cash from the debtor to the creditor.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Debtor <Dbtr> [0..1] ± 1698
   DebtorAgent <DbtrAgt> [0..1] ± 1698
   Creditor <Cdtr> [0..1] ± 1699
   CreditorAgent <CdtrAgt> [0..1] ± 1699
   Intermediary <Intrmy> [0..1] ± 1700
35.1.18.24.1  Debtor <Dbtr>
Presence: [0..1]
Definition: Party that owes an amount of money to the (ultimate) creditor.
Debtor <Dbtr> contains the following elements (see "PartyIdentificationAndAccount223" on page 1695
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1696
   LEI <LEI> [0..1] IdentifierSet 1696
   AlternateIdentification <AltrnId> [0..1] ± 1696
   CashAccount <CshAcct> [0..1] ± 1696
   ChargesAccount <ChrgsAcct> [0..1] ± 1696
   CommissionAccount <ComssnAcct> [0..1] ± 1697
   TaxAccount <TaxAcct> [0..1] ± 1697
   AdditionalInformation <AddtlInf> [0..1] ± C5 1697
35.1.18.24.2  DebtorAgent <DbtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the debtor.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1698 March 2026
```

