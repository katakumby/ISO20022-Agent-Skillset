---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["20 sese.026.001.12 SecuritiesSettlementTransactionReversalAdviceV12", "20.4 Message Building Blocks", "20.4.8 SettlementParameters <SttlmParams>", "20.4.9.2 Counterparty <CtrPty>"]
file_pages: [685, 686]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.026.001.12"]
---

# 20.4.9.2 Counterparty <CtrPty>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 685 to 686.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 685

```text
SettlementStandingInstructionDatabase <SttlmStgInstrDB> contains one of the following elements
(see "SettlementStandingInstructionDatabase4Choice" on page 1583 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1583
Or}   Proprietary <Prtry> [1..1] ± 1583
20.4.9.2  Counterparty <CtrPty>
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
20.4.9.3  Vendor <Vndr>
Presence: [0..1]
Definition: Vendor of the settlement standing instruction database that is to be consulted.
Vendor <Vndr> contains the following elements (see "PartyIdentification136" on page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
20.4.9.4  OtherDeliveringSettlementParties <OthrDlvrgSttlmPties>
Presence: [0..1]
Definition: Delivering parties, other than the seller, needed for deriving the standing settlement
instruction (for example, depository) or provided for information purposes (for example, instructing party
settlement chain).
Impacted by: C9 "BookTransferGuideline", C17 "DepositoryGuideline", C33 "Party2PresenceRule", C34
"Party3PresenceRule", C35 "Party4PresenceRule", C36 "Party5PresenceRule", C55
"SettlementChainGuideline"
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 685 March 2026
```

## File page 686

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
Approved by the Securities SEG on 27 January 2026 sese.026.001.12
SecuritiesSettlementTransactionReversalAdviceV12
Settlement And Reconciliation - Maintenance 2025 - 2026 686 March 2026
```

