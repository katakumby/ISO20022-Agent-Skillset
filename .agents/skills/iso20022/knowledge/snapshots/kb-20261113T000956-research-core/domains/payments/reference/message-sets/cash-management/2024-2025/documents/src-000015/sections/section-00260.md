---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["8 camt.009.001.08 GetLimitV08", "8.4 Message Building Blocks", "8.4.2 LimitQueryDefinition <LmtQryDef>", "8.4.2.2 LimitCriteria <LmtCrit>", "8.4.2.2.2 NewCriteria <NewCrit>", "8.4.2.2.2.2 SearchCriteria <SchCrit>", "8.4.2.2.2.2.8 UsedPercentage <UsdPctg>", "8.4.2.2.2.2.8.1 From <Fr>"]
file_pages: [384]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.009.001.08"]
---

# 8.4.2.2.2.2.8.1 From <Fr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 384 to 384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 384

```text
UsedPercentage <UsdPctg> contains one of the following PercentageRange1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   From <Fr> [1..1]  384
     BoundaryRate <BdryRate> [1..1] Rate 384
     Included <Incl> [1..1] Indicator 384
Or   To <To> [1..1]  385
     BoundaryRate <BdryRate> [1..1] Rate 385
     Included <Incl> [1..1] Indicator 385
Or   FromTo <FrTo> [1..1]  385
     From <Fr> [1..1]  385
       BoundaryRate <BdryRate> [1..1] Rate 386
       Included <Incl> [1..1] Indicator 386
     To <To> [1..1]  386
       BoundaryRate <BdryRate> [1..1] Rate 386
       Included <Incl> [1..1] Indicator 386
Or   Equal <EQ> [1..1] Rate 387
Or}   NotEqual <NEQ> [1..1] Rate 387
8.4.2.2.2.2.8.1  From <Fr>
Presence: [1..1]
Definition: Lower boundary of a range of percentage rates.
From <Fr> contains the following PercentageRangeBoundary1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryRate <BdryRate> [1..1] Rate 384
   Included <Incl> [1..1] Indicator 384
8.4.2.2.2.2.8.1.1  BoundaryRate <BdryRate>
Presence: [1..1]
Definition: Percentage rate of the range limit.
Datatype: "PercentageRate" on page 887
8.4.2.2.2.2.8.1.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary percentage rate is included in the range of percentage rates.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 886):
Approved by the Payments SEG on 04 February 2025 camt.009.001.08 GetLimitV08
Cash Management - Maintenance 2024 - 2025 384 February 2025
```

