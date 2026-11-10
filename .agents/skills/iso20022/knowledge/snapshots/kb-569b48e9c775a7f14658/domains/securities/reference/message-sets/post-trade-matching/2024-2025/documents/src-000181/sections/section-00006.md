---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "2.3 Constraints"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2.3 Constraints

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
2.3 Constraints
C1 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails and
PartyContactDetails must not contain information that can be provided in a structured field.
C2 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C4 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C5 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C6 IdentificationUsageRule
The presence of Identification and/or CountryOfResidence is mandatory.
C7 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 Pagination <Pgntn>
Presence: [0..*]
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 289 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 289
   LastPageIndicator <LastPgInd> [1..1] Indicator 289
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 8 February 2025
```

