---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.20 Party Identification", "7.1.20.26 PartyIdentificationAndAccount154", "7.1.20.26.2 SafekeepingAccount <SfkpgAcct>"]
file_pages: [477]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.20.26.2 SafekeepingAccount <SfkpgAcct>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 477 to 477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 477

```text
Identification <Id> contains one of the following elements (see "PartyIdentification245Choice" on
page 464 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 464
Or   ProprietaryIdentification <PrtryId> [1..1] ± 464
Or}   NameAndAddress <NmAndAdr> [1..1] ± 464
7.1.20.26.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Datatype: "Max35Text" on page 669
7.1.20.26.3  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account in which cash is maintained.
CashAccount <CshAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 223 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 223
Or}   Proprietary <Prtry> [1..1] Text 223
7.1.20.26.4  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Reference meaningful to the party identified.
Datatype: "Max35Text" on page 669
7.1.20.26.5  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information regarding the party.
Impacted by: C2 "AdditonalDetailsGuideline"
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 477 February 2025
```

