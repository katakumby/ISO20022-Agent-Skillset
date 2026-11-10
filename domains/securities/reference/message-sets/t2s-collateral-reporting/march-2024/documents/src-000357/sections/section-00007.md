---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 colr.001.001.02 CollateralValueQueryV02", "2.4 Message Building Blocks", "2.4.2 CollateralValueQueryDefinition <CollValQryDef>"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 2.4.2 CollateralValueQueryDefinition <CollValQryDef>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader3" on page 57 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 58
   CreationDateTime <CreDtTm> [0..1] DateTime 58
   RequestType <ReqTp> [0..1]  58
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 58
Or     Enquiry <Enqry> [1..1] CodeSet 59
Or}     Proprietary <Prtry> [1..1] ± 59
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 59
   QueryName <QryNm> [0..1] Text 60
2.4.2 CollateralValueQueryDefinition <CollValQryDef>
Presence: [0..1]
Definition: Definition of the collateral query.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.001.001.02 CollateralValueQueryV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
7 March 2024
```

