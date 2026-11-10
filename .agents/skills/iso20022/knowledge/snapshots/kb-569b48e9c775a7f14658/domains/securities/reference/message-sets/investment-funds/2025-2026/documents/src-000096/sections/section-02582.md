---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.6 RequestedSettlementCurrency <ReqdSttlmCcy>"]
file_pages: [3632, 3633, 3634]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.6 RequestedSettlementCurrency <ReqdSttlmCcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3632 to 3634.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3632

```text
53.4.5.17.6  RequestedSettlementCurrency <ReqdSttlmCcy>
Presence: [0..1]
Definition: Currency requested for settlement of cash proceeds.
Impacted by: C2 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
53.4.5.17.7  RequestedNAVCurrency <ReqdNAVCcy>
Presence: [0..1]
Definition: Currency to be used for pricing the fund. This currency must be among the set of currencies
in which the price may be expressed, as stated in the prospectus.
Impacted by: C3 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
53.4.5.17.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and tax to be applied to the net amount.
Impacted by: C17 "FeeTaxElementRule"
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3632 May 2026
```

## File page 3633

```text
TransactionOverhead <TxOvrhd> contains the following FeeAndTax2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 3635
   IndividualFee <IndvFee> [0..*]  C16,
C36,
C37
3635
     Type <Tp> [1..1]  3636
{Or       Code <Cd> [1..1] CodeSet 3636
Or}       Proprietary <Prtry> [1..1] ± 3637
     Basis <Bsis> [0..1]  3637
{Or       Code <Cd> [1..1] CodeSet 3638
Or}       Proprietary <Prtry> [1..1] ± 3638
     StandardAmount <StdAmt> [0..1] Amount C2, C7 3638
     StandardRate <StdRate> [0..1] Rate 3639
     DiscountDetails <DscntDtls> [0..1]  C14 3639
       Amount <Amt> [0..1] Amount C2, C7 3639
       Rate <Rate> [0..1] Rate 3640
       Basis <Bsis> [0..1]  3640
{Or         Code <Cd> [1..1] CodeSet 3640
Or}         Proprietary <Prtry> [1..1] ± 3641
     RequestedAmount <ReqdAmt> [0..1] Amount C2, C7 3641
     RequestedRate <ReqdRate> [0..1] Rate 3641
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 3642
     RecipientIdentification <RcptId> [0..1] ± 3642
   IndividualTax <IndvTax> [0..*]  3642
     Type <Tp> [1..1]  3643
{Or       Code <Cd> [1..1] CodeSet 3643
Or}       Proprietary <Prtry> [1..1] ± 3645
     Tax <Tax> [0..1]  3645
{Or       Amount <Amt> [1..1] Amount C2, C7 3645
Or}       Rate <Rate> [1..1] Rate 3646
     Country <Ctry> [0..1] CodeSet C6 3646
     ExemptionIndicator <XmptnInd> [1..1] Indicator 3646
     ExemptionReason <XmptnRsn> [0..1]  3646
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3633 May 2026
```

## File page 3634

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Code <Cd> [1..1] CodeSet 3646
Or}       Proprietary <Prtry> [1..1] ± 3649
     RecipientIdentification <RcptId> [0..1] ± 3649
     TaxCalculationDetails <TaxClctnDtls> [0..1]  3650
       Basis <Bsis> [1..1]  3650
{Or         Code <Cd> [1..1] CodeSet 3650
Or}         Proprietary <Prtry> [1..1] ± 3650
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  3651
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C22,
C23,
C28
3651
       ISIN <ISIN> [0..1] IdentifierSet 3653
       OtherIdentification <OthrId> [0..*]  3653
         Identification <Id> [1..1] Text 3653
         Suffix <Sfx> [0..1] Text 3653
         Type <Tp> [1..1]  3653
{Or           Code <Cd> [1..1] CodeSet 3654
Or}           Proprietary <Prtry> [1..1] Text 3655
       Description <Desc> [0..1] Text 3655
     Quantity <Qty> [1..1]  3656
{Or       Quantity <Qty> [1..1] ± C13 3656
Or}       ProprietaryQuantity <PrtryQty> [1..1]  3656
         Quantity <Qty> [1..1] Quantity 3657
         QuantityType <QtyTp> [1..1] Text 3657
         Issuer <Issr> [1..1] Text 3657
         SchemeName <SchmeNm> [0..1] Text 3657
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3657
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3634 May 2026
```

