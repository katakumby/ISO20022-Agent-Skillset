---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.2 Amount <Amt>"]
file_pages: [320]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.2 Amount <Amt>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 320 to 320.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 320

```text
Impacted by: C2 "ActiveOrHistoricCurrency", C9 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 585
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.4.3.8.9.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Amount <Amt> contains one of the following elements (see "AmountType4Choice" on page 532 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InstructedAmount <InstdAmt> [1..1] Amount C2, C19 532
Or}   EquivalentAmount <EqvtAmt> [1..1]  533
     Amount <Amt> [1..1] Amount C2, C19 533
     CurrencyOfTransfer <CcyOfTrf> [1..1] CodeSet C2 533
4.4.3.8.9.3  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Datatype: "ISODate" on page 603
4.4.3.8.9.4  RequestedCollectionDate <ReqdColltnDt>
Presence: [0..1]
Definition: Date and time at which the creditor requests that the amount of money is to be collected from
the debtor.
Datatype: "ISODate" on page 603
4.4.3.8.9.5  RequestedExecutionDate <ReqdExctnDt>
Presence: [0..1]
Definition: Date at which the initiating party requests the clearing agent to process the payment.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 320 March 2026
```

