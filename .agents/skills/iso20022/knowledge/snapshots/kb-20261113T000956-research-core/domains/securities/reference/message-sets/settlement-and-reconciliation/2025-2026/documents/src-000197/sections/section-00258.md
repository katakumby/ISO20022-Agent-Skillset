---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.24 QuantityAndAccountDetails <QtyAndAcctDtls>"]
file_pages: [389]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.24 QuantityAndAccountDetails <QtyAndAcctDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 389 to 389.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 389

```text
TypeOfPrice <TpOfPric> contains one of the following elements (see "TypeOfPrice29Choice" on
page 1711 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1711
Or}   Proprietary <Prtry> [1..1] ± 1711
10.4.6.24  QuantityAndAccountDetails <QtyAndAcctDtls>
Presence: [1..1]
Definition: Details about the financial instrument quantity and the account involved in the transaction.
Impacted by: C15 "DenominationRule", C41 "SafekeepingPlaceRule"
QuantityAndAccountDetails <QtyAndAcctDtls> contains the following elements (see
"QuantityAndAccount114" on page 1718 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± C12 1719
   DenominationChoice <DnmtnChc> [0..1] Text 1719
   CashAccount <CshAcct> [0..1] ± 1719
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1720
   SafekeepingPlace <SfkpgPlc> [0..1] ± C33 1720
Constraints
• DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is used, it
must not contain information that can be provided in a structured field.
• SafekeepingPlaceRule
The SafekeepingPlace functionality in the settlement instructions is only to be used for global
custodians that allow their clients to specify where the securities are to be held, for example, in an
ICSD account versus an account at the local CSD.
10.4.6.25  SecuritiesFinancingDetails <SctiesFincgDtls>
Presence: [0..1]
Definition: Details of the closing of the securities financing transaction.
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 389 March 2026
```

