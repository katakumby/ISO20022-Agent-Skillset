---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.3 Amount", "35.1.3.6 AmountAndDirection95", "35.1.3.6.9 ValueDate <ValDt>"]
file_pages: [1365]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.3.6.9 ValueDate <ValDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1365 to 1365.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1365

```text
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms23"
on page 1581 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 1581
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 1582
   ExchangeRate <XchgRate> [1..1] Rate 1582
   ResultingAmount <RsltgAmt> [1..1] Amount C1, C9 1582
35.1.3.6.9  ValueDate <ValDt>
Presence: [0..1]
Definition: Date and time at which the cash is at the disposal of the credit account owner, or ceases to
be at the disposal of the debit account owner.
ValueDate <ValDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.3.7  AmountAndDirection94
Definition: Posting of an item to a cash account, in the context of a cash transaction, that results in an
increase or decrease to the balance of the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccruedInterestIndicator <AcrdIntrstInd> [0..1] Indicator 1365
   StampDutyIndicator <StmpDtyInd> [0..1] Indicator 1366
   BrokerageAmountIndicator <BrkrgAmtInd> [0..1] Indicator 1366
   ResearchFeeIndicator <RsrchFeeInd> [0..1] Indicator 1366
   Amount <Amt> [1..1] Amount C1, C9 1366
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 1367
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C8 1367
   ForeignExchangeDetails <FXDtls> [0..1] ± 1367
   ValueDate <ValDt> [0..1] ± 1368
35.1.3.7.1  AccruedInterestIndicator <AcrdIntrstInd>
Presence: [0..1]
Definition: Indicates whether the net proceeds include interest accrued on the financial instrument.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1365 March 2026
```

