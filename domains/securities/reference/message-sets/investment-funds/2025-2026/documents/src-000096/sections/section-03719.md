---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.21 RiskLevel2Choice", "66.1.30.21.2 Proprietary <Prtry>"]
file_pages: [5004]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.21.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5004 to 5004.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5004

```text
66.1.30.21.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Risk level expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.30.22  CountryAndResidentialStatusType2
Definition: Country and residential status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Country <Ctry> [1..1] CodeSet C12 5004
   ResidentialStatus <ResdtlSts> [1..1] CodeSet 5004
66.1.30.22.1  Country <Ctry>
Presence: [1..1]
Definition: Country to which the residential status is applicable.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.30.22.2  ResidentialStatus <ResdtlSts>
Presence: [1..1]
Definition: Residential status of the organisation or individual, for example, non-permanent resident.
Datatype: "ResidentialStatus1Code" on page 5357
CodeName Name Definition
RESI Resident Resident.
PRES PermanentResident Permanent resident.
NRES NonResident Non-resident.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5004 May 2026
```

