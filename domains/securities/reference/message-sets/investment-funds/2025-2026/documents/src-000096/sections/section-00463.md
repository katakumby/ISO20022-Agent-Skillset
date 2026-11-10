---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.12 UnitsDetails <UnitsDtls>", "28.4.7.12.6 Reference <Ref>"]
file_pages: [638, 639]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.12.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 638 to 639.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 638

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
28.4.7.12.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
28.4.7.12.7  PriceDetails <PricDtls>
Presence: [0..1]
Definition: Information related to the price. This may specify the price of original order confirmation.
PriceDetails <PricDtls> contains the following elements (see "UnitPrice23" on page 5125 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 5125
   Value <Val> [1..1] ± 5125
   PriceMethod <PricMtd> [0..1] CodeSet 5125
   AccruedInterestNAV <AcrdIntrstNAV> [0..1] Amount C2, C10 5126
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity 5126
   TaxableIncomePerShare <TaxblIncmPerShr> [0..1] Amount C1 5126
   TaxableIncomePerShareCalculated
<TaxblIncmPerShrClctd>
[0..1]  5127
{Or     Code <Cd> [1..1] CodeSet 5127
Or}     Proprietary <Prtry> [1..1] ± 5127
28.4.7.12.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C23 "NonStandardSLAReferenceRule", C34 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 638 May 2026
```

## File page 639

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 640
   TotalFees <TtlFees> [0..1] Amount C1, C10 641
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 641
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 641
   IndividualFee <IndvFee> [0..*]  C6 642
     Type <Tp> [1..1]  642
{Or       Code <Cd> [1..1] CodeSet 643
Or}       Proprietary <Prtry> [1..1] ± 644
     Basis <Bsis> [0..1]  644
{Or       Code <Cd> [1..1] CodeSet 644
Or}       Proprietary <Prtry> [1..1] ± 645
     StandardAmount <StdAmt> [0..1] Amount C1, C10 645
     StandardRate <StdRate> [0..1] Rate 645
     DiscountDetails <DscntDtls> [0..1]  C15 646
       Amount <Amt> [0..1] Amount C1, C10 646
       Rate <Rate> [0..1] Rate 647
       Basis <Bsis> [0..1]  647
{Or         Code <Cd> [1..1] CodeSet 647
Or}         Proprietary <Prtry> [1..1] ± 647
     AppliedAmount <ApldAmt> [0..1] Amount C1, C10 648
     AppliedRate <ApldRate> [0..1] Rate 648
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 648
     RecipientIdentification <RcptId> [0..1] ± 648
     InformativeIndicator <InftvInd> [1..1] Indicator 649
   IndividualTax <IndvTax> [0..*] ± 649
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  649
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C24
650
       ISIN <ISIN> [0..1] IdentifierSet 652
       OtherIdentification <OthrId> [0..*]  652
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 639 May 2026
```

