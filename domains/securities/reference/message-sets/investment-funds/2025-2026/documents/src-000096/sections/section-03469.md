---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.3 InvestmentFundTransaction3"]
file_pages: [4717, 4718]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.3 InvestmentFundTransaction3

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4717 to 4718.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4717

```text
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.26.3  InvestmentFundTransaction3
Definition: Creation/cancellation of investment units on the books of the fund or its designated agent, as
a result of executing an investment fund order.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4717 May 2026
```

## File page 4718

```text
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4718 May 2026
```

