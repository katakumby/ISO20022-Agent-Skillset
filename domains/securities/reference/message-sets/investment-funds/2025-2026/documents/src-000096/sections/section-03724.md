---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.24 PartyIdentificationAndAccount194", "66.1.30.24.1 Identification <Id>"]
file_pages: [5010]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.24.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5010 to 5010.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5010

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5010
   LEI <LEI> [0..1] IdentifierSet 5010
   AlternateIdentification <AltrnId> [0..1] ± 5010
   SafekeepingAccount <SfkpgAcct> [0..1] ± 5010
   ProcessingDate <PrcgDt> [0..1] ± 5011
   ProcessingIdentification <PrcgId> [0..1] Text 5011
   AdditionalInformation <AddtlInf> [0..1] ± C4 5011
66.1.30.24.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification123Choice" on
page 5012 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 5012
Or   ProprietaryIdentification <PrtryId> [1..1] ± 5012
Or}   NameAndAddress <NmAndAdr> [1..1] ± 5012
66.1.30.24.2  LEI <LEI>
Presence: [0..1]
Definition: Legal Entity Identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
66.1.30.24.3  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for the party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 5044 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 5044
   Country <Ctry> [1..1] CodeSet C12 5044
   AlternateIdentification <AltrnId> [1..1] Text 5045
66.1.30.24.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5010 May 2026
```

