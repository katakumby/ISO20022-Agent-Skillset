---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.1 StatusIdentification <StsId>"]
file_pages: [172]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.1 StatusIdentification <StsId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 172 to 172.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 172

```text
3.4.3.7.1  StatusIdentification <StsId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the reported status.
Usage: The instructing party is the party sending the status message and not the party that sent the
original instruction that is being reported on.
Datatype: "Max35Text" on page 609
3.4.3.7.2  OriginalInstructionIdentification <OrgnlInstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original instructing party for the original instructed
party, to unambiguously identify the original instruction.
Datatype: "Max35Text" on page 609
3.4.3.7.3  OriginalEndToEndIdentification <OrgnlEndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the original initiating party, to unambiguously identify
the original transaction.
Datatype: "Max35Text" on page 609
3.4.3.7.4  OriginalUETR <OrgnlUETR>
Presence: [0..1]
Definition: Universally unique identifier to provide the original end-to-end reference of a payment
transaction.
Datatype: "UUIDv4Identifier" on page 605
3.4.3.7.5  TransactionStatus <TxSts>
Presence: [0..1]
Definition: Specifies the status of a transaction, as published in an external payment transaction status
code list.
Datatype: "ExternalPaymentTransactionStatus1Code" on page 596
3.4.3.7.6  StatusReasonInformation <StsRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the status reason.
Impacted by: C30 "StatusReasonRule"
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 172 March 2026
```

