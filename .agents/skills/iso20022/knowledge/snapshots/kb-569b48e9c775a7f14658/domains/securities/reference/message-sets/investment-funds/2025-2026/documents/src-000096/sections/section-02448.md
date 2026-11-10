---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.46 SourceOfCash <SrcOfCsh>"]
file_pages: [3425]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.46 SourceOfCash <SrcOfCsh>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3425 to 3425.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3425

```text
Equalisation <Equlstn> contains the following elements (see "Equalisation4" on page 4729 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C1, C13 4729
   Rate <Rate> [0..1] Rate 4730
   EqualisationMethodologyType <EqulstnMthdlgyTp> [0..1] CodeSet 4730
   ContingentLiquidationPerUnit <CntngntLqdtnPerUnit> [0..1] Amount C2, C10 4730
   DepreciationDepositPerUnit <DprctnDpstPerUnit> [0..1] Amount C2, C10 4731
   EqualisationCreditPerUnit <EqulstnCdtPerUnit> [0..1] Amount C2, C10 4731
   HighWatermark <HghWtrmrk> [0..1] Amount C2, C10 4732
   GrossAssetValue <GrssAsstVal> [0..1] Amount C2, C10 4732
Constraints
• ContingentLiquidationMethodologyTypeRule
Contingent Liquidation per Unit can only be used with Contingent Liquidation Methodology Type.
On Condition
    /EqualisationMethodologyType is equal to value 'ContingentLiquidation'
Following Must be True
    /DepreciationDepositPerUnit Must be absent
 And    /EqualisationCreditPerUnit Must be absent
• DepreciationDepositMethodologyTypeRule
Depreciation Deposit per Unit can only be used with Depreciation Deposit Methodology Type.
On Condition
    /EqualisationMethodologyType is equal to value 'DepreciationDeposit'
Following Must be True
    /ContingentLiquidationPerUnit Must be absent
 And    /EqualisationCreditPerUnit Must be absent
• EqualisationCreditMethodologyTypeRule
Equalisation Credit per Unit can only be used with Equalisation Credit Methodology Type.
On Condition
    /EqualisationMethodologyType is equal to value 'EqualisationCredit'
Following Must be True
    /ContingentLiquidationPerUnit Must be absent
 And    /DepreciationDepositPerUnit Must be absent
52.4.5.10.46  SourceOfCash <SrcOfCsh>
Presence: [0..*]
Definition: Source of cash used for the settlement of the subscription.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3425 May 2026
```

