---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["2 reda.024.001.01 CollateralValueCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 CollateralValue <CollVal>", "2.4.2.1 SecurityIdentification <SctyId>"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 2.4.2.1 SecurityIdentification <SctyId>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
2.4.2.1  SecurityIdentification <SctyId>
Presence: [1..1]
Definition: Identification of a security by an ISIN.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C9 "ISINGuideline", C10
"ISINPresenceRule", C11 "OtherIdentificationPresenceRule"
SecurityIdentification <SctyId> contains the following elements (see "SecurityIdentification19" on
page 63 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 64
   OtherIdentification <OthrId> [0..*]  64
     Identification <Id> [1..1] Text 64
     Suffix <Sfx> [0..1] Text 64
     Type <Tp> [1..1] ± 64
   Description <Desc> [0..1] Text 65
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
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 10 May 2025
```

