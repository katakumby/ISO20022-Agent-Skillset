---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.10 UnitsDetails <UnitsDtls>", "40.4.15.11.10.6 Reference <Ref>"]
file_pages: [1617, 1618]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.10.6 Reference <Ref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1617 to 1618.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1617

```text
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
40.4.15.11.10.6  Reference <Ref>
Presence: [0..1]
Definition: Reference to the units number. This may be the order reference of the original acquisition,
the identification of a lot, a client reference, a sub-position reference or other related reference.
Datatype: "Max35Text" on page 5403
40.4.15.11.10.7  PriceDetails <PricDtls>
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
40.4.15.11.10.8  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees and taxes. This may specify the fees and taxes related to the original order
confirmation.
Impacted by: C36 "NonStandardSLAReferenceRule", C53 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1617 May 2026
```

## File page 1618

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C1, C18 1619
   TotalFees <TtlFees> [0..1] Amount C1, C18 1620
   TotalTaxes <TtlTaxs> [0..1] Amount C1, C18 1620
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1620
   IndividualFee <IndvFee> [0..*]  C6 1621
     Type <Tp> [1..1]  1621
{Or       Code <Cd> [1..1] CodeSet 1622
Or}       Proprietary <Prtry> [1..1] ± 1623
     Basis <Bsis> [0..1]  1623
{Or       Code <Cd> [1..1] CodeSet 1623
Or}       Proprietary <Prtry> [1..1] ± 1624
     StandardAmount <StdAmt> [0..1] Amount C1, C18 1624
     StandardRate <StdRate> [0..1] Rate 1624
     DiscountDetails <DscntDtls> [0..1]  C24 1625
       Amount <Amt> [0..1] Amount C1, C18 1625
       Rate <Rate> [0..1] Rate 1626
       Basis <Bsis> [0..1]  1626
{Or         Code <Cd> [1..1] CodeSet 1626
Or}         Proprietary <Prtry> [1..1] ± 1626
     AppliedAmount <ApldAmt> [0..1] Amount C1, C18 1627
     AppliedRate <ApldRate> [0..1] Rate 1627
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 1627
     RecipientIdentification <RcptId> [0..1] ± 1627
     InformativeIndicator <InftvInd> [1..1] Indicator 1628
   IndividualTax <IndvTax> [0..*] ± 1628
   DigitalNetworkFee <DgtlNtwkFee> [0..2]  1628
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C21,
C22,
C33,
C34,
C37
1629
       ISIN <ISIN> [0..1] IdentifierSet 1631
       OtherIdentification <OthrId> [0..*]  1631
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1618 May 2026
```

