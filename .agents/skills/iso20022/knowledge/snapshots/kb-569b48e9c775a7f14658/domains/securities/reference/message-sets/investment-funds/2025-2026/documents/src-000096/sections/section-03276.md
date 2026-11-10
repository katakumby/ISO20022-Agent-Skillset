---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.12 FinancialInstrument71", "66.1.18.12.1 Identification <Id>"]
file_pages: [4513]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.12.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4513 to 4513.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4513

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± C3, C4,
C5, C6,
C7
4513
   ShortName <ShrtNm> [0..1] Text 4514
   Name <Nm> [0..1] Text 4514
   SupplementaryIdentification <SplmtryId> [0..1] Text 4514
   ClassType <ClssTp> [0..1] Text 4514
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4514
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4515
   ProductGroup <PdctGrp> [0..1] Text 4515
66.1.18.12.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the security, typically by an ISIN.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C5 "ISINGuideline", C6
"ISINPresenceRule", C7 "OtherIdentificationPresenceRule"
Identification <Id> contains the following elements (see "SecurityIdentification19" on page 4515 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 4516
   OtherIdentification <OthrId> [0..*]  4516
     Identification <Id> [1..1] Text 4516
     Suffix <Sfx> [0..1] Text 4517
     Type <Tp> [1..1] ± 4517
   Description <Desc> [0..1] Text 4517
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4513 May 2026
```

