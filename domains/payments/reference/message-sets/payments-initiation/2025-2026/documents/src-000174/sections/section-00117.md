---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.8 TrackerData <TrckrData>", "3.4.3.7.8.1 ConfirmedDate <ConfdDt>"]
file_pages: [178]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.8.1 ConfirmedDate <ConfdDt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 178 to 178.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 178

```text
3.4.3.7.8.1  ConfirmedDate <ConfdDt>
Presence: [1..1]
Definition: Point in time when an update to the tracking system has been confirmed.
Usage:
This date can be the point in time when an agent provides a pending status update to the tracking
system or when the creditor has been credited and can use the amount of money (as confirmed to the
tracking system by the creditor agent).
ConfirmedDate <ConfdDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 534 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 535
Or}   DateTime <DtTm> [1..1] DateTime 535
3.4.3.7.8.2  ConfirmedAmount <ConfdAmt>
Presence: [1..1]
Definition: Amount of money confirmed to the tracking system by the agent.
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
3.4.3.7.8.3  TrackerRecord <TrckrRcrd>
Presence: [1..*]
Definition: Provides tracker transaction information for a specific agent involved in the transaction chain.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 178 March 2026
```

