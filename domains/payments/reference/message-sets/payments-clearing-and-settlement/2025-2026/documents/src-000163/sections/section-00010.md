---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2.1 OriginalMessageIdentification <OrgnlMsgId>"]
file_pages: [21]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.2.1 OriginalMessageIdentification <OrgnlMsgId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 21 to 21.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 21

```text
Impacted by: C28 "StatusReasonInformationRule", C19 "NumberOfTransactionPerStatusGuideline"
OriginalGroupInformationAndStatus <OrgnlGrpInfAndSts> contains the following
OriginalGroupHeader22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMessageIdentification <OrgnlMsgId> [1..1] Text 21
   OriginalMessageNameIdentification <OrgnlMsgNmId> [1..1] Text 21
   OriginalCreationDateTime <OrgnlCreDtTm> [0..1] DateTime 22
   OriginalNumberOfTransactions <OrgnlNbOfTxs> [0..1] Text 22
   OriginalControlSum <OrgnlCtrlSum> [0..1] Quantity 22
   GroupStatus <GrpSts> [0..1] CodeSet 22
   StatusReasonInformation <StsRsnInf> [0..*]  C29 22
     Originator <Orgtr> [0..1] ± 23
     Reason <Rsn> [0..1]  24
{Or       Code <Cd> [1..1] CodeSet 25
Or}       Proprietary <Prtry> [1..1] Text 25
     AdditionalInformation <AddtlInf> [0..*] Text 25
   NumberOfTransactionsPerStatus <NbOfTxsPerSts> [0..*] ± 25
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
2.4.2.1  OriginalMessageIdentification <OrgnlMsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the original instructing party, to unambiguously
identify the original message.
Datatype: "Max35Text" on page 1246
2.4.2.2  OriginalMessageNameIdentification <OrgnlMsgNmId>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
21 March 2026
```

