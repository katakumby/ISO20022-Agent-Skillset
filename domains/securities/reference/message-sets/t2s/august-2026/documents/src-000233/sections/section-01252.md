---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["31 reda.010.001.01 SecurityQueryV01", "31.4 Message Building Blocks", "31.4.3 SearchCriteria <SchCrit>", "31.4.3.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [1770]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 31.4.3.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1770 to 1770.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1770

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}     CombinedIdentification <CmbndId> [1..1] ± 1777
   CSD <CSD> [0..1]  1778
{Or     OrganisationIdentification <OrgId> [1..1] ± 1778
Or}     CombinedIdentification <CmbndId> [1..1] ± 1778
31.4.3.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Way(s) of identifying the security.
Impacted by: C4 "DescriptionPresenceRule", C5 "DescriptionUsageRule", C7 "ISINGuideline", C8
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification39" on page 2945 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2946
   OtherIdentification <OthrId> [0..*]  2947
     Identification <Id> [1..1] Text 2947
     Suffix <Sfx> [0..1] Text 2947
     Type <Tp> [1..1] ± 2947
   Description <Desc> [0..1] Text 2947
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1770 August 2026
```

