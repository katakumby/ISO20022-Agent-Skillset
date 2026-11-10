---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2.3 OriginalCreationDateTime <OrgnlCreDtTm>"]
file_pages: [22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.2.3 OriginalCreationDateTime <OrgnlCreDtTm>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 22 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
Definition: Specifies the original message name identifier to which the message refers.
Datatype: "Max35Text" on page 1246
2.4.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Date and time at which the original message was created.
Datatype: "ISODateTime" on page 1239
2.4.2.4  OriginalNumberOfTransactions <OrgnlNbOfTxs>
Presence: [0..1]
Definition: Number of individual transactions contained in the original message.
Datatype: "Max15NumericText" on page 1244
2.4.2.5  OriginalControlSum <OrgnlCtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the original message, irrespective of currencies.
Datatype: "DecimalNumber" on page 1242
2.4.2.6  GroupStatus <GrpSts>
Presence: [0..1]
Definition: Specifies the status of a group of transactions.
Datatype: "ExternalPaymentGroupStatus1Code" on page 1231
2.4.2.7  StatusReasonInformation <StsRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the status reason.
Impacted by: C29 "StatusReasonRule"
StatusReasonInformation <StsRsnInf> contains the following StatusReasonInformation14
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 23
   Reason <Rsn> [0..1]  24
{Or     Code <Cd> [1..1] CodeSet 25
Or}     Proprietary <Prtry> [1..1] Text 25
   AdditionalInformation <AddtlInf> [0..*] Text 25
Constraints
• StatusReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
22 March 2026
```

