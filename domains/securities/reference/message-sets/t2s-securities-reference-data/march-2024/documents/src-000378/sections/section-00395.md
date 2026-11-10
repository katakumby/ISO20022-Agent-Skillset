---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.10 Miscellaneous", "13.1.10.8 RateAndAmountFormat1Choice", "13.1.10.8.3 NotSpecifiedRate <NotSpcfdRate>", "13.1.10.8.3.2 Proprietary <Prtry>"]
file_pages: [488]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.10.8.3.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 488 to 488.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 488

```text
13.1.10.8.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary code to express the type of rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification13" on page 480 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 480
   SchemeName <SchmeNm> [0..1] Text 480
   Issuer <Issr> [1..1] Text 481
13.1.11 Party Identification
13.1.11.1  PartyIdentification136
Definition: Identification of the party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 488
   LEI <LEI> [0..1] IdentifierSet 488
13.1.11.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 489 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 489
Or   ProprietaryIdentification <PrtryId> [1..1] ± 490
Or}   NameAndAddress <NmAndAdr> [1..1] ± 490
13.1.11.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 531
13.1.11.2  SystemPartyIdentification2Choice
Definition: Choice between an identification of a party or a combination of the responsible party
identification and the business identifier.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 488 March 2024
```

