---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.20 TwoLegTransactionDetails <TwoLegTxDtls>", "3.4.20.6 SecondLegNarrative <ScndLegNrrtv>"]
file_pages: [133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.20.6 SecondLegNarrative <ScndLegNrrtv>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 133 to 133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 133

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemunerationAmountRequest <RmnrtnAmtReq> [0..1] Indicator 242
   RemunerationAmount <RmnrtnAmt> [0..1] ± 242
   BorrowingInterestAmount <BrrwgIntrstAmt> [0..1] ± 242
   BorrowingFee <BrrwgFee> [0..1] ± 243
   NetMarketValue <NetMktVal> [0..1] ± 243
   RemainingFaceValue <RmngFaceVal> [0..1] ± 243
   RemainingBookValue <RmngBookVal> [0..1] ± 244
   ClearingBrokerCommission <ClrBrkrComssn> [0..1] ± 244
   DifferenceInPrice <DiffInPric> [0..1] ± 244
   OddLotFee <OddLotFee> [0..1] Indicator 245
3.4.20.6  SecondLegNarrative <ScndLegNrrtv>
Presence: [0..1]
Definition: Provides additional information about the second leg in narrative form.
Datatype: "Max140Text" on page 668
3.4.20.7  EndPrice <EndPric>
Presence: [0..1]
Definition: Negotiated fixed price of the security to buy it back.
EndPrice <EndPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
3.4.20.8  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Closing date/time or maturity date/time of the transaction.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 133 February 2025
```

