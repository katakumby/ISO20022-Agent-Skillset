---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.3 Date Time", "8.1.3.1 DateAndDateTime2Choice", "8.1.3.1.1 Date <Dt>"]
file_pages: [61]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.3.1.1 Date <Dt>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 61 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 61
Or}   DateTime <DtTm> [1..1] DateTime 61
8.1.3.1.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: "ISODate" on page 75
8.1.3.1.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: "ISODateTime" on page 75
8.1.4 Financial Instrument
8.1.4.1  SecurityIdentification19
Definition: Identification of a security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 62
   OtherIdentification <OthrId> [0..*]  62
     Identification <Id> [1..1] Text 62
     Suffix <Sfx> [0..1] Text 62
     Type <Tp> [1..1] ± 63
   Description <Desc> [0..1] Text 63
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
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 61 December 2024
```

