---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.24 IncomePreference <IncmPref>"]
file_pages: [1956, 1957]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.24 IncomePreference <IncmPref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1956 to 1957.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1956

```text
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms37"
on page 4532 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ToAmount <ToAmt> [0..1] Amount C1, C13 4532
   FromAmount <FrAmt> [0..1] Amount C1, C13 4532
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 4533
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 4533
   ExchangeRate <XchgRate> [1..1] Rate 4534
   QuotationDate <QtnDt> [0..1] DateTime 4534
   QuotingInstitution <QtgInstn> [0..1] ± 4534
43.4.5.9.24  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference1Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
DRIP DividendReinvestment Reinvestment of proceeds into
securities.
43.4.5.9.25  Group1Or2Units <Grp1Or2Units>
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
43.4.5.9.26  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and taxes that are taken into consideration for the transaction,
so that the total difference between the net amount and gross amount is known, without taking into
account equalisation.
Impacted by: C23 "NonStandardsSLAReferenceRule", C39 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1956 May 2026
```

## File page 1957

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes45 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C3, C10 1958
   TotalFees <TtlFees> [0..1] Amount C3, C10 1959
   TotalTaxes <TtlTaxs> [0..1] Amount C3, C10 1959
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 1959
   IndividualFee <IndvFee> [0..*]  C6 1960
     Type <Tp> [1..1]  1960
{Or       Code <Cd> [1..1] CodeSet 1961
Or}       Proprietary <Prtry> [1..1] ± 1962
     Basis <Bsis> [0..1]  1962
{Or       Code <Cd> [1..1] CodeSet 1962
Or}       Proprietary <Prtry> [1..1] ± 1963
     StandardAmount <StdAmt> [0..1] Amount C3, C10 1963
     StandardRate <StdRate> [0..1] Rate 1963
     DiscountDetails <DscntDtls> [0..1]  C17 1964
       Amount <Amt> [0..1] Amount C3, C10 1964
       Rate <Rate> [0..1] Rate 1965
       Basis <Bsis> [0..1]  1965
{Or         Code <Cd> [1..1] CodeSet 1965
Or}         Proprietary <Prtry> [1..1] ± 1965
     AppliedAmount <ApldAmt> [0..1] Amount C3, C10 1966
     AppliedRate <ApldRate> [0..1] Rate 1966
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 1966
     RecipientIdentification <RcptId> [0..1] ± 1966
     InformativeIndicator <InftvInd> [1..1] Indicator 1967
   IndividualTax <IndvTax> [0..*] ± 1967
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  1967
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
1968
       ISIN <ISIN> [0..1] IdentifierSet 1970
       OtherIdentification <OthrId> [0..*]  1970
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1957 May 2026
```

