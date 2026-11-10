---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.5 PartyIdentification33Choice", "12.1.14.5.3 NameAndAddress <NmAndAdr>", "12.1.14.5.3.1 Name <Nm>"]
file_pages: [449]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.5.3.1 Name <Nm>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 449 to 449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 449

```text
12.1.14.5.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: Max70Text on page 493
12.1.14.5.3.2  Address <Adr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Address <Adr> contains the following elements (see PostalAddress2 on page 467 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StreetName <StrtNm> [0..1] Text 467
   PostCodeIdentification <PstCdId> [1..1] Text 467
   TownName <TwnNm> [1..1] Text 467
   CountrySubDivision <CtrySubDvsn> [0..1] Text 467
   Country <Ctry> [1..1] CodeSet   'C5 467
12.1.14.6  PartyTextInformation1
Definition: Provides additional information regarding the party, for example, the contact unit or person
responsible for the transaction identified in the message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeclarationDetails <DclrtnDtls> [0..1] Text 449
   PartyContactDetails <PtyCtctDtls> [0..1] Text 449
   RegistrationDetails <RegnDtls> [0..1] Text 450
Constraints
• AdditonalDetailsGuideline
(Guideline)
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
12.1.14.6.1  DeclarationDetails <DclrtnDtls>
Presence: [0..1]
Definition: Provides declaration details narrative relative to the party.
Datatype: Max350Text on page 493
12.1.14.6.2  PartyContactDetails <PtyCtctDtls>
Presence: [0..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 449
```

