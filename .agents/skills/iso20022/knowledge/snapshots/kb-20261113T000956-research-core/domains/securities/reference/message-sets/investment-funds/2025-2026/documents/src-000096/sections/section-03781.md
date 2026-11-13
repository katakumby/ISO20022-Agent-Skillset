---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.3 IndividualPerson37", "66.1.32.3.16 PoliticallyExposedPerson <PltclyXpsdPrsn>", "66.1.32.3.16.1 PoliticallyExposedPersonType <PltclyXpsdPrsnTp>"]
file_pages: [5069]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.3.16.1 PoliticallyExposedPersonType <PltclyXpsdPrsnTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5069 to 5069.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5069

```text
PoliticallyExposedPerson <PltclyXpsdPrsn> contains the following PoliticallyExposedPerson1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PoliticallyExposedPersonType <PltclyXpsdPrsnTp> [1..1]  5069
{Or     Code <Cd> [1..1] CodeSet 5069
Or}     Proprietary <Prtry> [1..1] ± 5070
   PoliticallyExposedPersonStatus <PltclyXpsdPrsnSts> [0..1]  5070
{Or     Code <Cd> [1..1] CodeSet 5070
Or}     Proprietary <Prtry> [1..1] ± 5071
Constraints
• PoliticallyExposedPersonTypeRule
If PoliticallyExposedPersonType/Code is 'NoPoliticalExposure' (NPEX) then
PoliticallyExposedPersonStatus is not allowed.
On Condition
    /PoliticallyExposedPersonType/Code is equal to value 'NoPoliticalExposure'
Following Must be True
    /PoliticallyExposedPersonStatus Must be absent
66.1.32.3.16.1  PoliticallyExposedPersonType <PltclyXpsdPrsnTp>
Presence: [1..1]
Definition: Specifies if due diligence checks on the political exposure of the investor have been carried
out. (A politically exposed person is someone who has been entrusted with a prominent public function,
or an individual who is closely related to such a person.)
PoliticallyExposedPersonType <PltclyXpsdPrsnTp> contains one of the following
PoliticalExposureType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5069
Or}   Proprietary <Prtry> [1..1] ± 5070
66.1.32.3.16.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of political exposure expressed as a code.
Datatype: "PoliticalExposureType2Code" on page 5342
CodeName Name Definition
NPEX NoPoliticalExposure No political exposure.
YPEX PoliticalExposure Political exposure.
PEXD PoliticalExposureDomestic Political exposure type is domestic.
PEXF PoliticalExposureForeign Political exposure type is foreign.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5069 May 2026
```

