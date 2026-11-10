---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.3 Modification <Mod>", "32.4.2.3.6 QuantityAndAccountDetails <QtyAndAcctDtls>", "32.4.2.3.6.1 SettlementQuantity <SttlmQty>"]
file_pages: [1272]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.3.6.1 SettlementQuantity <SttlmQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1272 to 1272.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1272

```text
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
32.4.2.3.6.1  SettlementQuantity <SttlmQty>
Presence: [0..1]
Definition: Total quantity of securities to be settled.
SettlementQuantity <SttlmQty> contains one of the following elements (see "Quantity51Choice" on
page 1725 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C12 1725
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 1726
32.4.2.3.6.2  DenominationChoice <DnmtnChc>
Presence: [0..1]
Definition: Denomination of the security to be received or delivered.
Datatype: "Max210Text" on page 2191
32.4.2.3.6.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
32.4.2.3.6.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1272 March 2026
```

