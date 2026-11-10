---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.28 Settlement Chain", "82.1.28.1 SettlementParties78", "82.1.28.1.2 Party1 <Pty1>"]
file_pages: [3116]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.28.1.2 Party1 <Pty1>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3116 to 3116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3116

```text
Definition: First party in the settlement chain. In a plain vanilla settlement, it is the Central Securities
Depository where the counterparty requests to receive the financial instrument or from where the
counterparty delivers the financial instruments.
Depository <Dpstry> contains the following elements (see "PartyIdentification148" on page 3066 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  3066
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3066
Or     NameAndAddress <NmAndAdr> [1..1] ± 3067
Or}     Country <Ctry> [1..1] CodeSet C3 3067
   LEI <LEI> [0..1] IdentifierSet 3067
   ProcessingIdentification <PrcgId> [0..1] Text 3067
82.1.28.1.2  Party1 <Pty1>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the depository.
Party1 <Pty1> contains the following elements (see "PartyIdentificationAndAccount170" on page 3077
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3077
   LEI <LEI> [0..1] IdentifierSet 3077
   SafekeepingAccount <SfkpgAcct> [0..1] ± 3077
   ProcessingIdentification <PrcgId> [0..1] Text 3078
82.1.28.1.3  Party2 <Pty2>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 1.
Party2 <Pty2> contains the following elements (see "PartyIdentificationAndAccount170" on page 3077
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3077
   LEI <LEI> [0..1] IdentifierSet 3077
   SafekeepingAccount <SfkpgAcct> [0..1] ± 3077
   ProcessingIdentification <PrcgId> [0..1] Text 3078
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3116 August 2026
```

