---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.16 RedemptionLegDetails <RedLegDtls>", "53.4.5.16.10 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "53.4.5.16.10.7 ReceivingSideDetails <RcvgSdDtls>", "53.4.5.16.10.7.4 ReceivingAgentDetails <RcvgAgtDtls>"]
file_pages: [3599]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.16.10.7.4 ReceivingAgentDetails <RcvgAgtDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3599 to 3599.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3599

```text
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
53.4.5.16.10.7.4  ReceivingAgentDetails <RcvgAgtDtls>
Presence: [1..1]
Definition: Party that receives securities from the delivering agent at the place of settlement, for
example, central securities depository.
ReceivingAgentDetails <RcvgAgtDtls> contains the following PartyIdentificationAndAccount235
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 3599
   AccountIdentification <AcctId> [0..1] Text 3599
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 3599
53.4.5.16.10.7.4.1  PartyIdentification <PtyId>
Presence: [1..1]
Definition: Party that legally owns the account.
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.16.10.7.4.2  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Identification of the account owned by the party.
Datatype: "Max35Text" on page 5403
53.4.5.16.10.7.4.3  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3599 May 2026
```

