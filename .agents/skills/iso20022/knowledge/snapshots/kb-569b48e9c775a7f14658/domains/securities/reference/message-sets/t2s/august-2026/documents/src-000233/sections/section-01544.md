---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["44 reda.024.001.01 CollateralValueCreationRequestV01", "44.4 Message Building Blocks", "44.4.2 CollateralValue <CollVal>", "44.4.2.1 SecurityIdentification <SctyId>"]
file_pages: [2167]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 44.4.2.1 SecurityIdentification <SctyId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2167 to 2167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2167

```text
44.4.2.1  SecurityIdentification <SctyId>
Presence: [1..1]
Definition: Identification of a security by an ISIN.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C9 "ISINGuideline", C10
"ISINPresenceRule", C11 "OtherIdentificationPresenceRule"
SecurityIdentification <SctyId> contains the following elements (see "SecurityIdentification19" on
page 2951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2952
   OtherIdentification <OthrId> [0..*]  2952
     Identification <Id> [1..1] Text 2952
     Suffix <Sfx> [0..1] Text 2952
     Type <Tp> [1..1] ± 2952
   Description <Desc> [0..1] Text 2953
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
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities 2167 August 2026
```

