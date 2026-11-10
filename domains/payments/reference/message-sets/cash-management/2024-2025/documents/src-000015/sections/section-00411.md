---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["19 camt.020.001.04 GetGeneralBusinessInformationV04", "19.4 Message Building Blocks", "19.4.2 GeneralBusinessInformationQueryDefinition <GnlBizInfQryDef>", "19.4.2.2 GeneralBusinessInformationCriteria <GnlBizInfCrit>", "19.4.2.2.2 NewCriteria <NewCrit>", "19.4.2.2.2.2 SearchCriteria <SchCrit>", "19.4.2.2.2.2.1 Reference <Ref>"]
file_pages: [564]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.020.001.04"]
---

# 19.4.2.2.2.2.1 Reference <Ref>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 564 to 564.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 564

```text
SearchCriteria <SchCrit> contains the following GeneralBusinessInformationSearchCriteria1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [0..*] Text 564
   Subject <Sbjt> [0..*]  564
{Or     Equal <EQ> [1..1] Text 564
Or     NotEqual <NEQ> [1..1] Text 564
Or     Contain <CT> [1..1] Text 565
Or}     NotContain <NCT> [1..1] Text 565
   Qualifier <Qlfr> [0..*]  565
     IsFormatted <IsFrmtd> [0..1] Indicator 565
     Priority <Prty> [0..1] CodeSet 565
19.4.2.2.2.2.1  Reference <Ref>
Presence: [0..*]
Definition: Unique and unambiguous reference assigned to a general business information system.
Datatype: "Max35Text" on page 889
19.4.2.2.2.2.2  Subject <Sbjt>
Presence: [0..*]
Definition: Subject line of an item of general business information, summarizing the topic and intended
destination of the information.
Subject <Sbjt> contains one of the following CharacterSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] Text 564
Or   NotEqual <NEQ> [1..1] Text 564
Or   Contain <CT> [1..1] Text 565
Or}   NotContain <NCT> [1..1] Text 565
19.4.2.2.2.2.2.1  Equal <EQ>
Presence: [1..1]
Definition: Exact set of characters to be matched to be considered valid.
Datatype: "Max35Text" on page 889
19.4.2.2.2.2.2.2  NotEqual <NEQ>
Presence: [1..1]
Definition: Exact set of characters that cannot match to be considered valid.
Approved by the Payments SEG on 04 February 2025 camt.020.001.04
GetGeneralBusinessInformationV04
Cash Management - Maintenance 2024 - 2025 564 February 2025
```

