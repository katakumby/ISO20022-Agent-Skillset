---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.8 PartyIdentification136", "35.1.18.8.1 Identification <Id>"]
file_pages: [1672]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.8.1 Identification <Id>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1672 to 1672.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1672

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
35.1.18.8.1  Identification <Id>
Presence: [1..1]
Definition: Unique identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 1689 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1689
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1689
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1690
35.1.18.8.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 2187
35.1.18.9  PartyIdentificationAndAccount197
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1673
   LEI <LEI> [0..1] IdentifierSet 1673
   AlternateIdentification <AltrnId> [0..1] ± 1673
   Nationality <Ntlty> [0..1] CodeSet C7 1674
   SafekeepingAccount <SfkpgAcct> [0..1] Text 1674
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 1674
   ProcessingIdentification <PrcgId> [0..1] Text 1674
   AdditionalInformation <AddtlInf> [0..1] ± C5 1674
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1672 March 2026
```

