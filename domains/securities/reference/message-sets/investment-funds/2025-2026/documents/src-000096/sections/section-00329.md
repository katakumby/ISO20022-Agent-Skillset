---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.5 MasterReference <MstrRef>", "24.4.6.12 UnitsDetails <UnitsDtls>", "24.4.6.12.6 Reference <Ref>"]
file_pages: [462, 463]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.6.12.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 462 to 463.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 462

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
24.4.6.12.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
24.4.6.12.7  PriceDetails <PricDtls>
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
24.4.6.12.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C23 "NonStandardSLAReferenceRule", C34 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 462 May 2026
```

## File page 463

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 464
   TotalFees <TtlFees> [0..1] Amount C1, C10 465
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 465
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 465
   IndividualFee <IndvFee> [0..*]  C6 466
     Type <Tp> [1..1]  466
{Or       Code <Cd> [1..1] CodeSet 467
Or}       Proprietary <Prtry> [1..1] ± 468
     Basis <Bsis> [0..1]  468
{Or       Code <Cd> [1..1] CodeSet 468
Or}       Proprietary <Prtry> [1..1] ± 469
     StandardAmount <StdAmt> [0..1] Amount C1, C10 469
     StandardRate <StdRate> [0..1] Rate 469
     DiscountDetails <DscntDtls> [0..1]  C15 470
       Amount <Amt> [0..1] Amount C1, C10 470
       Rate <Rate> [0..1] Rate 471
       Basis <Bsis> [0..1]  471
{Or         Code <Cd> [1..1] CodeSet 471
Or}         Proprietary <Prtry> [1..1] ± 471
     AppliedAmount <ApldAmt> [0..1] Amount C1, C10 472
     AppliedRate <ApldRate> [0..1] Rate 472
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 472
     RecipientIdentification <RcptId> [0..1] ± 472
     InformativeIndicator <InftvInd> [1..1] Indicator 473
   IndividualTax <IndvTax> [0..*] ± 473
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  473
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C20,
C21,
C24
474
       ISIN <ISIN> [0..1] IdentifierSet 476
       OtherIdentification <OthrId> [0..*]  476
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 463 May 2026
```

