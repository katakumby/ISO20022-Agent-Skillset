---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.14 CashParties <CshPties>"]
file_pages: [119, 120]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.14 CashParties <CshPties>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 119 to 120.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 119

```text
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
Country code should be used for settlement taking place outside of an institution published in the
PSET's BIC list. This includes physical deliveries and investment funds not settling at a CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
3.4.14 CashParties <CshPties>
Presence: [0..1]
Definition: Cash parties involved in the specific transaction.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 119 February 2025
```

## File page 120

```text
CashParties <CshPties> contains the following elements (see "CashParties33" on page 447 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Debtor <Dbtr> [0..1]  449
     Identification <Id> [1..1] ± 449
     AlternateIdentification <AltrnId> [0..1] ± 450
     CashAccount <CshAcct> [0..1] ± 450
     ChargesAccount <ChrgsAcct> [0..1] ± 451
     CommissionAccount <ComssnAcct> [0..1] ± 451
     TaxAccount <TaxAcct> [0..1] ± 451
     AdditionalInformation <AddtlInf> [0..1] ± C4 451
   DebtorAgent <DbtrAgt> [0..1]  452
     Identification <Id> [1..1] ± 452
     AlternateIdentification <AltrnId> [0..1] ± 453
     CashAccount <CshAcct> [0..1] ± 453
     ChargesAccount <ChrgsAcct> [0..1] ± 454
     CommissionAccount <ComssnAcct> [0..1] ± 454
     TaxAccount <TaxAcct> [0..1] ± 454
     AdditionalInformation <AddtlInf> [0..1] ± C4 454
   Creditor <Cdtr> [0..1]  455
     Identification <Id> [1..1] ± 455
     AlternateIdentification <AltrnId> [0..1] ± 456
     CashAccount <CshAcct> [0..1] ± 456
     ChargesAccount <ChrgsAcct> [0..1] ± 457
     CommissionAccount <ComssnAcct> [0..1] ± 457
     TaxAccount <TaxAcct> [0..1] ± 457
     AdditionalInformation <AddtlInf> [0..1] ± C4 457
   CreditorAgent <CdtrAgt> [0..1]  458
     Identification <Id> [1..1] ± 458
     AlternateIdentification <AltrnId> [0..1] ± 459
     CashAccount <CshAcct> [0..1] ± 459
     ChargesAccount <ChrgsAcct> [0..1] ± 460
     CommissionAccount <ComssnAcct> [0..1] ± 460
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 120 February 2025
```

