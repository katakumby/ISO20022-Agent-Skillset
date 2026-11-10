---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["14 camt.076.001.01 BillingReportRequestV01", "14.4 Message Building Blocks"]
file_pages: [235]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 14.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 235 to 235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 235

```text
C5 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
14.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
14.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Defines the characteristics specific to the message, such as the identification or the creation
date and time.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader9" on page 3046 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3046
   CreationDateTime <CreDtTm> [0..1] DateTime 3046
   RequestType <ReqTp> [0..1]  3047
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 3047
Or     Enquiry <Enqry> [1..1] CodeSet 3047
Or}     Proprietary <Prtry> [1..1] ± 3047
14.4.2 SearchCriteria <SchCrit>
Presence: [1..*]
Definition: Defines the criteria to be used to extract the billing data.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.076.001.01 BillingReportRequestV01
Target2-Securities 235 August 2026
```

