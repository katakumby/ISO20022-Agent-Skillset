---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "75.4 Message Building Blocks", "75.4.1 QueryDefinition <QryDef>", "75.4.1.2 SearchCriteria <SchCrit>", "75.4.1.2.7 CreationDateTime <CreDtTm>", "75.4.1.2.7.2 DateTime <DtTm>", "75.4.1.2.7.2.1 FromDateTime <FrDtTm>"]
file_pages: [2650]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 75.4.1.2.7.2.1 FromDateTime <FrDtTm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2650 to 2650.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2650

```text
DateTime <DtTm> contains one of the following DateTimeSearch2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 2650
Or   ToDateTime <ToDtTm> [1..1] DateTime 2650
Or   FromToDateTime <FrToDtTm> [1..1] ± 2650
Or   EqualDateTime <EQDtTm> [1..1] DateTime 2650
Or}   NotEqualDateTime <NEQDtTm> [1..1] DateTime 2650
75.4.1.2.7.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODateTime" on page 3320
75.4.1.2.7.2.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODateTime" on page 3320
75.4.1.2.7.2.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on
page 2916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 2916
   ToDateTime <ToDtTm> [1..1] DateTime 2916
75.4.1.2.7.2.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 3320
75.4.1.2.7.2.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities 2650 August 2026
```

