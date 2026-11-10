---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.19 Equalisation3", "66.1.26.19.3 EqualisationMethodologyType <EqulstnMthdlgyTp>", "66.1.26.19.3.2 RelatedSubscription <RltdSbcpt>"]
file_pages: [4770]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.19.3.2 RelatedSubscription <RltdSbcpt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4770 to 4770.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4770

```text
CodeName Name Definition
fee. Performance fee to be paid by the
investor when the value of the
investment fund units were below their
applicable high-watermark on
subscription date, and above the high-
watermark on redemption date.
DDEP DepreciationDeposit Performance fee to be paid by the
investor when the net asset value
reaches the high-watermark if the net
asset value was under the high-
watermark on subscription date.
EQCR EqualisationCredit Prepayment amount to be paid by the
investor at the moment of the
subscription. The amount is based on
the positive difference between the gross
asset value at subscription and the high-
watermark, when the investment fund
units are subscribed to above their high-
watermark.
66.1.26.19.3.2  RelatedSubscription <RltdSbcpt>
Presence: [0..*]
Definition: Details of the related subscription order to which the equalisation applies.
RelatedSubscription <RltdSbcpt> contains the following RelatedSubscription1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] ± 4770
   RelatedQuantity <RltdQty> [0..1] Quantity 4771
   RelatedAmount <RltdAmt> [0..1] Amount C2, C10 4771
   ContingentLiquidationPerUnit <CntngntLqdtnPerUnit> [0..1] Amount C2, C10 4771
   DepreciationDepositPerUnit <DprctnDpstPerUnit> [0..1] Amount C2, C10 4771
   EqualisationCreditPerUnit <EqulstnCdtPerUnit> [0..1] Amount C2, C10 4772
66.1.26.19.3.2.1  Reference <Ref>
Presence: [1..1]
Definition: Reference to the related subscription order the performance fee is based on.
Reference <Ref> contains the following elements (see "AdditionalReference11" on page 4553 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4770 May 2026
```

