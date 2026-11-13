---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.10 InterbankSettlementDate <IntrBkSttlmDt>"]
file_pages: [604]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.10 InterbankSettlementDate <IntrBkSttlmDt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 604 to 604.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 604

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.3.10  InterbankSettlementDate <IntrBkSttlmDt>
Presence: [0..1]
Definition: Date on which the amount of money ceases to be available to the agent that owes it and
when the amount of money becomes available to the agent to which it is due.
Usage: The InterbankSettlementDate is the interbank settlement date of the reversal message, and not
of the original instruction.
Datatype: "ISODate" on page 1239
5.4.3.11  SettlementPriority <SttlmPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the settlement instruction.
Usage: the SettlementPriority is the settlement priority of the reversal message, and not of the original
instruction.
Datatype: "Priority3Code" on page 1236
CodeName Name Definition
URGT Urgent Priority level is urgent (highest priority
possible).
HIGH High Priority level is high.
NORM Normal Priority level is normal.
5.4.3.12  SettlementTimeIndication <SttlmTmIndctn>
Presence: [0..1]
Definition: Provides information on the occurred settlement time of the payment transaction.
SettlementTimeIndication <SttlmTmIndctn> contains the following SettlementDateTimeIndication1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitDateTime <DbtDtTm> [0..1] DateTime 605
   CreditDateTime <CdtDtTm> [0..1] DateTime 605
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
604 March 2026
```

