---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.6 StatusReasonInformation <StsRsnInf>", "3.4.3.7.6.1 Originator <Orgtr>"]
file_pages: [173]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.6.1 Originator <Orgtr>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 173 to 173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 173

```text
StatusReasonInformation <StsRsnInf> contains the following StatusReasonInformation14
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 173
   Reason <Rsn> [0..1]  174
{Or     Code <Cd> [1..1] CodeSet 175
Or}     Proprietary <Prtry> [1..1] Text 175
   AdditionalInformation <AddtlInf> [0..*] Text 175
Constraints
• StatusReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
On Condition
    /Reason/Code is within DataType <<Code>> ValidationRuleNarrative1Code
 And    /Reason is present
 And    /Reason/Code is present
Following Must be True
    /AdditionalInformation[1] Must be present
3.4.3.7.6.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the status.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 173 March 2026
```

