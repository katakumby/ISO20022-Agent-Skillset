---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.2 NewCriteria <NewCrit>", "30.4.2.2.2.2 SearchCriteria <SchCrit>", "30.4.2.2.2.2.9 AssociatedPoolAccount <AssoctdPoolAcct>"]
file_pages: [701]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.2.2.9 AssociatedPoolAccount <AssoctdPoolAcct>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 701 to 701.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 701

```text
30.4.2.2.2.2.9  AssociatedPoolAccount <AssoctdPoolAcct>
Presence: [0..1]
Definition: Liquidity transfer origin or destination account within the pool of accounts under management
of the requestor.
AssociatedPoolAccount <AssoctdPoolAcct> contains one of the following elements (see
"AccountIdentification4Choice" on page 787 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
30.4.2.2.2.2.10  LinkSetIdentification <LkSetId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the link set in which the standing order is
defined. The link set is a collection of standing order defined in a specific sequence.
Datatype: "Max35Text" on page 889
30.4.2.2.2.2.11  LinkSetOrderIdentification <LkSetOrdrId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify liquidity transfer standing order within the link
set.
Datatype: "Max35Text" on page 889
30.4.2.2.2.2.12  LinkSetOrderSequence <LkSetOrdrSeq>
Presence: [0..1]
Definition: Specifies the sequence in which the system will execute the liquidity transfers standing order
within the link set when additional liquidity is required.
Datatype: "Number" on page 886
30.4.2.2.2.2.13  ZeroSweepIndicator <ZeroSweepInd>
Presence: [0..1]
Definition: Indicates whether the query shall return all liquidity transfer standing orders defined as zero
sweeping orders.
When the indicator is set to true, the liquidity transfer standing order will transfer all amount of money
out of the account so the resulting balance is zero.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 886):
• Meaning When True: True
• Meaning When False: False
30.4.2.2.2.3  ReturnCriteria <RtrCrit>
Presence: [0..1]
Definition: Defines the expected standing order report.
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 701 February 2025
```

