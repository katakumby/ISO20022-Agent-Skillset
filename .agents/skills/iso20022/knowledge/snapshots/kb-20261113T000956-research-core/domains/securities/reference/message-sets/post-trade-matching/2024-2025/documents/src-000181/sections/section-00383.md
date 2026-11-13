---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.20 CashParties33", "7.1.20.20.1 Debtor <Dbtr>"]
file_pages: [449]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.20.1 Debtor <Dbtr>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 449 to 449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 449

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalInformation <AddtlInf> [0..1] ± C4 460
   Intermediary <Intrmy> [0..1]  461
     Identification <Id> [1..1] ± 461
     AlternateIdentification <AltrnId> [0..1] ± 462
     CashAccount <CshAcct> [0..1] ± 462
     ChargesAccount <ChrgsAcct> [0..1] ± 463
     CommissionAccount <ComssnAcct> [0..1] ± 463
     TaxAccount <TaxAcct> [0..1] ± 463
     AdditionalInformation <AddtlInf> [0..1] ± C4 463
7.1.20.20.1  Debtor <Dbtr>
Presence: [0..1]
Definition: Party that owes an amount of money to the (ultimate) creditor.
Debtor <Dbtr> contains the following PartyIdentificationAndAccount148 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 449
   AlternateIdentification <AltrnId> [0..1] ± 450
   CashAccount <CshAcct> [0..1] ± 450
   ChargesAccount <ChrgsAcct> [0..1] ± 451
   CommissionAccount <ComssnAcct> [0..1] ± 451
   TaxAccount <TaxAcct> [0..1] ± 451
   AdditionalInformation <AddtlInf> [0..1] ± C4 451
7.1.20.20.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 449 February 2025
```

