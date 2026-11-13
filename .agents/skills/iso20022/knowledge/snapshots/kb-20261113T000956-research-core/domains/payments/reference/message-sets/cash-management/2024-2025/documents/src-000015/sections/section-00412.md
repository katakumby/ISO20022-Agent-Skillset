---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["19 camt.020.001.04 GetGeneralBusinessInformationV04", "19.4 Message Building Blocks", "19.4.2 GeneralBusinessInformationQueryDefinition <GnlBizInfQryDef>", "19.4.2.2 GeneralBusinessInformationCriteria <GnlBizInfCrit>", "19.4.2.2.2 NewCriteria <NewCrit>", "19.4.2.2.2.2 SearchCriteria <SchCrit>", "19.4.2.2.2.2.2 Subject <Sbjt>", "19.4.2.2.2.2.2.3 Contain <CT>"]
file_pages: [565]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.020.001.04"]
---

# 19.4.2.2.2.2.2.3 Contain <CT>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 565 to 565.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 565

```text
Datatype: "Max35Text" on page 889
19.4.2.2.2.2.2.3  Contain <CT>
Presence: [1..1]
Definition: Set of characters to be matched to be considered valid.
Datatype: "Max35Text" on page 889
19.4.2.2.2.2.2.4  NotContain <NCT>
Presence: [1..1]
Definition: Set of characters that cannot match to be considered valid.
Datatype: "Max35Text" on page 889
19.4.2.2.2.2.3  Qualifier <Qlfr>
Presence: [0..*]
Definition: Further information about the criticality or importance of a general business information
system.
Qualifier <Qlfr> contains the following InformationQualifierType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IsFormatted <IsFrmtd> [0..1] Indicator 565
   Priority <Prty> [0..1] CodeSet 565
19.4.2.2.2.2.3.1  IsFormatted <IsFrmtd>
Presence: [0..1]
Definition: Indicates whether the information is formatted.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 886):
• Meaning When True: Yes
• Meaning When False: No
19.4.2.2.2.2.3.2  Priority <Prty>
Presence: [0..1]
Definition: Priority of the information.
Datatype: "Priority1Code" on page 871
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
LOWW Low Priority level is low.
19.4.2.2.2.3  ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected report.
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 565 February 2025
```

