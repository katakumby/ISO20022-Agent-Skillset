---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.12 PartyIdentificationAndAccount227"]
file_pages: [457]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.12 PartyIdentificationAndAccount227

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 457 to 457.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 457

```text
12.1.14.12  PartyIdentificationAndAccount227
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 457
   AlternateIdentification <AltrnId> [0..1] ± 457
   AdditionalInformation <AddtlInf> [0..1] ± C3 457
   ClearingAccount <ClrAcct> [0..1] ± 458
12.1.14.12.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following elements (see PartyIdentification254Choice on
page 455 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet   'C3 455
Or   ProprietaryIdentification <PrtryId> [1..1] ± 456
Or}   NameAndAddress <NmAndAdr> [1..1]  456
     Name <Nm> [1..1] Text 456
     Address <Adr> [1..1] ± 456
12.1.14.12.2  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see AlternatePartyIdentification4 on
page 445 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 445
   Country <Ctry> [1..1] CodeSet   'C5 445
   AlternateIdentification <AltrnId> [1..1] Text 446
12.1.14.12.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information to a party identification.
Impacted by: C3 AdditonalDetailsGuideline
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 457
```

