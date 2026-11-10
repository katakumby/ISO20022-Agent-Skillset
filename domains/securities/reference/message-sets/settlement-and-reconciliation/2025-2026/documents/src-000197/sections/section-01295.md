---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.25 Settlement Chain", "35.1.25.1 SettlementParties125", "35.1.25.1.1 Depository <Dpstry>"]
file_pages: [1752]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.25.1.1 Depository <Dpstry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1752 to 1752.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1752

```text
35.1.25.1.1  Depository <Dpstry>
Presence: [0..1]
Definition: First party in the settlement chain. In a plain vanilla settlement, it is the Central Securities
Depository where the counterparty requests to receive the financial instrument or from where the
counterparty delivers the financial instruments.
Depository <Dpstry> contains the following elements (see "PartyIdentification314" on page 1661 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1661
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1662
Or     NameAndAddress <NmAndAdr> [1..1] ± 1662
Or     Country <Ctry> [1..1] CodeSet C7 1662
Or}     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1662
   LEI <LEI> [0..1] IdentifierSet 1662
   ProcessingIdentification <PrcgId> [0..1] Text 1663
35.1.25.1.2  Party1 <Pty1>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the depository.
Impacted by: C18 "SafekeepingAccountOrBlockChainAddress1Rule", C20
"SafekeepingAccountOrBlockChainAddress2Rule"
Party1 <Pty1> contains the following elements (see "PartyIdentificationAndAccount195" on page 1681
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1681
   LEI <LEI> [0..1] IdentifierSet 1681
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1682
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1682
   ProcessingIdentification <PrcgId> [0..1] Text 1682
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1752 March 2026
```

