---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.2 Amount <Amt>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.2 Amount <Amt>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 1223
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
2.4.3.18.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Amount <Amt> contains one of the following elements (see "AmountType4Choice" on page 1166 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InstructedAmount <InstdAmt> [1..1] Amount C2, C12 1166
Or}   EquivalentAmount <EqvtAmt> [1..1]  1167
     Amount <Amt> [1..1] Amount C2, C12 1167
     CurrencyOfTransfer <CcyOfTrf> [1..1] CodeSet C2 1167
2.4.3.18.3  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 1239
2.4.3.18.4  RequestedCollectionDate <ReqdColltnDt>
Presence: [0..1]
Definition: Date and time at which the creditor requests that the amount of money is to be collected from
the debtor.
Datatype: "ISODate" on page 1239
2.4.3.18.5  RequestedExecutionDate <ReqdExctnDt>
Presence: [0..1]
Definition: Date at which the initiating party requests the clearing agent to process the payment.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
49 March 2026
```

