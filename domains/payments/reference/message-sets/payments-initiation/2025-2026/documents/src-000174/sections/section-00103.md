---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.2 OriginalGroupInformationAndStatus <OrgnlGrpInfAndSts>", "3.4.2.3 OriginalCreationDateTime <OrgnlCreDtTm>"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.2.3 OriginalCreationDateTime <OrgnlCreDtTm>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
Datatype: "Max35Text" on page 609
3.4.2.3  OriginalCreationDateTime <OrgnlCreDtTm>
Presence: [0..1]
Definition: Date and time at which the original message was created.
Datatype: "ISODateTime" on page 603
3.4.2.4  OriginalNumberOfTransactions <OrgnlNbOfTxs>
Presence: [0..1]
Definition: Number of individual transactions contained in the original message.
Datatype: "Max15NumericText" on page 608
3.4.2.5  OriginalControlSum <OrgnlCtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the original message, irrespective of currencies.
Datatype: "DecimalNumber" on page 606
3.4.2.6  GroupStatus <GrpSts>
Presence: [0..1]
Definition: Specifies the status of a group of transactions.
Datatype: "ExternalPaymentGroupStatus1Code" on page 595
3.4.2.7  StatusReasonInformation <StsRsnInf>
Presence: [0..*]
Definition: Provides detailed information on the status reason.
Impacted by: C30 "StatusReasonRule"
StatusReasonInformation <StsRsnInf> contains the following StatusReasonInformation14
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 149
   Reason <Rsn> [0..1]  150
{Or     Code <Cd> [1..1] CodeSet 151
Or}     Proprietary <Prtry> [1..1] Text 151
   AdditionalInformation <AddtlInf> [0..*] Text 151
Constraints
• StatusReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 148 March 2026
```

