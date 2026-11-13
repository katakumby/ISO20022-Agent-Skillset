---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.9 TransactionOverhead <TxOvrhd>"]
file_pages: [3564, 3565, 3566]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.9 TransactionOverhead <TxOvrhd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3564 to 3566.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3564

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
53.4.5.16.9  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and tax to be applied to the gross amount.
Impacted by: C17 "FeeTaxElementRule"
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3564 May 2026
```

## File page 3565

```text
TransactionOverhead <TxOvrhd> contains the following FeeAndTax2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3567
   IndividualFee <IndvFee> [0..*]  C16,
C36,
C37
3567
     Type <Tp> [1..1]  3568
{Or       Code <Cd> [1..1] CodeSet 3568
Or}       Proprietary <Prtry> [1..1] ± 3569
     Basis <Bsis> [0..1]  3569
{Or       Code <Cd> [1..1] CodeSet 3570
Or}       Proprietary <Prtry> [1..1] ± 3570
     StandardAmount <StdAmt> [0..1] Amount C2, C7 3570
     StandardRate <StdRate> [0..1] Rate 3571
     DiscountDetails <DscntDtls> [0..1]  C14 3571
       Amount <Amt> [0..1] Amount C2, C7 3571
       Rate <Rate> [0..1] Rate 3572
       Basis <Bsis> [0..1]  3572
{Or         Code <Cd> [1..1] CodeSet 3572
Or}         Proprietary <Prtry> [1..1] ± 3573
     RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3573
     RequestedRate <ReqdRate> [0..1] Rate 3573
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 3574
     RecipientIdentification <RcptId> [0..1] ± 3574
   IndividualTax <IndvTax> [0..*]  3574
     Type <Tp> [1..1]  3575
{Or       Code <Cd> [1..1] CodeSet 3575
Or}       Proprietary <Prtry> [1..1] ± 3577
     Tax <Tax> [0..1]  3577
{Or       Amount <Amt> [1..1] Amount C2, C7 3577
Or}       Rate <Rate> [1..1] Rate 3578
     Country <Ctry> [0..1] CodeSet C6 3578
     ExemptionIndicator <XmptnInd> [1..1] Indicator 3578
     ExemptionReason <XmptnRsn> [0..1]  3578
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3565 May 2026
```

## File page 3566

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Code <Cd> [1..1] CodeSet 3578
Or}       Proprietary <Prtry> [1..1] ± 3581
     RecipientIdentification <RcptId> [0..1] ± 3581
     TaxCalculationDetails <TaxClctnDtls> [0..1]  3582
       Basis <Bsis> [1..1]  3582
{Or         Code <Cd> [1..1] CodeSet 3582
Or}         Proprietary <Prtry> [1..1] ± 3582
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  3583
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3583
       ISIN <ISIN> [0..1] IdentifierSet 3585
       OtherIdentification <OthrId> [0..*]  3585
         Identification <Id> [1..1] Text 3585
         Suffix <Sfx> [0..1] Text 3585
         Type <Tp> [1..1]  3585
{Or           Code <Cd> [1..1] CodeSet 3586
Or}           Proprietary <Prtry> [1..1] Text 3587
       Description <Desc> [0..1] Text 3587
     Quantity <Qty> [1..1]  3588
{Or       Quantity <Qty> [1..1] ± C13 3588
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3588
         Quantity <Qty> [1..1] Quantity 3589
         QuantityType <QtyTp> [1..1] Text 3589
         Issuer <Issr> [1..1] Text 3589
         SchemeName <SchmeNm> [0..1] Text 3589
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3589
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3566 May 2026
```

