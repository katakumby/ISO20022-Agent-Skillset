---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.2 Organisation40", "66.1.29.2.6 RegistrationCountry <RegnCtry>"]
file_pages: [4891]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.2.6 RegistrationCountry <RegnCtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4891 to 4891.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4891

```text
Datatype: "Max35Text" on page 5403
66.1.29.2.6  RegistrationCountry <RegnCtry>
Presence: [0..1]
Definition: Country in which the organisation is registered.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.29.2.7  RegistrationDate <RegnDt>
Presence: [0..1]
Definition: Date and time at which a given organisation was officially registered.
Datatype: "ISODate" on page 5388
66.1.29.2.8  ModifiedPostalAddress <ModfdPstlAdr>
Presence: [0..*]
Definition: Information related to an address to be inserted, updated or deleted.
ModifiedPostalAddress <ModfdPstlAdr> contains the following ModificationScope34 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4891
   PostalAddress <PstlAdr> [1..1] ± C23 4891
66.1.29.2.8.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Specifies the type of modification to be applied on a set of information.
Datatype: "DataModification1Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
66.1.29.2.8.2  PostalAddress <PstlAdr>
Presence: [1..1]
Definition: Address of the organisation.
Impacted by: C23 "MailingIndicatorRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4891 May 2026
```

