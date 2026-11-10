---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.17 Structured Postal Address", "37.1.17.1 StructuredLongPostalAddress1", "37.1.17.1.11 PostCodeIdentification <PstCdId>"]
file_pages: [846]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.17.1.11 PostCodeIdentification <PstCdId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 846 to 846.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 846

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
37.1.17.1.11  PostCodeIdentification <PstCdId>
Presence: [1..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 888
37.1.17.1.12  PostOfficeBox <POB>
Presence: [0..1]
Definition: Numbered box in a post office, assigned to a person or organisation, where letters are kept
until called for.
Datatype: "Max16Text" on page 888
37.1.18 System Identification
37.1.18.1  SystemIdentification2Choice
Definition: Information used to identify a cash clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 846
Or}   Country <Ctry> [1..1] CodeSet C3 846
37.1.18.1.1  MarketInfrastructureIdentification <MktInfrstrctrId>
Presence: [1..1]
Definition: Clearing service selected for a transaction.
MarketInfrastructureIdentification <MktInfrstrctrId> contains one of the following elements (see
"MarketInfrastructureIdentification1Choice" on page 822 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 823
Or}   Proprietary <Prtry> [1..1] Text 823
37.1.18.1.2  Country <Ctry>
Presence: [1..1]
Definition: Country in which the system is located.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 851
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 846 February 2025
```

