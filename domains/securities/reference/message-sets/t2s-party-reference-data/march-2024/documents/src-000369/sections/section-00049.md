---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 reda.017.001.02 PartyReportV02", "5.4 Message Building Blocks", "5.4.2 ReportOrError <RptOrErr>", "5.4.2.1 PartyReport <PtyRpt>", "5.4.2.1.2 PartyOrError <PtyOrErr>", "5.4.2.1.2.2 BusinessError <BizErr>", "5.4.2.1.2.2.1 Error <Err>", "5.4.2.1.2.2.1.1 Code <Cd>"]
file_pages: [59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 5.4.2.1.2.2.1.1 Code <Cd>

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 59 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 59

```text
Error <Err> contains one of the following ErrorHandling2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 59
Or}   Proprietary <Prtry> [1..1] Text 59
5.4.2.1.2.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specification of the error, in coded form.
Datatype: "ErrorHandling1Code" on page 181
CodeName Name Definition
X020 DataNotYetAvailable Specifies the error code when the data
requested are not yet available.
X030 MessageSizeLimitExceeded Specifies the error code when the data
requested generates a message size
that exceed the processing capacity.
X050 DataNotAvailable Specifies the error code when the data
requested have not been found.
5.4.2.1.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specification of the error, in free format.
Datatype: "Max35Text" on page 188
5.4.2.1.2.2.2  Description <Desc>
Presence: [0..1]
Definition: Specification of the error, in free format.
Datatype: "Max140Text" on page 187
5.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Operational error resulting from a rejection.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  60
{Or     Code <Cd> [1..1] CodeSet 60
Or}     Proprietary <Prtry> [1..1] Text 60
   Description <Desc> [0..1] Text 60
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.017.001.02 PartyReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
59 March 2024
```

