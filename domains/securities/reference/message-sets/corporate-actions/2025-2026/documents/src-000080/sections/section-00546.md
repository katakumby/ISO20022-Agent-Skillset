---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.3 AccountsDetails <AcctsDtls>", "11.4.3.2 AccountsList <AcctsList>", "11.4.3.2.2 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [712]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.3.2.2 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 712 to 712.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 712

```text
11.4.3.2.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Datatype: "Max140Text" on page 1249
11.4.3.2.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 1037 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1038
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1038
11.4.3.2.4  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Location where the financial instruments are/will be safekept.
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormat42Choice" on page 1130 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  1130
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1130
     Identification <Id> [0..1] Text 1131
Or   Country <Ctry> [1..1] CodeSet C3 1131
Or   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1131
Or   TypeAndIdentification <TpAndId> [1..1]  1131
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 1132
     Identification <Id> [1..1] IdentifierSet C1 1132
Or}   Proprietary <Prtry> [1..1] ± 1132
11.4.4 CorporateActionDetails <CorpActnDtls>
Presence: [0..1]
Definition: Information about the corporate action event.
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 712 February 2026
```

