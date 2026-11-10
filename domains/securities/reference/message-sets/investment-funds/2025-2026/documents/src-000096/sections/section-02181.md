---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.15 AccumulationRightReference <AcmltnRghtRef>"]
file_pages: [3070, 3071, 3072]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.15 AccumulationRightReference <AcmltnRghtRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3070 to 3072.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3070

```text
50.4.4.9.15  AccumulationRightReference <AcmltnRghtRef>
Presence: [0..1]
Definition: Reference of an accumulation right program, in which sales commissions are based on a
customer's present purchases of shares and the aggregate quantity previously purchased by the
customer. An accumulation rights program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
50.4.4.9.16  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and tax to be applied to the net amount.
Impacted by: C19 "FeeTaxElementRule"
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3070 May 2026
```

## File page 3071

```text
TransactionOverhead <TxOvrhd> contains the following FeeAndTax2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3073
   IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
3073
     Type <Tp> [1..1]  3074
{Or       Code <Cd> [1..1] CodeSet 3074
Or}       Proprietary <Prtry> [1..1] ± 3075
     Basis <Bsis> [0..1]  3075
{Or       Code <Cd> [1..1] CodeSet 3076
Or}       Proprietary <Prtry> [1..1] ± 3076
     StandardAmount <StdAmt> [0..1] Amount C3, C10 3076
     StandardRate <StdRate> [0..1] Rate 3077
     DiscountDetails <DscntDtls> [0..1]  C16 3077
       Amount <Amt> [0..1] Amount C3, C10 3077
       Rate <Rate> [0..1] Rate 3078
       Basis <Bsis> [0..1]  3078
{Or         Code <Cd> [1..1] CodeSet 3078
Or}         Proprietary <Prtry> [1..1] ± 3079
     RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 3079
     RequestedRate <ReqdRate> [0..1] Rate 3079
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 3080
     RecipientIdentification <RcptId> [0..1] ± 3080
   IndividualTax <IndvTax> [0..*]  3080
     Type <Tp> [1..1]  3081
{Or       Code <Cd> [1..1] CodeSet 3081
Or}       Proprietary <Prtry> [1..1] ± 3083
     Tax <Tax> [0..1]  3083
{Or       Amount <Amt> [1..1] Amount C3, C10 3083
Or}       Rate <Rate> [1..1] Rate 3084
     Country <Ctry> [0..1] CodeSet C8 3084
     ExemptionIndicator <XmptnInd> [1..1] Indicator 3084
     ExemptionReason <XmptnRsn> [0..1]  3084
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3071 May 2026
```

## File page 3072

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Code <Cd> [1..1] CodeSet 3084
Or}       Proprietary <Prtry> [1..1] ± 3087
     RecipientIdentification <RcptId> [0..1] ± 3087
     TaxCalculationDetails <TaxClctnDtls> [0..1]  3088
       Basis <Bsis> [1..1]  3088
{Or         Code <Cd> [1..1] CodeSet 3088
Or}         Proprietary <Prtry> [1..1] ± 3088
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  3089
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
3089
       ISIN <ISIN> [0..1] IdentifierSet 3091
       OtherIdentification <OthrId> [0..*]  3091
         Identification <Id> [1..1] Text 3091
         Suffix <Sfx> [0..1] Text 3091
         Type <Tp> [1..1]  3091
{Or           Code <Cd> [1..1] CodeSet 3092
Or}           Proprietary <Prtry> [1..1] Text 3093
       Description <Desc> [0..1] Text 3093
     Quantity <Qty> [1..1]  3094
{Or       Quantity <Qty> [1..1] ± C15 3094
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3094
         Quantity <Qty> [1..1] Quantity 3095
         QuantityType <QtyTp> [1..1] Text 3095
         Issuer <Issr> [1..1] Text 3095
         SchemeName <SchmeNm> [0..1] Text 3095
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3095
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3072 May 2026
```

