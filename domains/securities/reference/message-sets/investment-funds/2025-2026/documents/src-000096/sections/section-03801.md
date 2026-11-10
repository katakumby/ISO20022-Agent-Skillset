---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.16 PoliticallyExposedPerson <PltclyXpsdPrsn>", "66.1.32.7.16.1 PoliticallyExposedPersonType <PltclyXpsdPrsnTp>", "66.1.32.7.16.1.1 Code <Cd>"]
file_pages: [5090]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.16.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5090 to 5090.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5090

```text
PoliticallyExposedPersonType <PltclyXpsdPrsnTp> contains one of the following
PoliticalExposureType2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5090
Or}   Proprietary <Prtry> [1..1] ± 5090
66.1.32.7.16.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of political exposure expressed as a code.
Datatype: "PoliticalExposureType2Code" on page 5342
CodeName Name Definition
NPEX NoPoliticalExposure No political exposure.
YPEX PoliticalExposure Political exposure.
PEXD PoliticalExposureDomestic Political exposure type is domestic.
PEXF PoliticalExposureForeign Political exposure type is foreign.
66.1.32.7.16.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of political exposure expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.32.7.16.2  PoliticallyExposedPersonStatus <PltclyXpsdPrsnSts>
Presence: [0..1]
Definition: Status of the politically exposed person.
PoliticallyExposedPersonStatus <PltclyXpsdPrsnSts> contains one of the following
PoliticallyExposedPersonStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5090
Or}   Proprietary <Prtry> [1..1] ± 5091
66.1.32.7.16.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5090 May 2026
```

