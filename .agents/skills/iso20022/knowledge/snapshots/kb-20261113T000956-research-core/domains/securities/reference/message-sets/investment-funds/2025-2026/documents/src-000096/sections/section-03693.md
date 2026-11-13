---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.14 FATCAStatus2", "66.1.30.14.1 Type <Tp>", "66.1.30.14.1.2 Proprietary <Prtry>"]
file_pages: [4961]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.14.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4961 to 4961.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4961

```text
CodeName Name Definition
F103 FATCA103 Account holder type is a non-
participating financial institution.
F104 FATCA104 Account holder type is a specified US
person.
F105 FATCA105 Account holder type is a direct reporting
non-financial foreign entity (NFFE).
F201 FATCA201 Account pool reporting type is a
recalcitrant account holder with US
indicia.
F202 FATCA202 Account pool reporting type is a
recalcitrant account holder without US
indicia.
F203 FATCA203 Account pool reporting type is a dormant
account.
F204 FATCA204 Account pool reporting type is a non-
participating foreign financial institution.
F205 FATCA205 Account pool reporting type is a
recalcitrant account holder that is a US
person.
F206 FATCA206 Account pool reporting type is
recalcitrant account holder that is a
passive non-financial foreign entity
(NFFE).
66.1.30.14.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Foreign Account Tax Compliance Act (FATCA) status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.30.14.2  Source <Src>
Presence: [0..1]
Definition: Source of the Foreign Account Tax Compliance Act (FATCA) status.
Source <Src> contains one of the following FATCASource1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4962
Or}   Proprietary <Prtry> [1..1] ± 4962
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4961 May 2026
```

