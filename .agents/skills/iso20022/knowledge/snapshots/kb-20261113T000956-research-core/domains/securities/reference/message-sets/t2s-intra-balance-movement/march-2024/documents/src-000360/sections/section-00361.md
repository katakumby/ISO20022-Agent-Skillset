---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.15 Postal Address", "17.1.15.3 PostalAddress1", "17.1.15.3.5 PostCode <PstCd>"]
file_pages: [427]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.15.3.5 PostCode <PstCd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 427 to 427.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 427

```text
Datatype: "Max16Text" on page 496
17.1.15.3.5  PostCode <PstCd>
Presence: [0..1]
Definition: Identifier consisting of a group of letters and/or numbers that is added to a postal address to
assist the sorting of mail.
Datatype: "Max16Text" on page 496
17.1.15.3.6  TownName <TwnNm>
Presence: [0..1]
Definition: Name of a built-up area, with defined boundaries, and a local government.
Datatype: "Max35Text" on page 497
17.1.15.3.7  CountrySubDivision <CtrySubDvsn>
Presence: [0..1]
Definition: Identifies a subdivision of a country for example, state, region, county.
Datatype: "Max35Text" on page 497
17.1.15.3.8  Country <Ctry>
Presence: [1..1]
Definition: Nation with its own government.
Impacted by: C7 "Country"
Datatype: "CountryCode" on page 478
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
17.1.16 Status
17.1.16.1  AcknowledgedAcceptedStatus24Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 428
Or}   Reason <Rsn> [1..*]  428
     Code <Cd> [1..1] ± 428
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 428
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
427 March 2024
```

