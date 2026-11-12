---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["20 camt.021.001.06 ReturnGeneralBusinessInformationV06", "20.3 Constraints"]
file_pages: [570]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.021.001.06"]
---

# 20.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 570 to 570.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 570

```text
20.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
20.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
20.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader7" on page 814 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 814
   CreationDateTime <CreDtTm> [0..1] DateTime 814
   RequestType <ReqTp> [0..1]  814
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 814
Or     Enquiry <Enqry> [1..1] CodeSet 815
Or}     Proprietary <Prtry> [1..1] ± 815
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 815
   QueryName <QryNm> [0..1] Text 815
20.4.2 ReportOrError <RptOrErr>
Presence: [1..1]
Definition: Report on the Business Information.
Approved by the Payments SEG on 04 February 2025 camt.021.001.06
ReturnGeneralBusinessInformationV06
Cash Management - Maintenance 2024 - 2025 570 February 2025
```

