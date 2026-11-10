---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["24 colr.001.001.02 CollateralValueQueryV02", "24.4 Message Building Blocks", "24.4.2 CollateralValueQueryDefinition <CollValQryDef>"]
file_pages: [581]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 24.4.2 CollateralValueQueryDefinition <CollValQryDef>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 581 to 581.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 581

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader3" on page 2995 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2995
   CreationDateTime <CreDtTm> [0..1] DateTime 2995
   RequestType <ReqTp> [0..1]  2995
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 2995
Or     Enquiry <Enqry> [1..1] CodeSet 2996
Or}     Proprietary <Prtry> [1..1] ± 2996
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 2996
   QueryName <QryNm> [0..1] Text 2997
24.4.2 CollateralValueQueryDefinition <CollValQryDef>
Presence: [0..1]
Definition: Definition of the collateral query.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.001.001.02 CollateralValueQueryV02
Target2-Securities 581 August 2026
```

