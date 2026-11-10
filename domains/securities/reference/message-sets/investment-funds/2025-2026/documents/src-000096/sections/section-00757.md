---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.9 UnitsDetails <UnitsDtls>", "35.4.14.10.9.6 Reference <Ref>"]
file_pages: [1039, 1040]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.9.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1039 to 1040.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1039

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
35.4.14.10.9.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
35.4.14.10.9.7  PriceDetails <PricDtls>
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
35.4.14.10.9.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C34 "NonStandardSLAReferenceRule", C46 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1039 May 2026
```

## File page 1040

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C18 1041
   TotalFees <TtlFees> [0..1] Amount C1, C18 1042
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C18 1042
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1042
   IndividualFee <IndvFee> [0..*]  C6 1043
     Type <Tp> [1..1]  1043
{Or       Code <Cd> [1..1] CodeSet 1044
Or}       Proprietary <Prtry> [1..1] ± 1045
     Basis <Bsis> [0..1]  1045
{Or       Code <Cd> [1..1] CodeSet 1045
Or}       Proprietary <Prtry> [1..1] ± 1046
     StandardAmount <StdAmt> [0..1] Amount C1, C18 1046
     StandardRate <StdRate> [0..1] Rate 1046
     DiscountDetails <DscntDtls> [0..1]  C23 1047
       Amount <Amt> [0..1] Amount C1, C18 1047
       Rate <Rate> [0..1] Rate 1048
       Basis <Bsis> [0..1]  1048
{Or         Code <Cd> [1..1] CodeSet 1048
Or}         Proprietary <Prtry> [1..1] ± 1048
     AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1049
     AppliedRate <ApldRate> [0..1] Rate 1049
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 1049
     RecipientIdentification <RcptId> [0..1] ± 1049
     InformativeIndicator <InftvInd> [1..1] Indicator 1050
   IndividualTax <IndvTax> [0..*] ± 1050
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  1050
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C20,
C21,
C31,
C32,
C35
1051
       ISIN <ISIN> [0..1] IdentifierSet 1053
       OtherIdentification <OthrId> [0..*]  1053
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1040 May 2026
```

