---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.20 Settlement Chain", "9.1.20.1 SettlementParties78", "9.1.20.1.1 Depository <Dpstry>"]
file_pages: [266]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.20.1.1 Depository <Dpstry>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 266 to 266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
9.1.20.1.1  Depository <Dpstry>
Presence: [0..1]
Definition: First party in the settlement chain. In a plain vanilla settlement, it is the Central Securities
Depository where the counterparty requests to receive the financial instrument or from where the
counterparty delivers the financial instruments.
Depository <Dpstry> contains the following elements (see "PartyIdentification148" on page 254 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  254
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C6 255
Or     NameAndAddress <NmAndAdr> [1..1] ± 255
Or}     Country <Ctry> [1..1] CodeSet C7 255
   LEI <LEI> [0..1] IdentifierSet 256
   ProcessingIdentification <PrcgId> [0..1] Text 256
9.1.20.1.2  Party1 <Pty1>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the depository.
Party1 <Pty1> contains the following elements (see "PartyIdentificationAndAccount170" on page 256
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 256
   LEI <LEI> [0..1] IdentifierSet 256
   SafekeepingAccount <SfkpgAcct> [0..1] ± 257
   ProcessingIdentification <PrcgId> [0..1] Text 257
9.1.20.1.3  Party2 <Pty2>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 1.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 266 September 2025
```

