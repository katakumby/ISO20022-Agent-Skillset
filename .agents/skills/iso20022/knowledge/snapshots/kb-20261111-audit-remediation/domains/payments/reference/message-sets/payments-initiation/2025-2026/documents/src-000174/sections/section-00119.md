---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.8 TrackerData <TrckrData>", "3.4.3.7.8.3 TrackerRecord <TrckrRcrd>", "3.4.3.7.8.3.3 ChargesAmount <ChrgsAmt>"]
file_pages: [180]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.8.3.3 ChargesAmount <ChrgsAmt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 180 to 180.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 180

```text
CodeName Name Definition
DEBT BorneByDebtor All transaction charges are to be borne
by the debtor.
CRED BorneByCreditor All transaction charges are to be borne
by the creditor.
SHAR Shared In a credit transfer context, means that
transaction charges on the sender side
are to be borne by the debtor,
transaction charges on the receiver side
are to be borne by the creditor. In a
direct debit context, means that
transaction charges on the sender side
are to be borne by the creditor,
transaction charges on the receiver side
are to be borne by the debtor.
SLEV FollowingServiceLevel Charges are to be applied following the
rules agreed in the service level and/or
scheme.
3.4.3.7.8.3.3  ChargesAmount <ChrgsAmt>
Presence: [0..1]
Definition: Transaction charges to be paid by the charge bearer.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 585
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.3.7.8.3.4  ExchangeRateData <XchgRateData>
Presence: [0..1]
Definition: Provides details of the rate and the currencies used in the foreign exchange.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 180 March 2026
```

