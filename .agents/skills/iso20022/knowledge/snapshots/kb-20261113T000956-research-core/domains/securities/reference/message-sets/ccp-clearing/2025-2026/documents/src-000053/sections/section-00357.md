---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.6 PartyTextInformation1", "12.1.14.6.3 RegistrationDetails <RegnDtls>"]
file_pages: [450]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.6.3 RegistrationDetails <RegnDtls>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 450 to 450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

```text
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Datatype: Max140Text on page 492
12.1.14.6.3  RegistrationDetails <RegnDtls>
Presence: [0..1]
Definition: Provides information required for the registration.
Datatype: Max350Text on page 493
12.1.14.7  PartyIdentificationAndAccount31
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 450
   AlternateIdentification <AltrnId> [0..1] ± 450
   AdditionalInformation <AddtlInf> [0..1] ± C3 451
   ClearingAccount <ClrAcct> [0..1] ± 451
12.1.14.7.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following elements (see PartyIdentification33Choice on
page 447 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet   'C4 448
Or   ProprietaryIdentification <PrtryId> [1..1] ± 448
Or}   NameAndAddress <NmAndAdr> [1..1]  448
     Name <Nm> [1..1] Text 449
     Address <Adr> [1..1] ± 449
12.1.14.7.2  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 450
```

