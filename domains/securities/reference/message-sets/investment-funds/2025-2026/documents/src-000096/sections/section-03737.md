---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.34 ContactAttributes5", "66.1.30.34.8 LEI <LEI>"]
file_pages: [5023]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.34.8 LEI <LEI>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5023 to 5023.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5023

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.30.34.8  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for the party.
Datatype: "LEIIdentifier" on page 5395
66.1.30.35  Intermediary46
Definition: Identification of a party and its role.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  5023
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 5024
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 5024
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 5024
   Account <Acct> [0..1]  5024
     Identification <Id> [0..1] Text 5025
     AccountServicer <AcctSvcr> [1..1] ± 5025
   WaivedTrailerCommissionIndicator <WvdTrlrComssnInd> [0..1] Indicator 5025
   Role <Role> [0..1] ± 5025
   PrimaryCommunicationAddress <PmryComAdr> [0..*] ± 5025
   SecondaryCommunicationAddress <ScndryComAdr> [0..*] ± 5026
   NameAndAddress <NmAndAdr> [0..1] ± 5026
66.1.30.35.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier for an organisation that is allocated by an institution.
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 5024
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 5024
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5023 May 2026
```

