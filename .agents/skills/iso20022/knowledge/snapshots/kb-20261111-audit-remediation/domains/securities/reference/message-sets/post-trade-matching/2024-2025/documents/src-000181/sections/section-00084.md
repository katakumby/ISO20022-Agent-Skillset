---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.9 ConfirmationParties <ConfPties>", "3.4.9.5 BrokerOfCredit <BrkrOfCdt>"]
file_pages: [109]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.9.5 BrokerOfCredit <BrkrOfCdt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 109 to 109.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 109

```text
Lender <Lndr> contains the following elements (see "ConfirmationPartyDetails7" on page 444 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 445
   AlternateIdentification <AltrnId> [0..1] ± 445
   ProcessingIdentification <PrcgId> [0..1] Text 446
   AdditionalInformation <AddtlInf> [0..1] ± C1 446
   InvestorCapacity <InvstrCpcty> [0..1] ± 446
   TradingPartyCapacity <TradgPtyCpcty> [0..1] ± 447
3.4.9.5  BrokerOfCredit <BrkrOfCdt>
Presence: [0..1]
Definition: Brokerage firm which is the commissioned broker in a multi-broker trade.
BrokerOfCredit <BrkrOfCdt> contains the following elements (see "ConfirmationPartyDetails8" on
page 481 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 481
   AlternateIdentification <AltrnId> [0..1] ± 482
   ProcessingIdentification <PrcgId> [0..1] Text 482
   AdditionalInformation <AddtlInf> [0..1] ± C1 482
3.4.9.6  IntroducingFirm <IntrdcgFirm>
Presence: [0..1]
Definition: Broker or other intermediary with the closest association with the investor.
IntroducingFirm <IntrdcgFirm> contains the following elements (see "ConfirmationPartyDetails8" on
page 481 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 481
   AlternateIdentification <AltrnId> [0..1] ± 482
   ProcessingIdentification <PrcgId> [0..1] Text 482
   AdditionalInformation <AddtlInf> [0..1] ± C1 482
3.4.9.7  StepInFirm <StepInFirm>
Presence: [0..1]
Definition: Brokerage firm assigned to take credit on the trade from the step-out brokerage firm.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 109 February 2025
```

