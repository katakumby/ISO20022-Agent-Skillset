---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.9 SubAccountDetails <SubAcctDtls>", "2.4.9.5 BalanceForSubAccount <BalForSubAcct>", "2.4.9.5.18 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "2.4.9.5.18.4 AggregateBalance <AggtBal>"]
file_pages: [70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.9.5.18.4 AggregateBalance <AggtBal>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 70 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
Pledgee <Pldgee> contains the following elements (see "Pledgee3" on page 1675 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PledgeeTypeAndIdentification <PldgeeTpAndId> [0..1]  1675
{Or     TypeAndIdentification <TpAndId> [1..1]  1676
       Identification <Id> [1..1] IdentifierSet C5 1676
       PledgeeType <PldgeeTp> [1..1] CodeSet 1676
Or     Identification <Id> [1..1]  1677
       Identification <Id> [0..1] Text 1677
       PledgeeType <PldgeeTp> [1..1] CodeSet 1677
Or}     Proprietary <Prtry> [1..1] ± 1677
   LEI <LEI> [0..1] IdentifierSet 1678
Constraints
• PledgeeTypeAndIdentificationOrLEIRule
PledgeeTypeAndIdentification must be present or LEI must be present.
Following Must be True
    /PledgeeTypeAndIdentification Must be present
 Or    /LEI Must be present
2.4.9.5.18.4  AggregateBalance <AggtBal>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
AggregateBalance <AggtBal> contains the following elements (see "Balance17" on page 1431 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1432
   Quantity <Qty> [1..1] ± 1432
2.4.9.5.18.5  AvailableBalance <AvlblBal>
Presence: [0..1]
Definition: Total quantity of financial instruments of the balance that is available.
AvailableBalance <AvlblBal> contains the following elements (see "Balance18" on page 1424 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 1424
   Quantity <Qty> [1..1] ± 1424
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 70 March 2026
```

