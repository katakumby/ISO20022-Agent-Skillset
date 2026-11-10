---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.25 Settlement Chain", "35.1.25.5 SettlementParties128"]
file_pages: [1774, 1775]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.25.5 SettlementParties128

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1774 to 1775.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1774

```text
Party5 <Pty5> contains the following elements (see "PartyIdentificationAndAccount196" on page 1667
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1668
   LEI <LEI> [0..1] IdentifierSet 1668
   AlternateIdentification <AltrnId> [0..1] ± 1668
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1669
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1669
   ProcessingDate <PrcgDt> [0..1] ± 1669
   ProcessingIdentification <PrcgId> [0..1] Text 1669
   AdditionalInformation <AddtlInf> [0..1] ± C5 1669
Constraints
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
35.1.25.5  SettlementParties128
Definition: Chain of parties involved in the settlement of a transaction, including receipts and deliveries,
book transfers, treasury deals, or other activities, resulting in the movement of a security or amount of
money from one account to another.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1774 March 2026
```

## File page 1775

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1776
   Party1 <Pty1> [0..1] ± C29,
C31
1777
   Party2 <Pty2> [0..1] ± C29,
C31
1778
   Party3 <Pty3> [0..1] ± C29,
C31
1778
   Party4 <Pty4> [0..1] ± C29,
C31
1779
   Party5 <Pty5> [0..1] ± C29,
C31
1780
Constraints
• BookTransferGuideline
In the case of an own account internal transfer, own account external transfer, portfolio transfer and
in specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
Country code should be used for settlement taking place outside of an institution published in the
PSET's BIC list. This includes physical deliveries and investment funds not settling at a CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1775 March 2026
```

