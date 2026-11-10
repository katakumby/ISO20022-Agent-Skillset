---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.18 CancellationReason31Choice", "66.1.45.18.1 Code <Cd>"]
file_pages: [5190]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.18.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5190 to 5190.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5190

```text
66.1.45.18.1  Code <Cd>
Presence: [1..1]
Definition: Confirmation cancellation reason expressed as a code.
Datatype: "ConfirmationCancellationReason1Code" on page 5287
CodeName Name Definition
CSHN CashNotReceived Confirmation is cancelled because the
cash has not been received.
REPL ConfirmationReplacement Confirmation is cancelled because it will
be replaced.
BENA IncorrectBackEndLoadAmount Confirmation is cancelled because the
back end load amount is incorrect.
CSHW IncorrectCashAmount Confirmation is cancelled because the
cash amount is incorrect.
DISA IncorrectDiscountAmount Confirmation is cancelled because the
discount amount is incorrect.
DISC IncorrectDiscountAmountCurrency Confirmation is cancelled because the
discount amount has an incorrect
currency.
EXCH IncorrectExchangeRate Confirmation is cancelled because the
exchange rate is incorrect.
FEEE IncorrectFeeOrCommission Confirmation is cancelled because a fee
or commission amount is incorrect.
DQUA IncorrectFinancialInstrumentQuantity Confirmation is cancelled because the
financial instrument quantity is incorrect.
FENA IncorrectFrontEndLoadAmount Confirmation is cancelled because the
front end load amount is incorrect.
GROA IncorrectGrossAmount Confirmation is cancelled because the
gross amount is incorrect.
GROC IncorrectGrossAmountCurrency Confirmation is cancelled because the
gross amount has an incorrect currency.
NETA IncorrectNetAmount Confirmation is cancelled because the
net amount is incorrect.
NETC IncorrectNetAmountCurrency Confirmation is cancelled because the
net amount has an incorrect currency.
OPER IncorrectOperation Confirmation is cancelled because of an
incorrect operation.
MINI IncorrectQuantityUnitsOrCash Confirmation is cancelled because of an
incorrect minimum traded quantity or
cash amount.
DMON IncorrectSettlementAmount Confirmation is cancelled because the
settlement amount is incorrect.
NCRR IncorrectSettlementAmountCurrency Confirmation is cancelled because the
settlement amount has an incorrect
currency.
DDAT IncorrectSettlementDate Confirmation is cancelled because the
settlement date is incorrect.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5190 May 2026
```

