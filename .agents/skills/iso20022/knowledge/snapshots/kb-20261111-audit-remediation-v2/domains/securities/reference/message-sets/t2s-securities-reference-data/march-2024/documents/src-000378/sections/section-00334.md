---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.22 SpreadAndBenchmarkCurve <SprdAndBchmkCrv>", "13.1.6.4.22.2 BenchmarkIdentification <BchmkId>"]
file_pages: [427]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.22.2 BenchmarkIdentification <BchmkId>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 427 to 427.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 427

```text
Definition: Either a swap spread or spread to benchmark depending upon order type. In case of a
spread to benchmark, the price offset is expressed in terms of basis points relative to a benchmark -
this can be a positive or a negative spread. In case of a swap spread, the price offset is a target spread
for a swap.
Datatype: "DecimalNumber" on page 532
13.1.6.4.22.2  BenchmarkIdentification <BchmkId>
Presence: [0..1]
Definition: Identification of a security by an ISIN.
Impacted by: C1 "DescriptionPresenceRule", C2 "DescriptionUsageRule", C3 "ISINGuideline", C4
"ISINPresenceRule", C5 "OtherIdentificationPresenceRule"
BenchmarkIdentification <BchmkId> contains the following elements (see "SecurityIdentification39"
on page 474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 475
   OtherIdentification <OthrId> [0..*]  475
     Identification <Id> [1..1] Text 475
     Suffix <Sfx> [0..1] Text 475
     Type <Tp> [1..1] ± 475
   Description <Desc> [0..1] Text 476
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 427 March 2024
```

