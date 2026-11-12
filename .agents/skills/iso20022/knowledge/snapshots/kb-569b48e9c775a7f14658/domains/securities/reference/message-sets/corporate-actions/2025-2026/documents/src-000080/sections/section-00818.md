---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.1 CashParties43", "16.1.17.1.3 MarketClaimCounterparty <MktClmCtrPty>"]
file_pages: [1036]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.1.3 MarketClaimCounterparty <MktClmCtrPty>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1036 to 1036.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1036

```text
CreditorAgent <CdtrAgt> contains the following elements (see "PartyIdentificationAndAccount226" on
page 1050 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1050
{Or     BICFI <BICFI> [1..1] IdentifierSet C2 1051
Or     NameAndAddress <NmAndAdr> [1..1] ± 1051
Or}     ProprietaryIdentification <PrtryId> [1..1] ± 1051
   CashAccount <CshAcct> [0..1] ± 1052
   ProcessingIdentification <PrcgId> [0..1] Text 1052
   AlternateIdentification <AltrnId> [0..1] ± 1052
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
16.1.17.1.3  MarketClaimCounterparty <MktClmCtrPty>
Presence: [0..1]
Definition: Party that has reimbursed the account owner with funds to which they were legally entitled.
Impacted by: C5 "AdditionalInforrmationRule"
MarketClaimCounterparty <MktClmCtrPty> contains the following
PartyIdentificationAndAccount225 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1036
   CashAccount <CshAcct> [0..1] ± 1037
   ProcessingIdentification <PrcgId> [0..1] Text 1037
   AlternateIdentification <AltrnId> [0..1] ± 1037
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
16.1.17.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1036 February 2026
```

