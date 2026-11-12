---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.8 StandingSettlementInstructionDetails <StgSttlmInstrDtls>", "29.4.8.3 Vendor <Vndr>"]
file_pages: [1034, 1035]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.8.3 Vendor <Vndr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1034 to 1035.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1034

```text
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
29.4.8.3  Vendor <Vndr>
Presence: [0..1]
Definition: Vendor of the settlement standing instruction database that is to be consulted.
Vendor <Vndr> contains the following elements (see "PartyIdentification136" on page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
29.4.8.4  OtherDeliveringSettlementParties <OthrDlvrgSttlmPties>
Presence: [0..1]
Definition: Delivering parties, other than the seller, needed for deriving the standing settlement
instruction (for example, depository) or provided for information purposes (for example, instructing party
settlement chain).
Impacted by: C9 "BookTransferGuideline", C17 "DepositoryGuideline", C31 "Party2PresenceRule", C32
"Party3PresenceRule", C33 "Party4PresenceRule", C34 "Party5PresenceRule", C51
"SettlementChainGuideline"
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
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1034 March 2026
```

## File page 1035

```text
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
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1035 March 2026
```

