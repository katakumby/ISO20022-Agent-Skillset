---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.9 ConfirmationParties <ConfPties>", "3.4.9.8 StepOutFirm <StepOutFirm>"]
file_pages: [110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.9.8 StepOutFirm <StepOutFirm>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 110 to 110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 110

```text
StepInFirm <StepInFirm> contains the following elements (see "ConfirmationPartyDetails8" on
page 481 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 481
   AlternateIdentification <AltrnId> [0..1] ± 482
   ProcessingIdentification <PrcgId> [0..1] Text 482
   AdditionalInformation <AddtlInf> [0..1] ± C1 482
3.4.9.8  StepOutFirm <StepOutFirm>
Presence: [0..1]
Definition: Brokerage firm that executes an order, but gives other firms credit and some of the
commission for the trade.
StepOutFirm <StepOutFirm> contains the following elements (see "ConfirmationPartyDetails8" on
page 481 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 481
   AlternateIdentification <AltrnId> [0..1] ± 482
   ProcessingIdentification <PrcgId> [0..1] Text 482
   AdditionalInformation <AddtlInf> [0..1] ± C1 482
3.4.9.9  ClearingFirm <ClrFirm>
Presence: [0..1]
Definition: Party, also know as take up broker, that settles security transactions from another broker for
a fee.
ClearingFirm <ClrFirm> contains the following elements (see "ConfirmationPartyDetails9" on
page 422 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 422
   AlternateIdentification <AltrnId> [0..1] ± 423
   ProcessingIdentification <PrcgId> [0..1] Text 423
   AdditionalInformation <AddtlInf> [0..1] ± C1 423
   InvestorProtectionAssociationMembership
<InvstrPrtcnAssoctnMmbsh>
[0..1] Indicator 424
3.4.9.10  ExecutingBroker <ExctgBrkr>
Presence: [0..1]
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 110 February 2025
```

