---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks", "22.4.7 SubBalance <SubBal>", "22.4.7.2 Movement <Mvmnt>", "22.4.7.2.14 Linkages <Lnkgs>", "22.4.7.2.14.3 Reference <Ref>", "22.4.7.2.14.3.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>"]
file_pages: [546]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4.7.2.14.3.1 SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 546 to 546.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 546

```text
Reference <Ref> contains one of the following References34Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 546
Or   IntraPositionMovementIdentification
<IntraPosMvmntId>
[1..1] Text 546
Or   IntraBalanceMovementIdentification
<IntraBalMvmntId>
[1..1] Text 546
Or   AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 546
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 546
Or   PoolIdentification <PoolId> [1..1] Text 547
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 547
22.4.7.2.14.3.1  SecuritiesSettlementTransactionIdentification <SctiesSttlmTxId>
Presence: [1..1]
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 3328
22.4.7.2.14.3.2  IntraPositionMovementIdentification <IntraPosMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-position movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 3328
22.4.7.2.14.3.3  IntraBalanceMovementIdentification <IntraBalMvmntId>
Presence: [1..1]
Definition: Unambiguous identification of the intra-balance movement transaction as known by the
account owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 3328
22.4.7.2.14.3.4  AccountServicerTransactionIdentification <AcctSvcrTxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the account servicer.
Datatype: "Max35Text" on page 3328
22.4.7.2.14.3.5  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 546 August 2026
```

