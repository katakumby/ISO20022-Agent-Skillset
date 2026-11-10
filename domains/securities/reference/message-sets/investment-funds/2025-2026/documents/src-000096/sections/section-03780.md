---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.3 IndividualPerson37", "66.1.32.3.13 Citizenship <Ctznsh>", "66.1.32.3.13.1 Nationality <Ntlty>"]
file_pages: [5068]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.3.13.1 Nationality <Ntlty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5068 to 5068.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5068

```text
Citizenship <Ctznsh> contains the following CitizenshipInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Nationality <Ntlty> [1..1] CodeSet C35 5068
   MinorIndicator <MnrInd> [1..1] Indicator 5068
66.1.32.3.13.1  Nationality <Ntlty>
Presence: [1..1]
Definition: Country where a person was born or is legally accepted as belonging to the country.
Impacted by: C35 "ValidationByTable"
Datatype: "NationalityCode" on page 5330
Constraints
• ValidationByTable
Must be a valid nationality.
66.1.32.3.13.2  MinorIndicator <MnrInd>
Presence: [1..1]
Definition: Indicates whether the person is a legal minor. This may depend on the nationality, the
domicile country or the transaction in which the person is involved.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.32.3.14  EmployingCompany <EmplngCpny>
Presence: [0..1]
Definition: Organisation represented by a person, or for which a person works.
Datatype: "Max140Text" on page 5402
66.1.32.3.15  BusinessFunction <BizFctn>
Presence: [0..1]
Definition: Title of the function.
Datatype: "Max35Text" on page 5403
66.1.32.3.16  PoliticallyExposedPerson <PltclyXpsdPrsn>
Presence: [0..1]
Definition: Politically exposed person checks.
Impacted by: C29 "PoliticallyExposedPersonTypeRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5068 May 2026
```

