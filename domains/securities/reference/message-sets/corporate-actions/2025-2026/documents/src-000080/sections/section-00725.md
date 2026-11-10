---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.18 InformationTypeFormat4Choice"]
file_pages: [918]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.18 InformationTypeFormat4Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 918 to 918.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 918

```text
16.1.15.18  InformationTypeFormat4Choice
Definition: Choice between a standard code or proprietary code to specify the information type format
required.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 918
Or}   Proprietary <Prtry> [1..1] ± 918
16.1.15.18.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the information type required.
Datatype: "CorporateActionInformationType1Code" on page 1194
CodeName Name Definition
CONF ConferenceCall Information is about an informal call
when an issuer, trustee, agent wishes to
talk to note holders to discuss a certain
issue or potential change to the notes;
nothing said being binding.
16.1.15.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the information type.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.19  BidRangeType1Choice
Definition: Bid range type as a choice of a defined coded value or a proprietary value.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 918
Or}   Proprietary <Prtry> [1..1] ± 919
16.1.15.19.1  Code <Cd>
Presence: [1..1]
Definition: Bid range type expressed as a code value.
Datatype: "BidRangeType1Code" on page 1165
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 918 February 2026
```

