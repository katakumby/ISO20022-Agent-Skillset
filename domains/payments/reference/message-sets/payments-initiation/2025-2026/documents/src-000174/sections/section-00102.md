---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.2 OriginalGroupInformationAndStatus <OrgnlGrpInfAndSts>", "3.4.2.1 OriginalMessageIdentification <OrgnlMsgId>"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.2.1 OriginalMessageIdentification <OrgnlMsgId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
OriginalGroupInformationAndStatus <OrgnlGrpInfAndSts> contains the following
OriginalGroupHeader22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 147
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 147
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 148
   OriginalNumberOfTransactions <OrgnlNbOfTxs> [0..1] Text 148
   OriginalControlSum <OrgnlCtrlSum> [0..1] Quantity 148
   GroupStatus <GrpSts> [0..1] CodeSet 148
   StatusReasonInformation <StsRsnInf> [0..*]  C30 148
     Originator <Orgtr> [0..1] ± 149
     Reason <Rsn> [0..1]  150
{Or       Code <Cd> [1..1] CodeSet 151
Or}       Proprietary <Prtry> [1..1] Text 151
     AdditionalInformation <AddtlInf> [0..*] Text 151
   NumberOfTransactionsPerStatus <NbOfTxsPerSts> [0..*] ± 151
Constraints
• NumberOfTransactionPerStatusGuideline
OriginalGroupInformationAndStatus/NumberOfTransactionsPerStatus should only be present if
GroupStatus equals 'PART'.
• StatusReasonInformationRule
If GroupStatus is present and is different from RJCT or PDNG then StatusReasonInformation/
AdditionalInformation must be absent.
On Condition
    /GroupStatus is present
 And    /GroupStatus is not within DataType <<Code>> 
ValidationRulePendingAndRejected1Code
Following Must be True
    /StatusReasonInformation[*]/AdditionalInformation[*] Must be absent
3.4.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original instructing party, to unambiguously
identify the original message.
Datatype: "Max35Text" on page 609
3.4.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Definition: Specifies the original message name identifier to which the message refers.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 147 March 2026
```

