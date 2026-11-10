---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.5 OriginalTransactionIdentification <OrgnlTxId>"]
file_pages: [34]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.5 OriginalTransactionIdentification <OrgnlTxId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 34 to 34.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 34

```text
Definition: Unique identification, as assigned by the original initiating party, to unambiguously identify
the original transaction.
Datatype: "Max35Text" on page 1246
2.4.3.5  OriginalTransactionIdentification <OrgnlTxId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original first instructing agent, to unambiguously
identify the transaction.
Datatype: "Max35Text" on page 1246
2.4.3.6  OriginalUETR <OrgnlUETR>
Presence: [0..1]
Definition: Universally unique identifier to provide the original end-to-end reference of a payment
transaction.
Datatype: "UUIDv4Identifier" on page 1241
2.4.3.7  TransactionStatus <TxSts>
Presence: [0..1]
Definition: Specifies the status of a transaction, as published in an external payment transaction status
code list.
Datatype: "ExternalPaymentTransactionStatus1Code" on page 1231
2.4.3.8  StatusReasonInformation <StsRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the status reason.
Impacted by: C29 "StatusReasonRule"
StatusReasonInformation <StsRsnInf> contains the following StatusReasonInformation14
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 35
   Reason <Rsn> [0..1]  36
{Or     Code <Cd> [1..1] CodeSet 37
Or}     Proprietary <Prtry> [1..1] Text 37
   AdditionalInformation <AddtlInf> [0..*] Text 37
Constraints
• StatusReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
On Condition
    /Reason/Code is within DataType <<Code>> ValidationRuleNarrative1Code
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
34 March 2026
```

