---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.12 ReceivingSettlementParties <RcvgSttlmPties>", "22.4.13.1 Debtor <Dbtr>"]
file_pages: [757]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.13.1 Debtor <Dbtr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 757 to 757.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 757

```text
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
• SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
22.4.13 CashParties <CshPties>
Presence: [0..1]
Definition: Specifies cash parties in the framework of a corporate action event.
CashParties <CshPties> contains the following CashParties42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Debtor <Dbtr> [0..1] ± 757
   DebtorAgent <DbtrAgt> [0..1] ± 758
   Creditor <Cdtr> [0..1] ± 758
   CreditorAgent <CdtrAgt> [0..1] ± 759
22.4.13.1  Debtor <Dbtr>
Presence: [0..1]
Definition: Party that owes an amount of money to the (ultimate) creditor.
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 757 March 2026
```

