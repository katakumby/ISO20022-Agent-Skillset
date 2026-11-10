---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.9 SubAccountDetails <SubAcctDtls>", "3.4.9.5 BalanceForSubAccount <BalForSubAcct>", "3.4.9.5.17 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "3.4.9.5.17.4 AggregateBalance <AggtBal>"]
file_pages: [127]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.9.5.17.4 AggregateBalance <AggtBal>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 127 to 127.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 127

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
3.4.9.5.17.4  AggregateBalance <AggtBal>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
AggregateBalance <AggtBal> contains the following elements (see "Balance17" on page 1431 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [1..1] CodeSet 1432
   Quantity <Qty> [1..1] ± 1432
3.4.9.5.17.5  PriceDetails <PricDtls>
Presence: [1..*]
Definition: Price of the financial instrument in one or more currencies.
Impacted by: C41 "ValueRule"
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 127 March 2026
```

