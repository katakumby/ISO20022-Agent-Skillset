---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.4 PartyIdentification136", "7.1.19.4.1 Identification <Id>"]
file_pages: [414]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.4.1 Identification <Id>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 414 to 414.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 414

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
7.1.19.4.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 433 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 433
Or   ProprietaryIdentification <PrtryId> [1..1] ± 433
Or}   NameAndAddress <NmAndAdr> [1..1] ± 433
7.1.19.4.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 552
7.1.19.5  PartyIdentificationAndAccount197
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 415
   LEI <LEI> [0..1] IdentifierSet 415
   AlternateIdentification <AltrnId> [0..1] ± 415
   Nationality <Ntlty> [0..1] CodeSet C3 416
   SafekeepingAccount <SfkpgAcct> [0..1] Text 416
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 416
   ProcessingIdentification <PrcgId> [0..1] Text 416
   AdditionalInformation <AddtlInf> [0..1] ± C1 416
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 414 March 2026
```

