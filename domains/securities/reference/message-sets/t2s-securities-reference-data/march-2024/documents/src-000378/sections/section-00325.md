---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.20 Issuance <Issnc>", "13.1.6.4.20.6 IssuerOrganisation <IssrOrg>", "13.1.6.4.20.6.2 Identification <Id>", "13.1.6.4.20.6.2.2 ProprietaryIdentification <PrtryId>"]
file_pages: [418]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.20.6.2.2 ProprietaryIdentification <PrtryId>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 418 to 418.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 418

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
13.1.6.4.20.6.2.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 478 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 478
   SchemeName <SchmeNm> [0..1] Text 478
   Issuer <Issr> [0..1] Text 478
13.1.6.4.20.6.3  Purpose <Purp>
Presence: [0..1]
Definition: Purpose of the organisation, eg, charity.
Datatype: "Max35Text" on page 534
13.1.6.4.20.6.4  TaxationCountry <TaxtnCtry>
Presence: [0..1]
Definition: Country of taxation of an organisation.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 513
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.1.6.4.20.6.5  RegistrationCountry <RegnCtry>
Presence: [0..1]
Definition: Country in which the organisation is registered.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 513
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 418 March 2024
```

