---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price"]
file_pages: [506]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22 Price

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 506 to 506.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 506

```text
Datatype: "CountryCode" on page 622
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.1.22 Price
7.1.22.1  TypeOfPrice47Choice
Definition: Choice of format for the type of price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 506
Or}   Proprietary <Prtry> [1..1] ± 506
7.1.22.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of price expressed as an ISO 20022 code.
Datatype: "TypeOfPrice3Code" on page 657
CodeName Name Definition
AVER Average Price is an average execution price.
AVOV AverageOverride Price is an override of the average price.
GREX GrossOfAll Price is a gross execution price. The
price is an all inclusive price, ie,
including all charges, fees, and taxes.
NET2 Net Price is a net price, ie, net only of local
broker's commission, local fees and local
taxes.
NET1 NetOfAll Price is a net price, ie, net of all charges,
fees and taxes.
PARV ParValue Price is equal to the nominal or face
value of the instrument.
RDAV RoundedAverage Price is a rounded average price.
7.1.22.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of price expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 506 February 2025
```

