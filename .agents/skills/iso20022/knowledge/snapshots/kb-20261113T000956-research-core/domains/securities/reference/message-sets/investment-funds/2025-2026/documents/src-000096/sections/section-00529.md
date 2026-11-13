---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.16 UnitsDetails <UnitsDtls>", "30.4.7.16.6 Reference <Ref>"]
file_pages: [726, 727]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.16.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 726 to 727.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 726

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
30.4.7.16.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
30.4.7.16.7  PriceDetails <PricDtls>
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
30.4.7.16.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C24 "NonStandardSLAReferenceRule", C35 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 726 May 2026
```

## File page 727

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 728
   TotalFees <TtlFees> [0..1] Amount C1, C10 729
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 729
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 729
   IndividualFee <IndvFee> [0..*]  C6 730
     Type <Tp> [1..1]  730
{Or       Code <Cd> [1..1] CodeSet 731
Or}       Proprietary <Prtry> [1..1] ± 732
     Basis <Bsis> [0..1]  732
{Or       Code <Cd> [1..1] CodeSet 732
Or}       Proprietary <Prtry> [1..1] ± 733
     StandardAmount <StdAmt> [0..1] Amount C1, C10 733
     StandardRate <StdRate> [0..1] Rate 733
     DiscountDetails <DscntDtls> [0..1]  C15 734
       Amount <Amt> [0..1] Amount C1, C10 734
       Rate <Rate> [0..1] Rate 735
       Basis <Bsis> [0..1]  735
{Or         Code <Cd> [1..1] CodeSet 735
Or}         Proprietary <Prtry> [1..1] ± 735
     AppliedAmount <ApldAmt> [0..1] Amount C1, C10 736
     AppliedRate <ApldRate> [0..1] Rate 736
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 736
     RecipientIdentification <RcptId> [0..1] ± 736
     InformativeIndicator <InftvInd> [1..1] Indicator 737
   IndividualTax <IndvTax> [0..*] ± 737
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  737
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C12,
C13,
C21,
C22,
C25
738
       ISIN <ISIN> [0..1] IdentifierSet 740
       OtherIdentification <OthrId> [0..*]  740
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 727 May 2026
```

