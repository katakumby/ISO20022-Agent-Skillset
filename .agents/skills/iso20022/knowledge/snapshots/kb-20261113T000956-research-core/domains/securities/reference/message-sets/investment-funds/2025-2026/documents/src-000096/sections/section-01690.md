---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.24 IncomePreference <IncmPref>"]
file_pages: [2376, 2377]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.24 IncomePreference <IncmPref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2376 to 2377.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2376

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
46.4.5.10.24  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference1Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
DRIP DividendReinvestment Reinvestment of proceeds into
securities.
46.4.5.10.25  Group1Or2Units <Grp1Or2Units>
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
46.4.5.10.26  TransactionOverhead <TxOvrhd>
Presence: [0..1]
Definition: Fees (charges/commission) and taxes that are taken into consideration for the transaction,
so that the total difference between the net amount and gross amount is known, without taking into
account equalisation.
Impacted by: C23 "NonStandardsSLAReferenceRule", C42 "TransactionOverheadElementRule"
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2376 May 2026
```

## File page 2377

```text
TransactionOverhead <TxOvrhd> contains the following TotalFeesAndTaxes45 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalOverheadApplied <TtlOvrhdApld> [0..1] Amount C3, C10 2378
   TotalFees <TtlFees> [0..1] Amount C3, C10 2379
   TotalTaxes <TtlTaxs> [0..1] Amount C3, C10 2379
   CommercialAgreementReference <ComrclAgrmtRef> [0..1] Text 2379
   IndividualFee <IndvFee> [0..*]  C6 2380
     Type <Tp> [1..1]  2380
{Or       Code <Cd> [1..1] CodeSet 2381
Or}       Proprietary <Prtry> [1..1] ± 2382
     Basis <Bsis> [0..1]  2382
{Or       Code <Cd> [1..1] CodeSet 2382
Or}       Proprietary <Prtry> [1..1] ± 2383
     StandardAmount <StdAmt> [0..1] Amount C3, C10 2383
     StandardRate <StdRate> [0..1] Rate 2383
     DiscountDetails <DscntDtls> [0..1]  C17 2384
       Amount <Amt> [0..1] Amount C3, C10 2384
       Rate <Rate> [0..1] Rate 2385
       Basis <Bsis> [0..1]  2385
{Or         Code <Cd> [1..1] CodeSet 2385
Or}         Proprietary <Prtry> [1..1] ± 2385
     AppliedAmount <ApldAmt> [0..1] Amount C3, C10 2386
     AppliedRate <ApldRate> [0..1] Rate 2386
     NonStandardSLAReference <NonStdSLARef> [0..1] Text 2386
     RecipientIdentification <RcptId> [0..1] ± 2386
     InformativeIndicator <InftvInd> [1..1] Indicator 2387
   IndividualTax <IndvTax> [0..*] ± 2387
   DigitalNetworkFee <DgtlNtwkFee> [0..*]  2387
     FinancialInstrumentIdentification <FinInstrmId> [1..1]  C14,
C15,
C21,
C22,
C28
2388
       ISIN <ISIN> [0..1] IdentifierSet 2390
       OtherIdentification <OthrId> [0..*]  2390
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2377 May 2026
```

