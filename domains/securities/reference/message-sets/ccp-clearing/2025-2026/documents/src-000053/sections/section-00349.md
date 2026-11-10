---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.14 Party Identification", "12.1.14.1 PartyIdentificationAndAccount228", "12.1.14.1.1 PartyIdentification <PtyId>"]
file_pages: [442]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.14.1.1 PartyIdentification <PtyId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 442 to 442.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 442

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 442
   AccountIdentification <AcctId> [0..1] Text 442
   ProcessingIdentification <PrcgId> [0..1] Text 442
   ProcessingDate <PrcgDt> [0..1] ± 442
   SubAccountDetails <SubAcctDtls> [0..1]  443
     Identification <Id> [1..1] ± 443
     Name <Nm> [0..1] Text 443
     Characteristic <Chrtc> [0..1] Text 443
   ContactPerson <CtctPrsn> [0..1] ± 444
12.1.14.1.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
PartyIdentification <PtyId> contains one of the following elements (see PartyIdentification254Choice
on page 455 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet   'C3 455
Or   ProprietaryIdentification <PrtryId> [1..1] ± 456
Or}   NameAndAddress <NmAndAdr> [1..1]  456
     Name <Nm> [1..1] Text 456
     Address <Adr> [1..1] ± 456
12.1.14.1.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: Max35Text on page 493
12.1.14.1.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Specifies the reference of the transaction at the party identified in the sequence.
Datatype: Max35Text on page 493
12.1.14.1.4  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date and optionally the time, at which this transaction was processed by the party identified
in this sequence.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 442
```

