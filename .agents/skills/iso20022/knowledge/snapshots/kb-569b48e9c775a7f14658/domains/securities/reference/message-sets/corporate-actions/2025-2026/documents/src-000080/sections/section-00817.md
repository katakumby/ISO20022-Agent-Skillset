---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.17 Party Identification", "16.1.17.1 CashParties43", "16.1.17.1.1 Creditor <Cdtr>", "16.1.17.1.1.2 CashAccount <CshAcct>"]
file_pages: [1035]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.17.1.1.2 CashAccount <CshAcct>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1035 to 1035.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1035

```text
Definition: Identification of a party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 1045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1045
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1046
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1046
16.1.17.1.1.2  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account in which cash is maintained.
CashAccount <CshAcct> contains one of the following elements (see
"CashAccountIdentification9Choice" on page 829 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 829
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 829
Or}   Proprietary <Prtry> [1..1] Text 830
16.1.17.1.1.3  ProcessingIdentification <PrcgId>
Presence: [0..1]
Definition: Reference meaningful to the party identified.
Datatype: "Max35Text" on page 1251
16.1.17.1.1.4  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 1046 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1046
   Country <Ctry> [1..1] CodeSet C3 1047
   AlternateIdentification <AltrnId> [1..1] Text 1047
16.1.17.1.2  CreditorAgent <CdtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the creditor.
Impacted by: C6 "AdditionalInforrmationRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1035 February 2026
```

