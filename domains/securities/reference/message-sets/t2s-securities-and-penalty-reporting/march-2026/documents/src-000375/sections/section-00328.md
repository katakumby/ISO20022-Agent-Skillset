---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Party Identification", "7.1.19.5 PartyIdentificationAndAccount197", "7.1.19.5.1 Identification <Id>"]
file_pages: [415]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.5.1 Identification <Id>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 415 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 415

```text
Constraints
• IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
7.1.19.5.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 433 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 433
Or   ProprietaryIdentification <PrtryId> [1..1] ± 433
Or}   NameAndAddress <NmAndAdr> [1..1] ± 433
7.1.19.5.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 552
7.1.19.5.3  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 415 March 2026
```

