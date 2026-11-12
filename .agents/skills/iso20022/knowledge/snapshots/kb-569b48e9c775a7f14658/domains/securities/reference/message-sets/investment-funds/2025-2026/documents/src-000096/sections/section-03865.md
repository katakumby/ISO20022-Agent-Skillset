---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.2 CashSettlement3"]
file_pages: [5154]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.2 CashSettlement3

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5154 to 5154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5154

```text
OtherCashSettlementDetails <OthrCshSttlmDtls> contains the following elements (see
"PaymentInstrument17" on page 5048 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementCurrency <SttlmCcy> [1..1] CodeSet C1 5049
   DividendPercentage <DvddPctg> [0..1] Rate 5050
   SubscriptionPaymentInstrument <SbcptPmtInstrm> [0..1]  5050
{Or     PaymentCardDetails <PmtCardDtls> [1..1] ± 5050
Or     DirectDebitDetails <DrctDbtDtls> [1..1] ± 5050
Or     Cheque <Chq> [1..1] Indicator 5051
Or}     BankersDraft <BkrsDrft> [1..1] Indicator 5051
   RedemptionPaymentInstrument <RedPmtInstrm> [0..1]  5051
{Or     ChequeDetails <ChqDtls> [1..1] ± 5052
Or}     BankersDraftDetails <BkrsDrftDtls> [1..1] ± 5052
   DividendPaymentInstrument <DvddPmtInstrm> [0..1]  5052
{Or     ChequeDetails <ChqDtls> [1..1] ± 5052
Or}     BankersDraftDetails <BkrsDrftDtls> [1..1] ± 5053
   SavingsPlanPaymentInstrument <SvgsPlanPmtInstrm> [0..1]  5053
{Or     PaymentCardDetails <PmtCardDtls> [1..1] ± 5053
Or     DirectDebitDetails <DrctDbtDtls> [1..1] ± 5054
Or     Cheque <Chq> [1..1] Indicator 5054
Or}     BankersDraft <BkrsDrft> [1..1] Indicator 5055
   InterestPaymentInstrument <IntrstPmtInstrm> [0..1]  5055
{Or     ChequeDetails <ChqDtls> [1..1] ± 5055
Or}     BankersDraftDetails <BkrsDrftDtls> [1..1] ± 5055
66.1.42.2  CashSettlement3
Definition: Cash settlement parties and accounts.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5154 May 2026
```

