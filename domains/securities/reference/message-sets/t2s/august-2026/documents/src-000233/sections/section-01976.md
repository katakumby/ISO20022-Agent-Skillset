---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "77.4 Message Building Blocks", "77.4.1 QueryDefinition <QryDef>", "77.4.1.2 SearchCriteria <SchCrit>", "77.4.1.2.7 CreationDateTime <CreDtTm>"]
file_pages: [2696]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 77.4.1.2.7 CreationDateTime <CreDtTm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2696 to 2696.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2696

```text
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
77.4.1.2.7  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Specifies the creation date/time of the settlement instruction or the intra-position movement.
CreationDateTime <CreDtTm> contains one of the following DateAndDateTimeSearch5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2696
{Or     FromDate <FrDt> [1..1] Date 2697
Or     ToDate <ToDt> [1..1] Date 2697
Or     FromToDate <FrToDt> [1..1] ± 2697
Or     EqualDate <EQDt> [1..1] Date 2697
Or}     NotEqualDate <NEQDt> [1..1] Date 2697
Or}   DateTime <DtTm> [1..1]  2697
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2698
Or     ToDateTime <ToDtTm> [1..1] DateTime 2698
Or     FromToDateTime <FrToDtTm> [1..1] ± 2698
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2698
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2698
77.4.1.2.7.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities 2696 August 2026
```

