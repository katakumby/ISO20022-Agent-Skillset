---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.2 Linkages <Lnkgs>", "19.4.7.1 SettledQuantity <SttldQty>"]
file_pages: [626]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.7.1 SettledQuantity <SttldQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 626 to 626.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 626

```text
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• SafekeepingPlaceGuideline
When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist between the
account servicer and the account owner, it is recommended to use the place of safekeeping field
following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and NCSD to
NCSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtICSD: an ICSD's BIC will be used for ICSD internal, ICSD/
local and ICSD to ICSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtLoaclCustodian: applicable, for instance, when the account
servicer is a global custodian and provides the account owner with a position reporting at global
custodian's agents' level. When instructing, the fund manager would therefore mention, as a place of
safekeeping, the BIC of the global custodian's agent on the market.
Absence of SafekeepingPlace means that:
• The SafekeepingPlace information is kept by the account servicer (SLA, account structure, ETC.)
and should not be provided by the account owner.
• The SafekeepingPlace is the counterparty's Depository. The transaction is therefore domestic (to
an NCSD) or internal to an ICSD.
For more details, see the relevant market practice document on www.smpg.info.
• SafekeepingPlaceRule
The SafekeepingPlace functionality in the settlement instructions is only to be used for global
custodians that allow their clients to specify where the securities are to be held, for example, in an
ICSD account versus an account at the local CSD.
19.4.7.1  SettledQuantity <SttldQty>
Presence: [1..1]
Definition: Quantity of financial instrument effectively settled.
SettledQuantity <SttldQty> contains one of the following elements (see "Quantity51Choice" on
page 1725 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1725
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1726
19.4.7.2  PreviouslySettledQuantity <PrevslySttldQty>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 626 March 2026
```

