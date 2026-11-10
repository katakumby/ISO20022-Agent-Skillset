---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["18 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "18.4 Message Building Blocks", "18.4.2 QueryDefinition <QryDef>", "18.4.2.2 SearchCriteria <SchCrit>", "18.4.2.2.7 CreationDateTime <CreDtTm>"]
file_pages: [432]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 18.4.2.2.7 CreationDateTime <CreDtTm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 432 to 432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 432

```text
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
18.4.2.2.7  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Specifies the creation date/time of the intra-balance movement.
CreationDateTime <CreDtTm> contains one of the following DateAndDateTimeSearch5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  432
{Or     FromDate <FrDt> [1..1] Date 433
Or     ToDate <ToDt> [1..1] Date 433
Or     FromToDate <FrToDt> [1..1] ± 433
Or     EqualDate <EQDt> [1..1] Date 433
Or}     NotEqualDate <NEQDt> [1..1] Date 433
Or}   DateTime <DtTm> [1..1]  433
{Or     FromDateTime <FrDtTm> [1..1] DateTime 434
Or     ToDateTime <ToDtTm> [1..1] DateTime 434
Or     FromToDateTime <FrToDtTm> [1..1] ± 434
Or     EqualDateTime <EQDtTm> [1..1] DateTime 434
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 434
18.4.2.2.7.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities 432 August 2026
```

