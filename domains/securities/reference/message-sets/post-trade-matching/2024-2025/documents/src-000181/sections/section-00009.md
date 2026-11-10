---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "2.4 Message Building Blocks", "2.4.3 ConfirmationParties <ConfPties>"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2.4.3 ConfirmationParties <ConfPties>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
2.4.3 ConfirmationParties <ConfPties>
Presence: [0..*]
Definition: Parties involved in the confirmation of the details of a trade.
ConfirmationParties <ConfPties> contains the following ConfirmationParties7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Buyer <Buyr> [0..1] ± 11
   Borrower <Brrwr> [0..1] ± 12
   Seller <Sellr> [0..1] ± 13
   Lender <Lndr> [0..1] ± 14
   BrokerOfCredit <BrkrOfCdt> [0..1] ± 15
   IntroducingFirm <IntrdcgFirm> [0..1] ± 16
   StepInFirm <StepInFirm> [0..1] ± 17
   StepOutFirm <StepOutFirm> [0..1] ± 18
   ClearingFirm <ClrFirm> [0..1] ± 19
   ExecutingBroker <ExctgBrkr> [0..1] ± 20
   CMUParty <CMUPty> [0..1] ± 21
   CMUCounterparty <CMUCtrPty> [0..1] ± 22
   AffirmingParty <AffrmgPty> [0..1] ± 23
   TradeBeneficiaryParty <TradBnfcryPty> [0..1] ± 24
2.4.3.1  Buyer <Buyr>
Presence: [0..1]
Definition: Party that buys goods or services, or a financial instrument.
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 11 February 2025
```

