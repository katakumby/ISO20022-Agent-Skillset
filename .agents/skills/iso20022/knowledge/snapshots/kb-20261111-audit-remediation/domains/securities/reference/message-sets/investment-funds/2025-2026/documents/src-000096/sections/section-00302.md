---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.4 Message Building Blocks", "22.4.7 TransactionOnAccount <TxOnAcct>", "22.4.7.5 ClassType <ClssTp>"]
file_pages: [418, 419]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.4.7.5 ClassType <ClssTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 418 to 419.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 418

```text
CodeName Name Definition
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
22.4.7.5  ClassType <ClssTp>
Presence: [0..1]
Definition: Features of units offered by a fund. For example, a unit may have a specific load structure,
eg, front end or back end, an income policy, eg, pay out or accumulate, or a trailer policy, eg, with or
without. Fund classes are typically denoted by a single character, eg, 'Class A', 'Class 2'.
Datatype: "Max35Text" on page 5403
22.4.7.6  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to a class type, ie, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 5294
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
22.4.7.7  TransactionDetails <TxDtls>
Presence: [1..*]
Definition: Process of buying, selling, switching or transferring fund units.
Impacted by: C9 "TransactionTypeLegExecutionIdentificationRule", C10
"TransactionTypeLegIdentificationRule"
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 418 May 2026
```

## File page 419

```text
TransactionDetails <TxDtls> contains the following elements (see "InvestmentFundTransaction3" on
page 4717 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TransactionType <TxTp> [1..1] CodeSet 4719
Or   ExtendedTransactionType <XtndedTxTp> [1..1] Text 4720
Or   CorporateActionEventType <CorpActnEvtTp> [1..1] CodeSet 4720
Or}   ExtendedCorporateActionEventType
<XtndedCorpActnEvtTp>
[1..1] Text 4722
   BookingStatus <BookgSts> [0..1] CodeSet 4722
   MasterReference <MstrRef> [0..1] Text 4723
   OrderReference <OrdrRef> [0..1] Text 4723
   ClientReference <ClntRef> [0..1] Text 4723
   DealReference <DealRef> [0..1] Text 4723
   LegIdentification <LegId> [0..1] Text 4723
   LegExecutionIdentification <LegExctnId> [0..1] Text 4723
   OrderDateTime <OrdrDtTm> [0..1] DateTime 4723
   SettledTransactionIndicator <SttldTxInd> [1..1] Indicator 4724
   RegisteredTransactionIndicator <RegdTxInd> [1..1] Indicator 4724
   UnitsQuantity <UnitsQty> [1..1] ± 4724
   CreditDebit <CdtDbt> [1..1] CodeSet 4724
   Reversal <Rvsl> [0..1] CodeSet 4724
   SettlementAmount <SttlmAmt> [0..1] Amount C1, C13 4725
   SettlementDate <SttlmDt> [0..1] Date 4725
   TradeDateTime <TradDtTm> [1..1] ± 4725
   CumDividendIndicator <CumDvddInd> [1..1] Indicator 4725
   PartiallyExecutedIndicator <PrtlyExctdInd> [1..1] Indicator 4726
   PriceDetails <PricDtls> [0..1]  4726
{Or     Type <Tp> [1..1] CodeSet 4726
Or}     ExtendedType <XtndedTp> [1..1] Text 4727
     Value <Val> [1..1] ± 4727
     PriceMethod <PricMtd> [0..1] CodeSet 4728
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 419 May 2026
```

