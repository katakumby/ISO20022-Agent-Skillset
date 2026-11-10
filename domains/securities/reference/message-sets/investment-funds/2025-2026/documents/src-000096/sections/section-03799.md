---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.13 ModifiedCitizenship <ModfdCtznsh>", "66.1.32.7.13.1 ModificationScopeIndication <ModScpIndctn>"]
file_pages: [5088]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.13.1 ModificationScopeIndication <ModScpIndctn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5088 to 5088.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5088

```text
ModifiedCitizenship <ModfdCtznsh> contains the following ModificationScope39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 5088
   Citizenship <Ctznsh> [1..1]  5088
     Nationality <Ntlty> [1..1] CodeSet C35 5088
     MinorIndicator <MnrInd> [1..1] Indicator 5088
66.1.32.7.13.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied on a set of information.
Datatype: "DataModification2Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
DELT DeleteDataSet Delete an existing set of data.
66.1.32.7.13.2  Citizenship <Ctznsh>
Presence: [1..1]
Definition: Nationality and legal status (minor or major).
Citizenship <Ctznsh> contains the following CitizenshipInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Nationality <Ntlty> [1..1] CodeSet C35 5088
   MinorIndicator <MnrInd> [1..1] Indicator 5088
66.1.32.7.13.2.1  Nationality <Ntlty>
Presence: [1..1]
Definition: Country where a person was born or is legally accepted as belonging to the country.
Impacted by: C35 "ValidationByTable"
Datatype: "NationalityCode" on page 5330
Constraints
• ValidationByTable
Must be a valid nationality.
66.1.32.7.13.2.2  MinorIndicator <MnrInd>
Presence: [1..1]
Definition: Indicates whether the person is a legal minor. This may depend on the nationality, the
domicile country or the transaction in which the person is involved.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5088 May 2026
```

