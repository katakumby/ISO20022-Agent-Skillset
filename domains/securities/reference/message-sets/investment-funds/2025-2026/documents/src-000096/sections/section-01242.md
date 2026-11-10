---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.12 ForeignExchangeDetails <FXDtls>", "41.4.4.8.12.5 QuotingInstitution <QtgInstn>"]
file_pages: [1745, 1746, 1747]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.12.5 QuotingInstitution <QtgInstn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1745 to 1747.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1745

```text
41.4.4.8.12.5  QuotingInstitution <QtgInstn>
Presence: [0..1]
Definition: Party that proposes a foreign exchange rate.
QuotingInstitution <QtgInstn> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
41.4.4.8.13  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference1Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
DRIP DividendReinvestment Reinvestment of proceeds into
securities.
41.4.4.8.14  Group1Or2Units <Grp1Or2Units>
Presence: [0..1]
Definition: Tax group to which the purchased investment fund units belong. The investor indicates to the
intermediary operating pooled nominees, which type of unit is to be sold.
Datatype: "UKTaxGroupUnit1Code" on page 5387
CodeName Name Definition
GRP1 Group1 The units that were purchased prior to
the last ex-div date.
GRP2 Group2 The units that were purchased since the
ex-div date, and that benefit from the tax
exemption.
41.4.4.8.15  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and tax to be applied to the gross amount.
Impacted by: C19 "FeeTaxElementRule"
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1745 May 2026
```

## File page 1746

```text
TransactionOverhead <TxOvrhd> contains the following FeeAndTax2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1748
   IndividualFee <IndvFee> [0..*]  C18,
C36,
C37
1748
     Type <Tp> [1..1]  1749
{Or       Code <Cd> [1..1] CodeSet 1749
Or}       Proprietary <Prtry> [1..1] ± 1750
     Basis <Bsis> [0..1]  1750
{Or       Code <Cd> [1..1] CodeSet 1751
Or}       Proprietary <Prtry> [1..1] ± 1751
     StandardAmount <StdAmt> [0..1] Amount C3, C10 1751
     StandardRate <StdRate> [0..1] Rate 1752
     DiscountDetails <DscntDtls> [0..1]  C16 1752
       Amount <Amt> [0..1] Amount C3, C10 1752
       Rate <Rate> [0..1] Rate 1753
       Basis <Bsis> [0..1]  1753
{Or         Code <Cd> [1..1] CodeSet 1753
Or}         Proprietary <Prtry> [1..1] ± 1754
     RequestedAmount <ReqdAmt> [0..1] Amount C3, C10 1754
     RequestedRate <ReqdRate> [0..1] Rate 1754
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 1755
     RecipientIdentification <RcptId> [0..1] ± 1755
   IndividualTax <IndvTax> [0..*]  1755
     Type <Tp> [1..1]  1756
{Or       Code <Cd> [1..1] CodeSet 1756
Or}       Proprietary <Prtry> [1..1] ± 1758
     Tax <Tax> [0..1]  1758
{Or       Amount <Amt> [1..1] Amount C3, C10 1758
Or}       Rate <Rate> [1..1] Rate 1759
     Country <Ctry> [0..1] CodeSet C8 1759
     ExemptionIndicator <XmptnInd> [1..1] Indicator 1759
     ExemptionReason <XmptnRsn> [0..1]  1759
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1746 May 2026
```

## File page 1747

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Code <Cd> [1..1] CodeSet 1759
Or}       Proprietary <Prtry> [1..1] ± 1762
     RecipientIdentification <RcptId> [0..1] ± 1762
     TaxCalculationDetails <TaxClctnDtls> [0..1]  1763
       Basis <Bsis> [1..1]  1763
{Or         Code <Cd> [1..1] CodeSet 1763
Or}         Proprietary <Prtry> [1..1] ± 1763
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  1764
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C13,
C14,
C22,
C23,
C27
1764
       ISIN <ISIN> [0..1] IdentifierSet 1766
       OtherIdentification <OthrId> [0..*]  1766
         Identification <Id> [1..1] Text 1766
         Suffix <Sfx> [0..1] Text 1766
         Type <Tp> [1..1]  1766
{Or           Code <Cd> [1..1] CodeSet 1767
Or}           Proprietary <Prtry> [1..1] Text 1768
       Description <Desc> [0..1] Text 1768
     Quantity <Qty> [1..1]  1769
{Or       Quantity <Qty> [1..1] ± C15 1769
Or}       ProprietaryQuantity <PrtryQty> [1..1]  1769
         Quantity <Qty> [1..1] Quantity 1770
         QuantityType <QtyTp> [1..1] Text 1770
         Issuer <Issr> [1..1] Text 1770
         SchemeName <SchmeNm> [0..1] Text 1770
     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1770
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1747 May 2026
```

