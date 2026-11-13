---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["2 camt.076.001.01 BillingReportRequestV01", "2.4 Message Building Blocks"]
file_pages: [6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 2.4 Message Building Blocks

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 6 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 6

```text
C5 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Defines the characteristics specific to the message, such as the identification or the creation
date and time.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader9" on page 118 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 119
   CreationDateTime <CreDtTm> [0..1] DateTime 119
   RequestType <ReqTp> [0..1]  119
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 119
Or     Enquiry <Enqry> [1..1] CodeSet 119
Or}     Proprietary <Prtry> [1..1] ± 120
2.4.2 SearchCriteria <SchCrit>
Presence: [1..*]
Definition: Defines the criteria to be used to extract the billing data.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.076.001.01 BillingReportRequestV01
Target2-Securities - Billing 6 December 2025
```

