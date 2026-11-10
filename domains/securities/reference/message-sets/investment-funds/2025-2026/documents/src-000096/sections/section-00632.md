---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.16 UnitsDetails <UnitsDtls>", "34.4.4.16.6 Reference <Ref>"]
file_pages: [864, 865]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.16.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 864 to 865.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 864

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
34.4.4.16.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
34.4.4.16.7  PriceDetails <PricDtls>
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
34.4.4.16.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C22 "NonStandardSLAReferenceRule", C27 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 864 May 2026
```

## File page 865

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C10 866
   TotalFees <TtlFees> [0..1] Amount C1, C10 867
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C10 867
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 867
   IndividualFee <IndvFee> [0..*]  C4 868
     Type <Tp> [1..1]  868
{Or       Code <Cd> [1..1] CodeSet 869
Or}       Proprietary <Prtry> [1..1] ± 870
     Basis <Bsis> [0..1]  870
{Or       Code <Cd> [1..1] CodeSet 870
Or}       Proprietary <Prtry> [1..1] ± 871
     StandardAmount <StdAmt> [0..1] Amount C1, C10 871
     StandardRate <StdRate> [0..1] Rate 871
     DiscountDetails <DscntDtls> [0..1]  C14 872
       Amount <Amt> [0..1] Amount C1, C10 872
       Rate <Rate> [0..1] Rate 873
       Basis <Bsis> [0..1]  873
{Or         Code <Cd> [1..1] CodeSet 873
Or}         Proprietary <Prtry> [1..1] ± 873
     AppliedAmount <ApldAmt> [0..1] Amount C1, C10 874
     AppliedRate <ApldRate> [0..1] Rate 874
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 874
     RecipientIdentification <RcptId> [0..1] ± 874
     InformativeIndicator <InftvInd> [1..1] Indicator 875
   IndividualTax <IndvTax> [0..*] ± 875
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  875
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C11,
C12,
C20,
C21,
C23
876
       ISIN <ISIN> [0..1] IdentifierSet 878
       OtherIdentification <OthrId> [0..*]  878
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 865 May 2026
```

