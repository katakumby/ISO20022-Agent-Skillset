---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.1 Addition <Addtn>", "32.4.2.1.7 StandingSettlementInstructionDetails <StgSttlmInstrDtls>", "32.4.2.1.7.2 Counterparty <CtrPty>"]
file_pages: [1197, 1198]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.1.7.2 Counterparty <CtrPty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1197 to 1198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1197

```text
Definition: Specifies what settlement standing instruction database is to be used to derive the
settlement parties involved in the transaction.
SettlementStandingInstructionDatabase <SttlmStgInstrDB> contains one of the following elements
(see "SettlementStandingInstructionDatabase4Choice" on page 1583 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1583
Or}   Proprietary <Prtry> [1..1] ± 1583
32.4.2.1.7.2  Counterparty <CtrPty>
Presence: [1..1]
Definition: Identification of the buyer or seller in a standing settlement instruction enabling to derive the
Standing Settlement Instruction.
Counterparty <CtrPty> contains one of the following elements (see "Counterparty15Choice" on
page 1665 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Seller <Sellr> [1..1] ± C29,
C31
1665
Or}   Buyer <Buyr> [1..1] ± C29,
C31
1666
32.4.2.1.7.3  Vendor <Vndr>
Presence: [0..1]
Definition: Vendor of the settlement standing instruction database that is to be consulted.
Vendor <Vndr> contains the following elements (see "PartyIdentification136" on page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
32.4.2.1.7.4  OtherDeliveringSettlementParties <OthrDlvrgSttlmPties>
Presence: [0..1]
Definition: Delivering parties, other than the seller, needed for deriving the standing settlement
instruction (for example, depository) or provided for information purposes (for example, instructing party
settlement chain).
Impacted by: C10 "BookTransferGuideline", C20 "DepositoryGuideline", C42 "Party2PresenceRule",
C44 "Party3PresenceRule", C47 "Party4PresenceRule", C50 "Party5PresenceRule", C75
"SettlementChainGuideline"
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1197 March 2026
```

## File page 1198

```text
OtherDeliveringSettlementParties <OthrDlvrgSttlmPties> contains the following elements (see
"SettlementParties126" on page 1767 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1769
   Party1 <Pty1> [0..1] ± C29,
C31
1770
   Party2 <Pty2> [0..1] ± C29,
C31
1771
   Party3 <Pty3> [0..1] ± C29,
C31
1771
   Party4 <Pty4> [0..1] ± C29,
C31
1772
   Party5 <Pty5> [0..1] ± C29,
C31
1773
Constraints
• BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC is to be used.
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
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1198 March 2026
```

