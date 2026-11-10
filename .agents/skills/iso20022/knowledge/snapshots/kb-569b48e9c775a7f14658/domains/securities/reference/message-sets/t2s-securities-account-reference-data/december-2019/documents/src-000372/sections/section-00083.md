---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.1 MessageComponents", "11.1.4 Miscellaneous", "11.1.4.7 MessageHeader2", "11.1.4.7.3 RequestType <ReqTp>", "11.1.4.7.3.3 Proprietary <Prtry>"]
file_pages: [89]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.1.4.7.3.3 Proprietary <Prtry>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 89 to 89.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 89

```text
11.1.4.7.3.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Request type is in proprietary format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 80 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 80
   SchemeName <SchmeNm> [0..1] Text 80
   Issuer <Issr> [0..1] Text 80
11.1.5 Party Identification
11.1.5.1  PartyIdentification136
Definition: Identification of the party.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 89
   LEI <LEI> [0..1] IdentifierSet 89
11.1.5.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 89 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 90
Or   ProprietaryIdentification <PrtryId> [1..1] ± 90
Or}   NameAndAddress <NmAndAdr> [1..1] ± 90
11.1.5.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 98
11.1.5.2  PartyIdentification120Choice
Definition: Choice between different formats for the identification of a party.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 89 December 2019
```

