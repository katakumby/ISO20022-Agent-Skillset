---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.6.16 UnitsDetails <UnitsDtls>", "26.4.6.16.6 Reference <Ref>"]
file_pages: [550, 551]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.6.16.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 550 to 551.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 550

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
26.4.6.16.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
26.4.6.16.7  PriceDetails <PricDtls>
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
26.4.6.16.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C24 "NonStandardSLAReferenceRule", C35 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 550 May 2026
```

## File page 551

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 552
   TotalFees <TtlFees> [0..1] Amount C1, C10 553
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 553
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 553
   IndividualFee <IndvFee> [0..*]  C6 554
     Type <Tp> [1..1]  554
{Or       Code <Cd> [1..1] CodeSet 555
Or}       Proprietary <Prtry> [1..1] ± 556
     Basis <Bsis> [0..1]  556
{Or       Code <Cd> [1..1] CodeSet 556
Or}       Proprietary <Prtry> [1..1] ± 557
     StandardAmount <StdAmt> [0..1] Amount C1, C10 557
     StandardRate <StdRate> [0..1] Rate 557
     DiscountDetails <DscntDtls> [0..1]  C15 558
       Amount <Amt> [0..1] Amount C1, C10 558
       Rate <Rate> [0..1] Rate 559
       Basis <Bsis> [0..1]  559
{Or         Code <Cd> [1..1] CodeSet 559
Or}         Proprietary <Prtry> [1..1] ± 559
     AppliedAmount <ApldAmt> [0..1] Amount C1, C10 560
     AppliedRate <ApldRate> [0..1] Rate 560
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 560
     RecipientIdentification <RcptId> [0..1] ± 560
     InformativeIndicator <InftvInd> [1..1] Indicator 561
   IndividualTax <IndvTax> [0..*] ± 561
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  561
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C21,
C22,
C25
562
       ISIN <ISIN> [0..1] IdentifierSet 564
       OtherIdentification <OthrId> [0..*]  564
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 551 May 2026
```

