---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.19 ConfirmationPartyDetails7", "7.1.20.19.6 TradingPartyCapacity <TradgPtyCpcty>"]
file_pages: [447, 448]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.19.6 TradingPartyCapacity <TradgPtyCpcty>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 447 to 448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 447

```text
7.1.20.19.6  TradingPartyCapacity <TradgPtyCpcty>
Presence: [0..1]
Definition: Capacity of customer placing the order. Primarily used by futures exchanges to indicate the
CTI code (customer type indicator) as required by the US CFTC (Commodity Futures Trading
Commission).
TradingPartyCapacity <TradgPtyCpcty> contains one of the following elements (see
"TradingPartyCapacity4Choice" on page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 420
Or}   Proprietary <Prtry> [1..1] ± 422
7.1.20.20  CashParties33
Definition: Payment processes required to transfer cash from the debtor to the creditor.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 447 February 2025
```

## File page 448

```text
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
     TaxAccount <TaxAcct> [0..1] ± 460
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 448 February 2025
```

