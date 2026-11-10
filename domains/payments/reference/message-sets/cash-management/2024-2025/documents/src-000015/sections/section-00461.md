---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks", "23.4.2 ReceiptDetails <RctDtls>", "23.4.2.3 RequestHandling <ReqHdlg>", "23.4.2.3.2 StatusReason <StsRsn>"]
file_pages: [620]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4.2.3.2 StatusReason <StsRsn>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 620 to 620.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 620

```text
Datatype: "Max35Text" on page 889
23.4.2.3.2  StatusReason <StsRsn>
Presence: [0..1]
Definition: Provides detailed information on the status reason.
Impacted by: C5 "StatusReasonRule"
StatusReason <StsRsn> contains the following StatusReasonInformation14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Originator <Orgtr> [0..1] ± 620
   Reason <Rsn> [0..1]  621
{Or     Code <Cd> [1..1] CodeSet 622
Or}     Proprietary <Prtry> [1..1] Text 622
   AdditionalInformation <AddtlInf> [0..*] Text 622
Constraints
• StatusReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
On Condition
    /Reason/Code is within DataType <<Code>> ValidationRuleNarrative1Code
 And    /Reason is present
 And    /Reason/Code is present
Following Must be True
    /AdditionalInformation[1] Must be present
23.4.2.3.2.1  Originator <Orgtr>
Presence: [0..1]
Definition: Party that issues the status.
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 620 February 2025
```

